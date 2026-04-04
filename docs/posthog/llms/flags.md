# Source: https://posthog.com/docs/api/flags.md

# Flags – the feature flags evaluation API endpoint - Docs

The `flags` endpoint is used to evaluate feature flags for a given `distinct_id`. This means it is the main endpoint not only for feature flags, but also experimentation, early access features, and survey display conditions.

It is a POST-only public endpoint that uses your [project token](https://app.posthog.com/project/settings) and does not return any sensitive data from your PostHog instance.

> **Note:** Make sure to send API requests to the correct domain. These are `https://us.i.posthog.com` for US Cloud, `https://eu.i.posthog.com` for EU Cloud, and your self-hosted domain for self-hosted instances. Confirm yours by checking your URL from your PostHog instance.

There are 3 steps to implement feature flags using the PostHog API:

### Step 1: Evaluate the feature flag value using `flags`

`flags` is the endpoint used to determine if a given flag is enabled for a certain user or not.

#### Request

PostHog AI

### Terminal

```shell
# Basic request (flags only)
curl -v -L --header "Content-Type: application/json" -d '  {
    "api_key": "<ph_project_token>",
    "distinct_id": "distinct_id_of_your_user",
    "groups" : {
        "group_type": "group_id"
    }
}' "https://us.i.posthog.com/flags?v=2"
# With configuration (flags + PostHog config)
curl -v -L --header "Content-Type: application/json" -d '  {
    "api_key": "<ph_project_token>",
    "distinct_id": "distinct_id_of_your_user",
    "groups" : {
        "group_type": "group_id"
    }
}' "https://us.i.posthog.com/flags?v=2&config=true"
```

### Python

```python
import requests
import json
# Basic request (flags only)
url = "https://us.i.posthog.com/flags?v=2"
headers = {
    "Content-Type": "application/json"
}
payload = {
    "api_key": "<ph_project_token>",
    "distinct_id": "user distinct id",
    "groups": {
        "group_type": "group_id"
    }
}
response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.json())
# With configuration (flags + PostHog config)
url_with_config = "https://us.i.posthog.com/flags?v=2&config=true"
response_with_config = requests.post(url_with_config, headers=headers, data=json.dumps(payload))
print(response_with_config.json())
```

### Node.js

```javascript
import fetch from "node-fetch";
async function sendFlagsRequest() {
    const headers = {
        "Content-Type": "application/json",
    };
    const payload = {
        api_key: "<ph_project_token>",
        distinct_id: "user distinct id",
        groups: {
            group_type: "group_id",
        },
    };
    // Basic request (flags only)
    const url = "https://us.i.posthog.com/flags?v=2";
    const response = await fetch(url, {
        method: "POST",
        headers: headers,
        body: JSON.stringify(payload),
    });
    const data = await response.json();
    console.log(data);
    // With configuration (flags + PostHog config)
    const urlWithConfig = "https://us.i.posthog.com/flags?v=2&config=true";
    const responseWithConfig = await fetch(urlWithConfig, {
        method: "POST",
        headers: headers,
        body: JSON.stringify(payload),
    });
    const dataWithConfig = await responseWithConfig.json();
    console.log(dataWithConfig);
}
sendFlagsRequest();
```

> **Note:** The `groups` key is only required for group-based feature flags. If you use it, replace `group_type` and `group_id` with the values for your group such as `company: "Twitter"`.

#### Using evaluation context tags and runtime filtering without SDKs

When making direct API calls to the `/flags` endpoint, you can control which flags are evaluated using evaluation context tags and runtime filtering.

##### Evaluation contexts

To filter flags by evaluation context, include the `evaluation_contexts` field in your request body:

> **Note:** The legacy parameter `evaluation_environments` is also supported for backward compatibility.

PostHog AI

### Terminal

```shell
curl -v -L --header "Content-Type: application/json" -d '  {
    "api_key": "<ph_project_token>",
    "distinct_id": "distinct_id_of_your_user",
    "evaluation_contexts": ["production", "web"]
}' "https://us.i.posthog.com/flags?v=2"
```

### Python

```python
import requests
import json
url = "https://us.i.posthog.com/flags?v=2"
headers = {
    "Content-Type": "application/json"
}
payload = {
    "api_key": "<ph_project_token>",
    "distinct_id": "user distinct id",
    "evaluation_contexts": ["production", "web"]
}
response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.json())
```

### JavaScript

```javascript
const response = await fetch("https://us.i.posthog.com/flags?v=2", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({
        api_key: "<ph_project_token>",
        distinct_id: "user-distinct-id",
        evaluation_contexts: ["production", "web"]
    }),
});
const data = await response.json();
```

Only flags where at least one evaluation tag matches (or flags with no tags at all) will be returned. For example:

-   Flag with evaluation context tags `["production", "api", "backend"]` + request with `["production", "web"]` = ✅ Flag evaluates ("production" matches)
-   Flag with evaluation context tags `["staging", "api"]` + request with `["production", "web"]` = ❌ Flag doesn't evaluate (no tags match)
-   Flag with evaluation context tags `["web", "mobile"]` + request with `["production", "web"]` = ✅ Flag evaluates ("web" matches)
-   Flag with no evaluation context tags = ✅ Always evaluates (backward compatibility)

##### Runtime detection

Evaluation runtime (server vs. client) is automatically detected based on your request headers and user-agent. This determines which flags are available based on their runtime setting (server-only, client-only, or all).

**How runtime is detected:**

1.  **User-Agent patterns** - The system analyzes the User-Agent header:

    -   **Client-side patterns**: `Mozilla/`, `Chrome/`, `Safari/`, `Firefox/`, `Edge/` (browsers), or mobile SDKs like `posthog-android/`, `posthog-ios/`, `posthog-react-native/`, `posthog-flutter/`
    -   **Server-side patterns**: `posthog-python/`, `posthog-ruby/`, `posthog-php/`, `posthog-java/`, `posthog-go/`, `posthog-node/`, `posthog-dotnet/`, `posthog-elixir/`, `python-requests/`, `curl/`
2.  **Browser-specific headers** - Presence of these headers indicates client-side:

    -   `Origin` header
    -   `Referer` header
    -   `Sec-Fetch-Mode` header
    -   `Sec-Fetch-Site` header
3.  **Default behavior** - If runtime can't be determined, the system includes flags with no runtime requirement and those set to "all"

**Examples of runtime detection:**

JavaScript

PostHog AI

```javascript
// Browser fetch - Detected as CLIENT runtime
// Will receive: client-only flags + "all" flags
// Won't receive: server-only flags
const response = await fetch("https://us.i.posthog.com/flags?v=2", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        // Browser automatically adds Origin, Referer, Sec-Fetch-* headers
    },
    body: JSON.stringify({
        api_key: "<ph_project_token>",
        distinct_id: "user-id"
    })
});
```

Python

PostHog AI

```python
# Python requests - Detected as SERVER runtime
# Will receive: server-only flags + "all" flags
# Won't receive: client-only flags
import requests
response = requests.post(
    "https://us.i.posthog.com/flags?v=2",
    json={
        "api_key": "<ph_project_token>",
        "distinct_id": "user-id"
    }
    # python-requests/ in User-Agent indicates server-side
)
```

Terminal

PostHog AI

```shell
# curl - Detected as SERVER runtime
# Will receive: server-only flags + "all" flags
# Won't receive: client-only flags
curl -v -L --header "Content-Type: application/json" -d '{
    "api_key": "<ph_project_token>",
    "distinct_id": "user-id"
}' "https://us.i.posthog.com/flags?v=2"
# curl/ in User-Agent indicates server-side
```

JavaScript

PostHog AI

```javascript
// Node.js with custom User-Agent - Control runtime detection
const response = await fetch("https://us.i.posthog.com/flags?v=2", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "User-Agent": "posthog-node/3.0.0"  // Explicitly indicates server-side
    },
    body: JSON.stringify({
        api_key: "<ph_project_token>",
        distinct_id: "user-id"
    })
});
```

##### Combining evaluation context tags and runtime filtering

Both features work together as sequential filters:

JavaScript

PostHog AI

```javascript
// Example: Production web client
const response = await fetch("https://us.i.posthog.com/flags?v=2", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        // Browser headers will trigger client runtime detection
    },
    body: JSON.stringify({
        api_key: "<ph_project_token>",
        distinct_id: "user-id",
        evaluation_contexts: ["production", "web"]
    })
});
// This request will only receive flags that:
// 1. Have runtime set to "client" OR "all" (due to browser headers)
// AND
// 2. Have evaluation context tags matching "production" OR "web" (or no tags)
// Note: You can also use the legacy "evaluation_environments" parameter
```

This allows precise control over which flags are evaluated in different contexts, helping optimize costs and improve security by ensuring flags only evaluate where intended.

#### Response

The response varies depending on whether you include the `config=true` query parameter:

##### Basic response (`/flags?v=2`)

Use this endpoint when you only need to evaluate feature flags. It returns a response with just the flag evaluation results.

> **Note:** If a feature flag is associated with an experiment that has a [holdout group](/docs/experiments/holdouts.md), users in the holdout receive a variant value in the format `holdout-{holdout_id}` (e.g., `holdout-727`). You can detect holdout users by checking if the variant starts with `holdout-`.

JSON

PostHog AI

```json
{
  "flags": {
    "my-awesome-flag": {
      "key": "my-awesome-flag",
      "enabled": true,
      "reason": {
        "code": "condition_match",
        "condition_index": 0,
        "description": "Condition set 1 matched"
      },
      "metadata": {
        "id": 1,
        "version": 1,
        "payload": "{\"example\": \"json\", \"payload\": \"value\"}"
      }
    },
    "my-multivariate-flag" :{
      "key":"my-multivariate-flag",
      "enabled": true,
      "variant": "some-string-value",
      "reason": {
        "code": "condition_match",
        "condition_index": 1,
        "description": "Condition set 2 matched"
      },
      "metadata": {
        "id": 2,
        "version": 42,
      }
    },
    "flag-thats-not-on": {
      "key": "flag-thats-not-on",
      "enabled": false,
      "reason": {
        "code": "no_condition_match",
        "condition_index": 0,
        "description": "No condition sets matched"
      },
      "metadata": {
        "id": 3,
        "version": 1
      }
    }
  },
  "errorsWhileComputingFlags": false,
  "requestId": "550e8400-e29b-41d4-a716-446655440000"
}
```

##### Full response with configuration (`/flags?v=2&config=true`)

Use this endpoint when you need both feature flag evaluation and PostHog configuration information (useful for client-side SDKs that need to initialize PostHog):

JSON

PostHog AI

```json
{
  "config": {
    "enable_collect_everything": true
  },
  "toolbarParams": {},
  "errorsWhileComputingFlags": false,
  "isAuthenticated": false,
  "requestId": "550e8400-e29b-41d4-a716-446655440000",
  "supportedCompression": [
    "gzip",
    "lz64"
  ],
  "flags": {
    "my-awesome-flag": {
      "key": "my-awesome-flag",
      "enabled": true,
      "reason": {
        "code": "condition_match",
        "condition_index": 0,
        "description": "Condition set 1 matched"
      },
      "metadata": {
        "id": 1,
        "version": 1,
        "payload": "{\"example\": \"json\", \"payload\": \"value\"}"
      }
    },
    "my-multivariate-flag" :{
      "key":"my-multivariate-flag",
      "enabled": true,
      "variant": "some-string-value",
      "reason": {
        "code": "condition_match",
        "condition_index": 1,
        "description": "Condition set 2 matched"
      },
      "metadata": {
        "id": 2,
        "version": 42,
      }
    },
    "flag-thats-not-on": {
      "key": "flag-thats-not-on",
      "enabled": false,
      "reason": {
        "code": "no_condition_match",
        "condition_index": 0,
        "description": "No condition sets matched"
      },
      "metadata": {
        "id": 3,
        "version": 1
      }
    }
  }
}
```

> **Note:** `errorsWhileComputingFlags` will return `true` if we didn't manage to compute some flags (for example, if there's an [ongoing incident involving flag evaluation](https://status.posthog.com/)).
>
> This enables partial updates to currently active flags in your clients.

#### Quota limiting

If your organization exceeds its feature flag quota, the `/flags` endpoint will return a modified response with `quotaLimited`.

For basic response (`/flags?v=2`):

JSON

PostHog AI

```json
{
  "flags": {},
  "errorsWhileComputingFlags": false,
  "quotaLimited": ["feature_flags"],
  "requestId": "d4d89b14-9619-4627-adf2-01b761691c2e"
}
```

For full response with configuration (`/flags?v=2&config=true`):

JSON

PostHog AI

```json
{
  "config": {
    "enable_collect_everything": true
  },
  "toolbarParams": {},
  "isAuthenticated": false,
  "supportedCompression": [
    "gzip",
    "lz64"
  ],
  "flags": {},
  "errorsWhileComputingFlags": false,
  "quotaLimited": ["feature_flags"],
  "requestId": "d4d89b14-9619-4627-adf2-01b761691c2e"
  // ... other fields, not relevant to feature flags
}
```

When you receive a response with `quotaLimited` containing `"feature_flags"`, it means:

1.  Your feature flag evaluations have been temporarily paused because you've exceeded your feature flag quota
2.  If you want to continue evaluating feature flags, you can increase your quota in [your billing settings](https://us.posthog.com/organization/billing) under **Feature flags & Experiments** or [contact support](https://us.posthog.com/#panel=support%3Asupport%3Abilling%3A%3Atrue)

### Step 2: Include feature flag information when capturing events

If you want use your feature flag to breakdown or filter events in your [insights](/docs/product-analytics/insights.md), you'll need to include feature flag information in those events. This ensures that the feature flag value is attributed correctly to the event.

> **Note:** This step is only required for events captured using our server-side SDKs or [API](/docs/api.md).

To do this, include the `$feature/feature_flag_name` property in your event:

PostHog AI

### Terminal

```shell
curl -v -L --header "Content-Type: application/json" -d '  {
    "api_key": "<ph_project_token>",
    "event": "your_event_name",
    "distinct_id": "distinct_id_of_your_user",
    "properties": {
      "$feature/feature-flag-key": "variant-key" # Replace feature-flag-key with your flag key. Replace 'variant-key' with the key of your variant
    }
}' https://us.i.posthog.com/i/v0/e/
```

### Python

```python
import requests
import json
url = "https://us.i.posthog.com/i/v0/e/"
headers = {
    "Content-Type": "application/json"
}
payload = {
    "api_key": "<ph_project_token>",
    "event": "your_event_name",
    "distinct_id": "distinct_id_of_your_user,
    "properties": {
      "$feature/feature-flag-key": "variant-key" # Replace feature-flag-key with your flag key. Replace 'variant-key' with the key of your variant
    }
}
response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response)
```

### Step 3: Send a `$feature_flag_called` event

To track usage of your feature flag and view related analytics in PostHog, submit the `$feature_flag_called` event whenever you check a feature flag value in your code.

You need to include two properties with this event:

1.  `$feature_flag_response`: This is the name of the variant the user has been assigned to e.g., "control" or "test"
2.  `$feature_flag`: This is the key of the feature flag in your experiment.

PostHog AI

### Terminal

```shell
curl -v -L --header "Content-Type: application/json" -d '  {
    "api_key": "<ph_project_token>",
    "event": "$feature_flag_called",
    "distinct_id": "distinct_id_of_your_user",
    "properties": {
      "$feature_flag": "feature-flag-key",
      "$feature_flag_response": "variant-name"
    }
}' https://us.i.posthog.com/i/v0/e/
```

### Python

```python
import requests
import json
url = "https://us.i.posthog.com/i/v0/e/"
headers = {
    "Content-Type": "application/json"
}
payload = {
    "api_key": "<ph_project_token>",
    "event": "feature_flag_called",
    "distinct_id": "distinct_id_of_your_user,
    "properties": {
      "$feature_flag": "feature-flag-key",
      "$feature_flag_response": "variant-name"
    }
}
response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response)
```

### Advanced: Overriding server properties

Sometimes, you may want to evaluate feature flags using [person properties](/docs/product-analytics/person-properties.md), [groups](/docs/product-analytics/group-analytics.md), or group properties that haven't been ingested yet, or were set incorrectly earlier.

You can provide properties to evaluate the flag with by using the `person properties`, `groups`, and `group properties` arguments. PostHog will then use these values to evaluate the flag, instead of any properties currently stored on your PostHog server.

For example:

PostHog AI

### Terminal

```shell
curl -v -L --header "Content-Type: application/json" -d '  {
    "api_key": "<ph_project_token>",
    "distinct_id": "distinct_id_of_your_user",
    "groups" : { # Required only for group-based feature flags
      "group_type": "group_id" # Replace "group_type" with the name of your group type. Replace "group_id" with the id of your group.
    },
    "person_properties": {"<personProp1>": "<personVal1>"}, # Optional. Include any properties used to calculate the value of the feature flag.
    "group_properties": {"group type": {"<groupProp1>":"<groupVal1>"}} # Optional. Include any properties used to calculate the value of the feature flag.
}' https://us.i.posthog.com/flags?v=2
```

### Python

```python
import requests
import json
url = "https://us.i.posthog.com/flags?v=2"
headers = {
    "Content-Type": "application/json"
}
payload = {
    "api_key": "<ph_project_token>",
    "distinct_id": "distinct_id_of_your_user",
    "groups" : { # Required only for group-based feature flags
      "group_type": "group_id" # Replace "group_type" with the name of your group type. Replace "group_id" with the id of your group.
    },
    "person_properties": {"<personProp1>": "<personVal1>"}, # Optional. Include any properties used to calculate the value of the feature flag.
    "group_properties": {"group type": {"<groupProp1>":"<groupVal1>"}} # Optional. Include any properties used to calculate the value of the feature flag.
}
response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.json())
```

### Overriding GeoIP properties

By default, a user's GeoIP properties are set using the IP address they use to capture events on the frontend. You may want to override the these properties when evaluating feature flags. A common reason to do this is when you're not using PostHog on your frontend, so the user has no GeoIP properties.

To override the GeoIP properties used to evaluate a feature flag, provide an IP address in the `HTTP_X_FORWARDED_FOR` when making your `/flags` request:

PostHog AI

### Terminal

```shell
curl -v -L \
--header "Content-Type: application/json" \
--header "HTTP_X_FORWARDED_FOR: the_client_ip_address_to_use " \
-d '  {
    "api_key": "<ph_project_token>",
    "distinct_id": "distinct_id_of_your_user"
}' https://us.i.posthog.com/flags?v=2
```

### Python

```python
import requests
import json
url = "https://us.i.posthog.com/flags?v=2"
headers = {
    "Content-Type": "application/json",
    "HTTP_X_FORWARDED_FOR": "the_client_ip_address_to_use"
}
payload = {
    "api_key": "<ph_project_token>",
    "distinct_id": "distinct_id_of_your_user"
}
response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.json())
```

The list of properties that this overrides:

1.  `$geoip_city_name`
2.  `$geoip_country_name`
3.  `$geoip_country_code`
4.  `$geoip_continent_name`
5.  `$geoip_continent_code`
6.  `$geoip_postal_code`
7.  `$geoip_time_zone`

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better