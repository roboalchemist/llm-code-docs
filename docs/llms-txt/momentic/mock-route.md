# Source: https://momentic.ai/docs/steps/mock-route.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Mock route

> Intercept network requests and mock their responses

For more information about using this step, see our guide on
[request mocking](../request-mocking).

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

<ResponseField name="Response" type="string" required>
  Javascript code used to generate a response for the intercepted requests. This code must return a Javascript `Response` object. This
  code behaves similarly to Momentic's standard javascript step with a couple of
  exceptions:

  * Environment variables can be read at `env.<VARIABLE_NAME>`, however, they cannot be updated using `setVariable`. This is to prevent potential race conditions.
  * The request itself is accessible at `mock.request`. It is a standard Javascript [request object](https://developer.mozilla.org/en-US/docs/Web/API/Request).
  * If the 'fetch real response' config is enabled, the original response is accessible at `mock.response`. It is a standard Javascript [response object](https://developer.mozilla.org/en-US/docs/Web/API/Response).
</ResponseField>

## Configs

<ResponseField name="Fetch real response" type="boolean">
  Complete the original request, and pass its response into the generator as
  `mock.response`. Enabling this option is helpful if you want to modify the
  original response rather than fully replacing it. You should not enable this
  option if the request will fail (for example if the host is inaccessible), as
  it will cause the mock to fail.
</ResponseField>

<ResponseField name="Key" type="string">
  A key that can be used to reference the mock later. This should be set if you
  want to remove the mock later in the test. If not set, a random key will be
  generated.
</ResponseField>

<ResponseField name="Save to environment variable" type="string">
  Store the output of this step into the environment at the given key. This
  configuration only applies for steps that output data.
</ResponseField>


Built with [Mintlify](https://mintlify.com).