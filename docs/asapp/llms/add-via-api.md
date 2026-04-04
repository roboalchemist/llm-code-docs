# Source: https://docs.asapp.com/generativeagent/configuring/connecting-your-knowledge-base/add-via-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add via API

> Learn how to add Knowledge Base articles programmatically using the API

The Knowledge Base Article Submission API offers an alternative to manual creation of article snippets and URL imports. This is especially beneficial for large data sources that are not easily scraped, such as internal knowledge bases or articles within a Content Management System.

All content imported via API follows the [Imported Articles](/generativeagent/configuring/connecting-your-knowledge-base#imported-articles) review process.

## Before you Begin

Before using the Knowledge Base Article Submission API, you need to:

* [Get your API Key Id and Secret](/getting-started/developers#access-api-credentials)
* Ensure your API key has been configured to access Knowledge Base APIs. Reach out to your ASAPP team if you need access enabled.

## Step 1: Create a submission

To import an article via API, you need to create a `submission`. A **submission** is the attempt to import an article. It will still need to be reviewed and published like any other imported article.

To [create a submission](/apis/knowledge-base/create-a-submission), you need to specify:

* `title`: The title of the article
* `content`: The content of the article

<Note>
  There are additional optional fields that can be used to improve the articles such as `url`, `metadata`, and `queryExamples`. More information can be found in the [API Reference](/apis/knowledge-base/create-a-submission).
</Note>

As an example, here's a request to create a submission for an article including additional values such as `url` and `metadata`:

```json  theme={null}
curl --request POST \
  --url https://api.sandbox.asapp.com/knowledge-base/v1/submissions \
  --header 'Content-Type: application/json' \
  --header 'asapp-api-id: <api-key>' \
  --header 'asapp-api-secret: <api-key>' \
  --data '{
  "title": "5G Data Plan",
  "content": "Our 5G data plans offer lightning-fast speeds and generous data allowances. The Basic 5G plan includes 50GB of data per month, while our Unlimited 5G plan offers truly unlimited data with no speed caps. Both plans include unlimited calls and texts within the country. International roaming can be added for an additional fee.",
  "url": "https://example.com/5g-data-plans",
  "metadata": [
    {
      "key": "department",
      "value": "Customer experience"
    }
  ],
  "queryExamples": [
    "What 5G plans do you offer?",
    "Is there an unlimited 5G plan?"
  ],
  "additionalInstructions": [
    {
      "clarificationInstruction": "Emphasize that 5G coverage may vary by location",
      "exampleResponse": "Our 5G plans offer great speeds and data allowances, but please note that 5G coverage may vary depending on your location. You can check coverage in your area on our website."
    }
  ]
}'
```

## Step 2: Article Processing

The Article Submission API submits the article that will still need review and publication like any other imported article.

You can check the status of the submission by calling the [Get a Submission](/apis/knowledge-base/retrieve-a-submission) API.

The response will include the `id` of the submission and the `status` of the submission.

```json  theme={null}
{
  "id": "fddd060c-22d7-4aed-acae-8f8dcc093a88",
  "articleId": "8f8dcc09-22d7-4aed-acae-fddd060c3a88",
  "submittedAt": "2024-12-12T00:00:00",
  "title": "5G Data Plan",
  "content": "Our 5G data plans offer lightning-fast speeds and generous data allowances...",
  "status": "PENDING_REVIEW"
}
```

## Step 3: Publication and Updates

Once you approve the submission, the system will publish the article and make it available in the Knowledge Base. The status of the submission will update to `ACCEPTED` and you will see it within the ASAPP AI-Console UI.

You can also update the article after the system has published it by creating another submission with the same `articleId`.

## Troubleshooting

Common API response codes and their solutions:

<AccordionGroup>
  <Accordion title="500 - Internal Server Error">
    If you receive a `500` code, there is an issue with the server. Wait and try again.

    If the error persists, contact your ASAPP Team.
  </Accordion>

  <Accordion title="400 - Bad Request">
    The `400` code usually means missing required parameters.

    Recheck your request body and try again.
  </Accordion>

  <Accordion title="401 - Unauthorized">
    A `401` code indicates incorrect credentials or unconfigured ASAPP credentials.
  </Accordion>

  <Accordion title="413 - Request Entity Too Large">
    The request body is too large. Article content is limited to 200,000 Unicode characters.

    Try again with less content.
  </Accordion>
</AccordionGroup>

## Next Steps

<CardGroup>
  <Card title="Knowledge Base API Reference" href="/apis/knowledge-base">
    View the Knowledge Base API documentation
  </Card>

  <Card title="Connecting your Knowledge Base" href="/generativeagent/configuring/connecting-your-knowledge-base">
    Learn more about managing your Knowledge Base articles
  </Card>

  <Card title="Configuring GenerativeAgent" href="/generativeagent/configuring">
    Configure how GenerativeAgent uses your Knowledge Base
  </Card>

  <Card title="Go Live" href="/generativeagent/go-live">
    Deploy your Knowledge Base to production
  </Card>
</CardGroup>
