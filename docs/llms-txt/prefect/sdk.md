# Source: https://docs.prefect.io/v3/api-ref/cli/sdk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

#  

# `prefect sdk`

```command  theme={null}
prefect sdk [OPTIONS] COMMAND [ARGS]...
```

<Info>
  Manage Prefect SDKs. (beta)
</Info>

## `prefect sdk generate`

```command  theme={null}
prefect sdk generate [OPTIONS]
```

<Info>
  (beta) Generate a typed Python SDK from workspace deployments.

  The generated SDK provides IDE autocomplete and type checking for your deployments.
  Requires an active Prefect API connection (use `prefect cloud login` or configure
  PREFECT\_API\_URL).

  
  Examples:
  Generate SDK for all deployments:
  \$ prefect sdk generate --output ./my\_sdk.py

  Generate SDK for specific flows:
  \$ prefect sdk generate --output ./my\_sdk.py --flow my-etl-flow

  Generate SDK for specific deployments:
  \$ prefect sdk generate --output ./my\_sdk.py --deployment my-flow/production
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--output">
      Output file path for the generated SDK.
    </ResponseField>

    <ResponseField name="--flow">
      Filter to specific flow(s). Can be specified multiple times.
    </ResponseField>

    <ResponseField name="--deployment">
      Filter to specific deployment(s). Can be specified multiple times. Use 'flow-name/deployment-name' format for exact matching.
    </ResponseField>
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).