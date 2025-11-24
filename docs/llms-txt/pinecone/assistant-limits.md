# Source: https://docs.pinecone.io/reference/api/assistant/assistant-limits.md

# Pinecone Assistant limits

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
