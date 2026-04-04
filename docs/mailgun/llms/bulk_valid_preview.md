# Source: https://documentation.mailgun.com/docs/validate/bulk_valid_preview.md

## List Health Preview

List Health Preview performs a free analysis of a list of email addresses allowing you to make an informed decision to run a complete bulk validation or not. Given a preview name and an uploaded file of email addresses, a preliminary validation run will be preformed. The results of the preview will be, on average, an estimate of the deliverability and risk of the emails provide. This evaluation is based on a statistical sampling of the list provided

Info
It's important to upload as *multi-part/form-data* where the file is defined by *file*.
Currently only raw *csv* and *gzip* are supported. While there is no limit on the number of email addresses that can be provided, the file size cannot exceed 25MB.
The column header for emails needs to be either *email* or *email_address*

Warning!
Lists must comply to either UTF-8 or ASCII encoding and not have a '@' in the name.


```
GET /v4/address/validate/preview
```

### Get list of all health previews.


```
POST /v4/address/validate/preview/\<list\_id\>
```

### Create a list Health Preview .

The `list_id` is an arbitrary unique identifier provided by the API caller.

Please note that the max number of validation previews that can be processed in parallel is 10. If this number is exceeded, a 400 response will be returned.


```
GET /v4/address/validate/preview/\<list\_id\>
```

### Check the current status of list Health Preview.


```
DELETE /v4/address/validate/preview/\<list\_id\>
```

### Delete a list Health Preview.


```
PUT /v4/address/validate/preview/\<list\_id\>
```

### Get the results of the list health preview:


```JSON
curl -s --user 'api:YOUR_API_KEY' -G \
    https://api.mailgun.net/v4/address/validate/preview/LIST_NAME
```

Sample Response:


```JSON
{
  "preview": {
    "id": "test_500",
    "valid": true,
    "status": "preview_complete",
    "quantity": 8,
    "created_at": 1590080191,
    "summary": {
      "result": {
        "deliverable": 37.5,
        "undeliverable": 19,
        "catch_all" : 6,
        "unknown": 37.5
      },
      "risk": {
        "high": 25,
        "low": 25,
        "medium": 12.5,
        "unknown": 37.5
      }
    }
  }
}
```

Field Explanation:

| Field | Type | Description |
|  --- | --- | --- |
| id | string | list_id name given when the list was initially created |
| created_at | string | Date/Time that the request was initiated |
| quantity | integer | number of total items in the list to be previewed |
| status | string | current state of the list validation request. (preview_processing, preview_complete) |
| valid | bool | a boolean to represent if the list is valid |
| summary | collection | summary of the verifications in the list provided |
| result | array | nested results averaged. (deliverable, undeliverable, catch_all and unknown) |
| risk | array | nested risk assessment count (high, low, medium or unknown) |


### Get a list:

This request will return a list health check.


```JSON
curl -s --user 'api:YOUR_API_KEY' -G \
    https://api.mailgun.net/v4/address/validate/preview
```

Sample Response:


```JSON
{
  "previews": [
    {
      "id": "test_500",
      "valid": true,
      "status": "preview_complete",
      "quantity": 8,
      "created_at": 1590080191,
      "summary": {
        "result": {
          "deliverable": 37.5,
          "do_not_send": 0,
          "undeliverable": 23,
          "catch_all": 2,
          "unknown": 37.5
        },
        "risk": {
          "high": 25,
          "low": 25,
          "medium": 12.5,
          "unknown": 37.5
        }
      }
    },
    {
      "id": "test_501",
      "valid": true,
      "status": "preview_complete",
      "quantity": 8,
      "created_at": 1590155015,
      "summary": {
        "result": {
          "deliverable": 37.5,
          "do_not_send": 0,
          "undeliverable": 23,
          "catch_all": 2,
          "unknown": 37.5
        },
        "risk": {
          "high": 25,
          "low": 25,
          "medium": 12.5,
          "unknown": 37.5
        }
      }
    }
  ]
}
```

### Response Fields Explanation:

| Field | Type | Description |
|  --- | --- | --- |
| previews | collection | A collection of bulk validation previews. |


## List Health Preview:


```JSON
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v4/address/validate/preview/LIST_NAME \
    -F 'file=@/path/to/file' \
```

Sample Response:


```JSON
{
  "id": "test_501",
  "message": "The bulk preview was submitted."
}
```

### Delete a list health check preview:


```JSON
curl -s --user 'api:YOUR_API_KEY' -X DELETE \
    https://api.mailgun.net/v4/address/validate/preview/LIST_NAME
```