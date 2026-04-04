# Source: https://docs.nimbleway.io/nimble-platform/online-pipelines/real-estate/zillow.md

# Zillow

## About

The US Real Estate pipeline provides comprehensive information on properties across the United States. The pipeline includes details such as property addresses, square footage, number of bathrooms and bedrooms, latitude and longitude, price history, and agent information. This data is essential for real estate analysis, market research, and investment decisions.

## Data Dictionary

| Field Name             | Data Type | Explanation                                                                 |
| ---------------------- | --------- | --------------------------------------------------------------------------- |
| zpid                   | Integer   | Unique Zillow property identifier                                           |
| address                | String    | Full address of the property                                                |
| city                   | String    | City where the property is located                                          |
| state                  | String    | State where the property is located                                         |
| zip                    | String    | ZIP code of the property location                                           |
| sqft                   | Integer   | Total square footage of the property                                        |
| is\_complex            | Boolean   | Indicates if the property is part of a complex or building                  |
| baths                  | Float     | Number of bathrooms in the property                                         |
| beds                   | Integer   | Number of bedrooms in the property                                          |
| lat                    | Float     | Latitude coordinates of the property location                               |
| lng                    | Float     | Longitude coordinates of the property location                              |
| rent                   | Float     | Monthly rent price (if the property is listed for rent)                     |
| zrent                  | Float     | Estimated rent price as calculated by Zillow                                |
| home\_status           | String    | Current status of the home (e.g., For Sale, For Rent, Sold)                 |
| home\_type             | String    | Type of property (e.g., Single Family, Condo, Apartment)                    |
| reference\_url         | String    | URL to the Zillow page or reference URL for the property listing            |
| url                    | String    | URL to the Zillow property listing                                          |
| description            | String    | Description of the property as provided in the listing                      |
| great\_schools\_rating | Integer   | Rating of nearby schools according to GreatSchools (if available)           |
| price\_history         | String    | History of price changes for the property (if available)                    |
| days\_on\_zillow       | Integer   | Number of days the property has been listed on Zillow                       |
| agent\_name            | String    | Name of the listing agent                                                   |
| agent\_business\_name  | String    | Business name or agency associated with the listing agent                   |
| agent\_type            | String    | Type of agent (e.g., Listing Agent, Buyer’s Agent)                          |
| agent\_info            | String    | Additional information about the agent (e.g., contact details, specialties) |
| days\_listed           | Integer   | Number of days the property has been actively listed                        |
| contacts               | Integer   | Number of contacts or inquiries received regarding the property listing     |
| applications           | Integer   | Number of rental applications submitted for the property (if applicable)    |
| owner                  | String    | Name or identifier of the owner (if available and applicable)               |

### CSV Example

{% embed url="<https://docs.google.com/spreadsheets/d/1tA1DhrPCAZ7weTnntd9GiVcznpVaxKox1wiKdOLZewY/edit?usp=sharing>" fullWidth="false" %}
