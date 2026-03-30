# Source: https://northflank.com/docs/v1/api/team/opentofu/get-opentofu-job-logs.md

# Get OpenTofu job logs

Get logs for an OpenTofu job

Required permission: Account > Templates > Runs > Read

**Path parameters:**

{object}
- `opentofuJobId`: (string) (required) ID of the opentofu job

**Query parameters:**

{object}
- `queryType`: (string) `range` selects a log range and returns immediately. (enum: range)
- `startTime`: (string) Fetch logs generated after this timestamp.
- `endTime`: (string) Fetch logs generated before this timestamp.
- `duration`: (integer) Range duration in seconds. If set, only one of `startTime` or `endTime` can be set.
- `lineLimit`: (number) Number of log lines to fetch.
- `direction`: (string) Ordering of log lines (enum: backward, forward)
- `textIncludes`: (string) Filter log lines to match this search string
- `textNotIncludes`: (string) Filter log lines to not match this search string
- `regexIncludes`: (string) Filter log lines to match this regular expression
- `regexNotIncludes`: (string) Filter log lines to not match this regular expression

**Request body:**

{object}
- `queryType`: (string) `range` selects a log range and returns immediately. (enum: range)
- `startTime`: (string) Fetch logs generated after this timestamp. (format: date-time)
- `endTime`: (string) Fetch logs generated before this timestamp. (format: date-time)
- `duration`: (integer) Range duration in seconds. If set, only one of `startTime` or `endTime` can be set.
- `lineLimit`: (number) Number of log lines to fetch. (format: float)
- `direction`: (string) Ordering of log lines (enum: backward, forward)
- `textIncludes`: (string) Filter log lines to match this search string (min length: 1) (max length: 100)
- `textNotIncludes`: (string) Filter log lines to not match this search string (min length: 1) (max length: 100)
- `regexIncludes`: (string) Filter log lines to match this regular expression (min length: 1) (max length: 100)
- `regexNotIncludes`: (string) Filter log lines to not match this regular expression (min length: 1) (max length: 100)

**Response body:**

{object}
- `data`: [array of] {object}
   - `containerId`: (string) (required)
   - `log`: (undefined) (required)
   - `ts`: (string) (required) (format: date-time)

## API reference

GET /v1/opentofu-jobs/{opentofuJobId}/logs

GET /v1/teams/{teamId}/opentofu-jobs/{opentofuJobId}/logs

### Example request

Request body

```curl
curl --header "Content-Type: application/json" \
  --header "Authorization: Bearer NORTHFLANK_API_TOKEN" \
  --request GET \
  --data '{"queryType":"range","startTime":"2023-02-16T14:00:00.000Z","endTime":"2023-02-16T15:00:00.000Z","duration":600,"lineLimit":250,"direction":"backward","textIncludes":"myvalue","textNotIncludes":"myvalue","regexIncludes":"my.*value","regexNotIncludes":"my.*value"}' \
  https://api.northflank.com/v1/opentofu-jobs/{opentofuJobId}/logs
```

```javascript
const payload = {
  "queryType": "range",
  "startTime": "2023-02-16T14:00:00.000Z",
  "endTime": "2023-02-16T15:00:00.000Z",
  "duration": 600,
  "lineLimit": 250,
  "direction": "backward",
  "textIncludes": "myvalue",
  "textNotIncludes": "myvalue",
  "regexIncludes": "my.*value",
  "regexNotIncludes": "my.*value"
}

const response = await fetch('https://api.northflank.com/v1/opentofu-jobs/{opentofuJobId}/logs', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${NORTHFLANK_API_TOKEN}`
  },
  body: JSON.stringify(payload)
})

const json = await response.json()
console.log(json)
```

```python
import requests

url = "https://api.northflank.com/v1/opentofu-jobs/{opentofuJobId}/logs"

payload = {"queryType":"range","startTime":"2023-02-16T14:00:00.000Z","endTime":"2023-02-16T15:00:00.000Z","duration":600,"lineLimit":250,"direction":"backward","textIncludes":"myvalue","textNotIncludes":"myvalue","regexIncludes":"my.*value","regexNotIncludes":"my.*value"}
headers = {"Content-Type": "application/json", "Authorization": "Bearer NORTHFLANK_API_TOKEN"}

response = requests.request("GET", url, headers = headers, json = payload)

print(response.json())
```

```go
package main

import (
  "bytes"
  "fmt"
  "io/ioutil"
  "net/http"
)

func main() {
  url := "https://api.northflank.com/v1/opentofu-jobs/{opentofuJobId}/logs"

  var jsonStr = []byte(`{"queryType":"range","startTime":"2023-02-16T14:00:00.000Z","endTime":"2023-02-16T15:00:00.000Z","duration":600,"lineLimit":250,"direction":"backward","textIncludes":"myvalue","textNotIncludes":"myvalue","regexIncludes":"my.*value","regexNotIncludes":"my.*value"}`)
  req, err := http.NewRequest("GET", url, bytes.NewBuffer(jsonStr))
  req.Header.Set("Content-Type", "application/json")
  req.Header.Set("Authorization", "Bearer NORTHFLANK_API_TOKEN")

  client := &http.Client{}
  resp, err := client.Do(req)
  if err != nil {
    panic(err)
  }
  defer resp.Body.Close()

  fmt.Println("Response status:", resp.Status)
  fmt.Println("Response headers:", resp.Header)
  body, _ := ioutil.ReadAll(resp.Body)
  fmt.Println("Response body:", string(body))
}
```

### Example Response

200 OK: List of logs values

```json
{
  "data": [
    {
      "log": "stdout F This is a log line",
      "ts": "2023-03-21T15:01:17.310Z"
    }
  ]
}
```

## CLI reference

$ northflank get opentofu-job logs

Options:

- `--opentofuJobId <opentofuJobId>`: ID of the opentofu job

- `--queryType <queryType>`: `range` selects a log range and returns immediately.

- `--startTime <startTime>`: Fetch logs generated after this timestamp.

- `--endTime <endTime>`: Fetch logs generated before this timestamp.

- `--duration <duration>`: Range duration in seconds. If set, only one of `startTime` or `endTime` can be set.

- `--lineLimit <lineLimit>`: Number of log lines to fetch.

- `--direction <direction>`: Ordering of log lines

- `--textIncludes <textIncludes>`: Filter log lines to match this search string

- `--textNotIncludes <textNotIncludes>`: Filter log lines to not match this search string

- `--regexIncludes <regexIncludes>`: Filter log lines to match this regular expression

- `--regexNotIncludes <regexNotIncludes>`: Filter log lines to not match this regular expression

- `-f --file <file>`: Path to a JSON/YAML resource definition file

- `-i --input <definition>`: JSON/YAML resource definition string (takes precedence over --file)

- `--verbose `: Verbose output

- `--quiet `: No console output

- `-o --output <format>`: Output formatting 

```json
{
  "queryType": "range",
  "startTime": "2023-02-16T14:00:00.000Z",
  "endTime": "2023-02-16T15:00:00.000Z",
  "duration": 600,
  "lineLimit": 250,
  "direction": "backward",
  "textIncludes": "myvalue",
  "textNotIncludes": "myvalue",
  "regexIncludes": "my.*value",
  "regexNotIncludes": "my.*value"
}
```

### Example Response

 List of logs values

```json
[
  {
    "log": "stdout F This is a log line",
    "ts": "2023-03-21T15:01:17.310Z"
  }
]
```

## JavaScript client reference

### Example request

Request body

```javascript
await apiClient.get.opentofuJob.logs({
  parameters: {
    "opentofuJobId": "example-job"
  },
  options: {
    "queryType": "range",
    "startTime": "2023-02-16T14:00:00.000Z",
    "endTime": "2023-02-16T15:00:00.000Z",
    "duration": 600,
    "lineLimit": 250,
    "direction": "backward",
    "textIncludes": "myvalue",
    "textNotIncludes": "myvalue",
    "regexIncludes": "my.*value",
    "regexNotIncludes": "my.*value"
  },
  data: {
    "queryType": "range",
    "startTime": "2023-02-16T14:00:00.000Z",
    "endTime": "2023-02-16T15:00:00.000Z",
    "duration": 600,
    "lineLimit": 250,
    "direction": "backward",
    "textIncludes": "myvalue",
    "textNotIncludes": "myvalue",
    "regexIncludes": "my.*value",
    "regexNotIncludes": "my.*value"
  }    
});
```

### Example Response

 List of logs values

```json
{
  "data": [
    {
      "log": "stdout F This is a log line",
      "ts": "2023-03-21T15:01:17.310Z"
    }
  ],
  "rawResponse": "...",
  "request": "...",
  "error": "..."
}
```

Previous: [Delete egress IP](/docs/v1/api//team/egress-ips/delete-egress-ip)

Next: [List tags](/docs/v1/api//team/tags/list-tags)