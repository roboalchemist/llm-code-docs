# Source: https://docs.prefect.io/v3/api-ref/cli/concurrency-limit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

#  

# `prefect concurrency-limit`

```command  theme={null}
prefect concurrency-limit [OPTIONS] COMMAND [ARGS]...
```

<Info>
  Manage task-level concurrency limits.
</Info>

## `prefect concurrency-limit create`

```command  theme={null}
prefect concurrency-limit create [OPTIONS] TAG CONCURRENCY_LIMIT
```

<Info>
  Create a concurrency limit against a tag.

  This limit controls how many task runs with that tag may simultaneously be in a
  Running state.
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="TAG" type="string" required>
      \[required]
    </ResponseField>

    <ResponseField name="CONCURRENCY_LIMIT" type="string" required>
      \[required]
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect concurrency-limit inspect`

```command  theme={null}
prefect concurrency-limit inspect [OPTIONS] TAG
```

<Info>
  View details about a concurrency limit. `active_slots` shows a list of TaskRun IDs
  which are currently using a concurrency slot.
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="TAG" type="string" required>
      \[required]
    </ResponseField>
  </Accordion>

  <Accordion title="Options" defaultOpen>
    <ResponseField name="--output">
      Specify an output format. Currently supports: json
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect concurrency-limit ls`

```command  theme={null}
prefect concurrency-limit ls [OPTIONS]
```

<Info>
  View all concurrency limits.
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--limit" />

    <ResponseField name="--offset" />
  </Accordion>
</AccordionGroup>

## `prefect concurrency-limit reset`

```command  theme={null}
prefect concurrency-limit reset [OPTIONS] TAG
```

<Info>
  Resets the concurrency limit slots set on the specified tag.
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="TAG" type="string" required>
      \[required]
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect concurrency-limit delete`

```command  theme={null}
prefect concurrency-limit delete [OPTIONS] TAG
```

<Info>
  Delete the concurrency limit set on the specified tag.
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="TAG" type="string" required>
      \[required]
    </ResponseField>
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).