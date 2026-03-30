# Source: https://momentic.ai/docs/steps/get-recorded-requests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get recorded requests

> Retrieve recorded requests

Retrieve recorded requests from a given recorder key. This step must be used
after the [record requests](../steps/record-requests) step to access the
captured requests and their responses.

## Inputs

<ResponseField name="Recorder key" type="string" required>
  The unique key of the recorded requests you want to retrieve. This key should
  match the one used in the [record requests](../steps/record-requests) step.
</ResponseField>

## Configs

<ResponseField name="Save to environment variable" type="string">
  Store the output of this step into the environment at the given key. This
  configuration only applies for steps that output data.
</ResponseField>

## Outputs

<ResponseField name="Requests" type="Array">
  <Expandable title="properties">
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

    <ResponseField name="response" type="Response object">
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
  </Expandable>
</ResponseField>


Built with [Mintlify](https://mintlify.com).