# Source: https://docs.nimbleway.io/nimble-platform/online-pipelines/restaurants/uber-eats-us.md

# Uber Eats US

## About

The US Uber Eats Restaurants pipeline provides detailed information on various restaurants available on Uber Eats in the United States. This pipeline is valuable for market analysis, restaurant comparison, and consumer behavior studies. It includes details such as restaurant descriptions, availability, pricing, location, and ratings.

## Data Dictionary

| Field Name       | Data Type | Explanation                               |
| ---------------- | --------- | ----------------------------------------- |
| data\_type       | string    | Type of data (e.g., restaurant)           |
| rst\_uuid        | string    | Unique identifier for the restaurant      |
| rst\_url         | string    | URL of the restaurant on Uber Eats        |
| rst\_title       | string    | Title of the restaurant                   |
| delivery\_fee    | float64   | Delivery fee for the restaurant           |
| price\_bucket    | string    | Price range of the restaurant             |
| latitude         | float64   | Latitude of the restaurant location       |
| longitude        | float64   | Longitude of the restaurant location      |
| state            | string    | State where the restaurant is located     |
| city             | string    | City where the restaurant is located      |
| zipcode          | int64     | Zip code of the restaurant location       |
| rst\_address     | string    | Address of the restaurant                 |
| rating\_score    | float64   | Rating score of the restaurant            |
| rating\_cnt      | int64     | Number of ratings for the restaurant      |
| cuisine\_cat\_1  | string    | First cuisine category of the restaurant  |
| cuisine\_cat\_2  | string    | Second cuisine category of the restaurant |
| cuisine\_cat\_3  | string    | Third cuisine category of the restaurant  |
| cuisine\_cat\_4  | string    | Fourth cuisine category of the restaurant |
| cuisine\_cat\_5  | string    | Fifth cuisine category of the restaurant  |
| phone\_num       | int64     | Phone number of the restaurant            |
| collection\_date | float     | Date when the data was collected          |

### CSV Example

{% embed url="<https://docs.google.com/spreadsheets/d/1mlccUyA4AVx5R5Vweki0Wu1UIkaqUoUQDZMDz28rKsI/edit?usp=sharing>" %}
