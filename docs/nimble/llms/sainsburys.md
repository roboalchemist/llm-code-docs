# Source: https://docs.nimbleway.io/nimble-platform/online-pipelines/supermarkets/sainsburys.md

# Sainsbury’s

## About

The Sainsbury's pipeline provides detailed information on various grocery items available at Sainsbury's. It includes details such as product description, availability, pricing, and manufacturer information. This pipeline is valuable for market analysis, product comparison, and consumer behavior studies.

## Data Dictionary

| Field Name             | Data Type | Explanation                                        |
| ---------------------- | --------- | -------------------------------------------------- |
| seller                 | String    | Seller of the product (e.g., Asda)                 |
| description            | String    | Description of the product                         |
| review\_count          | Integer   | Number of reviews the product has received         |
| availability           | String    | Availability status of the product (e.g., InStock) |
| collection\_time       | Timestamp | Time when the data was collected                   |
| gtin                   | String    | Global Trade Item Number (barcode)                 |
| uuid                   | String    | Unique identifier for the product                  |
| manufacturer           | String    | Manufacturer of the product                        |
| price                  | Float     | Price of the product                               |
| product\_id            | String    | Product identifier                                 |
| currency               | String    | Currency of the price (e.g., £)                    |
| sku                    | String    | Stock Keeping Unit identifier                      |
| brand                  | String    | Brand of the product                               |
| image                  | String    | URL of the product image                           |
| weight                 | String    | Weight of the product                              |
| rating\_score          | Float     | Average rating score of the product                |
| url                    | String    | URL of the product page                            |
| price\_unit            | String    | Unit price of the product                          |
| condition              | String    | Condition of the product (e.g., NewCondition)      |
| promotions             | String    | Promotions available for the product               |
| name                   | String    | Name of the product                                |
| category               | String    | Category of the product                            |
| price\_per\_unit       | Float     | Price per unit of the product                      |
| loyalty\_offers        | String    | Loyalty offers available for the product           |
| simple\_loyalty\_price | Float     | Simple loyalty price for the product               |
| day                    | Date      | Day when the data was collected                    |

### CSV Example

{% embed url="<https://docs.google.com/spreadsheets/d/1DjguHfahTko6t-j8xXPs4SYD4vrgMAYQ0DL0c51XrsA/edit?usp=sharing>" %}
