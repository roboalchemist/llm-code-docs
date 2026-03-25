# Source: https://ngrok.com/docs/traffic-policy/variables/time.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Time Variables

> Reference documentation for time variables in Traffic Policy for accessing current time, date, and timezone information.

## Time variables

The following variables are available under the `time` namespace:

| Name                   | Type     | Description                                                                              |
| ---------------------- | -------- | ---------------------------------------------------------------------------------------- |
| [`time.now`](#timenow) | `string` | The current UTC time in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |

### `time.now`

The current UTC time in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) format.

<CodeGroup>
  ```yaml policy.yml theme={null}
  expressions:
    - "conn.ts.end < timestamp(time.now)"
  ```

  ```json policy.json theme={null}
  {
    "expressions": [
      "conn.ts.end < timestamp(time.now)"
    ]
  }
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).