# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/InAppPurchasesFound.md.txt

# InAppPurchasesFound

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/InAppPurchasesFound#SCHEMA_REPRESENTATION)

Additional details of in-app purchases encountered during the crawl.

|                                    JSON representation                                    |
|-------------------------------------------------------------------------------------------|
| ``` { "inAppPurchasesFlowsStarted": integer, "inAppPurchasesFlowsExplored": integer } ``` |

|                                                                  Fields                                                                   ||
|-------------------------------|------------------------------------------------------------------------------------------------------------|
| `inAppPurchasesFlowsStarted`  | `integer` The total number of in-app purchases flows started.                                              |
| `inAppPurchasesFlowsExplored` | `integer` The total number of in-app purchases flows explored: how many times the robo tries to buy a SKU. |