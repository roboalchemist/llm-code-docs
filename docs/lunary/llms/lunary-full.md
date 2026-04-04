# Lunary Documentation

Source: https://docs.lunary.ai/llms-full.txt

---

# List top LLM models across an organization
Source: https://docs.lunary.ai/docs/api/analytics/list-top-llm-models-across-an-organization

https://api.lunary.ai/v1/openapi get /v1/analytics/org/models/top
Returns the top models used across every project in the authenticated organization.
This endpoint requires an org-level private API key supplied as a bearer token in the `Authorization` header.




# Retrieve audit logs
Source: https://docs.lunary.ai/docs/api/audit-logs/retrieve-audit-logs

https://api.lunary.ai/v1/openapi get /v1/audit-logs
Retrieve a list of audit logs for the current organization. Note that this functionality is still under development and the audits logs are not fully exhaustive.



# Create a new checklist
Source: https://docs.lunary.ai/docs/api/checklists/create-a-new-checklist

https://api.lunary.ai/v1/openapi post /v1/checklists
Creates a new checklist with the provided slug, type, and data.




# Delete a checklist
Source: https://docs.lunary.ai/docs/api/checklists/delete-a-checklist

https://api.lunary.ai/v1/openapi delete /v1/checklists/{id}
Delete a specific checklist by its ID.




# Get a specific checklist
Source: https://docs.lunary.ai/docs/api/checklists/get-a-specific-checklist

https://api.lunary.ai/v1/openapi get /v1/checklists/{id}
Retrieve a specific checklist by its ID.




# List all checklists
Source: https://docs.lunary.ai/docs/api/checklists/list-all-checklists

https://api.lunary.ai/v1/openapi get /v1/checklists
Retrieve all checklists for the current project.
Optionally filter by type. Returns checklists ordered by most recently updated.




# Update a checklist
Source: https://docs.lunary.ai/docs/api/checklists/update-a-checklist

https://api.lunary.ai/v1/openapi patch /v1/checklists/{id}
Update an existing checklist's slug and/or data.




# Attach an evaluator to a dataset
Source: https://docs.lunary.ai/docs/api/datasets-v2/attach-an-evaluator-to-a-dataset

https://api.lunary.ai/v1/openapi post /v1/datasets-v2/{datasetId}/evaluators



# Create dataset v2
Source: https://docs.lunary.ai/docs/api/datasets-v2/create-dataset-v2

https://api.lunary.ai/v1/openapi post /v1/datasets-v2



# Create dataset v2 item
Source: https://docs.lunary.ai/docs/api/datasets-v2/create-dataset-v2-item

https://api.lunary.ai/v1/openapi post /v1/datasets-v2/{datasetId}/items



# Create dataset version snapshot
Source: https://docs.lunary.ai/docs/api/datasets-v2/create-dataset-version-snapshot

https://api.lunary.ai/v1/openapi post /v1/datasets-v2/{datasetId}/versions



# Delete dataset v2
Source: https://docs.lunary.ai/docs/api/datasets-v2/delete-dataset-v2

https://api.lunary.ai/v1/openapi delete /v1/datasets-v2/{datasetId}



# Delete dataset v2 item
Source: https://docs.lunary.ai/docs/api/datasets-v2/delete-dataset-v2-item

https://api.lunary.ai/v1/openapi delete /v1/datasets-v2/{datasetId}/items/{itemId}



# Detach an evaluator from a dataset
Source: https://docs.lunary.ai/docs/api/datasets-v2/detach-an-evaluator-from-a-dataset

https://api.lunary.ai/v1/openapi delete /v1/datasets-v2/{datasetId}/evaluators/{slot}



# Duplicate dataset v2
Source: https://docs.lunary.ai/docs/api/datasets-v2/duplicate-dataset-v2

https://api.lunary.ai/v1/openapi post /v1/datasets-v2/{datasetId}/duplicate



# Generate dataset item output
Source: https://docs.lunary.ai/docs/api/datasets-v2/generate-dataset-item-output

https://api.lunary.ai/v1/openapi post /v1/datasets-v2/{datasetId}/items/{itemId}/generate



# Get dataset v2
Source: https://docs.lunary.ai/docs/api/datasets-v2/get-dataset-v2

https://api.lunary.ai/v1/openapi get /v1/datasets-v2/{datasetId}



# Get dataset v2 item
Source: https://docs.lunary.ai/docs/api/datasets-v2/get-dataset-v2-item

https://api.lunary.ai/v1/openapi get /v1/datasets-v2/{datasetId}/items/{itemId}



# Get dataset version
Source: https://docs.lunary.ai/docs/api/datasets-v2/get-dataset-version

https://api.lunary.ai/v1/openapi get /v1/datasets-v2/{datasetId}/versions/{versionId}



# Import dataset items from CSV or JSONL
Source: https://docs.lunary.ai/docs/api/datasets-v2/import-dataset-items-from-csv-or-jsonl

https://api.lunary.ai/v1/openapi post /v1/datasets-v2/{datasetId}/import



# List dataset v2 items
Source: https://docs.lunary.ai/docs/api/datasets-v2/list-dataset-v2-items

https://api.lunary.ai/v1/openapi get /v1/datasets-v2/{datasetId}/items



# List dataset versions
Source: https://docs.lunary.ai/docs/api/datasets-v2/list-dataset-versions

https://api.lunary.ai/v1/openapi get /v1/datasets-v2/{datasetId}/versions



# List datasets v2
Source: https://docs.lunary.ai/docs/api/datasets-v2/list-datasets-v2

https://api.lunary.ai/v1/openapi get /v1/datasets-v2



# Restore dataset to a previous version
Source: https://docs.lunary.ai/docs/api/datasets-v2/restore-dataset-to-a-previous-version

https://api.lunary.ai/v1/openapi post /v1/datasets-v2/{datasetId}/versions/{versionId}/restore



# Run all evaluators attached to a dataset on every item
Source: https://docs.lunary.ai/docs/api/datasets-v2/run-all-evaluators-attached-to-a-dataset-on-every-item

https://api.lunary.ai/v1/openapi post /v1/datasets-v2/{datasetId}/evaluators/run



# Update dataset v2
Source: https://docs.lunary.ai/docs/api/datasets-v2/update-dataset-v2

https://api.lunary.ai/v1/openapi patch /v1/datasets-v2/{datasetId}



# Update dataset v2 item
Source: https://docs.lunary.ai/docs/api/datasets-v2/update-dataset-v2-item

https://api.lunary.ai/v1/openapi patch /v1/datasets-v2/{datasetId}/items/{itemId}



# Create a new dataset
Source: https://docs.lunary.ai/docs/api/datasets/create-a-new-dataset

https://api.lunary.ai/v1/openapi post /v1/datasets



# Create a new prompt
Source: https://docs.lunary.ai/docs/api/datasets/create-a-new-prompt

https://api.lunary.ai/v1/openapi post /v1/datasets/prompts



# Create a new prompt variation
Source: https://docs.lunary.ai/docs/api/datasets/create-a-new-prompt-variation

https://api.lunary.ai/v1/openapi post /v1/datasets/variations



# Delete a dataset
Source: https://docs.lunary.ai/docs/api/datasets/delete-a-dataset

https://api.lunary.ai/v1/openapi delete /v1/datasets/{id}



# Delete a prompt
Source: https://docs.lunary.ai/docs/api/datasets/delete-a-prompt

https://api.lunary.ai/v1/openapi delete /v1/datasets/prompts/{id}



# Delete a prompt variation
Source: https://docs.lunary.ai/docs/api/datasets/delete-a-prompt-variation

https://api.lunary.ai/v1/openapi delete /v1/datasets/variations/{id}



# Get dataset by ID or slug
Source: https://docs.lunary.ai/docs/api/datasets/get-dataset-by-id-or-slug

https://api.lunary.ai/v1/openapi get /v1/datasets/{identifier}



# Get prompt by ID
Source: https://docs.lunary.ai/docs/api/datasets/get-prompt-by-id

https://api.lunary.ai/v1/openapi get /v1/datasets/prompts/{id}



# Get prompt variation by ID
Source: https://docs.lunary.ai/docs/api/datasets/get-prompt-variation-by-id

https://api.lunary.ai/v1/openapi get /v1/datasets/variations/{id}



# List datasets
Source: https://docs.lunary.ai/docs/api/datasets/list-datasets

https://api.lunary.ai/v1/openapi get /v1/datasets



# Update a dataset
Source: https://docs.lunary.ai/docs/api/datasets/update-a-dataset

https://api.lunary.ai/v1/openapi patch /v1/datasets/{id}



# Update a prompt
Source: https://docs.lunary.ai/docs/api/datasets/update-a-prompt

https://api.lunary.ai/v1/openapi patch /v1/datasets/prompts/{id}



# Update a prompt variation
Source: https://docs.lunary.ai/docs/api/datasets/update-a-prompt-variation

https://api.lunary.ai/v1/openapi patch /v1/datasets/variations/{variationId}



# Create a criterion
Source: https://docs.lunary.ai/docs/api/evals/create-a-criterion

https://api.lunary.ai/v1/openapi post /v1/evals/criteria



# Create a new evaluation
Source: https://docs.lunary.ai/docs/api/evals/create-a-new-evaluation

https://api.lunary.ai/v1/openapi post /v1/evals



# Delete a criterion
Source: https://docs.lunary.ai/docs/api/evals/delete-a-criterion

https://api.lunary.ai/v1/openapi delete /v1/evals/criteria/{id}



# Delete an evaluation
Source: https://docs.lunary.ai/docs/api/evals/delete-an-evaluation

https://api.lunary.ai/v1/openapi delete /v1/evals/{id}



# Get a single result
Source: https://docs.lunary.ai/docs/api/evals/get-a-single-result

https://api.lunary.ai/v1/openapi get /v1/evals/results/{id}



# Get criterion by ID
Source: https://docs.lunary.ai/docs/api/evals/get-criterion-by-id

https://api.lunary.ai/v1/openapi get /v1/evals/criteria/{id}



# Get evaluation by ID
Source: https://docs.lunary.ai/docs/api/evals/get-evaluation-by-id

https://api.lunary.ai/v1/openapi get /v1/evals/{id}



# List evaluations
Source: https://docs.lunary.ai/docs/api/evals/list-evaluations

https://api.lunary.ai/v1/openapi get /v1/evals



# List results for an evaluation
Source: https://docs.lunary.ai/docs/api/evals/list-results-for-an-evaluation

https://api.lunary.ai/v1/openapi get /v1/evals/{evalId}/results



# Run the evaluation
Source: https://docs.lunary.ai/docs/api/evals/run-the-evaluation

https://api.lunary.ai/v1/openapi post /v1/evals/{id}/run



# Update a criterion
Source: https://docs.lunary.ai/docs/api/evals/update-a-criterion

https://api.lunary.ai/v1/openapi patch /v1/evals/criteria/{id}



# Update an evaluation
Source: https://docs.lunary.ai/docs/api/evals/update-an-evaluation

https://api.lunary.ai/v1/openapi patch /v1/evals/{id}



# Introduction
Source: https://docs.lunary.ai/docs/api/introduction

Overview of the Lunary.ai API.

# API Reference

Use the Lunary API to access programmatically access your data.

## Base URL

The base URL for the Lunary Cloud API is:

```bash  theme={null}
https://api.lunary.ai/v1
```

In the case of self-hosting, replace the host with your backend's URL.

## Authentication

You'll need to authenticate your requests to access any of the endpoints in the data API.

To obtain your private API key, visit the [Settings Page](https://app.lunary.ai/settings). Each project has its own private and public API key.

The private API key can be passed in the Authorization header as a Bearer token.

Some endpoints, such as the ingestion endpoint, can be accessed with the public key.

### Sample request

```bash  theme={null}
curl --get 'https://api.lunary.ai/v1/runs' \
  -H "Authorization: Bearer <api_key>" \
  -d "limit=10" \
  -d "page=0" \
  -d "order=asc" \
  -d "type=llm" 
```

## Rate Limiting

The API employs a sliding window rate limiter. The current rate limit for this endpoint is set at 30 requests per second.

## Error Handling

Standard HTTP status codes are used for error handling:

* `429`: Rate limit exceeded.

* `422`: Missing or incorrect parameters.

* `403`: Unauthorized access .

* `50X`: Internal server error.


# Create a new model
Source: https://docs.lunary.ai/docs/api/models/create-a-new-model

https://api.lunary.ai/v1/openapi post /v1/models



# Delete a model
Source: https://docs.lunary.ai/docs/api/models/delete-a-model

https://api.lunary.ai/v1/openapi delete /v1/models/{id}



# List models
Source: https://docs.lunary.ai/docs/api/models/list-models

https://api.lunary.ai/v1/openapi get /v1/models



# Update a model
Source: https://docs.lunary.ai/docs/api/models/update-a-model

https://api.lunary.ai/v1/openapi patch /v1/models/{id}



# Create a playground endpoint
Source: https://docs.lunary.ai/docs/api/playground-endpoints/create-a-playground-endpoint

https://api.lunary.ai/v1/openapi post /v1/playground-endpoints
Create a new playground endpoint



# Delete a playground endpoint
Source: https://docs.lunary.ai/docs/api/playground-endpoints/delete-a-playground-endpoint

https://api.lunary.ai/v1/openapi delete /v1/playground-endpoints/{id}
Delete a playground endpoint



# Get a playground endpoint
Source: https://docs.lunary.ai/docs/api/playground-endpoints/get-a-playground-endpoint

https://api.lunary.ai/v1/openapi get /v1/playground-endpoints/{id}
Get a specific playground endpoint by ID



# List all playground endpoints
Source: https://docs.lunary.ai/docs/api/playground-endpoints/list-all-playground-endpoints

https://api.lunary.ai/v1/openapi get /v1/playground-endpoints
Get all playground endpoints for the current project



# Update a playground endpoint
Source: https://docs.lunary.ai/docs/api/playground-endpoints/update-a-playground-endpoint

https://api.lunary.ai/v1/openapi put /v1/playground-endpoints/{id}
Update an existing playground endpoint



# Delete a run
Source: https://docs.lunary.ai/docs/api/runs/delete-a-run

https://api.lunary.ai/v1/openapi delete /v1/runs/{id}
Delete a specific run by its ID. This action is irreversible.



# Export runs data
Source: https://docs.lunary.ai/docs/api/runs/export-runs-data

https://api.lunary.ai/v1/openapi get /v1/runs/export
This endpoint requires a valid private API key sent as a bearer token.




# Get a specific run
Source: https://docs.lunary.ai/docs/api/runs/get-a-specific-run

https://api.lunary.ai/v1/openapi get /v1/runs/{id}
Retrieve detailed information about a specific run by its ID.



# Get related runs
Source: https://docs.lunary.ai/docs/api/runs/get-related-runs

https://api.lunary.ai/v1/openapi get /v1/runs/{id}/related



# Get run usage statistics
Source: https://docs.lunary.ai/docs/api/runs/get-run-usage-statistics

https://api.lunary.ai/v1/openapi get /v1/runs/usage
Retrieve usage statistics for runs



# Get runs
Source: https://docs.lunary.ai/docs/api/runs/get-runs

https://api.lunary.ai/v1/openapi get /v1/runs
The Runs API endpoint allows you to retrieve data about specific runs from your Lunary application.

The most common run types are 'llm', 'agent', 'chain', 'tool', 'thread' and 'chat'.

It supports various filters to narrow down the results according to your needs.

This endpoint supports GET requests and expects query parameters for filtering the results.




# Ingest run events
Source: https://docs.lunary.ai/docs/api/runs/ingest-run-events

https://api.lunary.ai/v1/openapi post /v1/runs/ingest
This endpoint is for reporting data from platforms not supported by our SDKs.

You can use either your project's Public or Private Key as the Bearer token in the Authorization header.

The expected body is an array of Event objects.

For LLM calls, you would first track a `start` event with the `input` data.
Once your LLM call succeeds, you would need to send an `end` event to the API endpoint with the `output` data from the LLM call.

For a full step-by-step guide on sending LLM data to the Lunary API, see the [Custom Integration](/docs/integrations/custom) guide.




# Update run feedback
Source: https://docs.lunary.ai/docs/api/runs/update-run-feedback

https://api.lunary.ai/v1/openapi patch /v1/runs/{id}/feedback



# Update run score
Source: https://docs.lunary.ai/docs/api/runs/update-run-score

https://api.lunary.ai/v1/openapi patch /v1/runs/{id}/score



# Update run tags
Source: https://docs.lunary.ai/docs/api/runs/update-run-tags

https://api.lunary.ai/v1/openapi patch /v1/runs/{id}/tags



# Update run visibility
Source: https://docs.lunary.ai/docs/api/runs/update-run-visibility

https://api.lunary.ai/v1/openapi patch /v1/runs/{id}/visibility



# Create a new template
Source: https://docs.lunary.ai/docs/api/templates/create-a-new-template

https://api.lunary.ai/v1/openapi post /v1/templates
Creates a new template with the provided details.
The template includes a slug, mode, content, and additional configuration options.




# Create a new version
Source: https://docs.lunary.ai/docs/api/templates/create-a-new-version

https://api.lunary.ai/v1/openapi post /v1/templates/{id}/versions
This endpoint allows you to push a new version of a prompt.
You can specify the content, extra parameters, test values, draft status, and notes for the new version.




# Delete a template
Source: https://docs.lunary.ai/docs/api/templates/delete-a-template

https://api.lunary.ai/v1/openapi delete /v1/templates/{id}



# Get a specific template
Source: https://docs.lunary.ai/docs/api/templates/get-a-specific-template

https://api.lunary.ai/v1/openapi get /v1/templates/{id}
Get a specific prompt template and all its versions by its ID.




# Get the latest version
Source: https://docs.lunary.ai/docs/api/templates/get-the-latest-version

https://api.lunary.ai/v1/openapi get /v1/template-versions/latest
This is the most common endpoint you'll use when working with prompt templates.

This route is used by the Lunary SDKs to fetch the latest version of a template before making an LLM call.

This route differs from all the next ones in that:
- it requires only the `slug` parameter to reference a template
- it doesn't require using a Private Key to authenticate the request (Public Key is enough)




# List all templates
Source: https://docs.lunary.ai/docs/api/templates/list-all-templates

https://api.lunary.ai/v1/openapi get /v1/templates
List all the prompt templates in your project, along with their versions.
Useful for usecases where you might want to pre-load all the templates in your application.




# Update a template
Source: https://docs.lunary.ai/docs/api/templates/update-a-template

https://api.lunary.ai/v1/openapi patch /v1/templates/{id}
This endpoint allows you to update the slug and mode of an existing template.
The mode can be either "text" or "openai" (array of chat messages).




# Update a template version
Source: https://docs.lunary.ai/docs/api/templates/update-a-template-version

https://api.lunary.ai/v1/openapi patch /v1/template-versions/{id}



# Test endpoint for playground API testing
Source: https://docs.lunary.ai/docs/api/test/test-endpoint-for-playground-api-testing

https://api.lunary.ai/v1/openapi post /v1/test-endpoint
A public endpoint that echoes back the request data for testing the playground custom API feature



# Test endpoint with authentication check
Source: https://docs.lunary.ai/docs/api/test/test-endpoint-with-authentication-check

https://api.lunary.ai/v1/openapi post /v1/test-endpoint/auth
A test endpoint that validates authentication headers



# Delete a specific user
Source: https://docs.lunary.ai/docs/api/users/delete-a-specific-user

https://api.lunary.ai/v1/openapi delete /v1/external-users/{id}



# Get a specific user
Source: https://docs.lunary.ai/docs/api/users/get-a-specific-user

https://api.lunary.ai/v1/openapi get /v1/external-users/{id}



# List project users
Source: https://docs.lunary.ai/docs/api/users/list-project-users

https://api.lunary.ai/v1/openapi get /v1/external-users
This endpoint retrieves a list of users tracked within the project.
It supports pagination, filtering, and sorting options.




# Create a new view
Source: https://docs.lunary.ai/docs/api/views/create-a-new-view

https://api.lunary.ai/v1/openapi post /v1/views
Creates a new dashboard view with the provided details.



# Delete a view
Source: https://docs.lunary.ai/docs/api/views/delete-a-view

https://api.lunary.ai/v1/openapi delete /v1/views/{id}
Deletes a specific view by its ID.



# Get a specific view
Source: https://docs.lunary.ai/docs/api/views/get-a-specific-view

https://api.lunary.ai/v1/openapi get /v1/views/{id}
Retrieves details of a specific view by its ID.



# List all views
Source: https://docs.lunary.ai/docs/api/views/list-all-views

https://api.lunary.ai/v1/openapi get /v1/views
Retrieves a list of all views for the current project, ordered by most recently updated.



# Update a view
Source: https://docs.lunary.ai/docs/api/views/update-a-view

https://api.lunary.ai/v1/openapi patch /v1/views/{id}
Updates an existing view with the provided details.



# Classification
Source: https://docs.lunary.ai/docs/features/classification



Lunary uses local models to automatically classify your conversations into
topics, languages, sentiments and more.

This functionality is also fully available on the self-hosted versions of Lunary.

<Warning>
  This is currently in beta and not available on the open-source version of
  Lunary.
</Warning>

Full documentation coming soon.


# Chats & Threads
Source: https://docs.lunary.ai/docs/features/conversations



Record and replay chat conversations in your chatbot app. Helps you understand where your chatbot falls short and how to improve it.

Chats integrate seamlessly with traces by reconciliating messages with LLM calls and agents.

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/chat.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=6764f1443a7417b7d752f6484fdcd18f" alt="Feedback tracking" data-og-width="1922" width="1922" data-og-height="1262" height="1262" data-path="media/docs/features/chat.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/chat.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=8e8412742ab184e816f1e3aecf1ce0e9 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/chat.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=6554a7bea616a99b3ff11ff35f1ee270 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/chat.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=7bfcbaf14273aa2bfb7235090580e745 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/chat.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=a0fdd8e227b94724bb60f40d5751f3eb 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/chat.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=36741dbee9f37c12b07109e3d14b131d 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/chat.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=26ab09411248ab88aed1919de9e81ac7 2500w" />

You can record chats in the backend or directly on the frontend if it's easier for you.

## Setup the SDK

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="/docs/integrations/python/installation">
    Learn how to install the Python SDK.
  </Card>

  <Card title="JavaScript" icon="js" href="/docs/integrations/javascript/installation">
    Learn how to install the JS SDK.
  </Card>
</CardGroup>

## Open a thread

Start by opening a thread.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    const thread = lunary.openThread()
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    thread = lunary.open_thread()
    ```
  </Tab>
</Tabs>

You can resume an existing thread by passing an ID from an existing thread.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    // Save `thread.id` somewhere
    const thread = lunary.openThread({
      id: 'your-thread-id'; // Replace with your actual thread ID
    })
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    # Save `thread.id` somewhere
    existing_thread_id = 'your-thread-id'  # Replace with your actual thread ID
    thread = lunary.open_thread(existing_thread_id)
    ```
  </Tab>
</Tabs>

You can also add tags to a thread by passing a object with a `tags` param:

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    const thread = lunary.openThread({
      tags: ['support']
    })
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    thread = lunary.open_thread(existing_thread_id, tags=['support'])
    ```
  </Tab>
</Tabs>

## Track messages

Now you can track messages. The supported roles are `assistant`, `user`, `system`, & `tool`.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    thread.trackMessage({
      role: 'user',
      content: 'Hello, please help me'
    })

    thread.trackMessage({
    role: 'assistant',
    content: 'Hello, how can I help you?'
    })

    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    thread.track_message({
      "role": "user",
      "content": "Hello, please help me"
    })

    thread.track_message({
      "role": "assistant",
      "content": "Hello, how can I help you?"
    })
    ```
  </Tab>
</Tabs>

## Track custom events

You can track custom events that happen within your chatbot. This can include things like:

* opening a document
* clicking a button
* submitting a form
* user activity or inactivity
* other events that you want to track

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    thread.trackEvent("event-name")

    // you can also track additional metadata
    thread.trackEvent("open-document", {
    documentName: "my-document.pdf",
    })

    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    thread.track_event("event-name")

    # you can also use the following optional parameters
    thread.track_event("event-name", user_id="user1", user_props={"email": "hello@test.com"}, metadata={})
    ```
  </Tab>
</Tabs>

## Capture user feedback

Finally, you can track user feedback on bot replies:

The ID is the same as the one returned by `trackMessage`.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    const msgId = thread.trackMessage({
      role: "assistant",
      content: "Hope you like my answers :)"
    })

    lunary.trackFeedback(msgId, { thumb: "up" })

    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    msg_id = thread.track_message({
      "role": "assistant",
      "content": "Hope you like my answers :)"
    })

    lunary.track_feedback(msg_id, { "thumb": "up" })
    ```
  </Tab>
</Tabs>

To remove feedback, pass `null` as the feedback data.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    lunary.trackFeedback(msgId, { thumb: null })
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    lunary.track_feedback(msg_id, { "thumb": None })
    ```
  </Tab>
</Tabs>

## Reconciliate with LLM calls & agents

To take full advantage of Lunary's tracing capabilities, you can reconcile your LLM and agents runs with the messages.

We will automatically reconciliate messages with runs.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    const msgId = thread.trackMessage({ role: "user", content: "Hello!" });

    const res = await openai.chat.completions
      .create({
        model: "gpt-4o",
        temperature: 1,
        messages: [message],
      })
      .setParent(msgId);

    thread.trackMessage({
      role: "assistant",
      content: res.choices[0].message.content,
    });
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    msg_id = thread.track_message({ "role": "user", "content": "Hello!" })

    chat_completion = client.chat.completions.create(
        messages=[message],
        model="gpt-4o",
        parent=msg_id
    )

    thread.track_message(
        {"role": "assistant", "content": chat_completion.choices[0].message.content})
    ```
  </Tab>
</Tabs>

If you're using LangChain or agents behind your chatbot, you can inject the current message id into context as a parent:

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    const msgId = thread.trackMessage({ role: "user", content: "Hello!" });

    // In your backend, inject the message id into the context

    const agent = lunary.wrapAgent(function ChatbotAgent(query) {
      // your custom code...
    });

    await agent("Hello!").setParent(msgId);
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    msg_id = thread.track_message({ "role": "user", "content": "Hello!" })

    # In your backend, inject the message id into the context

    with lunary.parent(msg_id):
        # your custom code...
        pass
    ```
  </Tab>
</Tabs>

Note that *it's safe* to pass the message ID from your frontend to your backend, if you're tracking chats directly on the frontend for example.


# Feedback Tracking
Source: https://docs.lunary.ai/docs/features/feedback



Use feedback tracking for:

* user's reactions to your chatbot's responses directly on the frontend.
* score LLM outputs directly yourself

You can then use this to filter llm calls and fine-tune your own models based on the data.

Feedback tracking can be done in the backend or directly on the frontend if it's easier for you.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    const msgId = thread.trackMessage({
      role: 'assistant',
      content: 'Hello! How can I help you?',
    })

    lunary.trackFeedback(msgId, { thumb: 'up' })
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    msg_id = thread.track_message({
      "role": "assistant",
      "content": "Hello! How can I help you?"
    })

    lunary.track_feedback(msg_id, { "thumb": "up" })
    ```
  </Tab>
</Tabs>

## Example of a React Feedback component

You can also use the feedback method to track user reactions to your chatbot's responses directly on the frontend.

```jsx  theme={null}
<Button onClick={() => lunary.trackFeedback(message.id, { thumb: "up" })}>
  👍
</Button>
```

The `trackFeedback` method takes two arguments:

* `runId`: the ID of the message or run you want to track the feedback on.
* `feedback`: an object containing the feedback data. You can use any key/value pair you want.

## Feedback data

You can send any feedback data you want, as long as it's a valid JSON object.

We recommend using the following keys to ensure that data is displayed correctly in the dashboard.

| Key       | Value            | Preview                    |
| --------- | ---------------- | -------------------------- |
| `thumb`   | `up` or `down`   | 👍 / 👎                    |
| `comment` | arbitrary string | eg. "This is not correct." |

## Removing feedback

To remove feedback, simply pass `null` as the feedback data.

```js  theme={null}
lunary.trackFeedback(message.id, { thumb: null })
```


# Observability
Source: https://docs.lunary.ai/docs/features/observability



Lunary has powerful observability features that lets you record and analyze your LLM calls.

There are 3 main observability features: analytics, logs and traces.

Analytics and logs are automatically captured as soon as you integrate our SDK.

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="/docs/integrations/python/installation">
    Learn how to install the Python SDK.
  </Card>

  <Card title="JavaScript" icon="js" href="/docs/integrations/javascript/installation">
    Learn how to install the JS SDK.
  </Card>

  <Card title="LangChain" icon="box" href="/docs/integrations/langchain">
    Learn how to integrate with LangChain.
  </Card>
</CardGroup>

## Analytics

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/analytics.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=e2fe9a51b243ebbbc78cb099f6ca374b" alt="Analytics" data-og-width="2054" width="2054" data-og-height="1386" height="1386" data-path="media/docs/features/analytics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/analytics.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=7324ac1ead4d2aa84c4dfb93322927aa 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/analytics.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=85e881f6669fb1e0160f7d3fa5f87ab0 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/analytics.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=c7ac776dd57323254bebfe750cbfb185 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/analytics.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=ce35f69869dca8ad08f6a108b58f2b72 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/analytics.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=c933778159601e587f65523f9239635a 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/analytics.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=87b888fc4865e62b4012febfbe7b3d31 2500w" />

The following metrics are currently automatically captured:

| Metric         | Description                                          |
| -------------- | ---------------------------------------------------- |
| 💰 **Costs**   | Costs incurred by your LLM models                    |
| 📊 **Usage**   | Number of LLM calls made & tokens used               |
| ⏱️ **Latency** | Average latency of LLM calls and agents              |
| ❗ **Errors**   | Number of errors encountered by LLM calls and agents |
| 👥 **Users**   | Usage over time of your top users                    |

## Logs

Lunary allows you to log and inspect your LLM requests and responses.

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/logging.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=efe41ea1e2ea2000c706dc95f66697bb" alt="Logging" data-og-width="2488" width="2488" data-og-height="1498" height="1498" data-path="media/docs/features/logging.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/logging.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=8c04238386813dc1740d108746196e22 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/logging.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=535499789e0fae9eccb55804a05cb509 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/logging.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=10decf25b3b7422830ca7d723d573efb 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/logging.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=1ca894ce736fb0345d36fadf1b1b7cdd 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/logging.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=f832a203689a8eee91d50d24eb8da28c 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/logging.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=a317fc64e1d3d64895fc0d3516aef7a2 2500w" />

Logging is automatic as soon as you integrate our SDK.

## Tracing

Tracing is helpful to debug more complex AI agents and troubleshoot issues.

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/traces.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=3dc5d90a9d39a205179166eafda191de" alt="Feedback tracking" data-og-width="2520" width="2520" data-og-height="1652" height="1652" data-path="media/docs/features/traces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/traces.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=9b9e1111327b733dc94ce53a45f94aa4 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/traces.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=f7e6437612daabd2d59f65ed21af59f8 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/traces.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=090f8499d49e48e7e0691f4ebfcb9dd8 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/traces.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=4d0fc7de0dbd19e51ba092de97fbce78 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/traces.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=7a23d48481791e272c5b9f028feb5a2c 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/traces.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=2f3df53085c0ac478d0f1dee4392ac17 2500w" />

The easiest way to get started with traces is to use our utility wrappers to automatically track your agents and tools.

### Wrapping Agents

By wrapping an agent, input, outputs and errors are automatically tracked.

Any query ran inside the agent will be tied to the agent.

<Tabs>
  <Tab title="Javascript">
    <Alert title="Agents and tools names" icon={<IconRobot />}>
      Agents & tools are automatically named from the wrapped function's name. You can change the name by passing a 2nd argument `{ name: "custom-name" }` to the `wrapAgent` and `wrapTool` methods.
    </Alert>

    ```js  theme={null}
    // By wrapping your agent's function input, outputs and errors are automatically tracked.
    // Sub tools and logs will be tied to the correct agent.
    const myAgent = lunary.wrapAgent(async function MyAgent(input) {
      // Your agent custom logic
      // ...
    })

    await myAgent("Hello, how are you?")
    ```

    If you prefer to use anonymous functions, make sure to pass a name as a 2nd argument to the `wrapAgent` and `wrapTool` methods.

    ```js  theme={null}
    const myAgent = lunary.wrapAgent(
      (input) => {
        // Your agent custom logic
        // ...
      },
      { name: "MyAgent" }
    )
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    import lunary

    @lunary.agent()
    def MyAgent(input): # Your agent custom logic # ...
      pass
    ```
  </Tab>
</Tabs>

### Wrapping Chains

Chains are sequences of operations that combine multiple LLM calls, tools, or processing steps into a single workflow. By wrapping chains, you can track the entire sequence of operations as a single unit while still maintaining visibility into each individual step.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    const chain = lunary.wrapChain(async function Chain(input) {
      // Your chain custom logic
      // Call LLM
      // Invoke tool
      // etc...
    })

    await chain('Hello, how are you?')  
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    @lunary.chain()
    def Chain(input): # Your chain custom logic # ...
      pass
    ```
  </Tab>
</Tabs>

### Wrapping Tools

If your agents use tools, you can wrap them as well to track them.

If a wrapped tool is executed inside a wrapped agent, the tool will be automatically tied to the agent without the need to manually reconcialiate them.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    // By wrapping the tool, input, outputs and errors are automatically tracked.
    // And sub tools / logs will be tied to the correct agent.
    const calculator = lunary.wrapTool(async function Calculator(input) {
      // Your custom logic
      // ...
    })

    await calculator('1 + 2')
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    import lunary

    @lunary.tool(name='MySuperTool')
    def MyTool(input): # Your tool custom logic # ...
      pass
    ```
  </Tab>
</Tabs>


# Product Analytics
Source: https://docs.lunary.ai/docs/features/product-analytics



We're putting the finishing touches on our Product Analytics guide. Check back soon for the full walkthrough.

In the meantime, explore [User Tracking](/features/users) to see how teams are already learning from their user data.


# Prompt Playground
Source: https://docs.lunary.ai/docs/features/prompt-playground



The Prompt Playground is an interactive environment for testing and refining your prompts. It provides a powerful interface to experiment with different prompt variations, test against various models, and even run prompts against custom API endpoints.

## Overview

The Prompt Playground allows you to:

* Test prompts with different LLM providers (OpenAI, Anthropic, etc.)
* Compare outputs across multiple models
* Experiment with parameters like temperature and max tokens
* Test prompts against your own custom API endpoints
* Save and collaborate on prompt experiments with team members
* Create draft versions without affecting production (RBAC ensures only authorized users can deploy)

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/1.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=06c8964263612f54c373da2d7faac05c" alt="Image 1" data-og-width="3054" width="3054" data-og-height="1982" height="1982" data-path="media/docs/prompt-playground/1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/1.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=332600b3c150836e02da4f6a060a057d 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/1.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=df7e3ded9643512c262ab9ef1f9a77a4 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/1.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=46e0b943de4e2c04b7cbfa5daa617455 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/1.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=dec491fecf6d7853657b0a1a6f6bb8b4 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/1.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=44e4fcff12c456267fa93a1b234ecb94 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/1.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=974b970ba4b8e788c3ca5ea769f98b4a 2500w" />

## Variables and Dynamic Content

The Playground supports dynamic variables in your prompts:

1. Define variables using double curly braces: `{{variable_name}}`
2. Enter test values in the Variables section
3. See how different variable values affect the output

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/variables.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=5975e0dd9e1cc314fd2b664a62c86b47" alt="Screenshot: Using variables in prompts" data-og-width="1698" width="1698" data-og-height="426" height="426" data-path="media/docs/prompt-playground/variables.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/variables.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=eb57b5746e4bd7b8f7d10fe5114f0c8e 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/variables.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=fe63c7ee001116b038831e79aae9a9de 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/variables.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=5dbf641249bd1c456faeb469f9759a82 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/variables.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=037c401154b0664d32f90d9fffa1cbc8 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/variables.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=9b50613e9a7d7a0fea13089dddf484ba 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/variables.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=a90e06c9418dedf860f0fced270bf183 2500w" />

## Saving and Collaboration

The Playground supports team collaboration with built-in versioning and role-based access control:

### Creating Draft Versions

1. Click "Save as Draft" to save your experiments without affecting production
2. Add version notes to document your changes and findings
3. Share the draft with team members for review and feedback

### Collaboration Features

* **Draft Sharing**: Team members can view and test your draft prompts
* **Notepad**: Leave feedback on specific prompt versions via the notepad
* **Role-Based Access**:
  * Developers and prompt engineers can create and edit drafts
  * Only authorized users (with deployment permissions) can promote drafts to production
  * Viewers can test prompts but cannot modify them

## Testing with Custom Endpoints

One of the most powerful features of the Prompt Playground is the ability to test prompts against your own custom API endpoints. This is particularly useful for:

* **RAG (Retrieval-Augmented Generation) systems**
* **Custom AI applications** with proprietary logic
* **API wrappers** that combine multiple AI services
* **Complex systems** that include more components than just an LLM

### Setting Up Custom Endpoints

To configure a custom endpoint:

1. Toggle the **Run Mode** from "Model Provider" to "Custom Endpoint"
2. Click "Configure Endpoints" to set up your API endpoints

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/2.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=b9cd07cf9cc7d003edd0636eb3a7a3f9" alt="Screenshot: Switching to Custom Endpoint mode" data-og-width="794" width="794" data-og-height="1058" height="1058" data-path="media/docs/prompt-playground/2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/2.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=5e0340b924f3b973e52a2e96bc5e47e7 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/2.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=5612f00f6c49c579460f9959718d0b85 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/2.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=cd6cde89445f9d0943b3fbe06b9e11b4 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/2.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=da4d4eede109529edda519dfd8a61073 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/2.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=043567f03424f31eabf38cfd04726ffb 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/2.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=cc3f31de711296e4de9e9e66df647913 2500w" />

### Endpoint Configuration

When creating an endpoint, you'll need to provide:

* **Name**: A descriptive name for your endpoint
* **URL**: The full URL of your API endpoint
* **Authentication**: Choose from:
  * Bearer Token (for OAuth/JWT)
  * API Key (with custom header name)
  * Basic Authentication
  * No authentication
* **Custom Headers**: Additional headers to include in requests
* **Default Payload**: Base payload that will be merged with prompt data

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/3.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=9be1c88bc63d566f2a8fe17feca3d471" alt="Screenshot: Endpoint configuration dialog" data-og-width="3056" width="3056" data-og-height="1972" height="1972" data-path="media/docs/prompt-playground/3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/3.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=e22b3fe3e7b2af5bc8208512413a0937 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/3.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=cdf7ae8c4d0706f29f8aadb9b6f3d575 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/3.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=f3f746f4663c0ea0e1bd1e540ac4a1bd 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/3.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=65984dd0e940dc53573fb88e48f97925 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/3.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=a8268e4505b65af33f1742d372be1c55 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/3.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=66e4b842d71abfb7e786b44e69d37981 2500w" />

### Request Format

When you run a prompt against a custom endpoint, Lunary sends an HTTP POST request with the following JSON payload:

```json  theme={null}
{
  "messages": [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "What is the weather like?"}
  ],
  "model_params": {
    "temperature": 0.7,
    "max_tokens": 1000,
    "model": "gpt-4"
  },
  "variables": {
    "location": "San Francisco",
    "user_id": "12345"
  }
  // custom payload data will be merged here 
  "custom_data": {
    "example_key": "example_value"
  }
}
```

Your endpoint should process this request and return a response. Lunary supports various response formats:

* Simple text responses
* OpenAI-compatible message arrays
* Custom JSON structures

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/4.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=d42513dccca9c8ad838bb7bc28308273" alt="Screenshot: Example request payload" data-og-width="3058" width="3058" data-og-height="1984" height="1984" data-path="media/docs/prompt-playground/4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/4.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=d742a7196cd9d21d178c98d9ccf1c12d 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/4.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=ee5a62949e57777db83e66299a732f35 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/4.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=d0de4c59bea4bc819112ce9465ee541d 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/4.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=f59f56fe7b082a317f66413f66d55259 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/4.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=990ac01bde2869b2bc2a73625c8afd2f 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/4.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=e5f21f5e86f9b288fe10780c48d451c3 2500w" />

### Use Case Examples

#### RAG System Integration

Test how your prompts work with your retrieval-augmented generation system:

```javascript  theme={null}
// Example RAG endpoint that enriches prompts with context
app.post('/api/rag-chat', async (req, res) => {
  const { content, variables } = req.body;
  
  // Extract the user's query
  const userQuery = content[content.length - 1].content;
  
  // Search your knowledge base
  const relevantDocs = await vectorDB.search(userQuery, {
    filter: { user_id: variables.user_id },
    limit: 5
  });
  
  // Augment the prompt with retrieved context
  const augmentedContent = [
    ...content.slice(0, -1),
    {
      role: "system",
      content: `Relevant context:\n${relevantDocs.map(d => d.text).join('\n\n')}`
    },
    content[content.length - 1]
  ];
  
  // Generate response with your LLM
  const response = await llm.generate({
    ...req.body,
    content: augmentedContent
  });
  
  res.json({ content: response.text });
});
```

#### Custom Agent Testing

Test prompts against AI agents with tool access or custom logic:

```python  theme={null}
# Example agent endpoint with tool usage
@app.post("/api/agent")
async def agent_endpoint(request: dict):
    prompt = request["content"]
    variables = request["variables"]
    
    # Parse intent and determine required tools
    intent = parse_intent(prompt[-1]["content"])
    
    if intent.requires_search:
        search_results = await web_search(intent.query)
        context = format_search_results(search_results)
        prompt.append({"role": "system", "content": f"Search results: {context}"})
    
    if intent.requires_calculation:
        calc_result = await calculator(intent.expression)
        prompt.append({"role": "system", "content": f"Calculation: {calc_result}"})
    
    # Generate final response
    response = await generate_response(prompt, variables)
    
    return {"content": response, "tools_used": intent.tools}
```


# Prompt Templates
Source: https://docs.lunary.ai/docs/features/prompts



Prompt templates are a way to store, version and collaborate on prompts.

Developers use prompt templates to:

* clean up their source code
* make edits to prompts without re-deploying code
* collaborate with non-technical teammates
* A/B test prompts

## Creating a template

You can create a prompt template by clicking on the "Create prompt template" button in the Prompts section of the dashboard.

## Usage with OpenAI

You can use templates seamlessly with OpenAI's API with our SDKs.

This will make sure the tracking of the prompt is done automatically.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    import OpenAI from "openai";
    import lunary from "lunary"
    import { monitorOpenAI } from "lunary/openai";

    // Make sure your OpenAI instance is wrapped with `monitorOpenAI`
    const openai = monitorOpenAI(new OpenAI())

    const template = await lunary.renderTemplate("template-slug", {
    name: "John", // Inject variables
    })

    const result = await openai.chat.completions.create(template)

    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    import lunary
    from openai import OpenAI

    client = OpenAI()

    # Make sure your OpenAI instance is monitored
    lunary.monitor(client)

    template = lunary.render_template("template-slug", {
      "name": "John", # Inject variables
    })

    result = client.chat.completions.create(**template)
    ```
  </Tab>
</Tabs>

## Usage with LangChain's templates

You can pull templates in the LangChain format and use them directly as PromptTemplate and ChatPromptTemplate classes.

Example with simple text template:

<Tabs>
  <Tab title="Javascript">
    The `getLangChainTemplate` method returns a `PromptTemplate` object for simple templates, which can be used directly in chains or to format prompts.

    ```js  theme={null}
    import { getLangChainTemplate } from "lunary/langchain";

    const prompt = await getLangChainTemplate("icecream-prompt");

    const promptValue = await prompt.invoke({ topic: "ice cream" });

    console.log(promptValue);
    ```
  </Tab>

  <Tab title="Python">
    The `get_langchain_template` method returns a `PromptTemplate` object for simple templates, which can be used directly in chains or to format prompts.

    ```py  theme={null}
    import lunary

    template = lunary.get_langchain_template("my-template")

    prompt = template.format(question="What is the capital of France?")
    ```
  </Tab>
</Tabs>

Example with a Chat template (ChatPromptTemplate):

<Tabs>
  <Tab title="Javascript">
    The `getLangChainTemplate` function directly returns a `ChatPromptTemplate` object for chat messages templates, which can be used to format messages.

    ```js  theme={null}
    import { getLangChainTemplate } from "lunary/langchain";

    const prompt = await getLangChainTemplate("context-prompt");

    const promptValue = await prompt.invoke({ topic: "ice cream" });

    console.log(promptValue);
    /**
    ChatPromptValue {
      messages: [
        HumanMessage {
          content: 'Tell me a short joke about ice cream',
          name: undefined,
          additional_kwargs: {}
        }
      ]
    }
    */
    ```
  </Tab>

  <Tab title="Python">
    The `get_langchain_template` method returns a `ChatPromptTemplate` object for chat messages templates, which can be directly in chains or to format messages.

    ```py  theme={null}
    template = lunary.get_langchain_template("my-template")

    messages = lc_template.format_messages(question="What is the capital of France?")
    ```
  </Tab>
</Tabs>

## Manual LangChain Usage with LLM Classes

Using with LangChain LLM Classes is similar to using with OpenAI, but requires you to format the messages in the LangChain format as well as pass the template id in the metadata.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    Coming soon
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    from langchain_openai import ChatOpenAI
    from langchain_community.adapters.openai import convert_openai_messages
    from lunary import render_template, LunaryCallbackHandler

    template = render_template("template-slug", {
    "name": "John", # Inject variables
    })

    chat_model = ChatOpenAI(
    model=template["model"],
    metadata={
    "templateId": template["templateId"] # Optional: this allows to reconcile the logs with the template
    },

    # add any other parameters here...

    temperature=template["temperature"],
    callbacks=[LunaryCallbackHandler()]
    )

    # Convert messages to LangChain format

    messages = convert_openai_messages(template["messages"])

    result = chat_model.invoke(messages)

    ```
  </Tab>
</Tabs>

## Manual usage

You can also use templates manually with any LLM API by accessing the relevant fields (returned in OpenAI's format).

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    import lunary from "lunary"

    const {
      messages,
      model,
      temperature,
      max_tokens
    } = await lunary.renderTemplate("template-slug", {
      name: "John", // Inject variables
    })


    // ... use the fields like you want

    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    import lunary

    template = lunary.render_template("template-slug", {
    "name": "John", # Inject variables
    })

    messages = template["messages"]
    model = template["model"]
    temperature = template["temperature"]
    max_tokens = template["max_tokens"]

    # ... use the fields like you want

    ```
  </Tab>
</Tabs>

## Testing Prompts

The Prompt Playground provides a powerful interactive environment for testing and refining your prompts. You can experiment with different models, parameters, and even test against custom API endpoints.

[Learn more about the Prompt Playground →](/docs/features/prompt-playground)


# Tagging
Source: https://docs.lunary.ai/docs/features/tags



Tags allow you to label queries and completions.

This is useful to further segment your data. For example, you can label all the queries that are related to a specific feature or a specific company.

Later on, this can also be useful for creating fine-tune datasets.

<Steps>
  <Step n="1" title="Setup the SDK">
    <CardGroup cols={2}>
      <Card title="Python" icon="python" href="/docs/integrations/python/installation">
        Learn how to install the Python SDK.
      </Card>

      <Card title="JavaScript" icon="js" href="/docs/integrations/javascript/installation">
        Learn how to install the JS SDK.
      </Card>
    </CardGroup>
  </Step>

  <Step n="2" title="Simplest: Identify OpenAI calls">
    The easiest way to get started adding tags is to send them when doing your OpenAI API calls.

    <Tabs>
      <Tab title="Javascript">
        ```js  theme={null}
        const res = await openai.chat.completions.create({
          model: "gpt-4o",
          messages: [{ role: "user", content: "Hello" }],
          tags: ["some-tag"]
        })
        ```
      </Tab>

      <Tab title="Python">
        ```py  theme={null}
        chat_completion = client.chat.completions.create(
          messages=[{"role": "user", "content": "Say this is a test"}],
          model="gpt-4o",
          tags=["some-tag"],
        )
        ```
      </Tab>
    </Tabs>

    If you're using LangChain, you can similarly pass the tags on any LangChain object.

    <Tabs>
      <Tab title="Javascript">
        ```js  theme={null}
        const chat = new ChatOpenAI({
          callbacks: [new LunaryHandler()],
        });

        const res = await chat.call([new HumanMessage("Hello!")], {
        tags: ["some-tag"],
        });

        ```
      </Tab>

      <Tab title="Python">
        ```py  theme={null}
        handler = LunaryCallbackHandler()

        chat = ChatOpenAI(
          callbacks=[handler],
          tags=["some-tag"],
        )
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step n="3" title="Advanced: Inject tag into context">
    You can also inject tags into the context of your code. This is useful if you want to tag all the queries that are related to a specific feature or a specific company.

    <Tabs>
      <Tab title="Javascript">
        ```js  theme={null}
        Coming soon
        ```
      </Tab>

      <Tab title="Python">
        ```py  theme={null}
        import lunary
        # Method 2: everything inside the with statement will have tags2 and tags3
        with lunary.tags(["tag2", "tag3"]):
          my_agent()
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>


# User Tracking
Source: https://docs.lunary.ai/docs/features/users



Identify your users, track their cost, conversations and more.

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/users.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=d933944893652c32975b66fa049e19dd" alt="User tracking" data-og-width="1364" width="1364" data-og-height="404" height="404" data-path="media/docs/features/users.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/users.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=2d4571a9de34629899572cd8e28d19a4 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/users.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=57c55c90863b1c7ca4121989ae1f65c7 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/users.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=712c73f55b5747ee7cbae3d4b0b107df 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/users.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=0059266523892d1d8cbe090c882b0138 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/users.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=8f1720eecb018c94e023e7d9227076a6 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/users.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=953d9997bcd53a9d4896bbe25baae419 2500w" />

The strict minimum to enable user tracking is to report a `userId`, however you can report any property you'd like such as an email or name using an `userProps` object.

## Tracking users with the backend SDK

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="/docs/integrations/python/installation">
    Learn how to install the Python SDK.
  </Card>

  <Card title="JavaScript" icon="js" href="/docs/integrations/javascript/installation">
    Learn how to install the JS SDK.
  </Card>
</CardGroup>

### Identify OpenAI calls

The easiest way to get started tracking users is to send user data with your OpenAI API call.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    const res = await openai.chat.completions.create({
      model: "gpt-4o",
      messages: [{ role: "user", content: "Hello" }],
      user: "user123",
      userProps: { name: "John" },
    })
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    chat_completion = client.chat.completions.create(
      model="gpt-4o", 
      messages=[{"role": "user", "content": "Hello"}],
      user_id="user123",
      user_props={ "name": "John" }
    )
    ```
  </Tab>
</Tabs>

If you're using LangChain, you can similarly pass user data as metadata.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    const chat = new ChatOpenAI({
      callbacks: [new LunaryHandler()],
    });

    const res = await chat.call([new HumanMessage("Hello!")], {
    metadata: {
    userId: "123",
    userProps: { name: "John" },
    },
    });

    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    handler = LunaryCallbackHandler()

    chat = ChatOpenAI(
      callbacks=[handler],
      metadata={
        "user_id": "user123"
      },  # Assigning user ids to models in the metadata
    )
    ```
  </Tab>
</Tabs>

### Advanced: Inject user into context

When tracking traces, you can inject user data into the context using the `identify` methods. This will cascade down to all the child runs.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    async function TranslatorAgent(input) {
      // Some AI queries
      // Everything done in this context will be tracked with the user
    }

    // Wrap the agent with the monitor
    const translate = lunary.wrapAgent(TranslatorAgent)

    // Using identify to inject the user into the context
    const res = await translate(`Hello, what's your name?`)
    .identify("user123", { email: "email@example.org" })

    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    import lunary

    def my_agent():
      # Some AI queries
      # Everything done in this context will be tracked with the user

    def main():
      # Using identify to inject the user into the context
      with lunary.identify('user123', user_props={"email": "email@example.org"}):
        my_agent()
    ```
  </Tab>
</Tabs>

## Identifying users on the frontend

If you are [tracking chat messages](/docs/features/chats) or [feedback](/docs/features/feedback) on the frontend, you can use the `identify` method to identify the user there.

```js  theme={null}
lunary.identify("user123", {
  email: "test@example.org",
});
```

## Identifying Threads

If you are using [threads](/docs/features/threads) to track conversations, you can pass `userId` and `userProps` to the `openThread` method.

```js  theme={null}
const thread = await lunary.openThread({
  userId: "user123",
  userProps: { name: "John" },
});
```

## User Properties

While you can track any property you'd like, we recommend using the following ones:

| Property | Description                             |
| -------- | --------------------------------------- |
| `name`   | Name of the user                        |
| `email`  | Email of the user                       |
| `avatar` | URL to an avatar                        |
| `group`  | Group or company ID the user belongs to |


# Getting Started
Source: https://docs.lunary.ai/docs/get-started/index



## Welcome

**Lunary** is an open-source platform for developers of AI chatbots and other LLM-powered applications.

<CardGroup cols={2}>
  <Card title="Observability" icon="chart-area" href="/docs/features/observability">
    Monitor and debug your LLM calls and agents.
  </Card>

  <Card title="Chats" icon="messages" href="/docs/features/conversations">
    Track chatbot conversations and user feedback.
  </Card>

  <Card title="Prompts" icon="brackets-curly" href="/docs/features/prompts">
    Collaborate on prompt templates with versioning.
  </Card>

  <Card title="Classification" icon="tags" href="/docs/features/classification">
    Setup topics classification for your chats.
  </Card>
</CardGroup>

## Getting started

The first thing you'll need to get started is to sign up and get a tracking ID.

<TrackingIdButton />

<Card title="Open Lunary" href="https://app.lunary.ai/signupp" horizontal="true" />

## Pick an integration

We support integrating with the most popular AI libraries, with more in the work.

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="/docs/integrations/python/installation">
    Learn how to integrate with Python.
  </Card>

  <Card title="JavaScript" icon="js" href="/docs/integrations/javascript/installation">
    Learn how to integrate with JavaScript.
  </Card>

  <Card title="LangChain" icon="box" href="/docs/integrations/langchain">
    Learn how to integrate with LangChain.
  </Card>
</CardGroup>


# Azure OpenAI integration
Source: https://docs.lunary.ai/docs/integrations/azure-openai



Our Python SDK includes automatic integration with Azure OpenAI.

<Steps>
  <Step n="1" title="Setup the SDK">
    ```bash  theme={null}
    pip install openai lunary
    ```
  </Step>

  <Step n="2" title="Monitor AzureOpenAI">
    With our SDKs, tracking AzureOpenAI calls is super simple.

    ```py  theme={null}
    import os
    from openai import AzureOpenAI
    import lunary 

    API_VERSION = os.environ.get("OPENAI_API_VERSION")
    API_KEY = os.environ.get("AZURE_OPENAI_API_KEY")
    AZURE_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT")
    RESOURCE_NAME = os.environ.get("AZURE_OPENAI_RESOURCE_NAME")


    client = AzureOpenAI(
        api_version=API_VERSION,
        azure_endpoint=AZURE_ENDPOINT,
        api_key=API_KEY
    )
    lunary.monitor(client)

    completion = client.chat.completions.create(
        model=RESOURCE_NAME,
        messages=[
            {
                "role": "user",
                "content": "How do I output all files in a directory using Python?",
            },
        ],
    )
    print(completion.to_json())


    ```
  </Step>
</Steps>


# Step-by-Step Guide : Sending Events via the Lunary API
Source: https://docs.lunary.ai/docs/integrations/custom



If you'd like to report data from a platform not supported by our SDKs, this page is for you.

## Getting Started

The endpoint for sending events to the Lunary Cloud API is:

```txt  theme={null}
https://api.lunary.ai/v1/runs/ingest
```

You can find the full API documentation [here](/docs/api/introduction).

You will need your project's Public Key to authenticate requests (pass this as the Bearer token in the Authorization header).

## Step 1: Sending LLM data

### Start Event

At a minimum, you will need an ID, the model name, and the input data to send a start event.

While the ID can be any unique identifier, we recommend using a random UUID.

<Note>
  Make sure to replace the IDs with unique values, otherwise the ingestion will
  be rejected.
</Note>

Using `curl`, here's an example:

```json  theme={null}
curl -X POST "https://api.lunary.ai/v1/runs/ingest" \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer 0x0" \
 -d '{
  "events": [
    {
      "type": "llm",
      "event": "start",
      "runId": "replace-with-unique-id",
      "name": "gpt-4o",
      "timestamp": "2022-01-01T00:00:00Z",
      "input": [{"role": "user", "text": "Hello world!"}]
    }
  ]
}'
```

### End Event

Once your LLM call succeeds, you need to send an `end` event with the output data. Here’s an example:

```json  theme={null}
curl -X POST "https://api.lunary.ai/v1/runs/ingest" \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer 0x0" \
 -d '{
  "events": [
    {
      "type": "llm",
      "event": "end",
      "runId": "some-unique-id",
      "name": "gpt-4o",
      "timestamp": "2022-01-01T00:00:10Z",
      "output": [{"role": "assistant", "text": "Hello. How are you?"}],
      "tags": ["tag1"]
    }
  ]
}'
```

You should now see a completed run in the Lunary UI:

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/basic-llm.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=54125bd388ef74220ed0cde9a8ca41b3" alt="Run in Lunary UI" data-og-width="1746" width="1746" data-og-height="146" height="146" data-path="media/docs/custom-integration/basic-llm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/basic-llm.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=0b2dbf24ee152dba673fb3dfb6408556 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/basic-llm.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=017be77cf556f00201b8f8e8aa8325e1 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/basic-llm.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=d49ddebe92082d25970b2cf23d39cd1b 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/basic-llm.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=f2737b004ca377c6d9dd8ec45eec9364 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/basic-llm.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=e2633465bbc211cbe750fbca54ce245e 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/basic-llm.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=0e9adfb14f17534113ebca816ee1e655 2500w" />

<Note> These can be sent in the same batch or as separate requests.</Note>

### Additional Data

You can report additional LLM data in the `extra` object, such as `temperature`, `max_tokens`, and `tools`. Similarly, arbitrary metadata can be passed in the `metadata` object, user information can be reported in the `userId` and `userProps` fields, and tags can be added to the event.

Example with additional data:

```json  theme={null}
curl -X POST "https://api.lunary.ai/v1/runs/ingest" \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer 0x0" \
 -d '{
  "events": [
    {
      "type": "llm",
      "event": "start",
      "runId": "some-unique-id",
      "name": "gpt-4o",
      "timestamp": "2022-01-01T00:00:00Z",
      "input": [{"role": "user", "content": "Hello!"}],
      "userId": "some-internal-id",
      "tokensUsage": {
        "completion": 100,
        "prompt": 50
      },
      "userProps": {
        "name": "Jane Doe",
        "email": "jane@example.org"
      },
      "extra": {
        "temperature": 0.5,
        "max_tokens": 1000,
        "tools": []
      },
      "metadata": {
        "organizationId": "org-123",
      },
      "tags": ["tag1"]
    }
  ]
}'
```

You can also add a `templateVersionId` field to reference the template version used in the call.

### Reporting errors

If an error occurs during the LLM call, you can report it in the `error` field using an `error` event.

```json  theme={null}
curl -X POST "https://api.lunary.ai/v1/runs/ingest" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer 0x0" \
  -d '{
    "events": [
      {
        "type": "llm",
        "event": "error",
        "runId": "some-unique-id",
        "timestamp": "2022-01-01T00:00:00Z",
        "error": {
          "message": "Model failed to generate response",
          "stack": "Error: Model failed to generate response\n    at ...",
        }
      }
    ]
  }'
```

### Attaching feedback

If you have feedback from the user, you can attach it to the event using the `feedback` field and a `feedback` event.

```json  theme={null}
curl -X POST "https://api.lunary.ai/v1/runs/ingest" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer 0x0" \
  -d '{
    "events": [
      {
        "event": "feedback",
        "runId": "some-unique-id",
        "feedback": {
          "comment": "Great response!",
          "thumb": "up"
        },
        "overwrite": false
      }
    ]
  }'
```

*Note that feedback might take up to 1 minute to be reflected in the UI.*

## Step 2: Basic Traces

If you have multiple LLM calls in a single action, you can use the `parentRunId` field to link them together, under an "agent" run.

```json  theme={null}
curl -X POST "https://api.lunary.ai/v1/runs/ingest" \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer 0x0" \
 -d '{
  "events": [
    {
      "type": "agent",
      "event": "start",
      "runId": "agent-run-id",
      "name": "agent-007",
      "input": "Hello world!",
      "timestamp": "2024-07-16T00:00:00Z"
    },
    {
      "type": "llm",
      "event": "start",
      "runId": "llm-run-id",
      "parentRunId": "agent-run-id",
      "name": "gpt-4o",
      "timestamp": "2024-07-16T00:00:05Z",
      "input": [{"role": "user", "content": "The user had a question: Hello world!"}]
    },
    {
      "type": "llm",
      "event": "end",
      "runId": "llm-run-id",
      "parentRunId": "agent-run-id",
      "name": "gpt-4o",
      "timestamp": "2024-07-16T00:00:10Z",
      "output": [{"role": "assistant", "content": "Hello. How are you?"}]
    },
    {
      "type": "agent",
      "event": "end",
      "runId": "agent-run-id",
      "name": "agent-007",
      "output": "Hello. How are you?",
      "timestamp": "2024-07-16T00:00:15Z"
    }
  ]
}'
```

Now, if you head to the Traces section in the Lunary UI, you should see the new trace, with the agent and LLM runs nested together:

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/basic-trace.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=9e31e17db37a01a6d74675e0e3e50a75" alt="Traces in Lunary UI" data-og-width="1276" width="1276" data-og-height="332" height="332" data-path="media/docs/custom-integration/basic-trace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/basic-trace.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=1e44db91db9180620b43af325fee5015 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/basic-trace.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=3ca52fbd5018c74547dd6fb24adce0c0 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/basic-trace.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=4f3eb87186e46899346261a5c8fba3ab 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/basic-trace.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=8047364432f55b719dbf14dec3c9059b 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/basic-trace.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=a47cc15dd20f529000018d344273ea1c 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/basic-trace.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=068cadb3b792bbc905abaf9ee718e804 2500w" />

Similarly, you can nest multiple levels of agents together, and report other run types such as `tool` and `embed`.

<Note>
  {" "}

  User and feedback data cascades down between parent and child runs.
</Note>

## Step 3: Advanced Traces (with tools and threads)

A typical user/agent flow might look like this:

1. The user asks a question.
2. Your system invokes an agent to handle the request.
3. The agent makes an LLM call and asks a tool to be executed.
4. The tool is executed.
5. Another LLM call is made with the tool's output.
6. The final answer is returned to the user.

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/agent-flow.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=e378b21235007eb1c2b0cd0676ff1a7f" alt="trace" data-og-width="1254" width="1254" data-og-height="466" height="466" data-path="media/docs/custom-integration/agent-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/agent-flow.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=3b67293fdaf86dc05ebc5dd270192fae 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/agent-flow.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=37a5fcbd3790aaa039d78f9c2476a54f 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/agent-flow.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=fd67dc57c3f80dd88a59ae485b55a99e 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/agent-flow.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=8f76b29ba883121e42a28c50cf5904d8 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/agent-flow.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=60265db5d4044de160062f75e66af181 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/agent-flow.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=50c457be2f02f089d36a7a273ec89c35 2500w" />

Steps 2-5 could repeat multiple times.

Here's what that would look like in terms of events:

#### 1. The user asks a question

Capture the user message using a `thread.chat` event and the `message` field.

Note that we must pass a `parentRunId` here, which is the unique identifier of the current thread. Thread runs are opened and closed automatically, you don't need to explicitly start or end them.

For a `chat` event, a different `parentRunId` means a different conversation thread with the user.

```json  theme={null}
{
  "type": "thread",
  "event": "chat",
  "runId": "chat-run-id",
  "parentRunId": "thread-run-id",
  "timestamp": "2024-07-16T00:00:00Z",
  "message": { "role": "user", "content": "What's the weather in Boston?" }
}
```

#### 2. Invoke an Agent to handle the request.

While this is optional (as we already have a parent `chat` run), it's good practice to open an `agent` run to encapsulate the agent's logic.
This also allows us to see the isolated's agent execution in the Traces tab of the Lunary UI.

```json  theme={null}
{
  "type": "agent",
  "event": "start",
  "runId": "agent-run-id",
  "parentRunId": "chat-run-id",
  "name": "my-super-agent",
  "timestamp": "2024-07-16T00:00:01Z",
  "input": "What's the weather in Boston?"
}
```

#### 3. The agent makes an LLM call and asks a tool to be executed.

```json  theme={null}
{
  "type": "llm",
  "event": "start",
  "runId": "llm-run-id",
  "name": "gpt-4o",
  "parentRunId": "agent-run-id",
  "timestamp": "2024-07-16T00:00:02Z",
  "params": {
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_weather_forecast",
          "description": "Get the weather forecast for a specific location.",
          "parameters": {
            "type": "object",
            "properties": {
              "city": {
                "type": "string",
                "description": "The city for which to get the weather forecast."
              }
            },
            "required": ["city"]
          }
        }
      }
    ]
  },
  "input": [{ "role": "user", "content": "What's the weather in Boston?" }]
}
```

Assuming the LLM would respond with:

```json  theme={null}
{
  "type": "llm",
  "event": "end",
  "runId": "llm-run-id",
  "parentRunId": "agent-run-id",
  "timestamp": "2024-07-16T00:00:05Z",
  "output": {
    "role": "assistant",
    "content": "I can get the weather forecast for you. Please wait a moment.",
    "tool_calls": [
      {
        "id": "call_id",
        "type": "function",
        "function": {
          "name": "get_current_weather",
          "arguments": "{\"city\": \"Boston\"}"
        }
      }
    ]
  }
}
```

#### 3. We execute the tool.

```json  theme={null}
{
  "type": "tool",
  "event": "start",
  "runId": "tool-run-id",
  "parentRunId": "agent-run-id",
  "timestamp": "2024-07-16T00:00:06Z",
  "name": "get_weather_forecast",
  "input": {
    "city": "Boston"
  }
}
```

At this point we would call our weather API, and then respond with the output:

```json  theme={null}
{
  "type": "tool",
  "event": "end",
  "runId": "tool-run-id",
  "parentRunId": "agent-run-id",
  "timestamp": "2024-07-16T00:00:10Z",
  "output": {
    "temperature": 72,
    "weather": "sunny"
  }
}
```

#### 4. Another LLM call is made with the tool's output.

```json  theme={null}
{
  "type": "llm",
  "event": "start",
  "runId": "llm-run-id-2",
  "parentRunId": "agent-run-id",
  "timestamp": "2024-07-16T00:00:11Z",
  "name": "gpt-4o",
  "input": [
    { "role": "user", "content": "What's the weather in Boston?" },
    {
      "role": "assistant",
      "content": "I can get the weather forecast for you. Please wait a moment.",
      "tool_calls": [
        {
          "id": "call_id",
          "type": "function",
          "function": {
            "name": "get_current_weather",
            "arguments": "{\"city\": \"Boston\"}"
          }
        }
      ]
    },
    {
      "role": "tool",
      "content": "{\"temperature\": 72, \"weather\": \"sunny\"}"
    }
  ]
}
```

Let's assume the LLM would respond with:

```json  theme={null}
{
  "type": "llm",
  "event": "end",
  "runId": "llm-run-id-2",
  "timestamp": "2024-07-16T00:00:15Z",
  "parentRunId": "agent-run-id",
  "output": {
    "role": "assistant",
    "content": "The weather in Boston is sunny with a temperature of 72 degrees."
  }
}
```

#### 5. The final answer is returned to the user.

We can first mark the agent run as completed.

```json  theme={null}
{
  "type": "agent",
  "event": "end",
  "runId": "agent-run-id",
  "timestamp": "2024-07-16T00:00:20Z",
  "output": "The weather in Boston is sunny with a temperature of 72 degrees."
}
```

Then reply the final answer to the user (note that the `runId` & `parentRunId` here is the same as the previous `chat` run), as 1 ID is used per user->assistant interaction.

```json  theme={null}
{
  "type": "thread",
  "event": "chat",
  "runId": "chat-run-id",
  "parentRunId": "thread-run-id",
  "timestamp": "2024-07-16T00:00:25Z",
  "message": {
    "role": "assistant",
    "content": "The weather in Boston is sunny with a temperature of 72 degrees."
  }
}
```

As you can see, in the context of:

* chat messages, the user message is passed with the `message` field
* llm calls, `input` is the prompt and `output` is the llm's response
* tools, `input` is the arguments and the `output` is the tool's result

This is how it would look in the Lunary UI, under the Threads section:

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/advanced-thread.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=08eeef5a3c593af5e3a23f21b2e86326" alt="Advanced Traces in Lunary UI" data-og-width="2428" width="2428" data-og-height="1026" height="1026" data-path="media/docs/custom-integration/advanced-thread.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/advanced-thread.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=f912d84b339c2cf66cd0fc3473474e61 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/advanced-thread.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=a18668fc026cd8269f03496a1d586cde 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/advanced-thread.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=b900e4e97041db1de063b7553af39f3d 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/advanced-thread.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=a17d68cee2ccee0b76aca38ae65c1520 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/advanced-thread.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=3c9c8b6dc3b7a8c6014fd41eddd8786f 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/advanced-thread.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=53f21a806736e7474811d393988b6c7e 2500w" />

And clicking on "View trace" shows us:

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/advanced-trace.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=dcb3bc202a66a5ee1ca868b32863a863" alt="Advanced Traces in Lunary UI" data-og-width="2956" width="2956" data-og-height="1228" height="1228" data-path="media/docs/custom-integration/advanced-trace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/advanced-trace.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=038950115a8cbb107617f2dac9e9cbac 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/advanced-trace.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=1f6f2f9f3eba49abd8264472015d9116 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/advanced-trace.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=5529fcdd1be9fae6811f4fed36747a27 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/advanced-trace.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=65c191722e34c6b1b0fe7aa3dfa33b0e 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/advanced-trace.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=052fa2dffdee025eb7b278d061231824 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/custom-integration/advanced-trace.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=3fa0caa2761691b83ddb09b437614b14 2500w" />

### Bonus: Reporting User Feedback

If you have feedback from the user, you can attach it to the `chat` run using a `feedback` event and the `feedback` field.

```json  theme={null}
{
  "type": "chat",
  "event": "feedback",
  "runId": "chat-run-id",
  "feedback": {
    "comment": "Great response!",
    "thumb": "up"
  }
}
```

The feedback will now cascade down to all the child runs within the UI, for easy filtering of positive and negative runs.


# Flowise Integration
Source: https://docs.lunary.ai/docs/integrations/flowise



Flowise is an open-source & no-code AI Chatbot builder.

Lunary's Flowise integration allows you to connect your Flowise chatbot and track conversations, user properties, and more.

<Steps>
  <Step n="1" title="Click on 'Configuration'">
        <img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/1.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=71c72ca514e9fefd0e7ffa7bfdea5e25" alt="Click on 'Configuration'" data-og-width="1600" width="1600" data-og-height="1166" height="1166" data-path="media/docs/flowise/1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/1.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=09beaf6c80c14d8a63d099338b362ed2 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/1.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=21e2f65f9422788515b9e2eedbbc1cd1 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/1.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=021a47b9c9f7b08c6e20613473633e43 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/1.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=a654d0b770f290c67a7fc7b597844c6b 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/1.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=e91e37a836a324e537665cbe4130816c 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/1.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=8cdfca7375de3c937d31a7d76fdebe77 2500w" />
  </Step>

  <Step n="2" title="Click on 'Analyse Chatflow'">
        <img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/2.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=dbad08b823835c09d4fb196fbc5c050b" alt="Click on 'Analyse Chatflow'" data-og-width="1600" width="1600" data-og-height="218" height="218" data-path="media/docs/flowise/2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/2.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=57f9f2fe61c305fcdf0306a30cb0bdd0 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/2.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=9dba3c077f693d552663188154991164 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/2.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=4cca3d728b312b0ffe3a02ae02334c99 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/2.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=ddac133c809bb7588a672583d125d815 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/2.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=573e3bb7b69bd323b0eeea658f3c32aa 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/2.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=e1dceae41af9ecc12648f9cbd40b9ccc 2500w" />
  </Step>

  <Step n="3" title="Click on 'Create New'">
        <img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/3.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=9af68dfcc43aa3cd8c627163c08d8d4a" alt="Click on 'Create New'" data-og-width="1602" width="1602" data-og-height="476" height="476" data-path="media/docs/flowise/3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/3.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=31019260a5b94ccaf61a2859e838d4b6 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/3.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=f4cfb9dbc5803c17c8e033be1fec06bd 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/3.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=0235300ddbf23e301d8946e537f0e618 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/3.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=ba1f528a56b0952e7cc5d0729e9bbc88 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/3.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=29c3ffc6a1bc2b2fe6f95428bcbb772d 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/3.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=e99ecbfe010580f9d33f1b65c0b8d703 2500w" />
  </Step>

  <Step n="4" title="Paste your Lunary Public Key">
        <img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/4.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=1838466ab434575bf1a373006f05da00" alt="Paste your Lunary Publick Key" data-og-width="1600" width="1600" data-og-height="1240" height="1240" data-path="media/docs/flowise/4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/4.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=22c6a6edc9c7eebbf9c22a88df263387 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/4.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=a58ae839faac916ec532d696f129480e 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/4.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=03b26ca43a7af2d9479da85f04adf799 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/4.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=1ebe5924cf2fc1aa2036df5b4f6e4465 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/4.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=761ac028680b4262874d6abc0afc8ffc 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/4.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=dd464801ae1b17e999f8ec4dbdff50e6 2500w" />
  </Step>

  <Step n="5" title="Save and toggle ON">
        <img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/5.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=64b1fc50ff6d28eb462b28cab282bef6" alt="Save and toggle ON" data-og-width="1600" width="1600" data-og-height="544" height="544" data-path="media/docs/flowise/5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/5.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=12b3c8af3988698e9840a673366c9cfa 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/5.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=4285ca5b5d130fde18c0d783efce0029 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/5.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=0b9b3bf968b95259c48add23f315aacb 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/5.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=11e1eaf8a981f4fbaeca394a500cce2e 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/5.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=133e6a6113b3bf8ffebddcef3af6934c 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/flowise/5.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=5651923e184dc44cf344d3382969be91 2500w" />
  </Step>

  <Step n="🎉" title="That's it">
    Data from your conversations should now be visible in your dashboard.
  </Step>
</Steps>


# IBM WatsonX Integration
Source: https://docs.lunary.ai/docs/integrations/ibm



Lunary has partnered with IBM to provide a seamless integration for monitoring WatsonX calls in your Python app.

Our Python SDK includes automatic integration with IBM WatsonX's foundation models using Lunary.

<Steps>
  <Step n="1" title="Setup the SDK">
    First, ensure you have installed the IBM WatsonX SDK and Lunary. Set your environment variables for IBM authentication.

    ```bash  theme={null}
    pip install ibm-watsonx-ai lunary
    ```

    Configure your environment variables:

    * `IBM_API_KEY`: your IBM API key
    * `IBM_PROJECT_ID`: your IBM project id
  </Step>

  <Step n="2" title="Monitor IBM WatsonX calls">
    Wrap your WatsonX model instance with Lunary's `monitor` method to automatically track your calls.

    ```py  theme={null}
    import os
    from ibm_watsonx_ai import Credentials
    from ibm_watsonx_ai.foundation_models import ModelInference
    import lunary

    model = ModelInference(
        model_id="meta-llama/llama-3-1-8b-instruct",
        credentials=Credentials(
            api_key=os.environ.get("IBM_API_KEY"),
            url="https://us-south.ml.cloud.ibm.com"
        ),
        project_id=os.environ.get("IBM_PROJECT_ID")
    )

    lunary.monitor(model)

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"}
    ]

    response = model.chat(messages=messages)
    ```
  </Step>

  <Step n="3" title="Tag requests and identify users">
    Optionally, pass extra parameters to track details such as tags and user information by including additional arguments to the chat call.

    ```py  theme={null}
    response = model.chat(messages=messages, tags=["baseball"], user_id="1234", user_props={"name": "Alice"})
    ```
  </Step>
</Steps>


# JS Anthropic integration
Source: https://docs.lunary.ai/docs/integrations/javascript/anthropic



Our SDKs include automatic integration with Anthropic's modules.

<Steps>
  <Step n="1" title="Setup the SDK">
    <CardGroup cols={1}>
      <Card title="JavaScript" icon="js" href="/docs/integrations/javascript/installation">
        Learn how to set up the JS SDK.
      </Card>
    </CardGroup>
  </Step>

  <Step n="2" title="Monitor OpenAI">
    With our SDKs, tracking Anthropic calls is super simple.

    ```js  theme={null}
    import Anthropic from "@anthropic-ai/sdk"
    import { monitorAnthropic } from "lunary/anthropic"

    // Simply call monitor() on the Anthropic class to automatically track requests
    const anthropic = monitorAnthropic(new Anthropic())
    ```
  </Step>

  <Step n="3" title="Tag requests and identify users">
    You can now tag requests and identify users.

    ```js  theme={null}
    const result = await anthropic.messages.create({
      model: "claude-3-5-sonnet-20240620",
      temperature: 0.9,
      tags: ["chat", "support"],  // Optional: tags
      userId: "user_123",  // Optional: user ID
      userProps: { name: "John Doe" },  // Optional: user properties
      system: "You are an helpful assistant",
      messages: [
        { role: "user", content: "Hello friend" },
      ],
    })
    ```
  </Step>
</Steps>


# JS Azure OpenAI integration
Source: https://docs.lunary.ai/docs/integrations/javascript/azure-openai



Our JS SDK includes automatic integration with Azure OpenAI.

<Steps>
  <Step n="1" title="Setup the SDK">
    ```bash  theme={null}
    npm i openai lunary 
    ```
  </Step>

  <Step n="2" title="Monitor AzureOpenAI">
    With our SDKs, tracking AzureOpenAI calls is super simple.

    ```js  theme={null}
    import { AzureOpenAI } from "openai";
    import { monitorOpenAI } from "lunary/openai";

    const API_VERSION = process.env.OPENAI_API_VERSION;
    const API_KEY = process.env.AZURE_OPENAI_API_KEY;
    const AZURE_ENDPOINT = process.env.AZURE_OPENAI_ENDPOINT;
    const RESOURCE_NAME = process.env.AZURE_OPENAI_RESOURCE_NAME;

    const client = monitorOpenAI(
      new AzureOpenAI({
        apiVersion: API_VERSION,
        endpoint: AZURE_ENDPOINT,
        apiKey: API_KEY,
      })
    );

    async function main() {
      const chatCompletion = await client.chat.completions.create({
        model: RESOURCE_NAME,
        messages: [{ role: "user", content: "Say this is a test" }],
      });
      console.log(chatCompletion.choices[0].message.content);
    }

    main();

    ```
  </Step>
</Steps>


# Custom Models
Source: https://docs.lunary.ai/docs/integrations/javascript/custom-model



If you're not using LangChain or OpenAI, you can still integrate Lunary with your own LLMs.

### Method 1: `wrapModel`

In addition to the `lunary.wrapAgent` & `lunary.wrapTool` methods, we provide a `wrapModel` method.

It allows to wrap any async function. It also takes the following options:

```ts  theme={null}
const wrapped = lunary.wrapModel(yourLlmModel, {
  nameParser: (args) => 'custom-model-1.3', // name of the model used
  inputParser: (args) => { // parse the input to message format
    return [{
      role: 'system',
      text: args.systemPrompt
    }, {
      role: 'user',
      text: args.userPrompt
    }]
  },
  extraParser: (args) => { // Report any extre properties like temperature
    return {
      temperature: args.temperature,
    }
  },
  outputParser: (result) => { // Parse the result
    return {
      role: 'ai',
      text: result.content,
    }
  },
  tokensUsageParser: async (result) => { // Return the number of tokens used
    return {
      completion: 10
      prompt: 10
    }
  },
})
```

### Method 2: `.trackEvent`

If you don't want to wrap your model, you can also use the `lunary.trackEvent` method.

First, track the start of your query:

```ts  theme={null}

// Report the start of the model
const runId = 'some-unique-id'
lunary.trackEvent('llm','start',{
  runId,
  name: 'custom-model-1.3',
  input: [{
    role: 'system',
    text: args.systemPrompt
  }, {
    role: 'user',
    text: args.userPrompt
  }],
  extra: {
    temperature: args.temperature,
  },
})

```

Run your model:

```ts  theme={null}
const result = await yourLlmModel('Hello!')
```

Then, track the result of your query:

```ts  theme={null}
lunary.trackEvent('llm','end',{
  runId,
  output: {
    role: 'ai',
    text: result.content,
  },
  tokensUsage: {
    completion: 10
    prompt: 10
  }
})
```

<Card title="Note">
  Input & output can be any object or array of object, however we recommend using the ChatMessage format:

  ```ts  theme={null}
  interface ChatMessage {
    role: "user" | "ai" | "system" | "function"
    text: string
    functions?: cJSON[]
    functionCall?: {
      name: string
      arguments: cJSON
    }
  }
  ```
</Card>


# JavaScript SDK
Source: https://docs.lunary.ai/docs/integrations/javascript/installation



## Installation

The `lunary` module is lightweight and works with Node JS, Deno, Cloudflare Workers, Vercel Edge functions and even Bun.

### Node

```bash  theme={null}
npm install lunary
```

<Warning>
  ### For Cloudflare Workers

  In your `wrangler.toml` file, make sure to add the Node.js compatibility flag:

  ```toml  theme={null}
  compatibility_flags = [ "nodejs_compat" ]
  ```
</Warning>

## Setup

Start by importing the `lunary` module:

```js  theme={null}
import lunary from "lunary";
```

If you're using in the browser, import like this:

```js  theme={null}
import lunary from "lunary/browser";
```

Then initialize the module with your unique app ID.

Option 1: Automatic using environment variables (recommended):

```bash  theme={null}
LUNARY_PUBLIC_KEY="0x0"
```

Option 2: Manually using the `.init` method:

```ts  theme={null}
// Initialize the Lunary module with your unique app ID
lunary.init({
  publicKey: "0x0",
});
```

The `.init` method accepts the following arguments:

```ts  theme={null}
{
  "appId": string, // Your unique app ID obtained from the dashboard
  "apiUrl": string, // Optional: Use a custom endpoint if you're self-hosting (you can also set LUNARY_API_URL)
  "verbose": boolean // Optional: Enable verbose logging for debugging
}
```

<CardGroup cols={2}>
  <Card title="LangChain" icon="box" href="/docs/integrations/langchain">
    Usage with LangChain JS.
  </Card>

  <Card title="OpenAI" icon="microchip-ai" href="/docs/integrations/javascript/openai">
    Automatically track your OpenAI calls.
  </Card>

  <Card title="User Tracking" icon="users" href="/docs/features/users">
    Identify your users.
  </Card>

  <Card title="Tagging" icon="tags" href="/docs/features/tags">
    Segment your queries with tags.
  </Card>

  <Card title="Chats" icon="messages" href="/docs/features/conversations">
    Record user interactions with your chatbot.
  </Card>

  <Card title="Manual Integration" icon="code" href="/docs/integrations/javascript/manual">
    Learn how to use .trackEvent().
  </Card>

  <Card title="Serverless" icon="lambda" href="/docs/integrations/javascript/serverless">
    Use with Lambda, Cloudflare Workers, Edge Functions, etc.
  </Card>

  <Card title="Agents & Tools" icon="robot" href="/docs/features/observability">
    Setup tracing by tracking agents & tools.
  </Card>

  <Card title="API Reference" icon="terminal" href="/docs/api/introduction">
    Full list of methods and classes.
  </Card>
</CardGroup>


# Manual Usage
Source: https://docs.lunary.ai/docs/integrations/javascript/manual



If your application requires more flexibility and you can't use the `wrap` helpers, you can use the `trackEvent` method directly.

The `trackEvent` method is used to track and log runs in your application. It takes three parameters: `type`, `event`, and `data`.

### Parameters:

| Parameter | Type                                  | Description                   |
| --------- | ------------------------------------- | ----------------------------- |
| `type`    | `agent`, `tool`, `llm` or `chain`     | The type of the run           |
| `event`   | `start`, `end`, `error` or `feedback` | The name of the event.        |
| `data`    | `Partial<RunEvent>`                   | Data associated with the run. |

The `RunEvent` type is composed of the following properties:

| Field       | Type                                     | Description                               | Required |
| ----------- | ---------------------------------------- | ----------------------------------------- | -------- |
| runId       | string                                   | Unique identifier                         | Yes      |
| input       | JSON                                     | Input data                                | No       |
| output      | JSON                                     | Output data                               | No       |
| tokensUsage | `{ completion: number, prompt: number }` | Number of tokens used in the run.         | No       |
| userId      | string                                   | The user ID.                              | No       |
| userProps   | JSON                                     | The user properties.                      | No       |
| parentRunId | string                                   | The parent run ID.                        | No       |
| extra       | JSON                                     | Any extra data associated with the event. | No       |
| tags        | string\[]                                | Tags associated with the event.           | No       |
| error       | `{ message: string, stack?: string }`    | Error object if an error occurred.        | No       |

### Example to track an agent:

```ts  theme={null}
// Assuming you have an instance of Lunary
// Define your agent function
async function myAgentFunction(input: string): Promise<string> {
  // Start of the agent function
  const runId = 'unique_run_id'; // Replace with a unique run ID for each run
  lunary.trackEvent('agent', 'start', {
    runId,
    input,
    name: 'MySuperAgent',
    extra: { extra: 'data' },
    tags: ['tag1', 'tag2']
  });

  try {

    const output = await someAsyncOperation(input);

    lunary.trackEvent('agent', 'end', {
      runId,
      output,
    });

    return output;
  } catch (error) {

    lunary.trackEvent('agent', 'error', {
      runId,
      error: error.message, // Replace with actual error message
      name: 'myAgentFunction'
    })
  }
}

// Use the agent function
myAgentFunction('some input')
  .then(output => console.log('Output:', output))
  .catch(error => console.error('Error:', error));

```

### Using the `parentRunId` parameter

To create traces with sub-agents, you can use the `parentRunId` parameter to link child runs.

```ts  theme={null}
async function someTool(input: string, parentRunId: string): Promise<string> {

  const subRunId = 'sub_run_id'; 
  lunary.trackEvent('tool', 'start', {
    runId: subRunId,
    parentRunId,
    input,
    name: 'MyTool',
    tags: ['tag1', 'tag2']
  });

  try {

    const output = await someAsyncOperation(input);

    lunary.trackEvent('tool', 'end', {
      runId: subRunId,
      parentRunId,
      output,
    });

    return output;
  } catch (error) {

    lunary.trackEvent('tool', 'error', {
      runId: subRunId,
      parentRunId,
      error: error.message, // Replace with actual error message
      name: 'mySubAgentFunction'
    });

  }
}

// Use the main agent function
myAgentFunction('some input')
  .then(output => console.log('Output:', output))
  .catch(error => console.error('Error:', error));
```


# JS OpenAI integration
Source: https://docs.lunary.ai/docs/integrations/javascript/openai



Our SDKs include automatic integration with OpenAI's modules.

<Steps>
  <Step n="1" title="Setup the SDK">
    <CardGroup cols={1}>
      <Card title="JavaScript" icon="js" href="/docs/integrations/javascript/installation">
        Learn how to set up the JS SDK.
      </Card>
    </CardGroup>
  </Step>

  <Step n="2" title="Monitor OpenAI">
    With our SDKs, tracking OpenAI calls is super simple.

    ```js  theme={null}
    import OpenAI from "openai";
    import { monitorOpenAI } from "lunary/openai";

    // Simply call monitor() on the OpenAIApi class to automatically track requests
    const openai = monitorOpenAI(new OpenAI());
    ```
  </Step>

  <Step n="3" title="Tag requests and identify users">
    You can now tag requests and identify users.

    ```js  theme={null}
    const result = await openai.chat.completions.create({
      model: "gpt-4o",
      temperature: 0.9,
      tags: ["chat", "support"], // Optional: tags
      user: "user_123", // Optional: user ID
      userProps: { name: "John Doe" }, // Optional: user properties
      messages: [
        { role: "system", content: "You are an helpful assistant" },
        { role: "user", content: "Hello friend" },
      ],
    });
    ```
  </Step>
</Steps>


# Usage with React
Source: https://docs.lunary.ai/docs/integrations/javascript/react



<Steps>
  <Step n="1" title="Import">
    Install the package and import the necessary functions from our React export:

    ```ts  theme={null}
    import lunary, { useChatMonitor } from 'lunary/react';
    ```
  </Step>

  <Step n="2" title="Initialize lunary">
    Initialize the SDK with your application's tracking ID:

    ```ts  theme={null}
    lunary.init({
      publicKey: "0x0",
    })
    ```
  </Step>

  <Step n="3" title="Use the `useChatMonitor` hook">
    The `useChatMonitor` hook exposes the following functions:

    ```ts  theme={null}
    const { 
      restart, 
      trackFeedback, 
      trackMessage
    } = useChatMonitor();
    ```

    Here's an example of how you would it into your Chat component.

    ```ts  theme={null}
    import { useState, useEffect } from "react";

    const App = () => {
      const [input, setInput] = useState("");
      const [messages, setMessages] = useState([]);

      const { restart: restartMonitor, trackFeedback, trackMessage } = useChatMonitor();
      
      // Step 4: Use Effects for Initialization
      useEffect(() => {
        restartMonitor();
      }, []);

      // Step 5: Define Your Message Handlers
      const askBot = async (query) => { 

        // Track the user message and keep the message ID in reference
        const messageId = trackMessage({
          role: 'user',
          content: query,
        });

        setMessages([...messages, { id: messageId, role: "user", content: query }]);

        const answer = await fetchBotResponse(query, messages);

        setMessages([...messages, { role: "assistant", content: answer }]);

        // Track the bot answer
        trackMessage({
          role: 'assistant',
          content: answer,
        });
      }

      // Your message logic
      const fetchBotResponse = async (query, messages) => {
        const response = await fetch("https://...", {
          method: "POST",
          body: JSON.stringify({ messages }),
        });
        return await response.text();
      };

      const restartChat = () => { 
        setMessages([]);
        restartMonitor();
      }

      // Step 6: Render UI
      return (
        <>
          <div>
            {messages.map((message) => (
              <div key={message.id}>
                <div>{message.role}</div>
                <div>{message.text}</div>
              </div>
            ))}
          </div>
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                askBot(input);
                setInput("");
              }
            }}
          />
        </>
      );
    }
    ```
  </Step>

  <Step n="4" title="Reconcile calls on your backend">
    Make sure to pass the message IDs to your backend to reconcile with the backend calls and agents.
  </Step>
</Steps>

# Vercel AI SDK Integration

Effortlessly integrate the Vercel AI SDK into your Next.js app using lunary We've built a custom hook that makes tracking your AI-driven chats a breeze.

<Note>
  ### Other frameworks

  This assumes you are using Next.js. If you are using another framework, contact us and we'll help you integrate.
</Note>

<Steps>
  <Step n="1" title="Import and Initialize">
    Import lunary and the AI SDK helper hook, then initialize the monitor with your app ID.

    ```ts  theme={null}
    import lunary, { useMonitorVercelAI } from "lunary/react"

    lunary.init({
      publicKey: "0x0"
    })
    ```
  </Step>

  <Step n="2" title="Wrap the useChat hook">
    ```tsx  theme={null}
    export default function Chat() {
      const ai = useChat({
        // This is necessary to reconcile LLM calls made on the backend
        sendExtraMessageFields: true
      })

      // Use the hook to wrap and track the AI SDK
      const {
        trackFeedback, // this a new function you can use to track feedback
        messages,
        input,
        handleInputChange,
        handleSubmit
      } = useMonitorVercelAI(ai)

      // Optional: Identify the user
      useEffect(() => {
        lunary.identify("elon", {
          name: "Elon Musk",
          email: "elon@tesla.com",
        })
      }, [])

      return (
        // ... your chat UI ...
      )
    }
    ```
  </Step>

  <Step n="3" title="Setup the monitor on the backend">
    We'll need to reconcile the OpenAI calls made in the backend, with messages sent from the frontend. To do this, we'll need to use the backend version of the lunary.

    ```ts  theme={null}
    import lunary from "lunary";
    import { monitorOpenAI } from "lunary/openai";

    lunary.init({
      publicKey: "0x0",
    })

    // Create an OpenAI API client and monitor it
    const openai = monitorOpenAI(
      new OpenAI({
        apiKey: process.env.OPENAI_API_KEY
      })
    );
    ```
  </Step>

  <Step n="4" title="Reconcile messages with OpenAI calls">
    Once your openai client is monitored, you can use the `setParent` method to reconcile the frontend message IDs with the backend call:

    ```ts  theme={null}
    const response = await openai.chat.completions
      .create({
        model: "gpt-4",
        stream: true,
        messages: messages,
      })
      // The setParent method reconcilates the frontend call with the backend call
      .setParent(lastMessageId);
    ```

    ### Full API Function Example

    <Note>
      Make sure you've enabled `sendExtraMessageFields` on the  `useChat` hook so that message IDs are also sent.
    </Note>

    ```ts  theme={null}
    // ./app/api/chat/route.ts
    import OpenAI from "openai";
    import { OpenAIStream, StreamingTextResponse } from "ai";

    // Import the backend version of the monitor
    import lunary, { monitorOpenAI } from "lunary/openai";

    lunary.init({
      publicKey: "0x0",
    })

    // Create an OpenAI API client and monitor it
    const openai = monitorOpenAI(
      new OpenAI({
        apiKey: process.env.OPENAI_API_KEY
      })
    );

    export const runtime = "edge";

    export async function POST(req: Request) {
      const data = await req.json()
      const { messages: rawMessages } = data

      // Keep only the content and role of each message, otherwise OpenAI throws an error
      const messages = rawMessages.map(({ content, role }) => ({ role, content }))

      // Get the last message's run ID
      const lastMessageId = rawMessages[rawMessages.length - 1].id

      // Ask OpenAI for a streaming chat completion given the prompt
      const response = await openai.chat.completions
        .create({
          model: "gpt-4",
          stream: true,
          messages: messages,
        })
        // The setParent method reconcilates the frontend call with the backend call
        .setParent(lastMessageId);


      const stream = OpenAIStream(response);


      return new StreamingTextResponse(stream);
    }
    ```
  </Step>
</Steps>


# Serverless
Source: https://docs.lunary.ai/docs/integrations/javascript/serverless



Usage with serverless functions.

When using lunary with Serverless/Lambda functions, you need to make sure that you flush the queue at the end of each function otherwise the data may not be side.

```js  theme={null}
import lunary from 'lunary'

async function handler(event, context) {
  // do something

  // your function logic...

  // flush the queue (make sure to await)

  await lunary.flush()

  return {
    statusCode: 200,
    body: JSON.stringify({ message: 'Hello World' })
  }
}
```


# Vercel AI SDK
Source: https://docs.lunary.ai/docs/integrations/javascript/vercel-ai-sdk

Send Vercel AI SDK telemetry to Lunary via OpenTelemetry.

Lunary accepts OpenTelemetry traces, so you can forward the spans that the Vercel AI SDK
emits to Lunary without writing a custom logger. This guide walks through the minimal
changes required for a Next.js or Node.js app that already uses the AI SDK.

## Prerequisites

* A Lunary project with its public key copied from **Settings → API Keys**.
* A Vercel AI SDK app running on Node.js 18+ with access to modify instrumentation files.
* Optional (Next.js ≤14): `experimental.instrumentationHook` enabled in `next.config.mjs`.

## 1. Enable Vercel's OpenTelemetry instrumentation

Install the instrumentation helper if it is not already included in your project:

```bash  theme={null}
npm install @vercel/otel @opentelemetry/api
```

For Next.js, ensure `instrumentation.ts` exists at the project root (or inside `src/` if
you use that folder) and register OpenTelemetry:

```ts  theme={null}
// instrumentation.ts
import { registerOTel } from "@vercel/otel";

export function register() {
  registerOTel({ serviceName: "vercel-ai-with-lunary" });
}
```

If you target Next.js 14 or earlier, add the instrumentation hook in `next.config.mjs`:

```js  theme={null}
export default {
  experimental: {
    instrumentationHook: true,
  },
};
```

Vercel's helper wires the AI SDK to OpenTelemetry so spans are created whenever you call
`generateText`, `streamText`, or other AI SDK functions.citeturn5search1turn5search0

## 2. Point OpenTelemetry to Lunary

Configure the OTLP exporter to send traces to Lunary's managed collector. Using
environment variables keeps local and hosted deployments aligned:

```bash  theme={null}
# .env (or Vercel/Vault environment variables)
OTEL_EXPORTER_OTLP_ENDPOINT=https://api.lunary.ai
OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer ${LUNARY_PUBLIC_KEY}"
OTEL_RESOURCE_ATTRIBUTES="service.name=vercel-ai-app,deployment.environment=production"
```

If you prefer explicit code, supply Lunary's endpoint and headers when registering
OpenTelemetry:

```ts  theme={null}
// instrumentation.ts
import { registerOTel, OTLPHttpJsonTraceExporter } from "@vercel/otel";

export function register() {
  registerOTel({
    serviceName: "vercel-ai-with-lunary",
    traceExporter: new OTLPHttpJsonTraceExporter({
      url: "https://api.lunary.ai/v1/traces",
      headers: {
        Authorization: `Bearer ${process.env.LUNARY_PUBLIC_KEY}`,
      },
    }),
  });
}
```

Either approach sends OTLP/HTTP traces to Lunary using your project public key for
authentication. Resource attributes travel with every span and help Lunary group data by
service and environment.citeturn4search1turn5search1turn3search3

## 3. Emit AI spans with Lunary metadata

Telemetry remains an opt-in experimental flag in the AI SDK. Wrap the calls you want to
observe with `experimental_telemetry` and include metadata that Lunary can use for
filtering and trace grouping:

```ts  theme={null}
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";

export async function summarize(content: string, userId: string) {
  const result = await generateText({
    model: openai("gpt-5"),
    prompt: `Summarize:\n${content}`,
    experimental_telemetry: {
      isEnabled: true,
      functionId: "summarizer",
      metadata: {
        lunary_user_id: userId,
        thread_id: `thread-${userId}`,
      },
    },
  });

  return result.text;
}
```

Every traced invocation appears in Lunary with the function ID, custom metadata, tokens,
latency, and errors captured by the AI SDK spans.

## 4. Validate traces inside Lunary

Deploy or start your app locally and trigger the instrumented route. Open the Lunary
dashboard and visit **Observability → Traces** to confirm new spans tagged with your
`service.name` and metadata. From there you can drill into token usage, latency, and
prompt/response payloads per trace.


# LangChain Integration
Source: https://docs.lunary.ai/docs/integrations/langchain



We provide callback handler that can be used to track LangChain calls, chains and agents.

## Setup

First, install the relevant `lunary` and `langchain` packages:

<Tabs>
  <Tab title="Python">
    ```bash  theme={null}
    pip install lunary
    pip install langchain
    ```
  </Tab>

  <Tab title="Javascript">
    ```bash  theme={null}
    npm install lunary
    npm install langchain
    ```
  </Tab>
</Tabs>

Then, set the `LUNARY_PUBLIC_KEY` environment variable to your app tracking id.

```bash  theme={null}
LUNARY_PUBLIC_KEY="0x0"
```

If you'd prefer not to set an environment variable, you can pass the key directly when initializing the callback handler:

<Tabs>
  <Tab title="Python">
    ```py  theme={null}
    from lunary import LunaryCallbackHandler

    handler = LunaryCallbackHandler(app_id="0x0")
    ```
  </Tab>

  <Tab title="Javascript">
    ```js  theme={null}
    import { LunaryHandler } from "lunary/langchain"

    const handler = new LunaryHandler({
      appId: "0x0",
    })
    ```
  </Tab>
</Tabs>

## Usage with LLM calls

You can use the callback handler with any LLM or Chat class from LangChain.

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from langchain_openai import ChatOpenAI
    from lunary import LunaryCallbackHandler

    handler = LunaryCallbackHandler()

    chat = ChatOpenAI(
      callbacks=[handler],
    )
    chat.invoke("Say test")
    ```
  </Tab>

  <Tab title="Javascript">
    ```js  theme={null}
    import { LunaryHandler } from "lunary/langchain"

    const model = new ChatOpenAI({
      callbacks: [new LunaryHandler()],
    })
    ```
  </Tab>
</Tabs>

## Usage with chains (LCEL)

You can also use the callback handler with LCEL, LangChain Expression Language.

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from langchain_openai import ChatOpenAI
    from langchain_core.runnables import RunnablePassthrough, RunnableConfig
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatPromptTemplate
    import lunary

    # Initialize the Lunary handler
    handler = lunary.LunaryCallbackHandler()
    config = RunnableConfig({"callbacks": [handler]})

    prompt = ChatPromptTemplate.from_template(
      "Tell me a short joke about {topic}"
    )
    output_parser = StrOutputParser()
    model = ChatOpenAI(model="gpt-4")
    chain = (
      {"topic": RunnablePassthrough()} 
      | prompt
      | model
      | output_parser
    )

    chain.invoke("ice cream", config=config) # You need to pass the config each time you call `.invoke()`
    ```
  </Tab>

  <Tab title="Javascript">
    ```js  theme={null}
    import { ChatOpenAI } from "@langchain/openai";
    import { ChatPromptTemplate } from "@langchain/core/prompts";
    import { StringOutputParser } from "@langchain/core/output_parsers";
    import { LunaryHandler } from "lunary/langchain";

    const handler = new LunaryHandler();

    const prompt = ChatPromptTemplate.fromMessages([
      ["human", "Tell me a short joke about {topic}"],
    ]);
    const model = new ChatOpenAI({});
    const outputParser = new StringOutputParser();

    const chain = prompt.pipe(model).pipe(outputParser);

    const response = await chain.invoke({
      topic: "ice cream",
    }, {
      callbacks: [handler]
    })
    console.log(response);
    ```
  </Tab>
</Tabs>

## Usage with agents

The callback handler works seamlessly with LangChain agents and chains.

For agents, it is recommended to pass a name in the metadatas to track them in the dashboard.

<Alert title="Note">
  When tracking agents, make sure to add the handler to the agent's `run`
  method, otherwise the LLM calls and tools will not be automatically tracked.
</Alert>

Example:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from langchain.agents import AgentExecutor, create_openai_tools_agent
    from langchain_community.tools.tavily_search import TavilySearchResults
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain_core.runnables import RunnableConfig
    from langchain_openai import ChatOpenAI

    # Initialize the Lunary handler
    from lunary import LunaryCallbackHandler

    prompt = ChatPromptTemplate.from_messages([
      ("system", "You are a helpful assistant"),
      MessagesPlaceholder("chat_history", optional=True),
      ("human", "{input}"),
      MessagesPlaceholder("agent_scratchpad"),
    ])

    tools = [TavilySearchResults(max_results=1)]

    # Initialize the Lunary handler
    handler = LunaryCallbackHandler()
    config = RunnableConfig({"callbacks": [handler]})

    llm = ChatOpenAI(model="gpt-4")
    agent = create_openai_tools_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools)

    agent_executor.invoke({"input": "what is LangChain?"}, config)
    ```
  </Tab>

  <Tab title="Javascript">
    ```js  theme={null}
    import { initializeAgentExecutorWithOptions } from "langchain/agents"
    import { ChatOpenAI } from "langchain/chat_models/openai"
    import { Calculator } from "langchain/tools/calculator"
    import { LunaryHandler } from "lunary/langchain"

    const tools = [new Calculator()]
    const chat = new ChatOpenAI()

    const executor = await initializeAgentExecutorWithOptions(tools, chat, {
      agentType: "openai-functions",
    })

    const result = await executor.run(
      "What is the approximate result of 78 to the power of 5?",
      {
        callbacks: [new LunaryHandler()], // Add the handler to the agent
        metadata: { agentName: "SuperCalculator" }, // Identify the agent in the Lunary dashboard
      }
    )
    ```
  </Tab>
</Tabs>

## Usage with custom agents

If you're partially using LangChain, you can use the callback handler combined with the `lunary` module to track custom agents:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from langchain.schema.messages import HumanMessage, SystemMessage
    from langchain_openai import ChatOpenAI
    import lunary

    handler = lunary.LunaryCallbackHandler()

    chat = ChatOpenAI(
      callbacks=[handler],
    )

    @lunary.agent()
    def TranslatorAgent(query):
      messages = [ 
        SystemMessage(content="You're a helpful assistant"),
        HumanMessage(content="What is the purpose of model regularization?"),
      ]

      return chat.invoke(messages)

    res = TranslatorAgent("Good morning")
    ```
  </Tab>

  <Tab title="Javascript">
    ```js  theme={null}
    import { ChatOpenAI } from "langchain/chat_models/openai"
    import { HumanMessage, SystemMessage } from "langchain/schema"

    import { LunaryHandler } from "lunary/langchain"
    import lunary from "lunary"

    const chat = new ChatOpenAI({
      callbacks: [new LunaryHandler()], // <- Add the Lunary Callback Handler here
    })

    async function TranslatorAgent(query) {
      const res = await chat.call([
        new SystemMessage(
          "You are a translator agent that hides jokes in each translation."
        ),
        new HumanMessage(
          `Translate this sentence from English to French: ${query}`
        ),
      ])

      return res.content
    }

    // By wrapping the agent with wrapAgent, we automatically track all input, outputs and errors
    // And tools and logs will be tied to the correct agent
    const translate = lunary.wrapAgent(TranslatorAgent)

    const res = await translate("Good morning")
    ```
  </Tab>
</Tabs>

## Usage with LangServe

You can use the callback handler to track all calls to your LangServe server.

### Server

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from fastapi import FastAPI
    from langchain_openai import ChatOpenAI
    from langchain.schema.runnable import (
        ConfigurableField,
    )
    from langserve import add_routes
    from lunary import LunaryCallbackHandler

    handler = LunaryCallbackHandler()

    app = FastAPI(
        title="LangChain Server",
        version="1.0",
        description="Spin up a simple api server using Langchain's Runnable interfaces",
    )

    model = ChatOpenAI(callbacks=[handler]).configurable_fields(
        metadata=ConfigurableField(
            id="metadata",
            name="Metadata",
            description=("Custom metadata"),
        ),
    )

    add_routes(app, model, path="/openai", config_keys=["metadata"])

    if __name__ == "__main__":
        import uvicorn

        uvicorn.run(app, host="localhost", port=8000)

    ```
  </Tab>
</Tabs>

### Client

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from langchain.schema import SystemMessage, HumanMessage
    from langserve import RemoteRunnable

    openai = RemoteRunnable("http://localhost:8000/openai/")

    prompt = [
      SystemMessage(content="Act like either a cat or a parrot."),
      HumanMessage(content="Hello!"),
    ]

    res = openai.invoke("Hello", config={"metadata": {
                        "user_id": "123", "tags": ["user1"]}})
    print(res)
    ```
  </Tab>
</Tabs>


# LiteLLM Integration
Source: https://docs.lunary.ai/docs/integrations/litellm



LiteLLM provides callbacks, making it easy for you to log your completions responses.

## Using Callbacks

First, sign up to get an app ID on the Lunary dashboard.

With these 2 lines of code, you can instantly log your responses across all providers with lunary:

```py  theme={null}
litellm.success_callback = ["lunary"]
litellm.failure_callback = ["lunary"]
```

Complete code

```python  theme={null}
from litellm import completion

## set env variables
os.environ["LUNARY_PUBLIC_KEY"] = "0x0"
# Optional: os.environ["LUNARY_API_URL"] = "self-hosting-url"

os.environ["OPENAI_API_KEY"], os.environ["COHERE_API_KEY"] = "", ""

# set callbacks
litellm.success_callback = ["lunary"]
litellm.failure_callback = ["lunary"]

#openai call
response = completion(
  model="gpt-4o", 
  messages=[{"role": "user", "content": "Hi 👋 - i'm openai"}],
  user="some_user_id",
  metadata={"tags": ["tag1", "tag2"]}
)

#cohere call
response = completion(
  model="command-nightly", 
  messages=[{"role": "user", "content": "Hi 👋 - i'm cohere"}],
  user="some_user_id"
)
```


# Mistral integration
Source: https://docs.lunary.ai/docs/integrations/mistral



Our Python SDK includes automatic integration with Mistral via OpenAI's package.

<Steps>
  <Step n="1" title="Setup the SDK">
    <CardGroup cols={1}>
      <Card title="Python" icon="python" href="/docs/integrations/python/installation">
        Learn how to set up the Python SDK.
      </Card>
    </CardGroup>
  </Step>

  <Step n="2" title="Monitor your client">
    With our SDKs, tracking Mistral calls is super simple.

    ```py  theme={null}
    import os
    from openai import OpenAI
    import lunary

    MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

    client = OpenAI(api_key=MISTRAL_API_KEY, base_url="https://api.mistral.ai/v1/")

    lunary.monitor(client)  # This line sets up monitoring for all calls made through the 'openai' module

    chat_completion = client.chat.completions.create(
      model="mistral-small-latest",
      messages=[{"role": "user", "content": "Hello world"}]
    )
    ```
  </Step>
</Steps>


# Ollama Integration
Source: https://docs.lunary.ai/docs/integrations/ollama



Ollama allow you to self-host quickly large language models.
Our SDKs include automatic integrations with Ollama.

<Steps>
  <Step n="1" title="Setup the SDK">
    <CardGroup cols={2}>
      <Card title="Python" icon="python" href="/docs/integrations/python/installation">
        Learn how to set up the Python SDK.
      </Card>

      <Card title="Javascript" icon="js" href="/docs/integrations/javascript/installation">
        Learn how to set up the JavaScript SDK.
      </Card>
    </CardGroup>
  </Step>

  <Step n="2" title="Monitor Ollama">
    With our SDKs, tracking Ollama calls is super simple.

    <Tabs>
      <Tab title="Python" icon="python">
        ```py  theme={null}
        from openai import OpenAI
        import lunary

        client = OpenAI(
        base_url='http://localhost:11434/v1/', # replace by your Ollama base url
        api_key='ollama', #required but ignored
        )

        lunary.monitor(client)

        chat_completion = client.chat.completions.create(
        messages=[
        {
        'role': 'user',
        'content': 'Say this is a test',
        }
        ],  
         model='llama3.2',
        )

        ```
      </Tab>

      <Tab title="Javascript">
        ```js  theme={null}
        import OpenAI from 'openai'
        import { monitorOpenAI } from "lunary/openai"

        const openai = monitorOpenAI(new OpenAI({
          baseURL: 'http://localhost:11434/v1/', //  replace by your Ollama base url
          apiKey: 'ollama', // required but ignored
        }))

        const chatCompletion = await openai.chat.completions.create({
            messages: [{ role: 'user', content: 'Say this is a test' }],
            model: 'llama3.2',
        })
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>


# OpenAI integration
Source: https://docs.lunary.ai/docs/integrations/openai



Our Python SDK includes automatic integration with OpenAI's module.

<Steps>
  <Step n="1" title="Setup the SDK">
    <CardGroup cols={1}>
      <Card title="Python" icon="python" href="/docs/integrations/python/installation">
        Learn how to set up the Python SDK.
      </Card>
    </CardGroup>
  </Step>

  <Step n="2" title="Monitor OpenAI">
    With our SDKs, tracking OpenAI calls is super simple.

    ```py  theme={null}
    from openai import OpenAI
    import lunary

    client = OpenAI()

    lunary.monitor(client)  # This line sets up monitoring for all calls made through the 'openai' module

    chat_completion = client.chat.completions.create(
      model="gpt-4.1",
      messages=[{"role": "user", "content": "Hello world"}]
    )
    ```
  </Step>

  <Step n="3" title="Tag requests and identify users">
    You can now tag requests and identify users.

    ```py  theme={null}
    chat_completion = client.chat.completions.create(
      model="gpt-4.1",
      user_id="user_123",  # Optional: user ID
      user_props={"name": "John Doe"},  # Optional: user properties
      tags=["chat", "support"],  # Optional: add tags
      messages=[{"role": "user", "content": "Hello world"}]
    )
    ```
  </Step>
</Steps>


# OpenTelemetry (OTEL) Mapping
Source: https://docs.lunary.ai/docs/integrations/opentelemetry/otel-mapping

Mapping OpenTelemetry attributes to Lunary properties.

This page is coming soon.


# Sending OTEL Traces from Python
Source: https://docs.lunary.ai/docs/integrations/opentelemetry/otel-python

How to use OpenTelemetry Python SDK to export traces to Lunary.

# Exporting OpenTelemetry Traces from Python

You can send traces from any Python application or framework to Lunary using the standard OpenTelemetry SDK.

## 1. Install Dependencies

```sh  theme={null}
pip install opentelemetry-sdk opentelemetry-exporter-otlp
```

## 2. Configure Your Environment

Set your Lunary API key and endpoint as OTEL environment variables:

```sh  theme={null}
import os

os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = "https://api.lunary.ai/v1/otel"
os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = f"Authorization=Bearer {os.environ['LUNARY_PUBLIC_KEY']}"
```

## 3. Set up OTEL Tracing

```python  theme={null}
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry import trace

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

exporter = OTLPSpanExporter()
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(exporter))
```

## 4. Emit Traces

You can now add spans to your code:

```python  theme={null}
with tracer.start_as_current_span("My LLM Call") as span:
    # Attach GenAI-related context
    span.set_attribute("gen_ai.request.model", "gpt-4.1")
    span.set_attribute("gen_ai.prompt.0.content", "Hello, LLM world!")
    span.set_attribute("gen_ai.usage.prompt_tokens", 25)
    # Call your LLM/model here
```

## Advanced: Custom Attributes

You can tag spans for sessions, users, or experiments:

```python  theme={null}
span.set_attribute("lunary.user.id", "user-123")
span.set_attribute("lunary.tags", ["my-experiment", "beta"])
```


# Observability via OpenTelemetry
Source: https://docs.lunary.ai/docs/integrations/opentelemetry/overview

Connect your LLM apps to Lunary with the OpenTelemetry standard.

# OpenTelemetry Integration

OpenTelemetry, or OTEL, is the open-source standard for tracing and monitoring distributed applications—including LLM-based workflows.

Lunary offers first-class support for ingesting OTEL traces via its `/v1/otel` endpoint. This means you can export traces, metrics, and events from LLM stacks or frameworks—no matter the language or platform—directly to Lunary’s observability dashboard.

> **Why OpenTelemetry?**
>
> * Unified tracing across polyglot apps (Python, JS, Java, Go, etc.)
> * Bring-your-own instrumentation: works with OpenLIT, Arize, OpenLLMetry, MLflow, and more.
> * Rich, future-proof GenAI semantic conventions.

***

## How It Works

1. Your app or framework emits OpenTelemetry trace data.
2. Data is sent to the Lunary endpoint: `https://api.lunary.ai/v1/otel`
3. Lunary’s backend standardizes, stores, and displays all your traces.

## Supported Libraries and Frameworks

You can send OTEL traces to Lunary from any library or SDK that supports the OTLP protocol, including:

* Python: [`opentelemetry-sdk`](https://opentelemetry.io/docs/languages/python/)
* JavaScript/TypeScript: [`@opentelemetry/api`](https://opentelemetry.io/docs/languages/js/)
* Instrumentation: [OpenLIT](https://openlit.io/), [OpenLLMetry](https://www.traceloop.com/docs/openllmetry/introduction), [Arize OpenInference](https://github.com/Arize-ai/openinference), [MLflow](https://mlflow.org/)
* AI stacks: LangChain, LlamaIndex, Haystack, CrewAI, Semantic Kernel, and more!

***

## Quickstart

* [Python OTEL Setup](./otel-python)

For property mapping and advanced tips, see [OTEL attribute mapping](./otel-mapping).

## Supported Providers

| Model SDK                | Python | Typescript |
| ------------------------ | ------ | ---------- |
| Azure OpenAI             | ✅      | ✅          |
| Aleph Alpha              | ✅      | ❌          |
| Anthropic                | ✅      | ✅          |
| Amazon Bedrock           | ✅      | ✅          |
| Amazon SageMaker         | ✅      | ❌          |
| Cohere                   | ✅      | ✅          |
| IBM watsonx              | ✅      | ⏳          |
| Google Gemini            | ✅      | ✅          |
| Google VertexAI          | ✅      | ✅          |
| Groq                     | ✅      | ⏳          |
| Mistral AI               | ✅      | ⏳          |
| Ollama                   | ✅      | ⏳          |
| OpenAI                   | ✅      | ✅          |
| Replicate                | ✅      | ⏳          |
| together.ai              | ✅      | ⏳          |
| HuggingFace Transformers | ✅      | ⏳          |


# Pydantic AI Integration
Source: https://docs.lunary.ai/docs/integrations/pydantic-ai



<Warning>
  This integration is currently in beta. If you encounter any issues or unexpected behavior, please reach out for feedback and support.
</Warning>

Lunary supports Pydantic AI through OpenTelemetry instrumentation via Logfire.

To integrate Pydantic AI with Lunary, you only need to configure the OpenTelemetry exporter and instrument Pydantic AI:

```python  theme={null}
os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = "https://api.lunary.ai" # replace by your api endpoint if you're self-hosting Lunary
os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = f"Authorization=Bearer {os.environ['LUNARY_PRIVATE_KEY']}"

logfire.configure(send_to_logfire=False)
logfire.instrument_pydantic_ai()
```

## Full Example

Here's a complete example showing how to use Pydantic AI with Lunary:

```python  theme={null}
import os
import logfire
from pydantic import BaseModel
from pydantic_ai import Agent

os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = "https://api.lunary.ai"
os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = f"Authorization=Bearer {os.environ['LUNARY_PRIVATE_KEY']}"

logfire.configure(send_to_logfire=False)
logfire.instrument_pydantic_ai()


class MyModel(BaseModel):
    city: str
    country: str

agent = Agent(model='open:gpt-4.1', output_type=MyModel, model_settings={'temperature': 0.7})

if __name__ == '__main__':
    result = agent.run_sync('The windy city in the US of A.')
    print(result.output)
```

This will automatically track:

* Agent calls and responses
* Model parameters and settings
* Output schema validation
* Performance metrics
* Errors and exceptions

All telemetry data will be sent to Lunary for monitoring and analysis.


# Python Azure OpenAI integration
Source: https://docs.lunary.ai/docs/integrations/python/azure-openai



Our Python SDK includes automatic integration with Azure OpenAI.

<Steps>
  <Step n="1" title="Setup the SDK">
    ```bash  theme={null}
    pip install openai lunary
    ```
  </Step>

  <Step n="2" title="Monitor AzureOpenAI">
    With our SDKs, tracking AzureOpenAI calls is super simple.

    ```py  theme={null}
    import os
    from openai import AzureOpenAI
    import lunary 

    API_VERSION = os.environ.get("OPENAI_API_VERSION")
    API_KEY = os.environ.get("AZURE_OPENAI_API_KEY")
    AZURE_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT")
    RESOURCE_NAME = os.environ.get("AZURE_OPENAI_RESOURCE_NAME")


    client = AzureOpenAI(
        api_version=API_VERSION,
        azure_endpoint=AZURE_ENDPOINT,
        api_key=API_KEY
    )
    lunary.monitor(client)

    completion = client.chat.completions.create(
        model=RESOURCE_NAME,
        messages=[
            {
                "role": "user",
                "content": "How do I output all files in a directory using Python?",
            },
        ],
    )
    print(completion.to_json())


    ```
  </Step>
</Steps>


# Python SDK Installation
Source: https://docs.lunary.ai/docs/integrations/python/installation



Please use Python version 3.10 or higher to ensure compatibility.

```bash  theme={null}
pip install lunary
```

## Setup

Add the `LUNARY_PUBLIC_KEY` to your environment variables.

```bash  theme={null}
export LUNARY_PUBLIC_KEY="PUBLIC KEY"
```

You can use dotenv to load the environment variables from a `.env` file.

```python  theme={null}
from dotenv import load_dotenv
load_dotenv()
```

## Next steps

<CardGroup cols={2}>
  <Card title="LangChain" icon="box" href="/docs/integrations/langchain">
    Usage with LangChain.
  </Card>

  <Card title="OpenAI" icon="microchip-ai" href="/docs/integrations/python/openai">
    Automatically track your OpenAI calls.
  </Card>

  <Card title="User Tracking" icon="users" href="/docs/features/users">
    Identify your users.
  </Card>

  <Card title="Tagging" icon="tags" href="/docs/features/tags">
    Segment your queries with tags.
  </Card>

  <Card title="Manual Integration" icon="code" href="/docs/integrations/python/manual">
    Learn how to use track\_event().
  </Card>

  <Card title="Agents & Tools" icon="robot" href="/docs/features/observability">
    Setup tracing by tracking agents & tools.
  </Card>

  <Card title="API Reference" icon="terminal" href="/docs/api/introduction">
    Full list of methods and classes.
  </Card>
</CardGroup>


# Manual Usage
Source: https://docs.lunary.ai/docs/integrations/python/manual



If your application requires more flexibility and you can't use the decorators, you can use the `track_event` method directly.

Here's a brief overview of how to use it:

```py  theme={null}
import lunary

lunary.track_event(
    run_type,
    event_name,
    run_id,
    parent_run_id=None,
    name=None,
    input=None,
    output=None,
    error=None,
    token_usage=None,
    user_id=None,
    user_props=None,
    tags=None,
    params=None,
    metadata=None,
)
```

The parameters are as follows:

* run\_type: The type of the run. It can be "llm", "agent", "tool", "chain" or "embed".
* event\_name: The event. It can be "start", "end", or "error".
* run\_id: A unique identifier for the run.
* parent\_run\_id: (Optional) The unique identifier of the parent run in case of nested run.
* name: (Optional) The name of the model, agent or chain.
* input: (Optional) The input data for the event. Can be any JSON-safe value.
* output: (Optional) The output data for the event. Can be any JSON-safe value.
* error: (Optional) Any error information.
* token\_usage: (Optional) The number of tokens used.
* user\_id: (Optional) The user ID.
* user\_props: (Optional) Any user properties.
* tags: (Optional) Any tags associated with the event.
* params: (Optional) The params passed to entity you're tracking (for example, the `temperature` for an LLM call).
* metadata: (Optional) Any metadata.

Here's an example of how to use it:

```py  theme={null}
import uuid
import lunary

run_id = uuid.uuid4()

def my_tool(input):

  lunary.track_event(
      run_type="tool",
      event_name="start",
      run_id=run_id,
      name="my_tool",
      input=input,
      user_id="123",
      tags=["tag1", "tag2"],
  )

  # ...
  # do something
  # ...

  lunary.track_event(
      run_type="tool",
      event_name="end",
      run_id=run_id,
      output={"result": "success"},
  )
```


# Python OpenAI integration
Source: https://docs.lunary.ai/docs/integrations/python/openai



Our Python SDK includes automatic integration with OpenAI's module.

<Steps>
  <Step n="1" title="Setup the SDK">
    <CardGroup cols={1}>
      <Card title="Python" icon="python" href="/docs/integrations/python/installation">
        Learn how to set up the Python SDK.
      </Card>
    </CardGroup>
  </Step>

  <Step n="2" title="Monitor OpenAI">
    With our SDKs, tracking OpenAI calls is super simple.

    ```py  theme={null}
    from openai import OpenAI
    import lunary

    client = OpenAI()

    lunary.monitor(client)  # This line sets up monitoring for all calls made through the 'openai' module

    chat_completion = client.chat.completions.create(
      model="gpt-4o",
      messages=[{"role": "user", "content": "Hello world"}]
    )
    ```
  </Step>

  <Step n="3" title="Tag requests and identify users">
    You can now tag requests and identify users.

    ```py  theme={null}
    chat_completion = client.chat.completions.create(
      model="gpt-4o",
      user_id="user_123",  # Optional: user ID
      user_props={"name": "John Doe"},  # Optional: user properties
      tags=["chat", "support"],  # Optional: add tags
      messages=[{"role": "user", "content": "Hello world"}]
    )
    ```
  </Step>
</Steps>


# Python SDK Reference
Source: https://docs.lunary.ai/docs/integrations/python/reference



## Classes

| Class                | Description                                               |
| -------------------- | --------------------------------------------------------- |
| `EventQueue`         | A class that represents a queue of events.                |
| `Consumer`           | A class that consumes events from the `EventQueue`.       |
| `UserContextManager` | A context manager for setting and resetting user context. |

## Methods

| Method                                                                                                                                                                                                             | Description                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------- |
| `config(app_id: str \| None = None, verbose: str \| None = None, api_url: str \| None = None, disable_ssl_verify: bool \| None = None)`                                                                            | Configures the SDK with the given parameters.  |
| `track_event(event_type: str, event_name: str, run_id: uuid, parent_run_id: uuid, name: str, input: Any, output: Any, error: Any, token_usage: Any, user_id: str, user_props: Any, tags: Any, extra: Any) -> None` | Tracks an event with the given parameters.     |
| `handle_internal_error(e: Exception) -> None`                                                                                                                                                                      | Handles internal errors.                       |
| `wrap(fn: Callable, type: str, name: str, user_id: str, user_props: Any, tags: Any, input_parser: Callable, output_parser: Callable) -> Callable`                                                                  | Wraps a function with monitoring capabilities. |
| `monitor(object: OpenAIUtils) -> None`                                                                                                                                                                             | Monitors an instance of `OpenAIUtils`.         |
| `identify(user_id: str, user_props: Any) -> UserContextManager`                                                                                                                                                    | Identifies a user and sets the user context.   |

## Decorators

| Decorator                                                                | Description                                     |
| ------------------------------------------------------------------------ | ----------------------------------------------- |
| `agent(name: str, user_id: str, user_props: Any, tags: Any) -> Callable` | A decorator for marking a function as an agent. |
| `tool(name: str, user_id: str, user_props: Any, tags: Any) -> Callable`  | A decorator for marking a function as a tool.   |

## Context Variables

| Variable         | Description                                     |
| ---------------- | ----------------------------------------------- |
| `user_ctx`       | A context variable for storing the user ID.     |
| `user_props_ctx` | A context variable for storing user properties. |

## Environment variables

| Variable             | Description                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `LUNARY_PUBLIC_KEY`  | Your project's public key                                                                                          |
| `LUNARY_PRIVATE_KEY` | Your project's private key                                                                                         |
| `LUNARY_VERBOSE`     | Enable verbose logging                                                                                             |
| `LUNARY_API_URL`     | Base URL for the API server. Defaults to `https://api.lunary.ai`; can be customized for self-hosting or local use. |
| `DISABLE_SSL_VERIFY` | Disable SSL verification if set to `True`                                                                          |


# Concepts
Source: https://docs.lunary.ai/docs/more/concepts



Understanding these concepts can be useful for working with Lunary's APIs and SDKs, though they are not required to get started.

<Card title="Run" icon="play">
  Runs are the fundamental units in Lunary. They can represent an LLM request, an agent execution, a tool execution, a workflow, and more. Each run has an input and usually an output.

  You can track the number of runs on the billing page.

  Types of runs include:

  <Card title="LLM Calls" icon="microchip-ai">
    An LLM call refers to a request made to a large language model, such as GPT-4.

    In this context, `input` is the prompt or chat history you send to the model, and `output` is the response you get back.
  </Card>

  <Card title="Chains" icon="link">
    Chains denote sequences of connected runs, tools, and LLM calls.

    They help visualize the flow and dependencies in complex tasks, clarifying the interactions between different components of the system.

    They are useful for creating subtraces and subtrees inside agents.
  </Card>

  <Card title="Agents" icon="robot">
    An agent is usually composed of tools and LLM calls.

    It autonomously interacts with various components and might iterate over tasks until it finds a solution.
  </Card>

  <Card title="Tools" icon="wrench">
    A tool is a piece of code that your AI agent can invoke to perform external actions. A tool usually doesn't make AI queries itself (but it can).

    Examples of tools: Web search, Calculator, Database query, Random number generator

    In the context of a tool, `input` is the arguments you send to the tool, and `output` is the result you get back.
    Note that tools cannot be tracked standalone; they need to be part of an agent or a chain run.
  </Card>

  <Card title="Threads" icon="messages">
    A thread contains multiple `chat` runs and is used to represent a conversation or a chatbot session.

    You don't need to pass any `input` or `output` to a thread. You also don't need to end a thread explicitly.
  </Card>

  <Card title="Chat" icon="message">
    A chat is a run that represents a single interaction user->assistant in a conversation.
  </Card>
</Card>

<Card title="Traces" icon="list-tree">
  A trace is a collection of related runs.

  An agent will generate a trace every time it executes.

  Exploring traces on the dashboard helps you understand how your code is behaving and how the different LLM components are interacting.

  Using our SDKs, runs are automatically organized into traces.
</Card>

<Card title="Users" icon="users">
  A user is someone who uses your app. With all our SDKs, you can identify users.

  Sometimes, you might have multiple levels of users, such as organizations, teams within organizations, and individual users.

  Which to report as user then? It depends on your use case. For example, if you're building a chatbot, you might want to report the end-user as the user. If you're building a tool for a team, you might want to report the team as the user, to be able to track costs and usage grouped by team.

  In any case, you can pass an `organizationId` or `teamId` as metadata to identify those levels of users.

  [Learn more about users](/docs/features/users)
</Card>


# BigQuery Connector
Source: https://docs.lunary.ai/docs/more/data-warehouse/bigquery



## Setup Google Cloud

### Enable APIs

If not already done, enable the following APIs for the project where you want to install the Google BigQuery instance:

* [Datastream API](https://console.cloud.google.com/marketplace/product/google/datastream.googleapis.com)
* [BigQuery API](https://console.cloud.google.com/marketplace/product/google-cloud-platform/bigquery)

### Get your API Key

1. Go to [Create Service Account](https://console.cloud.google.com/iam-admin/serviceaccounts/create).
2. Give it the name `Lunary Data Warehouse Account`.
3. Click on **Create and continue**.
4. Click on **Select a role** and choose the `Datastream Admin` role.
5. Click on **Add another role**.
6. Click on **Select a role** and choose the `BigQuery Admin` role.
7. Click on **Continue**.
8. Click on **Done**.
9. Click on the `Lunary Data Warehouse Account`.
10. Click on **Keys**.
11. Click on **Add Key** and select the `Create new key` option from the drop-down menu.
12. Make sure `JSON` is selected for the **Key Type**, and click on **Create**.
13. Your private key will be downloaded to your computer. Save this private key.

## Setup PostgreSQL source

### Cloud SQL

1. Go to the [Cloud SQL](https://console.cloud.google.com/sql/instances) Instances page in the Google Cloud Console.
2. Select the instance to which you want Datastream to connect.
3. Click **Edit**.
4. Scroll down to the **Flags** section.
5. Click **ADD FLAG**.
6. Choose the `cloudsql.logical_decoding` flag from the drop-down menu.
7. Set its flag value to `on`.
8. Click `SAVE` to save your changes. You'll need to restart your instance to update it with the changes. Once your instance has been restarted, confirm your changes under **Database flags** on the Overview page.

### Amazon RDS

1. Launch your Amazon RDS Dashboard.
2. In the **Navigation Drawer**, click **Parameter Groups**, and then click **Create Parameter Group**. The **Create Parameter Group** page appears.
3. Select `PostgreSQL` for the database family, provide a name and description for the parameter group, and then click **Create**.
4. Select the check box to the left of your newly created parameter group, and then, under **Parameter Group Actions**, click **Edit**.
5. Set `logical_replication` to `1`.
6. Click **Save changes**.
7. In the **Navigation drawer**, click **Databases**.
8. Select your source, and then click **Modify**.
9. Scroll down to the **Additional configuration** section.
10. Select the parameter group that you created.
11. Click **Continue**.
12. Under **Scheduling of modifications**, select `Apply immediately`.

Because you've modified your source, you must wait until the changes to your parameter group are applied before proceeding.

13. In the **Navigation drawer**, click **Databases**, and then select your database instance.
14. Click the **Configurations** tab.
15. Verify that you see the parameter group that you created, and that its status is `pending-reboot`.
16. From the **Instance Actions** menu, select `Reboot`.

### Self-hosted PostgreSQL

1. Add `wal_level=logical` to the postgresql.conf file, or do this on the server command line.
2. Restart the server.


# CCPA compliance guide
Source: https://docs.lunary.ai/docs/more/security/CCPA



For those serving Californian users, grasping the nuances of secure and private data handling is crucial. Lunary, capable of being integrated into your own infrastructure without accessing your data, stands as a highly compliant CCPA observability solution.

This guide delves into [California Consumer Privacy Act (CCPA)](https://oag.ca.gov/privacy/ccpa), the types of data that need safeguarding, and how to to ensure your logs collection align with CCPA standards.

## What is the CCPA?

The CCPA empowers consumers with control over their personal data held by businesses, offering:

* Knowledge of, and details on, how their personal data is collected, utilized, and shared
* The ability to erase their personal data, subject to certain conditions
* The option to refuse the sale of their personal data
* Protection against discrimination when they exercise their CCPA rights.

## What data is protected under CCPA?

CCPA rights are exclusive to individuals residing in California, including those temporarily away from the state.

For-profit entities are subject to CCPA if they meet any of the criteria below:

* Their annual gross revenue exceeds \$25 million.
* They engage in buying, receiving, or selling the personal data of more than 50,000 California residents, households, or devices.
* At least 50% of their yearly revenue comes from selling the personal data of California residents.

Under CCPA, personal information encompasses data that can identify or be associated with an individual.

Essentially, personal information includes anything linked to an identifiable person, ranging from social security numbers and license plates to photographs, email addresses, web addresses, IP addresses, or pseudonyms.

## What is the impact of CCPA on observability?

Under CCPA, businesses are mandated to provide a "notice at collection" to consumers. This entails informing users upon registration about the utilization of their data to enhance the product.

Such a notice should enumerate the types of personal information collected and the reasons for its collection. Additionally, it must include a link to the privacy policy for further information on privacy practices.

CCPA also mandates the ability for users to request the deletion of their personal information, with businesses required to comply within 45 days.

## How to set Lunary up for CCPA compliance

Lunary can be hosted on your onwn infrastructure, giving you complete control over data management. This includes deciding the hosting location for personal information and full authority over the database, enabling straightforward sharing or deletion of individual data.

### Step 1: Choose how to host Lunary

For complete control of end-users' data, we recommend hosting Lunary on your own infrastructure, or a private cloud such as AWS, Google Cloud Platform or Microsoft Azure. A simpler alternative is to use Lunary Cloud, where we handle the infrastructure and security for you.

### Step 2: Deploy Lunary

If using Lunary Cloud, simply follow the steps in the onboarding process to start sending events. Read our [getting started guide](/docs/get-started) for more information on sending logs to Lunary. 

Setting up Lunary on your own infrastructure is simple, and our team is here to assist with any issues that arise. Begin by consulting our [self-hosting guide](/docs/more/self-hosting/docker).

### Step 3: Security configuration

Our SDKs used with Lunary Cloud utilize HTTPS to ensure the security of data during transmission. When self-hosting Lunary, we strongly recommend using HTTPS as well to secure data transmission.

It is highly advised to restrict access to Lunary and its underlying infrastructure strictly to individuals who have authorization and a legitimate need to interact with the data, this includes links to shared dashboards.

## Deleting personal information in Lunary

Users should have the capability to demand the deletion of their data. The method through which you accommodate such requests is at your discretion. For instance, you might choose to receive these requests through email or by a form.

You can remove a user from a Lunary instance via the Lunary user interface. To do this:

* Select "Users" from the sidebar menu
* Search and click on the concerned user
* Click "Delete" to remove them and all their associated data from Lunary.


# GDPR compliance guide
Source: https://docs.lunary.ai/docs/more/security/GDPR



The [General Data Protection Regulation (GDPR)](https://gdpr.eu/) represents a set of regulations on privacy and security, established and enacted by the European Union (EU). It mandates responsibilities for organizations globally, provided they process or gather data concerning individuals within the EU.

It is advisable to delve into the complete GDPR docs and consult with a legal expert to understand your specific responsibilities. Non-compliance with GDPR can lead to significant repercussions.

## What data is protected under GDPR?

Under GDPR, personal data is safeguarded, encompassing any details that can identify an individual either directly or indirectly. This includes, but is not limited to, names, email addresses, geographical data, ethnic background, gender, biometric details, religious convictions, internet cookies, and political views.

## What is the impact of GDPR on observability?

The primary guideline is to avoid gathering, storing, or utilizing any personal data without a valid justification, such as:

* The individual has provided explicit, clear consent for data processing (for instance, they have subscribed to your marketing emails).

* The processing is essential for the formation of a contract with someone (for example, conducting a background investigation is necessary).

* The processing is required to fulfill a legal duty (for example, responding to a court order in your area).

* The data needs to be processed to protect someone's life (in such cases, the circumstances will be evident).

* The processing is necessary to execute a task that serves the public interest or an official duty (for example, if you operate a private waste collection service).

* You possess a valid interest in processing an individual's personal data. This basis for processing is notably adaptable, yet the "fundamental rights and freedoms of the data subject" take precedence over your interests, particularly in the case of minors.

### You must acquire "Unambiguous Consent"

Specific guidelines exist regarding the definition of consent:

* Consent must be "freely given, specific, informed and unambiguous"

* Consent requests must be "clearly distinguishable from the other matters" and conveyed in "clear and plain language"

* At any time, data subjects are allowed to revoke their consent, and it's your responsibility to respect this choice

* Only with a parent's permission can children under the age of 13 provide consent

* Documentary proof of consent must be maintained by you

Therefore, if your product tracks users through Lunary, it's crucial to directly request their consent for this data usage and clearly detail how it will be employed at the time they register for your service.

### Data must be handled securely

It's mandatory to ensure data security through the adoption of "appropriate technical and organizational measures."

This encompasses technical strategies (such as data encryption) and organizational tactics (such as conducting staff training and restricting access to sensitive data).

In the event of a data breach, you are obligated to inform the affected individuals within 72 hours to avoid penalties. (However, this requirement for notification can be bypassed if technological protections, like encryption, are employed to make the data inaccessible to unauthorized parties.)

### You should not transfer EU users' personal data outside the EU

For those who have chosen to self-host Lunary on servers located outside the EU while handling data from EU users, it's advised to anonymize the personal data of such users.

Similarly, for users of Lunary Cloud, anonymizing personal data of EU users is also recommended.

## How to set Lunary up for GDPR compliance

The obligations under GDPR vary based on the manner in which your organization handles personal data. Entities can function as data controllers, data processors, or fulfill both roles simultaneously. [Data controllers](https://gdpr-info.eu/art-24-gdpr/) are responsible for collecting data from their end users and determining the purposes and means of processing that data. On the other hand, [data processors](https://gdpr-info.eu/art-28-gdpr/) are entities that process personal data on the instructions of another business.

You will be using Lunary in one of three ways:

1. Hosted and managed by us on Lunary Cloud
2. Hosted and managed by us on a region of your choice with the Dedicated option
3. Self-hosted by you on a private cloud or your own infrastructure

If you are using Lunary Cloud or then Lunary is the Data Processor and you are the Data Controller.

If you are self-hosting Lunary then you are both the Data Processor and the Data Controller because you are responsible for your Lunary instance.

### Step 1: Choose how to host Lunary

We recommend using Lunary Cloud for GDPR compliance. If self-hosting, the steps will depend on where you're hosting your data.

### Step 2: Deploy Lunary

If using Lunary Cloud, simply follow the steps in the onboarding process to start sending events. Read our [getting started guide](/docs/get-started) for more information on sending logs to Lunary.

Setting up Lunary on your own infrastructure is simple, and our team is here to assist with any issues that arise. Begin by consulting our [self-hosting guide](/docs/more/self-hosting/docker).

### Step 3: Security configuration

Our SDKs used with Lunary Cloud utilize HTTPS to ensure the security of data during transmission. When self-hosting Lunary, we strongly recommend using HTTPS as well to secure data transmission.

It is highly advised to restrict access to Lunary and its underlying infrastructure strictly to individuals who have authorization and a legitimate need to interact with the data, this includes links to shared dashboards.

### Step 4: Configure consent

Given that Lunary inherently collects data, which may include personal information, it's imperative to establish a method for obtaining consent for such data collection. This requirement aligns with the GDPR's [right to be informed](https://gdpr-info.eu/issues/right-to-be-informed/).

The consent form should clearly specify which categories of personal data are being gathered and the tools utilized for this collection:

* If you are using Lunary Cloud you should identify Lunary as a tool
* If you are self-hosting you can either not list a tool or provide a generic description such as "Monitoring".

If a user opts out then you must stop data capturing and processing. Here are some ways Lunary makes this possible:

* If Lunary has been initialized, call `lunary.opt_out()` in Python or `lunary.optOut()` in JS.

* Do not load the Lunary SDK.

* Do not initialize the Lunary SDK by setting an empty Public Key / Project ID.

## Complying with 'right to be forgotten' requests

Users should have the capability to demand the deletion of their data. The method through which you accommodate such requests is at your discretion. For instance, you might choose to receive these requests through email or by a form.

You can remove a user from a Lunary instance via the Lunary user interface. To do this:

* Select "Users" from the sidebar menu
* Search and click on the concerned user
* Click "Delete" to remove them and all their associated data from Lunary.


# Data Security
Source: https://docs.lunary.ai/docs/more/security/introduction



We take data security extremely seriously. A number of measures have been implemented to ensure the safety and security of your data.

## Security Measures

### Technical

When utilizing Lunary Cloud, we prioritize the security of your data through several key technical measures:

* **Encryption in Transit:** All data transmitted to and from the Lunary Cloud platform, as well as data communicated via our SDKs, is encrypted using HTTPS/TLS. This ensures that your data remains secure during its transmission over the internet.

* **Encryption at Rest:** On our production servers, we employ encryption at rest to protect your data. This means that all data stored on our servers is encrypted, providing an additional layer of security against unauthorized access.

* **Bug Bounties:** We actively participate in bug bounty programs, inviting security researchers to identify and report vulnerabilities in our system. This proactive approach allows us to continually enhance our security measures and protect your data against emerging threats.

* **Datacenter Security**: We use Hetzner as our server provider. Hetzner has implemented robust security measures for their data centers, including: high-security fencing with video monitoring, electronic access control via transponder key or card, 24/7 surveillance across all critical areas, diesel generator for power backup and advanced fire protection systems. Hetzner is DIN ISO/IEC 27001 certified.

### Organizational

Organizational measures are a critical component of our security framework, ensuring that our operations and employee behaviors align with our high standards for data protection. These measures include:

* **Security Training:** All employees undergo regular security awareness training to understand the latest threats and best practices for data protection.
* **Access Control:** Access to sensitive data is strictly controlled and limited to authorized personnel only, based on their role within the organization.
* **Data Privacy Policies:** We have comprehensive data privacy policies in place, which are regularly reviewed and updated to comply with current data protection laws.
* **Incident Response Plan:** A well-defined incident response plan is in place, allowing us to quickly address any security breaches and mitigate their impact.
* **Vendor Management:** We carefully assess and monitor all third-party vendors to ensure they meet our security standards, particularly those who handle or have access to our data.

### SOC 2 and ISO27001

Lunary is certified as SOC 2 Type 2 and ISO27001:2022 compliant, following external audits. Audit reports are available to Scale and Enterprise customers upon request.

### Policies

To support with compliance, we have established numerous policies. All team members are required to review these policies and complete security training and background checks as part of their onboarding process.

The following policies are available for review upon request:

* Physical Security Policy
* Access Control and Termination Policy
* Risk Assessment and Treatment Policy
* Incident Response Plan
* Secure Development Policy
* Vulnerability and Patch Management Policy
* Internal Control Policy
* Network Security Policy
* Data retention and Disposal Policy
* Data backup policy
* Business Continuity and Disaster Recovery Plan
* Third Party Risk Management policy

These policies are also pertinent to GDPR compliance (see below).

## GDPR

Customers can use Lunary in one of two ways:

* Lunary Cloud
* Self-hosting a Lunary instance

When using Lunary Cloud, Lunary acts as the Data Processor and the customer is the Data Controller. In this scenario, we have certain GDPR obligations to the customer's end users.

When self-hosting a Lunary instance, the customer is both the Data Processor and the Data Controller, as they are responsible for their instance. Since we do not have access to any user data in this case, we do not have specific GDPR obligations to the customer's end users.

Read our [GDPR compliance guide](/docs/more/security/GDPR) for more information.

### Lunary's Obligations as a Data Processor

We have examined our architecture, data flows, and agreements to ensure that our platform is GDPR compliant. Lunary Cloud does not interact directly with our customers’ end users, nor does it automatically collect personal data. However, our customers may collect and send personal data to Lunary for processing.

Lunary does not require personally identifiable information or personal data to enable LLM observability.

## CCPA

Under the California Consumer Privacy Act (CCPA), Lunary serves as a Service Provider to Lunary Cloud customers only. This role is similar to the Processor role under GDPR. Our Privacy Policy includes a CCPA Addendum.

We equip all Lunary customers with the tools necessary to comply with their end users' requests under CCPA, including data deletion. We provide detailed guidance for our customers on how to use Lunary in a CCPA-compliant manner in our docs.

We process data collected by our customers from end-users and enable them to understand usage metrics of their products. We do not access customer end-user data unless directed by a customer, and we never sell customer data to third parties. We do not have access to data collected by customers who self-host Lunary from their end-users, unless they grant us access to their instance.

Read our [CCPA compliance guide](/docs/more/security/CCPA) for more information.

## HIPAA

By self-hosting Lunary on your own infrastructure, you maintain full control of your data, making it an ideal solution for LLM observability in healthcare settings.

Since you retain full control, there is no need to sign a Business Associate Agreement with us.

Lunary Cloud is not suitable for HIPAA-compliant data collection.

## Security Contact

Please reach out at `security@lunary.ai` for any security-related question.


# Docker
Source: https://docs.lunary.ai/docs/more/self-hosting/docker



Lunary is designed to be simple to self-host using Docker images for the backend and frontend components.

<Note>Note: The Docker setup is available only with [Lunary Enterprise Edition](https://lunary.ai/pricing)</Note>

<Steps>
  <Step title="Set up a PostgreSQL database">
    ta (version 15 or higher).
  </Step>

  <Step title="Log in to the private Docker Repository">
    Make sure Docker is installed on your host machine before running the following command:

    ```bash  theme={null}
    docker login -u lunarycustomer
    ```

    Then, paste your organization's access token, which will be provided by Lunary when your subscription is activated.
  </Step>

  <Step title="Run the Docker images">
    Run the following commands to start the Lunary Docker images:

    For the backend:

    ```bash  theme={null}
    docker run -d \
      -e DATABASE_URL="postgresql://<username>:<password>@<host>:<port>/<dbname>" \
      -e API_URL="http://<your-backend-ip>:3333" \
      -e APP_URL="http://<your-frontend-ip>:8080" \
      -e JWT_SECRET="<jwt_secret>" \
      -e LICENSE_KEY="<your_license_key>" \
      -p "3333:3333" \
      lunary/backend:1.4.8
    ```

    For the frontend:

    ```bash  theme={null}
    docker run -d \
      -e API_URL="http://<your-backend-ip>:3333" \
      -e APP_URL="http://<your-frontend-ip>:8080" \
      -p "8080:8080" \
      lunary/frontend:1.4.8
    ```

    Note: Replace `<your-backend-ip>` and `<your-frontend-ip>` with your actual IP addresses or domain names.
  </Step>

  <Step title="Configure optional environment variables">
    The following environment variables are optional and can be used to enable the playground, evaluation, and radar features:

    ```bash  theme={null}
    OPENAI_API_KEY=sk-...
    # Or if using Azure OpenAI:
    AZURE_OPENAI_API_KEY=...
    AZURE_OPENAI_RESOURCE_NAME=...
    AZURE_OPENAI_DEPLOYMENT_ID=...

    ANTHROPIC_API_KEY=sk-...
    OPENROUTER_API_KEY=sk-...
    PALM_API_KEY=AI...
    ```

    You can also use your custom email server for sending invite members to your organization:

    ```bash  theme={null}
    EMAIL_SENDER_ADDRESS=...
    SMTP_HOST=...
    SMTP_PORT=...
    SMTP_USER=...
    SMTP_PASSWORD=...
    ```

    If those values are not provided, no email will be send and you will need to send the invitation links manually.
  </Step>

  <Step title="🎉 Done!">
    You're all set! Open `http://<your-frontend-ip-or-url>:8080` to access the app. <br />
    Make sure to export the environment variable `LUNARY_API_URL=http://<your-backend-ip-or-url>:3333` when using the SDK to send queries to your server.
  </Step>
</Steps>

## Troubleshooting

### Requested access to the resource is denied.

You need to log in to the private Docker repository before running the image. Make sure you have the correct access token and that you are logged in.

### Error: connect ECONNREFUSED 127.0.0.1:5432

If you are running the database on the same machine, you can use `--network=host` when running the Docker images.

```bash  theme={null}
docker run -d \
  -e DATABASE_URL="postgresql://postgres:mysecretpassword@localhost:5432/lunary" \
  --network=host \
  -e API_URL="http://localhost:3333" \
  -e JWT_SECRET="replace_with_your_secret_string" \
  lunary/backend:1.4.8
```

### Error: Client network socket disconnected before secure TLS connection was established

This means the database's SSL certificate is not properly set. Either fix the SSL certificate or disable SSL by removing `?sslmode=require` from the `DATABASE_URL` environment variable (not recommended if the database is exposed to the internet).


# Docker Compose
Source: https://docs.lunary.ai/docs/more/self-hosting/docker-compose



Lunary is designed to be simple to self-host using Docker Compose, which makes managing all components easier.

<Note>
  Note: The Docker Compose setup is **available** only with [Lunary Enterprise
  Edition](https://lunary.ai/pricing)
</Note>

## Steps

<Steps>
  <Step title="Set up a PostgreSQL database">
    First, set up a PostgreSQL database (version 15 or higher). This can be on the same host or a separate server.

    You'll need the following information for your database:

    * Host address and port
    * Database name
    * Username and password with appropriate permissions

    For production use, we recommend using a managed PostgreSQL service or properly configuring your self-hosted PostgreSQL instance with backups and security.
  </Step>

  <Step title="Log in to the private Docker Repository">
    Make sure Docker is installed on your host machine before running the following command:

    ```bash  theme={null}
    docker login -u lunarycustomer
    ```

    Then, paste your organization's access token, which will be provided by Lunary when your subscription is activated.
  </Step>

  <Step title="Create the Docker Compose file">
    Create a new directory for your Lunary installation and create a `docker-compose.yml` file with the following content:

    ```yaml  theme={null}
    services:
      backend:
        container_name: lunary-backend
        image: lunary/backend:latest # or specific version (lunary/backend:1.9.8 - contact Lunary support for available versions)
        ports:
          - "3333:3333"
        restart: unless-stopped
        environment:
          DATABASE_URL: ${DATABASE_URL}
          API_URL: ${API_URL:-http://localhost:3333}
          APP_URL: ${APP_URL:-http://localhost:8080}
          JWT_SECRET: ${JWT_SECRET}
          LICENSE_KEY: ${LICENSE_KEY}
          IS_SELF_HOSTED: "true"
          # Optional environment variables for playground
          OPENAI_API_KEY: ${OPENAI_API_KEY:-}
          AZURE_OPENAI_API_KEY: ${AZURE_OPENAI_API_KEY:-}
          AZURE_OPENAI_RESOURCE_NAME: ${AZURE_OPENAI_RESOURCE_NAME:-}
          AZURE_OPENAI_DEPLOYMENT_ID: ${AZURE_OPENAI_DEPLOYMENT_ID:-}
          ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY:-}
          OPENROUTER_API_KEY: ${OPENROUTER_API_KEY:-}
          PALM_API_KEY: ${PALM_API_KEY:-}
          # Email configuration
          EMAIL_SENDER_ADDRESS: ${EMAIL_SENDER_ADDRESS:-}
          SMTP_HOST: ${SMTP_HOST:-}
          SMTP_PORT: ${SMTP_PORT:-}
          SMTP_USER: ${SMTP_USER:-}
          SMTP_PASSWORD: ${SMTP_PASSWORD:-}
        networks:
          - lunary-network
        depends_on:
          - ml
          - enrichers
        healthcheck:
          test: ["CMD", "curl", "-f", "http://localhost:3333/v1/health"]
          interval: 10s
          start_period: 20s
          timeout: 10s
          retries: 3

      frontend:
        container_name: lunary-frontend
        image: lunary/frontend:latest
        ports:
          - "8080:8080"
        restart: unless-stopped
        environment:
          API_URL: ${API_URL:-http://localhost:3333}
          APP_URL: ${APP_URL:-http://localhost:8080}
        networks:
          - lunary-network
        depends_on:
          - backend
        healthcheck:
          test: ["CMD", "curl", "-f", "http://localhost:8080"]
          interval: 10s
          start_period: 20s
          timeout: 10s
          retries: 3

      enrichers:
        container_name: lunary-enrichers
        image: lunary/realtime-evaluators:latest
        ports:
          - "3334:3333"
        restart: unless-stopped
        environment:
          DATABASE_URL: ${DATABASE_URL}
          ML_URL: http://ml:4242
        networks:
          - lunary-network
        depends_on:
          - ml

      ml:
        container_name: lunary-ml
        image: lunary/ml:latest
        ports:
          - "4242:4242"
        restart: unless-stopped
        environment:
          DATABASE_URL: ${DATABASE_URL}
        networks:
          - lunary-network
        healthcheck:
          test: ["CMD", "curl", "-f", "http://localhost:4242/health"]
          interval: 20s
          start_period: 80s
          timeout: 10s
          retries: 5

      autoheal:
        restart: always
        image: willfarrell/autoheal
        environment:
          AUTOHEAL_CONTAINER_LABEL: all
        volumes:
          - /var/run/docker.sock:/var/run/docker.sock

    networks:
      lunary-network:
    ```

    This configuration includes:

    * `backend`: The Lunary API server
    * `frontend`: The Lunary web interface
    * `enrichers`: Enriches your data by communicating with the ml service
    * `ml`: The machine learning service for advanced features
    * `autoheal`: A service to automatically restart unhealthy containers

    Each service is configured with health checks to ensure reliability.
  </Step>

  <Step title="Create the environment file">
    In the same directory, create a `.env` file with the following variables:

    ```env  theme={null}
    # Required configuration
    DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<dbname>
    API_URL=http://localhost:3333
    APP_URL=http://localhost:8080
    JWT_SECRET=<your_jwt_secret>
    LICENSE_KEY=<your_license_key>

    # Optional: API keys for AI services (needed for playground)
    OPENAI_API_KEY=
    ANTHROPIC_API_KEY=
    OPENROUTER_API_KEY=
    PALM_API_KEY=

    # Optional: Azure OpenAI configuration
    AZURE_OPENAI_API_KEY=
    AZURE_OPENAI_RESOURCE_NAME=
    AZURE_OPENAI_DEPLOYMENT_ID=

    # Optional: Email configuration (if not provided, no emails will be sent)
    EMAIL_SENDER_ADDRESS=
    SMTP_HOST=
    SMTP_PORT=
    SMTP_USER=
    SMTP_PASSWORD=
    ```

    Replace the placeholder values with your actual configuration:

    * `<username>, <password>, <host>, <port>, <dbname>`: Your PostgreSQL database credentials
    * `<your-backend-ip-or-url>`, `<your-frontend-ip-or-url>`: Your server's IP address or domain name
    * `<your_jwt_secret>`: A secure random string for JWT token generation
    * `<your_license_key>`: Your Lunary Enterprise Edition license key

    The other environment variables are optional and enable specific features:

    * API keys for various AI services enable the playground
    * Email configuration allows Lunary to send invitation emails to organization members

    ````
    </Step>


    <Step title="Start the services" >
    Run the following command to start all services:

    ```bash
    docker compose up -d
    ````

    This will pull the necessary images and start all services in detached mode. You can check the status of your services with:

    ```bash  theme={null}
    docker compose ps
    ```

    And view logs with:

    ```bash  theme={null}
    docker compose logs -f
    ```

    Or for a specific service:

    ```bash  theme={null}
    docker compose logs -f backend
    ```
  </Step>

  <Step title="🎉 Done!">
    You're all set! Open `http://<your-frontend-ip-or-url>:8080` to access the app. <br />
    Make sure to export the environment variable `LUNARY_API_URL=http://<your-backend-ip-or-url>:3333` when using the SDK to send queries to your server.
  </Step>
</Steps>

## Troubleshooting

### Requested access to the resource is denied

You need to log in to the private Docker repository before running the containers. Make sure you have the correct access token and that you are logged in:

```bash  theme={null}
docker login -u lunarycustomer
```

### Cannot connect to the database

Verify that your `DATABASE_URL` is correct and that the database is accessible from the Docker containers. If your PostgreSQL server is on the same host, make sure it's configured to accept connections from Docker containers.

### Container health checks are failing

Check the container logs for specific error messages:

```bash  theme={null}
docker compose logs backend
docker compose logs ml
docker compose logs enrichers
docker compose logs frontend
```

### Error: Client network socket disconnected before secure TLS connection was established

This means the database's SSL certificate is not properly set. Either fix the SSL certificate or disable SSL by adding `?sslmode=disable` to the `DATABASE_URL` environment variable (not recommended if the database is exposed to the internet):

```
DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<dbname>?sslmode=disable
```

### Services are not communicating with each other

If services can't communicate with each other despite being on the same Docker network, check that the service names match the hostnames used in environment variables (e.g., `ML_URL` should be `http://ml:3333` to properly resolve the ML service).

### Frontend showing "Failed to connect to the API"

This typically happens when:

1. The backend service is not running or healthy
2. The `API_URL` is not correctly set in the frontend service
3. There's a network issue preventing the frontend from reaching the backend

Check the backend logs and verify that the `API_URL` is correctly set in both the frontend container and your browser's environment.

## Upgrading

To upgrade to a newer version of Lunary:

1. Pull the latest images:

   ```bash  theme={null}
   docker compose pull
   ```

2. Restart the services:
   ```bash  theme={null}
   docker compose down
   docker compose up -d
   ```

This will update all services to the latest available versions while preserving your configuration.


# Kubernetes
Source: https://docs.lunary.ai/docs/more/self-hosting/kubernetes



Lunary was designed to be surprisingly simple to self-host, through a Helm Chart which includes the frontend, the API, and workers.<br />

<Note>
  Note: The Kubernetes setup is available only with [Lunary Enterprise
  Edition](https://lunary.ai/pricing)
</Note>

## Steps

<Steps>
  <Step title="Set up a PostgreSQL database">
    Set up a PostgreSQL database to store your Lunary data (version 15 or higher).
  </Step>

  <Step title="Log in to the private Docker Repository">
    Run the following command:

    ```bash  theme={null}
    helm registry login registry-1.docker.io -u lunarycustomer -p <your_organization_access_token>
    ```

    Your Organization's Access Token, will be provided by Lunary when your subscription is activated.
  </Step>

  <Step title="Download the Helm Chart">
    ```bash  theme={null}
    kubectl create ns lunary
    helm pull oci://registry-1.docker.io/lunary/lunary --untar --version '1.2.11' # contact Lunary support to get the latest version list
    ```
  </Step>

  <Step title="Set up mandatory secrets">
    ```bash  theme={null}
    kubectl create secret -n lunary docker-registry regcred --docker-server=docker.io --docker-username=lunarycustomer --docker-password=<your_organization_access_token>
    kubectl create secret -n lunary generic db-connection --from-literal=url="postgres://<username>:<password>@<host>:5432/lunary"
    kubectl create secret -n lunary generic license-key --from-literal=LICENSE_KEY='<license_key>'
    kubectl create secret -n lunary generic jwt-secret --from-literal=JWT_SECRET='<jwt_secret>' # You can generate a random string using `openssl rand -base64 32`
    ```

    Your License Key will be provided by Lunary when your subscription is activated.
    The Organization Access Token is the same one you used to log in with `helm login`.
  </Step>

  <Step title="(Optional) Set up API Keys and SMTP client">
    In order to use the Prompt Playground and [Evaluations](https://lunary.ai/docs/features/evals) features, you need to set up at least one of the following secrets:

    ```bash  theme={null}
    kubectl create secret -n lunary generic api-keys \
      --from-literal=OPENAI_API_KEY='<your-openai-api-key>' \
      # Or if using Azure
      --from-literal=AZURE_OPENAI_API_KEY='<your-azure-openai-api-key>' \
      --from-literal=AZURE_OPENAI_RESOURCE_NAME='<your-azure-openai-resource-name>' \
      --from-literal=AZURE_OPENAI_DEPLOYMENT_ID='<your-azure-openai-deployment-id>' \
      --from-literal=ANTHROPIC_API_KEY='<your-anthropic-api-key>' \
      --from-literal=OPENROUTER_API_KEY='<your-openrouter-api-key>' \
      --from-literal=PALM_API_KEY='<your-palm-api-key>'

    ```

    You can also use your custom email server to send invitations to members of your organization:

    ```bash  theme={null}
    kubectl create secret -n lunary generic smtp-config \
      --from-literal=EMAIL_SENDER_ADDRESS='<your-email-sender-address>' \
      --from-literal=SMTP_HOST='<your-smtp-host>' \
      --from-literal=SMTP_PORT='<your-smtp-port>' \
      --from-literal=SMTP_USER='<your-smtp-user>' \
      --from-literal=SMTP_PASSWORD='<your-smtp-password>
    ```

    Then, configure the corresponding values in `values.yaml`, in the Helm Chart's root directory:

    ```yaml  theme={null}
     ---
    global:
      ...
      secrets:
        useCustomSMTP: true
        useOpenAI: false
        useAzureOpenAI: true
        useAnthropic: true
        useOpenRouter: true
        usePalm: true
    ...

    ```
  </Step>

  <Step title="Install the Helm Chart">
    <Alert>
      Note: Before installing, please review at least the top-level values.yaml file. If you wish, it may also be useful to dive into the individual subchart values.yaml files for more custom configuration.
    </Alert>

    ```bash  theme={null}
    cd lunary
    helm upgrade --install -n lunary lunary .
    ```
  </Step>

  <Step title="🎉 Done!">
    The Helm Chart should be installed and ready to go.<br />
    You can now set up an ingress controller to expose the services.
  </Step>
</Steps>


