# Source: https://momentic.ai/docs/steps/ai-extract.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# AI extract

> Use AI to get data from the page

The AI extract step allows you to pull textual information from the page in a
structured format. You can then reference that information in later steps using
variables.

If you would like our AI to interpret the page results instead of simply
returning data that already exists on the page, you should explicitly instruct
the AI to do so by using the keywords "interpret and then \[…]" or "analyze"

## Inputs

<ResponseField name="Description" type="string" required>
  A description of the data you'd like to extract. You should try to include a
  location or section of the page that the data should be extracted from. For
  example, "the pricing data in dollars from the plans table".
</ResponseField>

<ResponseField name="Schema" type="object">
  An optional JSON schema for the format the data should be returned in. The
  schema should follow the [official JSON schema
  specification](https://json-schema.org/learn/getting-started-step-by-step#introduction-to-json-schema).
</ResponseField>

## Configs

<ResponseField name="Save to environment variable" type="string">
  Store the output of this step into the environment at the given key. This
  configuration only applies for steps that output data.
</ResponseField>


Built with [Mintlify](https://mintlify.com).