# Source: https://docs.promptlayer.com/features/prompt-history/groups.md

# Groups

[Endpoint Reference](/reference/track-group)

It is helpful to link requests to eachother when building workflows with chains and agents. PromptLayer allows you to create a group and add individual request IDs into the group. You will then be able to visually inspect groups through the dashboard.

<CodeGroup>
  ```python Python theme={null}
  pl_group_id = promptlayer_client.group.create()

  promptlayer_client.track.group(
    request_id=pl_request_id, 
    group_id=pl_group_id
  )
  ```

  ```js JavaScript theme={null}
  const pl_group_id = await promptLayerClient.group.create()

  await promptLayerClient.track.group({
    request_id: pl_request_id, 
    group_id: pl_group_id
  })
  ```

  ```bash REST theme={null}
  curl --request POST \
    --url https://api.promptlayer.com/rest/track-group \
    --header 'Content-Type: application/json' \
    --data '{
      "api_key": "pl_<YOUR API KEY>",
      "request_id": "<REQUEST ID>",
      "group_id": "<GROUP ID>",
  }'
  ```
</CodeGroup>

Request group information will appear on the dashboard.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt