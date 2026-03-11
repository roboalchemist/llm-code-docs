# Source: https://developers.activecampaign.com/reference/shared-objects.md

# Shared Objects

The following are objects that are shared across multiple request types in the Ecommerce GraphQL API.

## BulkAsync Response

For asynchonous bulk operations, we return a reference id which references the entire bulk operation.

| Name                | Description                                            |
| :------------------ | :----------------------------------------------------- |
| recordId (`String`) | A guid identifier recording the batch being processed. |

## Address

| Name                 | Description                                  |
| :------------------- | :------------------------------------------- |
| firstName (`String`) | Customer first name for address              |
| lastName (`String`)  | Customer last name  for address              |
| address1 (`String`)  | First line of address                        |
| address2 (`String`)  | Second line of address                       |
| address3 (`String`)  | Third line of address                        |
| city (`String`)      | Address city                                 |
| province (`String`)  | Address province or state                    |
| country (`String`)   | Address country, using 2-letter country code |
| postal (`String`)    | Address postal or zip code                   |
| phone (`String`)     | Phone number for address                     |
| company (`String`)   | Company for address                          |
| email (`String`)     | Email associated with address                |

## AddressFilter

Within search requests, each subfield within the address filter is a StringFieldFilter. Users can set one or more of these filters.

| Name                            | Description                                  |
| :------------------------------ | :------------------------------------------- |
| firstName (`StringFieldFilter`) | Customer first name for address              |
| lastName (`StringFieldFilter`)  | Customer last name  for address              |
| address1 (`StringFieldFilter`)  | First line of address                        |
| address2 (`StringFieldFilter`)  | Second line of address                       |
| address3 (`StringFieldFilter`)  | Third line of address                        |
| city (`StringFieldFilter`)      | Address city                                 |
| province (`StringFieldFilter`)  | Address province or state                    |
| country (`StringFieldFilter`)   | Address country, using 2-letter country code |
| postal (`StringFieldFilter`)    | Address postal or zip code                   |
| phone (`StringFieldFilter`)     | Phone number for address                     |
| company (`StringFieldFilter`)   | Company for address                          |
| email (`StringFieldFilter`)     | Email associated with address                |