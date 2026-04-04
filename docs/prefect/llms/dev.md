# Source: https://docs.prefect.io/v3/api-ref/cli/dev.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

#  

# `prefect dev`

```command  theme={null}
prefect dev [OPTIONS] COMMAND [ARGS]...
```

<Info>
  Internal Prefect development.

  Note that many of these commands require extra dependencies (such as npm and MkDocs)
  to function properly.
</Info>

## `prefect dev build-docs`

```command  theme={null}
prefect dev build-docs [OPTIONS]
```

<Info>
  Builds REST API reference documentation for static display.
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--schema-path" />
  </Accordion>
</AccordionGroup>

## `prefect dev build-ui`

```command  theme={null}
prefect dev build-ui [OPTIONS]
```

<Info>
  Installs dependencies and builds UI locally. Requires npm.
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--no-install" />
  </Accordion>
</AccordionGroup>

## `prefect dev ui`

```command  theme={null}
prefect dev ui [OPTIONS]
```

<Info>
  Starts a hot-reloading development UI.
</Info>

## `prefect dev api`

```command  theme={null}
prefect dev api [OPTIONS]
```

<Info>
  Starts a hot-reloading development API.
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--host" />

    <ResponseField name="--port" />

    <ResponseField name="--log-level" />

    <ResponseField name="--services" />
  </Accordion>
</AccordionGroup>

## `prefect dev start`

```command  theme={null}
prefect dev start [OPTIONS]
```

<Info>
  Starts a hot-reloading development server with API, UI, and agent processes.

  Each service has an individual command if you wish to start them separately.
  Each service can be excluded here as well.
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--no-api" />

    <ResponseField name="--no-ui" />
  </Accordion>
</AccordionGroup>

## `prefect dev build-image`

```command  theme={null}
prefect dev build-image [OPTIONS]
```

<Info>
  Build a docker image for development.
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--arch">
      The architecture to build the container for. Defaults to the architecture of the host Python. \[default: x86\_64]
    </ResponseField>

    <ResponseField name="--python-version">
      The Python version to build the container for. Defaults to the version of the host Python. \[default: 3.12]
    </ResponseField>

    <ResponseField name="--flavor">
      An alternative flavor to build, for example 'conda'. Defaults to the standard Python base image
    </ResponseField>

    <ResponseField name="--build-arg">
      This will directly pass a --build-arg into the docker build process. Can be added to the command line multiple times.
    </ResponseField>

    <ResponseField name="--dry-run" />
  </Accordion>
</AccordionGroup>

## `prefect dev container`

```command  theme={null}
prefect dev container [OPTIONS]
```

<Info>
  Run a docker container with local code mounted and installed.
</Info>

<AccordionGroup>
  <Accordion title="Options" defaultOpen>
    <ResponseField name="--bg" />

    <ResponseField name="--name" />

    <ResponseField name="--api" />

    <ResponseField name="--tag" />
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).