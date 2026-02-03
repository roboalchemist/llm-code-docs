# Source: https://docs.apify.com/api/v2/dataset-get.md

# Get dataset


```
GET 
https://api.apify.com/v2/datasets/:datasetId
```


Returns dataset object for given dataset ID.

This does not return dataset items, only information about the storage itself. To retrieve dataset items, use the [List dataset items](https://docs.apify.com/api/v2/dataset-items-get.md) endpoint.

note

Keep in mind that attributes `itemCount` and `cleanItemCount` are not propagated right away after data are pushed into a dataset.

There is a short period (up to 5 seconds) during which these counters may not match with exact counts in dataset items.

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
