# Source: https://docs.upsun.com/create-apps/runtime-operations.md

# Runtime operations

Runtime operations allow you to trigger one-off commands or scripts on your project.
Similar to [crons](https://docs.upsun.com/create-apps/image-properties/crons.md), they run in the app container but not on a specific schedule.
You can [define runtime operations](#define-a-runtime-operation) in your [app configuration](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md)
and [trigger them](#run-a-runtime-operation) at any time through the Upsun CLI.

For example, if you have a static website,
you may want to set up a runtime operation to occasionally fetch content from a backend system
without having to rebuild your whole app.

## Define a runtime operation

To define a runtime operation, add a configuration similar to the following:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    source:
      root: "/"
    operations:
      <RUNTIME_OPERATION_NAME>:
        role: <USER_ROLE>
        commands:
          start: <COMMAND>
```
When you define a runtime operation,
you can specify which users can trigger it according to their user `role`:

- `viewer`
- `contributor`
- `admin`

If you don't set the `role` option when configuring your runtime operation,
by default all users with the `contributor` role can trigger it.

For example, to allow admin users to clear the cache of a Drupal site,
you could define an operation like the following:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    source:
      root: "/"
    operations:
      clear-rebuild:
        role: admin
        commands:
          start: drush cache:rebuild
```
The name of the runtime operation in this case is `clear-rebuild`.

For more possibilities, see other [runtime operation examples](#runtime-operation-examples).

## Run a runtime operation

A runtime operation can be triggered through the Upsun CLI once it has been [defined](#define-a-runtime-operation).
Run the following command:

```bash {}
upsun operation:run <RUNTIME_OPERATION_NAME> --project <PROJECT_ID> --environment <ENVIRONMENT_NAME>
```

You can only trigger a runtime operation if you have permission to do so.
Permissions are granted through the ``role`` option specified in the [runtime operation configuration](#define-a-runtime-operation). This can only be done if a [runtime operation has been defined](#define-a-runtime-operation).
For example, to trigger the runtime operation [defined previously](#define-a-runtime-operation),
you could run the following command:

```bash {}
upsun operation:run clear-rebuild --project <PROJECT_ID> --environment <ENVIRONMENT_NAME>
```

## List your runtime operations

To list all the runtime operations available on an environment,
run the following command:

```bash
upsun operation:list --project <PROJECT_ID> --environment <ENVIRONMENT_NAME>
```

## Runtime operation examples

### Build your app when using a static site generator

During every Upsun deployment, a standard [`build` step](https://docs.upsun.com/learn/overview/build-deploy.md#the-build) is run.
When you use a static site generator like Gatsby
or Next.js with a headless backend
you need to run a second `build` step to get your app ready for production.

This is because, as its framework is being built,
your frontend needs to pull content-related data from your backend’s API
(to generate all the static HTML pages your site is to serve).
To accomplish this on Upsun, where each app goes through a build-deploy pipeline in parallel,
your frontend’s build must be delayed _until after_ your backend has fully deployed.
It's often delayed up until the [`post_deploy` hook](https://docs.upsun.com../create-apps/hooks/hooks-comparison.md#post-deploy-hook) stage,
when the filesystem is read-only.

You can use a runtime operation to trigger the second `build` step
after the initial deployment of your app or after a redeployment.
You can also trigger it when you need to fetch content from your backend
but want to avoid going through the whole Upsun [build and deploy processes](https://docs.upsun.com/learn/overview/build-deploy.md) again.

**Note**: 

The following examples assume that the frontend and backend containers are included in the same environment.
This isn’t necessary for the commands to run successfully.<BR>
What is necessary is that the build destination for your frontend **is  writable at runtime**
(meaning, you must [define a mount](https://docs.upsun.com/create-apps/image-properties/mounts.md) for it).
If you don’t want to include a build within a mount (especially if your data source **isn’t** on Upsun),
you can use [source operations](https://docs.upsun.com/create-apps/source-operations.md) to achieve a similar effect,
but through generating a new commit.

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    operations:
      gatsby-build:
        role: viewer
        commands:
          start: gatsby build
```

To trigger your runtime operation, run a command similar to the following:

```bash {}
upsun operation:run gatsby-build --project <PROJECT_ID> --environment <ENVIRONMENT_NAME>
```

To run the [Next.js build](https://nextjs.org/docs/deployment#nextjs-build-api) step,
define a runtime operation similar to the following:

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    operations:
      next-build:
        role: admin
        commands:
          # All below are valid, depending on your setup
          start: next build
          # start: npx next build
          # start: npm run build
```

To trigger your runtime operation, run a command similar to the following:

```bash {}
upsun operation:run next-build --project <PROJECT_ID> --environment <ENVIRONMENT_NAME>
```

### Execute actions on your Node.js app

You can define runtime operations for common [pm2](https://pm2.io/docs/runtime/overview/) process manager tasks.

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    operations:
      pm2-ping:
        role: admin
        commands:
          start: |
            # Assuming pm2 start npm --no-daemon --watch --name $APP -- start -- -p $PORT
            APP=$(cat package.json | jq -r '.name')
            pm2 ping $APP            
```

To trigger your runtime operation, run a command similar to the following:

```bash {}
upsun operation:run pm2-ping --project <PROJECT_ID> --environment <ENVIRONMENT_NAME>
```

To reload your Node.js app, define a runtime operation similar to the following:

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    operations:
      pm2-reload:
        role: admin
        commands:
          start: |
            # Assuming pm2 start npm --no-daemon --watch --name $APP -- start -- -p $PORT
            APP=$(cat package.json | jq -r '.name')
            pm2 reload $APP            
```

To trigger your runtime operation, run a command similar to the following:

```bash {}
upsun operation:run pm2-reload --project <PROJECT_ID> --environment <ENVIRONMENT_NAME>
```

To restart your Node.js app, define a runtime operation similar to the following:

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    operations:
      pm2-restart:
        role: admin
        commands:
          start: |
            # Assuming pm2 start npm --no-daemon --watch --name $APP -- start -- -p $PORT
            APP=$(cat package.json | jq -r '.name')
            pm2 restart $APP            
```

To trigger your runtime operation, run a command similar to the following:

```bash {}
upsun operation:run pm2-restart --project <PROJECT_ID> --environment <ENVIRONMENT_NAME>
```

### Define management commands on your Django project

On a Django project, you can [define custom `django-admin` commands](https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/), for example to run a one-off management command (`manual migration` in the example above) outside of the Django ORM migration framework.
To do so, define a runtime operation similar to the following:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    source:
      root: "/"
    type: python:3.14
    operations:
      manual-migration:
        role: admin
        commands:
          start: python manage.py manual_migration
```
To trigger your runtime operation, run a command similar to the following:

```bash
upsun operation:run manual-migration --project <PROJECT_ID> --environment <ENVIRONMENT_NAME>
```

