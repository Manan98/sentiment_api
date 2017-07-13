==========
Data Model
==========
-------
Summary
-------

+ **OrganizationInfo**
  
  +----------------------------------+-------------------------------------------------------+  
  | Fields                           | Description                                           | 
  |                                  |                                                       | 
  +==================================+=======================================================+
  | **entityType**                   |**string**                                             |
  |                                  |                                                       |
  |                                  | The type of work the organization does.               |
  |                                  |                                                       |
  |                                  |Sample: *cretecarrier*                                 |
  +----------------------------------+-------------------------------------------------------+
  | **hoursOfOperation**             |**string**                                             |
  |                                  |                                                       |
  |                                  | The duration for which the organization works for on  |
  |                                  |                                                       |
  |                                  | every day of the week.                                |
  |                                  |Sample: *Mon - 10:00 AM - 10:00 PM*                    |
  +----------------------------------+-------------------------------------------------------+
  | **industry**                     |**string**                                             |
  |                                  |                                                       |
  |                                  | The type of industry the organization works under.    |
  |                                  |                                                       |
  |                                  |Sample: *Hospitality*                                  |
  +----------------------------------+-------------------------------------------------------+
  | **orgName**                      |**string**                                             |
  |                                  |                                                       |
  |                                  | The unofficial name of the organization.              |
  |                                  |                                                       |
  |                                  |Sample: *Ontario Medical Association*                  |
  +----------------------------------+-------------------------------------------------------+
  | **legalName**                    |**string**                                             |
  |                                  |                                                       |
  |                                  | Legal name of the organization that was registered    |
  |                                  |                                                       |
  |                                  | with the government.                                  |
  |                                  |                                                       |
  |                                  |Sample: *Church Street Automotive LLC*                 | 
  +----------------------------------+-------------------------------------------------------+
  | **dbaNames**                     |**string**                                             |
  |                                  |                                                       |
  |                                  | The business name that is different from the owner's  |
  |                                  |                                                       |
  |                                  | name or the registered name of the corporation.       |
  |                                  |                                                       |
  |                                  |Sample: *MNO Consulting*                               |
  +----------------------------------+-------------------------------------------------------+
  | **dotNumber**                    |**string**                                             |
  |                                  |                                                       |
  |                                  | The companies USDOT number registered with the FMCSA  |
  |                                  |                                                       |
  |                                  | which is required to operate commercial vehicles.     |
  |                                  |                                                       |
  |                                  |Sample: *1948674*                                      |
  +----------------------------------+-------------------------------------------------------+
  | **dunsNumbers**                  |**string**                                             |
  |                                  |                                                       |
  |                                  | The 9 digit DUNS number is registered with the        |
  |                                  |                                                       |
  |                                  | federal government to uniquely identifies each        |
  |                                  |                                                       |
  |                                  | physical location of business.                        |
  |                                  |                                                       |
  |                                  |Sample: *008016958*                                    |
  +----------------------------------+-------------------------------------------------------+
  | **mcmxffNumbers**                |**string**                                             |
  |                                  |                                                       |
  |                                  | A 6 character MC/MX number that authorizes a carrier  |
  |                                  |                                                       |
  |                                  | to transport regulated commodities for hire in        |
  |                                  |                                                       |
  |                                  | interstate commerce.                                  |
  |                                  |                                                       |
  |                                  |Sample: *MC-126118*                                    |
  +----------------------------------+-------------------------------------------------------+
  | **stateCarrierIdNumber**         |**string**                                             |
  |                                  |                                                       |
  |                                  | The carrier id number is registered with the state    |
  |                                  |                                                       |
  |                                  | government.                                           |
  |                                  |                                                       |
  |                                  |Sample: *CA 333071*                                    |
  +----------------------------------+-------------------------------------------------------+
  | **annualSales**                  |**string**                                             |
  |                                  |                                                       |
  |                                  | The annual sales price of the organization.           |
  |                                  |                                                       |
  |                                  |Sample: *$0.11mn*                                      |
  +----------------------------------+-------------------------------------------------------+
  | **actualSalesVolume**            |**string**                                             |
  |                                  |                                                       |
  |                                  | The total volume of products sold by the organization.|
  +----------------------------------+-------------------------------------------------------+
  | **buissnessStatus**              |**string**                                             |
  |                                  |                                                       |
  |                                  | It states what the companies are authorized to do or  |
  |                                  |                                                       |
  |                                  | own.                                                  |
  |                                  |                                                       |
  |                                  |Sample: *AUTHORIZED FOR Property*                      |
  +----------------------------------+-------------------------------------------------------+
  | **buissnessStartDate**           |**string**                                             |
  |                                  |                                                       |
  |                                  | The year when the company was started.                |
  |                                  |                                                       |
  |                                  |Sample: *1966*                                         |
  +----------------------------------+-------------------------------------------------------+
  | **buissnessCategory**            |**string**                                             |
  |                                  |                                                       |
  |                                  | The type of sector or industry the company falls      |
  |                                  |                                                       |
  |                                  | under.                                                |
  |                                  |                                                       |
  |                                  |Sample: *Local Trucking*                               |
  +----------------------------------+-------------------------------------------------------+
  | **numOfEmployees**               |**string**                                             |
  |                                  |                                                       |
  |                                  | The number of people employed in that office.         |
  |                                  |                                                       |
  |                                  |Sample: *225*                                          |
  +----------------------------------+-------------------------------------------------------+
  | **website**                      |**string**                                             |
  |                                  |                                                       |
  |                                  | The official company website url.                     |
  |                                  |                                                       |
  |                                  |Sample: *http://www.oma.org*                           |
  +----------------------------------+-------------------------------------------------------+
  | **phoneNum**                     |**string**                                             |
  |                                  |                                                       |
  |                                  | The primary contact number for the organization       |
  |                                  |                                                       |
  |                                  | with the international calling code.                  |
  |                                  |                                                       |
  |                                  |Sample: *+1 812-234-8030*                              |
  +----------------------------------+-------------------------------------------------------+
  | **faxNum**                       |**string**                                             |
  |                                  |                                                       |
  |                                  | A fax number to which to send in scanned documents.   |
  |                                  |                                                       |
  |                                  |Sample: *402-479-2073*                                 |
  +----------------------------------+-------------------------------------------------------+
  | **empSizeRange**                 |**string**                                             |
  |                                  |                                                       |
  |                                  | The size range of the employees working in the        |
  |                                  |                                                       |
  |                                  | organization.                                         |
  |                                  |                                                       |
  |                                  |Sample: *100 to 250*                                   |
  +----------------------------------+-------------------------------------------------------+
  | **primarySic**                   |**string**                                             |
  |                                  |                                                       |
  |                                  | The 4 digit SIC code used to categorize business      |
  |                                  |                                                       |
  |                                  | activities based on its primary activity.             |
  |                                  |                                                       |
  |                                  |Sample: *3571*                                         |
  +----------------------------------+-------------------------------------------------------+
  | **primarySicDesc**               |**string**                                             |
  |                                  |                                                       |
  |                                  | The description of the business category illustrated  |
  |                                  |                                                       |
  |                                  | by the primary SIC code.                              |
  |                                  |                                                       |
  |                                  |Sample: *Electronic Computers*                         |
  +----------------------------------+-------------------------------------------------------+
  | **secondarySic1**                |**string**                                             |
  |                                  |                                                       |
  |                                  | The 4 digit SIC code used to categorize businesses    |
  |                                  |                                                       |
  |                                  | based on activities other than its primary activity.  |
  |                                  |                                                       |
  |                                  |Sample: *7361*                                         |
  +----------------------------------+-------------------------------------------------------+
  | **secondarySic1Desc**            |**string**                                             |
  |                                  |                                                       |
  |                                  | The description of the business category illustrated  |
  |                                  |                                                       |
  |                                  | by the secondary SIC code.                            |
  |                                  |                                                       |
  |                                  |Sample: *Employment Agencies*                          |
  +----------------------------------+-------------------------------------------------------+
  | **secondarySic2**                |**string**                                             |
  |                                  |                                                       |
  |                                  | The 4 digit SIC code used to categorize businesses    |
  |                                  |                                                       |
  |                                  | based on activities other than its primary and        |
  |                                  |                                                       |
  |                                  | secondary activity.                                   |
  |                                  |                                                       |
  |                                  |Sample: *7372*                                         |
  +----------------------------------+-------------------------------------------------------+
  | **secondarySic2Desc**            |**string**                                             |
  |                                  |                                                       |
  |                                  | The description of the business category illustrated  |
  |                                  |                                                       |
  |                                  | by the tertiary SIC code.                             |
  |                                  |                                                       |
  |                                  |Sample: *Prepackaged Software*                         |
  +----------------------------------+-------------------------------------------------------+
  | **creditAlphaScore**             |**string**                                             |
  |                                  |                                                       |
  |                                  | An indicator of the potential of the company stock    |
  |                                  |                                                       |
  |                                  | which ranges from 0 to 200.                           |
  |                                  |                                                       |
  |                                  |Sample: *158*                                          |
  +----------------------------------+-------------------------------------------------------+
  | **creditNumericScore**           |**string**                                             |
  |                                  |                                                       |
  |                                  | A number that depicts the company's credit worthiness |
  |                                  |                                                       |
  |                                  | which ranges from 300 to 850.                         |
  |                                  |                                                       |
  |                                  |Sample: *700*                                          |
  +----------------------------------+-------------------------------------------------------+
  | **headQuaters**                  |**string**                                             |
  |                                  |                                                       |
  |                                  | The place which serves as the administrative center   |
  |                                  |                                                       |
  |                                  | of an organization.                                   |
  |                                  |                                                       |
  |                                  |Sample: *seattle*                                      |
  +----------------------------------+-------------------------------------------------------+
  | **officeSize**                   |**string**                                             |
  |                                  |                                                       |
  |                                  | The size of the office.                               |
  +----------------------------------+-------------------------------------------------------+
  | **officeSquareFootage**          |**string**                                             |
  |                                  |                                                       |
  |                                  | The square footage area of the office.                |
  |                                  |                                                       |
  |                                  |Sample: *54444*                                        |
  +----------------------------------+-------------------------------------------------------+
  | **firm**                         |**string**                                             |
  |                                  |                                                       |
  |                                  | The type of firm.                                     |
  +----------------------------------+-------------------------------------------------------+
  | **pcCode**                       |**string**                                             |
  |                                  |                                                       |
  |                                  | The PC code of the organization.                      |
  +----------------------------------+-------------------------------------------------------+
  | **franchise1**                   |**string**                                             |
  |                                  |                                                       |
  |                                  | A group or company that is authorized to carry out    |
  |                                  |                                                       |
  |                                  | a specified commercial activity of the parent         |
  |                                  |                                                       |
  |                                  | organization.                                         |
  +----------------------------------+-------------------------------------------------------+
  | **franchise2**                   |**string**                                             |
  |                                  |                                                       |
  |                                  | A group or company that is authorized to carry out    |
  |                                  |                                                       |
  |                                  | a specified commercial activity of the parent         |
  |                                  |                                                       |
  |                                  | organization.                                         |
  +----------------------------------+-------------------------------------------------------+
  | **metroArea**                    |**string**                                             |
  |                                  |                                                       |
  |                                  | The metropolitan area where the company is located.   |
  +----------------------------------+-------------------------------------------------------+
  | **stAddrDelPointBarCode**        |**string**                                             |
  |                                  |                                                       |
  |                                  | A barcode representation of the address of the        |
  |                                  |                                                       |
  |                                  | company with 67 bars.                                 |
  +----------------------------------+-------------------------------------------------------+
  | **stAddrCarrierRoute**           |**string**                                             |
  |                                  |                                                       |
  |                                  | A 9 character postal carrier route which is common to |
  |                                  |                                                       |
  |                                  | a group of addresses with the same USPS delivery code |
  |                                  |                                                       |
  |                                  |Sample: *92019C005*                                    |
  +----------------------------------+-------------------------------------------------------+
  | **products**                     |**string**                                             |
  |                                  |                                                       |
  |                                  | The type of merchandise or item sold by the company.  |
  +----------------------------------+-------------------------------------------------------+
  | **services**                     |**string**                                             |
  |                                  |                                                       |
  |                                  | The description of the services offered by the        |
  |                                  |                                                       |
  |                                  | company.                                              |
  +----------------------------------+-------------------------------------------------------+
  | **brands**                       |**string**                                             |
  |                                  |                                                       |
  |                                  | The name under which the products are manufactured    |
  |                                  |                                                       |
  |                                  | and sold by the company.                              |
  +----------------------------------+-------------------------------------------------------+
  | **paymentOptions**               |**string**                                             |
  |                                  |                                                       |
  |                                  | The way in which a consumer can pay the company for   |
  |                                  |                                                       |
  |                                  | the product or service provided to them.              |
  +----------------------------------+-------------------------------------------------------+
  | **affiliations**                 |**string**                                             |
  |                                  |                                                       |
  |                                  | The organizations to which the company is formally    |
  |                                  |                                                       |
  |                                  | connected or joined to.                               |
  +----------------------------------+-------------------------------------------------------+
  | **secondaryServices**            |**string**                                             |
  |                                  |                                                       |
  |                                  | A secondary service provided by the company.          |
  +----------------------------------+-------------------------------------------------------+
  | **preferredBrands**              |**string**                                             |
  |                                  |                                                       |
  |                                  | The brands the company prefers to use.                |
  +----------------------------------+-------------------------------------------------------+
  | **Specializations**              |**string**                                             |
  |                                  |                                                       |
  |                                  | The organization's field of expertise.                |
  +----------------------------------+-------------------------------------------------------+
