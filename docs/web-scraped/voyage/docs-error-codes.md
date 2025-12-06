# Source: https://docs.voyageai.com/docs/error-codes

## GET STARTED 

- [[[Introduction]]](/docs/introduction)
- [[[API Key and Python Client]]](/docs/api-key-and-installation)
- [[[Quickstart Tutorial]]](/docs/quickstart-tutorial)

## CAPABILITIES 

- [[[Text Embeddings]]](/docs/embeddings)
- [[[Contextualized Chunk Embeddings]]](/docs/contextualized-chunk-embeddings)
- [[[Multimodal Embeddings]]](/docs/multimodal-embeddings)
- [[[Rerankers]]](/docs/reranker)

## GUIDES 

- [[[Tokenization]]](/docs/tokenization)
- [[[Flexible Dimensions and Quantization]]](/docs/flexible-dimensions-and-quantization)
- [[[Batch Inference]]](/docs/batch-inference)
- [[[Error Codes]]](/docs/error-codes)
- [[[Rate Limits]]](/docs/rate-limits)
- [[[Pricing]]](/docs/pricing)
- [[[Organizations and Projects]]](/docs/organizations-and-projects)
- [[[Service Level Objectives]]](/docs/service-level-objectives)

## DEPLOYMENT ON VPC 

- [[AWS Marketplace Model Package]]
  - [[[MongoDB Voyage AI Models in AWS]]](/docs/aws-marketplace-mongodb-voyage)
  - [[[Voyage AI Models in AWS]]](/docs/aws-marketplace-voyage)
- [[Azure Marketplace Managed Application]]
  - [[[MongoDB Voyage AI Models in Azure]]](/docs/azure-marketplace-mongodb-voyage)
  - [[[Voyage AI Models in Azure]]](/docs/azure-marketplace-voyage)

## ACCESS VIA DATA PLATFORMS 

- [[[Snowflake]]](/docs/snowflake)

## Community 

- [[[Integrations]]](/docs/integrations-and-other-libraries)
- [[[Community SDKs]]](/docs/community-sdks)

## HELP 

- [[[FAQ]]](/docs/faq)
- [[[Contact Email]]](/docs/contact-email)
- [[[Discord]]](/docs/discord)

Powered by [](https://readme.com?ref_src=hub&project=voyage-ai)

# Error Codes

The following table shows the possible error codes that might be returned from the API.

+--------------------------+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::  | :::                                           | Description                                                                                                                                                                                                                                                                             |
| Error Code               | Error Type                                                         |                                                                                                                                                                                                                                                                                         |
| :::                      | :::                                                                |                                                                                                                                                                                                                                                                                         |
+==========================+====================================================================+=========================================================================================================================================================================================================================================================================================+
| 🔴 400                   | `Invalid Request`     | - **Cause:** The request is invalid, which might be due to one of the following reasons:                                                                                                                                                                                                |
|                          |                                                                    |                                                                                                                                                                                                                                                                                         |
|                          |                                                                    | <!-- -->                                                                                                                                                                                                                                                                                |
|                          |                                                                    |                                                                                                                                                                                                                                                                                         |
|                          |                                                                    | - The request body is not a valid [JSON](https://en.wikipedia.org/wiki/JSON);                                                                                                                                                                                           |
|                          |                                                                    | - A parameter is invalid or has the wrong type.                                                                                                                                                                                                                                         |
|                          |                                                                    | - Batch size is too large;                                                                                                                                                                                                                                                              |
|                          |                                                                    | - Total number of tokens in the batch exceeds the limit;                                                                                                                                                                                                                                |
|                          |                                                                    | - Number of tokens in an example exceeds the context length;                                                                                                                                                                                                                            |
|                          |                                                                    |                                                                                                                                                                                                                                                                                         |
|                          |                                                                    | **Solution:** The specific error will be indicated in the error message. Double check the request body and correct the errors.                                                                                                                                                          |
+--------------------------+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 🔴 401                   | `Unauthorized`        | - **Cause:** Invalid authentication.\                                                                                                                                                                                                                                                   |
|                          |                                                                    |   **Solution:** Ensure the API key is correctly specified in the HTTP request header. Please create or view your API key in our [dashboard](https://dash.voyageai.com).                                                                                                 |
+--------------------------+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 🔴 403                   | `Forbidden`           | - **Cause:** The IP address you are sending the request from might be forbidden.\                                                                                                                                                                                                       |
|                          |                                                                    |   **Solution:** Try to use a different IP address to call the API.                                                                                                                                                                                                                      |
+--------------------------+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 🔴 429                   | `Rate Limit Exceeded` | - **Cause:** The frequency of your requests is too high.\                                                                                                                                                                                                                               |
|                          |                                                                    |   **Solution:** Please pace your requests. Read the [rate limit guide](/docs/rate-limits) for more information.                                                                                                                                                         |
+--------------------------+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 🔴 500                   | `Server Error`        | - **Cause:** Unexpected issue on our servers.\                                                                                                                                                                                                                                          |
|                          |                                                                    |   **Solution:** Retry your request after a brief wait. If the error persists, please contact us at [[\[email protected\]]](/cdn-cgi/l/email-protection#f1929e9f85909285b1879e889096949098df929e9c). |
+--------------------------+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 🔴 502\                  | `Service Unavailable` | - **Cause:** Our servers are currently experiencing high traffic.\                                                                                                                                                                                                                      |
| 🔴 503\                  |                                                                    |   **Solution:** Retry your requests after a brief wait.                                                                                                                                                                                                                                 |
| 🔴 504                   |                                                                    |                                                                                                                                                                                                                                                                                         |
+--------------------------+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Updated 24 days ago

------------------------------------------------------------------------

[[]](/docs/batch-inference)

Batch Inference

[](/docs/rate-limits)

Rate Limits

[]