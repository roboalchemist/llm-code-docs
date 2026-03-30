# Source: https://docs.prefect.io/v3/api-ref/cli/profile.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

#  

# `prefect profile`

```command  theme={null}
prefect profile [OPTIONS] COMMAND [ARGS]...
```

<Info>
  Select and manage Prefect profiles.
</Info>

## `prefect profile ls`

```command  theme={null}
prefect profile ls [OPTIONS]
```

<Info>
  List profile names.
</Info>

## `prefect profile create`

```command  theme={null}
prefect profile create [OPTIONS] NAME
```

<Info>
  Create a new profile.
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="NAME" type="string" required>
      \[required]
    </ResponseField>
  </Accordion>

  <Accordion title="Options" defaultOpen>
    <ResponseField name="--from">
      Copy an existing profile.
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect profile use`

```command  theme={null}
prefect profile use [OPTIONS] NAME
```

<Info>
  Set the given profile to active.
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="NAME" type="string" required>
      \[required]
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect profile delete`

```command  theme={null}
prefect profile delete [OPTIONS] NAME
```

<Info>
  Delete the given profile.
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="NAME" type="string" required>
      \[required]
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect profile rename`

```command  theme={null}
prefect profile rename [OPTIONS] NAME NEW_NAME
```

<Info>
  Change the name of a profile.
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="NAME" type="string" required>
      \[required]
    </ResponseField>

    <ResponseField name="NEW_NAME" type="string" required>
      \[required]
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect profile inspect`

```command  theme={null}
prefect profile inspect [OPTIONS] [NAME]
```

<Info>
  Display settings from a given profile; defaults to active.
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="NAME" type="string">
      Name of profile to inspect; defaults to active profile.
    </ResponseField>
  </Accordion>

  <Accordion title="Options" defaultOpen>
    <ResponseField name="--output">
      Specify an output format. Currently supports: json
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect profile populate-defaults`

```command  theme={null}
prefect profile populate-defaults [OPTIONS]
```

<Info>
  Populate the profiles configuration with default base profiles, preserving existing user profiles.
</Info>


Built with [Mintlify](https://mintlify.com).