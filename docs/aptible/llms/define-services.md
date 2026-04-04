# Source: https://www.aptible.com/docs/how-to-guides/app-guides/define-services.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to define services

Learn how to define [services](/core-concepts/apps/deploying-apps/services)

## Implicit Service (CMD)

If your App's [Image](/core-concepts/apps/deploying-apps/image/overview) includes a `CMD` and/or `ENTRYPOINT` declaration, a single implicit `cmd` service will be created for it when you deploy your App.

[Containers](/core-concepts/architecture/containers/overview) for the implicit `cmd` Service will execute the `CMD` your image defines (if you have an `ENTRYPOINT` defined, then the `CMD` will be passed as arguments to the `ENTRYPOINT`).

This corresponds to Docker's behavior when you use `docker run`, so if you've started Containers for your image locally using `docker run my-image`, you can expect Containers started on Aptible to behave identically.

Typically, the `CMD` declaration is something you'd add in your Dockerfile, like so:

```sql  theme={null}
FROM alpine:3.5
ADD . /app
CMD ["/app/run"]
```

> 📘 Using an implicit service is recommended if your App only has one Service.

## Explicit Services (Procfiles)

Procfiles are used to define explicit services for an app. They are optional; in the absence of a Procfile, Aptible will fall back to an Implicit Service. Explicit services allow you to specify commands for each service, like `web` or `worker` while implicit services use the `cmd` or `ENTRYPOINT` defined in the image.

### Step 01: Providing a Procfile

There are two ways to provide a Procfile:

* **Deploying via Git Push:**

  If you are deploying via Git, add a file named 

  `Procfile`

   at the root of your repository.

* **Deploying via Docker Image:**

  If you are using Docker Image, it must be located at 

  `/.aptible/Procfile`

   in your Docker image. See 

  [Procfiles and `.aptible.yml` with Direct Docker Image Deploy](/core-concepts/apps/deploying-apps/image/deploying-with-docker-image/procfile-aptible-yml-direct-docker-deploy)

   for more information.

> 📘 Note the following when using Procfile:
> **-Procfile syntax:** The [Procfile syntax is standardized](https://ddollar.github.io/foreman/), and consists of a mapping of one or more Service names to commands that should be executed for those Services. The two should be separated by a `:` character.
> **-Procfile commands:** The commands in your Procfile (i.e. the section to the right of the : character) is interpreted differently depending on whether your image has an ENTRYPOINT or not:

### Step 02: Executing your Procfile

#### Images without an `ENTRYPOINT`

If your image does not have an `ENTRYPOINT`, the Procfile will be executed using a shell (`/bin/sh`). This means you can use shell syntax, such as:

```sql  theme={null}
web: setup && run "$ENVIRONMENT"
```

**Advanced: PID 1 in your Container is a shell**

> 📘 The following is advanced information. You don't need to understand or leverage this information to use Aptible, but it might be relevant if you want to precisely control the behavior of your Containers. PID 1 is the process that receives signals when your Container is signaled (e.g. PID receives `SIGTERM` when your Container needs to shut down during a deployment). Since a shell is used as the command in your Containers to interpret your Procfile, this means PID 1 will be a shell. Shells don't typically forward signals, which means that when your Containers receive `SIGTERM`, they'll do nothing if a shell is running as PID 1. As a result, running a shell there may not be desirable.

If you'd like to get the shell out of the equation when running your Containers, you can use the exec call, like so:

```sql  theme={null}
web: setup && exec run "$ENVIRONMENT"
```

This will replace the shell with the run program as PID 1.

#### Images with an `ENTRYPOINT`

If your image has an `ENTRYPOINT`, Aptible will not use a shell to interpret your Procfile. Instead, your Procfile line is split according to shell rules, then simply passed to your Container's `ENTRYPOINT` as a series of arguments.

For example, if your Procfile looks like this:

```
web: run "$ENVIRONMENT"
```

Then, your `ENTRYPOINT` will receive the **literal** strings `run` and `$ENVIRONMENT` as arguments (i.e. the value for `$ENVIRONMENT` will **not** be interpolated).

This means your Procfile doesn't need to reference commands that exist in your Container: it only means to reference commands that make sense to your `ENTRYPOINT`.

However, it also means that you can't interpolate variables in your Procfile line. If you do need shell processing for interpolation with an `ENTRYPOINT`, here are two options:

**Call a shell from the Procfile**

The simplest option is to alter your `Procfile` to call a shell itself, like so:

```sql  theme={null}
web: sh -c 'setup && exec run "$ENVIRONMENT"'
```

**Use a launcher script**

A better approach is to add a launcher script in your Docker image, and delegate shell processing there. To do so, create a file called `/app.sh` in your image, with the following contents, and make it executable:

```sql  theme={null}
#!/bin/sh
# Make this executable
# Adjust the commands as needed, of course!
setup && exec run "$ENVIRONMENT"
```

Once you have this launcher script, your Procfile can simply reference the launcher script, which is simpler and more explicit:

```sql  theme={null}
web: /app.sh
```

Of course, you can use any name you like: `/app.sh` isn't the only one that works! Just make sure the Procfile references the launcher script.

## Step 03: Scale your services (optionally)

Aptible will automatically provision the services defined in your Procfile into app containers. You can scale services independently via the Aptible Dashboard or Aptible CLI:

```sql  theme={null}
aptible apps:scale SERVICE [--container-count COUNT] [--container-size SIZE_MB]
```

When a service is scaled with 2+ containers, the platform will automatically deploy your app containers with high availability.
