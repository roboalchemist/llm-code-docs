# Source: https://docs.nimbleway.io/nimble-platform/online-pipelines/restaurants/uber-eats-japan.md

# Uber Eats Japan

## About

The Uber Eats Japan pipeline provides comprehensive information on various restaurants and stores available on Uber Eats in Japan. The pipeline includes details such as restaurant/store names, URLs, addresses, latitude and longitude, delivery fees, price buckets, ratings, and categories. This data is crucial for understanding the food delivery landscape, consumer preferences, and market analysis in Japan.

## Data Dictionary

| Field Name       | Data Type | Explanation                                         |
| ---------------- | --------- | --------------------------------------------------- |
| rst\_uuid        | String    | Unique identifier of the restaurant/store           |
| rst\_url         | String    | URL of the restaurant/store's Uber Eats page        |
| rst\_title       | String    | Name of the restaurant/store                        |
| delivery\_fee    | Float     | Delivery fee for the restaurant/store               |
| price\_bucket    | String    | Price range category of the restaurant/store        |
| latitude         | Float     | Latitude of the restaurant/store                    |
| longitude        | Float     | Longitude of the restaurant/store                   |
| rst\_address     | String    | Full address of the restaurant/store                |
| rating\_score    | Float     | Average rating of the restaurant/store              |
| rating\_cnt      | Integer   | Number of ratings the restaurant/store has received |
| cuisine\_cat\_1  | String    | Primary cuisine/category of the restaurant/store    |
| cuisine\_cat\_2  | String    | Secondary cuisine/category of the restaurant/store  |
| cuisine\_cat\_3  | String    | Tertiary cuisine/category of the restaurant/store   |
| cuisine\_cat\_4  | String    | Quaternary cuisine/category of the restaurant/store |
| cuisine\_cat\_5  | String    | Quinary cuisine/category of the restaurant/store    |
| phone\_num       | String    | Contact number of the restaurant/store              |
| prefecture       | String    | Prefecture where the restaurant/store is located    |
| city             | String    | City where the restaurant/store is located          |
| district         | String    | District where the restaurant/store is located      |
| collection\_date | Float     | Date the information was collected                  |

### CSV Example

{% embed url="<https://docs.google.com/spreadsheets/d/1NTy2YDdz00cxGd5v6UFap9hvcuAWkX0PxVnZ6v-tIU0/edit?gid=1240679413#gid=1240679413>" %}
