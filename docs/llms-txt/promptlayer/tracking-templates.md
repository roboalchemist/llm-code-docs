# Source: https://docs.promptlayer.com/features/prompt-history/tracking-templates.md

# Tracking Templates

PromptLayer allows you to track prompt template usage, latency, cost, and more. This is done by associating a request with a prompt template as shown below.

[Endpoint Reference](/reference/track-prompt)

To associate requests with a prompt from the prompt registry, run the code

<CodeGroup>
  ```python Python theme={null}
  promptlayer_client.track.prompt(
    request_id=pl_request_id, 
    prompt_name="example-2",
    prompt_input_variables=input_variables,
    version=2
  )
  ```

  ```js JavaScript theme={null}
  promptLayerClient.track.prompt({
    request_id: pl_request_id, 
    prompt_name: "example-2",
    prompt_input_variables: input_variables,
    version: 2
  })
  ```

  ```bash REST theme={null}
  curl --request POST \
    --url https://api.promptlayer.com/rest/track-prompt \
    --header 'Content-Type: application/json' \
    --data '{
      "api_key": "pl_<YOUR API KEY>",
      "request_id": "<REQUEST ID>",
      "prompt_name": "<PROMPT TEMPLATE NAME>",
      "prompt_input_variables": <PROMPT TEMPLATE INPUT VARIABLES>,
      "version": <PROMPT TEMPLATE VERSION NUMBER>
    }'
  ```
</CodeGroup>

Where `prompt_name` is a prompt in your prompt registry, `prompt_input_variables` is a dictionary corresponding to the input variables you formatted the prompt with, and `version` is the version of the prompt you are trying to track. `version` is optional, by default it will track the newest version of the prompt.

This information will appear on your dashboard under your request and prompt template pages.

<img src="https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/tracking-template-ui.png?fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=62cf872a1e4808489e25304b43c43284" alt="score" data-og-width="691" width="691" data-og-height="207" height="207" data-path="images/tracking-template-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/tracking-template-ui.png?w=280&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=002e7529376a9174cc6765e9c0ceb01f 280w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/tracking-template-ui.png?w=560&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=22fb7efc58e7fbea185d86ba83bcaccf 560w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/tracking-template-ui.png?w=840&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=b0ec773e178f6e49a6a3588e7408c349 840w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/tracking-template-ui.png?w=1100&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=b97aa9023f2e90f28766584fa7b728ce 1100w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/tracking-template-ui.png?w=1650&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=db4b4676f23101f6133781a9a2975923 1650w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/tracking-template-ui.png?w=2500&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=c27d7b69e4cf22bcbd53eb42433af0d1 2500w" />

You can also use prompt [template release labels](/features/prompt-registry#release-labels) instead of a version number.

<CodeGroup>
  ```python Python theme={null}
  promptlayer_client.track.prompt(
    request_id=pl_request_id, 
    prompt_name="example-2",
    prompt_input_variables=input_variables,
    label="prod"
  )
  ```

  ```js JavaScript theme={null}
  promptLayerClient.track.prompt({
    request_id: pl_request_id, 
    prompt_name: "example-2",
    prompt_input_variables: input_variables,
    label: "prod"
  })
  ```

  ```bash REST theme={null}
  curl --request POST \
    --url https://api.promptlayer.com/rest/track-prompt \
    --header 'Content-Type: application/json' \
    --data '{
      "api_key": "pl_<YOUR API KEY>",
      "request_id": "<REQUEST ID>",
      "prompt_name": "<PROMPT TEMPLATE NAME>",
      "prompt_input_variables": <PROMPT TEMPLATE INPUT VARIABLES>,
      "label": "<YOUR PROMPT VERSION LABEL>"
    }'
  ```
</CodeGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt