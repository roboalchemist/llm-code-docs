# Source: https://docs.acceldata.io/api/activities--votes---comments-.md

# Activities (Votes & Comments)

Activities let users upvote, downvote, or comment on assets. This is especially useful for crowd-sourced data governance.
For example, analysts can upvote a trusted dataset, while commenting that another dataset is deprecated, making it easier for others to choose the right data.

> ⚠️ All endpoints require authentication. See [Authentication & Headers](https://docs.acceldata.io/acceldata-data-observability-cloud/api/authentication).

## Endpoint(s)

- `GET /catalog-server/api/assets/:id/activity` - **Get upvotes/downvotes**
- `GET /catalog-server/api/assets/:id/comments` - **Get comments**

## Path Parameters

| Name | Type | Required | Description | Example | 
| ---- | ---- | ---- | ---- | ---- | 
| id | int | Yes | Asset ID | `12616` | 


## Sample Request

```bash
curl -X GET "https://demo.acceldata.io/catalog-server/api/assets/12616/comments"
```



## Response Schema

See [Activities Schema](https://docs.acceldata.io/acceldata-data-observability-cloud/api/activities-schema).