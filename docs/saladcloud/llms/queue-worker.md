# Source: https://docs.salad.com/container-engine/how-to-guides/job-processing/queue-worker.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Job Queue Worker

*Last Updated: October 15, 2024*

# Overview

To work with a job queue, you'll need to customize the container that you deploy on SaladCloud to include some way to
receive jobs from the Job Queue, pass them to your application, then receive the results from your application and
return them to the Queue. For this purpose, we provide a Job Queue Worker as a precompiled go binary which can be
included and run inside your container. You can download it from
[Github](https://github.com/SaladTechnologies/salad-cloud-job-queue-worker). Note that the binary will work for any
Linux-based image.

> 📘 Prerequisites
>
> The examples that follow can be found on [GitHub](https://github.com/SaladTechnologies/salad-cloud-job-queue-worker).
> If you want to follow along with the sample images, download them to your pc with
>
> `git clone https://github.com/SaladTechnologies/salad-cloud-job-queue-worker.git`

# Managing Multiple Processes

To configure your container to receive Jobs from a Job Queue, you'll be running two processes in the same container -
your application, as well as the Job Queue Worker. There are many ways to manage multiple processes in a single
container, and we outline two such methods for you below.

## Build a wrapper image with s6-overlay

In this example, we are going to build a new image which uses `s6-overlay` to serve as a hypervisor for both your
primary application and the Job Queue Worker process. Here's how to do it.

1. You'll need to include the Job Queue Worker in your container. In this example, we first download the binary to our
   local machine and build it into our container image by adding a `COPY` command to the Dockerfile.
   1. Alternatively, you may choose to download and unpack the SDK when your container is built by including `ADD` and
      `RUN` commands in your Dockerfile, or expand your entrypoint to include the download/unpack process.
   2. You may compare the SHA256 checksum of your downloaded file with the one found on the Github releases page.

2. Now we will build your original image. As an example, see
   [samples/mandelbrot/base/](https://github.com/SaladTechnologies/salad-cloud-job-queue-worker/tree/main/samples/mandelbrot/base) -
   this is a simple container that receives requests and returns images of the mandelbrot set. It uses `uvicorn` to
   listen on port 80 on the `generate` path for requests to be handled by the mandelbrot generation code.

   ```dockerfile dockerfile theme={null}
   FROM python:3.11-slim
   WORKDIR /app
   COPY ./requirements.txt \*.py ./
   RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
   CMD ["uvicorn", "main:app", "--host", "*", "--port", "80"]
   ```

   1. Navigate to the
      [samples/mandelbrot/base/](https://github.com/SaladTechnologies/salad-cloud-job-queue-worker/tree/main/samples/mandelbrot/base)
      directory and run `docker build -t foobar .`
   2. Notice that the name of the output container image in this case is `foobar`; you may substitute any name you like.
      The image with that name will not be pushed to any registry and will remain solely on your local disk.

3. Because the resulting container will run two processes, we will use the `s6-overlay` hypervisor to manage them. It
   has to be configured with the way to start your application, as probably indicated in CMD or ENTRYPOINT lines in the
   original Dockerfile. As an example, see
   [samples/mandelbrot/with-s6-overlay/](https://github.com/SaladTechnologies/salad-cloud-job-queue-worker/tree/main/samples/mandelbrot/with-s6-overlay)

   ```dockerfile  theme={null}
   FROM foobar

   WORKDIR /app

   ARG S6_OVERLAY_VERSION=3.1.6.2
   ENV S6_KEEP_ENV=1

   RUN apt-get update && \
       apt-get -y install xz-utils curl && \
       apt-get clean && \
       rm -rf /var/lib/apt/lists/*
   ADD https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-noarch.tar.xz /tmp
   RUN \
     tar -C / -Jxpf /tmp/s6-overlay-noarch.tar.xz && \
     rm -rf /tmp/s6-overlay-noarch.tar.xz
   ADD https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-x86_64.tar.xz /tmp
   RUN \
     tar -C / -Jxpf /tmp/s6-overlay-x86_64.tar.xz && \
     rm -rf /tmp/s6-overlay-x86_64.tar.xz
   COPY --chmod=755 s6 /etc/

   COPY --chmod=755 ./salad-job-queue-worker /usr/local/bin/

   ENTRYPOINT ["/init"]
   CMD ["/usr/local/bin/salad-job-queue-worker"]
   ```

   1. The s6 configuration files are stored in
      [samples/mandelbrot/with-s6-overlay/s6/s6-overlay/s6-rc.d/](https://github.com/SaladTechnologies/salad-cloud-job-queue-worker/tree/main/samples/mandelbrot/with-s6-overlay/s6/s6-overlay/s6-rc.d).
      You'll find the configuration for the sample service already there. The configuration must have two files, type
      and run. You can copy over the type from the provided sample, but the run \*\*must \*\*contain the command which
      starts your application: it is equivalent to the CMD or ENTRYPOINT in your original Dockerfile.

4. Next, build the wrapper image. First locate the line `FROM foobar` and replace `foobar` with whatever name you used
   in the previous step, save the file, and build the wrapper image:
   1. `docker build -t my-company/my-image -f docker/Dockerfile .`
   2. Note that the the name of the image here is important. That is what you are going to deploy to the SaladCloud .
   3. Replace `my-company/my-image` with whatever name you want the resulting image to have.

```dockerfile dockerfile theme={null}
FROM foobar

WORKDIR /app

# install the s6-overlay
ARG S6_OVERLAY_VERSION=3.1.6.2

RUN apt-get update \
    && apt-get install -y xz-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ADD https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-noarch.tar.xz /tmp
RUN tar -C / -Jxpf /tmp/s6-overlay-noarch.tar.xz

ADD https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-x86_64.tar.xz /tmp
RUN tar -C / -Jxpf /tmp/s6-overlay-x86_64.tar.xz

# copy previously downloaded salad-queue-client
COPY salad-http-job-queue-worker /usr/local/bin/

# copy the s6-overlay configuration
COPY --chmod=755 s6 /etc/

ENV S6_KEEP_ENV=1

ENTRYPOINT ["/init"]
CMD ["/usr/local/bin/salad-http-job-queue-worker"]
```

5. You will need to note the *port* and *path* of your application within the container for use in the next step, when
   you're configuring your container group to include a connection to a job queue. This port and path are where the
   queue worker SDK will be sending the jobs to. In our example, we have the following values:
   1. Port: **80**
   2. Path: **generate**

## Build a wrapper image with a shell script

In order to add the salad-queue-client into the image we are going to build a new image which uses a shell script.
Here's how to do it.

1. First, you'll need to include the job queue worker SDK in your container. In this example, we first download the
   binary to our local machine and build it into our container image by adding a `COPY` command to the Dockerfile.
   Alternatively, you may choose to download and unpack the SDK when your container starts by including `ADD` and `RUN`
   commands in your Dockerfile.
   1. The binary will work for any Linux-based base image.

2. Now we will build your original image. As an example, see
   [samples/mandelbrot/base/](https://github.com/SaladTechnologies/salad-cloud-job-queue-worker/tree/main/samples/mandelbrot/base) -
   this is a simple container that receives JSON requests on port 80 at the `generate` path and returns images of the
   mandelbrot set. It uses `uvicorn` to listen on port 80 for requests to be handled by the mandelbrot generation code.

   ```dockerfile dockerfile theme={null}
   FROM python:3.11-slim
   WORKDIR /app
   COPY ./requirements.txt \*.py ./
   RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
   CMD ["uvicorn", "main:app", "--host", "*", "--port", "80"]
   ```

   1. Navigate to the
      [samples/mandelbrot/base/](https://github.com/SaladTechnologies/salad-cloud-job-queue-worker/tree/main/samples/mandelbrot/base)
      directory and run `docker build -t foobar .`
   2. Notice that the name of the output container image in this case is `foobar`; you may substitute any name you like.
      The image with that name will not be pushed to any registry and will remain solely on your local disk.

3. Because the resulting container will run two processes we will use a shell script run.sh to manage the multiple
   processes. The relevant sample is in the
   [samples/mandelbrot/with-shell-script/](https://github.com/SaladTechnologies/salad-cloud-job-queue-worker/tree/main/samples/mandelbrot/with-shell-script):

   ```dockerfile dockerfile theme={null}
   FROM foobar

   WORKDIR /app

   # copy previously downloaded salad-http-job-queue-worker
   COPY ./salad-http-job-queue-worker /usr/local/bin/
   # copy the shell script
   COPY run.sh ./

   CMD ["/app/run.sh"]
   ```

   1. Locate the line `FROM foobar` and replace `foobar` with whatever name you used in the previous step.

   2. Save the file.

   3. Open the shell script `run.sh`:

      ```shell  theme={null}
      #!/bin/bash

      # Start the salad-http-job-queue-worker
      /usr/local/bin/salad-http-job-queue-worker &

      # Start the rest service
      uvicorn main:app --host '*' --port 80 &

      # Wait for any process to exit
      wait -n

      # Exit with status of process that exited first
      exit $?
      ```

   4. Locate the line `uvicorn main:app --host '\*' --port 80 &` and replace the start command with whatever is required
      to start your application, it is indicated in either `ENTRYPOINT` or `CMD` directive in the original Dockerfile.
      In our example, we can leave it as-is.

4. Now, build the wrapper image with `docker build -t my-company/my-image -f docker/Dockerfile .` Note that the the name
   of the image here is important. That is what you are going to deploy to the SaladCloud . Replace
   `my-company/my-image` with whatever the name you want the resulting image to have.

5. You will need to note the *port* and *path* of your application within the container for use in the next step, when
   you're configuring your container group to include a connection to a job queue. This port and path are where the
   queue worker SDK will be sending the jobs to. In our example, we have the following values:
   1. Port: **80**
   2. Path: **generate**

# Pushing the image to a Registry

Regardless of which path you chose, you should now have an image built with your application, the Job Queue Worker, and
some way of managing both processes. It's time to push it to the container registry of your choice. Learn more about the
registries supported by SaladCloud at
[Container Registries](/container-engine/explanation/infrastructure-platform/container-registries).

# Additional notes about the SaladCloud Job Queue Worker;

* The Worker needs to connect to a local HTTP server running inside of SEL, our special version of Linux running on the
  host machine behind your container replica. This means you won't be able to test the Job Queue Worker locally.
* By default, the Worker logging level is set to `error`. Logs will be sent to the
  [SaladCloud Container Logs](/container-engine/explanation/container-groups/container-logs) or your
  [external logging](/container-engine/explanation/infrastructure-platform/external-logging) tools. You can adjust the
  logging level by adding a 'SALAD\_QUEUE\_WORKER\_LOG\_LEVEL'
  [environment variable](/container-engine/how-to-guides/environment-variables).

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-configure-job-queue-worker-log-level.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=38d39b5d7b2ff1a6b69977efd5691f19" data-og-width="472" width="472" data-og-height="434" height="434" data-path="container-engine/images/portal-configure-job-queue-worker-log-level.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-configure-job-queue-worker-log-level.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=92fb723f363548e77c75a8d3c2cfb077 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-configure-job-queue-worker-log-level.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=153734c664f7f2cdbfcef6df46c64996 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-configure-job-queue-worker-log-level.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=ef18493e0d36508a0ead201ff0fb6c8f 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-configure-job-queue-worker-log-level.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=49f86c4fde58bdc500cd36546e734dbb 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-configure-job-queue-worker-log-level.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=98ec02492999fcf1b1a5cb3bb67c643c 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-configure-job-queue-worker-log-level.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=759283daeac92a20be58029d2a26bd9b 2500w" />

* The value can be changed to `warn`, `info`, and `debug`. If the logging level is set to `debug` the worker will output
  a heartbeat log every few seconds as it checks for a new job. That log will look something like this
  `time="2024-04-26T14:30:42Z" level=info msg=heartbeat file="[worker.go:162]"`.
* If you choose not to use any Startup and/or Readiness probes, the Job Queue Worker will immediately start to look for
  jobs, even if your application inside is not yet ready to receive jobs. If this happens, the job will fail and you\`ll
  need to submit it again.
  [Read more about health probes here. ](/container-engine/explanation/infrastructure-platform/health-probes)
