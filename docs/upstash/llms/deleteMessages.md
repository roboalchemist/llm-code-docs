# Source: https://upstash.com/docs/qstash/api/dlq/deleteMessages.md

# Delete multiple messages from the DLQ

> Manually remove messages

Delete multiple messages from the DLQ.

<Info>
  You can get the `dlqId` from the [list DLQs endpoint](/qstash/api/dlq/listMessages).
</Info>

## Request

<ParamField body="dlqIds" type="string[]" required>
  The list of DLQ message IDs to remove.
</ParamField>

## Response

A deleted object with the number of deleted messages.

```JSON  theme={"system"}
{
  "deleted": number
}
```

<ResponseExample>
  ```json 200 OK theme={"system"}
  {
    "deleted": 3
  }
  ```
</ResponseExample>

<RequestExample>
  ```sh curl theme={"system"}
  curl -XDELETE https://qstash.upstash.io/v2/dlq \
    -H "Authorization: Bearer <token>" \
    -H "Content-Type: application/json" \
    -d '{
       "dlqIds": ["11111-0", "22222-0", "33333-0"]
      }'
  ```

  ```js Node theme={"system"}
  const response = await fetch("https://qstash.upstash.io/v2/dlq", {
    method: "DELETE",
    headers: {
      Authorization: "Bearer <token>",
      "Content-Type": "application/json",
    },
    body: {
      dlqIds: [
        "11111-0",
        "22222-0",
        "33333-0",
      ],
    },
  });
  ```

  ```python Python theme={"system"}
  import requests

  headers = {
      'Authorization': 'Bearer <token>',
      'Content-Type': 'application/json',
  }

  data = {
    "dlqIds": [
      "11111-0",
      "22222-0",
      "33333-0"
    ]
  }

  response = requests.delete(
    'https://qstash.upstash.io/v2/dlq',
    headers=headers,
    data=data
  )
  ```

  ```go Go theme={"system"}
  var data = strings.NewReader(`{
    "dlqIds": [
      "11111-0",
      "22222-0",
      "33333-0"
    ]
  }`)
  req, err := http.NewRequest("DELETE", "https://qstash.upstash.io/v2/dlq", data)
  if err != nil {
    log.Fatal(err)
  }
  req.Header.Set("Authorization", "Bearer <token>")
  req.Header.Set("Content-Type", "application/json")
  resp, err := http.DefaultClient.Do(req)
  if err != nil {
    log.Fatal(err)
  }
  defer resp.Body.Close()
  ```
</RequestExample>
