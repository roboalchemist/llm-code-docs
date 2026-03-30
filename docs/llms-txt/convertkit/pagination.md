# Source: https://developers.kit.com/api-reference/pagination.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Pagination

> Working with paginated responses

<ResponseExample>
  ```json  theme={null}
  {
    "broadcasts": [...],
    "pagination": {
      "has_previous_page": false,
      "has_next_page": true,
      "start_cursor": "WzEzXQ==",
      "end_cursor": "WzE0XQ==",
      "per_page": 100
    }
  }
  ```
</ResponseExample>

All of our list endpoints are paginated unless noted otherwise, using cursor based pagination.

Each one will return a `pagination` object in the JSON response, with an example shown on the right.

In order to navigate the results, follow these steps:

* The default page size is 500 results. To change the page size, use the `per_page` query parameter. The maximum page size allowed is 1000.
* To request the next page of results, use the `after` query param with the `end_cursor` value of the response.
* To request the previous page of results, use the `before` query param with the `start_cursor` value of the response.
* To request the total count of the collection, use the `include_total_count` query param with a value of `true`. This will complete another data query to return the total count. Expect a slightly slower response when using this option.


Built with [Mintlify](https://mintlify.com).