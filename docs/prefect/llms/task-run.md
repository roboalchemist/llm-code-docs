# Source: https://docs.prefect.io/v3/api-ref/cli/task-run.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

#  

# `prefect task-run`

```command  theme={null}
prefect task-run [OPTIONS] COMMAND [ARGS]...
```

<Info>
  View and inspect task runs.
</Info>

## `prefect task-run inspect`

```command  theme={null}
prefect task-run inspect [OPTIONS] ID
```

<Info>
  View details about a task run.
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="ID" type="string" required>
      \[required]
    </ResponseField>
  </Accordion>

  <Accordion title="Options" defaultOpen>
    <ResponseField name="--web">
      Open the task run in a web browser.
    </ResponseField>

    <ResponseField name="--output">
      Specify an output format. Currently supports: json
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect task-run ls`

```command  theme={null}
prefect task-run ls [OPTIONS]
```

<Info>
  View recent task runs
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--task-run-name">
      Name of the task
    </ResponseField>

    <ResponseField name="--limit">
      Maximum number of task runs to list
    </ResponseField>

    <ResponseField name="--state">
      Name of the task run's state
    </ResponseField>

    <ResponseField name="--state-type">
      Type of the task run's state
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect task-run logs`

```command  theme={null}
prefect task-run logs [OPTIONS] ID
```

<Info>
  View logs for a task run.
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="ID" type="string" required>
      \[required]
    </ResponseField>
  </Accordion>

  <Accordion title="Options" defaultOpen>
    <ResponseField name="--head">
      Show the first 20 logs instead of all logs.
    </ResponseField>

    <ResponseField name="--num-logs">
      Number of logs to show when using the --head or --tail flag. If None, defaults to 20.
    </ResponseField>

    <ResponseField name="--reverse">
      Reverse the logs order to print the most recent logs first
    </ResponseField>

    <ResponseField name="--tail">
      Show the last 20 logs instead of all logs.
    </ResponseField>
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).