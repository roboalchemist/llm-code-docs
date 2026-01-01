# Source: https://docs.promptlayer.com/features/prompt-history/scoring-requests.md

# Score Requests

Every PromptLayer request can be given an integer score 0-100.

<img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score.png?fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=8b896707afa30337bb9f55c279d760dc" alt="score" data-og-width="508" width="508" data-og-height="323" height="323" data-path="images/score.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score.png?w=280&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=9db97db42d8866c96c6daef256712239 280w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score.png?w=560&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=4c682ccc105c128932f2b557bfcd60bb 560w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score.png?w=840&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=978572c9b692ad7fb93f3968213db360 840w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score.png?w=1100&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=27b528431eb381b9870941596a31b9a9 1100w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score.png?w=1650&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=0519c71245467e1a34fe6d6b7a9caa0a 1650w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score.png?w=2500&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=872a8c4d9ee9f4db5b97ecfbee9147a7 2500w" />

To associate a score with a prompt, you can either do this visually from the dashboard or programmatically.
By default, an individual score is named default. You can enrich a request with multiple scores using "named scores" as shown below.
[Endpoint Reference](/reference/track-score)

<CodeGroup>
  ```python Python theme={null}
  # named score
  promptlayer_client.track.score(
    request_id=pl_request_id, 
    score_name="summarization",
    score=100
  )

  # default score
  promptlayer_client.track.score(
    request_id=pl_request_id, 
    # score_name="default",
    score=100
  )
  ```

  ```js JavaScript theme={null}
  promptLayerClient.track.score({
    request_id: pl_request_id,
    score: 100
  })
  ```

  ```bash REST theme={null}
  curl --request POST \
    --url https://api.promptlayer.com/rest/track-score \
    --header 'Content-Type: application/json' \
    --data '{
      "api_key": "pl_<YOUR API KEY>",
      "request_id": "<REQUEST ID>",
      "score": <YOUR SCORE>,
      "name": <YOUR SCORE NAME>,
    }'
  ```
</CodeGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt