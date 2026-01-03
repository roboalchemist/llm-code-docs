# Source: https://documentation.mailgun.com/docs/validate/bulk-valid-ir.md

# Bulk Validation

Note:
NoteÂ Bulk Validation allows for the validation of a list of email addresses. Given a list name and an uploaded file of email addresses, a backend processing job will be run to verify the list. Once the validations have all been completed, the results will be provided with download links.

Note:
NoteÂ Itâs important to upload asÂ multi-part/form-dataÂ where the file is defined byÂ file.Â Currently only rawÂ csvÂ andÂ gzipÂ are supported. While there is no limit on the number of email addresses that can be provided, the file size cannot exceed 25MB.Â The column header for emails needs to be eitherÂ emailÂ orÂ email_address

Warning!
WarningÂ Lists must comply to either UTF-8 or ASCII encoding and not have a â@â in the name.


```
GET /v4/address/validate/bulk
```

Get list of all bulk validation jobs.


```
POST /v4/address/validate/bulk/<list_id>
```

Create a bulk validation job. TheÂ `list_id`Â is an arbitrary unique identifier provided by the API caller.

Please note that the max number of validation jobs that can be processed in parallel is 5. If this number is exceeded, a 400 response will be returned.


```
GET /v4/address/validate/bulk/<list_id>
```

Check the current status of a bulk validation job.


```
DELETE /v4/address/validate/bulk/<list_id>
```

This endpoint can be used to cancel an in-progress bulk validation job or delete results for a completed bulk validation job. When this endpoint is called for an âuploadedâ job, associated result files will be deleted and the jobâs status will be set to âdeletedâ.

Get the status of a bulk validation job:


```JSON
curl -s --user 'api:YOUR_API_KEY' -G \
    https://api.mailgun.net/v4/address/validate/bulk/LIST_NAME
```

Sample Response:


```JSON
{
  "created_at": "Tue, 26 Feb 2019 21:30:03 GMT",
  "download_url": {
    "csv": "<download_link>",
    "json": "<download_link>"
  },
  "id": "bulk_validations_sandbox_mailgun_org",
  "quantity": 207665,
  "records_processed": 207665,
  "status": "uploaded",
  "summary": {
    "result": {
      "deliverable": 181854,
      "do_not_send": 5647,
      "undeliverable": 12116,
      "catch_all" : 2345,
      "unknown": 5613
    },
    "risk": {
      "high": 17763,
      "low": 142547,
      "medium": 41652,
      "unknown": 5613
    }
  }
}
```

## Field Explanation:

| Parameter | Type | Description |
|  --- | --- | --- |
| created_at | string | Date/Time that the request was initiated |
| download_url | array | csvÂ andÂ jsonÂ representation of the download link for the results of the bulk validation |
| id | string | list_id name given when the list was initially created} |
| quantity | integer | number of total items in the list to be verified |
| records_processed | integer | de-duplicated total of verified email addresses |
| status | string | current state of the list validation request. (created,Â processing,Â completed,Â uploading,Â uploaded, andÂ failed) |
| summary | collection | summary of the validations in the list provided |
| result | array | nested results count. (catch_all,Â deliverable,Â do_not_send,Â undeliverable, andÂ unknown) |
| risk | array | nested risk assessment count (high,Â low,Â mediumÂ orÂ unknown) |


Get a list of bulk validation jobs:
This request will return a list of validation jobs in descending order by time created.


```JSON
curl -s --user 'api:YOUR_API_KEY' -G \
    https://api.mailgun.net/v4/address/validate/bulk
```

| Parameter | Type | Description |
|  --- | --- | --- |
| limit | integer | Number of entries to return. Default: 500. |


Sample Response:


```JSON
    {
        "jobs":[
        {
            "created_at": "Tue, 26 Feb 2019 21:30:03 GMT",
            "download_url": {
                "csv": "<download_link>",
                "json": "<download_link>"
            }
            "id": "bulk_validations_sandbox2_mailgun_org",
            "quantity": 207665,
            "records_processed": 207665,
            "status": "uploaded",
            "summary": {
                "result": {
                    "deliverable": 181854,
                    "do_not_send": 5647,
                    "undeliverable": 12116,
                    "catch_all" : 2345,
                    "unknown": 5613},
                "risk": {
                    "high": 17763,
                    "low": 142547,
                    "medium": 41652,
                    "unknown": 5613}
            }
        },
        {
            "created_at": "Tue, 23 Feb 2019 21:30:03 GMT",
            "download_url": {
                "csv": "<download_link>",
                "json": "<download_link>"
            }
            "id": "bulk_validations_sandbox_mailgun_org",
            "quantity": 207,
            "records_processed": 207,
            "status": "uploaded",
            "summary": {
                "result": {
                    "deliverable": 181854,
                    "do_not_send": 5647,
                    "undeliverable": 12116,
                    "catch_all" : 2345,
                    "unknown": 5613},
                "risk": {
                    "high": 17763,
                    "low": 142547,
                    "medium": 41652,
                    "unknown": 5613}
            }
        }],
    "total":3,
    "paging": {
      "next":
          "https://url_to_next_page",
      "previous":
          "https://url_to_previous_page",
      "first":
          "https://url_to_first_page",
      "last":
          "https://url_to_last_page"
    },
}
```

Results Fields Explanation:

| Field | Description |
|  --- | --- |
| Deliverable | The collection of validation jobs requested for. |
| Undeliverable | The total number of validation jobs. |
| Do Not Send | A collection of pagination links for traversing the validation jobs. |
| Catch All | The total number of domain associated with result is considered a catch_all domain |


Create a bulk validation job:


```JSON
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v4/address/validate/bulk/LIST_NAME \
    -F 'file=@/path/to/file' \
```

Sample Response:


```JSON
{
 "id": "myemails",
 "message": "The validation job was submitted."
}
```

Cancel a bulk validation job:


```
curl -s --user 'api:YOUR_API_KEY' -X DELETE \
    https://api.mailgun.net/v4/address/validate/bulk/LIST_NAME
```

Sample Response:


```JSON
{
 "message": "Validation job canceled."
}
```