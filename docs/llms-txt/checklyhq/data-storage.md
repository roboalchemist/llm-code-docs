# Source: https://checklyhq.com/docs/platform/data-storage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How we store data

> Learn about how Checkly stores check run data

Every check we run generates a certain amount of data. We call these the "results". Results are made up of various parts:

* Metadata like timestamps, response times, fail/success flags, run location etc.
* JSON or other response bodies, response headers, request timing data
* Playwright Test traces and videos
* Screenshot files
* Run logs with debug or `console.log` statements.

## Data Retention

Depending on your plan we keep the results data according to the following retention policy:

|                               | Hobby   | Team    | Enterprise |
| ----------------------------- | ------- | ------- | ---------- |
| **Raw data retention**        | 7 days  | 30 days | 180 days   |
| **Aggregated data retention** | 30 days | 1 year  | 25 months  |

Simply put, you can "scroll back" within the defined period for raw data and inspect all the details of each result. After that, we store aggregates
of the relevant statistics like average, p95 and p99 response time and success ratio.


Built with [Mintlify](https://mintlify.com).