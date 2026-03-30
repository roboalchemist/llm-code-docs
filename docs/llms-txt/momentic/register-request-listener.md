# Source: https://momentic.ai/docs/steps/register-request-listener.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Register request listener

> Register a listener for requests that match a specific URL pattern

Starts listening for requests that match a specific URL pattern. When awaited
using an [await listener](../steps/await-listener) step, it will return the
first request matching the pattern, if any.

You should register your listener before the request is made. If an action
triggers the request, make sure to add this step before the action in your test.

## Inputs

<ResponseField name="URL Matcher" type="object">
  <Expandable>
    <Tabs>
      <Tab title="Substring">
        <ResponseField name="url" type="string" required>
          The substring to look for
        </ResponseField>
      </Tab>

      <Tab title="Glob">
        <ResponseField name="glob" type="string" required>
          The glob pattern to match against
        </ResponseField>
      </Tab>

      <Tab title="Regex">
        <ResponseField name="regex" type="string" required>
          The regex pattern to match against
        </ResponseField>
      </Tab>

      <Tab title="Domain">
        <ResponseField name="domain" type="string" required>
          The domain to match against. If matching a subdomain, the exact subdomain is required.
        </ResponseField>
      </Tab>
    </Tabs>
  </Expandable>
</ResponseField>

<ResponseField name="HTTP Method" type="POST | GET | DELETE | PUT | PATCH | OPTIONS">
  Only match requests that have this HTTP Method
</ResponseField>

<ResponseField name="Listener key" type="string" required>
  A unique key to identify the listener. This key can be used in the [await
  listener](../steps/await-listener) step to wait for the request to complete.
</ResponseField>

## Outputs

The following outputs will be returned once the listener resolves in an
[await listener](../steps/await-listener) step:

<ResponseField name="request" type="Request object" required>
  <Expandable title="properties">
    <ResponseField name="url" type="string" required>
      The URL of the request that matched the pattern.
    </ResponseField>

    <ResponseField name="method" type="string" required>
      The HTTP method of the request (e.g., GET, POST).
    </ResponseField>

    <ResponseField name="headers" type="object" required>
      A key-value object containing the request headers.
    </ResponseField>

    <ResponseField name="json" type="object">
      The JSON body of the request. This will be undefined if the content-type is not JSON.
    </ResponseField>

    <ResponseField name="text" type="string">
      The raw body of the request. This will be undefined if the content-type is not text.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="response" type="Response object" required>
  <Expandable title="properties">
    <ResponseField name="status" type="number" required>
      The HTTP status code of the response.
    </ResponseField>

    <ResponseField name="headers" type="object" required>
      A key-value object containing the response headers.
    </ResponseField>

    <ResponseField name="json" type="object">
      The JSON body of the response. This will be undefined if the content-type is not JSON.
    </ResponseField>

    <ResponseField name="text" type="string">
      The raw body of the response. This will be undefined if the content-type is not text.
    </ResponseField>
  </Expandable>
</ResponseField>


Built with [Mintlify](https://mintlify.com).