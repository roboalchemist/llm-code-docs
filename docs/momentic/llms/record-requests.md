# Source: https://momentic.ai/docs/steps/record-requests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Record requests

> Record requests matching a specific URL pattern

Start recording requests that match a specific URL pattern. This is useful for
capturing API calls or other network requests made by the application during
testing. The recorded requests can later be retrieved using the
[get recorded requests](./get-recorded-requests) step.

Only requests made after this step is executed will be recorded. If an action
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

<ResponseField name="Key" type="string" required>
  A unique key to identify the recorder. This key can be used in the [get
  recorded requests](./get-recorded-requests) step to wait for the request to
  complete.
</ResponseField>


Built with [Mintlify](https://mintlify.com).