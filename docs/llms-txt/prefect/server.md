# Source: https://docs.prefect.io/v3/concepts/server.md

# Source: https://docs.prefect.io/v3/api-ref/cli/server.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

#  

# `prefect server`

```command  theme={null}
prefect server [OPTIONS] COMMAND [ARGS]...
```

<Info>
  Start a Prefect server instance and interact with the database
</Info>

## `prefect server start`

```command  theme={null}
prefect server start [OPTIONS]
```

<Info>
  Start a Prefect server instance
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--host" />

    <ResponseField name="--port" />

    <ResponseField name="--keep-alive-timeout" />

    <ResponseField name="--log-level" />

    <ResponseField name="--scheduler" />

    <ResponseField name="--analytics-on" />

    <ResponseField name="--late-runs" />

    <ResponseField name="--ui" />

    <ResponseField name="--no-services">
      Only run the webserver API and UI
    </ResponseField>

    <ResponseField name="--background">
      Run the server in the background
    </ResponseField>

    <ResponseField name="--workers">
      Number of worker processes to run. Only runs the webserver API and UI
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect server status`

```command  theme={null}
prefect server status [OPTIONS]
```

<Info>
  Check the status of the Prefect server.
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--wait">
      Wait for the server to become available before returning.
    </ResponseField>

    <ResponseField name="--timeout">
      Maximum number of seconds to wait when using --wait. A value of 0 means wait indefinitely.
    </ResponseField>

    <ResponseField name="--output">
      Specify an output format. Currently supports: json
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect server stop`

```command  theme={null}
prefect server stop [OPTIONS]
```

<Info>
  Stop a Prefect server instance running in the background
</Info>

## `prefect server database`

```command  theme={null}
prefect server database [OPTIONS] COMMAND [ARGS]...
```

<Info>
  Interact with the database.
</Info>

### `prefect server database reset`

```command  theme={null}
prefect server database reset [OPTIONS]
```

<Info>
  Drop and recreate all Prefect database tables
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--yes" />
  </Accordion>
</AccordionGroup>

### `prefect server database upgrade`

```command  theme={null}
prefect server database upgrade [OPTIONS]
```

<Info>
  Upgrade the Prefect database
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--yes" />

    <ResponseField name="-r">
      The revision to pass to `alembic upgrade`. If not provided, runs all migrations.
    </ResponseField>

    <ResponseField name="--dry-run">
      Flag to show what migrations would be made without applying them. Will emit sql statements to stdout.
    </ResponseField>
  </Accordion>
</AccordionGroup>

### `prefect server database downgrade`

```command  theme={null}
prefect server database downgrade [OPTIONS]
```

<Info>
  Downgrade the Prefect database
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--yes" />

    <ResponseField name="-r">
      The revision to pass to `alembic downgrade`. If not provided, downgrades to the most recent revision. Use 'base' to run all migrations.
    </ResponseField>

    <ResponseField name="--dry-run">
      Flag to show what migrations would be made without applying them. Will emit sql statements to stdout.
    </ResponseField>
  </Accordion>
</AccordionGroup>

### `prefect server database revision`

```command  theme={null}
prefect server database revision [OPTIONS]
```

<Info>
  Create a new migration for the Prefect database
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--message">
      A message to describe the migration.
    </ResponseField>

    <ResponseField name="--autogenerate" />
  </Accordion>
</AccordionGroup>

### `prefect server database stamp`

```command  theme={null}
prefect server database stamp [OPTIONS] REVISION
```

<Info>
  Stamp the revision table with the given revision; don't run any migrations
</Info>

<AccordionGroup>
  <Accordion title="Arguments" defaultOpen>
    <ResponseField name="REVISION" type="string" required>
      \[required]
    </ResponseField>
  </Accordion>
</AccordionGroup>

## `prefect server services`

```command  theme={null}
prefect server services [OPTIONS] COMMAND [ARGS]...
```

<Info>
  Interact with server loop services.
</Info>

### `prefect server services manager`

```command  theme={null}
prefect server services manager [OPTIONS]
```

<Info>
  This is an internal entrypoint used by `prefect server services start --background`.
  Users do not call this directly.

  We do everything in sync so that the child won't exit until the user kills it.
</Info>

### `prefect server services list-services`

```command  theme={null}
prefect server services list-services [OPTIONS]
```

<Info>
  List all available services and their status.
</Info>

### `prefect server services ls`

```command  theme={null}
prefect server services ls [OPTIONS]
```

<Info>
  List all available services and their status.
</Info>

### `prefect server services start-services`

```command  theme={null}
prefect server services start-services [OPTIONS]
```

<Info>
  Start all enabled Prefect services in one process.
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--background">
      Run the services in the background
    </ResponseField>
  </Accordion>
</AccordionGroup>

### `prefect server services start`

```command  theme={null}
prefect server services start [OPTIONS]
```

<Info>
  Start all enabled Prefect services in one process.
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--background">
      Run the services in the background
    </ResponseField>
  </Accordion>
</AccordionGroup>

### `prefect server services stop-services`

```command  theme={null}
prefect server services stop-services [OPTIONS]
```

<Info>
  Stop any background Prefect services that were started.
</Info>

### `prefect server services stop`

```command  theme={null}
prefect server services stop [OPTIONS]
```

<Info>
  Stop any background Prefect services that were started.
</Info>


Built with [Mintlify](https://mintlify.com).