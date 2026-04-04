# Source: https://docs.prefect.io/v3/api-ref/cli/profiles.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

#  

# `prefect profiles`

```command  theme={null}
prefect profiles [OPTIONS] COMMAND [ARGS]...
```

<Info>
  Select and manage Prefect profiles.
</Info>

## `prefect profiles ls`

```command  theme={null}
prefect profiles ls [OPTIONS]
```

<Info>
  List profile names.
</Info>

## `prefect profiles create`

```command  theme={null}
prefect profiles create [OPTIONS] NAME
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

## `prefect profiles use`

```command  theme={null}
prefect profiles use [OPTIONS] NAME
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

## `prefect profiles delete`

```command  theme={null}
prefect profiles delete [OPTIONS] NAME
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

## `prefect profiles rename`

```command  theme={null}
prefect profiles rename [OPTIONS] NAME NEW_NAME
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

## `prefect profiles inspect`

```command  theme={null}
prefect profiles inspect [OPTIONS] [NAME]
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

## `prefect profiles populate-defaults`

```command  theme={null}
prefect profiles populate-defaults [OPTIONS]
```

<Info>
  Populate the profiles configuration with default base profiles, preserving existing user profiles.
</Info>


Built with [Mintlify](https://mintlify.com).