# Source: https://docs.salad.com/container-engine/how-to-guides/job-processing/rabbitmq.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# RabbitMQ and SaladCloud

> Managing Long-Running Tasks on SaladCloud with RabbitMQ

*Last Updated: November 06, 2025*

# Managing Long-Running Tasks on SaladCloud with RabbitMQ

Managing long running tasks, such as molecular simulations, LoRA training, and LLM finetuning, presents unique
challenges on SaladCloud, due primarily to the interruptible nature of nodes. At the core of all solutions to this
problem are a job queue, and progress checkpoints. The job queue is responsible for distributing tasks to workers, and
detecting when a worker has been interrupted. Workloads should save checkpoints of their progress and upload it to cloud
storage, so that they can be resumed from the last checkpoint in the event of an interruption. Workers should also
upload completed artifacts to cloud storage.

<Frame caption="Basic architecture for long-running tasks on SaladCloud">
  <img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=0aecbde9d765a2712eb7293c4e0d2466" alt="Basic Architecture" data-og-width="2719" width="2719" data-og-height="1275" height="1275" data-path="container-engine/images/lrt-basic-arch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=3d0b91baef22a492d5a7c48971b3f95c 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=3c02fb0e88ba714b93aafce5e2c3b864 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=8c04940f12b79accdb53fbbfde12c341 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=a19ee1a0a51acce431a99ab7da564acc 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=c5fc29cc18ef306cd484c4102768d7c7 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/lrt-basic-arch.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=39a8fed8ff7194c233e20d4199d36514 2500w" />
</Frame>

We will be using [RabbitMQ](https://www.rabbitmq.com/) hosted on [CloudAMQP](https://www.cloudamqp.com/) as our job
queue, and [Cloudflare R2](https://www.cloudflare.com/developer-platform/products/r2/), an S3-compatible object storage
service, as our cloud storage. We prefer R2 to AWS S3 for many SaladCloud workloads, because R2 does not charge for
egress data, and SaladCloud's distributed nodes are not in datacenters, and therefore may incur egress fees from other
providers. Instrumenting your code to use S3-compatible storage will make it easier to switch storage providers in the
future if you choose to do so.

For this guide, we will build an application that slowly calculates a sum for *n* steps, sleeping for 30 seconds between
steps to simulate work. We will set up a job queue and related resources, a storage bucket, a checkpoint saving system,
and a simple auto-scaling mechanism.

You will need a CloudAMQP account, and a Cloudflare account to follow this guide.

## The Job Queue: RabbitMQ

RabbitMQ is a highly configurable open-source message broker that implements the Advanced Message Queuing Protocol
(AMQP) and has client libraries in many languages. It is a robust and scalable solution for job queues, and is widely
used in the industry. You can self-host if desired, but for this guide we will be using CloudAMQP's hosted RabbitMQ
service.

### Relevant Limitations

* While RabbitMQ itself has no such inherent limitations, The "Sassy Squirrel" plan we'll be using on CloudAMQP supports
  a maximum of 1.5k connections, and up to 500 messages per second. This will be more than sufficient for this guide,
  where we will only be scaling up to 250 workers.
* Maximum message size is 512MB, and further limited by the amount of RAM available on the host machine, as messages are
  held in memory, with optional persistence. The default max message size on CloudAMQP is 128MB. As is true for most job
  queues, it is recommended to keep large amounts of data in cloud storage, putting only references to the data location
  in the message itself.
* CloudAMQP's default message timeout is 2 hours, but we can disable this limit entirely, allowing for extremely
  long-running tasks.
* RabbitMQ relies on long-lived connections between the message broker and clients, so it is important to handle
  reconnections gracefully in your code.
* Using RabbitMQ in python in a multi-threaded environment can be a little tricky, however it is required in order to
  support long lived jobs and quick interruption detection. We will be using the `pika` library, which does have support
  for threaded workers.

### Setting Up RabbitMQ on CloudAMQP

Once you have your account on CloudAMQP, it's time to deploy a new instance. We will be using the "Sassy Squirrel" plan
for this guide, which is \$50/month (billed by the second). You can choose a different plan if you need more or less
resources.

<Frame caption="Creating a new instance on CloudAMQP">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-1.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=bc0618a1fc712988aca6c3b89493881b" alt="Creating a new instance on CloudAMQP" data-og-width="1341" width="1341" data-og-height="840" height="840" data-path="container-engine/images/rabbitmq-create-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-1.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=73873054eb496ac488e98b62a5f17abb 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-1.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=b2057461f9d85efbf7de4681780f8a66 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-1.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=59d9b928ee74a267a96f3d6230ac6354 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-1.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=6aa6d46fc3fa41f61199650989295cac 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-1.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=de74c1c54f3353544ed6673dd73967e8 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-1.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=c79d0116e45359975373c1b873a81e7e 2500w" />
</Frame>

Next, you can choose the datacenter and region for your instance. We will be using DigitalOcean's New York 3 datacenter
for this guide, but if you have other application components (besides the worker) in a different cloud, you should
consider deploying the broker to the same cloud and region as your other components.

<Frame caption="Choosing a Datacenter and Region">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-2.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=0c2e762fa0ce6021703992af6b3d0fba" alt="Choosing a datacenter and region" data-og-width="1314" width="1314" data-og-height="759" height="759" data-path="container-engine/images/rabbitmq-create-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-2.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=479893ffb484316e0b8d2d879ddd6f85 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-2.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=cec0d6b50d29419eecb9ee9d346d2bf8 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-2.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=d6ffa435d2ff2ca4ddf28361775a8d27 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-2.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=a29fac80bba5c2104e065bfe89100db6 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-2.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=3d2f0472252c1f0a652478a9bface526 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-2.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=9bde957bc311cdd9b2fc87af75879349 2500w" />
</Frame>

Next, select the number of nodes you want to deploy, and the version of RabbitMQ. We will be using a single node, and
the latest version of RabbitMQ (4.0.5 as of the time of this writing)

<Frame caption="Choosing the number of nodes and RabbitMQ version">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-3.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=4c3a3f45b538c75c066b7eb2319c2935" alt="Choosing the number of nodes and RabbitMQ version" data-og-width="1306" width="1306" data-og-height="739" height="739" data-path="container-engine/images/rabbitmq-create-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-3.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=a7a9204deee2327f8a201936a7e50da4 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-3.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=978df0eec3edc2788e3eaff8a0ffc808 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-3.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=4ec3fd3069091e9b1b1b85a6e2747b11 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-3.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=23247f53547f1ad028c49e3092e61086 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-3.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=30343e1dce23770c81be4d925c458a85 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-3.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=7904ec65f6bae7a3fffe816f5cc95bf7 2500w" />
</Frame>

Confirm all of your settings on the next page, and deploy your instance. Once deployed, you should see something like
this on the CloudAMQP console:

<Frame caption="CloudAMQP Console">
  <img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/cloudamqp-console.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=898a32ac56f6523549561656111e664f" alt="CloudAMQP Console" data-og-width="1349" width="1349" data-og-height="273" height="273" data-path="container-engine/images/cloudamqp-console.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/cloudamqp-console.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=398f51391f9babc286ade7dd33370f09 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/cloudamqp-console.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=c7343dd0ed6e9c34adcb9da36f48cb73 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/cloudamqp-console.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=53f9b9d77966150ee99fc02d5863acea 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/cloudamqp-console.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=b5f305c73ee57890cd5dabfd827ed2c7 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/cloudamqp-console.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=40526d0adf8de6d35d14805ee570da28 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/cloudamqp-console.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=86c84bb1c7b3afb71439e703dd7dfa92 2500w" />
</Frame>

Click the name of the instance to pull up the details page. Later, you will need info from this page to connect to your
RabbitMQ instance, but for now, just navigate to the configuration tab on the left-hand navigation bar. Once there,
disable the field labeled `rabbit.consumer_timeout`. This will allow us to have tasks run longer than the default 2-hour
timeout.

<Frame caption="Disabling the consumer timeout">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-disable-consumer-timeout.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=c886da82519abed5ccc8b84d03530de5" alt="Disabling the consumer timeout" data-og-width="1328" width="1328" data-og-height="815" height="815" data-path="container-engine/images/rabbitmq-disable-consumer-timeout.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-disable-consumer-timeout.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=31c16789cf2214736b52392a535f30ad 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-disable-consumer-timeout.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=154a80e1b6a64993f44358a106bd4e4b 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-disable-consumer-timeout.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=36b4cc13a6318a7303bb018807b60375 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-disable-consumer-timeout.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=f82b2f93f34fd030725c18b3ce8c6756 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-disable-consumer-timeout.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=3976cdd35a1c3b54a368c40284d2e6a6 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-disable-consumer-timeout.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=43c961196989b75e9699030e6ae54a3c 2500w" />
</Frame>

Save your changes when done, and then navigate to the "RabbitMQ Manager", which will open a new tab. The RabbitMQ
Manager is a web interface for managing your RabbitMQ instance. You can view queues, exchanges, and other RabbitMQ
objects, as well as publish and consume messages. There is an HTTP API for this management layer, but for this guide we
will be using the web interface.

<Frame caption="RabbitMQ Manager">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-manager.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=44180afbef771a767b9a042e6169c75c" alt="RabbitMQ Manager" data-og-width="1693" width="1693" data-og-height="811" height="811" data-path="container-engine/images/rabbitmq-manager.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-manager.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=330901a04e8153b2b689e413c13f8400 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-manager.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=36f58891a4caed538fca686fc283c923 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-manager.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=f9ee6031be947d372ee06e3ab0bd8126 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-manager.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=c0ad11dde2489ff2c6a1f59854ed4645 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-manager.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=341044b6f42c7cdcfe262beb34b7eee5 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-manager.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=56f690cc70cf124b972c3f4c6fb57898 2500w" />
</Frame>

### Deadletter Exchange

A deadletter exchange is an exchange that messages are sent to when they are rejected by a queue. This can happen when a
message is not acknowledged by a consumer, typically indicating that the consumer has gone offline, or the message is
malformed.

We will be creating a deadletter exchange and queue first, so that we can configure our main queue to send messages to
it when they are rejected. This will allow us to inspect and requeue messages that have failed to be processed.

From the RabbitMQ Manager, navigate to the Exchanges tab, and add a new exchange called "deadletter".

<Frame caption="Adding a deadletter exchange">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-deadletter-exchange.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=2a3687cd9c1578aa762ca71887b8dc0d" alt="Adding a deadletter exchange" data-og-width="679" width="679" data-og-height="319" height="319" data-path="container-engine/images/rabbitmq-create-deadletter-exchange.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-deadletter-exchange.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=936fce93832dd96b72bb54754c14e073 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-deadletter-exchange.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=6831531b6e941d67bc9f86348ccd09c0 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-deadletter-exchange.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=9b359e72dfacf4dbe1ed102ea1c27855 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-deadletter-exchange.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=fc47620783dba430da9dbdc56b91eeb4 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-deadletter-exchange.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=aec56e43add50ba4f1873d7e0ec354e4 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-deadletter-exchange.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=5246e30dea887492ad030691ecc6a2d5 2500w" />
</Frame>

Make sure to select the non-root virtual host, and set the type to "direct."

Next, navigate to the Queues tab, and add a new queue called "deadletter". Make sure to select the same virtual host as
the exchange.

<Frame caption="Adding a deadletter queue">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-deadletter-queue.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=a950b71574f474cc5cb9556a16264921" alt="Adding a deadletter queue" data-og-width="769" width="769" data-og-height="337" height="337" data-path="container-engine/images/rabbitmq-create-deadletter-queue.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-deadletter-queue.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=9568231eb32e7b97666e9ac1661b9e15 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-deadletter-queue.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=660b6372e3b4d4df906171adaf482b5e 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-deadletter-queue.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=499018974d6528ea8e4c5fc328d5aa87 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-deadletter-queue.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=f773a9d0d7d5c653fb762c420ec573c2 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-deadletter-queue.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=6d78dcafa32dace83e8ae27821cf4843 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-deadletter-queue.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=2df76cb2648aa01d6049d9dd0b10bf43 2500w" />
</Frame>

Once the queue is created, click on it in the list of queues, and create a binding from the deadletter exchange to the
deadletter queue. This will ensure that messages sent to the deadletter exchange are routed to the deadletter queue.

<Frame caption="Binding the deadletter exchange to the deadletter queue">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-bind-dlq.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=f9df766500c3c74cf51ceaa5c7ec82ea" alt="Binding the deadletter exchange to the deadletter queue" data-og-width="751" width="751" data-og-height="348" height="348" data-path="container-engine/images/rabbitmq-bind-dlq.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-bind-dlq.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=08d405edac60553e1c8eca248b0cb27d 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-bind-dlq.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=7d10de16682f31ec00b576f14592c7f2 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-bind-dlq.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=56e57dd098765dd36085b8d430c879d9 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-bind-dlq.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=6eede696845f8dfc4ae55fc4a0caf7fe 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-bind-dlq.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=d687f4855d7557e91e4ee72a8fd94da4 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-bind-dlq.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=2b39b7ba3ceaf55602089b7eb6c2bd4e 2500w" />
</Frame>

### Main Job Queue

Next, we will create the main job queue. This queue will hold messages that represent tasks to be processed by workers.
Navigate back to the Queues tab, and add a new Quorum queue called "my-job-queue", and set the deadletter exchange to
the exchange we created earlier, and setting the delivery limit to 3. This will allow a message to be retried 3 times
before being sent to the deadletter exchange.

<Frame caption="Creating the main job queue">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-queue.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=1b8f1152d7dc08f54d1991cf16d3a968" alt="Creating the main job queue" data-og-width="955" width="955" data-og-height="613" height="613" data-path="container-engine/images/rabbitmq-create-queue.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-queue.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=0871a085ea6fe00493a969d2944fbaaf 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-queue.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=243e27a9fb72d494c2cf8ba2e64c2fc2 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-queue.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=b6f6116c9049b06cd58eee026a27de7b 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-queue.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=9a666c5a854f22ec1e8a2b12c72ebc2a 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-queue.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=40af5f49a8c8a05d2ec6cee33187981c 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-create-queue.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=538b6998fa6cd619ad649861702b8ca1 2500w" />
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

We're going to use the `boto3` library to interact with R2, and the `pika` library to interact with RabbitMQ. You can
install it with `pip install boto3 pika`.

First, we need to set up our environment variables. All of the following environment variables will be needed by the
application code.

There are several ways to do this, but what I've done for my development environment is create a file called
`worker.env` in the root of my project, and add the following lines:

```shell  theme={null}
AMQP_URL=amqps://your-username:your-password@your-hostname/your-vhost
JOB_QUEUE=my-job-queue
R2_AWS_ACCESS_KEY_ID=your-access-key-id
R2_AWS_SECRET_ACCESS_KEY=your-secret-access-key
R2_S3_ENDPOINT_URL=your-s3-endpoint-url
R2_BUCKET_NAME=your-bucket-name
```

Then, to source this into my environment when I run my code, I run the following command:

```shell  theme={null}
export $(grep -v '^#' worker.env | xargs -d '\n')
```

Make sure `*.env` is in your .gitignore. You don't want to commit your secrets to your repository.

Now, create a file called `main.py` in the root of your project, and add the following code:

```python  theme={null}
import os
import boto3
import pika
import json
import time
import threading
import functools

# Get the environment variables
r2_aws_region = "auto"
r2_aws_access_key_id = os.getenv('R2_AWS_ACCESS_KEY_ID')
r2_aws_secret_access_key = os.getenv('R2_AWS_SECRET_ACCESS_KEY')
r2_s3_endpoint_url = os.getenv('R2_S3_ENDPOINT_URL')
r2_bucket_name = os.getenv('R2_BUCKET_NAME')

amqp_url = os.getenv('AMQP_URL')
job_queue = os.getenv('JOB_QUEUE')

machine_id = os.getenv('SALAD_MACHINE_ID')

# Create the R2 client
r2 = boto3.client('s3',
                  aws_access_key_id=r2_aws_access_key_id,
                  aws_secret_access_key=r2_aws_secret_access_key,
                  region_name=r2_aws_region,
                  endpoint_url=r2_s3_endpoint_url)
```

Next, let's take a look at the "work" function, where we will do the actual work for the job. This function will
simulate work by sleeping for 30 seconds and incrementing the step and sum in the checkpoint, and saving that checkpoint
to R2.

```python  theme={null}
cancel_signal = threading.Event()


def do_the_actual_work(job: dict, checkpoint: dict) -> int | None:
    '''
    Do the actual work for the job. This function will simulate work by
    sleeping for 30 seconds and incrementing the step and sum in the
    checkpoint.

    Parameters:
    - job: dict, the job
    - checkpoint: dict, the checkpoint
    '''
    global cancel_signal
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

Additionally, we may want a function that validates the job before starting work on it. In our simple example, we'll
just make sure the basic fields are present.

```python  theme={null}
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
```

We also want functions to upload and download our progress checkpoints, and to upload the result. In this simplified
example, we're going to use a small JSON file for the checkpoint, but the principle is the same no matter what the
actual checkpoint is.

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

We also are going to make helper functions for acknowledging and rejecting messages from the queue.

```python  theme={null}
def ack_message(channel, delivery_tag):
    '''
    Acknowledge the message, indicating that it has been processed successfully
    '''
    if channel.is_open:
        channel.basic_ack(delivery_tag)
    else:
        # Channel is already closed, so we can't ack this message;
        print("Channel is closed, message not acked")


def nack_message(channel, delivery_tag, requeue=True):
    '''
    Reject the message, indicating that it has not been processed successfully
    '''
    if channel.is_open:
        channel.basic_nack(delivery_tag, requeue=requeue)
    else:
        # Channel is already closed, so we can't nack this message;
        print("Channel is closed, message not nacked")
```

Now, we put these parts together in a function called `process_job`.

```python  theme={null}
def process_job(channel, delivery_tag, body):
    job = json.loads(body)
    print(f"Received job {job['job_id']}", flush=True)

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
        cb = functools.partial(nack_message, channel, delivery_tag, False)
        if channel.is_open:
            channel.connection.add_callback_threadsafe(cb)
        return

    # Now we can do the actual work
    try:
        result = do_the_actual_work(job, checkpoint)
    except Exception as e:
        print(f"Error in job {job['job_id']}: {str(e)}")
        cb = functools.partial(nack_message, channel, delivery_tag)
        if channel.is_open:
            channel.connection.add_callback_threadsafe(cb)
        return

    if result is None:
        # Job was interrupted
        cb = functools.partial(nack_message, channel, delivery_tag)
        if channel.is_open:
            channel.connection.add_callback_threadsafe(cb)
        return

    # Upload the result and ack the message
    upload_result(job['job_id'], result)
    cb = functools.partial(ack_message, channel, delivery_tag)
    if channel.is_open:
        channel.connection.add_callback_threadsafe(cb)
```

Now, because we need to run our long-running task in a separate thread from the rabbitmq client, we need a function that
spawns that worker thread for us.

```python  theme={null}
def on_message(channel, method_frame, header_frame, body, args):
    threads = args
    delivery_tag = method_frame.delivery_tag
    t = threading.Thread(target=process_job, args=(
        channel, delivery_tag, body))
    t.start()
    threads.append(t)
```

Finally, we need to connect to RabbitMQ and start consuming messages from the queue, taking care to handle all sorts of
connection errors that may arise.

```python  theme={null}
if __name__ == "__main__":
    # We will be doing all of our work in separate threads, so that rabbitmq's heartbeat
    # can be properly handled.
    threads = []
    while True:
        try:
            # Create the connection and channel, heartbeating every 30 seconds.
            connection = pika.BlockingConnection(
                pika.URLParameters(amqp_url + "?heartbeat=30"))
            channel = connection.channel()

            # We only want 1 job at a time per worker
            channel.basic_qos(prefetch_count=1)

            # Start consuming the messages
            on_message_callback = functools.partial(
                on_message, args=(threads)
            )
            channel.basic_consume(
                queue=job_queue, on_message_callback=on_message_callback, consumer_tag=machine_id)
            channel.start_consuming()
        # Don't recover if connection was closed by broker
        except pika.exceptions.ConnectionClosedByBroker:
            print("Connection closed by broker")
            break
        # Don't recover on channel errors
        except pika.exceptions.AMQPChannelError as e:
            print("Channel error")
            print(str(e))
            break
        # Recover on all other connection errors
        except pika.exceptions.AMQPConnectionError as e:
            print("Connection error, retrying...")
            print(str(e))
            time.sleep(1)
            continue
        except KeyboardInterrupt:
            print("Keyboard interrupt")
            channel.stop_consuming()
            break
        except Exception as e:
            print(f"Error: {str(e)}")
            break

    cancel_signal.set()
    print("Exiting")
    for thread in threads:
        thread.join()
    connection.close()
```

#### Completed Example

```python  theme={null}
import os
import boto3
import pika
import json
import time
import threading
import functools

# Get the environment variables
r2_aws_region = "auto"
r2_aws_access_key_id = os.getenv('R2_AWS_ACCESS_KEY_ID')
r2_aws_secret_access_key = os.getenv('R2_AWS_SECRET_ACCESS_KEY')
r2_s3_endpoint_url = os.getenv('R2_S3_ENDPOINT_URL')
r2_bucket_name = os.getenv('R2_BUCKET_NAME')

amqp_url = os.getenv('AMQP_URL')
job_queue = os.getenv('JOB_QUEUE')

machine_id = os.getenv('SALAD_MACHINE_ID')

# Create the R2 client
r2 = boto3.client('s3',
                  aws_access_key_id=r2_aws_access_key_id,
                  aws_secret_access_key=r2_aws_secret_access_key,
                  region_name=r2_aws_region,
                  endpoint_url=r2_s3_endpoint_url)


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


cancel_signal = threading.Event()


def do_the_actual_work(job: dict, checkpoint: dict) -> int | None:
    '''
    Do the actual work for the job. This function will simulate work by
    sleeping for 30 seconds and incrementing the step and sum in the
    checkpoint.

    Parameters:
    - job: dict, the job
    - checkpoint: dict, the checkpoint
    '''
    global cancel_signal
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


def ack_message(channel, delivery_tag):
    '''
    Acknowledge the message, indicating that it has been processed successfully
    '''
    if channel.is_open:
        channel.basic_ack(delivery_tag)
    else:
        # Channel is already closed, so we can't ack this message;
        print("Channel is closed, message not acked")


def nack_message(channel, delivery_tag, requeue=True):
    '''
    Reject the message, indicating that it has not been processed successfully
    '''
    if channel.is_open:
        channel.basic_nack(delivery_tag, requeue=requeue)
    else:
        # Channel is already closed, so we can't nack this message;
        print("Channel is closed, message not nacked")


def process_job(channel, delivery_tag, body):
    job = json.loads(body)
    print(f"Received job {job['job_id']}", flush=True)

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
        cb = functools.partial(nack_message, channel, delivery_tag, False)
        if channel.is_open:
            channel.connection.add_callback_threadsafe(cb)
        return

    # Now we can do the actual work
    try:
        result = do_the_actual_work(job, checkpoint)
    except Exception as e:
        print(f"Error in job {job['job_id']}: {str(e)}")
        cb = functools.partial(nack_message, channel, delivery_tag)
        if channel.is_open:
            channel.connection.add_callback_threadsafe(cb)
        return

    if result is None:
        # Job was interrupted
        cb = functools.partial(nack_message, channel, delivery_tag)
        if channel.is_open:
            channel.connection.add_callback_threadsafe(cb)
        return

    # Upload the result and ack the message
    upload_result(job['job_id'], result)
    cb = functools.partial(ack_message, channel, delivery_tag)
    if channel.is_open:
        channel.connection.add_callback_threadsafe(cb)


def on_message(channel, method_frame, header_frame, body, args):
    threads = args
    delivery_tag = method_frame.delivery_tag
    t = threading.Thread(target=process_job, args=(
        channel, delivery_tag, body))
    t.start()
    threads.append(t)


if __name__ == "__main__":
    # We will be doing all of our work in separate threads, so that rabbitmq's heartbeat
    # can be properly handled.
    threads = []
    while True:
        try:
            # Create the connection and channel, heartbeating every 30 seconds.
            connection = pika.BlockingConnection(
                pika.URLParameters(amqp_url + "?heartbeat=30"))
            channel = connection.channel()

            # We only want 1 job at a time per worker
            channel.basic_qos(prefetch_count=1)

            # Start consuming the messages
            on_message_callback = functools.partial(
                on_message, args=(threads)
            )
            channel.basic_consume(
                queue=job_queue, on_message_callback=on_message_callback, consumer_tag=machine_id)
            channel.start_consuming()
        # Don't recover if connection was closed by broker
        except pika.exceptions.ConnectionClosedByBroker:
            print("Connection closed by broker")
            break
        # Don't recover on channel errors
        except pika.exceptions.AMQPChannelError as e:
            print("Channel error")
            print(str(e))
            break
        # Recover on all other connection errors
        except pika.exceptions.AMQPConnectionError as e:
            print("Connection error, retrying...")
            print(str(e))
            time.sleep(1)
            continue
        except KeyboardInterrupt:
            print("Keyboard interrupt")
            channel.stop_consuming()
            break
        except Exception as e:
            print(f"Error: {str(e)}")
            break

    cancel_signal.set()
    print("Exiting")
    for thread in threads:
        thread.join()
    connection.close()
```

## Submitting Jobs to the Queue

Next, we need a way to submit jobs to the queue. We're going to use the `pika` library for this as well, with the same
`AMQP_URL` and `JOB_QUEUE` from `worker.env`. I've saved mine in a file called `submitter.env`, and I'm going to source
them into my environment with the following command:

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

It is pretty straightforward to submit these jobs to the queue. Here's an example script that does just that:

```python  theme={null}
import csv
import json
import pika
import os

amqp_url = os.getenv('AMQP_URL')
job_queue = os.getenv('JOB_QUEUE')

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
    channel = connection.channel()
    with open("data.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            job = {
                "job_id": row["job_id"],
                "steps": int(row["steps"])
            }
            channel.basic_publish(
                exchange='',
                routing_key=job_queue,
                body=json.dumps(job)
            )
            print(f'Job {job["job_id"]} submitted')
    connection.close()
```

### Running the Job Submitter

Run the job submitter with `python submit-jobs.py`. It will read the csv file and submit all the jobs to the queue.

Once that has run, we can see in the RabbitMQ management interface

<Frame caption="RabbitMQ Management Interface showing a full queue">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-10k-messages.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=391934af67c67adc7bf51c9169919013" alt="RabbitMQ Management Interface showing a full queue" data-og-width="978" width="978" data-og-height="306" height="306" data-path="container-engine/images/rabbitmq-10k-messages.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-10k-messages.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=4b52d8da565ee257fedbc205cdb41be2 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-10k-messages.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=3561a164b533b029318f846441fa7c44 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-10k-messages.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=14361a1cc78fdf3897d379cf1aa9e527 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-10k-messages.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=b3b3113bc5dc7a7efc424e838ab0879a 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-10k-messages.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=7ef3573f666667f28895bbc9b704831b 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-10k-messages.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=4d43f5f96b66fd5c7cea825fc42731e7 2500w" />
</Frame>

## Containerize the Worker Application

Now that we have our worker application and our job submitter, we can package our worker in a docker container, and run
it on a SaladCloud Container Group.

First, let's make sure our dependencies are documented in `requirements.txt`.

```shell  theme={null}
boto3
pika
```

Now, create a new file called `Dockerfile`. Our application is simple, so a basic python base image should be fine.

```dockerfile  theme={null}
FROM python:3.10.12-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

CMD ["python", "main.py"]
```

Now, build the docker image, and use a tag that makes sense for you.

```shell  theme={null}
docker build -t saladtechnologies/lrt-worker-examples:rabbitmq .
```

Now, we can test it locally to make sure it works, before we deploy it to SaladCloud.

```shell  theme={null}
docker run -it --rm  --env-file worker.env saladtechnologies/lrt-worker-examples:rabbitmq
```

You should see it start up and begin processing a job. Once this is working, you can go ahead and terminate the
container with `Ctrl+C`.

Now, we can push the image to Docker Hub.

```shell  theme={null}
docker push saladtechnologies/lrt-worker-examples:rabbitmq
```

## Deploying the Worker to SaladCloud

To deploy our worker to SaladCloud, we need to create a new Container Group. This can be done via the API, SDKs, or the
Portal. We're going to use the Portal.

We're going to create a new Container Group, and we're going to use the image we just pushed to Docker Hub. We're going
to request 100 replicas (the max via the portal), and we're going to set all of our environment variables from
`worker.env`.

<Frame caption="Creating a new Container Group">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-1.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=788a83369b498f7edb8af69ce4a7ec41" alt="Creating a new Container Group" data-og-width="704" width="704" data-og-height="850" height="850" data-path="container-engine/images/rabbitmq-cg-create-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-1.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=64223e7af247a6efec6cb64ff2b8f83f 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-1.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=74a5a5d64ee45cbefdb65bc27a0ad6a5 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-1.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=055ba8d6dbb9e240641ef7a05707b660 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-1.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=b47adb65fd67da99f4f45fb359cee60e 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-1.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=5ac0d98e51c6cc0187c12cd4bc05adca 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-1.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=f8938a94d5a3ef1bf3382770fe00b6f0 2500w" />
</Frame>

Our application is extremely simple, so we're going to only request 1 vCPU, 1 GB of RAM, and no GPU. Your hardware
requirements are likely significantly higher than this.

<Frame caption="Setting the hardware requirements">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-2.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=a6e12a31a937c12b0de03d713e844d6f" alt="Setting the hardware requirements" data-og-width="640" width="640" data-og-height="1054" height="1054" data-path="container-engine/images/rabbitmq-cg-create-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-2.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=9fd829b30ec46f7072ea74a508e9f6c3 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-2.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=85130c045494468b6e6eacf9ef0422e8 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-2.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=f6b10ec1fb9db3da50cfb09083b2e52a 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-2.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=eea02ca1d8b49eeec5d06ecf9568e01b 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-2.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=1b937e1214e99747f49e009f41cb9b6d 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-2.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=872124dba8ddf0793a4bcb000eb8fa0f 2500w" />
</Frame>

All CPU-only jobs are prioritized as "Lowest", and we don't need any additional storage for this particular application.

<Frame caption="Setting the job priority and storage requirements">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-3.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=f264406369197b18cd18363a6ccc7715" alt="Setting the job priority and storage requirements" data-og-width="645" width="645" data-og-height="565" height="565" data-path="container-engine/images/rabbitmq-cg-create-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-3.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=36af05427fa5b1e3dc4a85e125b94b5a 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-3.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=28f90a0015e980059c42320363aff9f1 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-3.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=f90cdb3281ecab7fdb8627c7d8607daa 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-3.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=11071214196206337b42f93c22512081 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-3.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=e6960da4d19dfce04250e122c54a01b9 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-create-3.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=3aca73bd56a10669ea26347944b040da 2500w" />
</Frame>

We do not need the container gateway, as our application pulls its work from a queue. We also do not need health probes,
as those are primarily for services accessed via Container Gateway. Go ahead and hit deploy, and you'll be taken to the
container group page, where you can see its status.

First, it will prepare by pulling the container image into our high-performance cache.

<Frame caption="Preparing the container">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-preparing.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=c36b6121c11c49400064f4ac4b437a0d" alt="Preparing the container" data-og-width="1203" width="1203" data-og-height="483" height="483" data-path="container-engine/images/rabbitmq-cg-preparing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-preparing.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=1e45e32f8c7bc1d5d9a4b4e53af0b68e 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-preparing.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=3b11b1402b980b2d39d520084529ef70 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-preparing.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=01acf28f1448270ba8941537d6c71d15 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-preparing.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=53f5ce09163171e65794fba9fa3f4e7b 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-preparing.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=b59793f28bd168aa8f9f3a34f053f610 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-preparing.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=b451471459018782296ef91e097e6008 2500w" />
</Frame>

Once it's prepared, it will start allocating replicas, and downloading the container image to those replicas.

<Frame caption="Downloading the images to the replicas">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-deploying.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=8c9cf6bda84c88b6c5f83a90d489f52d" alt="Downloading the images to the replicas" data-og-width="1213" width="1213" data-og-height="1025" height="1025" data-path="container-engine/images/rabbitmq-cg-deploying.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-deploying.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=9bfe30bf5c1a2e491a7946f8c7e01e7e 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-deploying.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=b93558856074f39269b7d5f812c49d40 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-deploying.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=7ba50e343c1e47aead7ba3109b172f41 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-deploying.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=32faa5c63aef5faad4a18dc2027ed1bd 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-deploying.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=4d5953efb96bef98c03fe2c526fcbab3 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-deploying.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=136855859018374e2fec1e44ae521d24 2500w" />
</Frame>

After a minute or so, we should see our instances up and running.

<Frame caption="Instances up and running">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-running.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=c4a83944d0d97164e85391691a939585" alt="Instances up and running" data-og-width="1221" width="1221" data-og-height="1013" height="1013" data-path="container-engine/images/rabbitmq-cg-running.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-running.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=f90a8f91e6d4c9389dc0d25f4a2da848 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-running.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=db52af0e25a4acdea754be6548708a53 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-running.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=b3a37c0785d4b5dabbb768b19c136714 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-running.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=86d7b8323db239b39f796e15a89e2937 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-running.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=d595a6dc193ed6933472102af639fef2 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-cg-running.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=de45ac137780e891c2846a6a65e2479a 2500w" />
</Frame>

## Validating That It Works

Now that our cluster is up and running, we can go to the RabbitMQ management console, and see that we have in-flight
messages now.

<Frame caption="In-flight messages in our queue">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-messages-in-flight.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=8162b91b1c4e7c472fd6c4cbbdd57934" alt="In-flight messages in the queue" data-og-width="1013" width="1013" data-og-height="360" height="360" data-path="container-engine/images/rabbitmq-messages-in-flight.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-messages-in-flight.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=e54a52629ad6e9445cd3d2654cb32c75 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-messages-in-flight.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=5efd0716d17912e15f33751bd872c651 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-messages-in-flight.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=3e1a4d2b7e880fbefdc805ea220366e3 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-messages-in-flight.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=742e4fef8706ad4da4a2f371c7731644 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-messages-in-flight.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=2fb5c2c5c875e3a3e09ae97db7454b3e 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-messages-in-flight.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=b15455d9fb0d27d0997b58591eda2f9a 2500w" />
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
(the maximum in the API). To implement this, we're going to use Cloudflare Workers with a schedule trigger.

Navigate to the Cloudflare portal, and select the "Compute (Workers)" tab from the left navigation bar. Click "Create",
and then choose the "Hello World" template. Go ahead and deploy the default, we're going to edit it in the next step.

<Frame caption="Creating a new Worker">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-create.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=667ef5c35f37c54f0db23fd6fd720d68" alt="Creating a new Worker" data-og-width="928" width="928" data-og-height="912" height="912" data-path="container-engine/images/rabbitmq-workers-create.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-create.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=585809fdca87377d98ec0a0a9cf73594 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-create.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=c585ab2f5ed20ce7d161a22bdbe24e24 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-create.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=bf6b7494de5ff5c2d32bfa2a46e72d12 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-create.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=f66bd0987d8609d99f72b45171de0504 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-create.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=63af6e1dda9d63d086731aff80399d31 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-create.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=fcc892a458c42d7b606a540df022877c 2500w" />
</Frame>

Now, we're going to edit the worker code to set the number of replicas to be equal to the number of messages in the
queue. First, we need some helper functions to interact with the
[SaladCloud API](/reference/saladcloud-api/container-groups/get-container-group).

```javascript  theme={null}
const saladBaseUrl = 'https://api.salad.com/api/public'

async function getContainerGroup(org, project, containerGroupName, saladApiKey) {
  const url = `${saladBaseUrl}/organizations/${org}/projects/${project}/containers/${containerGroupName}`
  const resp = await fetch(url, {
    method: 'GET',
    headers: {
      'Salad-Api-Key': saladApiKey,
    },
  })
  if (!resp.ok) {
    throw new Error(`Failed to fetch container group: ${resp.statusText}`)
  }
  return resp.json()
}

async function startContainerGroup(org, project, containerGroupName, saladApiKey) {
  console.log('Starting container group')
  const url = `${saladBaseUrl}/organizations/${org}/projects/${project}/containers/${containerGroupName}/start`
  const resp = await fetch(url, {
    method: 'POST',
    headers: {
      'Salad-Api-Key': saladApiKey,
    },
  })
  if (!resp.ok) {
    throw new Error(`Failed to start container group: ${resp.statusText}`)
  }
}

async function stopContainerGroup(org, project, containerGroupName, saladApiKey) {
  console.log('Stopping container group')
  const url = `${saladBaseUrl}/organizations/${org}/projects/${project}/containers/${containerGroupName}/stop`
  const resp = await fetch(url, {
    method: 'POST',
    headers: {
      'Salad-Api-Key': saladApiKey,
    },
  })
  if (!resp.ok) {
    throw new Error(`Failed to stop container group: ${resp.statusText}`)
  }
}

async function setReplicas(org, project, containerGroupName, replicas, saladApiKey) {
  console.log(`Setting replicas to ${replicas}`)
  const url = `${saladBaseUrl}/organizations/${org}/projects/${project}/containers/${containerGroupName}`
  const resp = await fetch(url, {
    method: 'PATCH',
    headers: {
      'Salad-Api-Key': saladApiKey,
      'Content-Type': 'application/merge-patch+json',
    },
    body: JSON.stringify({ replicas }),
  })
  if (!resp.ok) {
    throw new Error(`Failed to set replicas: ${resp.statusText}`)
  }
}
```

Next, we need a helper function to get metadata about the queue, including the number of messages it contains. This can
be done via the RabbitMQ Management API.

```javascript  theme={null}
async function getQueueInfo(baseUrl, username, password, vHost, queueName) {
  const url = `${baseUrl}/api/queues/${vHost}/${queueName}`
  const resp = await fetch(url, {
    method: 'GET',
    headers: {
      Authorization: `Basic ${btoa(`${username}:${password}`)}`,
    },
  })
  if (!resp.ok) {
    throw new Error(`Failed to fetch queue info: ${resp.statusText}`)
  }
  return resp.json()
}
```

Now, we can put it all together in a `scheduled` event listener. Note all of the values that we will provide via
environment variables.

```javascript  theme={null}
export default {
  async scheduled(event, env, ctx) {
    const {
      min_replicas,
      max_replicas,
      org,
      project,
      container_group_name,
      salad_api_key,
      rabbitmq_url,
      rabbitmq_username,
      rabbitmq_password,
      vhost,
      queue_name,
    } = env

    const queueInfo = await getQueueInfo(rabbitmq_url, rabbitmq_username, rabbitmq_password, vhost, queue_name)
    const numMessages = queueInfo.messages
    console.log(`Queue ${queue_name} has ${numMessages} messages`)

    const desiredReplicas = Math.min(Math.max(parseInt(min_replicas), numMessages), parseInt(max_replicas))

    const containerGroup = await getContainerGroup(org, project, container_group_name, salad_api_key)
    const currentReplicas = containerGroup.replicas
    const currentState = containerGroup.current_state.status
    console.log(
      `Current replicas: ${currentReplicas}, current state: ${currentState}, desired replicas: ${desiredReplicas}`,
    )
    if (currentState === 'stopped' && desiredReplicas > 0) {
      await startContainerGroup(org, project, container_group_name, salad_api_key)
    }
    if (currentState === 'running' && desiredReplicas === 0) {
      await stopContainerGroup(org, project, container_group_name, salad_api_key)
    }
    if (currentReplicas !== desiredReplicas) {
      await setReplicas(org, project, container_group_name, desiredReplicas, salad_api_key)
    }
  },
}
```

Click Deploy, and find your way to the settings tab for the worker function. Here, we are going to disable the domains
and routes that point to our function, since it doesn't even have an http handler. We will also fill in all of the
environment variables that we used in our function. Make sure to use the type "Secret" for sensitive values like your
rabbitmq password and your Salad API key.

<Frame caption="Disabling the domains and routes, and setting the environment variables">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-settings.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=5a3de001e8654b3f4c4bdc103c2654d7" alt="Disabling the domains and routes" data-og-width="1056" width="1056" data-og-height="979" height="979" data-path="container-engine/images/rabbitmq-workers-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-settings.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=644be9185012da4f75a0214111dffcfc 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-settings.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=5d13d2ff7b1244f9f286a34f6c074ea8 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-settings.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=7983fdd3c0f2db8d7e426b811d29ef7d 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-settings.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=b650310267bed8268c03faca8d201741 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-settings.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=21353d3ef0b7fcb8c3a80f2648663d0d 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-settings.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=22863891dc76432c2c7e49f29e207afd 2500w" />
</Frame>

Finally, we can set a trigger for the function to run every 5 minutes.

<Frame caption="Setting the trigger to run every 5 minutes">
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-trigger.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=da2ed235e2975a906f94033dd0ca21bb" alt="Setting the trigger to run every 5 minutes" data-og-width="763" width="763" data-og-height="230" height="230" data-path="container-engine/images/rabbitmq-workers-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-trigger.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=63f81a82e7e5652d22b65bcbcca29d3b 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-trigger.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=f4324493c1697fd4fa9343e2550d13a8 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-trigger.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=0536468b3fd86f44de2033bc198b6415 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-trigger.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=f04242f362572d1e3e1946ec5eeb0cac 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-trigger.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=8b60b6869556f3eec68e917bed6d3d9c 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/rabbitmq-workers-trigger.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=628ddf9c4cd1673a98c510d7f726bbcb 2500w" />
</Frame>

Now, if we've done everything correctly, we should see our worker scale up and down based on the number of messages in
the queue. You can live-tail the logs via the "Logs" tab in the Cloudflare Workers console, or with the wrangler cli.

### Completed Example

```javascript  theme={null}
const saladBaseUrl = 'https://api.salad.com/api/public'

async function getContainerGroup(org, project, containerGroupName, saladApiKey) {
  const url = `${saladBaseUrl}/organizations/${org}/projects/${project}/containers/${containerGroupName}`
  const resp = await fetch(url, {
    method: 'GET',
    headers: {
      'Salad-Api-Key': saladApiKey,
    },
  })
  if (!resp.ok) {
    throw new Error(`Failed to fetch container group: ${resp.statusText}`)
  }
  return resp.json()
}

async function startContainerGroup(org, project, containerGroupName, saladApiKey) {
  console.log('Starting container group')
  const url = `${saladBaseUrl}/organizations/${org}/projects/${project}/containers/${containerGroupName}/start`
  const resp = await fetch(url, {
    method: 'POST',
    headers: {
      'Salad-Api-Key': saladApiKey,
    },
  })
  if (!resp.ok) {
    throw new Error(`Failed to start container group: ${resp.statusText}`)
  }
}

async function stopContainerGroup(org, project, containerGroupName, saladApiKey) {
  console.log('Stopping container group')
  const url = `${saladBaseUrl}/organizations/${org}/projects/${project}/containers/${containerGroupName}/stop`
  const resp = await fetch(url, {
    method: 'POST',
    headers: {
      'Salad-Api-Key': saladApiKey,
    },
  })
  if (!resp.ok) {
    throw new Error(`Failed to stop container group: ${resp.statusText}`)
  }
}

async function setReplicas(org, project, containerGroupName, replicas, saladApiKey) {
  console.log(`Setting replicas to ${replicas}`)
  const url = `${saladBaseUrl}/organizations/${org}/projects/${project}/containers/${containerGroupName}`
  const resp = await fetch(url, {
    method: 'PATCH',
    headers: {
      'Salad-Api-Key': saladApiKey,
      'Content-Type': 'application/merge-patch+json',
    },
    body: JSON.stringify({ replicas }),
  })
  if (!resp.ok) {
    throw new Error(`Failed to set replicas: ${resp.statusText}`)
  }
}

async function getQueueInfo(baseUrl, username, password, vHost, queueName) {
  const url = `${baseUrl}/api/queues/${vHost}/${queueName}`
  const resp = await fetch(url, {
    method: 'GET',
    headers: {
      Authorization: `Basic ${btoa(`${username}:${password}`)}`,
    },
  })
  if (!resp.ok) {
    throw new Error(`Failed to fetch queue info: ${resp.statusText}`)
  }
  return resp.json()
}

export default {
  async scheduled(event, env, ctx) {
    const {
      min_replicas,
      max_replicas,
      org,
      project,
      container_group_name,
      salad_api_key,
      rabbitmq_url,
      rabbitmq_username,
      rabbitmq_password,
      vhost,
      queue_name,
    } = env

    const queueInfo = await getQueueInfo(rabbitmq_url, rabbitmq_username, rabbitmq_password, vhost, queue_name)
    const numMessages = queueInfo.messages
    console.log(`Queue ${queue_name} has ${numMessages} messages`)

    const desiredReplicas = Math.min(Math.max(parseInt(min_replicas), numMessages), parseInt(max_replicas))

    const containerGroup = await getContainerGroup(org, project, container_group_name, salad_api_key)
    const currentReplicas = containerGroup.replicas
    const currentState = containerGroup.current_state.status
    console.log(
      `Current replicas: ${currentReplicas}, current state: ${currentState}, desired replicas: ${desiredReplicas}`,
    )
    if (currentState === 'stopped' && desiredReplicas > 0) {
      await startContainerGroup(org, project, container_group_name, salad_api_key)
    }
    if (currentState === 'running' && desiredReplicas === 0) {
      await stopContainerGroup(org, project, container_group_name, salad_api_key)
    }
    if (currentReplicas !== desiredReplicas) {
      await setReplicas(org, project, container_group_name, desiredReplicas, salad_api_key)
    }
  },
}
```

## Conclusion

In this guide, we've built a simple worker application that processes jobs from a RabbitMQ queue, and we've deployed it
to SaladCloud. We've also implemented autoscaling for our worker using a scheduled Cloudflare worker function, so that
it can automatically scale up and down based on the number of messages in the queue.
