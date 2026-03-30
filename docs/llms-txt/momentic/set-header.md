# Source: https://momentic.ai/docs/steps/set-header.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set header

> Adds a custom header to later requests

You should use this step before the request is initiated. If you need to add a
custom header to the initial page load, you can use this step followed by either
a [navigate](../steps/navigate) step or a [refresh](../steps/refresh) step.

## Inputs

<ResponseField name="Name" type="string" required>
  The name of the header. This should be a valid HTTP header name.
</ResponseField>

<ResponseField name="Value" type="string" required>
  The value of the header. This can be any string value.
</ResponseField>

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


Built with [Mintlify](https://mintlify.com).