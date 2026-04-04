# Source: https://docs.prefect.io/v3/api-ref/cli/automation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

#  

# `prefect automation`

```command  theme={null}
prefect automation [OPTIONS] COMMAND [ARGS]...
```

<Info>
  Manage automations.
</Info>

## `prefect automation ls`

```command  theme={null}
prefect automation ls [OPTIONS]
```

<Info>
  List all automations.
</Info>

## `prefect automation inspect`

```command  theme={null}
prefect automation inspect [OPTIONS] [NAME]
```

<Info>
  Inspect an automation.

  Arguments:

  name: the name of the automation to inspect

  id: the id of the automation to inspect

  yaml: output as YAML

  json: output as JSON

  Examples:

  `$ prefect automation inspect "my-automation"`

  `$ prefect automation inspect --id "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"`

  `$ prefect automation inspect "my-automation" --yaml`

  `$ prefect automation inspect "my-automation" --output json`
  `$ prefect automation inspect "my-automation" --output yaml`
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="NAME" type="string">
      An automation's name
    </ResponseField>
  </Accordion>

  <Accordion title="Options" defaultOpen>
    <ResponseField name="--id">
      An automation's id
    </ResponseField>

    <ResponseField name="--yaml">
      Output as YAML
    </ResponseField>

    <ResponseField name="--json">
      Output as JSON
    </ResponseField>

    <ResponseField name="--output">
      Specify an output format. Currently supports: json, yaml
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect automation resume`

```command  theme={null}
prefect automation resume [OPTIONS] [NAME]
```

<Info>
  Resume an automation.

  Arguments:

  name: the name of the automation to resume

  id: the id of the automation to resume

  Examples:

  `$ prefect automation resume "my-automation"`

  `$ prefect automation resume --id "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"`
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="NAME" type="string">
      An automation's name
    </ResponseField>
  </Accordion>

  <Accordion title="Options" defaultOpen>
    <ResponseField name="--id">
      An automation's id
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect automation enable`

```command  theme={null}
prefect automation enable [OPTIONS] [NAME]
```

<Info>
  Resume an automation.

  Arguments:

  name: the name of the automation to resume

  id: the id of the automation to resume

  Examples:

  `$ prefect automation resume "my-automation"`

  `$ prefect automation resume --id "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"`
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="NAME" type="string">
      An automation's name
    </ResponseField>
  </Accordion>

  <Accordion title="Options" defaultOpen>
    <ResponseField name="--id">
      An automation's id
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect automation pause`

```command  theme={null}
prefect automation pause [OPTIONS] [NAME]
```

<Info>
  Pause an automation.

  Arguments:

  name: the name of the automation to pause

  id: the id of the automation to pause

  Examples:

  `$ prefect automation pause "my-automation"`

  `$ prefect automation pause --id "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"`
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="NAME" type="string">
      An automation's name
    </ResponseField>
  </Accordion>

  <Accordion title="Options" defaultOpen>
    <ResponseField name="--id">
      An automation's id
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect automation disable`

```command  theme={null}
prefect automation disable [OPTIONS] [NAME]
```

<Info>
  Pause an automation.

  Arguments:

  name: the name of the automation to pause

  id: the id of the automation to pause

  Examples:

  `$ prefect automation pause "my-automation"`

  `$ prefect automation pause --id "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"`
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="NAME" type="string">
      An automation's name
    </ResponseField>
  </Accordion>

  <Accordion title="Options" defaultOpen>
    <ResponseField name="--id">
      An automation's id
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect automation delete`

```command  theme={null}
prefect automation delete [OPTIONS] [NAME]
```

<Info>
  Delete an automation.
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="NAME" type="string">
      An automation's name
    </ResponseField>
  </Accordion>

  <Accordion title="Options" defaultOpen>
    <ResponseField name="--id">
      An automation's id
    </ResponseField>

    <ResponseField name="--all">
      Delete all automations
    </ResponseField>
  </Accordion>
</AccordionGroup>

<Note>
  **Example:**

  `$ prefect automation delete "my-automation"`
  `$ prefect automation delete --id "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"`
  `$ prefect automation delete --all`
</Note>

## `prefect automation create`

```command  theme={null}
prefect automation create [OPTIONS]
```

<Info>
  Create one or more automations from a file or JSON string.
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--from-file">
      Path to YAML or JSON file containing automation(s)
    </ResponseField>

    <ResponseField name="--from-json">
      JSON string containing automation(s)
    </ResponseField>
  </Accordion>
</AccordionGroup>

<Note>
  **Example:**

  `$ prefect automation create --from-file automation.yaml`
  `$ prefect automation create -f automation.json`
  `$ prefect automation create --from-json '{"name": "my-automation", "trigger": {...}, "actions": [...]}'`
  `$ prefect automation create -j '[{"name": "auto1", ...}, {"name": "auto2", ...}]'`
</Note>

## `prefect automation update`

```command  theme={null}
prefect automation update [OPTIONS]
```

<Info>
  Update an existing automation from a file or JSON string.
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--id">
      The ID of the automation to update
    </ResponseField>

    <ResponseField name="--from-file">
      Path to YAML or JSON file containing the updated automation
    </ResponseField>

    <ResponseField name="--from-json">
      JSON string containing the updated automation
    </ResponseField>
  </Accordion>
</AccordionGroup>

<Note>
  **Example:**

  `$ prefect automation update --id "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa" --from-file automation.yaml`
  `$ prefect automation update --id "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa" -f automation.json`
  `$ prefect automation update --id "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa" --from-json '{"name": "updated-automation", "trigger": {...}, "actions": [...]}'`
</Note>


Built with [Mintlify](https://mintlify.com).