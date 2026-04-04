# Source: https://docs.salad.com/container-engine/how-to-guides/job-processing/kelpie.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🐕 Salad Kelpie

> Managing long-running tasks on SaladCloud with Salad Kelpie

*Last Updated: June 11, 2025*

# Managing Long-Running Tasks on SaladCloud with 🐕 Kelpie

Managing long running tasks, such as molecular simulations, LoRA training, and LLM finetuning, presents unique
challenges on SaladCloud, due primarily to the interruptible nature of nodes. At the core of all solutions to this
problem are a job queue, and progress checkpoints. The job queue is responsible for distributing tasks to workers, and
detecting when a worker has been interrupted. Workloads should save checkpoints of their progress and upload it to cloud
storage, so that they can be resumed from the last checkpoint in the event of an interruption. Workers should also
upload completed artifacts to cloud storage.

<Frame caption="Basic architecture for long-running tasks on SaladCloud">
  <img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=0aecbde9d765a2712eb7293c4e0d2466" alt="Basic Architecture" data-og-width="2719" width="2719" data-og-height="1275" height="1275" data-path="container-engine/images/lrt-basic-arch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=3d0b91baef22a492d5a7c48971b3f95c 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=3c02fb0e88ba714b93aafce5e2c3b864 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=8c04940f12b79accdb53fbbfde12c341 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=a19ee1a0a51acce431a99ab7da564acc 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=c5fc29cc18ef306cd484c4102768d7c7 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=39a8fed8ff7194c233e20d4199d36514 2500w" />
</Frame>

We will use [🐕 Kelpie](https://github.com/SaladTechnologies/kelpie) as our job queue and
[Cloudflare R2](https://www.cloudflare.com/developer-platform/products/r2/), an S3-compatible object storage service, as
our cloud storage. We prefer R2 to AWS S3 for many SaladCloud workloads, because R2 does not charge for egress data, and
SaladCloud's distributed nodes are not in datacenters, and therefore may incur egress fees from other providers. Kelpie
handles all interactions with the storage service, so your job will only need to write to the local file system, and
Kelpie will take care of uploading the files to R2.

For this guide, we will build an application that slowly calculates a sum for *n* steps, sleeping for 30 seconds between
steps to simulate work. We will set up a storage bucket and a checkpoint saving system, and enable Kelpie's autoscaling
to handle scaling the number of workers based on the number of jobs in the queue.

## The Job Queue: Kelpie

[🐕 Kelpie](https://github.com/SaladTechnologies/kelpie) is an open-source job queue that is particularly focused on the
challenges of running extremely long tasks on interruptible hardware, and has been used in production for hundreds of
thousands of hours of molecular dynamics simulations and AI model finetuning. It is designed to be simple to instrument,
and to be able to integrate with any containerized workload. It executes scripts in a container according to a job
definition, and optionally handles downloading input data, uploading output data, and syncing progress checkpoints to
your s3-compatible storage. It also provides a mechanism for scaling your container group in response to job volume. It
has deep integrations with SaladCloud that are very convenient for our purposes. It has no cost to use on SaladCloud.

You can use your Salad API key to authenticate with Kelpie, which will allow you to submit and manage jobs. Kelpie can
authenticate automatically from a SaladCloud node.

Kelpie uses the Salad container group ID as a queue name, which can be retrieved with the
[Get Container Group Endpoint](/reference/saladcloud-api/container-groups/get-container-group).

You can explore the full API with the [Swagger UI](https://kelpie.saladexamples.com/docs).

## Cloud Storage: R2

R2 is a cloud storage service from Cloudflare that is compatible with the S3 API. It is a great choice for SaladCloud
workloads because it does not charge egress fees, and SaladCloud's distributed nodes are mostly not in datacenters, and
therefore may incur egress fees from other providers.

From the [R2 console](https://dash.cloudflare.com/), navigate to "R2 Object Storage", and click "Create Bucket".

<Frame caption="The R2 Object Storage Console">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-console.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=2e5dbef1bda3c805645010f16a740b22" alt="The R2 Object Storage Console" data-og-width="1586" width="1586" data-og-height="975" height="975" data-path="container-engine/images/r2-console.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-console.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=fee2371d67fbc4c480459d1754e429b6 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-console.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=d197faf89d1cf41e2c061a5c339fcae2 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-console.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=05ec55c00d6f6c2481ba6e0f980605f2 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-console.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=2ad475415ec5164d5c8f8da3e9f2a764 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-console.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=2b4667441e4cf4759defdb89940d15ba 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-console.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=b7c7aeb7e521dd434557df0d7bb05847 2500w" />
</Frame>

Give your bucket a meaningful name, and select an appropriate location. We are going to use the standard storage class,
and automatic location.

<Frame caption="Creating a new bucket">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-create-bucket.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=f71883c122d1b1cfaeb6f648b4bb8bb4" alt="Creating a new bucket" data-og-width="852" width="852" data-og-height="751" height="751" data-path="container-engine/images/r2-create-bucket.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-create-bucket.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=9147b9b03b491c1707fd7e4218c014fe 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-create-bucket.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=4b3eb82d2dfac7cf44ad9e943f40c890 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-create-bucket.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=a1be0c5dfa12017cd56b04bee6a87899 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-create-bucket.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=ae3898b74e3219b8237a5598c4c60099 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-create-bucket.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=1e5b7c9b0d901323648d8981b1518092 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-create-bucket.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=e638ffd448b8c00c4033f2b28fa2a63f 2500w" />
</Frame>

Once your bucket is created, you will need to create an access key and secret key. Select "Manage API tokens" from the
"\{ } API" menu, and click "Create Token".

<Frame caption="You still need an API token to access your bucket">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-api-tokens.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=2c921bc691340fd4a3cd2bde7f52554c" alt="Navigate to manage api tokens" data-og-width="1285" width="1285" data-og-height="515" height="515" data-path="container-engine/images/r2-api-tokens.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-api-tokens.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=468911096b31050679e649db785328e6 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-api-tokens.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=58c6df3f944c833421f8010a7706be78 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-api-tokens.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=af1e7d2e570538908eab92b7f3a90771 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-api-tokens.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=44853ad19d73b4f5c77a652712d835f4 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-api-tokens.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=9fc262018d58166786a955a5f0a93d27 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-api-tokens.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=b760a42100aa8b30884facdf8c13e627 2500w" />
</Frame>

Create a token with "Object Read & Write" permissions, and only grant it access to the bucket we've just created. Since
secret rotation is outside the scope of this guide, we're going to use the "forever" TTL. However, it is best practice
to user shorter-lived secrets and to have easy automatic mechanisms in place to rotate secrets as needed.

Once created you will be given an access key and secret key. Save these somewhere safe, as you will not be able to
retrieve them again. The application code will get these keys from environment variables, so you will need to set them
in your environment. Also on that page will be the S3 endpoint URL for your bucket. Save this as well, as it will be
needed in the application code.

## Instrumenting Our Application

Using Kelpie just requires adding the Kelpie worker binary to your container, and setting it to run as the command in
your Dockerfile. The worker binary will read the job queue, and execute the job script with the provided arguments. The

```dockerfile  theme={null}
# Start with a base image that has the dependencies you need,
# and can successfully run your script.
FROM yourimage:yourtag

# Add the kelpie binary to your container image
ARG KELPIE_VERSION=0.6.0
ADD https://github.com/SaladTechnologies/kelpie/releases/download/${KELPIE_VERSION}/kelpie /kelpie
RUN chmod +x /kelpie

# Use kelpie as the "main" command. Kelpie will then execute your
# command with the provided arguments and environment variables
# from the job definition, from the WORKDIR of the container.
CMD ["/kelpie"]
```

### Code

Our actual application code can be very simple:

```python  theme={null}
import json
import time
import sys

def do_the_actual_work(num_steps: int, checkpoint: dict, checkpoint_file: str) -> int | None:
    '''
    Do the actual work for the job. This function will simulate work by
    sleeping for 30 seconds and incrementing the step and sum in the
    checkpoint.

    Parameters:
    - num_steps: int, the number of steps to run
    - checkpoint: dict, the checkpoint
    - checkpoint_file: str, the checkpoint file
    '''
    print(f"Max steps: {num_steps}", flush=True)
    print(f"Starting step: {checkpoint['step']}", flush=True)
    while checkpoint['step'] < num_steps:
        # Simulate work
        print(f"step {checkpoint['step']}", flush=True)
        time.sleep(30)
        # Update the checkpoint.
        checkpoint['step'] += 1
        checkpoint['sum'] += checkpoint['step']
        with open(checkpoint_file, 'w') as f:
            json.dump(checkpoint, f)

    print(f"Job Finished. Sum: {checkpoint['sum']}", flush=True)
    return checkpoint['sum']


if __name__ == '__main__':
    '''
    Main function to run the job. This function will read the number of steps
    to run, the checkpoint file, and the output file from the command line
    arguments.
    '''
    usage = f"Usage: python {sys.argv[0]} <num_steps> <checkpoint_file> <output_file>"
    if len(sys.argv) != 4:
        print(usage, file=sys.stderr)
        sys.exit(1)
    num_steps = int(sys.argv[1])
    checkpoint_file = sys.argv[2]
    output_file = sys.argv[3]

    checkpoint = {'step': 0, 'sum': 0}

    # Load the checkpoint if it exists
    try:
        with open(checkpoint_file, 'r') as f:
            checkpoint = json.load(f)
    except FileNotFoundError:
        # If the checkpoint file does not exist, we start from scratch
        pass

    sum = do_the_actual_work(num_steps, checkpoint, checkpoint_file)

    # Write the final sum to the output file
    with open(output_file, 'w') as f:
        f.write(str(sum))
```

You'll notice that the script does not interact with Kelpie directly, or with the storage service directly. It simply
reads the command line arguments, which are provided by Kelpie, and writes to the local file system. Kelpie will handle
the rest, including uploading the checkpoint file and output file to the storage service, and updating the job status in
the queue.

### Dockerfile

```dockerfile  theme={null}
FROM python:3.10.12-slim-buster

# Our app has no dependencies, but yours probably does.
WORKDIR /app

# Our app has no dependencies, but yours probably does.
# If you have a requirements.txt, uncomment the next two lines
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# Copy your main application code into the container.
COPY main.py .

# Set up directories for checkpoints and outputs.
RUN mkdir -p checkpoints && \
    mkdir -p outputs

# Add the kelpie binary to your container image
ARG KELPIE_VERSION=0.6.0
ADD https://github.com/SaladTechnologies/kelpie/releases/download/${KELPIE_VERSION}/kelpie /kelpie
RUN chmod +x /kelpie

# Use kelpie as the "main" command. Kelpie will then execute your
# command with the provided arguments and environment variables
# from the job definition, from the WORKDIR of the container.
CMD ["/kelpie"]
```

## Building and Testing the Worker

Now, build the docker image, and use a tag that makes sense for you.

```shell  theme={null}
docker build -t saladtechnologies/lrt-worker-examples:kelpie .
```

You can push this image to Docker Hub or any other container registry you prefer.

```shell  theme={null}
docker push saladtechnologies/lrt-worker-examples:kelpie
```

We can test the image locally by running it with our Salad API Key and a contrived container group ID.

First, generate a random UUID to use as the container group ID. You can use the `uuidgen` command on Linux or macOS, or
use an online UUID generator. Do this again to simulate a machine ID.

```shell  theme={null}
uuidgen
# b26a8cb1-1806-454f-80df-9721a6e76910
uuidgen
# 4b659cb9-d508-4e1e-9cee-7116d36dd542
```

Create a file called `worker.env` with the following contents, replacing `<your_api_key>` with your Salad API key and
`<container_group_id>` with the UUID you generated above. Some of these will not be required in production, as they can
be derived automatically from the SaladCloud node, but we will set them explicitly for local testing.

```env  theme={null}
SALAD_API_KEY=your-api-key
SALAD_ORGANIZATION=your-organization-name
SALAD_PROJECT=your-project-name
SALAD_CONTAINER_GROUP_ID=b26a8cb1-1806-454f-80df-9721a6e76910
SALAD_MACHINE_ID=4b659cb9-d508-4e1e-9cee-7116d36dd542
AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
AWS_ENDPOINT_URL=your-s3-endpoint-url
AWS_REGION=auto
```

Then, run the container with the environment variables set:

```shell  theme={null}
docker run --rm \
  --env-file worker.env \
  saladtechnologies/lrt-worker-examples:kelpie
```

You should see the Kelpie worker start up, and it will wait for jobs to be submitted to the queue. You will see logs
that it is failing to set the
[deletion cost](/container-engine/explanation/infrastructure-platform/instance-deletion-cost), because we are not
running on SaladCloud, but this is not an issue for our purposes.

## Submitting Jobs to the Queue

Now we need to populate the queue with jobs. First, we'll define some environment variables in a new file
`submitter.env`.

```shell  theme={null}
SALAD_API_KEY=your-api-key
SALAD_ORGANIZATION=your-organization-name
SALAD_PROJECT=your-project-name
SALAD_CONTAINER_GROUP_ID=b26a8cb1-1806-454f-80df-9721a6e76910
BUCKET_NAME=long-running-tasks-checkpoints-and-artifacts
```

I've saved mine in a file called `submitter.env`, and I'm going to source them into my environment with the following
command:

```shell  theme={null}
export $(grep -v '^#' submitter.env | xargs -d '\n')
```

Suppose we have a csv with our 10,000 jobs, and we want to submit them all. Our CSV (data.csv) looks like this, with
10,000 rows.

```csv  theme={null}
job_id,steps
job-0,600
job-1,600
job-2,600
job-3,600
```

We can submit all of these jobs with the following code:

```python  theme={null}
import csv
import os
import requests
import sys

salad_api_key = os.getenv('SALAD_API_KEY')
salad_organization = os.getenv('SALAD_ORGANIZATION')
salad_project = os.getenv('SALAD_PROJECT')
container_group_id = os.getenv('SALAD_CONTAINER_GROUP_ID')
bucket_name = os.getenv('BUCKET_NAME')

kelpie_api_url = "https://kelpie.saladexamples.com"
batch_size = 100

kelpie_headers = {
    "Salad-Api-Key": salad_api_key,
    "Salad-Organization": salad_organization,
    "Salad-Project": salad_project,
    "Content-Type": "application/json"
}


def submit_one_batch(jobs: list) -> None:
    '''
    Kelpie API can accept up to 100 jobs in a single batch submission.
    '''
    response = requests.post(
        f"{kelpie_api_url}/jobs/batch", headers=kelpie_headers, json=jobs)
    if response.status_code != 202:
        print(f"Error submitting jobs: {response.text}")


def job_to_kelpie_job(id: str, steps: int) -> dict:
    return {
        # Our Container Group ID is used as a Job Queue ID
        "container_group_id": container_group_id,

        # We define how to run our job
        "command": "python",
        "arguments": [
            "main.py",
            str(steps),
            f"checkpoints/checkpoint.json",
            f"outputs/sum.txt"
        ],

        # We define the storage actions needed for the job
        "sync": {

            # Before the job runs, we download the checkpoint file
            "before": [
                {
                    "bucket": bucket_name,
                    "prefix": f"{id}/checkpoints/",
                    "local_path": "checkpoints/",
                    "direction": "download"
                }
            ],

            # During the job, we upload the checkpoint file when it changes
            "during": [
                {
                    "bucket": bucket_name,
                    "prefix": f"{id}/checkpoints/",
                    "local_path": "checkpoints/",
                    "direction": "upload"
                }
            ],

            # After the job runs, we upload the output file
            "after": [
                {
                    "bucket": bucket_name,
                    "prefix": f"{id}/outputs/",
                    "local_path": "outputs/",
                    "direction": "upload"
                }
            ]
        }
    }


if __name__ == "__main__":
    '''
    Main function to read the jobs from a CSV file and submit them to the Kelpie API.
    The CSV file should have two columns: job_id and steps.
    '''

    # We can pass a max number of jobs to submit as an argument. Helpful for testing.
    max_jobs = sys.argv[1] if len(sys.argv) > 1 else None

    jobs = []
    total_jobs = 0
    with open('data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            job_id = row['job_id']
            steps = int(row['steps'])
            jobs.append(job_to_kelpie_job(job_id, steps))
            total_jobs += 1
            if max_jobs and total_jobs >= int(max_jobs):
                break
            if len(jobs) >= batch_size:
                submit_one_batch(jobs)
                jobs = []
    if jobs:
        submit_one_batch(jobs)
        jobs = []
    print(
        f"All jobs submitted successfully. Total jobs submitted: {total_jobs}")

```

This code reads the jobs from a CSV file, converts them to Kelpie job definitions, and submits them to the Kelpie API in
batches of 100. The job definitions specify the command to run, the arguments to pass, and the storage actions to take
before, during, and after the job runs. The checkpoint file is downloaded before the job runs, uploaded during the job
when it changes, and the output file is uploaded after the job runs.

You can run this code with the following command:

```shell  theme={null}
python submit_jobs.py 1
```

You should see output indicating that the jobs were submitted successfully. If you check your running container, you
should see it pick up a job and start working.

## Deploying the Worker to SaladCloud

To deploy our worker to SaladCloud, we need to create a new Container Group. This can be done via the API, SDKs, or the
Portal. We're going to use the Portal.

We're going to create a new Container Group, and we're going to use the image we just pushed to Docker Hub. We're going
to request 100 replicas (the max via the portal), and we're going to set most, but not all, of our environment variables
from `worker.env`.

<Frame caption="Creating a new Container Group">
  <img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-create-1.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=36675eed9c00e66e2c5970df22d879b7" alt="Creating a new Container Group" data-og-width="1423" width="1423" data-og-height="802" height="802" data-path="container-engine/images/kelpie-cg-create-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-create-1.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=906557351637e71dc9f7724c46001c48 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-create-1.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=1cbb678e20dcc0d120ed6d44d7bd468f 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-create-1.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=86eb8adcf11828cab8487252c6ec311f 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-create-1.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=df6acc171d113d5dfe9cb2d0d2bab857 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-create-1.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=f23bcb267f3cb4585f00ed1978d0bd82 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-create-1.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=31717e609f385d7059eaf2b00ecce123 2500w" />
</Frame>

Our application is extremely simple, so we're going to only request 1 vCPU, 1 GB of RAM, and no GPU. Your hardware
requirements are likely significantly higher than this.

<Frame caption="Setting the hardware requirements">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-2.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=a6e12a31a937c12b0de03d713e844d6f" alt="Setting the hardware requirements" data-og-width="640" width="640" data-og-height="1054" height="1054" data-path="container-engine/images/rabbitmq-cg-create-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-2.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=9fd829b30ec46f7072ea74a508e9f6c3 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-2.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=85130c045494468b6e6eacf9ef0422e8 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-2.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=f6b10ec1fb9db3da50cfb09083b2e52a 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-2.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=eea02ca1d8b49eeec5d06ecf9568e01b 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-2.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=1b937e1214e99747f49e009f41cb9b6d 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-2.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=872124dba8ddf0793a4bcb000eb8fa0f 2500w" />
</Frame>

All CPU-only jobs are prioritized as "Batch" (the lowest tier), and we don't need any additional storage for this
particular application.

<Frame caption="Setting the job priority and storage requirements">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-3.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=f264406369197b18cd18363a6ccc7715" alt="Setting the job priority and storage requirements" data-og-width="645" width="645" data-og-height="565" height="565" data-path="container-engine/images/rabbitmq-cg-create-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-3.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=36af05427fa5b1e3dc4a85e125b94b5a 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-3.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=28f90a0015e980059c42320363aff9f1 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-3.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=f90cdb3281ecab7fdb8627c7d8607daa 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-3.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=11071214196206337b42f93c22512081 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-3.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=e6960da4d19dfce04250e122c54a01b9 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-3.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=3aca73bd56a10669ea26347944b040da 2500w" />
</Frame>

We do not need the container gateway, as our application pulls its work from a queue. We also do not need health probes,
as those are primarily for services accessed via Container Gateway. Go ahead and hit deploy, and you'll be taken to the
container group page, where you can see its status.

First, it will prepare by pulling the container image into our high-performance cache.

<Frame caption="Preparing the container">
  <img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-preparing.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=9202e387dc5851952f9656d0c59d6c8c" alt="Preparing the container" data-og-width="1341" width="1341" data-og-height="630" height="630" data-path="container-engine/images/kelpie-cg-preparing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-preparing.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=ecafb9dc4437841b94d1dcfddae465b5 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-preparing.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=27ae308d9b5a7aedfd1618210d2d9ae0 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-preparing.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=44dab1f61402ffd585326fe1330e8beb 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-preparing.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=c73c550468d948c0e84de28f50a17c9b 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-preparing.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=2738cab5190298b0ff775a30395177f2 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-preparing.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=7fa06499a4dd040cc2fd63502d194016 2500w" />
</Frame>

Once it's prepared, it will start allocating replicas, and downloading the container image to those replicas.

<Frame caption="Allocating replicas">
  <img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-allocating.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=217fa9db5a8fe8968ad41f3d8c3328dd" alt="Allocating replicas" data-og-width="1323" width="1323" data-og-height="922" height="922" data-path="container-engine/images/kelpie-cg-allocating.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-allocating.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=a3f6203ff89960f9d00435d8255e1963 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-allocating.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=9255a78fc7884f70761251b65d5537f9 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-allocating.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=92186f746590c1a0849fd9114a92ddcc 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-allocating.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=3d4c2b7f963815372f9d5b56b0437ef2 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-allocating.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=7c1ae93f6dba8f39c43b5cdfd40ea08b 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-allocating.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=caf89adbf425f6f42b4d8209e6888cde 2500w" />
</Frame>

Once the replicas are allocated, they will start downloading the container image from our internal cache. This can take
a few minutes, depending on the size of the image.

<Frame caption="Downloading the images to the replicas">
  <img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-downloading.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=1e97525f1eebb569f83bce059f925d4b" alt="Downloading the images to the replicas" data-og-width="1278" width="1278" data-og-height="963" height="963" data-path="container-engine/images/kelpie-cg-downloading.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-downloading.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=24823fbc7f101e930344e89be3c6402d 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-downloading.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=972b72c0116afa2fcaff48002f5b70b6 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-downloading.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=06c8a0597ef44640ed28e3fa95c8ece2 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-downloading.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=18805391074042109bcf92dcb3762c65 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-downloading.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=7b15de46bb020a4c9e6ef2dbe00ba664 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-downloading.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=f1369bbf08caae73c2c3e2d395267f82 2500w" />
</Frame>

After a minute or so, we should see our instances up and running.

<Frame caption="Instances up and running">
  <img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-running.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=5011aca50cd2f9665d48b7f6befe07c0" alt="Instances up and running" data-og-width="1269" width="1269" data-og-height="968" height="968" data-path="container-engine/images/kelpie-cg-running.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-running.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=af289a933c1903c9b2ef36e34abd0de6 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-running.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=4f10a2b4e8a2ce3286eb14d115b7a778 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-running.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=c3ea4bba3b3642f668c5284464828b22 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-running.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=e628a2535a05e034b89fce917bf8e4a5 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-running.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=9be912f3e7b2140fbb5369e83ce7a233 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-cg-running.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=5350f16e110358809f2718156abff33a 2500w" />
</Frame>

## Validating That It Works

Now that our cluster is up and running, we need to retrieve the container group id from the
[Get Container Group Endpoint](/reference/saladcloud-api/container-groups/get-container-group) and set it in our
`submitter.env` variables, and then run our job submitter script to submit jobs to the queue.

```shell  theme={null}
export $(grep -v '^#' submitter.env | xargs -d '\n')
python submit-jobs.py
```

Then, we'll be able to see our jobs being processed in our container group logs:

<Frame caption="Kelpie worker hard at work">
  <img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-logs.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=90966c6a1b3ce230d689ca7c66c5c860" alt="Kelpie worker hard at work" data-og-width="1274" width="1274" data-og-height="1098" height="1098" data-path="container-engine/images/kelpie-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-logs.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=d42dcfeaa86e44d84de7fce309151dae 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-logs.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=7fc69b244cad1566d7e41c9de26202b9 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-logs.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=33fba4b9645227c65a2662750e931384 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-logs.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=719088703002dffcf268862bcda85e08 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-logs.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=4a20f1fd71d3c970816015561901a92e 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/kelpie-logs.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=85fb723c49b0558b30207fc4e227a155 2500w" />
</Frame>

We can also see this by querying the Kelpie API for the jobs in the queue. The
[List Jobs Endpoint](https://kelpie.saladexamples.com/docs#/default/get_ListJobs) lets us query by status and container
group ID.

```shell  theme={null}
curl -X 'GET' \
  'https://kelpie.saladexamples.com/jobs?status=running&container_group_id=<your-container-group-id>&page_size=2' \
  -H 'accept: application/json' \
  -H 'Salad-Api-Key: <your-salad-api-key>' \
  -H 'Salad-Organization: <your-salad-organization>' \
  -H 'Salad-Project: <your-salad-project>'
```

You'll get a list of jobs that are currently running, and you can see the job ID, status, and other details. Learn more
about [job lifecycle](https://github.com/SaladTechnologies/kelpie?tab=readme-ov-file#job-lifecycle) and
[job statuses](https://github.com/SaladTechnologies/kelpie?tab=readme-ov-file#understanding-job-status).

```json  theme={null}
{
  "_count": 2,
  "jobs": [
    {
      "id": "0376cf91-6287-4783-82ae-456054c5d4ef",
      "user_id": "5b0f6331-fc03-423c-919e-11728c2b97b2",
      "status": "running",
      "created": "2025-06-11T14:59:14.000Z",
      "started": "2025-06-11T14:59:18.000Z",
      "heartbeat": "2025-06-11T15:05:03.000Z",
      "num_failures": 0,
      "machine_id": "5bcbf73a-a4cc-2d50-ac39-5493edb9431a",
      "command": "python",
      "arguments": ["main.py", "600", "checkpoints/checkpoint.json", "outputs/sum.txt"],
      "environment": {},
      "max_failures": 3,
      "heartbeat_interval": 30,
      "container_group_id": "26506e01-6356-48ab-8b63-fd4c32cd881f",
      "webhook": null,
      "compression": false,
      "num_heartbeats": 12,
      "sync": {
        "before": [
          {
            "bucket": "long-running-tasks-checkpoints-and-artifacts",
            "prefix": "job-15/checkpoints/",
            "local_path": "checkpoints/",
            "direction": "download"
          }
        ],
        "during": [
          {
            "bucket": "long-running-tasks-checkpoints-and-artifacts",
            "prefix": "job-15/checkpoints/",
            "local_path": "checkpoints/",
            "direction": "upload"
          }
        ],
        "after": [
          {
            "bucket": "long-running-tasks-checkpoints-and-artifacts",
            "prefix": "job-15/outputs/",
            "local_path": "outputs/",
            "direction": "upload"
          }
        ]
      }
    },
    {
      "id": "30af44d4-9c01-44eb-8bcd-6ecf7a63c1f9",
      "user_id": "5b0f6331-fc03-423c-919e-11728c2b97b2",
      "status": "running",
      "created": "2025-06-11T14:59:14.000Z",
      "started": "2025-06-11T14:59:30.000Z",
      "heartbeat": "2025-06-11T15:09:56.000Z",
      "num_failures": 0,
      "machine_id": "60127913-82f0-be50-a4df-1d052b8daf84",
      "command": "python",
      "arguments": ["main.py", "600", "checkpoints/checkpoint.json", "outputs/sum.txt"],
      "environment": {},
      "max_failures": 3,
      "heartbeat_interval": 30,
      "container_group_id": "26506e01-6356-48ab-8b63-fd4c32cd881f",
      "webhook": null,
      "compression": false,
      "num_heartbeats": 19,
      "sync": {
        "before": [
          {
            "bucket": "long-running-tasks-checkpoints-and-artifacts",
            "prefix": "job-56/checkpoints/",
            "local_path": "checkpoints/",
            "direction": "download"
          }
        ],
        "during": [
          {
            "bucket": "long-running-tasks-checkpoints-and-artifacts",
            "prefix": "job-56/checkpoints/",
            "local_path": "checkpoints/",
            "direction": "upload"
          }
        ],
        "after": [
          {
            "bucket": "long-running-tasks-checkpoints-and-artifacts",
            "prefix": "job-56/outputs/",
            "local_path": "outputs/",
            "direction": "upload"
          }
        ]
      }
    }
  ]
}
```

From the R2 console, we can see that our bucket is being filled with checkpoints and results.

<Frame caption="Checkpoints and results in the R2 bucket">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=9099bb501409fe12bc243608f06e4e5a" alt="Checkpoints and results in the R2 bucket" data-og-width="1319" width="1319" data-og-height="1054" height="1054" data-path="container-engine/images/r2-bucket-has-objects.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=fca917d1c54e99f0024ab124f5312a72 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=33700862cbd01bb8c2bae4ce71c9c6c9 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=ca8443a6b6c6ed132359446e5ea3c23c 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=e1751e77b2a6e0c363276500941307d7 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=4a2d26134b14417dab07c3ab57cc68a3 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=881dcd7187190b5a42b55021b7ffe42a 2500w" />
</Frame>

## Autoscaling

Kelpie supports autoscaling based on the number of jobs in the queue. You can enable autoscaling by first adding the
kelpie user (currently [shawn.rushefsky@salad.com](mailto:shawn.rushefsky@salad.com)) to your organization, and then creating an autoscaling rule through
the Kelpie API with the
[Create Scaling Rule Endpoint](https://kelpie.saladexamples.com/docs#/default/post_CreateScalingRule)

```shell  theme={null}
curl -X 'POST' \
  'https://kelpie.saladexamples.com/scaling-rules' \
  -H 'accept: application/json' \
  -H 'Salad-Api-Key: <your-salad-api-key>' \
  -H 'Salad-Organization: <your-salad-organization>' \
  -H 'Salad-Project: <your-salad-project>' \
  -H 'Content-Type: application/json' \
  -d '{
  "container_group_id": "<your-container-group-id>",
  "min_replicas": 0,
  "max_replicas": 100,
  "idle_threshold_seconds": 0
  }'
```

Every 5 minutes, the Kelpie API evaluates the number of jobs in the queue, and scales the number of replicas to be equal
to the number of jobs in the queue, up to the maximum number of replicas specified in the scaling rule. If there are no
jobs in the queue, the API will scale down the number of replicas to the minimum specified in the scaling rule,
including stopping the container group if the minimum is 0.

[Learn more about Kelpie autoscaling](https://github.com/SaladTechnologies/kelpie?tab=readme-ov-file#autoscaling-configuration).

## Conclusion

In this guide, we have covered how to manage long-running tasks on SaladCloud using Kelpie as a job queue, and R2 as
cloud storage. We have built a simple application that simulates work by calculating a sum, and we have set up
checkpoints and output files to be uploaded to R2. We have also covered how to submit jobs to the queue, and how to
deploy the worker to SaladCloud. Finally, we have covered how to enable autoscaling for the worker based on the number
of jobs in the queue. This setup can be used for a wide range of long-running tasks, such as molecular simulations, LoRA
training, and LLM finetuning, and can be easily adapted to your specific needs.
