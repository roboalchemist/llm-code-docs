# Source: https://loops.so/docs/api-reference/dedicated-sending-ips.md

# List dedicated sending IP addresses

> Retrieve a list of Loops' dedicated sending IP addresses.

<Warning>
  This endpoint is provided for the rare instances where you may need to whitelist our sending IPs. Please note that this list is subject to change and will not include shared IPs used for sending mail.

  Unless you are sure you need this and are comfortable watching for changes, we strongly recommend you *do not* whitelist these IPs.

  This endpoint may be rate-limited.
</Warning>

## Request

No parameters.

## Response

Returns an array of IP address strings.

<ResponseField name="IP addresses" type="array" required>
  IP address (e.g., "1.2.3.4")
</ResponseField>

If there are no dedicated IP addresses an empty array is returned.

### Error

A `405` error will be returned if the wrong HTTP request method is used.

<ResponseField name="success" type="boolean" required />

<ResponseField name="message" type="string" required>
  Error message
</ResponseField>

<ResponseExample>
  ```json Response theme={"dark"}
  [
    "1.2.3.4"
  ]
  ```
</ResponseExample>
