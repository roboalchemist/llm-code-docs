# Source: https://docs.confluent.io/kafka/get-started.md

<a id="get-started-ak"></a>

# Get Started with Kafka

Apache KafkaÂ® is an open-source distributed streaming system used for stream processing,
real-time data pipelines, and data integration at scale.

This topic provides some links to help you get started using Kafka either on your local computer or in the cloud.

For more about what Kafka is, see [Introduction to Apache Kafka](introduction.md#kafka-intro).
If you want to learn more about how Kafka is designed, and the various architecture decisions that went into designing Kafka, see the [Kafka Design Overview](design/index.md#design-overview) section.

<!-- WARNING: THIS IS A SHARED FILE AND THE SOURCE IS LOCATED IN DOCS-COMMON. DO NOT ADD TO ANY OTHER REPO. -->

## Quick start options

There are numerous ways to get started using Kafka. You can:

- Use Confluent Cloud. Confluent Cloud is the fully managed Kafka service that Confluent provides.
  With Confluent Cloud, you can run Kafka on the cloud provider of your choice; no downloads required. To get started, see
  the [Quick Start for Confluent Cloud](/cloud/current/get-started/index.html).

  This quick start provides steps using the Confluent Cloud Console, the Confluent CLI or REST APIs to create a cluster, topics and move data through the topics.
  When you use Confluent Cloud, some of the Kafka concerns are abstracted away for you, and you wonât need specialized hardware.
  It is [free to get started](/cloud/current/get-started/free-trial.html)  with Confluent Cloud.
- Download and run Confluent Platform on your computer, particularly if your use cases require that you use Kafka
  on-premises. You have a couple of choices:
  - Use the [Confluent Platform CLI Quick Start](https://developer.confluent.io/quickstart/kafka-local/).
    Confluent Platform is an enterprise-ready platform that completes Kafka with advanced capabilities designed to help
    accelerate application development and connectivity.  This quick start walks you through the steps to download and run Kafka as a part of Confluent Platform.
    You will create topics and a producer and consumer, all using a command-line interface.
  - Use the [Confluent Platform Quick Start (with Control Center)](/platform/current/platform-quickstart.html#quick-start-for-cp).
    Confluent Platform is an enterprise-ready platform that completes Kafka. This quick start that features Confluent Control Center (Legacy), a web-based UI and one of Confluent Platformâs commercial features.
    The quick start walks you through the steps to download and run Kafka as a part of Confluent Platform,
    and you will create topics and a producer with Control Center (Legacy).

  To understand the relationship between Confluent Platform and Kafka, see [Kafka Basics on Confluent Platform](/platform/current/kafka/kafka-basics.html)
  and [Confluent Platform License Types](/platform/current/installation/license.html#license-types).
- Download and run the latest Kafka release from the Kafka site.
  The [Apache Quick Start](https://developer.confluent.io/quickstart/kafka-local/) walks you through the steps to run Kafka using Docker, creating
  a topic, and producing to and consuming from that topic.

## Related content

- [Introduction to Apache Kafka](introduction.md#kafka-intro)
- [Kafka Design Overview](design/index.md#design-overview)
- [Kafka Basics on Confluent Platform](/platform/current/kafka/kafka-basics.html)
- [Learn the Basics of Apache Kafka](https://developer.confluent.io/tutorials/#learn-the-basics)
- [Confluent Cloud Examples](/cloud/current/get-started/tutorials/index.html)
- [Confluent Cloud Console](/cloud/current/get-started/cloud-basics.html)
