# Source: https://braintrust.dev/docs/api-reference/introduction.md

# API Reference

> Complete API reference for the Braintrust API

## Welcome to the Braintrust API

The Braintrust API allows you to interact with all aspects of the Braintrust platform programmatically. You can use it to:

* Create and manage projects, experiments, and datasets
* Log traces and metrics
* Manage prompts, tools, and scorers
* Configure access control and permissions
* Retrieve and analyze results

## Base URL

The API is hosted globally at:

```
https://api.braintrust.dev
```

## Authentication

Most Braintrust endpoints are authenticated by providing your API key as a header to your HTTP request:

```
Authorization: Bearer [api_key]
```

You can create an API key in the Braintrust [organization settings page](https://www.braintrust.dev/app/settings?subroute=api-keys).

## SDKs

While you can call the API directly, we recommend using one of our official SDKs:

<CardGroup cols={2}>
  <Card title="TypeScript SDK" icon="js" href="https://github.com/braintrustdata/braintrust-sdk">
    Official TypeScript/JavaScript SDK
  </Card>

  <Card title="Python SDK" icon="python" href="https://github.com/braintrustdata/braintrust-sdk">
    Official Python SDK
  </Card>
</CardGroup>

## API Resources

The API is organized around REST principles. Each resource has predictable URLs and uses HTTP response codes to indicate API errors. We use built-in HTTP features, like HTTP authentication and HTTP verbs.

### Core Resources

* **Projects**: Organize your AI features and experiments
* **Experiments**: Run and track evaluation experiments
* **Datasets**: Manage test data for evaluations
* **Logs**: Store and query production traces
* **Prompts**: Version control your prompts
* **Functions**: Manage tools, scorers, and agents

### Organization Resources

* **Organizations**: Manage your organization settings
* **Users**: Manage team members
* **Roles & ACLs**: Configure access control

## Response Format

All API responses are returned in JSON format. Successful responses will have a `2xx` status code, while errors will return `4xx` or `5xx` status codes with error details.

## Rate Limits

The API uses rate limiting to ensure fair usage. Rate limits are applied per organization and endpoint. If you exceed the rate limit, you'll receive a `429 Too Many Requests` response.

## Support

Need help with the API?

* Join our [Discord community](https://discord.gg/6G8s47F44X)
* Check the [GitHub repository](https://github.com/braintrustdata/braintrust-sdk)
* Email us at [support@braintrust.dev](mailto:support@braintrust.dev)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt