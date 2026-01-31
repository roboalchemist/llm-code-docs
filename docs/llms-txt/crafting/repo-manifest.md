# Source: https://docs.sandboxes.cloud/docs/repo-manifest.md

# Repo Manifest

## Overview

`Repo Manifest` defines how Crafting system automates the setup for a git repository in the workspace after checking out the code. It is in YAML format including the following information:

* [Hooks](#hooks): define what to do after checkout, and how to build;
* [Daemons](#daemons): define what should run inside the workspace;
* [Jobs](#jobs): define what to run based on schedules.

An example:

```yaml
env: # Environment variables shared by all hooks, daemons and jobs.
- DB_ROOT_PASSWORD=mysql
- RAILS_ENV=development

hooks:
  post-checkout:
    cmd: |
      bundle install
      bundle exec rake db:migrate
  build:
    cmd: |
      bundle exec rubocop

daemons:
  rails: # Name of the process is "rails", which is to launch a rails server on port 3001.
    run:
      cmd: bundle exec rails s -p 3001 -b 0.0.0.0

jobs:
  housekeep: # Name of job is "housekeep", which performs house keeping every 10 minutes.
    run: 
      cmd: ./housekeep  
    schedule: "*/10 * * * *"
```

### Location

The default manifest file in a source repository is `.sandbox/manifest.yaml`, unless override is specified in [Sandbox Definition](https://docs.sandboxes.cloud/docs/sandbox-definition#checkouts).

### Shared Environment

The top-level section `env` defines environment variables shared by all hooks, daemons and jobs. Each item must be defined in the form of `KEY=VALUE` (no spaces around `=`) where environment extraction `$NAME` and `${NAME}` are supported in `VALUE`.

### Hooks

Hooks are invoked at specific stage during workspace creation or automatic branch follow. The supported hooks are:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Hook
      </th>

      <th>
        When to Run
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        post-checkout
      </td>

      <td>
        Optional, after any new code change pulled from the remote repository.
      </td>
    </tr>

    <tr>
      <td>
        build
      </td>

      <td>
        After new code change is pulled from the remote repository, and after post-checkout.\
        If unspecified, no build will be performed.
      </td>
    </tr>
  </tbody>
</Table>

The value of each hook follows the [Run Schema](#run-schema).

All the hooks in the manifest are optional. If unspecified, the script `.sandbox/HOOK-NAME` will be attempted when the hook is supposed to be invoked. If the script doesn't exist, the hook is simply skipped (treated as success).

### Daemons

*Daemons* are long-running processes in the background. They are automatically launched (after a successful build if build hook is provided), unless `disable_on_start: true` is specified (see [Disable On Start](#disable-on-start) ). The `run` property follows the [Run Schema](#run-schema). The processes are managed by the workspace and kept running (restarted if failed). And they can be further controlled in the web console, or the CLI commands:

* `cs ps`
* `cs restart [NAME]`
* `cs stop [NAME]`
* `cs start [NAME]`
* `cs logs`

### Jobs

*Jobs* are one-shot processes executed based on a schedule. The property `schedule` defines the schedule using [crontab](https://man7.org/linux/man-pages/man5/crontab.5.html) format. The property `disable_on_start` set to `true` can be used to not schedule the job after workspace start (see [Disable On Start](#disable-on-start) ). The `run` property follows the [Run Schema](#run-schema). The process is not restarted if failed.

### Disable On Start

Both [Daemons](#daemons)  and [Jobs](#jobs) supports the property `disable_on_start` to not start/schedule after workspace startup. For example:

```yaml
daemons:
  rails: # Name of the process is "rails", which is to launch a rails server on port 3001.
    run:
      cmd: bundle exec rails s -p 3001 -b 0.0.0.0
    disable_on_start: true

jobs:
  housekeep: # Name of job is "housekeep", which performs house keeping every 10 minutes.
    run: 
      cmd: ./housekeep  
    schedule: "*/10 * * * *"
    disable_on_start: true
```

This has the effect to not start the daemon or schedule the job after workspace startup. Later, the daemon and job can be manually started/scheduled from either the UI or CLI.

### Run Schema

This schema defines how to run a process:

* `cmd`: defines the command line, and will be interpreted by `$SHELL -c`;
* `dir`: defines the working directory, default is the checkout directory of the source repository;
* `env`: a list of environment variables in the form of `KEY=VALUE` (no spaces around `=`) (overrides [Shared Environment](#shared-environment)) and environment extraction `$NAME` and `${NAME}` are supported.