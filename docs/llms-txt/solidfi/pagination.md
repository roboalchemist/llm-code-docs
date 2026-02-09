# Source: https://docs.solidfi.com/v2/api-reference/getting-started/pagination.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Pagination

> Solid Platform support cursor pagination

When calling any of the List All APIs on the Solid platform, you can control the pagination of the response using the following filters. For other filters, see the documentation for the relevant List All API.

All the list APIs return a has\_more boolean flag in the response to indicate whether there are more records to iterate.

| Filter (Type)            | Type                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| limit (int)              | number of records to return (default = 25, max = 100)                                                                                                                                                                                                                                                                                                                            |
| starting\_after (string) | A cursor for use in pagination. starting\_after is an ID that defines your place in the list. For instance, if you make a list request and receive 50 records, ending with Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky, your subsequent call can include starting\_after=Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky in order to fetch the next page of the list.      |
| ending\_before (string)  | A cursor for use in pagination. ending\_before is an ID that defines your place in the list. For instance, if you make a list request and receive 50 records, starting with Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky, your subsequent call can include ending\_before= Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky in order to fetch the previous page of the list. |
