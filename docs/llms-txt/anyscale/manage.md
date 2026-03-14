# Source: https://docs.anyscale.com/platform/workspaces/manage.md

# Source: https://docs.anyscale.com/jobs/manage.md

# Create and manage jobs

[View Markdown](/jobs/manage.md)

# Create and manage jobs

This page provides an overview of creating and managing Anyscale jobs.

## Submit a job[​](#submit-a-job "Direct link to Submit a job")

To submit your job to Anyscale, use the Python SDK or CLI and pass in any additional options or configurations for the job.

By default, Anyscale uses your workspace or cloud to provision a cluster to run your job. You can define a custom cluster through a [compute config](/reference/compute-config-api.md) or specify an existing cluster.

Once submitted, Anyscale runs the job as specified in the entrypoint command, which is typically a [Ray Job](https://docs.ray.io/en/latest/cluster/running-applications/job-submission/index.html). If the run doesn't succeed, the job restarts using the same entrypoint up to the number of `max_retries`.

* CLI
* SDK

Run the following command to submit a job:

```
anyscale job submit --name=my-job-name \
  --working-dir=. --max-retries=5 \
  --image-uri="anyscale/image/<image-name>:<image-version>" \
  --compute-config=<compute-config> \
  -- python main.py
```

With the CLI, you can either specify an existing compute config with `--compute-config=<compute-config-name>` or define a new one in a job YAML.

See [`anyscale job submit`](/reference/job-api.md#anyscale-job-submit).

Run the following command to submit a job:

```
import anyscale
from anyscale.job.models import JobConfig

config = JobConfig(
  name="my-job-name",
  entrypoint="python main.py",
  working_dir=".",
  max_retries=5,
  image_uri="anyscale/image/<image-name>:<image-version>",
  compute_config="<compute-config-name>"
)

anyscale.job.submit(config)
```

With the SDK, you can either specify an existing compute config or define a new one using the compute config API.

See [`anyscale.job.submit`](/reference/job-api.md#anyscalejobsubmit).

For a complete list of supported options defining a `JobConfig`, see [`JobConfig`](/reference/job-api.md#jobconfig).

## Define a job[​](#define-a-job "Direct link to Define a job")

You can define jobs in a YAML configuration file and submit them using the CLI.

Create your job configuration in a YAML file:

```
#my-job.yaml
name: my-job-name
entrypoint: python main.py

# Container image: Can be an Anyscale base image, external registry, or custom image
image_uri: anyscale/ray:2.51.1-slim-py312-cu128
# OR use containerfile: ./Dockerfile (see "Using a custom container" section below)

# Compute config: Can be name of existing config OR inline definition
# Use existing: compute_config: my-compute-config:1
# Or define inline as shown below
compute_config: 
  head_node:
    instance_type: m5.8xlarge
  worker_nodes:
    - instance_type: m5.4xlarge
      min_nodes: 1
      max_nodes: 5

working_dir: . # Local directory to upload (defaults to current directory)
requirements: # Python dependencies - can be list or path to requirements.txt
  - numpy==1.26.4
  - pandas==2.3.3
env_vars:
  MY_ENV_VAR: production
max_retries: 3
tags:
  team: ml-ops
```

For the complete list of available fields, see [`JobConfig`](/reference/job-api.md#jobconfig).

## Wait on a job[​](#wait-on-a-job "Direct link to Wait on a job")

You can block CLI and SDK commands until a job enters a specified state. By default, commands wait for `JobState.SUCCEEDED`. See [`JobState`](/reference/job-api.md#jobstate).

* CLI
* SDK

Run the following command to wait on a job:

```
anyscale job wait -n my-job-name
```

When you submit a job, you can specify `--wait`, which waits for the job to succeed or exits if the job fails.

```
anyscale job submit -n my-job-name --wait -- sleep 30
```

See [`anyscale job wait`](/reference/job-api.md#anyscale-job-wait).

Run the following command to submit and wait on a job:

```
import anyscale
from anyscale.job.models import JobConfig

config = JobConfig(name="my-job-name", entrypoint="sleep 30")

anyscale.job.submit(config)
anyscale.job.wait(name="my-job-name")
```

See [`anyscale.job.wait`](/reference/job-api.md#anyscalejobwait).

## Terminate a job[​](#terminate "Direct link to Terminate a job")

Terminate a job to stop the workload and the underlying cluster.

* Anyscale console
* CLI
* SDK

On the **Jobs** page in the [Anyscale console](https://console.anyscale.com/), open the job and click **Terminate**.

Run the following command to terminate a job:

```
anyscale job terminate --id 'prodjob_xxx'
```

See [`anyscale job terminate`](/reference/job-api.md#anyscale-job-terminate).

Run the following command to terminate a job:

```
import anyscale

anyscale.job.terminate(name="my-job-name")
```

See [`anyscale.job.terminate`](/reference/job-api.md#anyscalejobterminate).

## Archive a job[​](#archive-a-job "Direct link to Archive a job")

Archiving jobs hides them from the job list page, but you can still access them through the CLI and SDK. Anyscale automatically archives the cluster associated with an archived job.

You must have created the job or be an organization admin to archive a job. You can't archive running jobs. Terminate a job or wait for it to succeed or fail before archiving it.

You can archive jobs in the Anyscale console, CLI, or SDK.

* Anyscale console
* CLI
* SDK

On the **Jobs** page in the [Anyscale console](https://console.anyscale.com/), select the job and use the archive action.

Run the following command to archive a job:

```
anyscale job archive --id 'prodjob_...'
```

See [`anyscale job archive`](/reference/job-api.md#anyscale-job-archive).

Run the following command to archive a job:

```
import anyscale

anyscale.job.archive(name="my-job-name")
```

See [`anyscale.job.archive`](/reference/job-api.md#anyscalejobarchive).

## Delete a job[​](#delete-a-job "Direct link to Delete a job")

You can delete a job using the CLI or SDK. You can't delete running jobs. Terminate a job or wait for it to succeed or fail before deleting it.

* CLI
* SDK

Run the following command to delete a job:

```
anyscale job delete --id 'prodjob_...'
```

See [`anyscale job delete`](/reference/job-api.md#anyscale-job-delete).

Run the following command to delete a job:

```
import anyscale

anyscale.job.delete(name="my-job-name")
```

See [`anyscale.job.delete`](/reference/job-api.md#anyscalejobdelete).

## Manage dependencies[​](#manage-dependencies "Direct link to Manage dependencies")

When developing Anyscale jobs, you may need to include additional Python packages or system-level dependencies. There are several ways to manage these dependencies:

### Use a requirements.txt file[​](#use-a-requirementstxt-file "Direct link to Use a requirements.txt file")

The simplest way to manage Python package dependencies is by using a `requirements.txt` file.

1. Create a `requirements.txt` file in your project directory:

   ```
   emoji==2.12.1
   numpy==1.21.0
   ```

2. When submitting your job, include the `-r` or `--requirements` flag:

* CLI
* SDK

```
anyscale job submit --config-file my-job.yaml -r ./requirements.txt
```

```
import anyscale
from anyscale.job.models import JobConfig

config = JobConfig(
    name="my-job-name",
    entrypoint="python main.py",
    working_dir=".",
    requirements="./requirements.txt"
)

anyscale.job.submit(config)
```

This method works well for straightforward Python package dependencies. Anyscale installs these packages in the job's environment before running your code.

### Use a custom container[​](#use-a-custom-container "Direct link to Use a custom container")

For more complex dependency management, including system-level packages or specific environment configurations, use a custom container:

1. Create a `Dockerfile`:

   ```
   FROM anyscale/ray:2.10.0-py310

   # Install system dependencies if needed
   RUN apt-get update && apt-get install -y <your-system-packages>

   # Install Python dependencies
   COPY requirements.txt /tmp/
   RUN pip install -r /tmp/requirements.txt
   ```

2. Build and submit the job with the custom container:

* CLI
* SDK

```
anyscale job submit --config-file my-job.yaml --containerfile Dockerfile
```

```
import anyscale
from anyscale.job.models import JobConfig

config = JobConfig(
    name="my-job-name",
    entrypoint="python main.py",
    working_dir=".",
    containerfile="./Dockerfile"
)

anyscale.job.submit(config)
```

This method gives you full control over the job's environment, allowing you to install both system-level and Python packages.

### Use pre-built custom images[​](#use-pre-built-custom-images "Direct link to Use pre-built custom images")

For frequently used environments, you can build and reuse custom images:

1. Build the image:

* CLI
* SDK

```
anyscale image build -n my-custom-image --containerfile Dockerfile
```

```
import anyscale

image_uri = anyscale.image.build(
    containerfile="./Dockerfile",
    name="my-custom-image"
)
```

2. Use the built image in your job submission:

* CLI
* SDK

```
anyscale job submit --config-file my-job.yaml --image-uri anyscale/image/my-custom-image:1
```

```
import anyscale
from anyscale.job.models import JobConfig

config = JobConfig(
    name="my-job-name",
    entrypoint="python main.py",
    working_dir=".",
    image_uri="anyscale/image/my-custom-image:1"
)

anyscale.job.submit(config)
```

This approach is efficient for teams working on multiple jobs that share the same dependencies.
