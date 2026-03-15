# Source: https://posthog.com/docs/product-analytics/installation/nodejs.md

# Source: https://posthog.com/docs/logs/installation/nodejs.md

# Source: https://posthog.com/docs/feature-flags/installation/nodejs.md

# Source: https://posthog.com/docs/endpoints/start-here/retrieve-data/nodejs.md

# Retrieve data from your endpoint with Node.js - Docs

Call PostHog endpoints from Node.js.

## Basic request

JavaScript

PostHog AI

```javascript
const response = await fetch(
  "<ph_app_host>/api/environments/{project_id}/endpoints/{endpoint_name}/run",
  {
    headers: {
      "Authorization": `Bearer ${process.env.POSTHOG_PERSONAL_API_KEY}`
    }
  }
);
const data = await response.json();
console.log(data);
```

## With variables

JavaScript

PostHog AI

```javascript
const response = await fetch(
  "<ph_app_host>/api/environments/{project_id}/endpoints/{endpoint_name}/run",
  {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${process.env.POSTHOG_PERSONAL_API_KEY}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ variables: { customer_id: "cust_123" } })
  }
);
const data = await response.json();
```

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better