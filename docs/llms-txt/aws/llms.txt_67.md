# Source: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/llms.txt

# Amazon MQ Developer Guide

> Use Amazon MQ to set up and operate message brokers in the cloud.

- [What is Amazon MQ?](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html)
- [Setting up](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-setting-up.html)
- [Getting started: Creating and connecting to an ActiveMQ broker](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/getting-started-activemq.html)
- [Getting started: Creating and connecting to a RabbitMQ broker](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/getting-started-rabbitmq.html)
- [Quotas](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-limits.html)
- [Related resources](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-related-resources.html)
- [Release notes](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-release-notes.html)

## [Managing a broker](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/managing-amazon-mq-broker.html)

- [Connecting to Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/connect-to-amazonmq.html): Learn about how to connect to Amazon MQ from another AWS service.
- [Authentication and authorization](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-access.html): Authentication and authorization options for Amazon MQ brokers, including user management and access control methods.
- [Upgrading the engine version](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/upgrading-brokers.html): Describes manually performing major and minor version upgrades for Amazon MQ brokers, including RabbitMQ 4 upgrade limitations and new broker creation requirements.
- [Upgrading the instance type](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/upgrading-instance-type.html): Describes Upgrading the broker instance type using console, API, and CLI.
- [Storage](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-storage.html): Amazon MQ for ActiveMQ supports Amazon Elastic File System (EFS) and Amazon Elastic Block Store (EBS).
- [Configuring a private broker](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/configuring-private-broker.html): Learn how to configure a private broker.
- [Scheduling broker maintenance](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/maintaining-brokers.html): Describes the broker maintenance window and how Amazon MQ applies periodic security patches, minor engine version upgrades, and updates to brokers and automatic minor version upgrades.
- [Rebooting a broker](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-rebooting-broker.html): Reboot an Amazon MQ broker.
- [Deleting a broker](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-deleting-broker.html): Delete an Amazon MQ broker using the AWS Management Console.
- [Broker statuses](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-statuses.html): Lists every Amazon MQ broker status for the console and API.
- [Tagging](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-tagging.html): You can use tags to organize and identify your Amazon MQ resources.


## [Amazon MQ for ActiveMQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/working-with-activemq.html)

- [Amazon MQ for ActiveMQ brokers](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-basic-elements.html): This section highlights the basic elements of Amazon MQ for ActiveMQ.
- [Deploying a broker](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-architecture.html): Amazon MQ for ActiveMQ brokers can be created as single-instance brokers or active/standby brokers.
- [Network of brokers](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/network-of-brokers.html): A network of brokers is comprised of multiple simultaneously active single-instance brokers or active/standby brokers.
- [Instance types](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-instance-types.html): Lists the Amazon MQ broker instance types.

### [Broker configurations](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html)

Describes the permitted configuration parameters for an Amazon MQ broker.

- [Creating a configuration](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-creating-applying-configurations.html): Create and apply configurations to your Amazon MQ broker.
- [Edit a configuration revision](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/edit-current-configuration-console.html): Create and apply configurations to your Amazon MQ broker.
- [Permitted elements](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/permitted-elements.html): The following is a detailed listing of the elements permitted in Amazon MQ configurations.
- [Permitted Attributes](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/permitted-attributes.html): The following is a detailed listing of the elements and their attributes permitted in Amazon MQ configurations.
- [Permitted Collections](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/permitted-collections.html): The following is a detailed listing of the elements, child collection elements, and their child elements permitted in Amazon MQ configurations.
- [Child Element Attributes](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/child-element-details.html): The following is a detailed explanation of child element attributes.

### [Cross-Region data replication](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/crdr-for-active-mq.html)

This section provides tutorials that you can use to set up Cross-Region data replication and functionality on Amazon MQ.

- [Creating a CRDR broker](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/create-replica-broker.html): This section shows how you can Create a primary and replica broker for Cross-Region data replication for Amazon MQ for ActiveMQ.
- [Deleting a CRDR broker](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/delete-crdr-broker.html): To delete a primary or replica cross-Region data replication (CRDR) broker, you must first unpair then reboot the brokers.
- [Promoting a CRDR broker](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/initate-failover.html): The differences between switchover and failover and how to initate failover from the console.
- [Metrics](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/crdr-metrics.html): Viewing and understanding Amazon CloudWatch metrics for CRDR

### [ActiveMQ tutorials](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/activemq-on-amazon-mq.html)

This section provides tutorials that you can use to explore ActiveMQ features and functionality on Amazon MQ.

- [Creating and configuring a network of brokers](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-creating-configuring-network-of-brokers.html): Create and configure a network of Amazon MQ brokers.
- [Connecting a Java application to your broker](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-connecting-application.html): Connect a Java application to your Amazon MQ broker.
- [Integrating ActiveMQ brokers with LDAP](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-authentication-authorization.html): Learn about controlling authentication for ActiveMQ brokers and authorization for queues and topics.
- [Creating an ActiveMQ broker user](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-listing-managing-users.html): List your Amazon MQ broker users and manage user accounts.
- [Edit an ActiveMQ broker user](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/edit-existing-user-console.html): To edit an existing user, do the following:
- [Delete an ActiveMQ broker user](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/delete-existing-user-console.html): When you no longer need a user, you can delete the user.
- [Working Java examples](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-working-java-example.html): The following examples show how you can work with ActiveMQ programmatically:
- [Version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/activemq-version-management.html): Describes the difference between Amazon MQ for ActiveMQ minor and major engine versions, lists supported ActiveMQ engine versions, and information about upgrading brokers.
- [Amazon MQ for ActiveMQ best practices](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/best-practices-activemq.html): Describes best practices for using the ActiveMQ engine on Amazon MQ


## [Amazon MQ for RabbitMQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/working-with-rabbitmq.html)

### [Version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-version-management.html)

Describes the difference between Amazon MQ for RabbitMQ minor and major engine versions, lists supported RabbitMQ engine versions, and information about upgrading brokers.

- [RabbitMQ 4](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-4.html): Amazon MQ supports RabbitMQ 4.2 in the RabbitMQ 4 release series only on the mq.m7g instance type across all supported instance sizes.
- [Version support](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-version-support.html): The Amazon MQ version support calendar below indicates when a broker engine version will reach end of support.
- [Version upgrades](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/version-upgrades.html): You can manually upgrade your broker at any time to the next supported major or minor version.
- [Deploying a RabbitMQ broker](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-broker-architecture.html): RabbitMQ brokers can be created as single-instance brokers or in a cluster deployment.
- [Instance types](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rmq-broker-instance-types.html): The combined description of the broker instance class (m7g) and size (large, medium) is called the broker instance type (for example, mq.m7g.large).

### [Sizing guidelines](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-sizing-guidelines.html)

You can choose the broker instance type that best supports your application.

- [Default resource limits](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-resource-limits-configuration.html): Amazon MQ for RabbitMQ supports configuring the broker resource limits from RabbitMQ 4 onwards.
- [Maximum resource limit](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-resource-hard-limit.html)
- [Broker defaults](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-defaults.html): Describes the default broker policies and vhost limits applied by Amazon MQ for every new Amazon MQ for RabbitMQ broker.

### [Broker configurations](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-broker-configuration-parameters.html)

Describes how to configure Amazon MQ for RabbitMQ brokers and the permitted configuration parameters.

- [Creating a configuration](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-creating-applying-configurations.html): Create and apply configurations to your Amazon MQ broker.
- [Editing a configuration revision](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/edit-current-rabbitmq-configuration-console.html): The following instructions describe how to edit a configuration revision for your broker.

### [Configurable values](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/configurable-values.html)

You can set the value of the following broker configuration options by modifying the broker configuration file in the AWS Management Console.

- [Configuring OAuth 2.0](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/configure-oauth2.html): For information about OAuth 2.0 configuration options and setting up OAuth 2.0 authentication for your brokers, see Supported OAuth 2.0 configurations and Using OAuth 2.0 authentication and authorization.
- [Configuring LDAP](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/configure-ldap.html): For information about LDAP configuration options and setting up LDAP authentication for your brokers, see Supported LDAP configurations and .
- [Configuring HTTP](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/configure-http.html): Configure HTTP authentication and authorization for Amazon MQ for RabbitMQ brokers.
- [Configuring SSL](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/configure-ssl.html): Configure SSL certificate authentication for Amazon MQ for RabbitMQ brokers.
- [Configuring mTLS](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/configure-mtls.html): Configure mutual TLS (mTLS) for Amazon MQ for RabbitMQ brokers.
- [Configuring Resource Limit](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/configure-resource-limits.html): Amazon MQ for RabbitMQ supports configuring broker resource limits from RabbitMQ 4 onwards.
- [ARN support in RabbitMQ configuration](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/arn-support-rabbitmq-configuration.html): Amazon MQ for RabbitMQ supports AWS ARNs for the values of some RabbitMQ configuration settings.
- [AMQP client SSL configuration](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-amqp-client-ssl-configuration.html): Federation and shovel use AMQP for communication between upstream and downstream brokers.

### [Authentication and Authorization](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-authentication.html)

Authentication and authorization methods for Amazon MQ for RabbitMQ brokers.

- [Simple authentication and authorization](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-simple-auth-broker-users.html)
- [OAuth 2.0 authentication and authorization](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/oauth-for-amq-for-rabbitmq.html): Learn about OAuth 2.0 authentication and authorization for Amazon MQ for RabbitMQ.
- [IAM authentication and authorization](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/iam-for-amq-for-rabbitmq.html): Learn about IAM authentication and authorization for Amazon MQ for RabbitMQ.
- [HTTP authentication and authorization](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/http-for-amq-for-rabbitmq.html): Learn about HTTP authentication and authorization for Amazon MQ for RabbitMQ.
- [SSL certificate authentication](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/ssl-for-amq-for-rabbitmq.html): Learn about SSL certificate authentication for Amazon MQ for RabbitMQ.
- [LDAP authentication and authorization](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/ldap-for-amq-for-rabbitmq.html): Learn about LDAP authentication and authorization for Amazon MQ for RabbitMQ.
- [Plugins](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-basic-elements-plugins.html): Amazon MQ for RabbitMQ also supports the following plugins.
- [Protocols](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-supported-protocols.html): You can access your RabbitMQ brokers by using any programming language that RabbitMQ supports and by enabling TLS for any of the following protocol specifications:
- [JMS support](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-jms-support.html): You can now run JMS 1.1, 2.0, and 3.1 workloads on Amazon MQ for RabbitMQ 4 with RabbitMQ JMS client.
- [Policies](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-defaults-applying-policies.html): You can apply custom policies and limits with Amazon MQ recommended default values.

### [Quorum queues](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/quorum-queues.html)

Set up quorum queues for Amazon MQ.

- [Migrating to quorum queues](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/quorum-queues-migration.html): You can migrate your classic mirrored queues to quorum queues on Amazon MQ brokers on version 3.13 or above by creating a new virtual host on the same cluster, or by migrating in place.
- [Policy configuration](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/quorum-queues-policy-configurations.html): You can add specific policy configurations to quorum queues for your RabbitMQ broker on Amazon MQ.
- [Best practices](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/quorum-queues-best-practices.html): We recommend using the following best practices to improve performance when working with quorum queues.

### [Amazon MQ for RabbitMQ best practices](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/best-practices-rabbitmq.html)

Describes best practices for using the RabbitMQ engine on Amazon MQ

- [Broker setup](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/best-practices-broker-setup.html): Broker setup and connection management are the first step in preventing issues with broker message throughput, resource utilization, and ability to handle production workloads.
- [Message reliability](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/best-practices-message-reliability.html): Before moving your application to production, complete the following best practices for preventing message loss and resource overutilization.
- [Performance optimization](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/best-practices-performance.html): You can optimize your Amazon MQ for RabbitMQ broker performance by maximizing throughput, minimizing latency, and ensuring efficient resource utilization.
- [Network resilience](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/best-practices-network-resilience.html): Network resilience and monitoring broker metrics are essential for maintaining reliable messaging applications.

### [RabbitMQ tutorials](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-on-amazon-mq.html)

This section provides tutorials that you can use to explore RabbitMQ features and functionality on Amazon MQ.

- [Editing broker preferences](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-rabbitmq-editing-broker-preferences.html): Edit RabbitMQ broker engine version, CloudWatch logs, and maintenance preferences.
- [Using Python Pika with Amazon MQ for RabbitMQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-rabbitmq-pika.html): Describes setting up a Python Pika client with TLS configured to connect to an Amazon MQ for RabbitMQ broker, publish messages to the default exchange, and consume messages from a queue.
- [Resolving paused queue sync](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-queue-sync.html): Resolve a paused or hung queue sync for classic mirrored queues in an Amazon MQ for RabbitMQ cluster deployment.
- [Reducing the number of connections and channels](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/reducing-connections-and-channels.html): Connections to your RabbitMQ on Amazon MQ broker can be closed either by your client applications, or by manually closing them using the RabbitMQ web console.
- [Using OAuth 2.0 authentication and authorization](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/oauth-tutorial.html): Configure OAuth 2.0 authentication for Amazon MQ for RabbitMQ brokers using Amazon Cognito as the identity provider (IdP).
- [Using IAM authentication and authorization](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-iam-tutorial.html): Learn how to enable and use AWS IAM authentication and authorization for Amazon MQ for RabbitMQ brokers.
- [Using LDAP authentication and authorization](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-ldap-tutorial.html): Configure LDAP authentication and authorization for Amazon MQ for RabbitMQ brokers using AWS Managed Microsoft AD as the directory service.
- [Using HTTP authentication and authorization](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-http-tutorial.html): Configure HTTP authentication and authorization for Amazon MQ for RabbitMQ brokers using an external HTTP server as the authentication provider.
- [Using SSL certificate authentication](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-ssl-tutorial.html): Configure SSL certificate authentication for Amazon MQ for RabbitMQ brokers using X.509 client certificates.
- [Using mTLS for AMQP and management endpoints](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-mtls-tutorial.html): Configure mutual TLS (mTLS) for AMQP client connections and the RabbitMQ management interface.
- [Connecting your JMS application](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-tutorial-jms.html): This tutorial shows you how to connect your JMS application to Amazon MQ for RabbitMQ broker using the RabbitMQ JMS client.


## [Security](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security.html)

- [Data protection](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Amazon MQ.

### [Identity and access management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-iam.html)

How to authenticate requests and manage access your Amazon MQ resources.

- [How Amazon MQ works with IAM](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon MQ, you should understand what IAM features are available to use with Amazon MQ.
- [Identity-based policy examples](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon MQ resources.
- [API authentication and authorization](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-api-authentication-authorization.html): Learn about controlling authentication for Amazon MQ brokers and authorization for brokers, configurations, and users.
- [Broker authentication and authorization](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-broker-auth-ref.html): Amazon MQ provides different authentication and authorization methods depending on your broker engine type.
- [AWS managed policies](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-iam-awsmanpol.html): Learn about AWS managed permission policies for Amazon MQ and recent changes to those policies.
- [Using service-linked roles](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/using-service-linked-roles.html): How to use service-linked roles to give Amazon MQ access to resources in your AWS account.
- [Troubleshooting](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon MQ and IAM.
- [Compliance validation](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon MQ features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/infrastructure-security.html): Learn how Amazon MQ isolates service traffic.
- [Security best practices](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/using-amazon-mq-securely.html): The following design patterns can improve the security of your Amazon MQ broker.


## [Logging and monitoring](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-logging-monitoring.html)

- [Accessing CloudWatch metrics](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-accessing-metrics.html): Access CloudWatch metrics for Amazon MQ.
- [Metrics for ActiveMQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/activemq-logging-monitoring.html): You can integrate CloudWatch with Amazon MQ for ActiveMQ.
- [Metrics for RabbitMQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-logging-monitoring.html): You can integrate Amazon MQ for RabbitMQ with CloudWatch This section has the metrics you can monitor.
- [Logging API calls using CloudTrail](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-logging-monitoring-cloudtrail.html): This section provides information about logging Amazon MQ API calls using CloudTrail.
- [Configuring Amazon MQ for ActiveMQ logs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/configure-logging-monitoring-activemq.html): This section provides information about configuring Amazon MQ for ActiveMQ logs using CloudTrail.
- [Troubleshooting](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-logging-monitoring-configure-cloudwatch-troubleshoot.html): You can integrate CloudWatch with Amazon MQ for ActiveMQ and RabbitMQ.


## [Troubleshooting](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/troubleshooting.html)

- [Troubleshooting: General Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/general.html): Learn how to troubleshoot general issues when working with Amazon MQ brokers.
- [Troubleshooting ActiveMQ on Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/troubleshooting-activemq.html): Learn how to troubleshoot general issues when working with ActiveMQ on Amazon MQ brokers.
- [Troubleshooting: RabbitMQ on Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/troubleshooting-rabbitmq.html): Learn how to troubleshoot general issues when working with RabbitMQ on Amazon MQ brokers.
- [BROKER_ENI_DELETED](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/troubleshooting-action-required-codes-broker-eni-deleted.html): You may experience a BROKER_ENI_DELETED when you delete your broker ENI.
- [BROKER_OOM](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/troubleshooting-action-required-codes-broker-out-of-memory.html): You may experience a BROKER_OOM when the broker undergoes a restart loop due to the insufficient memory capacity.
- [RABBITMQ_MEMORY_ALARM](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/troubleshooting-action-required-codes-rabbitmq-memory-alarm.html): You may experience a RABBITMQ_MEMORY_ALARM when you run out of memory.
- [RABBITMQ_INVALID_KMS_KEY](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/troubleshooting-action-required-codes-invalid-kms-key.html): You may experience a RABBITMQ_INVALID_KMS_KEY when your kms key is disabled.
- [RABBITMQ_DISK_ALARM](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/troubleshooting-action-required-codes-disk-limit-alarm.html): You may experience a BROKER_DISK_ALARM when the broker undergoes a restart loop due to the insufficient memory capacity.
- [RABBITMQ_CLUSTER_DISK_USAGE_TOO_HIGH_FOR_INSTANCE_CHANGE](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/troubleshooting-action-required-instance-change-alarm.html): You may experience a BROKER_DISK_ALARM when the broker undergoes a restart loop due to the insufficient memory capacity.
- [RABBITMQ_INVALID_ASSUMEROLE](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/troubleshooting-action-required-codes-invalid-assumerole.html): You may experience a RABBITMQ_INVALID_ASSUMEROLE when the IAM role specified for ARN resolution cannot be assumed.
- [RABBITMQ_INVALID_ARN_LDAP](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/troubleshooting-action-required-codes-invalid-arn-ldap.html): You may experience a RABBITMQ_INVALID_ARN_LDAP when the LDAP service account password ARN is invalid or inaccessible.
- [RABBITMQ_INVALID_ARN_HTTP](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/troubleshooting-action-required-codes-invalid-arn-http.html): You may experience a RABBITMQ_INVALID_ARN_HTTP when the ARNs of ssl certificates or key file for HTTP auth_backend are invalid or inaccessible.
- [RABBITMQ_INVALID_ARN_SSL](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/troubleshooting-action-required-codes-invalid-arn-ssl.html): You may experience a RABBITMQ_INVALID_ARN_SSL when the ARNs of ssl certificates for SSL auth_mechanism are invalid or inaccessible.
- [RABBITMQ_INVALID_ARN](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/troubleshooting-action-required-codes-invalid-arn.html): You may experience a RABBITMQ_INVALID_ARN when one or more ARNs in the broker configuration are invalid or inaccessible.
