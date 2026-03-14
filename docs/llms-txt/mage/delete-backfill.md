# Source: https://docs.mage.ai/extensibility/api-reference/backfills/delete-backfill.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete backfill

`DELETE /api/backfills/:backfill_id`

<RequestExample>
  ```curl cURL theme={"system"}
  curl -X DELETE 
  --url http://localhost:6789/api/backfills/1
  -H 'Content-Type: application/json' 
  -H 'Cookie: oauth_token=some_really_long_string' 
  -H 'X-API-KEY: zkWlN0PkIKSN0C11CfUHUj84OT5XOJ6tDZ6bDRO2' 
  ```

  ```python Python theme={"system"}
  headers = {
  "Content-Type": "application/json",
  "X-API-KEY": "zkWlN0PkIKSN0C11CfUHUj84OT5XOJ6tDZ6bDRO2",
  "Cookie": "oauth_token=some_really_long_string"
  }

  r = requests.delete('http://localhost:6789/api/backfills/1', headers=headers)
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"system"}
  {
      "backfill": {
          "id": 1,
          "block_uuid": null,
          "completed_at": null,
          "created_at": "2023-07-17 21:48:42",
          "end_datetime": null,
          "failed_at": null,
          "interval_type": null,
          "interval_units": null,
          "metrics": null,
          "name": "arwen_starlight_backfill",
          "pipeline_schedule_id": null,
          "pipeline_uuid": "arwen_starlight",
          "start_datetime": null,
          "started_at": null,
          "status": null,
          "updated_at": "2023-07-17 21:48:42",
          "variables": null
      }
  }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).