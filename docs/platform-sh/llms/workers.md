# Source: https://docs.upsun.com/create-apps/workers.md

# Source: https://docs.upsun.com/create-apps/image-properties/workers.md

# workers


Defines the list of worker names, which are alternate copies of the application to run as background processes.

Optional in [single-runtime](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#primary-application-properties) and [composable](https://docs.upsun.com/create-apps/app-reference/composable-image.md#primary-application-properties) images.

Workers require resource definition using `upsun resources:set`, same as application containers.
For more information, see how to [manage resources](https://docs.upsun.com/manage-resources.md).

Workers are exact copies of the code and compilation output as a `web` instance after a [`build` hook](https://docs.upsun.com/create-apps/image-properties/hooks.md).
They use the same container image.

Workers can't accept public requests and so are suitable only for background tasks.
If they exit, they're automatically restarted.

```yaml {}
applications:
  <APP_NAME>:
    type: 'python:3.14'
    source:
      root: "/"
    workers:
      queue:
        commands:
          start: |
            ./worker.sh            
```

The keys of the ``workers`` definition are the names of the workers.
You can then define how each worker differs from the ``web`` instance using
the [primary application properties](https://docs.upsun.com/create-apps/app-reference/composable-image.md#primary-application-properties).
Each worker can differ from the ``web`` instance in all properties except for:

 - ``crons`` as cron jobs don’t run on workers
 - ``hooks`` as the ``build`` hook must be the same
and the ``deploy`` and ``post_deploy`` hooks don’t run on workers.

A worker named ``queue`` that was small and had a different start command could look like this:

    .upsun/config.yaml

```yaml {}
applications:
  <APP_NAME>:
    type: "composable:25.11"
    source:
      root: "/"
    stack:
      runtimes: [ "python@3.14" ]
    workers:
      queue:
        commands:
          start: |
            ./worker.sh            
```


