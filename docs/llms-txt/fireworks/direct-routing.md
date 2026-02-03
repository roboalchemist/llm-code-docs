# Source: https://docs.fireworks.ai/deployments/direct-routing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Direct routing

> Direct routing enables enterprise users reduce latency to their deployments.

## Internet direct routing

Internet direct routing bypasses our global API load balancer and directly routes your request to the machines where
your deployment is running. This can save several tens or even hundreds of milliseconds of time-to-first-token (TTFT)
latency.

To create a deployment using Internet direct routing:

<Note>
  When creating a deployment with direct routing, the `--region` parameter is required to specify the deployment region.
</Note>

```bash  theme={null}
$ firectl deployment create accounts/fireworks/models/llama-v3p1-8b-instruct \
    --direct-route-type INTERNET \
    --direct-route-api-keys <API_KEYS> \
    --region <REGION>

Name: accounts/my-account/deployments/abcd1234
...
Direct Route Handle: my-account-abcd1234.us-arizona-1.direct.fireworks.ai
Region: US_ARIZONA_1
```

If you have multiple API keys, use repeated fields, such as:
`--direct-route-api-keys=<API_KEY_1> --direct-route-api-keys=<API_KEY_2>`. These keys can
be any alpha-numeric string and are a distinct concept from the API keys provisioned via the Fireworks console. A key
provisioned in the console but not specified the list here will not be allowed when querying the model via direct
routing.

Take note of the `Direct Route Handle` to get the inference endpoint. This is what you will use access the deployment
instead of the global `https://api.fireworks.ai/inference/` endpoint. For example:

```bash  theme={null}
curl \
    --header 'Authorization: Bearer <DIRECT_ROUTE_API_KEY>' \
    --header 'Content-Type: application/json' \
    --data '{
        "model": "accounts/fireworks/models/llama-v3-8b-instruct",
        "prompt": "The sky is"
    }' \
    --url https://my-account-abcd1234.us-arizona-1.direct.fireworks.ai/v1/completions
```

### Use Python SDKs with direct routing

Set the direct route handle as the `base_url` when you initialize the SDK so your calls go straight to the regional deployment endpoint.

<Warning>
  **Important:** The `base_url` format differs between SDKs:

  * **OpenAI SDK:** Include the `/v1` suffix (e.g., `https://...direct.fireworks.ai/v1`)
  * **Fireworks SDK:** Omit the `/v1` suffix (e.g., `https://...direct.fireworks.ai`)
</Warning>

<CodeGroup>
  ```python OpenAI SDK theme={null}
  from openai import OpenAI

  client = OpenAI(
      # Note: Include /v1 suffix for OpenAI SDK
      base_url="https://my-account-abcd1234.us-arizona-1.direct.fireworks.ai/v1",
      api_key="<YOUR_DIRECT_ROUTE_API_KEY>"
  )

  response = client.chat.completions.create(
      model="accounts/fireworks/models/llama-v3-8b-instruct",
      messages=[{"role": "user", "content": "Hello!"}]
  )
  ```

  ```python Fireworks SDK theme={null}
  from fireworks import Fireworks

  client = Fireworks(
      # Note: No /v1 suffix for Fireworks SDK
      base_url="https://my-account-abcd1234.us-arizona-1.direct.fireworks.ai",
      api_key="<YOUR_DIRECT_ROUTE_API_KEY>"
  )

  response = client.chat.completions.create(
      model="accounts/fireworks/models/llama-v3-8b-instruct",
      messages=[{"role": "user", "content": "Hello!"}]
  )
  ```
</CodeGroup>

<Info>
  The direct route handle replaces the standard `https://api.fireworks.ai/inference/v1` endpoint, bypassing the global load balancer to reduce latency.
</Info>

For a complete code-only example that demonstrates creating a direct route deployment and querying it, see the [Python SDK direct route deployment example](https://github.com/fw-ai-external/python-sdk/blob/main/examples/direct_route_deployment.py).

## Supported Regions for Direct Routing

Direct routing is currently supported in the following regions:

* `US_IOWA_1`
* `US_VIRGINIA_1`
* `US_ARIZONA_1`
* `US_ILLINOIS_1`
* `US_TEXAS_1`
* `US_ILLINOIS_2`
* `EU_FRANKFURT_1`
* `US_WASHINGTON_3`
* `US_WASHINGTON_1`
* `AP_TOKYO_1`

## Private Service Connect (PSC)

Contact your Fireworks representative to set up [GCP Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect)
to your deployment.

## AWS PrivateLink

Contact your Fireworks representative to set up [AWS PrivateLink](https://aws.amazon.com/privatelink/) to your
deployment.
