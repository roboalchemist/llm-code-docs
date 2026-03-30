# Source: https://docs.prefect.io/v3/api-ref/cli/flow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

#  

# `prefect flow`

```command  theme={null}
prefect flow [OPTIONS] COMMAND [ARGS]...
```

<Info>
  View and serve flows.
</Info>

## `prefect flow ls`

```command  theme={null}
prefect flow ls [OPTIONS]
```

<Info>
  View flows.
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--limit" />
  </Accordion>
</AccordionGroup>

## `prefect flow serve`

```command  theme={null}
prefect flow serve [OPTIONS] ENTRYPOINT
```

<Info>
  Serve a flow via an entrypoint.
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="ENTRYPOINT" type="string" required>
      The path to a file containing a flow and the name of the flow function in the format `./path/to/file.py:flow_func_name`.  \[required]
    </ResponseField>
  </Accordion>

  <Accordion title="Options" defaultOpen>
    <ResponseField name="--name">
      The name to give the deployment created for the flow.
    </ResponseField>

    <ResponseField name="--description">
      The description to give the created deployment. If not provided, the description will be populated from the flow's description.
    </ResponseField>

    <ResponseField name="-v">
      A version to give the created deployment.
    </ResponseField>

    <ResponseField name="-t">
      One or more optional tags to apply to the created deployment.
    </ResponseField>

    <ResponseField name="--cron">
      A cron string that will be used to set a schedule for the created deployment.
    </ResponseField>

    <ResponseField name="--interval">
      An integer specifying an interval (in seconds) between scheduled runs of the flow.
    </ResponseField>

    <ResponseField name="--anchor-date">
      The start date for an interval schedule.
    </ResponseField>

    <ResponseField name="--rrule">
      An RRule that will be used to set a schedule for the created deployment.
    </ResponseField>

    <ResponseField name="--timezone">
      Timezone to used scheduling flow runs e.g. 'America/New\_York'
    </ResponseField>

    <ResponseField name="--pause-on-shutdown">
      If set, provided schedule will be paused when the serve command is stopped. If not set, the schedules will continue running.
    </ResponseField>

    <ResponseField name="--limit">
      The maximum number of runs that can be executed concurrently by the created runner; only applies to this served flow. To apply a limit across multiple served flows, use global\_limit.
    </ResponseField>

    <ResponseField name="--global-limit">
      The maximum number of concurrent runs allowed across all served flow instances associated with the same deployment.
    </ResponseField>
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).