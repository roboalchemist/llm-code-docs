# Source: https://docs.pinecone.io/guides/assistant/pricing-and-limits.md

# Pricing and limits

> Understand Pinecone Assistant pricing and service limits.

Pricing and limits vary based on [subscription plan](https://www.pinecone.io/pricing/).

## Pricing

The cost of using Pinecone Assistant is determined by the following factors:

* Monthly usage
* Hourly rate
* Tokens used
* Storage

### Minimum usage

The Standard and Enterprise [pricing plans](https://www.pinecone.io/pricing/) include a monthly minimum usage committment:

| Plan       | Minimum usage |
| ---------- | ------------- |
| Starter    | \$0/month     |
| Standard   | \$50/month    |
| Enterprise | \$500/month   |

Beyond the monthly minimum, customers are charged for what they use each month.

**Examples**

<AccordionGroup>
  <Accordion title="Usage below monthly minimum">
    * You are on the Standard plan.
    * Your usage for the month of August amounts to \$20.
    * Your usage is below the \$50 monthly minimum, so your total for the month is \$50.

    In this case, the August invoice would include line items for each service you used (totaling \$20), plus a single line item covering the rest of the minimum usage commitment (\$30).
  </Accordion>

  <Accordion title="Usage exceeds monthly minimum">
    * You are on the Standard plan.
    * Your usage for the month of August amounts to \$100.
    * Your usage exceeds the \$50 monthly minimum, so your total for the month is \$100.

    In this case, the August invoice would only show line items for each service you used (totaling \$100). Since your usage exceeds the minimum usage commitment, you are only charged for your actual usage and no additional minimum usage line item appears on your invoice.
  </Accordion>
</AccordionGroup>

### Hourly rate

For paid plans, you are charged an hourly rate for each assistant, regardless of assistant activity.

| Plan       | Hourly rate |
| ---------- | ----------- |
| Starter    | Free        |
| Standard   | \$0.05/hour |
| Enterprise | \$0.05/hour |

### Tokens

For paid plans, you are charged for the number of tokens used by each assistant.

#### Chat tokens

[Chatting with an assistant](/guides/assistant/chat-with-assistant) involves both input and output tokens:

* **Input tokens** are based on the messages sent to the assistant and the context snippets retrieved from the assistant and sent to a model. Messages sent to the assistant can include messages from the [chat history](/guides/assistant/chat-with-assistant#provide-conversation-history) in addition to the newest message.

* **Output tokens** are based on the answer from the model.

| Plan       | Input token rate            | Output token rate           |
| ---------- | --------------------------- | --------------------------- |
| Starter    | Free (1.5M max per project) | Free (200k max per project) |
| Standard   | \$8/million tokens          | \$15/million tokens         |
| Enterprise | \$8/million tokens          | \$15/million tokens         |

<Note>
  Chat input tokens appear as "Assistants Input Tokens" on invoices and `prompt_tokens` in API responses. Chat output tokens appear as "Assistants Output Tokens"" on invoices and `completion_tokens` in API responses.
</Note>

#### Context tokens

When you [retrieve context snippets](/guides/assistant/context-snippets-overview), tokens are based on the messages sent to the assistant and the context snippets retrieved from the assistant. Messages sent to the assistant can include messages from the [chat history](/guides/assistant/chat-with-assistant#provide-conversation-history) in addition to the newest message.

| Plan       | Token rate                  |
| ---------- | --------------------------- |
| Starter    | Free (500k max per project) |
| Standard   | \$5/million tokens          |
| Enterprise | \$8/million tokens          |

<Note>
  Context retrieval tokens appear as **Assistants Context Tokens Processed** on invoices and `prompt_tokens` in API responses. In API responses, `completion_tokens` will always be 0 because, unlike for chat, there is no answer from a model.
</Note>

#### Evaluation tokens

[Evaluating responses](/guides/assistant/evaluation-overview) involves both input and output tokens:

* **Input tokens** are based on two requests to a model: The first request contains a question, answer, and ground truth answer, and the second request contains the same details plus generated facts returned by the model for the first request.
* **Output tokens** are based on two responses from a model: The first response contains generated facts, and the second response contains evaluation metrics.

| Plan       | Input token rate   | Output token rate   |
| ---------- | ------------------ | ------------------- |
| Starter    | Not available      | Not available       |
| Standard   | \$8/million tokens | \$15/million tokens |
| Enterprise | \$8/million tokens | \$15/million tokens |

<Note>
  Evaluation input tokens appear as **Assistants Evaluation Tokens Processed** on invoices and `prompt_tokens` in API responses. Evalulation output tokens appear as as **Assistants Evaluation Tokens Out** on invoices and `completion_tokens` in API responses.
</Note>

### Storage

For paid plans, you are charged for the size of each assistant.

| Plan       | Storage rate                |
| ---------- | --------------------------- |
| Starter    | Free (1 GB max per project) |
| Standard   | \$3/GB per month            |
| Enterprise | \$3/GB per month            |

## Limits

Pinecone Assistant limits vary based on [subscription plan](https://www.pinecone.io/pricing/).

### Object limits

Object limits are restrictions on the number or size of assistant-related objects.

| Metric                               | Starter plan  | Standard plan | Enterprise plan |
| :----------------------------------- | :------------ | :------------ | :-------------- |
| Assistants per project               | 5             | Unlimited     | Unlimited       |
| File storage per project             | 1 GB          | Unlimited     | Unlimited       |
| Chat input tokens per project        | 1,500,000     | Unlimited     | Unlimited       |
| Chat output tokens per project       | 200,000       | Unlimited     | Unlimited       |
| Context retrieval tokens per project | 500,000       | Unlimited     | Unlimited       |
| Evaluation input tokens per project  | Not available | 150,000       | 500,000         |
| Files per assistant                  | 100           | 10,000        | 10,000          |
| File size (.docx, .json, .md, .txt)  | 10 MB         | 10 MB         | 10 MB           |
| File size (.pdf)                     | 10 MB         | 100 MB        | 100 MB          |
| Metadata size per file               | 16 KB         | 16 KB         | 16 KB           |

Additionally, the following limits apply to [multimodal PDFs](/guides/assistant/multimodal) (currently in [public preview](/release-notes/feature-availability)):

| Metric                        | Starter plan | Standard plan | Enterprise plan |
| :---------------------------- | :----------- | :------------ | :-------------- |
| Max file size                 | 10 MB        | 50 MB         | 50 MB           |
| Page limit                    | 100          | 100           | 100             |
| Multimodal PDFs per assistant | 1            | 20            | 20              |

### Rate limits

Rate limits help protect your applications from misuse and maintain the health of our shared infrastructure. These limits are designed to support typical production workloads while ensuring reliable performance for all users.

**Most rate limits can be adjusted upon request.** If you need higher limits to scale your application, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) with details about your use case.

Requests that exceed a rate limit fail and return a `429 - TOO_MANY_REQUESTS` status.

<Tip>To handle rate limits, implement [retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic).</Tip>

| Metric                                      | Starter plan | Standard plan | Enterprise plan |
| :------------------------------------------ | :----------- | :------------ | :-------------- |
| Assistant list/get requests per minute      | 40           | 100           | 500             |
| Assistant create/update requests per minute | 20           | 50            | 100             |
| Assistant delete requests per minute        | 20           | 50            | 100             |
| File get requests per minute                | 100          | 300           | 6,000           |
| File list requests per minute               | 50           | 150           | 3,000           |
| File upload requests per minute             | 5            | 20            | 300             |
| File delete requests per minute             | 5            | 20            | 300             |
| Chat input tokens per minute                | 100,000      | 300,000       | 1,000,000       |
| Chat history tokens per query               | 64,000       | 64,000        | 64,000          |
