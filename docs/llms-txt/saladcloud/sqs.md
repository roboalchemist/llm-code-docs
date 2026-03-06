# Source: https://docs.salad.com/container-engine/how-to-guides/job-processing/sqs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SQS and SaladCloud

> Managing Long-Running Tasks on SaladCloud with SQS

*Last Updated: February 25, 2025*

# Managing Long-Running Tasks on SaladCloud with SQS

Managing long running tasks, such as molecular simulations, LoRA training, and LLM finetuning, presents unique
challenges on SaladCloud, due primarily to the interruptible nature of nodes. At the core of all solutions to this
problem are a job queue, and progress checkpoints. The job queue is responsible for distributing tasks to workers, and
detecting when a worker has been interrupted. Workloads should save checkpoints of their progress and upload it to cloud
storage, so that they can be resumed from the last checkpoint in the event of an interruption. Workers should also
upload completed artifacts to cloud storage.

<Frame caption="Basic architecture for long-running tasks on SaladCloud">
  <img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=0aecbde9d765a2712eb7293c4e0d2466" alt="Basic Architecture" data-og-width="2719" width="2719" data-og-height="1275" height="1275" data-path="container-engine/images/lrt-basic-arch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=3d0b91baef22a492d5a7c48971b3f95c 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=3c02fb0e88ba714b93aafce5e2c3b864 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=8c04940f12b79accdb53fbbfde12c341 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=a19ee1a0a51acce431a99ab7da564acc 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=c5fc29cc18ef306cd484c4102768d7c7 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=39a8fed8ff7194c233e20d4199d36514 2500w" />
</Frame>

We will be using [Amazon SQS](https://aws.amazon.com/sqs/) as our job queue, and
[Cloudflare R2](https://www.cloudflare.com/developer-platform/products/r2/), an S3-compatible object storage service, as
our cloud storage. We prefer R2 to AWS S3 for many SaladCloud workloads, because R2 does not charge for egress data, and
SaladCloud's distributed nodes are not in datacenters, and therefore may incur egress fees from other providers.
Instrumenting your code to use S3-compatible storage will make it easier to switch storage providers in the future if
you choose to do so.

For this guide, we will build an application that slowly calculates a sum for *n* steps, sleeping for 30 seconds between
steps to simulate work. We will set up a job queue and related resources, a storage bucket, a checkpoint saving system,
and a simple auto-scaling mechanism.

You will need an AWS account, and a Cloudflare account to follow this guide.

## IAM: Identity and Access Management

IAM is the AWS system for managing users, roles, and permissions. We will need to create two IAM users: one for us, the
user submitting the jobs, and one for the workers. The user submitting the jobs will need to be able to submit jobs to
the queue, and the workers will need to be able to read and delete jobs from the queue. To get started, navigate to the
[IAM console](https://console.aws.amazon.com/iam/), and select "Users" from the left-hand menu. Click "Create User".

<Frame caption="The IAM Users Console">
  <img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-users-console.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=32be6f236abf85882f4bc1ef5cf9da5e" alt="The IAM Console" data-og-width="1883" width="1883" data-og-height="463" height="463" data-path="container-engine/images/iam-users-console.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-users-console.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=551a134884717d64525fde368d18b2b3 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-users-console.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=58ce6955555c8d29fda111994b21934a 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-users-console.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=cab16d6582b7a813c300cf5f1a03294c 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-users-console.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=b432a29a263ce8c697c24b138391b5c3 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-users-console.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=b5261388ac19183dc90aa954018931bd 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-users-console.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=d03e840a216b4133e8e72bffbb08f847 2500w" />
</Frame>

We're going to name our user `job-submitter`. It does not need console access.

<Frame caption="Creating the job-submitter user">
  <img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st1.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=8cd4ce30b5d354e3884d0c90fcb2a24e" alt="Creating the job-submitter user" data-og-width="1586" width="1586" data-og-height="459" height="459" data-path="container-engine/images/iam-submitter-st1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st1.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=f8ab7c09f002ffa2aacb13b2485c6cbb 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st1.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=9b881901d07b6b3fdd908eddd6ffc34a 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st1.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=daec89a0f321f8163a1115f496c1c8a6 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st1.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=538ef8f3cfedc77c476346184d831a05 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st1.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=53d87b97c5dba375a2fc56396822dad1 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st1.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=84bd06abf42f8c54732c95b91f8a4f44 2500w" />
</Frame>

On the next screen, we're going to grant no permissions the the user. We will be using a resource-based policy later to
grant the user access to the queue.

<Frame caption="Granting no permissions to the job-submitter user">
  <img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st2.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=2f4589996a778f129a35923b8e4f66d8" alt="Granting no permissions to the job-submitter user" data-og-width="1579" width="1579" data-og-height="532" height="532" data-path="container-engine/images/iam-submitter-st2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st2.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=14dc057c1c0379e28df06e3f3d119ae5 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st2.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=653aff94efa0409f8c2801c0b92fd9cb 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st2.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=84cfdaeba352a8ae8ef59d026cde7218 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st2.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=6dfd26e5ed28f9cad65c9de33eb40e4f 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st2.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=c790446c14e0398f3cac77003039007a 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st2.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=c7cce31b632dc4b8137241ef4d6dd553 2500w" />
</Frame>

Finally, give the user any tags that will make it easier to find and organize later. We're going to give it a tag of
"project: sqs-demo".

<Frame caption="Tagging the job-submitter user">
  <img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st3.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=8cf9738cd2c96b6fe7aac38d9f8e1bc2" alt="Tagging the job-submitter user" data-og-width="1585" width="1585" data-og-height="765" height="765" data-path="container-engine/images/iam-submitter-st3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st3.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=34e3b1d7ef5f3522c82eb0be58d309cd 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st3.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=10913866e283e29f29915b8ab36657b2 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st3.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=39e5fdb1f6b20010d97d048470320530 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st3.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=7cedfe027afeac46bafc7183b445cb64 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st3.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=0c6b5bbaec490282ce470299910dbc68 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-submitter-st3.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=080531c4f40bccb72fbe05ce80699ea7 2500w" />
</Frame>

Repeat that process to create a user called `job-worker`. Once you're done, leave this tab open, because we will need
the resource IDs (ARNs) of the users later.

We need to create a set of access keys for both IAM users in AWS. Navigate back to your IAM console tab, and click on
the job-worker user. Select "Create access key", and save the access keys and secret keys somewhere safe. Make sure to
keep track of which set of keys belongs to which user, since they have different permissions.

<Frame caption="Creating an access key for the job-worker user">
  <img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-worker-create-key.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=c697820f30841ceaaa71abab627ac0f9" alt="Creating an access key for the job-worker user" data-og-width="1278" width="1278" data-og-height="209" height="209" data-path="container-engine/images/iam-worker-create-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-worker-create-key.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=8fd65b693c4b4624ceb5a9238f544292 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-worker-create-key.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=ce103320b0c03ae9fb8032c9f83e96b7 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-worker-create-key.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=0e0bf7bed803d6205123fc13c5c060f2 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-worker-create-key.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=d7e51adb63f2c06c440bc2a57f833b6b 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-worker-create-key.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=a701a417593227ed26225c617ec96268 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/iam-worker-create-key.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=9b5344383165c139b9e8f6e9701e68ca 2500w" />
</Frame>

## The Job Queue: SQS

Simple Queue Service, or SQS, is a fully managed serverless queue solution from AWS. It is a great choice for managing
long-running tasks (but \< 12 hours) on SaladCloud because it is highly available, scalable, and requires no ongoing
maintenance. For tasks longer than 12 hours, the job will be processed no more than 12 hours at a time by any particular
worker, and the job must be completed with 14 days of being submitted. SQS is not free, and while the pricing may seem
low, the cost can add up quickly if you are not careful. That said, if you are processing less than a few million jobs
per month, the cost should be negligible.

### Relevant Limitations

* Maximum message size of 256KB. This means if our job has much in the way of input data, we will need to store that
  input data in cloud storage, and only include references to it in the job definition.
* Maximum message retention of 14 days. This means if jobs sit in the queue for longer than 14 days, they will be
  automatically deleted.
* Maximum message visibility timeout of 12 hours. This means that if a worker does not delete a message from the queue
  within 12 hours of receiving it, the message will be made available to other workers. For some particularly long
  workloads, this presents challenges. For others, it is a non-issue.
* There is no built-in mechanism to look up what jobs are in the queue, or what jobs have finished. This means that if
  you need to know the status of a job, you will need to store that information somewhere in the cloud (database, bucket
  storage, etc), and update it as the job progresses.
* There is no built-in mechanism for canceling a job once submitted. If that is something you need, you would need to
  build an additional mechanism for it, and have your worker check for a cancel signal periodically.
* AWS is pretty complicated if you are unfamiliar with it (and even if you are!).

### Creating SQS Queues

To create an SQS queue, navigate to the [SQS console](https://console.aws.amazon.com/sqs/), and click "Create queue".

<Frame caption="The SQS Console">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-console.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=19c97d2a5158622d05e21e7dbe6dc77b" alt="The SQS Console" data-og-width="1399" width="1399" data-og-height="343" height="343" data-path="container-engine/images/sqs-console.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-console.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=39fb5681be536a168add27f07e1ec378 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-console.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=161c2bcc5045c245b070ee6aa55dae4e 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-console.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=cf6810f09e1dcdc1730e3a11208e3f00 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-console.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=15cb4ff319e53318bd79f2a6910418c2 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-console.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=c9da2f281983ed9f8a8c4085a6c8f6c5 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-console.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=5eccb1752f810b002b89ba4bc99253b3 2500w" />
</Frame>

<Frame caption="Creating a new FIFO queue">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-create-queue.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=027972e8bebb9be4d8bc4139f25cc303" alt="Creating a new FIFO queue" data-og-width="1224" width="1224" data-og-height="1151" height="1151" data-path="container-engine/images/sqs-create-queue.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-create-queue.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=7515f305c7f6fe946b44c3063befaf0a 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-create-queue.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=5351f803598ed2f765ce35598483c99e 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-create-queue.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=d873876491039da239117f4f66e0e18f 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-create-queue.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=9e299f3cdbd62cfc33b3b309a1f19cea 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-create-queue.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=5fb361158f97116e29a4f46d78de4a6b 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-create-queue.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=62bc02b6c63c2b2b1ba80600fd70a18b 2500w" />
</Frame>

You may want to choose a better name than I have, but for the purposes of this guide, we'll call our queue
`my-job-queue.fifo`. The `.fifo` suffix indicates that this is a FIFO queue.

* FIFO queues are recommended for long-running tasks, because the cost of processing a job is often relatively high, and
  FIFO queues ensure *exactly-once* processing of each job. In non-FIFO queues, throughput is higher and the cost of
  jobs potentially being delivered more than once.
* Set the visibility timeout to 60 seconds. You might think, don't we want it to be way longer than that? The answer is
  no, because we want the job queue to hand the job out to a new worker as soon as possible if a worker gets
  interrupted. In our application, we will programmatically extend the visibility timeout while the job is running. The
  60 second value then becomes the maximum amount of time a worker can be out of communication before a job is handed
  out again.
* Set the message retention period to 14 days. This is the maximum value, and we want to keep jobs around as long as
  possible in case we need to reprocess them, or in case our we have a scenario with dramatically more jobs than
  workers.
* Set the default message delay to 0 seconds. This is the amount of time a message will sit in the queue before it is
  available to be picked up by a worker. We want this to be as low as possible, because we want workers to be able to
  pick up jobs as soon as they are available.
* Set maximum message size to 256KB. This is the maximum size of a message in the queue. If your job input is larger
  than this, you will need to store the job inputs in cloud storage, and only include a reference to the job in the
  message. An example would be dreambooth training, where many images are needed as an input to the job.
* Set the "Receive message wait time" to 20 seconds. In order to minimize the number of api requests (which are billed),
  we want workers to wait up to 20 seconds on an open connection for a job to become available. In times of high
  throughput, this setting doesn't really matter because workers will always have a wait time of 0 seconds. however, in
  times of low job volume, this setting can lead to significant savings in billed api requests.
* Leave content-based deduplication disabled. We will be using the more lightweight `MessageDeduplicationId` field to
  ensure exactly-once processing of jobs, and assigning GUIDs to jobs in our application code.
* We want the deduplication scope to be queue-wide, so that we can ensure exactly-once processing of jobs across all
  workers.
* For "FIFO throughput limit", we want to set this to "Per queue". Selecting "Per message group ID" enables
  high-throughput FIFO queues, which are excessive for out application. If you are processing tens of thousands of
  simultaneous jobs, you may want to enable high-throughput FIFO queues, but for most applications, this is unnecessary.

More info on [limitations](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-fifo.html)
and [pricing](https://aws.amazon.com/sqs/pricing/) can be found on the AWS website and in the SQS documentation.

Leave encryption enabled. We will be using the default KMS key, which is managed by AWS, but you can also use your own
KMS key if you have one.

We're going to use a basic access policy, which allows the job-submitter user to send messages to the queue, and the
job-worker user to receive and delete messages from the queue.

<Frame caption="Assigning permissions to the users we previously created.">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-assign-permissions.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=cc1f6a5a7318799c539b2d2b92ffcf24" alt="Assigning permissions to the users" data-og-width="1165" width="1165" data-og-height="620" height="620" data-path="container-engine/images/sqs-assign-permissions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-assign-permissions.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=0a9d9305bf58fce110dcb4faacfc94d1 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-assign-permissions.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=cce7cd23d58922ae89d1f10d3fe39b8a 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-assign-permissions.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=8d767baf1ea0fcdcee00d5bf44de4c70 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-assign-permissions.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=121286f163ed77ca514029b3b4cdfa62 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-assign-permissions.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=d0658010285c182259ec483b9537dd2e 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-assign-permissions.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=73b89f9b56e55ddc87d3bd864e7ce325 2500w" />
</Frame>

For now, we're not going to enable "Redrive allow policy,"" or "Dead-letter queue", because we haven't created our dead
letter queue yet. Once we have, we will come back and enable this feature.

<Frame caption="Skipping the dead-letter queue for now">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-no-dlq-yet.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ae35c69362bf2eea26f4416d9434d1a3" alt="Skipping the dead-letter queue for now" data-og-width="1170" width="1170" data-og-height="371" height="371" data-path="container-engine/images/sqs-no-dlq-yet.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-no-dlq-yet.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=71c76bfb86e3ca8c375b4b42009008d6 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-no-dlq-yet.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=7b7a9668393eedd22ad954e114e553d2 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-no-dlq-yet.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=0f2d074f7d0a0d17a99aede5b9091a81 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-no-dlq-yet.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=891b554ea9d47f90d2bbd2b70986aaa3 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-no-dlq-yet.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=8857106ca2446a5d9420a1ad70d586fa 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-no-dlq-yet.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=7eeaf972f662e4e20922ac92aaee56e7 2500w" />
</Frame>

Again, I'm going to tag the queue with "project: sqs-demo". Being religious about tagging resources will save you a lot
of time and headache later.

Now we're going to create our dead-letter queue. Navigate back to the SQS console, and click "Create queue". We're going
to use mostly the same settings as before, but we're going to name this queue `my-job-queue-dlq.fifo`, and set its
permissions to allow `job-worker` to *send* messages to it. For this one, we will enable "Redrive allow policy", and
allow our first queue as the source queue.

<Frame caption="Enable access from our main queue to the dead-letter queue">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-create-dlq-redrive.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=43153d2c22fcbfddf3e08719144be002" alt="Creating a dead-letter queue" data-og-width="1058" width="1058" data-og-height="550" height="550" data-path="container-engine/images/sqs-create-dlq-redrive.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-create-dlq-redrive.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ae78c7182fbc9397f92759a9fc4f030c 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-create-dlq-redrive.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=da8136b4ac375e037c9d1664066795d2 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-create-dlq-redrive.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=7df4d43b20898080d71311198edf6d2f 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-create-dlq-redrive.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ff380c859070aadecc4da76862941057 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-create-dlq-redrive.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=05f046f8aecc792930512ac0474a32bd 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-create-dlq-redrive.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=1f07b118476636164530e1f74b878baf 2500w" />
</Frame>

Once this dead-letter queue is created, we can go back and edit our original queue, and enable the dead-letter queue.
We'll choose our dead-letter queue as the destination, and set the maximum receive count to 3. This means that if a job
is received 3 times without being deleted, it will be moved to the dead-letter queue.

<Frame caption="Enable the dead-letter queue on the main queue">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-assign-dlq.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=8097505ff2c298d61f9552bdfcc7db44" alt="Enabling the dead-letter queue" data-og-width="1064" width="1064" data-og-height="371" height="371" data-path="container-engine/images/sqs-assign-dlq.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-assign-dlq.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=4d0302391606d0a32ece76e2bc0a7f4d 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-assign-dlq.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=0626db761b9322b6e71e4714f0d57da2 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-assign-dlq.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=5ea5b4f8848449dc261d2baaab0a16b3 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-assign-dlq.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=afc7c5ab2d87dc2a2b360dd941347277 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-assign-dlq.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=82eb88c66826b6d474c85163f8def2d3 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-assign-dlq.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=82998399e6fb551f6acd82902bc5a23b 2500w" />
</Frame>

For our application to use these queues, we will need the Queue URL, available on the queue's details page.

<Frame caption="The Queue URL">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-get-queue-url.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=afca31cb2c25dd6906cd48fff60f435a" alt="The Queue URL" data-og-width="1584" width="1584" data-og-height="374" height="374" data-path="container-engine/images/sqs-get-queue-url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-get-queue-url.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=5bb20c3b9ee22b8eec93b08e533c2cac 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-get-queue-url.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=00f636d3dd1b8cd1ffe67d013837feee 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-get-queue-url.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=f9cf4fbdb0a43b472eb5b2bce5abbe5c 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-get-queue-url.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=6cbb11c370d2fa75ca4c627eb38c53b2 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-get-queue-url.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=d8d7b94acb3fc2d1c82b4463e020dbf0 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-get-queue-url.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=8ffd2333c45b933f61cefe465af9468c 2500w" />
</Frame>

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

We're going to use the `boto3` library to interact with both SQS and R2. You can install it with `pip install boto3`.

First, we need to set up our environment variables. All of the following environment variables will be needed by the
application code.

There are several ways to do this, but what I've done for my development environment is create a file called
`worker.env` in the root of my project, and add the following lines:

```shell  theme={null}
R2_AWS_ACCESS_KEY_ID=your-access-key-id
R2_AWS_SECRET_ACCESS_KEY=your-secret-access-key
R2_S3_ENDPOINT_URL=your-s3-endpoint-url
R2_BUCKET_NAME=your-bucket-name
SQS_AWS_ACCESS_KEY_ID=your-access-key-id
SQS_AWS_SECRET_ACCESS_KEY=your-secret-access-key
SQS_AWS_REGION=your-region
SQS_QUEUE_URL=your-queue-url
SQS_DLQ_URL=your-dlq-url
```

Then, to source this into my environment when I run my code, I run the following command:

```shell  theme={null}
export $(grep -v '^#' worker.env | xargs -d '\n')
```

Make sure `*.env` is in your .gitignore. You don't want to commit your secrets to your repository.

Now, create a file called `clients.py`, and add the following code:

```python  theme={null}
import boto3
import os

# Get the environment variables
r2_aws_region = "auto"
r2_aws_access_key_id = os.getenv('R2_AWS_ACCESS_KEY_ID')
r2_aws_secret_access_key = os.getenv('R2_AWS_SECRET_ACCESS_KEY')
r2_s3_endpoint_url = os.getenv('R2_S3_ENDPOINT_URL')
r2_bucket_name = os.getenv('R2_BUCKET_NAME')

sqs_aws_access_key_id = os.getenv('SQS_AWS_ACCESS_KEY_ID')
sqs_aws_secret_access_key = os.getenv('SQS_AWS_SECRET_ACCESS_KEY')
sqs_aws_region = os.getenv('SQS_AWS_REGION')
sqs_queue_url = os.getenv('SQS_QUEUE_URL')
sqs_dlq_url = os.getenv('SQS_DLQ_URL')

# Create the clients
sqs = boto3.client('sqs',
                   aws_access_key_id=sqs_aws_access_key_id,
                   aws_secret_access_key=sqs_aws_secret_access_key,
                   region_name=sqs_aws_region)

s3 = boto3.client('s3',
                  aws_access_key_id=r2_aws_access_key_id,
                  aws_secret_access_key=r2_aws_secret_access_key,
                  region_name=r2_aws_region,
                  endpoint_url=r2_s3_endpoint_url)
```

Now, we create our main application file, `main.py`, where we need to define functions for retrieving a job, for
extending the visibility timeout of a job, and for deleting a job. We also need to define a function for saving a
checkpoint to cloud storage, and for loading a checkpoint from cloud storage.

We're going to need to import some things from our client file.

```python  theme={null}
from clients import sqs, s3, sqs_queue_url, sqs_dlq_url, r2_bucket_name
```

Now, we define a `get_job` function:

```python  theme={null}
import json

visibility_timeout = 60


def get_job():
    '''
    Get the job from the SQS queue

    Returns:
    - job: dict, the job to be processed
    - receipt_handle: str, the receipt handle of the message

    If there are no messages in the queue, return None, None
    '''
    response = sqs.receive_message(
        QueueUrl=sqs_queue_url,
        AttributeNames=['All'],
        MaxNumberOfMessages=1,
        MessageAttributeNames=['All'],
        VisibilityTimeout=visibility_timeout,
        WaitTimeSeconds=20
    )

    if 'Messages' in response:
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']
        job = json.loads(message['Body'])
        return job, receipt_handle
    else:
        return None, None
```

Now, we define a `heartbeat_job` function, that will extend the visibility timeout on a cadence, and can be interrupted
from a different thread. This function also needs to be able to stop the main job if the receipt handle is invalid,
which means the job has been acknowledged (finished), or the message has been given to another worker.

```python  theme={null}
import time
import threading


def heartbeat_job(receipt_handle: str, heartbeat_stop_signal: threading.Event, job_stop_signal: threading.Event):
    '''
    Send a heartbeat to the SQS queue to keep the job alive

    Parameters:
    - receipt_handle: str, the receipt handle of the message
    - heartbeat_stop_signal: threading.Event, a signal to stop the heartbeat
    - job_stop_signal: threading.Event, a signal to stop the main job
    '''
    while not heartbeat_stop_signal.is_set():
        try:
            sqs.change_message_visibility(
                QueueUrl=sqs_queue_url,
                ReceiptHandle=receipt_handle,
                VisibilityTimeout=visibility_timeout
            )
            time.sleep(visibility_timeout / 2)
        except boto3.SQS.Client.exceptions.ReceiptHandleIsInvalid:
            # If the receipt handle is invalid, it means the job has been
            # acknowledged, or the message has been given to another worker.
            # In this case, we can stop the heartbeat, and interrupt the
            # main job.
            job_stop_signal.set()
            break
```

Now, we need functions to release the job to be retried, and to acknowledge the job, completed or failed.

```python  theme={null}
def release_job(receipt_handle: str):
    '''
    Release the job back to the SQS queue

    Parameters:
    - receipt_handle: str, the receipt handle of the message
    '''
    try:
        sqs.change_message_visibility(
            QueueUrl=sqs_queue_url,
            ReceiptHandle=receipt_handle,
            VisibilityTimeout=0
        )
    except boto3.SQS.Client.exceptions.ReceiptHandleIsInvalid:
        # If the receipt handle is invalid, it means the job has been
        # acknowledged, or the message has been given to another worker.
        # In this case, we can ignore the error, because we were trying to
        # release the job anyway.
        pass


def acknowledge_job(receipt_handle: str):
    '''
    Acknowledge the job and delete it from the SQS queue

    Parameters:
    - receipt_handle: str, the receipt handle of the message
    '''
    sqs.delete_message(
        QueueUrl=sqs_queue_url,
        ReceiptHandle=receipt_handle
    )


def fail_job(job, receipt_handle: str):
    '''
    Move the job to the dead-letter queue

    Parameters:
    - receipt_handle: str, the receipt handle of the message
    '''
    # First remove job from the queue
    acknowledge_job(receipt_handle)

    # Then send it to the DLQ
    sqs.send_message(
        QueueUrl=sqs_dlq_url,
        MessageBody=json.dumps(job)
    )
```

We also want a function to download the checkpoint from cloud storage, and a function to upload the checkpoint to cloud
storage. In this simplified example, we're going to use a small JSON file for the checkpoint, but the principle is the
same no matter what the actual checkpoint is.

```python  theme={null}
def download_checkpoint(job_id: str):
    '''
    Download the checkpoint from S3

    Parameters:
    - job_id: str, the job ID

    Returns:
    - checkpoint: dict, the checkpoint
    '''
    try:
        response = s3.get_object(
            Bucket=r2_bucket_name,
            Key=f'{job_id}/checkpoint.json'
        )
    except boto3.exceptions.S3.NoSuchKey:
        return None

    checkpoint = json.loads(response['Body'].read())
    return checkpoint


def upload_checkpoint(job_id: str, checkpoint: dict):
    '''
    Upload the checkpoint to S3

    Parameters:
    - job_id: str, the job ID
    - checkpoint: dict, the checkpoint
    '''
    s3.put_object(
        Bucket=r2_bucket_name,
        Key=f'{job_id}/checkpoint.json',
        Body=json.dumps(checkpoint)
    )
```

We may also need a function to validate the job before engaging in the main work. This function should return `True` if
the job is valid, and `False` if the job is invalid. In our case, we're going to assume that any job with a `job_id` and
`steps` is valid, but your usecase is likely far more complex than that.

```python  theme={null}
def validate_job(job: dict):
    # This is a very simple function for our very simple application.
    # You should replace this with your actual validation logic.
    return 'job_id' in job and 'steps' in job
```

Now, we need a function for "doing the work", which in our case is just slowly calculating a sum. For you this may be AI
training jobs or molecular simulations.

```python  theme={null}
def do_the_actual_work(job: dict, checkpoint: dict, stop_signal: threading.Event) -> int | None:
    '''
    Do the actual work for the job. This function will simulate work by
    sleeping for 30 seconds and incrementing the step and sum in the
    checkpoint.

    Parameters:
    - job: dict, the job
    - checkpoint: dict, the checkpoint
    - stop_signal: threading.Event, a signal to stop the work
    '''
    while checkpoint['step'] < job['steps'] and not stop_signal.is_set():
        # Simulate work
        time.sleep(30)

        # If the job was interrupted, we don't want to upload the
        # checkpoint, because it may conflict with the next worker.
        if not stop_signal.is_set():
            # Update the checkpoint.
            checkpoint['step'] += 1
            checkpoint['sum'] += checkpoint['step']
            upload_checkpoint(job['job_id'], checkpoint)

    if not stop_signal.is_set():
        return checkpoint['sum']
    else:
        return None
```

Once our work has completed, we'll need a function to upload the results to cloud storage.

```python  theme={null}
def upload_result(job_id: str, result: int):
    '''
    Upload the result to S3

    Parameters:
    - job_id: str, the job ID
    - result: int, the result
    '''
    s3.put_object(
        Bucket=r2_bucket_name,
        Key=f'{job_id}/result.txt',
        Body=str(result)
    )
```

Now, we need to put it all together in a function called `process_job`.

```python  theme={null}
def process_job(job: dict, receipt_handle: str) -> None:
    # Now that we have the job, we need to start a separate thread that
    # heartbeats for it. This will keep the job alive in the SQS queue.
    # Separate threads are critical here, because our main work is likely
    # blocking, and we don't want to block the heartbeat.
    heartbeat_stop_signal = threading.Event()
    job_stop_signal = threading.Event()
    heartbeat_thread = threading.Thread(
        target=heartbeat_job, args=(
            receipt_handle, heartbeat_stop_signal, job_stop_signal))
    heartbeat_thread.start()

    # If there's a checkpoint, we want to use it, but if not, we need to
    # initialize our state.
    checkpoint = download_checkpoint(job['job_id'])
    if checkpoint is None:
        checkpoint = {'step': 0, 'sum': 0}

    # Some jobs may have a validation step. For instance, dreambooth training may have a step
    # that verifies if all inputs have faces. If the validation fails, we should stop the job
    # and not retry it, but instead move it to the DLQ. In this situation, we can
    # be confident that the job will never succeed.
    if not validate_job(job):
        heartbeat_stop_signal.set()
        fail_job(job, receipt_handle)
        heartbeat_thread.join()
        return

    # Now we can do the actual work
    try:
        result = do_the_actual_work(job, checkpoint)
        if result is None:
            # This means the job was interrupted, so we need to release it
            # back to the queue.
            heartbeat_stop_signal.set()
            heartbeat_thread.join()
            release_job(receipt_handle)
            return

        # The job isn't really done until the result is uploaded.
        upload_result(job['job_id'], result)

        # Once the result is uploaded, we can acknowledge the job and stop
        # the heartbeat.
        acknowledge_job(receipt_handle)
        heartbeat_stop_signal.set()
        heartbeat_thread.join()
    except Exception as e:
        # If there's an error, we need to release the job back to the queue
        # so it can be retried.
        heartbeat_stop_signal.set()
        heartbeat_thread.join()
        release_job(receipt_handle)
        return
```

Finally, we need to create a loop that will run forever, processing jobs as they come in.

```python  theme={null}
if __name__ == '__main__':
    while True:
        job, receipt_handle = get_job()
        if job is not None:
            process_job(job, receipt_handle)
        else:
            time.sleep(10)
```

### Completed Example

```python  theme={null}
from clients import sqs, r2, sqs_queue_url, sqs_dlq_url, r2_bucket_name
import json
import time
import threading
import boto3

visibility_timeout = 60


def get_job() -> tuple:
    '''
    Get the job from the SQS queue

    Returns:
    - job: dict, the job to be processed
    - receipt_handle: str, the receipt handle of the message

    If there are no messages in the queue, return None, None
    '''
    response = sqs.receive_message(
        QueueUrl=sqs_queue_url,
        AttributeNames=['All'],
        MaxNumberOfMessages=1,
        MessageAttributeNames=['All'],
        VisibilityTimeout=visibility_timeout,
        WaitTimeSeconds=20
    )

    if 'Messages' in response:
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']
        job = json.loads(message['Body'])
        return job, receipt_handle
    else:
        return None, None


def heartbeat_job(receipt_handle: str, heartbeat_stop_signal: threading.Event, job_stop_signal: threading.Event) -> None:
    '''
    Send a heartbeat to the SQS queue to keep the job alive

    Parameters:
    - receipt_handle: str, the receipt handle of the message
    - heartbeat_stop_signal: threading.Event, a signal to stop the heartbeat
    - job_stop_signal: threading.Event, a signal to stop the main job
    '''
    while not heartbeat_stop_signal.is_set():
        try:
            sqs.change_message_visibility(
                QueueUrl=sqs_queue_url,
                ReceiptHandle=receipt_handle,
                VisibilityTimeout=visibility_timeout
            )
            time.sleep(visibility_timeout / 2)
        except boto3.SQS.Client.exceptions.ReceiptHandleIsInvalid:
            # If the receipt handle is invalid, it means the job has been
            # acknowledged, or the message has been given to another worker.
            # In this case, we can stop the heartbeat, and interrupt the
            # main job.
            job_stop_signal.set()
            break


def release_job(receipt_handle: str) -> None:
    '''
    Release the job back to the SQS queue

    Parameters:
    - receipt_handle: str, the receipt handle of the message
    '''
    try:
        sqs.change_message_visibility(
            QueueUrl=sqs_queue_url,
            ReceiptHandle=receipt_handle,
            VisibilityTimeout=0
        )
    except boto3.SQS.Client.exceptions.ReceiptHandleIsInvalid:
        # If the receipt handle is invalid, it means the job has been
        # acknowledged, or the message has been given to another worker.
        # In this case, we can ignore the error, because we were trying to
        # release the job anyway.
        pass


def acknowledge_job(receipt_handle: str) -> None:
    '''
    Acknowledge the job and delete it from the SQS queue

    Parameters:
    - receipt_handle: str, the receipt handle of the message
    '''
    sqs.delete_message(
        QueueUrl=sqs_queue_url,
        ReceiptHandle=receipt_handle
    )


def fail_job(job, receipt_handle: str) -> None:
    '''
    Move the job to the dead-letter queue

    Parameters:
    - receipt_handle: str, the receipt handle of the message
    '''
    # First remove job from the queue
    acknowledge_job(receipt_handle)

    # Then send it to the DLQ
    sqs.send_message(
        QueueUrl=sqs_dlq_url,
        MessageBody=json.dumps(job)
    )


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
    except boto3.exceptions.S3.NoSuchKey:
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


def do_the_actual_work(job: dict, checkpoint: dict, stop_signal: threading.Event) -> int | None:
    '''
    Do the actual work for the job. This function will simulate work by
    sleeping for 30 seconds and incrementing the step and sum in the
    checkpoint.

    Parameters:
    - job: dict, the job
    - checkpoint: dict, the checkpoint
    - stop_signal: threading.Event, a signal to stop the work
    '''
    while checkpoint['step'] < job['steps'] and not stop_signal.is_set():
        # Simulate work
        time.sleep(30)

        # If the job was interrupted, we don't want to upload the
        # checkpoint, because it may conflict with the next worker.
        if not stop_signal.is_set():
            # Update the checkpoint.
            checkpoint['step'] += 1
            checkpoint['sum'] += checkpoint['step']
            upload_checkpoint(job['job_id'], checkpoint)

    if not stop_signal.is_set():
        return checkpoint['sum']
    else:
        return None


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


def process_job(job: dict, receipt_handle: str) -> None:
    # Now that we have the job, we need to start a separate thread that
    # heartbeats for it. This will keep the job alive in the SQS queue.
    # Separate threads are critical here, because our main work is likely
    # blocking, and we don't want to block the heartbeat.
    heartbeat_stop_signal = threading.Event()
    job_stop_signal = threading.Event()
    heartbeat_thread = threading.Thread(
        target=heartbeat_job, args=(
            receipt_handle, heartbeat_stop_signal, job_stop_signal))
    heartbeat_thread.start()

    # If there's a checkpoint, we want to use it, but if not, we need to
    # initialize our state.
    checkpoint = download_checkpoint(job['job_id'])
    if checkpoint is None:
        checkpoint = {'step': 0, 'sum': 0}

    # Some jobs may have a validation step. For instance, dreambooth training may have a step
    # that verifies if all inputs have faces. If the validation fails, we should stop the job
    # and not retry it, but instead move it to the DLQ. In this situation, we can
    # be confident that the job will never succeed.
    if not validate_job(job):
        heartbeat_stop_signal.set()
        fail_job(job, receipt_handle)
        heartbeat_thread.join()
        return

    # Now we can do the actual work
    try:
        result = do_the_actual_work(job, checkpoint)
        if result is None:
            # This means the job was interrupted, so we need to release it
            # back to the queue.
            heartbeat_stop_signal.set()
            heartbeat_thread.join()
            release_job(receipt_handle)
            return

        # The job isn't really done until the result is uploaded.
        upload_result(job['job_id'], result)

        # Once the result is uploaded, we can acknowledge the job and stop
        # the heartbeat.
        acknowledge_job(receipt_handle)
        heartbeat_stop_signal.set()
        heartbeat_thread.join()
    except Exception as e:
        # If there's an error, we need to release the job back to the queue
        # so it can be retried.
        heartbeat_stop_signal.set()
        heartbeat_thread.join()
        release_job(receipt_handle)
        return


if __name__ == '__main__':
    while True:
        job, receipt_handle = get_job()
        if job is not None:
            process_job(job, receipt_handle)
        else:
            time.sleep(10)
```

Now that we have our worker application ready to go, we can run it with `python main.py`. It will run forever, polling
the queue for jobs, and processing them as they come in.

## Submitting Jobs to the Queue

Next, we need a way to submit jobs to the queue. We're going to use the `boto3` library for this as well, but we'll be
using the AWS keys for the `job-submitter` user. I've saved mine in a file called `submitter.env`, and I'm going to
source them into my environment with the following command:

```shell  theme={null}
export $(grep -v '^#' submitter.env | xargs -d '\n')
```

I've named my submitter script `submit-jobs.py`.

The first part should look familiar, getting config from the environment, and initializing our SQS client.

```python  theme={null}
import boto3
import os

# Get the environment variables
sqs_aws_access_key_id = os.getenv('SQS_AWS_ACCESS_KEY_ID')
sqs_aws_secret_access_key = os.getenv('SQS_AWS_SECRET_ACCESS_KEY')
sqs_aws_region = os.getenv('SQS_AWS_REGION')
sqs_queue_url = os.getenv('SQS_QUEUE_URL')

# Create the client
sqs = boto3.client('sqs',
                   aws_access_key_id=sqs_aws_access_key_id,
                   aws_secret_access_key=sqs_aws_secret_access_key,
                   region_name=sqs_aws_region)
```

For this, let's assume we have ten thousand jobs we want to submit, each taking 5 hours to complete. We're going to use
`send_message_batch` to maximize throughput, and we're going to assign a `MessageDeduplicationId` to each job to ensure
exactly-once processing.

```python  theme={null}
from uuid import uuid4
import json

def submit_one_batch(jobs: list) -> None:
    '''
    Submit a batch of jobs to the SQS queue

    Parameters:
    - jobs: list, the list of jobs
    '''
    if len(jobs) == 0:
        return
    if len(jobs) > 10:
        raise ValueError('You can submit at most 10 jobs at a time')

    def job_to_entry(job):
        if 'job_id' not in job:
            job["job_id"] = str(uuid4())
        job["steps"] = int(job["steps"])
        return {
            'Id': job["job_id"],
            'MessageDeduplicationId': job["job_id"],
            'MessageGroupId': job["job_id"],
            'MessageBody': json.dumps(job)
        }

    entries = [job_to_entry(job) for job in jobs]
    response = sqs.send_message_batch(
        QueueUrl=sqs_queue_url,
        Entries=entries
    )
    if 'Failed' in response:
        print(response)
        raise Exception(f'Failed to submit jobs: {response["Failed"]}')
    else:
        print(f'Submitted {len(jobs)} jobs')
```

This first function we've defined will submit one single batch, up to the SQS-imposed limit of 10 messages at a time.
Now we need a function that can take an arbitrarily large set of jobs and submit them all successfully.

```python  theme={null}
from typing import Iterable


def submit_jobs(jobs: Iterable) -> None:
    '''
    Submit an arbitrary number of jobs to the queue

    Parameters:
    - jobs: Iterable, the iterable of jobs
    '''
    batch = []
    for job in jobs:
        batch.append(job)
        if len(batch) == 10:
            submit_one_batch(batch)
            batch = []
    if batch:
        submit_one_batch(batch)
```

Now, suppose we have a csv with our 10,000 jobs, and we want to submit them all. Our CSV (data.csv) looks like this,
with 10,000 rows.

```csv  theme={null}
job_id,steps
job-0,600
job-1,600
job-2,600
job-3,600
```

Now, in our job submitter script, we can read this CSV and submit all the jobs, lazily reading the csv so as not to run
out of memory. We wouldn't anyways with this tiny example, but it's a good habit to get into.

```python  theme={null}
import csv

if __name__ == '__main__':
    with open("data.csv") as f:
        reader = csv.DictReader(f)
        submit_jobs(reader)
```

### Completed Example

```python  theme={null}
import boto3
import os
from uuid import uuid4
import json
from typing import Iterable
import csv

# Get the environment variables
sqs_aws_access_key_id = os.getenv('SQS_AWS_ACCESS_KEY_ID')
sqs_aws_secret_access_key = os.getenv('SQS_AWS_SECRET_ACCESS_KEY')
sqs_aws_region = os.getenv('SQS_AWS_REGION')
sqs_queue_url = os.getenv('SQS_QUEUE_URL')

# Create the client
sqs = boto3.client('sqs',
                   aws_access_key_id=sqs_aws_access_key_id,
                   aws_secret_access_key=sqs_aws_secret_access_key,
                   region_name=sqs_aws_region)


def submit_one_batch(jobs: list) -> None:
    '''
    Submit a batch of jobs to the SQS queue

    Parameters:
    - jobs: list, the list of jobs
    '''
    if len(jobs) == 0:
        return
    if len(jobs) > 10:
        raise ValueError('You can submit at most 10 jobs at a time')

    def job_to_entry(job):
        if 'job_id' not in job:
            job["job_id"] = str(uuid4())
        job["steps"] = int(job["steps"])
        return {
            'Id': job["job_id"],
            'MessageDeduplicationId': job["job_id"],
            'MessageGroupId': job["job_id"],
            'MessageBody': json.dumps(job)
        }

    entries = [job_to_entry(job) for job in jobs]
    response = sqs.send_message_batch(
        QueueUrl=sqs_queue_url,
        Entries=entries
    )
    if 'Failed' in response:
        print(response)
        raise Exception(f'Failed to submit jobs: {response["Failed"]}')
    else:
        print(f'Submitted {len(jobs)} jobs')


def submit_jobs(jobs: Iterable) -> None:
    '''
    Submit an arbitrary number of jobs to the queue

    Parameters:
    - jobs: Iterable, the iterable of jobs
    '''
    batch = []
    for job in jobs:
        batch.append(job)
        if len(batch) == 10:
            submit_one_batch(batch)
            batch = []
    if batch:
        submit_one_batch(batch)


if __name__ == '__main__':
    with open("data.csv") as f:
        reader = csv.DictReader(f)
        submit_jobs(reader)
```

### Running the Job Submitter

Run the job submitter with `python submit-jobs.py`. It will read the csv file and submit all the jobs to the queue.

Once that has run, we can see in the SQS console that our queue has 10000 messages.

<Frame caption="The SQS Console showing 10000 messages in the queue">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-10k-messages.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=323473264fdd06c2b734a7054921916e" alt="The SQS Console showing 10000 messages in the queue" data-og-width="1054" width="1054" data-og-height="702" height="702" data-path="container-engine/images/sqs-10k-messages.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-10k-messages.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=39959ce12ed26a15877b93f8bd33f91e 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-10k-messages.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=6ace1cf35d2cdef86b80c506a5f1f98b 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-10k-messages.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=e5384996a7a6bf40e50d6799220124be 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-10k-messages.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ee31e0bd064d4302edd1b0e5471af02d 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-10k-messages.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=31be3553cf24c7010635e25278996863 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-10k-messages.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=828d81cb4255b1e064f5bbd705bc9bf0 2500w" />
</Frame>

## Containerize the Worker Application

Now that we have our worker application and our job submitter, we can package our worker in a docker container, and run
it on a SaladCloud Container Group.

First, let's make sure our dependencies are documented in `requirements.txt`.

```shell  theme={null}
boto3
```

Now, create a new file called `Dockerfile`. Our application is simple, so a basic python base image should be fine.

```dockerfile  theme={null}
FROM python:3.10.12-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY clients.py .
COPY main.py .

CMD ["python", "main.py"]
```

Now, build the docker image, and use a tag that makes sense for you.

```shell  theme={null}
docker build -t saladtechnologies/lrt-worker-examples:sqs .
```

Now, we can test it locally to make sure it works, before we deploy it to SaladCloud.

```shell  theme={null}
docker run -it --rm  --env-file worker.env saladtechnologies/lrt-worker-examples:sqs
```

You should see it start up and begin processing a job. Once this is working, you can go ahead and terminate the
container with `Ctrl+C`.

Now, we can push the image to Docker Hub.

```shell  theme={null}
docker push saladtechnologies/lrt-worker-examples:sqs
```

## Deploying the Worker to SaladCloud

To deploy our worker to SaladCloud, we need to create a new Container Group. This can be done via the API, SDKs, or the
Portal. We're going to use the Portal.

We're going to create a new Container Group, and we're going to use the image we just pushed to Docker Hub. We're going
to request 100 replicas (the max via the portal), and we're going to set all of our environment variables from
`worker.env`.

<Frame caption="Creating a new Container Group">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-1.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=a3b857168f8b8065d3851101f2a10586" alt="Creating a new Container Group" data-og-width="662" width="662" data-og-height="789" height="789" data-path="container-engine/images/sqs-cg-create-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-1.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=a269135a4d30e73389c9019a5848f53b 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-1.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=6b14f875b936048e932ab7ed7342bb72 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-1.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=517fecdd967a0db6a9329fce35c04271 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-1.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ea57317d7c5c50d4c645ab271503e06d 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-1.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=a96f13b1d1314118e3eb279ba19dfd2e 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-1.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=a60d4b8c39a310076886879d09fdfb72 2500w" />
</Frame>

Our application is extremely simple, so we're going to only request 1 vCPU, 1 GB of RAM, and no GPU. Your hardware
requirements are likely significantly higher than this.

<Frame caption="Setting the hardware requirements">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-2.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=dd064fd61720978b199cfbf9a2e251aa" alt="Setting the hardware requirements" data-og-width="648" width="648" data-og-height="1058" height="1058" data-path="container-engine/images/sqs-cg-create-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-2.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=f2a3bb09d27d42bb68022ed85b498441 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-2.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=2665ee57a09a1c61a1a47a16b48cc594 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-2.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=3bf1dbdf30d7b5bc3f010109be1b225c 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-2.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=800b59815f4783e942e2eaf116bf9165 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-2.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=7808a6d2a691d54eea83d01fe74ffde2 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-2.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=20dcb4da25d1079a4d4f3824425e9579 2500w" />
</Frame>

All CPU-only jobs are prioritized as "Batch" (the lowest tier), and we don't need any additional storage for this
particular application.

<Frame caption="Setting the job priority and storage requirements">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-3.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=e0255a7f76525200bbb03dd0a25f2a83" alt="Setting the job priority and storage requirements" data-og-width="643" width="643" data-og-height="568" height="568" data-path="container-engine/images/sqs-cg-create-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-3.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=e633cd94adc006d7361cc441b6908c2a 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-3.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=8cb74fe6b1b67ec6851fe5aa6f83afa1 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-3.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=b8d40ab9ae86795bd51e8991f2556586 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-3.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=c8c22665fa8c7028fca77194e832a069 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-3.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=d0090c081440d294d0651932bce2d115 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-create-3.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=478657d38cb767e153c1ecdcb137851f 2500w" />
</Frame>

We do not need the container gateway, as our application pulls its work from a queue. We also do not need health probes,
as those are primarily for services accessed via Container Gateway. Go ahead and hit deploy, and you'll be taken to the
container group page, where you can see its status.

First, it will prepare by pulling the container image into our high-performance cache.

<Frame caption="Preparing the container">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-preparing.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=27d9729b052b1b6a4fa502ac5f34906d" alt="Preparing the container" data-og-width="427" width="427" data-og-height="210" height="210" data-path="container-engine/images/sqs-cg-preparing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-preparing.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=0bf18919702dcc05b9e2cd789cea82c5 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-preparing.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=627e78d5062e1a2d86d4b9689d2c152e 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-preparing.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=042faf4b815158aadcd9eb7b72ef2411 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-preparing.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=37adc34e500cad04c6ce8f24b7a7a2f1 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-preparing.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=8950b2fc01311bed2c78c7fe76a8f890 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-preparing.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=1ed0694af63ed3cac138e4d782cd0972 2500w" />
</Frame>

Once it's prepared, it will start allocating replicas, and downloading the container image to those replicas.

<Frame caption="Downloading the images to the replicas">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-deploying.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=1c3453f8d23dafe990bc182c23e16fc0" alt="Downloading the images to the replicas" data-og-width="1265" width="1265" data-og-height="753" height="753" data-path="container-engine/images/sqs-cg-deploying.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-deploying.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=0e8caf48283816ba18f9a1fec62d2cce 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-deploying.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=d50d6310ad55d4916b24dcb257724f24 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-deploying.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=210e1159d30fe9aa9fc6c85d45e2e2e7 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-deploying.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=b26a9ecd6a7e8aae98caa17a2d18b0d3 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-deploying.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=e6eb494dc0a20f1131d1bb80cc1194ca 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-deploying.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=3f1edec784192e2ac7a3662dbcbd456e 2500w" />
</Frame>

After a minute or so, we should see our instances up and running.

<Frame caption="Instances up and running">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-running.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=594f88c42f3301de433d728c593ec4f4" alt="Instances up and running" data-og-width="1196" width="1196" data-og-height="977" height="977" data-path="container-engine/images/sqs-cg-running.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-running.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=d68f26b3cdabea70bc6d37ae627706d7 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-running.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=212f77be592db0628a8a9ec1e83ada98 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-running.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=3285b8cf691621d4b24c78d88f0c3567 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-running.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=bccc427c5abd28933d6668284916aa7a 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-running.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=47375f27f4a53cca65014510481441bb 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-cg-running.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=d5a9788994d7997767a807258bcee6f7 2500w" />
</Frame>

## Validating That It Works

Now that our cluster is up and running, we can go to the SQS console, and see that we have in-flight messages now.

<Frame caption="In-flight messages in the SQS queue">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-messages-in-flight.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=6084c7549004058c7f64f724ae3bcc58" alt="In-flight messages in the SQS queue" data-og-width="1651" width="1651" data-og-height="669" height="669" data-path="container-engine/images/sqs-messages-in-flight.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-messages-in-flight.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=3fc47c4b912c540a03ef1def0a1010da 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-messages-in-flight.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=de4e85fe4e042f7e85b05fd98f70c7dd 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-messages-in-flight.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=83d9885941a2ce131690df43b6844d8b 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-messages-in-flight.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=da6343ef58da56062d13d57a52241d3f 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-messages-in-flight.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=46be56288cd490c477f76c8faf4bb160 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-messages-in-flight.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=9d33450f886925e46c47634e2c43e06d 2500w" />
</Frame>

From the R2 console, we can see that our bucket is being filled with checkpoints and results.

<Frame caption="Checkpoints and results in the R2 bucket">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=9099bb501409fe12bc243608f06e4e5a" alt="Checkpoints and results in the R2 bucket" data-og-width="1319" width="1319" data-og-height="1054" height="1054" data-path="container-engine/images/r2-bucket-has-objects.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=fca917d1c54e99f0024ab124f5312a72 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=33700862cbd01bb8c2bae4ce71c9c6c9 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=ca8443a6b6c6ed132359446e5ea3c23c 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=e1751e77b2a6e0c363276500941307d7 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=4a2d26134b14417dab07c3ab57cc68a3 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/r2-bucket-has-objects.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=881dcd7187190b5a42b55021b7ffe42a 2500w" />
</Frame>

## Autoscaling

Now that we have our worker running, we can set up some simple autoscaling to automatically scale the number of replicas
up and down based on the number of messages in the queue.

There are many ways to implement autoscaling, but for simplicity, we are going to use a scheduled task that runs every 5
minutes, and sets the number of replicas to be equal to the number of messages in the queue, limited to 250 replicas
(the maximum in the API). To implement this, we're going to use AWS Lambda, a serverless compute service that can run
code in response to events. Cloudflare Workers can also be used to implement this, along with most other serverless
compute platforms.

Navigate to the Lambda console, and create a new function.

<Frame caption="Creating a new Lambda function">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-console.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=83bde0a9ce7f9f988f2cfbcf346b6ead" alt="Creating a new Lambda function" data-og-width="1410" width="1410" data-og-height="220" height="220" data-path="container-engine/images/sqs-lambda-console.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-console.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=e2583c4fb7eb3adfc85952a89d864e3d 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-console.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=868db3689e58c455ba5602b55fa22184 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-console.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=c426808c17ebf8a4d6e92802c46918cf 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-console.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=0a8a8ed9d5aa9a5ee1eccd0ff85af435 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-console.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=06606febe54ce4f9a19a0237bcf5d117 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-console.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=d17f2036eed363b966abdd4a693c4c28 2500w" />
</Frame>

We're going to use Python 3.13, and we'll run it with `arm64`, because it is cheaper, and we aren't doing anything
architecture-specific. We can leave the default permissions for now.

<Frame caption="Setting the runtime and architecture">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-create.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=a5192da4ffb0223476c1bb81814cdaf6" alt="Setting the runtime and architecture" data-og-width="1416" width="1416" data-og-height="815" height="815" data-path="container-engine/images/sqs-lambda-create.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-create.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=a7b337a6ede99118fa5c8d392b7f07e4 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-create.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=f3702b02da774ca7ff98e02b862b99c6 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-create.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=f3a16676a1bd1aef3ec330849d9cff5f 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-create.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=6d7a5f8aea9dddcf5859ce6422cc23c8 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-create.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=31ecc4c9a0603e92156c47aeef9522ac 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-create.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ff2f78f1764078e7de330cf8b641f19b 2500w" />
</Frame>

Once your function has been created, you'll land on the function overview page.

<Frame caption="The function overview page">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-editor.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=d6646c8832891aaf76670cab8d00caaa" alt="The function overview page" data-og-width="1400" width="1400" data-og-height="1009" height="1009" data-path="container-engine/images/sqs-lambda-editor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-editor.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=c19a3eac6cc457e8570f19e66455868c 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-editor.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=76979c5a42c0b78fbb68ed1766dd3189 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-editor.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=d04eff8d90a17e6bcc79083fbc587c0c 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-editor.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=1cfcc69864a5e7e3e50657cef38855bf 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-editor.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=eac288229330d27727f1276b5915cb0d 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-editor.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=a86c7771e8f26e529552071c14968db0 2500w" />
</Frame>

Next, we need to give this lambda the correct permissions to interact with our SQS queue.

First, we need to get the ARN for the *execution role* of the function, not the ARN of the function itself.

<Frame caption="Find The Execution Role">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-find-execution-role.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=65f029d4224991df603325e11ba030e7" alt="The ARN of the execution role" data-og-width="1651" width="1651" data-og-height="945" height="945" data-path="container-engine/images/sqs-lambda-find-execution-role.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-find-execution-role.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=e6ab98c80bb6eaf51bb2358d1ac2deb4 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-find-execution-role.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=8510c61d162adaa2ad51e06576c9f84e 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-find-execution-role.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=607a7d3eb6da993359acc241c2ccc566 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-find-execution-role.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=08c6dace0490a91ba3de86dd4ca53dd3 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-find-execution-role.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=d854ac93b98b474418dbeeea0278e99e 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-find-execution-role.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=63e0da02965271f99a382883a4d84599 2500w" />
</Frame>

Clicking that link will take you the IAM console page for that role, where you can then copy the ARN.

<Frame caption="The ARN of the execution role">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-find-role-arn.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=7976517ac29c1c0be8f0fe53f5671c27" alt="The ARN of the execution role" data-og-width="1423" width="1423" data-og-height="257" height="257" data-path="container-engine/images/sqs-lambda-find-role-arn.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-find-role-arn.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ccf52415baa8a50335018d9fb9e3764a 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-find-role-arn.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=cc45aea2f321f026885aa0ea107a2a56 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-find-role-arn.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=1978035d22f261d0ecef266c67c5d5b8 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-find-role-arn.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=174e6682d970c2bcb418aaedc2ccc16b 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-find-role-arn.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=157e9c21e5c20af1e2cf2fd48efd6460 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-find-role-arn.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=5b67a50dc540896ab311e48e98bb574f 2500w" />
</Frame>

We're going to do this by editing the policy created by the queue. Back in the SQS console, on the details page for our
queue, navigate to the "Queue Policies" tab.

<Frame caption="The Queue Policies tab">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-permissions.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=a74eae0d1183ea8435bff5cceb225884" alt="The Queue Policies tab" data-og-width="1636" width="1636" data-og-height="874" height="874" data-path="container-engine/images/sqs-lambda-permissions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-permissions.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=179149a54891386a2e68395f1f6e01f2 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-permissions.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=5bcf7eec18f0fa4b7b029edafaf0d619 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-permissions.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=e915fc6982bbf57b52d3ef4bb432b7ab 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-permissions.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=51fb8391b041c478cba01c647458bbb0 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-permissions.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=d593543feddaac709513fb326ea10ddd 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-permissions.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ce106e0d4c824e345b3111b01f385cb7 2500w" />
</Frame>

Add this additional statement to the Access policy, replacing the ARN with the ARN of the execution role of the lambda

```json  theme={null}
{
  "Sid": "AutoscalerAccess",
  "Action": ["sqs:GetQueueAttributes"],
  "Effect": "Allow",
  "Resource": "arn:aws:sqs:us-east-2:523358417554:my-job-queue.fifo",
  "Principal": {
    "AWS": ["arn:aws:iam::523358417554:role/service-role/lrt-autoscaling-role-some-unique-ending"]
  }
}
```

Save the queue policy, and now the lambda has the permissions it needs to get the current number of messages from the
queue.

Now, we need to write the code for the lambda. We're going to use the `boto3` library to interact with the SQS queue,
which in included by default in the lambda environment.

We will be setting our configuration for this lambda in environment variables. You can find this under configuration on
the lambda console page for our function. Alsol in configuration, we want to increase our function timeout to 10s, since
we have to make multiple serial requests to external services.

```python  theme={null}
import boto3
import os

# Our job queue
queue_url = os.environ['queue_url']

# Scaling Configuration
max_replicas = int(os.environ['max_replicas'])
min_replicas = int(os.environ['min_replicas'])

# Salad Info
org = os.environ['salad_org']
project = os.environ['salad_project']
container_group_name = os.environ['salad_container_group_name']
salad_api_key = os.environ['salad_api_key']

salad_base_url = "https://api.salad.com/api/public"
```

We also are going to write a simple helper function for making http requests. We don't need everything offered by
requests, just some basic functionality.

```python  theme={null}
import urllib
import http.client
import ssl
import json

def send_request(
    method: str,
    url: str,
    headers: Dict[str, str],
    body: Optional[Union[Dict[str, Any], str]] = None,
    timeout: int = 30,
    verify_ssl: bool = True
) -> Dict[str, Any]:
    """
    Send an HTTP request with precise control over headers case.

    Args:
        method: HTTP method (GET, POST, PUT, DELETE, etc.)
        url: The URL to send the request to
        headers: Dictionary of headers with exact case to preserve
        body: Optional request body (dict will be converted to JSON)
        timeout: Request timeout in seconds
        verify_ssl: Whether to verify SSL certificates

    Returns:
        Dictionary containing:
            - status_code: HTTP status code
            - headers: Response headers
            - body: Response body (parsed as JSON if possible)
            - raw: Raw response body as string
    """
    # Parse the URL to get components
    parsed_url = urllib.parse.urlparse(url)
    host = parsed_url.netloc
    path = parsed_url.path
    if parsed_url.query:
        path += f"?{parsed_url.query}"

    # Set up SSL context if needed
    context = None
    if parsed_url.scheme == 'https':
        context = ssl.create_default_context()
        if not verify_ssl:
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE

    # Prepare the body data if needed
    data = None
    if body is not None:
        if isinstance(body, dict):
            data = json.dumps(body).encode('utf-8')
        elif isinstance(body, str):
            data = body.encode('utf-8')
        else:
            data = str(body).encode('utf-8')

    try:
        # Choose the appropriate connection type
        if parsed_url.scheme == 'https':
            conn = http.client.HTTPSConnection(
                host=host,
                timeout=timeout,
                context=context
            )
        else:
            conn = http.client.HTTPConnection(
                host=host,
                timeout=timeout
            )

        # Send the request with unmodified headers
        conn.request(
            method=method.upper(),
            url=path,
            body=data,
            headers=headers  # Headers case is preserved exactly as provided
        )

        # Get the response
        response = conn.getresponse()
        status_code = response.status
        response_headers = dict(response.getheaders())
        response_body = response.read().decode('utf-8')

        # Try to parse the response as JSON
        try:
            parsed_body = json.loads(response_body)
        except json.JSONDecodeError:
            parsed_body = None

        return {
            "status_code": status_code,
            "headers": response_headers,
            "body": parsed_body,
            "raw": response_body
        }

    except http.client.HTTPException as e:
        return {
            "status_code": None,
            "headers": {},
            "body": None,
            "raw": None,
            "error": f"HTTP Error: {str(e)}"
        }
    except ssl.SSLError as e:
        return {
            "status_code": None,
            "headers": {},
            "body": None,
            "raw": None,
            "error": f"SSL Error: {str(e)}"
        }
    except Exception as e:
        return {
            "status_code": None,
            "headers": {},
            "body": None,
            "raw": None,
            "error": str(e)
        }
    finally:
        # Always close the connection
        if 'conn' in locals():
            conn.close()
```

Next, we're going to define some helper function for using the 4 API methods we need to interact with SaladCloud.

```python  theme={null}
def get_container_group():
    response = send_request(
        method="GET",
        url=f"{salad_base_url}/organizations/{org}/projects/{project}/containers/{container_group_name}",
        headers={
            "Salad-Api-Key": salad_api_key
        }
    )
    return response["body"]


def start_container_group():
    send_request(
        method="POST",
        url=f"{salad_base_url}/organizations/{org}/projects/{project}/containers/{container_group_name}/start",
        headers={
            "Content-Type": "application/json",
            "Salad-Api-Key": salad_api_key
        }
    )


def stop_container_group():
    send_request(
        method="POST",
        url=f"{salad_base_url}/organizations/{org}/projects/{project}/containers/{container_group_name}/stop",
        headers={
            "Content-Type": "application/json",
            "Salad-Api-Key": salad_api_key
        }
    )


def set_replicas(replicas: int):
    send_request(
        method="PATCH",
        url=f"{salad_base_url}/organizations/{org}/projects/{project}/containers/{container_group_name}",
        body=json.dumps({
            "replicas": replicas
        }),
        headers={
            "Content-Type": "application/merge-patch+json",
            "Salad-Api-Key": salad_api_key
        }
    )
```

Finally, we can stitch it all together in the lambda handler.

```python  theme={null}
def lambda_handler(event, context):
    sqs = boto3.client('sqs')

    # We need to know how much work is waiting and how much is in flight
    attributes = sqs.get_queue_attributes(
        QueueUrl=queue_url,
        AttributeNames=['ApproximateNumberOfMessages',
                        'ApproximateNumberOfMessagesNotVisible']
    )

    num_waiting_messages = int(
        attributes['Attributes']['ApproximateNumberOfMessages'])
    num_messages_in_flight = int(
        attributes['Attributes']['ApproximateNumberOfMessagesNotVisible'])

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

    return {
        'statusCode': 200
    }
```

Now, deploy and test your lambda. You can use the default test event, as our lambda does not use any information from
the event itself.

<Frame caption="Testing the Lambda">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-deploy-and-test.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=3cf3084551fc02fa3eea9e43bb1903a8" alt="Testing the Lambda" data-og-width="863" width="863" data-og-height="463" height="463" data-path="container-engine/images/sqs-lambda-deploy-and-test.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-deploy-and-test.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=0d5dd74ed5ea325260e58d31e2d494d0 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-deploy-and-test.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=a7343e6de958beb7b7af0faf6b37a9b2 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-deploy-and-test.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=92db95a01f49d81bc70e25b57ce43e5a 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-deploy-and-test.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=1a45805f12cba7b72c10bf398855901d 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-deploy-and-test.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ba894c85cb46e69a464ad5682cbd1225 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-deploy-and-test.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=58baae84512b9f6a9e80e53b2dd9e445 2500w" />
</Frame>

You should see it log the current and desired replicas, and the current state of the container group. Then, if you've
configured everything correctly, you should see the desired changes reflected in your SaladCloud Container Group.

The final step is adding a trigger for our lambda. We're going to use a CloudWatch Event, which will trigger our lambda
based on a schedule. We're going to set it to run every 5 minutes.

<Frame caption="Creating a new CloudWatch Event">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-add-trigger.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=472307ce96fa32bbdb7f472ed958f5e9" alt="Creating a new CloudWatch Event" data-og-width="1145" width="1145" data-og-height="376" height="376" data-path="container-engine/images/sqs-lambda-add-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-add-trigger.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=4014fc2bc324c0923e6b6321218c8210 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-add-trigger.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ef1b11e42af4418c449e383624e416b1 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-add-trigger.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=443b59743fbce78e6fef72381fd760fc 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-add-trigger.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=922f252c96f6aadaa878b3f99783998a 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-add-trigger.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=fcf1512a2722099b79b7946b332d8a54 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-add-trigger.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=4a069d47dbba589a1f3808aedd8f8e4a 2500w" />
</Frame>

<Frame caption="Setting the schedule">
  <img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-configure-trigger.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=855274adf61ed0335139e0225ec9e5d8" alt="Setting the schedule" data-og-width="1653" width="1653" data-og-height="778" height="778" data-path="container-engine/images/sqs-lambda-configure-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-configure-trigger.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=7fdb93d13ba9e9204278f364ad75b48e 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-configure-trigger.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=2d316e778b8ca925252e92b04ad2d59f 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-configure-trigger.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=c302aff63585ab15dce1d55f6ea75b5e 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-configure-trigger.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=8b5dd3beca60747b1aa87567f168a4d0 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-configure-trigger.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=bb40f2000ef60b61d2ad9c6aecc27fe2 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/sqs-lambda-configure-trigger.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ca4d59c40020e8a32acc5a6c8867a209 2500w" />
</Frame>

## Conclusion

In this guide, we've built a simple worker application that processes jobs from an SQS queue, and we've deployed it to
SaladCloud. We've also implemented autoscaling for our worker using a scheduled Lambda function, so that it can
automatically scale up and down based on the number of messages in the queue.
