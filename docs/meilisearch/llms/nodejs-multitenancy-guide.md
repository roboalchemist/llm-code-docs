# Node.js multitenancy guide
Source: https://www.meilisearch.com/docs/guides/multitenancy_nodejs

Learn how to implement secure, multitenant search in your Node.js applications.

This guide will walk you through implementing search in a multitenant Node.js application handling sensitive medical data.

## What is multitenancy?

In Meilisearch, you might have one index containing data belonging to many distinct tenants. In such cases, your tenants must only be able to search through their own documents. You can implement this using [tenant tokens](/learn/security/multitenancy_tenant_tokens).

## Requirements

* [Node.js](https://nodejs.org/en) and a package manager like `npm`, `yarn`, or `pnpm`
* [Meilisearch JavaScript SDK](/learn/resources/sdks)
* A Meilisearch server running — see our [quick start](/learn/getting_started/cloud_quick_start)
* A search API key — available in your Meilisearch dashboard
* A search API key UID — retrieve it using the [keys endpoints](/reference/api/keys)

<Tip>
  Prefer self-hosting? Read our [installation guide](/learn/self_hosted/install_meilisearch_locally).
</Tip>

## Data models

This guide uses a simple data model to represent medical appointments. The documents in the Meilisearch index will look like this:

```json theme={null}
[
  {
    "id": 1,
    "patient": "John",
    "details": "I think I caught a cold. Can you help me?",
    "status": "pending"
  },
  {
    "id": 2,
    "patient": "Zia",
    "details": "I'm suffering from fever. I need an appointment ASAP.",
    "status": "pending"
  },
  {
    "id": 3,
    "patient": "Kevin",
    "details": "Some confidential information Kevin has shared.",
    "status": "confirmed"
  }
]
```

For the purpose of this guide, we assume documents are stored in an `appointments` index.

## Creating a tenant token

The first step is generating a tenant token that will allow a given patient to search only for their appointments. To achieve this, you must first create a tenant token that filters results based on the patient's ID.

Create a `search.js` file and use the following code to generate a tenant token:

```js theme={null}
// search.js

import { Meilisearch } from 'meilisearch'

const apiKey = 'YOUR_SEARCH_API_KEY'
const apiKeyUid = 'YOUR_SEARCH_API_KEY_UID'
const indexName = 'appointments'

const client = new Meilisearch({
  host: 'https://edge.meilisearch.com', // Your Meilisearch host
  apiKey: apiKey
})

export function createTenantToken(patientName) {
  const searchRules = {
    [indexName]: {
      'filter': `patient = ${patientName}`
    }
  }

  const tenantToken = client.generateTenantToken(
    apiKeyUid,
    searchRules,
    {
      expiresAt: new Date('2030-01-01'), // Choose an expiration date
      apiKey: apiKey,
    }
  )
  return tenantToken
}
```

When Meilisearch gets a search query with a tenant token, it decodes it and applies the search rules to the search request. In this example, the results are filtered by the `patient` field. This means that a patient can only search for their own appointments.

## Using the tenant token

Now that you have a tenant token, use it to perform searches. To achieve this, you will need to:

* On the server: create an endpoint to send the token to your front-end
* On the client: retrieve the token and use it to perform searches

### Serving the tenant token

This guide uses [Express.js](https://expressjs.com/en/starter/installing.html) to create the server. You can install `express` by running:

```sh theme={null}