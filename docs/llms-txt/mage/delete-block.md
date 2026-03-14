# Source: https://docs.mage.ai/extensibility/api-reference/blocks/delete-block.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete block

`DELETE /api/pipelines/:pipeline_uuid/blocks/:block_uuid`

Delete a block from a pipeline.

By default, blocks with downstream dependencies may not be deleted. To force delete blocks, set the `force` query parameter to the boolean `True`.

The following example deletes a fictional block `winter_wildflower` from the `broken_wave` pipeline.

<RequestExample>
  ```bash Request theme={"system"}
  curl 'http://localhost:6789/api/pipelines/broken_wave/blocks/winter_wildflower?block_type=data_loader&api_key=zkWlN0PkIKSN0C11CfUHUj84OT5XOJ6tDZ6bDRO2&force=True' \
    -X 'DELETE'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"system"}
  {
      "block": {
          "all_upstream_blocks_executed": true,
          "color": null,
          "configuration": {},
          "downstream_blocks": [],
          "executor_config": null,
          "executor_type": "local_python",
          "has_callback": false,
          "name": "winter wildflower",
          "language": "python",
          "retry_config": null,
          "status": "not_executed",
          "type": "data_loader",
          "upstream_blocks": [],
          "uuid": "winter_wildflower"
      }
  }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).