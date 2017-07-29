
import csv
from utils import *
import numpy as np
import os
import timeit
from sentiment_db import SentDB

import sentiment_service

sent_instance = sentiment_service

class SentimentGenerator:
    current_dir = os.getcwd()
    UPLOAD_DIR = current_dir + "/files/"
    stdb = SentDB()

    def process_bulk_files(self, filename):
        errors = []
        try:
            print("about to open file = "+self.UPLOAD_DIR+filename)
            generated_sentiments = []
            with open(self.UPLOAD_DIR+filename, 'r') as f:
                csvfile = csv.reader(f)
                firstrow = next(csvfile, None)  # skip header
                # firstrow = csvfile[0]
                print("first row text = "+firstrow[2])
                if firstrow[0] != "GENERATED" or firstrow[1] != "ACTUAL" or firstrow[2] != "TEXT":
                    errors.append("Invalid excel template! Please use a valid template")

                if len(errors) > 0:
                    f.close()
                    os.remove(self.UPLOAD_DIR+filename)
                    return errors

                deviations = 0
                total_count = 0
                for row in csvfile:
                    if row[2] == 'TEXT':
                        continue
                    sentiment_resp = self.runSentiment(row[2], row[3], reference_id=filename)
                    # print(sentiment_resp['sentiment'])
                    row[0] = sentiment_resp['sentiment']
                    #
                    # keep a count of deviations if the sentiment does not matches.
                    #
                    deviations += 0 if (row[0] == row[1]) else 1
                    total_count += 1
                    generated_sentiments.append(row)
                    # csvfile.writerow(row)
                # finally close file
                f.close()
            #
            # calculate percent error
            #
            accuracy_percentage = ((total_count - deviations) / total_count) * 100

            print("writing csv file")
            with open(self.UPLOAD_DIR+filename, 'w', newline='') as f:
                writer = csv.writer(f)
                #
                # write down the stats
                #
                stats_row = ["TOTAL = ", str(total_count)]
                writer.writerow(stats_row)
                stats_row = ["DEVIATIONS = ", str(deviations)]
                writer.writerow(stats_row)
                stats_row = [" ACCURACY = ",str(accuracy_percentage) + "%"]
                writer.writerow(stats_row)
                header_row = ["GENERATED", "ACTUAL", "TEXT", "PROCESSED_TERMS"]
                writer.writerow(header_row)
                for row in generated_sentiments:
                    writer.writerow(row)
                f.close()

            new_filename = filename.replace("IN-PROGRESS", "COMPLETE")
            os.rename(self.UPLOAD_DIR+filename, self.UPLOAD_DIR+new_filename)
            print("renamed the file to "+new_filename)
            return None
        except Exception as e:
            print(str(e))
            new_filename = filename.replace("IN-PROGRESS", "ERROR")
            os.rename(self.UPLOAD_DIR + filename, self.UPLOAD_DIR + new_filename)
            errors.append("some error occurred, please check logs")
            return errors

    def runSentiment(self, text, pt, user="", reference_id=""):
        start_time = timeit.default_timer()
        status = "SUCCESS"

        sentiment_score = sent_instance.get_score(text, pt)

        if sentiment_score == "1":
            sentiment = "POSITIVE"
        elif sentiment_score == "-1":
            sentiment = "NEGATIVE"
        else:
            sentiment = "NEUTRAL"

        time = (timeit.default_timer() - start_time) * 1000
        result_json = {
            'status': status,
            'user': user,
            'score': sentiment_score,
            'sentiment': sentiment,
            'text': text,
            'time_taken': str(round(time, 0)) + ' ms',
            'reference_id': reference_id,
            'model_ver': self.MODEL_VERSION
            'time': time
            'type': 'bulk request'
        }
        result_json['_id'] = self.stdb.save_record(result_json)

        return result_json