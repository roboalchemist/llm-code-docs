# Source: https://docs.gitguardian.com/api-docs/pagination.md

# Pagination

> Explains cursor-based pagination for navigating large datasets returned by the GitGuardian API, with examples in Python and Bash.

Cursor-based pagination is the method used to navigate through the large datasets offered by the GitGuardian API. This method allows you to retrieve items in chunks (pages) by using cursors, which are pointers to a specific item in a dataset. The cursor indicates the position in the dataset, making it easier to navigate back and forth between pages.

## How cursor-based pagination works

- **Initial Request**: When you make the first request to an endpoint, you receive the first set of results
- **Subsequent Requests**: Use the response's [`link`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link) header to request the next set of results.
`link: <https://api.staging.gitguardian.tech/v1/members?cursor=cD03Mjc%3D>; rel="next"`
- **No more data**: If there's no more data to retrieve, the response will have no `link` header.

## Examples

### Python

```python

BASE_URL = "https://api.gitguardian.com/v1"
API_KEY = os.environ['GITGUARDIAN_API_TOKEN']
HEADERS = {"Authorization": f"Token {API_KEY}"}
endpoint_url = f"{BASE_URL}/members?per_page=10"
all_members = []

while True:
    response = requests.get(endpoint_url, headers=HEADERS)
    assert response.status_code == 200, response.json()
    all_members += response.json()

    if "next" not in response.links:
        # final page was reached
        break

    endpoint_url = response.links["next"]["url"]
```

### Bash/cURL

```bash
#!/bin/bash

URL="https://api.gitguardian.com/v1/members?per_page=10"

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "jq could not be found, please install it to parse JSON."
    exit 1
fi

MEMBERS="[]"

while [ "${URL}" ]; do
    RESP=$(curl -i -Ss -H "Authorization: Token $API_KEY" "${URL}")
    # Check for curl error
    if [ $? -ne 0 ]; then
        echo "Error: Failed to retrieve data from ${URL}"
        exit 1
    fi

    # Extract HTTP status code
    HTTP_STATUS=$(echo "$RESP" | grep HTTP | awk '{print $2}')
    if [ "$HTTP_STATUS" != "200" ]; then
        echo "Error: Received HTTP status $HTTP_STATUS"
        exit 1
    fi

    # Retrieve the body of the response and parse it with jq
    BODY=$(echo "$RESP" | sed -n '/^\r$/,$p' | sed '1d' | jq '.')
    # Append to members list
    MEMBERS=$(echo "${MEMBERS}" | jq ". + ${BODY}")

    # Retrieve the next url from the response's headers
    URL=$(echo "$RESP" | grep -i '^link:' | sed -n -E 's/^link:.*<(.*)>; rel="next".*/\1/p')
done

# Output the members list formatted with jq
echo "${MEMBERS}" | jq '.'
```
