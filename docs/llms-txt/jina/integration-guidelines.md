# Integration guidelines

You should always:
- Handle API errors using try/catch blocks;
- Implement retries for network failures;
- Validate inputs before API calls;
- Pay attention to the response of each API and parse it to a usable state;

You should not:
- Chain API's unnecessarily;
- Use reranker API without query-document pairs (reranker API needs a query as context to estimate relevancy);
- Directly use the response of an API without parsing it;