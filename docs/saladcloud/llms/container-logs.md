# Source: https://docs.salad.com/container-engine/explanation/container-groups/container-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Container Logs

*Last Updated: January 6, 2026*

## How to Log From Your Container

When running a container on SaladCloud, you can log to the standard output and standard error streams. These logs are
collected and stored by SaladCloud, and exported to any configured
[external logging source](/container-engine/explanation/infrastructure-platform/external-logging).

[Learn more about logging best practices.](/container-engine/how-to-guides/external-logging/best-practices)

## Basic Logging

### How to View Container Logs In the Portal

Once your container is up and running on a SaladCloud node, you can view the logs from your container on the "Container
Logs" tab of a Container Group. To access this feature in the portal, navigate to your Container Group details page, and
click on the 'Container Logs' tab.

<img src="https://mintcdn.com/salad/CzUR5YJ7qRb7L5z3/container-engine/images/portal-container-logs.png?fit=max&auto=format&n=CzUR5YJ7qRb7L5z3&q=85&s=301a2b36a02a078cf5260d7d6dc39093" data-og-width="1563" width="1563" data-og-height="683" height="683" data-path="container-engine/images/portal-container-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/CzUR5YJ7qRb7L5z3/container-engine/images/portal-container-logs.png?w=280&fit=max&auto=format&n=CzUR5YJ7qRb7L5z3&q=85&s=e6e963161c6676fc002406e49f87fe75 280w, https://mintcdn.com/salad/CzUR5YJ7qRb7L5z3/container-engine/images/portal-container-logs.png?w=560&fit=max&auto=format&n=CzUR5YJ7qRb7L5z3&q=85&s=4ca345de1842dbb6c7c0f5669999a20a 560w, https://mintcdn.com/salad/CzUR5YJ7qRb7L5z3/container-engine/images/portal-container-logs.png?w=840&fit=max&auto=format&n=CzUR5YJ7qRb7L5z3&q=85&s=ebc564e2e463284880699b1cb272d317 840w, https://mintcdn.com/salad/CzUR5YJ7qRb7L5z3/container-engine/images/portal-container-logs.png?w=1100&fit=max&auto=format&n=CzUR5YJ7qRb7L5z3&q=85&s=70dfdcdf90f6e364e3046b707a2a0cad 1100w, https://mintcdn.com/salad/CzUR5YJ7qRb7L5z3/container-engine/images/portal-container-logs.png?w=1650&fit=max&auto=format&n=CzUR5YJ7qRb7L5z3&q=85&s=85a2ab479beb1c880d63431889ac1410 1650w, https://mintcdn.com/salad/CzUR5YJ7qRb7L5z3/container-engine/images/portal-container-logs.png?w=2500&fit=max&auto=format&n=CzUR5YJ7qRb7L5z3&q=85&s=cd2bb4e09cde58047f86159955fcd0b3 2500w" />

You can also navigate to this page from the Action menu of an instance. This option will take you to the Container Logs
tab with the Machine ID value pre-filled.

<img src="https://mintcdn.com/salad/UiepyIUZKZjvv7fL/container-engine/images/portal-container-instance-actions-view-logs.png?fit=max&auto=format&n=UiepyIUZKZjvv7fL&q=85&s=363db9105a1eadf1102cd3b90fedc4a2" data-og-width="1385" width="1385" data-og-height="408" height="408" data-path="container-engine/images/portal-container-instance-actions-view-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/UiepyIUZKZjvv7fL/container-engine/images/portal-container-instance-actions-view-logs.png?w=280&fit=max&auto=format&n=UiepyIUZKZjvv7fL&q=85&s=9d885ac017d8f42a2740d3aa446fecd0 280w, https://mintcdn.com/salad/UiepyIUZKZjvv7fL/container-engine/images/portal-container-instance-actions-view-logs.png?w=560&fit=max&auto=format&n=UiepyIUZKZjvv7fL&q=85&s=12497fdcb32c3a54a9ba9ee5311fad04 560w, https://mintcdn.com/salad/UiepyIUZKZjvv7fL/container-engine/images/portal-container-instance-actions-view-logs.png?w=840&fit=max&auto=format&n=UiepyIUZKZjvv7fL&q=85&s=717c98f6d4f8594f95e8b57f683c0816 840w, https://mintcdn.com/salad/UiepyIUZKZjvv7fL/container-engine/images/portal-container-instance-actions-view-logs.png?w=1100&fit=max&auto=format&n=UiepyIUZKZjvv7fL&q=85&s=2b5e6ed6db224aa3047d6df3e5ad6502 1100w, https://mintcdn.com/salad/UiepyIUZKZjvv7fL/container-engine/images/portal-container-instance-actions-view-logs.png?w=1650&fit=max&auto=format&n=UiepyIUZKZjvv7fL&q=85&s=43f5d9a6160251a1292b6daf1307e999 1650w, https://mintcdn.com/salad/UiepyIUZKZjvv7fL/container-engine/images/portal-container-instance-actions-view-logs.png?w=2500&fit=max&auto=format&n=UiepyIUZKZjvv7fL&q=85&s=3cd2aeedd8a401983fb164c2a20cfee6 2500w" />

The Container Logs feature has a simple interface meant to provide you with enough visibility for basic troubleshooting
of your applications running on SaladCloud. For more robust logging functionality, we recommend configuring the
[External Logging Service option](/container-engine/explanation/infrastructure-platform/external-logging) in your
container group.

The Container Logs feature allows you to query your container logs with these options:

* search for specific log messages with case-insensitive string filtering
* filter for logs from a specific Machine ID. If left blank, logs from all Machine IDs in the Container Group will be
  returned.
* filter for logs in a specified time period. Choose one of the predefined options, or use the custom start date and end
  date option

When your query returns results you will see them in a scrollable table view. Each result includes:

* Log Message
* Machine ID (The unique ID of the node running the container that created the log message.)
* Log Create Time

Should your query yield no results, the table view will display "No data to display"

For more sophisticated querying, you can use the Log Explorer or the Public API
[Query Log Entries endpoint](/reference/saladcloud-api/logs/query-log-entries). Clicking the Log Explorer button will
take you to the Log Explorer page in the SaladCloud Portal with the current query pre-populated.

**Availability and Limitations**

* A maximum of 500 logs can be returned per query. Utilize specific query filters and time ranges to get the logs you
  are looking for.
* Logs are retained and accessible for up to 90 days.
* If you encounter this error message, try narrowing your query's time range
  * <img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-logs-error-getting-logs.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=64f92c88084899a9453ae0ff7bca5542" data-og-width="1233" width="1233" data-og-height="152" height="152" data-path="container-engine/images/portal-container-logs-error-getting-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-logs-error-getting-logs.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=30b27677681c6fade2997be1867f29d3 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-logs-error-getting-logs.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=7cb89b49c77338f8e5d5d34a13bbe620 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-logs-error-getting-logs.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=91f2d2f8321002e162b83ddc7fa0e9ee 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-logs-error-getting-logs.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=9eebdf2ec0c9f0618d4a763cb3db2cf2 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-logs-error-getting-logs.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=64ffb02c478921ebb1a0ccae10eb6cff 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-logs-error-getting-logs.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=f5bf858f45c2bb5ceeb2d7c41ed52cc8 2500w" />

## Advanced Logging

For more advanced on-platform logging capabilities, you can make use of the
[Query Log Entries endpoint](/reference/saladcloud-api/logs/query-log-entries) in the API. This endpoint is scoped at
the organization level, rather than the container group level, allowing you to view logs from any number of container
groups and projects.

This endpoint supports a more flexible query language as well, allowing you to make much more sophisticated filters
across many fields, and supporting filters on structured logs emitted by your application.
[See the full query reference](/container-engine/reference/log-queries).

You can query logs by making a POST request to the query logs endpoint like this:

```shell  theme={null}
curl --request POST \
  --url https://api.salad.com/api/public/organizations/$organization_name/log-entries \
  --header 'Content-Type: application/json' \
  --header "Salad-Api-Key: $salad_api_key" \
  --data '{
  "end_time": "2025-11-07T05:31:56Z",
  "page_size": 1,
  "query": "<string>",
  "sort_order": "desc",
  "start_time": "2025-11-07T05:31:56Z"
}'
```

and receive a response like:

```json  theme={null}
{
  "items": [
    {
      "json_log": {},
      "parent_span_id": "<string>",
      "receive_time": "2025-11-07T05:31:56Z",
      "resource": {
        "labels": {},
        "type": "<string>"
      },
      "severity": "debug",
      "span_Id": "<string>",
      "time": "2025-11-07T05:31:56Z",
      "trace_Id": "<string>"
    }
  ],
  "organization_name": "acme-corp",
  "page_max_time": "2025-11-07T05:31:56Z",
  "page_min_time": "2025-11-07T05:31:56Z"
}
```

Each log event takes the following structure.

```json  theme={null}
{
  "time": "string iso8601",
  "receive_time": "string iso8601",
  "resource": {
    "type": "string enum",
    "labels": {
      // key-value pairs (string to string) specific to `type`
    }
  },
  "severity": "string enum",
  "severity_number": "integer",

  "trace_id": "string", // optional
  "span_id": "string", // optional
  "parent_span_id": "string", //optional

  // only one of `text_log` or `json_log`
  "text_log": "string",
  "json_log": {
    // key-value pairs (string to any valid JSON type) specific to log entry
  }
}
```

* Note that this will contain **EITHER** `text_log` **OR** `json_log`, but not both. If you emit logs that are valid
  json, they will end up in the `json_log` field. Otherwise, the full log line will be in the `text_log` field.
* The `time` field indicates the system time on the node where the log was emitted.
* the `receive_time` field indicates the time when Axiom (what we use under the hood for log storage) received the log
  entry.
* Any of these fields can be used in the query language.
  [Here](https://docs.salad.com/container-engine/reference/log-queries#examples) are some examples of queries you can
  make. These queries can be passed as the `query` parameter in the body of the request to the API.
