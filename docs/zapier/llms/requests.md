# Source: https://docs.zapier.com/powered-by-zapier/api-reference/common-types/requests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Requests

Requests follow the [JSON API spec](https://jsonapi.org/format/#fetching) and should send the header Accept: application/vnd.api+json.

Typical arguments for requests are sent via query params, for more information check the specific requests for each endpoint in the API Reference section.

Example:

```bash  theme={null}
curl --request GET \
  --url https://stoplight.io/mocks/zapier/public-api/181772442/zaps \
  --header 'Accept: application/vnd.api+json'
```
