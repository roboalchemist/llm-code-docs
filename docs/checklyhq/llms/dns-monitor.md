# Source: https://checklyhq.com/docs/constructs/dns-monitor.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# DnsMonitor Construct

> Learn how to configure DNS monitors with the Checkly CLI.

<Tip>
  Learn more about DNS Monitors in [the DNS monitor overview](/detect/uptime-monitoring/dns-monitors/overview).
</Tip>

Use DNS Monitors to verify that DNS records resolve correctly and to track lookup performance over time.

<Accordion title="Prerequisites">
  Before creating DNS Monitors, ensure you have:

  * An initialized Checkly CLI project
  * A domain or hostname you want to monitor
  * Basic understanding of DNS record types (A, AAAA, CNAME, MX, NS, TXT, SOA)

  For additional setup information, see [CLI overview](/cli/overview).
</Accordion>

<CodeGroup>
  ```ts Basic Example theme={null}
  import { Frequency, DnsAssertionBuilder, DnsMonitor } from "checkly/constructs"

  new DnsMonitor("dns-monitor", {
    name: "DNS A Record Monitor",
    activated: true,
    maxResponseTime: 1000,
    degradedResponseTime: 500,
    frequency: Frequency.EVERY_5M,
    locations: ["us-east-1", "eu-central-1"],
    request: {
      query: "example.com",
      recordType: "A",
      assertions: [
        DnsAssertionBuilder.jsonAnswer("$.Answer[0].data").equals("93.184.216.34")
      ],
    },
  })
  ```

  ```ts Advanced Example theme={null}
  import { Frequency, DnsAssertionBuilder, DnsMonitor } from "checkly/constructs"

  new DnsMonitor("advanced-dns-monitor", {
    name: "Advanced DNS Monitor",
    activated: true,
    frequency: Frequency.EVERY_5M,
    locations: ["us-east-1", "eu-central-1"],
    maxResponseTime: 800,
    degradedResponseTime: 400,
    tags: ["dns", "production", "critical"],
    request: {
      query: "api.example.com",
      recordType: "A",
      nameServer: "9.9.9.9",
      port: 53,
      protocol: "UDP",
      assertions: [
        DnsAssertionBuilder.jsonAnswer("$.Answer[0].TTL").greaterThan(300),
        DnsAssertionBuilder.responseTime().lessThan(500),
        DnsAssertionBuilder.jsonAnswer("$.Answer[0].data").equals("93.184.216.34")
      ],
    },
  })
  ```
</CodeGroup>

## Configuration

A DNS Monitor has its own DNS-specific settings, plus the standard monitor options shared across all check types.

<Tabs>
  <Tab title="DNS Monitor Settings">
    | Parameter              | Type     | Required | Default | Description                                                    |
    | ---------------------- | -------- | -------- | ------- | -------------------------------------------------------------- |
    | `request`              | `object` | ✅        | -       | DNS request configuration object                               |
    | `degradedResponseTime` | `number` | ❌        | `500`   | Response time threshold in milliseconds for degraded status    |
    | `maxResponseTime`      | `number` | ❌        | `1000`  | Maximum response time in milliseconds before marking as failed |
  </Tab>

  <Tab title="General Monitor Settings">
    | Property                | Type                                     | Required | Default     | Description                                                             |
    | ----------------------- | ---------------------------------------- | -------- | ----------- | ----------------------------------------------------------------------- |
    | `name`                  | `string`                                 | ✅        | -           | Friendly name for your monitor                                          |
    | `activated`             | `boolean`                                | ❌        | `true`      | Whether the monitor is enabled                                          |
    | `alertChannels`         | `Array<AlertChannel \| AlertChannelRef>` | ❌        | `[]`        | Array of AlertChannel objects for notifications                         |
    | `alertEscalationPolicy` | `AlertEscalationPolicy`                  | ❌        | -           | Advanced alert escalation settings                                      |
    | `frequency`             | `Frequency`                              | ❌        | `EVERY_10M` | How often to run your monitor                                           |
    | `group`                 | `CheckGroupV1` `CheckGroupV2`            | ❌        | -           | The CheckGroup this monitor belongs to                                  |
    | `locations`             | `string[]`                               | ❌        | `[]`        | Array of public location codes                                          |
    | `privateLocations`      | `string[]`                               | ❌        | `[]`        | Array of Private Location slugs                                         |
    | `muted`                 | `boolean`                                | ❌        | `false`     | Whether alert notifications are muted                                   |
    | `tags`                  | `string[]`                               | ❌        | `[]`        | Array of tags to organize monitors                                      |
    | `testOnly`              | `boolean`                                | ❌        | `false`     | Only run with test, not during deploy                                   |
    | `retryStrategy`         | `RetryStrategy`                          | ❌        | -           | Strategy for configuring retries                                        |
    | `runParallel`           | `boolean`                                | ❌        | `false`     | Run monitors in parallel or round-robin                                 |
    | `triggerIncident`       | `IncidentTrigger`                        | ❌        | -           | Create and resolve an incident based on the check's alert configuration |
  </Tab>
</Tabs>

### `DnsMonitor` Options

<ResponseField name="request" type="object" required>
  DNS request configuration that defines the DNS query to perform and how to validate the response.

  **Usage:**

  ```ts  theme={null}
  new DnsMonitor("dns-monitor", {
    name: "DNS A Record Monitor",
    request: {
      query: "example.com",
      recordType: "A",
      assertions: [
        DnsAssertionBuilder.jsonAnswer("$.Answer[0].data").equals("93.184.216.34")
      ]
    }
  })
  ```

  **Parameters:**

  | Parameter    | Type             | Required | Default | Description                                       |
  | ------------ | ---------------- | -------- | ------- | ------------------------------------------------- |
  | `query`      | `string`         | ✅        | -       | The DNS query (domain name or IP address)         |
  | `recordType` | `DnsRecordType`  | ✅        | -       | DNS record type: A, AAAA, CNAME, MX, NS, TXT, SOA |
  | `nameServer` | `string`         | ❌        | -       | Custom DNS server to query (e.g. "9.9.9.9")       |
  | `port`       | `number`         | ❌        | `53`    | Port of the DNS server                            |
  | `protocol`   | `DnsProtocol`    | ❌        | `UDP`   | Protocol to use: UDP or TCP                       |
  | `assertions` | `DnsAssertion[]` | ❌        | `[]`    | Response assertions using `DnsAssertionBuilder`   |
</ResponseField>

<ResponseField name="degradedResponseTime" type="number" default="500">
  Response time threshold in milliseconds for marking the DNS Monitor as degraded (warning state).

  **Usage:**

  ```ts highlight={3} theme={null}
  new DnsMonitor("dns-performance-tiers", {
    name: "DNS Performance Tiers",
    degradedResponseTime: 300, // Warn at 300ms
    request: {
      query: "example.com",
      recordType: "A",
      assertions: [
        DnsAssertionBuilder.jsonAnswer("$.Answer[0].data").equals("93.184.216.34")
      ],
    },
  })
  ```
</ResponseField>

<ResponseField name="maxResponseTime" type="number" default="1000">
  Maximum response time in milliseconds before the DNS Monitor is marked as failed.

  **Usage:**

  ```ts highlight={3} theme={null}
  new DnsMonitor("fast-dns", {
    name: "Fast DNS Resolution",
    maxResponseTime: 500, // Fail at 500ms
    request: {
      query: "fast.example.com",
      recordType: "A",
    },
  })
  ```
</ResponseField>

### `DnsMonitor` Assertions

To define `assertions` for the `request` of an `DnsMonitor` you should use the `DnsAssertionBuilder`. The following sources are available for DNS monitor assertions:

* `responseTime()`: Assert the total response time of the DNS request in milliseconds. Use this to set thresholds for failed lookups
* `responseCode()`: By default, DNS monitors pass when the return code is NOERROR and fail on error codes (FORMERR, SERVFAIL, NXDOMAIN, etc.). You can override this behavior by defining a custom return code assertion
* `textAnswer()`: The raw DNS response as plain text. Use this to check for specific strings in the response
* `jsonAnswer(property?)`: The [DNS response in JSON format](/detect/uptime-monitoring/dns-monitors/configuration#json-response-schemas). This allows you to target specific fields using JSON path assertions. The response structure varies by record type. [Learn more about using JSON path](/detect/assertions/#json-responses-with-json-path).

Here are some examples:

* Assert the total response time of the DNS request

```ts  theme={null}
DnsAssertionBuilder.responseTime().lessThan(1000)
// Equivalent to:
{ source: 'RESPONSE_TIME', comparison: 'LESS_THAN', target: '1000' }
```

* Assert the DNS response code

```ts  theme={null}
DnsAssertionBuilder.responseCode().equals('NOERROR')
// Equivalent to:
{ source: 'RESPONSE_CODE', comparison: 'EQUALS', target: 'NOERROR' }
```

* Assert against specific JSON fields in the response.

```ts  theme={null}
DnsAssertionBuilder.jsonAnswer('$.Answer.length').equals(4)
// Equivalent to:
{ source: 'JSON_ANSWER', property: '$.Answer.length', comparison: 'EQUALS', target: '4' }
```

Learn more in our docs on [Assertions](/detect/assertions).

### General Monitor Options

<ResponseField name="name" type="string" required>
  Friendly name for your DNS Monitor that will be displayed in the Checkly dashboard and used in notifications.

  **Usage:**

  ```ts highlight={2} theme={null}
  new DnsMonitor("my-monitor", {
    name: "DNS Resolution Monitor",
    /* More options ... */
  })
  ```
</ResponseField>

<ResponseField name="frequency" type="Frequency">
  How often the DNS Monitor should run. Use the `Frequency` enum to set the check interval.

  **Usage:**

  ```ts highlight={2} theme={null}
  new DnsMonitor("my-monitor", {
    frequency: Frequency.EVERY_1M,
    /* More options ... */
  })
  ```

  **Available frequencies**: `EVERY_10S`, `EVERY_20S`, `EVERY_30S`, `EVERY_1M`, `EVERY_2M`, `EVERY_5M`, `EVERY_10M`, `EVERY_15M`, `EVERY_30M`, `EVERY_1H`, `EVERY_2H`, `EVERY_3H`, `EVERY_6H`, `EVERY_12H`, `EVERY_24H`
</ResponseField>

<ResponseField name="locations" type="string[]" default="[]">
  Array of [public location codes](/concepts/locations/#public-locations) where the DNS Monitor should run from. Multiple locations provide geographic coverage and help detect regional DNS issues.

  **Usage:**

  ```ts highlight={2} theme={null}
  new DnsMonitor("global-dns-monitor", {
    locations: ["us-east-1", "eu-central-1", "ap-southeast-1"]
  })
  ```
</ResponseField>

<ResponseField name="activated" type="boolean" default="true">
  Whether the DNS Monitor is enabled and will run according to its schedule.

  **Usage:**

  ```ts highlight={2} theme={null}
  new DnsMonitor("my-monitor", {
    activated: false // Disabled monitor
  })
  ```
</ResponseField>


Built with [Mintlify](https://mintlify.com).