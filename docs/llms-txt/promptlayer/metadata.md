# Source: https://docs.promptlayer.com/features/prompt-history/metadata.md

# Metadata

PromptLayer allows you to attach multiple key value pairs as metadata to a request. In the dashboard, you can look up requests and analyze analytics using metadata.

We recommend using this for things like session IDs, user IDs, or error messages. Metadata is useful to help you use the [advanced search](/why-promptlayer/advanced-search) or understand the Analytics page.

[Endpoint Reference](/reference/track-metadata)

<CodeGroup>
  ```python Python theme={null}
  promptlayer_client.track.metadata(
    request_id=pl_request_id,
    metadata={
        "user_id":"1abf2345f",
        "post_id": "2cef2345f"
    }
  )
  ```

  ```js JavaScript theme={null}
  promptLayerClient.track.metadata({
    request_id: pl_request_id,
    metadata: {
        "user_id":"1abf2345f",
        "post_id": "2cef2345f"
    }
  })
  ```

  ```java Java theme={null}
  ```

  ```bash REST theme={null}
  curl --request POST \
    --url https://api.promptlayer.com/rest/track-metadata \
    --header 'Content-Type: application/json' \
    --data '{
      "api_key": "pl_<YOUR API KEY>",
      "request_id": "<REQUEST ID>",
      "metadata": {
        "user_id":"1abf2345f",
        "post_id": "2cef2345f"
      }
    }'
  ```
</CodeGroup>

Things to note:

1. Currently keys and values need to be strings in PromptLayer.
2. If you track a key that was already tracked before for a specific request\_id, the value that corresponds to that key will be replaced.

***

Once metadata is added, you will then be able to see it in the web UI.

<img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/metadata-ui.png?fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=240bbb2b1105d461328cd5f70fb67d20" alt="score" data-og-width="596" width="596" data-og-height="652" height="652" data-path="images/metadata-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/metadata-ui.png?w=280&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=ddfc19ae8ce3ffe718e66d37bafe01e4 280w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/metadata-ui.png?w=560&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=83a629275f1fcfcf728d2196d6b4c8d1 560w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/metadata-ui.png?w=840&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=f65b1d65d5231aaba78742aabe2401a1 840w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/metadata-ui.png?w=1100&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=56a713f45aee902dac51d8aa2ea766f5 1100w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/metadata-ui.png?w=1650&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=79e8e9d99d251db66bd34e9cf3ef3317 1650w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/metadata-ui.png?w=2500&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=5b8faf61b8840c1f11503ca0efb6d53e 2500w" />

Please note that while metadata is optimized for storing unique, request-specific data such as user IDs or session IDs, it might not be the best choice for categorizing requests when you have a small set of predefined categories. For categorization based on a small number of predefined options, please use [tags](/features/prompt-history/tagging-requests) instead.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt