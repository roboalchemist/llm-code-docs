# Source: https://docs.fireworks.ai/deployments/direct-routing.md

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
$ firectl create deployment accounts/fireworks/models/llama-v3p1-8b-instruct \
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

### Use the OpenAI SDK with direct routing

Set the direct route handle (with the `/v1` suffix) as the `base_url` when you initialize the OpenAI SDK so your calls go straight to the regional deployment endpoint.

```python  theme={null}
from openai import OpenAI

client = OpenAI(
    api_key="<YOUR_DIRECT_ROUTE_API_KEY>",
    base_url="https://my-account-abcd1234.us-arizona-1.direct.fireworks.ai/v1"
)

response = client.chat.completions.create(
    model="accounts/fireworks/models/llama-v3-8b-instruct",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

<Info>
  The direct route handle replaces the standard [https://api.fireworks.ai/inference/v1](https://api.fireworks.ai/inference/v1) endpoint—keep the `/v1` suffix so the OpenAI SDK routes requests correctly while bypassing the global load balancer to reduce latency.
</Info>

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
