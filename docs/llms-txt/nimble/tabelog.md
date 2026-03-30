# Source: https://docs.nimbleway.io/nimble-platform/online-pipelines/restaurants/tabelog.md

# Tabelog

## About

The Tabelog pipeline provides detailed information on various restaurants across Japan. The pipeline includes details such as restaurants name, URLs, addresses, prefectures, cities, districts, latitude and longitude, categories, cuisines, ratings, review counts, hours of operation, and various attributes like private dining options, reservation details, and more. This data is essential for market analysis, consumer behavior studies, and location-based services in Japan.

## Data Dictionary

| Field Name                         | Data Type | Explanation                                                                                                      |
| ---------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------- |
| rst\_uuid                          | Integer   | Unique identifier of the restaurant                                                                              |
| rst\_title                         | String    | Name of the restaurant                                                                                           |
| rst\_address                       | String    | Full address of the restaurant                                                                                   |
| prefecture                         | String    | Prefecture where the restaurant is located                                                                       |
| city                               | String    | City where the restaurant is located                                                                             |
| district                           | String    | District or neighborhood where the restaurant is located                                                         |
| latitude                           | Float     | Latitude coordinates of the restaurant location                                                                  |
| longitude                          | Float     | Longitude coordinates of the restaurant location                                                                 |
| rst\_cat                           | String    | General category of the restaurant (e.g., cuisine types, establishment types)                                    |
| cuisine\_cat\_1                    | String    | Primary cuisine category of the restaurant                                                                       |
| cuisine\_cat\_2                    | String    | Secondary cuisine category of the restaurant                                                                     |
| cuisine\_cat\_3                    | String    | Tertiary cuisine category of the restaurant                                                                      |
| rating\_cnt                        | Integer   | Number of ratings received by the restaurant                                                                     |
| rating\_score                      | Float     | Average rating score of the restaurant (on a scale of 1-5)                                                       |
| dinner\_max\_price                 | Integer   | Maximum price for dinner (in yen)                                                                                |
| dinner\_min\_price                 | Integer   | Minimum price for dinner (in yen)                                                                                |
| lunch\_max\_price                  | Integer   | Maximum price for lunch (in yen)                                                                                 |
| lunch\_min\_price                  | Integer   | Minimum price for lunch (in yen)                                                                                 |
| nearest\_station\_info             | String    | Information about the nearest station to the restaurant                                                          |
| image\_url                         | String    | URL to the image of the restaurant                                                                               |
| home\_page\_url                    | String    | URL to the official homepage of the restaurant                                                                   |
| rst\_url                           | String    | URL to the restaurant's page on the review site (e.g., Tabelog)                                                  |
| is\_family\_friendly               | Boolean   | Whether the restaurant is family-friendly (1: yes, 0: no)                                                        |
| is\_friend\_friendly               | Boolean   | Whether the restaurant is friend-friendly (1: yes, 0: no)                                                        |
| is\_alone\_friendly                | Boolean   | Whether the restaurant is suitable for dining alone (1: yes, 0: no)                                              |
| phone\_num                         | String    | Contact phone number of the restaurant                                                                           |
| access\_info                       | String    | Information about how to access the restaurant (e.g., nearby public transport stations, directions)              |
| business\_hours\_info              | String    | Information on the restaurant’s business hours and last order times                                              |
| payment\_info                      | String    | Accepted payment methods at the restaurant (e.g., credit cards, electronic money, QR code payments)              |
| num\_seats                         | Integer   | Number of seats available in the restaurant                                                                      |
| smoking\_info                      | String    | Information on smoking policy in the restaurant (e.g., non-smoking, smoking area available)                      |
| parking\_info                      | String    | Information on parking availability for the restaurant                                                           |
| space\_equipment\_info             | String    | Information on the space and equipment available in the restaurant (e.g., Wi-Fi, seating options, accessibility) |
| cellular\_info                     | String    | Information on cellular reception or services available in the restaurant                                        |
| drinks\_info                       | String    | Information on drinks served at the restaurant (e.g., types of alcoholic beverages)                              |
| private\_room\_info                | String    | Information on the availability of private rooms and capacity of such rooms                                      |
| cooking\_info                      | String    | Information on any special cooking styles or focus of the restaurant (e.g., focus on vegetables or fish dishes)  |
| reservation\_possibility\_info     | String    | Whether reservations are accepted and details about reservation policies                                         |
| service\_charge\_info              | String    | Information on any service charge or table charge applicable                                                     |
| holiday\_info                      | String    | Days when the restaurant is closed (e.g., Sundays, holidays)                                                     |
| usage\_info                        | String    | Common usage scenarios for the restaurant (e.g., family dining, large parties)                                   |
| service\_info                      | String    | Information on additional services offered by the restaurant (e.g., takeout, delivery, party services)           |
| opening\_date                      | Date      | The date when the restaurant was opened                                                                          |
| children\_info                     | String    | Information about the restaurant’s policies or accommodations for children (e.g., high chairs, children’s menu)  |
| dress\_code\_info                  | String    | Information about any dress code required for dining at the restaurant                                           |
| reservation\_num                   | String    | Contact number for making reservations                                                                           |
| max\_num\_people\_for\_reservation | Integer   | Maximum number of people allowed for a reservation                                                               |
| course\_info                       | String    | Information on set menus or courses available at the restaurant                                                  |
| awards\_info                       | String    | Information on any awards received by the restaurant                                                             |
| collection\_date                   | Date      | The date when the data was last collected or updated                                                             |

### CSV Example

{% embed url="<https://docs.google.com/spreadsheets/d/1i2dYYeJqU4mNaLkKyE-sUy1QMXk03ovlNLn0U92vSlY/edit?gid=219203318#gid=219203318>" %}
