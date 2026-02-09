# queryispmetrics

Source: https://developer.ui.com/site-manager/v1.0.0/queryispmetrics

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Query ISP Metrics

POST`/v1/isp-metrics/{type}/query`

Retrieves ISP metrics data based on specific query parameters. 5-minute interval metrics are available for at least 24 hours, and 1-hour interval metrics are available for at least 30 days.

**Note:** If the UI account lacks access to all requested sites, a 502 error is returned. If partial access is granted, the response will include `status: partialSuccess`.

path Parameters

type

required

string

Specifies whether metrics are returned using `5m` or `1h` intervals

request Body

sitesExpand

Array of object

## Responses

200400401429500502

Response Schema: application/json

dataExpand

object

Generic response data, specific schema depends on the endpoint

httpStatusCode

integer

HTTP status code

traceId

string

Request trace identifier