# Source: https://upstash.com/docs/qstash/api/url-groups/remove.md

# Source: https://upstash.com/docs/qstash/api/schedules/remove.md

# Source: https://upstash.com/docs/qstash/api/queues/remove.md

# Source: https://upstash.com/docs/qstash/api/url-groups/remove.md

# Remove URL Group

> Remove a URL group and all its endpoints

The URL Group and all its endpoints are removed. In flight messages in the URL Group are not removed but you will not be able to send messages to the topic anymore.

## Request

<ParamField path="urlGroupName" type="string" required>
  The name of the URL Group to remove.
</ParamField>

## Response

This endpoint returns 200 if the URL Group is removed successfully.

<RequestExample>
  ```sh curl theme={"system"}
  curl -XDELETE https://qstash.upstash.io/v2/topics/my-url-group \
    -H "Authorization: Bearer <token>"
  ```

  ```js Node theme={"system"}
  const response = await fetch('https://qstash.upstash.io/v2/topics/my-url-group', {
    method: 'DELETE',
    headers: {
      'Authorization': 'Bearer <token>'
    }
  });
  ```

  ```python Python theme={"system"}
  import requests

  headers = {
      'Authorization': 'Bearer <token>',
  }

  response = requests.delete(
    'https://qstash.upstash.io/v2/topics/my-url-group', 
    headers=headers
  )
  ```

  ```go Go  theme={"system"}
  req, err := http.NewRequest("DELETE", "https://qstash.upstash.io/v2/topics/my-url-group", nil)
  if err != nil {
    log.Fatal(err)
  }
  req.Header.Set("Authorization", "Bearer <token>")
  resp, err := http.DefaultClient.Do(req)
  if err != nil {
    log.Fatal(err)
  }
  defer resp.Body.Close()
  ```
</RequestExample>
