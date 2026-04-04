# Source: https://docs.apify.com/api/v2/dataset-items-post.md

# Store items


```
POST 
https://api.apify.com/v2/datasets/:datasetId/items
```


Appends an item or an array of items to the end of the dataset. The POST payload is a JSON object or a JSON array of objects to save into the dataset.

If the data you attempt to store in the dataset is invalid (meaning any of the items received by the API fails the validation), the whole request is discarded and the API will return a response with status code 400. For more information about dataset schema validation, see [Dataset schema](https://docs.apify.com/platform/actors/development/actor-definition/dataset-schema/validation).

**IMPORTANT:** The limit of request payload size for the dataset is 5 MB. If the array exceeds the size, you'll need to split it into a number of smaller arrays.

## Request

## Responses

* 201
* 400

**Response Headers**

* **Location**

**Response Headers**

