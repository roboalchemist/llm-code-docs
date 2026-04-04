# Source: https://docs.prefect.io/v3/api-ref/cli/variable.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

#  

# `prefect variable`

```command  theme={null}
prefect variable [OPTIONS] COMMAND [ARGS]...
```

<Info>
  Manage variables.
</Info>

## `prefect variable ls`

```command  theme={null}
prefect variable ls [OPTIONS]
```

<Info>
  List variables.
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--limit">
      The maximum number of variables to return.
    </ResponseField>

    <ResponseField name="--output">
      Specify an output format. Currently supports: json
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect variable inspect`

```command  theme={null}
prefect variable inspect [OPTIONS] NAME
```

<Info>
  View details about a variable.
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="NAME" type="string" required>
      \[required]
    </ResponseField>
  </Accordion>

  <Accordion title="Options" defaultOpen>
    <ResponseField name="--output">
      Specify an output format. Currently supports: json
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect variable get`

```command  theme={null}
prefect variable get [OPTIONS] NAME
```

<Info>
  Get a variable's value.
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="NAME" type="string" required>
      \[required]
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect variable set`

```command  theme={null}
prefect variable set [OPTIONS] NAME VALUE
```

<Info>
  Set a variable.

  If the variable already exists, use `--overwrite` to update it.
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="NAME" type="string" required>
      \[required]
    </ResponseField>

    <ResponseField name="VALUE" type="string" required>
      \[required]
    </ResponseField>
  </Accordion>

  <Accordion title="Options" defaultOpen>
    <ResponseField name="--overwrite">
      Overwrite the variable if it already exists.
    </ResponseField>

    <ResponseField name="--tag">
      Tag to associate with the variable.
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect variable unset`

```command  theme={null}
prefect variable unset [OPTIONS] NAME
```

<Info>
  Unset a variable.
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="NAME" type="string" required>
      \[required]
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect variable delete`

```command  theme={null}
prefect variable delete [OPTIONS] NAME
```

<Info>
  Unset a variable.
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="NAME" type="string" required>
      \[required]
    </ResponseField>
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).