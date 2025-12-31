# Source: https://docs.upsun.com/create-apps/image-properties/crons.md

# Source: https://docs.upsun.com/guides/symfony/crons.md

# Source: https://docs.upsun.com/create-apps/image-properties/crons.md

# crons


A cron dictionary that defines scheduled tasks for the app.

Optional in [single-runtime](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#primary-application-properties) and [composable](https://docs.upsun.com/create-apps/app-reference/composable-image.md#primary-application-properties) images.

The keys of the `crons` definition are the names of the cron jobs.
The names must be unique.

If an application defines both a `web` instance and `worker` instances, cron jobs run only on the `web` instance.

See how to [get cron logs](https://docs.upsun.com/increase-observability/logs/access-logs.md#container-logs).

The following table shows the properties for each job:

| Name               | Type                                         | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------|----------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `spec`             | `string`                                     | Yes      | The [cron specification](https://en.wikipedia.org/wiki/Cron#Cron_expression). To prevent competition for resources that might hurt performance, use `H` in definitions to indicate an unspecified but invariant time. For example, instead of using `0 * * * *` to indicate the cron job runs at the start of every hour, you can use `H * * * *` to indicate it runs every hour, but not necessarily at the start. This prevents multiple cron jobs from trying to start at the same time. |
| `commands`         | A [cron commands dictionary](#cron-commands) | Yes      | A definition of what commands to run when starting and stopping the cron job.                                                                                                                                                                                                                                                                                                                                                                                                               |
| `shutdown_timeout` | `integer`                                    | No       | When a cron is canceled, this represents the number of seconds after which a `SIGKILL` signal is sent to the process to force terminate it. The default is `10` seconds.                                                                                                                                                                                                                                                                                                                    |
| `timeout`          | `integer`                                    | No       | The maximum amount of time a cron can run before it's terminated. Defaults to the maximum allowed value of `86400` seconds (24 hours).                                                                                                                                                                                                                                                                                                                                                      |

Note that you can [cancel pending or running crons](https://docs.upsun.com/environments/cancel-activity.md).

### Cron commands

| Name    | Type     | Required | Description                                                                                                                                                                                                                                                                        |
|---------|----------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `start` | `string` | Yes      | The command that's run. It's run in [Dash](https://en.wikipedia.org/wiki/Almquist_shell).                                                                                                                                                                                          |
| `stop`  | `string` | No       | The command that's issued to give the cron command a chance to shutdown gracefully, such as to finish an active item in a list of tasks. Issued when a cron task is interrupted by a user through the CLI or Console. If not specified, a `SIGTERM` signal is sent to the process. |

```yaml {}
applications:
  <APP_NAME>:
    type: 'nodejs:24'
    source:
      root: "/"
    crons:
      mycommand:
        spec: 'H * * * *'
        commands:
          start: sleep 60 && echo sleep-60-finished && date
          stop: killall sleep
        shutdown_timeout: 18
```

    .upsun/config.yaml

```yaml {}
applications:
  <APP_NAME>:
    type: "composable:25.11"
    stack:
      runtimes: [ 'nodejs:24' ]
    source:
      root: "/"
    crons:
      mycommand:
        spec: 'H * * * *'
        commands:
          start: sleep 60 && echo sleep-60-finished && date
          stop: killall sleep
        shutdown_timeout: 18
```

In this example configuration, the crons `spec` key uses the `H` syntax.

### Single-runtime image: Example cron jobs

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'php:8.5'
    crons:
      # Run Drupal's cron tasks every 19 minutes.
      drupal:
        spec: '*/19 * * * *'
        commands:
          start: 'cd web ; drush core-cron'
      # But also run pending queue tasks every 7 minutes.
      # Use an odd number to avoid running at the same time as the `drupal` cron.
      drush-queue:
        spec: '*/7 * * * *'
        commands:
          start: 'cd web ; drush queue-run aggregator_feeds'

```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'ruby:4.0'
    crons:
      # Execute a rake script every 19 minutes.
      ruby:
        spec: '*/19 * * * *'
        commands:
          start: 'bundle exec rake some:task'

```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'php:8.5'
    crons:
      # Run Laravel's scheduler every 5 minutes.
      scheduler:
        spec: '*/5 * * * *'
        commands:
          start: 'php artisan schedule:run'

```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: 'php:8.5'
    crons:
      # Take a backup of the environment every day at 5:00 AM.
      snapshot:
        spec: 0 5 * * *
        commands:
          start: |
            # Only run for the production environment, aka main branch
            if [ "$PLATFORM_ENVIRONMENT_TYPE" = "production" ]; then
                croncape symfony ...
            fi            

```

### Composable image: Example cron jobs

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: "composable:25.11"
    stack:
      runtimes: [ "php@8.4" ]
    crons:
      # Run Drupal's cron tasks every 19 minutes.
      drupal:
        spec: '*/19 * * * *'
        commands:
          start: 'cd web ; drush core-cron'
      # But also run pending queue tasks every 7 minutes.
      # Use an odd number to avoid running at the same time as the `drupal` cron.
      drush-queue:
        spec: '*/7 * * * *'
        commands:
          start: 'cd web ; drush queue-run aggregator_feeds'
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: "composable:25.11"
    stack:
      runtimes: [ "ruby@4.0" ]
    crons:
      # Execute a rake script every 19 minutes.
      ruby:
        spec: '*/19 * * * *'
        commands:
          start: 'bundle exec rake some:task'
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: "composable:25.11"
    stack:
      runtimes: [ "php@8.4" ]
    crons:
      # Run Laravel's scheduler every 5 minutes.
      scheduler:
        spec: '*/5 * * * *'
        commands:
          start: 'php artisan schedule:run'
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    type: "composable:25.11"
    stack:
      runtimes: [ "php@8.4" ]
    crons:
      # Take a backup of the environment every day at 5:00 AM.
      snapshot:
        spec: 0 5 * * *
        commands:
          start: |
            # Only run for the production environment, aka main branch
            if [ "$PLATFORM_ENVIRONMENT_TYPE" = "production" ]; then
                croncape symfony ...
            fi            
```

### Conditional crons

If you want to set up customized cron schedules depending on the environment type,
define conditional crons.
To do so, use a configuration similar to the following:

```yaml {}
applications:
  myapp:
    type: 'php:8.5'
    source:
      root: "/"
    crons:
      update:
        spec: '0 0 * * *'
        commands:
          start: |
            if [ "$PLATFORM_ENVIRONMENT_TYPE" = production ]; then
              upsun backup:create --yes --no-wait
              upsun source-operation:run update --no-wait --yes
            fi            
```

    .upsun/config.yaml

```yaml {}
applications:
  myapp:
    type: "composable:25.11"
    source:
      root: "/"
    stack:
      runtimes: [ "php@8.4" ]
    crons:
      update:
        spec: '0 0 * * *'
        commands:
          start: |
            if [ "$PLATFORM_ENVIRONMENT_TYPE" = production ]; then
              upsun backup:create --yes --no-wait
              upsun source-operation:run update --no-wait --yes
            fi            
```

### Cron job timing

The minimum time between cron jobs being triggered is 5 minutes.

For each app container, only one cron job can run at a time.
If a new job is triggered while another is running, the new job is paused until the other completes.

To minimize conflicts, a random offset is applied to all triggers.
The offset is a random number of seconds up to 20 minutes or the cron frequency, whichever is smaller.

Crons are also paused while activities such as [backups](https://docs.upsun.com/environments/backup.md) are running.
The crons are queued to run after the other activity finishes.

To run cron jobs in a timezone other than UTC, set the `timezone` property property as described for the image type ([single-runtime image](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#primary-application-properties) or
[composable image](https://docs.upsun.com/create-apps/app-reference/composable-image.md#primary-application-properties)).

To run cron jobs in a timezone other than UTC, set the [timezone property](https://docs.upsun.com/create-apps/timezone.md).

### Paused crons

[Preview environments](https://docs.upsun.com/glossary.md#preview-environment) are often used for a limited time and then abandoned.
While it's useful for environments under active development to have scheduled tasks,
unused environments don't need to run cron jobs.
To minimize unnecessary resource use,
crons on environments with no deployments are paused.

This affects all preview environments _and_ production environments that do not yet have a domain attached to them.

Such environments with deployments within 14 days have crons with the status `running`.
If there haven't been any deployments within 14 days, the status is `paused`.

You can see the status in the Console
or using the CLI by running `upsun environment:info` and looking under `deployment_state`.

#### Restarting paused crons

If the crons on your preview environment are paused but you're still using them,
you can push changes to the environment or redeploy it.

To restart crons without changing anything:

Run the following command:

```bash {}
upsun redeploy
```


