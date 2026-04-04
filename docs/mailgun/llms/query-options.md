# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/events/query-options.md

# Query Options

URL parameters allow you to manipulate the results of your query.

| Parameter | Description |
|  --- | --- |
| begin | The beginning of the search time range. It can be specified as a string (see date-format) or linux epoch seconds. Refer to Time Range for details. |
| end | The end of the search time range. It can be specified as a string (see `date-format`) or linux epoch seconds. Refer to Time Range for details. |
| ascending | Defines the direction of the search time range and must be provided if the range end time is not specified. Can be either `yes` or `no`. Refer to Time Range for details. |
| limit | Number of entries to return. (300 max) |
| field | `field` is the name of the Filter Field. The value of the parameter should be a valid Filter Expression. Several field filters can be specified in one request. If the same field is mentioned, more than once, then all its filter expressions are combined with AND operator. |