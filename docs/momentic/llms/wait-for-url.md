# Source: https://momentic.ai/docs/steps/wait-for-url.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wait for URL

> Wait for the active page to match a URL

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

## Configs

<ResponseField name="Case sensitive" type="boolean">
  Ignore case when comparing the URL.
</ResponseField>

<ResponseField name="Negate comparison" type="boolean">
  Wait for the URL to NOT match the given pattern instead.
</ResponseField>


Built with [Mintlify](https://mintlify.com).