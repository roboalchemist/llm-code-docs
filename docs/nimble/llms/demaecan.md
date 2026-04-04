# Source: https://docs.nimbleway.io/nimble-platform/online-pipelines/restaurants/demaecan.md

# Demaecan

## About

The Demaecan pipeline provides detailed information on various restaurants available on Demaecan in Japan. The pipeline includes details such as restaurant names, URLs, addresses, categories, whether they are delivered by Demaecan, average ratings, number of ratings, and additional restaurant information. This data is essential for market analysis, consumer behavior studies, and understanding the food delivery landscape in Japan.

## Data Dictionary

| Field Name              | Data Type | Explanation                                          |
| ----------------------- | --------- | ---------------------------------------------------- |
| rst\_url                | String    | URL of the restaurant's Demaecan page                |
| rst\_title              | String    | Name of the restaurant                               |
| rst\_address            | String    | Full address of the restaurant                       |
| rst\_cat                | String    | Category of the restaurant                           |
| delivered\_by\_demaecan | Boolean   | Indicates if the restaurant is delivered by Demaecan |
| avg\_rating\_score      | Float     | Average rating of the restaurant                     |
| rating\_cnt             | Integer   | Number of ratings the restaurant has received        |
| rst\_info               | string    | Additional information about the restaurant          |
| rst\_id                 | Integer   | Unique identifier for the restaurant                 |
| rst\_holidays           | String    | Holidays or days off for the restaurant              |
| delivery\_fee           | Float     | Delivery fee for the restaurant                      |
| latitude                | Float     | Latitude of the restaurant                           |
| longitude               | Float     | Longitude of the restaurant                          |
| prefecture              | String    | Prefecture where the restaurant is located           |
| city                    | String    | City where the restaurant is located                 |
| district                | String    | District where the restaurant is located             |
| collection\_date        | Float     | Date the information was collected                   |

### CSV Example

{% embed url="<https://docs.google.com/spreadsheets/d/1vC-DBqQP1D-uGFnoVQ8w3p7LH8nBFGFFqBqSqvRDRfg/edit?usp=sharing>" %}
