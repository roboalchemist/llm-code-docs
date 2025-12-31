# Source: https://docs.avaamo.com/user-guide/llamb/citation-links.md

# Citation links

In LLaMB responses, citation links are references provided by the agent to indicate the source of information. They often point to [ingested documents](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/upload-content) or [preview URLs ](https://docs.avaamo.com/user-guide/get-started/step-2-ingest-enterprise-content/common-actions#edit)added during the document ingestion. This feature adds credibility to the information displayed to the user.

For example, when LLaMB responds based on an ingested document, it can include a clickable hyperlink pointing to the section or location in the document from which the information was drawn. This enables users to view the source for more context or additional details.

## **Citation links security**

When a citation link is included in a response, it is authenticated and authorized before redirecting to the document's URL with an expiration time. This ensures that only the intended users can access the document for a limited time.

### 1. Authorization Expiry

{% hint style="success" %}
**Key point:** Authorization Expiry applies exclusively to non-web channels.
{% endhint %}

* The citation links have an expiration time of **24 hours** from the moment of generation.

**For example:** When a user submits a query to the agent and the agent responds with citation links, these links remain valid for 24 hours. Access is prohibited if the citation links are accessed beyond this period or from the same response after the expiration. To retrieve a valid citation link, the user must resubmit the original query to generate new citation links, which can then be used to access the referenced document.

* Document URLs have an expiration time of **one minute** from the moment of generation.

### 2. URL format

The format of the citation link includes security tokens for validation. Below is the format:

{% code overflow="wrap" %}

```
https://cx.avaamo.com/llamb/messages/{message_uuid}/documents/{document_uuid}?lt={base64_encoded_JWT_token}&page={page_number}
```

{% endcode %}

## **Key points**

* Authorization Expiry applies exclusively to non-web channels.
* Citation links in the [Conversation history](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents/conversation-history) page are always accessible without limitations on access duration and can be used for debugging.
