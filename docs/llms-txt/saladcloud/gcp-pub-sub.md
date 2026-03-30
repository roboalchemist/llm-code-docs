# Source: https://docs.salad.com/container-engine/how-to-guides/job-processing/gcp-pub-sub.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# GCP Pub/Sub and SaladCloud

> Managing Long-Running Tasks on SaladCloud with GCP Pub/Sub

*Last Updated: March 17, 2025*

# Managing Long-Running Tasks on SaladCloud with Google Cloud Pub/Sub

Managing long running tasks, such as molecular simulations, LoRA training, and LLM finetuning, presents unique
challenges on SaladCloud, due primarily to the interruptible nature of nodes. At the core of all solutions to this
problem are a job queue, and progress checkpoints. The job queue is responsible for distributing tasks to workers, and
detecting when a worker has been interrupted. Workloads should save checkpoints of their progress and upload it to cloud
storage, so that they can be resumed from the last checkpoint in the event of an interruption. Workers should also
upload completed artifacts to cloud storage.

<Frame caption="Basic architecture for long-running tasks on SaladCloud">
  <img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=0aecbde9d765a2712eb7293c4e0d2466" alt="Basic Architecture" data-og-width="2719" width="2719" data-og-height="1275" height="1275" data-path="container-engine/images/lrt-basic-arch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=3d0b91baef22a492d5a7c48971b3f95c 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=3c02fb0e88ba714b93aafce5e2c3b864 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=8c04940f12b79accdb53fbbfde12c341 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=a19ee1a0a51acce431a99ab7da564acc 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=c5fc29cc18ef306cd484c4102768d7c7 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=39a8fed8ff7194c233e20d4199d36514 2500w" />
</Frame>

We will be using [Google Cloud Pub/Sub](https://cloud.google.com/pubsub) as our job queue, and
[Cloudflare R2](https://www.cloudflare.com/developer-platform/products/r2/), an S3-compatible object storage service, as
our cloud storage. We prefer R2 to AWS S3 for many SaladCloud workloads, because R2 does not charge for egress data, and
SaladCloud's distributed nodes are not in datacenters, and therefore may incur egress fees from other providers.
Instrumenting your code to use S3-compatible storage will make it easier to switch storage providers in the future if
you choose to do so.

For this guide, we will build an application that slowly calculates a sum for *n* steps, sleeping for 30 seconds between
steps to simulate work. We will set up a job queue and related resources, a storage bucket, a checkpoint saving system,
and review a simple auto-scaling mechanism.

You will need a Google Cloud account, and a Cloudflare account to follow this guide.

## The Job Queue: Google Cloud Pub/Sub

Google Cloud Pub/Sub is a messaging service that allows you to send and receive messages between independent
applications. We will use it to distribute tasks to workers. You can create a new Pub/Sub topic and subscription using
the Google Cloud Console.

### Relevant Limitations

* Pub/Sub messages can be at most 10MB in size. This means that you should not send large payloads in a single message.
  Instead, you should send a reference to the payload in cloud storage.
* Pub/Sub messages are not guaranteed to be delivered in order. This means that you should not rely on the order of
  messages in the queue to determine the order of tasks.
* Pub/Sub is billed primarily based on the amount of throughput you use, in kB. This means there are significant cost
  savings to only including references to large assets, as opposed to encoding them in the message itself.
* Similar to other hyperscaler clouds, permission management can be complex and painful in Google Cloud. Make sure you
  understand the IAM roles and permissions you are granting to your Pub/Sub resources.

### Creating a Topic and Subscription

Navigate to the [GCP Pub/Sub Console](https://console.cloud.google.com/cloudpubsub/schema) and create a new schema
called `job-schema`. This will enable automatic message validation for your topic, which can be useful for ensuring that
your workers are receiving the valid jobs.

Use the following JSON schema, defining a `Job` record with a `job_id` and `steps` field:

```JSON  theme={null}
{
  "type": "record",
  "name": "Job",
  "fields": [
    {
      "name": "job_id",
      "type": "string"
    },
    {
      "name": "steps",
      "type": "int"
    }
  ]
}
```

With this created, navigate to the "Topics" tab, and click "Create Topic". We'll call our topic `Jobs`, and we won't use
the default subscription. Go ahead and select the schema we just created, and use the default google-managed encryption
key.

<Frame caption="Creating a new topic">
  <img src="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-topic.png?fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=dc4d66b5fb633f6a9d8fb12f5dcc77db" alt="Creating a new topic" data-og-width="593" width="593" data-og-height="1012" height="1012" data-path="container-engine/images/gcp-pubsub-create-topic.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-topic.png?w=280&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=36052edb166279a2ceabe13a4fe4dbe5 280w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-topic.png?w=560&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=9ce4e8b99656350b94fb09300c1af2ec 560w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-topic.png?w=840&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=7accb45f980ae1687e21e40176fb065e 840w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-topic.png?w=1100&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=2fb9c62477f4497ec0b4e9d259528f14 1100w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-topic.png?w=1650&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=f2e41e351fe12dddc3b82e53b2e74955 1650w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-topic.png?w=2500&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=c35544adf5ffbcd4a712e60d6d561811 2500w" />
</Frame>

Create a second topic called `deadletter` that we will use for failed jobs. For this one, we do not want the schema, and
we do want to enable message retention.

Next, navigate to the "Subscriptions" tab, and click "Create Subscription". We'll call our subscription `job-workers`,
and assign it to the `jobs` topic. We'll use the "Pull" delivery type, set message retention to the maximum of 31 days,
and set it to "Never expire". We'll also set the "Acknowledgement deadline" to 60 seconds, which means that if a worker
doesn't acknowledge the message, or extend the deadline within 60 seconds, the message will be handed out to a different
worker.

<Frame caption="Creating a new subscription">
  <img src="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-subscription.png?fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=96aed812d9d90899a6a24519567b0543" alt="Creating a new subscription" data-og-width="558" width="558" data-og-height="1016" height="1016" data-path="container-engine/images/gcp-pubsub-create-subscription.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-subscription.png?w=280&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=88d142beab40904eb9a79cdef6f4bfaf 280w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-subscription.png?w=560&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=189aec2bc6b9085489ec8dbcb42fc5a1 560w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-subscription.png?w=840&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=c2362e95d0805fc8c9f20feb440153fa 840w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-subscription.png?w=1100&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=43a8d6f834ade3724535a359c3dd09a8 1100w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-subscription.png?w=1650&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=13c3d2ee5ca8f2801eb292ba56da63c6 1650w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-subscription.png?w=2500&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=b2424fc0bb40b6eb315bb305c4834c7c 2500w" />
</Frame>

We will enable exactly once delivery, to ensure that our long-running, presumably expensive tasks do not get run more
than once. We will also enable dead-lettering, and set the dead-letter topic to the `deadletter` topic we created
earlier. Maximum delivery attempts can be the minimum value of 5. We want failed jobs to be immediately retried.

<Frame caption="Creating a new subscription">
  <img src="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-subscription-2.png?fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=bdcd31efab38f039fa4a8a613bb95a55" alt="Creating a new subscription" data-og-width="592" width="592" data-og-height="787" height="787" data-path="container-engine/images/gcp-pubsub-create-subscription-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-subscription-2.png?w=280&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=78839b05c6428e6f5c1964b16f3edb0b 280w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-subscription-2.png?w=560&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=d1ee041d510eed6a27929c6a1f20100b 560w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-subscription-2.png?w=840&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=72559f6f54a78f8a3042063e6c9c508c 840w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-subscription-2.png?w=1100&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=0967a298ec21a370e0db06f617294f93 1100w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-subscription-2.png?w=1650&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=adf6f91d0aea39f0719d7f68c1d9a6a0 1650w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-create-subscription-2.png?w=2500&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=cf320fe6488392808dc2daf97a1242bb 2500w" />
</Frame>

Once this is created, go ahead and create another subscription called `deadletter`, and attach it to the `deadletter`
topic. This is where you could attach something to process failed messages, although we will not be covering that in
this guide.

Finally, you will need to use the [Service Accounts console](https://console.cloud.google.com/iam-admin/serviceaccounts)
to create an IAM principal with the `Pub/Sub Subscriber` permission set. Create a set of JSON service account keys for
the new principal, and save the file as `keys.json`. Add this file to your `.gitignore` to avoid committing it to your
repository.

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

We're going to use the `boto3` library to interact with R2, and the `google-cloud-pubsub` library to interact with
Google Cloud Pub/Sub. You can install these libraries with `pip install boto3 google-cloud-pubsub`.

First, we need to set up our environment variables. All of the following environment variables will be needed by the
application code.

There are several ways to do this, but what I've done for my development environment is create a file called
`worker.env` in the root of my project, and add the following lines:

```shell  theme={null}
PROJECT_ID=your-gcp-project-id
SUBSCRIPTION_ID=your-pubsub-subscription-id
ACK_DEADLINE_SECONDS=60
R2_AWS_ACCESS_KEY_ID=your-access-key-id
R2_AWS_SECRET_ACCESS_KEY=your-secret-access-key
R2_S3_ENDPOINT_URL=your-s3-endpoint-url
R2_BUCKET_NAME=your-bucket-name
GCP_KEY=B64_ENCODED_GCP_SERVICE_ACCOUNT_KEY
GOOGLE_APPLICATION_CREDENTIALS=/path/to/keys.json
```

To get the `GCP_KEY`, you can run the following command:

```shell  theme={null}
cat keys.json | base64 -w 0
```

It is important to use the `-w 0` flag to ensure that the base64 encoded string is on a single line.

Then, to source this into my environment when I run my code, I run the following command:

```shell  theme={null}
export $(grep -v '^#' worker.env | xargs -d '\n')
```

Make sure `*.env` is in your .gitignore. You don't want to commit your secrets to your repository.

Now, create a file called `main.py` in the root of your project, and add the following code:

```python  theme={null}
import os
import boto3
import json
import time
import threading
from google.cloud import pubsub_v1

# Get the environment variables
r2_aws_region = "auto"
r2_aws_access_key_id = os.getenv('R2_AWS_ACCESS_KEY_ID')
r2_aws_secret_access_key = os.getenv('R2_AWS_SECRET_ACCESS_KEY')
r2_s3_endpoint_url = os.getenv('R2_S3_ENDPOINT_URL')
r2_bucket_name = os.getenv('R2_BUCKET_NAME')

project_id = os.getenv('PROJECT_ID')
subscription_id = os.getenv('SUBSCRIPTION_ID')
ack_deadline_seconds = int(os.getenv('ACK_DEADLINE_SECONDS'))


# Create the R2 client
r2 = boto3.client('s3',
                  aws_access_key_id=r2_aws_access_key_id,
                  aws_secret_access_key=r2_aws_secret_access_key,
                  region_name=r2_aws_region,
                  endpoint_url=r2_s3_endpoint_url)

# Create the Pub/Sub client
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(
    project_id, subscription_id)
```

First, let's look at our simulated workload:

```python  theme={null}
def do_the_actual_work(job: dict, checkpoint: dict, cancel_signal: threading.Event) -> int | None:
    '''
    Do the actual work for the job. This function will simulate work by
    sleeping for 30 seconds and incrementing the step and sum in the
    checkpoint.

    Parameters:
    - job: dict, the job
    - checkpoint: dict, the checkpoint
    '''
    print(f'Starting job {job["job_id"]}', flush=True)
    print(f"Max steps: {job['steps']}", flush=True)
    print(f"Starting step: {checkpoint['step']}", flush=True)
    while checkpoint['step'] < job['steps'] and not cancel_signal.is_set():
        # Simulate work
        print(
            f"Working on job {job['job_id']}, step {checkpoint['step']}", flush=True)
        time.sleep(30)
        if cancel_signal.is_set():
            # If we were interrupted, we need to return None to indicate that
            # the job was interrupted.
            return None
        # Update the checkpoint.
        checkpoint['step'] += 1
        checkpoint['sum'] += checkpoint['step']
        upload_checkpoint(job['job_id'], checkpoint)

    print(f'Job {job["job_id"]} finished')
    return checkpoint['sum']
```

Next, we want some helper functions to interact with R2:

```python  theme={null}
def download_checkpoint(job_id: str) -> dict:
    '''
    Download the checkpoint from S3

    Parameters:
    - job_id: str, the job ID

    Returns:
    - checkpoint: dict, the checkpoint
    '''
    try:
        response = r2.get_object(
            Bucket=r2_bucket_name,
            Key=f'{job_id}/checkpoint.json'
        )
    except r2.exceptions.NoSuchKey:
        return None

    checkpoint = json.loads(response['Body'].read())
    return checkpoint


def upload_checkpoint(job_id: str, checkpoint: dict) -> None:
    '''
    Upload the checkpoint to S3

    Parameters:
    - job_id: str, the job ID
    - checkpoint: dict, the checkpoint
    '''
    r2.put_object(
        Bucket=r2_bucket_name,
        Key=f'{job_id}/checkpoint.json',
        Body=json.dumps(checkpoint)
    )
    print(f'Checkpoint uploaded for job {job_id}', flush=True)


def upload_result(job_id: str, result: int) -> None:
    '''
    Upload the result to S3

    Parameters:
    - job_id: str, the job ID
    - result: int, the result
    '''
    r2.put_object(
        Bucket=r2_bucket_name,
        Key=f'{job_id}/result.txt',
        Body=str(result)
    )
    print(f'Result uploaded for job {job_id}', flush=True)
```

Next, we want a function that will periodically extend the message deadline:

```python  theme={null}
def heartbeat_job(ack_id: str, heartbeat_stop_signal: threading.Event, job_stop_signal: threading.Event) -> None:
    '''
    Send a heartbeat to the GCP subscription

    Parameters:
    - receipt_handle: str, the receipt handle of the message
    - heartbeat_stop_signal: threading.Event, a signal to stop the heartbeat
    - job_stop_signal: threading.Event, a signal to stop the main job
    '''
    while not heartbeat_stop_signal.is_set():
        try:
            subscriber.modify_ack_deadline(
                subscription=subscription_path,
                ack_ids=[ack_id],
                ack_deadline_seconds=ack_deadline_seconds
            )
            time.sleep(ack_deadline_seconds // 2)
        except Exception as e:
            print(f"Error in heartbeat: {str(e)}", flush=True)
            job_stop_signal.set()
            break
```

We also will use some helper functions to interact with Pub/Sub:

```python  theme={null}
def ack_job(ack_id: str) -> None:
    '''
    Acknowledge the job

    Parameters:
    - ack_id: str, the ack ID
    '''
    subscriber.acknowledge(subscription=subscription_path, ack_ids=[ack_id])


def nack_job(ack_id: str) -> None:
    '''
    Reject the job

    Parameters:
    - ack_id: str, the ack ID
    '''
    subscriber.modify_ack_deadline(
        subscription=subscription_path,
        ack_ids=[ack_id],
        ack_deadline_seconds=0
    )
```

Now, we need a function that ties everything together:

```python  theme={null}
def process_job(job, ack_id):
    print(f"Received job {job['job_id']}", flush=True)

    # Start the heartbeat thread to keep the job alive
    heartbeat_stop_signal = threading.Event()
    job_stop_signal = threading.Event()
    heartbeat_thread = threading.Thread(
        target=heartbeat_job, args=(
            ack_id, heartbeat_stop_signal, job_stop_signal))
    heartbeat_thread.start()

    # If there's a checkpoint, we want to use it, but if not, we need to
    # initialize our state.
    checkpoint = download_checkpoint(job['job_id'])
    if checkpoint is None:
        print('No checkpoint found. Initializing state.', flush=True)
        checkpoint = {'step': 0, 'sum': 0}
    else:
        print(
            f'Found checkpoint, resuming from step {checkpoint["step"]}', flush=True)

    # Some jobs may have a validation step. For instance, dreambooth training may have a step
    # that verifies if all inputs have faces. If the validation fails, we should nack the job.
    if not validate_job(job):
        print(f"Job {job['job_id']} failed validation")
        heartbeat_stop_signal.set()
        nack_job(ack_id)
        return

    # Now we can do the actual work
    try:
        result = do_the_actual_work(job, checkpoint, job_stop_signal)
    except Exception as e:
        print(f"Error in job {job['job_id']}: {str(e)}", flush=True)
        heartbeat_stop_signal.set()
        nack_job(ack_id)
        return

    if result is None:
        # Heartbeat failed, so we need to nack the job
        print(f"Heartbeat for {job['job_id']} failed", flush=True)
        heartbeat_stop_signal.set()
        nack_job(ack_id)
        return

    # Upload the result and ack the message
    upload_result(job['job_id'], result)
    heartbeat_stop_signal.set()
    ack_job(ack_id)
    heartbeat_thread.join()
```

Finally, we need a function to start the worker:

```python  theme={null}
if __name__ == '__main__':
    print("Polling for messages", flush=True)
    while True:
        response = subscriber.pull(
            subscription=subscription_path, max_messages=1, timeout=30)
        if not response or len(response.received_messages) == 0:
            print("No messages received, sleeping for 10s", flush=True)
            time.sleep(10)
            continue

        message = response.received_messages[0]
        ack_id = message.ack_id
        body = json.loads(message.message.data.decode('utf-8'))
        process_job(body, ack_id)
```

### Completed Example

```python  theme={null}
import os
import boto3
import json
import time
import threading
from google.cloud import pubsub_v1

# Get the environment variables
r2_aws_region = "auto"
r2_aws_access_key_id = os.getenv('R2_AWS_ACCESS_KEY_ID')
r2_aws_secret_access_key = os.getenv('R2_AWS_SECRET_ACCESS_KEY')
r2_s3_endpoint_url = os.getenv('R2_S3_ENDPOINT_URL')
r2_bucket_name = os.getenv('R2_BUCKET_NAME')

project_id = os.getenv('PROJECT_ID')
subscription_id = os.getenv('SUBSCRIPTION_ID')
ack_deadline_seconds = int(os.getenv('ACK_DEADLINE_SECONDS'))


# Create the R2 client
r2 = boto3.client('s3',
                  aws_access_key_id=r2_aws_access_key_id,
                  aws_secret_access_key=r2_aws_secret_access_key,
                  region_name=r2_aws_region,
                  endpoint_url=r2_s3_endpoint_url)

# Create the Pub/Sub client
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(
    project_id, subscription_id)


def download_checkpoint(job_id: str) -> dict:
    '''
    Download the checkpoint from S3

    Parameters:
    - job_id: str, the job ID

    Returns:
    - checkpoint: dict, the checkpoint
    '''
    try:
        response = r2.get_object(
            Bucket=r2_bucket_name,
            Key=f'{job_id}/checkpoint.json'
        )
    except r2.exceptions.NoSuchKey:
        return None

    checkpoint = json.loads(response['Body'].read())
    return checkpoint


def upload_checkpoint(job_id: str, checkpoint: dict) -> None:
    '''
    Upload the checkpoint to S3

    Parameters:
    - job_id: str, the job ID
    - checkpoint: dict, the checkpoint
    '''
    r2.put_object(
        Bucket=r2_bucket_name,
        Key=f'{job_id}/checkpoint.json',
        Body=json.dumps(checkpoint)
    )
    print(f'Checkpoint uploaded for job {job_id}', flush=True)


def validate_job(job: dict) -> bool:
    '''
    Validate the job

    Parameters:
    - job: dict, the job

    Returns:
    - bool, whether the job is valid
    '''
    # This is a very simple function for our very simple application.
    # You should replace this with your actual validation logic.
    return 'job_id' in job and 'steps' in job


def upload_result(job_id: str, result: int) -> None:
    '''
    Upload the result to S3

    Parameters:
    - job_id: str, the job ID
    - result: int, the result
    '''
    r2.put_object(
        Bucket=r2_bucket_name,
        Key=f'{job_id}/result.txt',
        Body=str(result)
    )
    print(f'Result uploaded for job {job_id}', flush=True)


def do_the_actual_work(job: dict, checkpoint: dict, cancel_signal: threading.Event) -> int | None:
    '''
    Do the actual work for the job. This function will simulate work by
    sleeping for 30 seconds and incrementing the step and sum in the
    checkpoint.

    Parameters:
    - job: dict, the job
    - checkpoint: dict, the checkpoint
    '''
    print(f'Starting job {job["job_id"]}', flush=True)
    print(f"Max steps: {job['steps']}", flush=True)
    print(f"Starting step: {checkpoint['step']}", flush=True)
    while checkpoint['step'] < job['steps'] and not cancel_signal.is_set():
        # Simulate work
        print(
            f"Working on job {job['job_id']}, step {checkpoint['step']}", flush=True)
        time.sleep(30)
        if cancel_signal.is_set():
            # If we were interrupted, we need to return None to indicate that
            # the job was interrupted.
            return None
        # Update the checkpoint.
        checkpoint['step'] += 1
        checkpoint['sum'] += checkpoint['step']
        upload_checkpoint(job['job_id'], checkpoint)

    print(f'Job {job["job_id"]} finished')
    return checkpoint['sum']


def heartbeat_job(ack_id: str, heartbeat_stop_signal: threading.Event, job_stop_signal: threading.Event) -> None:
    '''
    Send a heartbeat to the GCP subscription

    Parameters:
    - receipt_handle: str, the receipt handle of the message
    - heartbeat_stop_signal: threading.Event, a signal to stop the heartbeat
    - job_stop_signal: threading.Event, a signal to stop the main job
    '''
    while not heartbeat_stop_signal.is_set():
        try:
            subscriber.modify_ack_deadline(
                subscription=subscription_path,
                ack_ids=[ack_id],
                ack_deadline_seconds=ack_deadline_seconds
            )
            time.sleep(ack_deadline_seconds // 2)
        except Exception as e:
            print(f"Error in heartbeat: {str(e)}", flush=True)
            job_stop_signal.set()
            break


def ack_job(ack_id: str) -> None:
    '''
    Acknowledge the job

    Parameters:
    - ack_id: str, the ack ID
    '''
    subscriber.acknowledge(subscription=subscription_path, ack_ids=[ack_id])


def nack_job(ack_id: str) -> None:
    '''
    Reject the job

    Parameters:
    - ack_id: str, the ack ID
    '''
    subscriber.modify_ack_deadline(
        subscription=subscription_path,
        ack_ids=[ack_id],
        ack_deadline_seconds=0
    )


def process_job(job, ack_id):
    print(f"Received job {job['job_id']}", flush=True)

    # Start the heartbeat thread to keep the job alive
    heartbeat_stop_signal = threading.Event()
    job_stop_signal = threading.Event()
    heartbeat_thread = threading.Thread(
        target=heartbeat_job, args=(
            ack_id, heartbeat_stop_signal, job_stop_signal))
    heartbeat_thread.start()

    # If there's a checkpoint, we want to use it, but if not, we need to
    # initialize our state.
    checkpoint = download_checkpoint(job['job_id'])
    if checkpoint is None:
        print('No checkpoint found. Initializing state.', flush=True)
        checkpoint = {'step': 0, 'sum': 0}
    else:
        print(
            f'Found checkpoint, resuming from step {checkpoint["step"]}', flush=True)

    # Some jobs may have a validation step. For instance, dreambooth training may have a step
    # that verifies if all inputs have faces. If the validation fails, we should nack the job.
    if not validate_job(job):
        print(f"Job {job['job_id']} failed validation")
        heartbeat_stop_signal.set()
        nack_job(ack_id)
        return

    # Now we can do the actual work
    try:
        result = do_the_actual_work(job, checkpoint, job_stop_signal)
    except Exception as e:
        print(f"Error in job {job['job_id']}: {str(e)}", flush=True)
        heartbeat_stop_signal.set()
        nack_job(ack_id)
        return

    if result is None:
        # Heartbeat failed, so we need to nack the job
        print(f"Heartbeat for {job['job_id']} failed", flush=True)
        heartbeat_stop_signal.set()
        nack_job(ack_id)
        return

    # Upload the result and ack the message
    upload_result(job['job_id'], result)
    heartbeat_stop_signal.set()
    ack_job(ack_id)
    heartbeat_thread.join()


if __name__ == '__main__':
    print("Polling for messages", flush=True)
    while True:
        response = subscriber.pull(
            subscription=subscription_path, max_messages=1, timeout=30)
        if not response or len(response.received_messages) == 0:
            print("No messages received, sleeping for 10s", flush=True)
            time.sleep(10)
            continue

        message = response.received_messages[0]
        ack_id = message.ack_id
        body = json.loads(message.message.data.decode('utf-8'))
        process_job(body, ack_id)
```

## Submitting Jobs To The Queue

Now we need to populate the queue with jobs. First, we'll define some environment variables in a new file
`submitter.env`.

```shell  theme={null}
PROJECT_ID=your-gcp-project-id
TOPIC_ID=jobs
GOOGLE_APPLICATION_CREDENTIALS=/path/to/keys.json
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
import os
import json
import csv
from google.cloud import pubsub_v1

project_id = os.getenv('PROJECT_ID')
topic_id = os.getenv('TOPIC_ID')

publisher = pubsub_v1.PublisherClient(
    batch_settings=pubsub_v1.types.BatchSettings(max_messages=100))
topic_path = publisher.topic_path(project_id, topic_id)

if __name__ == '__main__':
    with open("data.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["steps"] = int(row["steps"])
            data = bytes(json.dumps(row), 'utf-8')
            publisher.publish(topic_path, data=data)
```

### Running the Job Submitter

To run the job submitter, you can use the following command:

```shell  theme={null}
python submitter.py
```

## Containerize the Worker Application

Now that we have our worker application and our job submitter, we can package our worker in a docker container, and run
it on a SaladCloud Container Group.

First, let's make sure our dependencies are documented in `requirements.txt`.

```shell  theme={null}
boto3
google-cloud-pubsub
```

Now, we're going to use create a launch script called `launch.sh` that will decode our base64 encoded GCP service
account key, and then run our worker application.

```shell  theme={null}
#! /usr/bin/env bash

# GCP_KEY is the base64 encoded service account key, which is used to authenticate with GCP. We want to write it
# to a file so that we can use it to authenticate with GCP.
echo $GCP_KEY | base64 -d > $GOOGLE_APPLICATION_CREDENTIALS

# Run the worker
python main.py
```

Now, create a new file called `Dockerfile`. Our application is simple, so a basic python base image should be fine.

```dockerfile  theme={null}
FROM python:3.10.12-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
COPY launch.sh .
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/credentials.json"

CMD ["./launch.sh"]
```

Now, build the docker image, and use a tag that makes sense for you.

```shell  theme={null}
docker build -t saladtechnologies/lrt-worker-examples:gcp-pub-sub .
```

Now, we can test it locally to make sure it works, before we deploy it to SaladCloud.

```shell  theme={null}
docker run -it --rm  --env-file worker.env saladtechnologies/lrt-worker-examples:gcp-pub-sub
```

You should see it start up and begin processing a job. Once this is working, you can go ahead and terminate the
container with `Ctrl+C`.

Now, we can push the image to Docker Hub.

```shell  theme={null}
docker push saladtechnologies/lrt-worker-examples:gcp-pub-sub
```

## Deploying the Worker to SaladCloud

To deploy our worker to SaladCloud, we need to create a new Container Group. This can be done via the API, SDKs, or the
Portal. We're going to use the Portal.

We're going to create a new Container Group, and we're going to use the image we just pushed to Docker Hub. We're going
to request 100 replicas (the max via the portal), and we're going to set all of our environment variables from
`worker.env`.

<Frame caption="Creating a new container group">
  <img src="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-1.png?fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=3ce505894e3b745bef70fbdd166fab24" alt="Creating a new container group" data-og-width="694" width="694" data-og-height="772" height="772" data-path="container-engine/images/gcp-pubsub-cg-create-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-1.png?w=280&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=b30cb9b75ace4837146d3b7d5478d51a 280w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-1.png?w=560&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=b38ae6eb9abeddc4485ca7f0612a362a 560w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-1.png?w=840&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=26f6b1231236a9da25d6bcffc0d6e7f4 840w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-1.png?w=1100&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=35e9ff9648d3da88cc314d515eb44291 1100w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-1.png?w=1650&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=9cc9808193181b79552113c51a8a61bc 1650w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-1.png?w=2500&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=a5c7eaf17740968206286177c7826a6a 2500w" />
</Frame>

Our application is extremely simple, so we're going to only request 1 vCPU, 1 GB of RAM, and no GPU. Your hardware
requirements are likely significantly higher than this.

<Frame caption="Setting the hardware requirements">
  <img src="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-2.png?fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=6a633b6239b309b00ed9215d381d67c8" alt="Setting the hardware requirements" data-og-width="686" width="686" data-og-height="1101" height="1101" data-path="container-engine/images/gcp-pubsub-cg-create-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-2.png?w=280&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=695b583cbe0135d65048e45defbf793e 280w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-2.png?w=560&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=b187508088fa9a89eef6383cbf6645bd 560w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-2.png?w=840&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=aec426eac6989712aea900c42616187f 840w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-2.png?w=1100&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=d04dfe4a0909ff4fff388145a60df9ec 1100w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-2.png?w=1650&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=6e3a0dbe594391fdda2d95211b762732 1650w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-2.png?w=2500&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=a61cf70e8319bf954b1d510b16aeaaf3 2500w" />
</Frame>

All CPU-only jobs are prioritized as "Batch" (the lowest tier), and we don't need any additional storage for this
particular application.

<Frame caption="Setting the job priority and storage requirements">
  <img src="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-3.png?fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=9dbf57e82da11aee3f14b8d36bfa23fc" alt="Setting the job priority and storage requirements" data-og-width="664" width="664" data-og-height="576" height="576" data-path="container-engine/images/gcp-pubsub-cg-create-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-3.png?w=280&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=20b2a67b8343d6e52766c315c0f133db 280w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-3.png?w=560&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=f7675dd1d712168261b5a0e204b93153 560w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-3.png?w=840&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=3f663d3a87d69bd9b5c26bfc78ccaa69 840w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-3.png?w=1100&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=67db143db412bba93e80ddc1a026e83b 1100w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-3.png?w=1650&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=aa02dbebe68a19a17b9c0aad75436740 1650w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-create-3.png?w=2500&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=45f6173fff385d4d4acea7d33946f183 2500w" />
</Frame>

We do not need the container gateway, as our application pulls its work from a queue. We also do not need health probes,
as those are primarily for services accessed via Container Gateway. Go ahead and hit deploy, and you'll be taken to the
container group page, where you can see its status.

<Frame caption="Deploying the container group">
  <img src="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-deploying.png?fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=98d558da88f8a04b3eec62489e858d57" alt="Deploying the container group" data-og-width="1214" width="1214" data-og-height="1018" height="1018" data-path="container-engine/images/gcp-pubsub-cg-deploying.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-deploying.png?w=280&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=c3dde9689cc36134b9b5b185fa44cba2 280w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-deploying.png?w=560&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=a0f1520beba5f2f44a1a4976467ffc90 560w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-deploying.png?w=840&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=3499d6f47fa6949997505ce6062c4b61 840w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-deploying.png?w=1100&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=b0d23c367882684f7839c8669caee658 1100w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-deploying.png?w=1650&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=f8e7a4438dbf86a2fe538ec986256436 1650w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-deploying.png?w=2500&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=ffdbe5c5b96f1e1b47a6dab664359524 2500w" />
</Frame>

After a few minutes, instances should start to become "Running".

<Frame caption="Container group running">
  <img src="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-running.png?fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=a255930ffeec9dc4882aeea538fc51fb" alt="Container group running" data-og-width="1160" width="1160" data-og-height="914" height="914" data-path="container-engine/images/gcp-pubsub-cg-running.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-running.png?w=280&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=6d054fe302cc693f4b3fe4ed95e3bb5b 280w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-running.png?w=560&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=c0f2d7823766174a3fba9d56165037e9 560w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-running.png?w=840&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=bc5536724e93f1721cf31e01f5b8ef5e 840w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-running.png?w=1100&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=6614f312867868d6927073d54bc11167 1100w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-running.png?w=1650&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=f0d34fdc813402c54c830fa3ca060a01 1650w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/gcp-pubsub-cg-running.png?w=2500&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=ee31d6481d410d560941be734d74609d 2500w" />
</Frame>

## Validating That It Works

Now that our cluster is up and running, we can go to the Subscription console, and look at the "metrics" tab to verify
there is activity on the subscription.

<Frame caption="Active messages in the subscription">
  <img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/gcp-pubsub-subscription-active.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=223ea81d78a169719772b591b195af7b" alt="Active messages in the subscription" data-og-width="1232" width="1232" data-og-height="913" height="913" data-path="container-engine/images/gcp-pubsub-subscription-active.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/gcp-pubsub-subscription-active.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=637aa5142f085cbeaf22740f176351e5 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/gcp-pubsub-subscription-active.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=de9807a63037f520fe85627e2d09614e 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/gcp-pubsub-subscription-active.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=651bed3a62dbbea6c5e88640ebd7acf0 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/gcp-pubsub-subscription-active.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=1306916cf71d2426f347f0353ab00977 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/gcp-pubsub-subscription-active.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=1bb2e580bce20aed699568bfc52bb705 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/gcp-pubsub-subscription-active.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=56fb68cda5997cabd2787448c356005a 2500w" />
</Frame>

From the R2 console, we can see that our bucket is being filled with checkpoints and results.

<Frame caption="Checkpoints and results in the R2 bucket">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=9099bb501409fe12bc243608f06e4e5a" alt="Checkpoints and results in the R2 bucket" data-og-width="1319" width="1319" data-og-height="1054" height="1054" data-path="container-engine/images/r2-bucket-has-objects.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=fca917d1c54e99f0024ab124f5312a72 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=33700862cbd01bb8c2bae4ce71c9c6c9 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=ca8443a6b6c6ed132359446e5ea3c23c 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=e1751e77b2a6e0c363276500941307d7 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=4a2d26134b14417dab07c3ab57cc68a3 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=881dcd7187190b5a42b55021b7ffe42a 2500w" />
</Frame>

## Autoscaling

Now that we have our worker running, we can set up some simple autoscaling to automatically scale the number of replicas
up and down based on the number of messages in the queue.

There are many ways to implement autoscaling, but for simplicity, we recommend creating a scheduled task that runs every
5 minutes, and sets the number of replicas to be equal to the number of messages in the queue, limited to 250 replicas
(the maximum in the API). To implement this, you can use a serverless function, such as Cloudflare workers, or GCP Cloud
Functions

Here is the outline of a python implementation that you can modify to suit your needs.

```python  theme={null}
# This is our ideal number of replicas
total_messages = num_waiting_messages + num_messages_in_flight

# We need to constrain this number by our min and max.
desired_replicas = min(max(min_replicas, total_messages), max_replicas)

container_group = get_container_group()
current_replicas = container_group["replicas"]
print(
    f"Current replicas: {current_replicas}, Desired replicas: {desired_replicas}")

# always one of pending, running, stopped, failed, deploying
current_state = container_group["current_state"]["status"]
print(f"Current state: {current_state}")

if current_state == "stopped" and desired_replicas > 0:
    start_container_group()

if current_state == "running" and desired_replicas == 0:
    stop_container_group()

if desired_replicas != current_replicas:
    set_replicas(desired_replicas)
```

From the Salad API, you will need the following endpoints:

* [Get Container Group](/reference/saladcloud-api/container-groups/get-container-group)
* [Start Container Group](/reference/saladcloud-api/container-groups/start-container-group)
* [Stop Container Group](/reference/saladcloud-api/container-groups/stop-container-group)
* [Set Replicas](/reference/saladcloud-api/container-groups/update-container-group)

## Conclusion

In this guide, we've shown you how to set up a simple long-running task worker on SaladCloud using Google Cloud Pub/Sub
as a job queue, and R2 as a storage backend. We've also shown you how to deploy the worker to SaladCloud, and how to
implement autoscaling based on the number of messages in the queue.
