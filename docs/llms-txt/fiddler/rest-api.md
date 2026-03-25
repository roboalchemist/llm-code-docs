# Source: https://docs.fiddler.ai/api/rest-api/rest-api.md

# API Reference

### API Reference

The Fiddler API is organized around REST. Our API has predictable resource-oriented URLs, accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

### API Response types

Fiddler API returns three kinds of responses

#### Normal Response

Normal response are the ones which doesn’t need to be paginated.

```
{
  api_version: <API version responding back with the response>,
  kind: "NORMAL",
  data: <Actual Response Object>
}
```

#### Paginated Response

Paginated response contains the relevant items along with pagination data.

```
{
  api_version: <API version responding back with the response>,
  kind: "PAGINATED",
  data: {
    page_size: <integer>,
    item_count: <integer>,
    total: <integer>,
    page_count: <integer>,
    page_index: <integer>,
    offset: <integer>,
    items: [<Array of items>]
  }
}
```

#### Error Response

In case something goes wrong, error response is returned.

```
{
  api_version: <API version responding back with the response>,
  kind: "ERROR",
  error: {
    code: <Error code>,
    message: <string>,
    errors: [
      {
        reason: <string>,
        message: <string>,
        help: <string>
      }
    ]
  }
}
```

Fiddler uses conventional HTTP response codes to indicate the success or failure of an API request. In general: Codes in the ***2xx*** range indicate success. Codes in the ***4xx*** range indicate an error that failed given the information provided (e.g., a required parameter was omitted, a charge failed, etc.). Codes in the ***5xx*** range indicate an error with Fiddler’s servers (these are rare).

### List of APIs

* [Projects](https://docs.fiddler.ai/api/rest-api/rest-api/projects)
* [Model](https://docs.fiddler.ai/api/rest-api/rest-api/model)
* [File Upload](https://docs.fiddler.ai/api/rest-api/rest-api/file-upload)
* [Custom Metrics](https://docs.fiddler.ai/api/rest-api/rest-api/custom-metrics)
* [Segments](https://docs.fiddler.ai/api/rest-api/rest-api/segments)
* [Baseline](https://docs.fiddler.ai/api/rest-api/rest-api/baseline)
* [Jobs](https://docs.fiddler.ai/api/rest-api/rest-api/jobs)
* [Alert Rules](https://docs.fiddler.ai/api/rest-api/rest-api/alert-rules)
* [Environment](https://docs.fiddler.ai/api/rest-api/rest-api/environment)
* [Explainability](https://docs.fiddler.ai/api/rest-api/rest-api/explainability)
* [Server Info](https://docs.fiddler.ai/api/rest-api/rest-api/server-info)

***

### Just getting started?

Check out our [Quick Start Notebooks](https://app.gitbook.com/o/MIMFsmMfRqhAZbzV2AtV/s/jZC6ysdlGhDKECaPCjwm/).
