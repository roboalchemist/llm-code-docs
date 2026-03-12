# Source: https://docs.prefect.io/v3/api-ref/cli/event.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

#  

# `prefect event`

```command  theme={null}
prefect event [OPTIONS] COMMAND [ARGS]...
```

<Info>
  Stream events.
</Info>

## `prefect event stream`

```command  theme={null}
prefect event stream [OPTIONS]
```

<Info>
  Subscribes to the event stream of a workspace, printing each event
  as it is received. By default, events are printed as JSON, but can be
  printed as text by passing `--format text`.
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--format">
      Output format (json or text)
    </ResponseField>

    <ResponseField name="--output-file">
      File to write events to
    </ResponseField>

    <ResponseField name="--account">
      Stream events for entire account, including audit logs
    </ResponseField>

    <ResponseField name="--run-once">
      Stream only one event
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect event emit`

```command  theme={null}
prefect event emit [OPTIONS] EVENT
```

<Info>
  Emit a single event to Prefect.
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="EVENT" type="string" required>
      The name of the event  \[required]
    </ResponseField>
  </Accordion>

  <Accordion title="Options" defaultOpen>
    <ResponseField name="--resource">
      Resource specification as 'key=value' or JSON. Can be used multiple times.
    </ResponseField>

    <ResponseField name="--resource-id">
      The resource ID (shorthand for --resource prefect.resource.id=\<id>)
    </ResponseField>

    <ResponseField name="--related">
      Related resources as JSON string
    </ResponseField>

    <ResponseField name="--payload">
      Event payload as JSON string
    </ResponseField>
  </Accordion>
</AccordionGroup>

<Note>
  **Example:**

  ```bash  theme={null}
  # Simple event with resource ID
  prefect event emit user.logged_in --resource-id user-123

  # Event with payload
  prefect event emit order.shipped --resource-id order-456 --payload '{"tracking": "ABC123"}'

  # Event with full resource specification
  prefect event emit customer.subscribed --resource '{"prefect.resource.id": "customer-789", "prefect.resource.name": "ACME Corp"}'
  ```
</Note>


Built with [Mintlify](https://mintlify.com).