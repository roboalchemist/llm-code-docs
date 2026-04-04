# Source: https://developers.make.com/api-documentation/pagination-sorting-filtering.md

# Pagination, sorting and filtering

The majority of responses containing a collection of resources are paginated. Pagination limits the number of returned results per request to avoid delays in receiving a response and prevent overloading with results. Thanks to pagination, the API can run at its best performance.

You set pagination, sorting, and filtering parameters in query parameters. Separate multiple query parameters using the & symbol. The order of the parameters does not matter.

{% hint style="warning" %}
Pagination and filtering parameters contain square brackets -- `[` and `]`. Always encode them in URLs.
{% endhint %}
