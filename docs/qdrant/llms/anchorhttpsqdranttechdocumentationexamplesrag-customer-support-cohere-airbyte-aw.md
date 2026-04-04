# [Anchor](https://qdrant.tech/documentation/examples/rag-customer-support-cohere-airbyte-aws/\#question-answering-system-for-ai-customer-support) Question-Answering System for AI Customer Support

| Time: 120 min | Level: Advanced |  |  |
| --- | --- | --- | --- |

Maintaining top-notch customer service is vital to business success. As your operation expands, so does the influx of customer queries. Many of these queries are repetitive, making automation a time-saving solution.
Your support team’s expertise is typically kept private, but you can still use AI to automate responses securely.

In this tutorial we will setup a private AI service that answers customer support queries with high accuracy and effectiveness. By leveraging Cohere’s powerful models (deployed to [AWS](https://cohere.com/deployment-options/aws)) with Qdrant Hybrid Cloud, you can create a fully private customer support system. Data synchronization, facilitated by [Airbyte](https://airbyte.com/), will complete the setup.

![Architecture diagram](https://qdrant.tech/documentation/examples/customer-support-cohere-airbyte/architecture-diagram.png)

## [Anchor](https://qdrant.tech/documentation/examples/rag-customer-support-cohere-airbyte-aws/\#system-design) System design

The history of past interactions with your customers is not a static dataset. It is constantly evolving, as new
questions are coming in. You probably have a ticketing system that stores all the interactions, or use a different way
to communicate with your customers. No matter what is the communication channel, you need to bring the correct answers
to the selected Large Language Model, and have an established way to do it in a continuous manner. Thus, we will build
an ingestion pipeline and then a Retrieval Augmented Generation application that will use the data.

- **Dataset:** a [set of Frequently Asked Questions from Qdrant\\
users](https://qdrant.tech/documentation/faq/qdrant-fundamentals/) as an incrementally updated Excel sheet
- **Embedding model:** Cohere `embed-multilingual-v3.0`, to support different languages with the same pipeline
- **Knowledge base:** Qdrant, running in Hybrid Cloud mode
- **Ingestion pipeline:** [Airbyte](https://airbyte.com/), loading the data into Qdrant
- **Large Language Model:** Cohere [Command-R](https://docs.cohere.com/docs/command-r)
- **RAG:** Cohere [RAG](https://docs.cohere.com/docs/retrieval-augmented-generation-rag) using our knowledge base
through a custom connector

All the selected components are compatible with the [AWS](https://aws.amazon.com/) infrastructure. Thanks to Cohere models’ availability, you can build a fully private customer support system completely isolates data within your infrastructure. Also, if you have AWS credits, you can now use them without spending additional money on the models or
semantic search layer.

### [Anchor](https://qdrant.tech/documentation/examples/rag-customer-support-cohere-airbyte-aws/\#data-ingestion) Data ingestion

Building a RAG starts with a well-curated dataset. In your specific case you may prefer loading the data directly from
a ticketing system, such as [Zendesk Support](https://airbyte.com/connectors/zendesk-support),
[Freshdesk](https://airbyte.com/connectors/freshdesk), or maybe integrate it with a shared inbox. However, in case of
customer questions quality over quantity is the key. There should be a conscious decision on what data to include in the
knowledge base, so we do not confuse the model with possibly irrelevant information. We’ll assume there is an [Excel\\
sheet](https://docs.airbyte.com/integrations/sources/file) available over HTTP/FTP that Airbyte can access and load into
Qdrant in an incremental manner.

### [Anchor](https://qdrant.tech/documentation/examples/rag-customer-support-cohere-airbyte-aws/\#cohere--qdrant-connector-for-rag) Cohere <> Qdrant Connector for RAG

Cohere RAG relies on [connectors](https://docs.cohere.com/docs/connectors) which brings additional context to the model.
The connector is a web service that implements a specific interface, and exposes its data through HTTP API. With that
setup, the Large Language Model becomes responsible for communicating with the connectors, so building a prompt with the
context is not needed anymore.

### [Anchor](https://qdrant.tech/documentation/examples/rag-customer-support-cohere-airbyte-aws/\#answering-bot) Answering bot

Finally, we want to automate the responses and send them automatically when we are sure that the model is confident
enough. Again, the way such an application should be created strongly depends on the system you are using within the
customer support team. If it exposes a way to set up a webhook whenever a new question is coming in, you can create a
web service and use it to automate the responses. In general, our bot should be created specifically for the platform
you use, so we’ll just cover the general idea here and build a simple CLI tool.

## [Anchor](https://qdrant.tech/documentation/examples/rag-customer-support-cohere-airbyte-aws/\#prerequisites) Prerequisites

### [Anchor](https://qdrant.tech/documentation/examples/rag-customer-support-cohere-airbyte-aws/\#cohere-models-on-aws) Cohere models on AWS

One of the possible ways to deploy Cohere models on AWS is to use AWS SageMaker. Cohere’s website has [a detailed\\
guide on how to deploy the models in that way](https://docs.cohere.com/docs/amazon-sagemaker-setup-guide), so you can
follow the steps described there to set up your own instance.

### [Anchor](https://qdrant.tech/documentation/examples/rag-customer-support-cohere-airbyte-aws/\#qdrant-hybrid-cloud-on-aws) Qdrant Hybrid Cloud on AWS

Our documentation covers the deployment of Qdrant on AWS as a Hybrid Cloud Environment, so you can follow the steps described
there to set up your own instance. The deployment process is quite straightforward, and you can have your Qdrant cluster
up and running in a few minutes.

Once you perform all the steps, your Qdrant cluster should be running on a specific URL. You will need this URL and the
API key to interact with Qdrant, so let’s store them both in the environment variables:

shellpython

```shell
export QDRANT_URL="https://qdrant.example.com"
export QDRANT_API_KEY="your-api-key"

```

```python
import os

os.environ["QDRANT_URL"] = "https://qdrant.example.com"
os.environ["QDRANT_API_KEY"] = "your-api-key"

```

### [Anchor](https://qdrant.tech/documentation/examples/rag-customer-support-cohere-airbyte-aws/\#airbyte-open-source) Airbyte Open Source

Airbyte is an open-source data integration platform that helps you replicate your data in your warehouses, lakes, and
databases. You can install it on your infrastructure and use it to load the data into Qdrant. The installation process is described in the [official documentation](https://docs.airbyte.com/deploying-airbyte/).
Please follow the instructions to set up your own instance.

#### [Anchor](https://qdrant.tech/documentation/examples/rag-customer-support-cohere-airbyte-aws/\#setting-up-the-connection) Setting up the connection

Once you have an Airbyte up and running, you can configure the connection to load the data from the respective source
into Qdrant. The configuration will require setting up the source and destination connectors. In this tutorial we will
use the following connectors:

- **Source:** [File](https://docs.airbyte.com/integrations/sources/file) to load the data from an Excel sheet
- **Destination:** [Qdrant](https://docs.airbyte.com/integrations/destinations/qdrant) to load the data into Qdrant

Airbyte UI will guide you through the process of setting up the source and destination and connecting them. Here is how
the configuration of the source might look like:

![Airbyte source configuration](https://qdrant.tech/documentation/examples/customer-support-cohere-airbyte/airbyte-excel-source.png)

Qdrant is our target destination, so we need to set up the connection to it. We need to specify which fields should be
included to generate the embeddings. In our case it makes complete sense to embed just the questions, as we are going
to look for similar questions asked in the past and provide the answers.

![Airbyte destination configuration](https://qdrant.tech/documentation/examples/customer-support-cohere-airbyte/airbyte-qdrant-destination.png)

Once we have the destination set up, we can finally configure a connection. The connection will define the schedule
of the data synchronization.

![Airbyte connection configuration](https://qdrant.tech/documentation/examples/customer-support-cohere-airbyte/airbyte-connection.png)

Airbyte should now be ready to accept any data updates from the source and load them into Qdrant. You can monitor the
progress of the synchronization in the UI.

## [Anchor](https://qdrant.tech/documentation/examples/rag-customer-support-cohere-airbyte-aws/\#rag-connector) RAG connector

One of our previous tutorials, guides you step-by-step on [implementing custom connector for Cohere\\
RAG](https://qdrant.tech/documentation/examples/rag-customer-support-cohere-airbyte-aws/documentation/examples/cohere-rag-connector/) with Cohere Embed v3 and Qdrant. You can just point it to use your Hybrid Cloud
Qdrant instance running on AWS. Created connector might be deployed to Amazon Web Services in various ways, even in a
[Serverless](https://aws.amazon.com/serverless/) manner using [AWS\\
Lambda](https://aws.amazon.com/lambda/?c=ser&sec=srv).

In general, RAG connector has to expose a single endpoint that will accept POST requests with `query` parameter and
return the matching documents as JSON document with a specific structure. Our FastAPI implementation created [in the\\
related tutorial](https://qdrant.tech/documentation/examples/rag-customer-support-cohere-airbyte-aws/documentation/examples/cohere-rag-connector/) is a perfect fit for this task. The only difference is that you
should point it to the Cohere models and Qdrant running on AWS infrastructure.

> Our connector is a lightweight web service that exposes a single endpoint and glues the Cohere embedding model with
> our Qdrant Hybrid Cloud instance. Thus, it perfectly fits the serverless architecture, requiring no additional
> infrastructure to run.

You can also run the connector as another service within your [Kubernetes cluster running on AWS\\
(EKS)](https://aws.amazon.com/eks/), or by launching an [EC2](https://aws.amazon.com/ec2/) compute instance. This step
is dependent on the way you deploy your other services, so we’ll leave it to you to decide how to run the connector.

Eventually, the web service should be available under a specific URL, and it’s a good practice to store it in the
environment variable, so the other services can easily access it.

shellpython

```shell
export RAG_CONNECTOR_URL="https://rag-connector.example.com/search"

```

```python
os.environ["RAG_CONNECTOR_URL"] = "https://rag-connector.example.com/search"

```

## [Anchor](https://qdrant.tech/documentation/examples/rag-customer-support-cohere-airbyte-aws/\#customer-interface) Customer interface

At this part we have all the data loaded into Qdrant, and the RAG connector is ready to serve the relevant context. The
last missing piece is the customer interface, that will call the Command model to create the answer. Such a system
should be built specifically for the platform you use and integrated into its workflow, but we will build the strong
foundation for it and show how to use it in a simple CLI tool.

> Our application does not have to connect to Qdrant anymore, as the model will connect to the RAG connector directly.

First of all, we have to create a connection to Cohere services through the Cohere SDK.

```python
import cohere