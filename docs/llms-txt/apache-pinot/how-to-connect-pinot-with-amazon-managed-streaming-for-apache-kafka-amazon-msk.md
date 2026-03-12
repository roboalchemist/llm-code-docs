# Source: https://docs.pinot.apache.org/release-0.4.0/operators/tutorials/how-to-connect-pinot-with-amazon-managed-streaming-for-apache-kafka-amazon-msk.md

# Source: https://docs.pinot.apache.org/release-0.9.0/operators/tutorials/how-to-connect-pinot-with-amazon-managed-streaming-for-apache-kafka-amazon-msk.md

# Source: https://docs.pinot.apache.org/release-0.10.0/operators/tutorials/how-to-connect-pinot-with-amazon-managed-streaming-for-apache-kafka-amazon-msk.md

# Source: https://docs.pinot.apache.org/release-0.11.0/operators/tutorials/how-to-connect-pinot-with-amazon-managed-streaming-for-apache-kafka-amazon-msk.md

# Source: https://docs.pinot.apache.org/release-0.12.0/operators/tutorials/how-to-connect-pinot-with-amazon-managed-streaming-for-apache-kafka-amazon-msk.md

# Source: https://docs.pinot.apache.org/release-0.12.1/operators/tutorials/how-to-connect-pinot-with-amazon-managed-streaming-for-apache-kafka-amazon-msk.md

# Source: https://docs.pinot.apache.org/release-1.0.0/for-operators/tutorials/how-to-connect-pinot-with-amazon-managed-streaming-for-apache-kafka-amazon-msk.md

# Source: https://docs.pinot.apache.org/release-1.1.0/for-operators/tutorials/how-to-connect-pinot-with-amazon-managed-streaming-for-apache-kafka-amazon-msk.md

# Source: https://docs.pinot.apache.org/release-1.2.0/for-operators/tutorials/how-to-connect-pinot-with-amazon-managed-streaming-for-apache-kafka-amazon-msk.md

# Source: https://docs.pinot.apache.org/release-1.3.0/for-operators/tutorials/how-to-connect-pinot-with-amazon-managed-streaming-for-apache-kafka-amazon-msk.md

# Source: https://docs.pinot.apache.org/release-1.4.0/for-operators/tutorials/how-to-connect-pinot-with-amazon-managed-streaming-for-apache-kafka-amazon-msk.md

# Source: https://docs.pinot.apache.org/operators/tutorials/how-to-connect-pinot-with-amazon-managed-streaming-for-apache-kafka-amazon-msk.md

# Amazon MSK (Kafka)

This wiki documents how to connect Pinot deployed in [Amazon EKS](https://us-west-2.console.aws.amazon.com/eks/home) to [Amazon Managed Kafka](https://aws.amazon.com/msk/).

## Prerequisite

Follow this [AWS Quickstart Wiki](https://docs.pinot.apache.org/getting-started/quickstart/aws-quickstart) to run Pinot on Amazon EKS.

## Create an Amazon MSK Cluster

1. Go to [MSK Landing Page](https://us-west-2.console.aws.amazon.com/msk/home) to create a Kafka Cluster.

{% hint style="info" %}
Note:

* For demo simplicity, this MSK cluster reuses same VPC created by EKS cluster in the previous step. Otherwise a [VPC Peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) is required to ensure two VPCs could talk to each other.
* Under **Encryption** section, choose **`Both TLS encrypted and plaintext traffic allowed`**
  {% endhint %}

1. Click **Create**. b
2. Once the cluster is created, click **`View client information`** to see the Zookeeper and Kafka Broker list.

![MSK Cluster View](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-M4QUh5tNmZ0Caycb1Un%2F-M4QkiQm0U-gWfuhQ-JT%2Fimage.png?alt=media\&token=4b7390b2-ad2d-42da-b7b7-782468945db3)

Sample Client Information

![](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-M4QUh5tNmZ0Caycb1Un%2F-M4QkwCLANHkzP8VEMqJ%2Fimage.png?alt=media\&token=c96cf9c3-e6f6-40d2-a10b-cea716b909b2)

## Connect to MSK

### Config SecurityGroup

Until now, the MSK cluster is still not accessible, you can follow this [Wiki](https://docs.aws.amazon.com/msk/latest/developerguide/create-client-machine.html) to create an EC2 instance to connect to it for topic creation, run console producer and consumer.

In order to connect MSK to EKS, we need to allow the traffic could go through each other.

This is configured through Amazon VPC Page.

1. Record the Amazon MSK `SecurityGroup` from the Cluster page, in the above demo, it's `sg-01e7ab1320a77f1a9`.
2. Open [Amazon VPC Page](https://us-west-2.console.aws.amazon.com/vpc/home), click on **`SecurityGroups`** on left bar. Find the EKS Security group: `eksctl-${PINOT_EKS_CLUSTER}-cluster/ClusterSharedNodeSecurityGroup.`

![Amazon EKS ClusterSharedNodeSecurityGroup](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2Fgit-blob-2d8d8ffd09bc9f5eaca1847d3d690a43aefeff89%2Famazon_eks_cluster%20\(3\).png?alt=media)

{% hint style="info" %}
Ensure you are picking **ClusterShardNodeSecurityGroup**
{% endhint %}

1. In SecurityGroup, click on MSK SecurityGroup (`sg-01e7ab1320a77f1a9`), then Click on `Edit Rules` , then add above `ClusterSharedNodeSecurityGroup` (`sg-0402b59d7e440f8d1`) to it.

![Add SecurityGroup to Amazon MSK](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-M4QUh5tNmZ0Caycb1Un%2F-M4RjemM99vzKdVkj8zY%2Fimage.png?alt=media\&token=bcde4e71-614c-43c8-9505-02131bb592f8)

1. Click EKS Security Group `ClusterSharedNodeSecurityGroup` (`sg-0402b59d7e440f8d1`), add In bound Rule for MSK Security Group (`sg-01e7ab1320a77f1a9`).

![Add SecurityGroup to Amazon EKS](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-M4QUh5tNmZ0Caycb1Un%2F-M4Rl4YxDn_zyiprNJm5%2Fimage.png?alt=media\&token=12298b4c-a53c-4d84-b16c-5d1352d81c6c)

Now, EKS cluster should be able to talk to Amazon MSK.

### Create Kafka topic

To run below commands, ensure you set two environment variable with `ZOOKEEPER_CONNECT_STRING` and `BROKER_LIST_STRING` (Use plaintext) from Amazon MSK client information, and replace the Variables accordingly.

E.g.

```
ZOOKEEPER_CONNECT_STRING="z-3.pinot-quickstart-msk-d.ky727f.c3.kafka.us-west-2.amazonaws.com:2181,z-1.pinot-quickstart-msk-d.ky727f.c3.kafka.us-west-2.amazonaws.com:2181,z-2.pinot-quickstart-msk-d.ky727f.c3.kafka.us-west-2.amazonaws.com:2181"
BROKER_LIST_STRING="b-1.pinot-quickstart-msk-d.ky727f.c3.kafka.us-west-2.amazonaws.com:9092,b-2.pinot-quickstart-msk-d.ky727f.c3.kafka.us-west-2.amazonaws.com:9092"
```

You can log into one EKS node or container and run below command to create a topic.

E.g. Enter into Pinot controller container:

```
kubectl exec -it pod/pinot-controller-0  -n pinot-quickstart bash
```

Then install `wget` then download Kafka binary.

```
apt-get update
apt-get install wget -y
wget https://archive.apache.org/dist/kafka/2.2.1/kafka_2.12-2.2.1.tgz
tar -xzf kafka_2.12-2.2.1.tgz
cd kafka_2.12-2.2.1
```

Create a Kafka topic:

```
bin/kafka-topics.sh \
  --zookeeper ${ZOOKEEPER_CONNECT_STRING} \
  --create \
  --topic pullRequestMergedEventsAwsMskDemo \
  --replication-factor 1 \
  --partitions 1
```

Topic creation succeeds with below message:

```
Created topic "pullRequestMergedEventsAwsMskDemo".
```

### Write sample data into Kafka

Once topic is created, we can start a simple application to produce to it.

You can download below yaml file, then replace:

* `${ZOOKEEPER_CONNECT_STRING}` -> MSK Zookeeper String
* `${BROKER_LIST_STRING}` -> MSK **Plaintext** Broker String in the deployment
* `${GITHUB_PERSONAL_ACCESS_TOKEN}` -> A personal Github Personal Access Token generated from [here](https://github.com/settings/tokens), grant all read permissions to it. Here is the [source code](https://github.com/apache/pinot/commit/1baede8e760d593fcd539d61a147185816c44fc9) to generate Github Events.

{% file src="<https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2Fgit-blob-146246528bf7b26e239295170ae4f6314b338fb5%2Fgithub-events-aws-msk-demo.yaml?alt=media>" %}
github-events-aws-msk-demo.yaml
{% endfile %}

And apply the YAML file by.

```
kubectl apply -f github-events-aws-msk-demo.yaml
```

Once the pod is up, you can verify by running a console consumer to read from it.

{% hint style="info" %}
Try to run from the Pinot Controller container entered in above step.
{% endhint %}

```
bin/kafka-console-consumer.sh \
  --bootstrap-server ${BROKER_LIST_STRING} \
  --topic pullRequestMergedEventsAwsMskDemo
```

## Create a Pinot table

This step is relatively easy.

Since we already put table creation request into the ConfigMap, we can just enter into `pinot-github-events-data-into-msk-kafka` pod to execute the command.

* Check if the pod is running:

```
kubectl get pod -n pinot-quickstart  |grep pinot-github-events-data-into-msk-kafka
```

Sample output:

```
pinot-github-events-data-into-msk-kafka-68948fb4cd-rrzlf   1/1     Running     0          14m
```

* Enter into the pod

```
podname=`kubectl get pod -n pinot-quickstart  |grep pinot-github-events-data-into-msk-kafka|awk '{print $1}'`
kubectl exec -it ${podname} -n pinot-quickstart bash
```

* Create Table

```
bin/pinot-admin.sh AddTable \
  -controllerHost pinot-controller \
  -tableConfigFile /var/pinot/examples/pullRequestMergedEventsAwsMskDemo_realtime_table_config.json \
  -schemaFile /var/pinot/examples/pullRequestMergedEventsAwsMskDemo_schema.json \
  -exec
```

Sample output:

```
Executing command: AddTable -tableConfigFile /var/pinot/examples/pullRequestMergedEventsAwsMskDemo_realtime_table_config.json -schemaFile /var/pinot/examples/pullRequestMergedEventsAwsMskDemo_schema.json -controllerHost pinot-controller -controllerPort 9000 -exec
Sending request: http://pinot-controller:9000/schemas to controller: pinot-controller-0.pinot-controller-headless.pinot-quickstart.svc.cluster.local, version: Unknown
{"status":"Table pullRequestMergedEventsAwsMskDemo_REALTIME succesfully added"}
```

* Then you can open Pinot Query Console to browse the data

![](https://github.com/pinot-contrib/pinot-docs/blob/latest/.gitbook/assets/amazon-msk-query-console-browse.png)
