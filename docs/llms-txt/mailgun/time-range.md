# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/events/time-range.md

# Time Range

When making a request, you need to specify a time range, which consists of a starting timestamp. Additionally, you must include either an ending timestamp or indicate a search direction. If you don't provide an ending timestamp, you must specify a search direction.

When you provide a range end timestamp, the relationship between the beginning and end timestamps determines the traversal direction of eventsâeither ascending or descending. For instance, if the end timestamp is less (older) than the beginning timestamp, the result pages are returned from newer to older, and events on these pages are sorted in descending order based on their timestamps.

If the end timestamp is not provided, the direction must be specified, and based on this direction, the behavior of result page traversal behaves differently:

- If the range is descending, then the end timestamp is determined by the user tariff plan retention period.
- If the range is ascending, events will continue to be recorded, however, the request time range won't be displayed on the provided pages. After retrieving the latest events and reaching an empty result page, requesting the next page URL later will show events that happened afterward. This process can continue indefinitely.


Warning!
Although it may appear that real-time event polling can be achieved by continuously traversing the next URLs of an ascending time range without an explicit end timestamp, the process is not as straightforward as it seems. Please refer to the guidelines outlined in the Event Polling section for the correct approach.

If both the end range dates and the direction of the search are specfied, then they should agree with each other, otherwise the request will return an error.