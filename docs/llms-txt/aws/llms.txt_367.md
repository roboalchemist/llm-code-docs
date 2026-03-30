# Source: https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/llms.txt

# Amazon EMR Amazon EMR on EKS Development Guide

> With Amazon EMR, you can run your Apache Spark workloads on Kubernetes clusters managed by Amazon Elastic Kubernetes Service (Amazon EKS). Use this guide together with the Amazon EMR on EKS API Reference.

- [Getting started with Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/getting-started.html)
- [Best practices](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/best-practices.html)
- [Uploading data](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/upload-data-s3-express.html)
- [Monitoring jobs](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/monitoring.html)
- [Managing virtual clusters](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/virtual-cluster.html)
- [Tagging resources](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/tag-resources.html)
- [Service endpoints and quotas](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/service-quotas.html)
- [Document history](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/doc-history.html)

## [What is Amazon EMR on EKS?](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks.html)

- [Architecture for Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-overview.html): Amazon EMR on EKS loosely couples applications to the infrastructure that they run on.
- [Understanding Amazon EMR on EKS concepts and terminology](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-concepts.html): Amazon EMR on EKS provides a deployment option for Amazon EMR that allows you to run open-source big data frameworks on Amazon Elastic Kubernetes Service (Amazon EKS).
- [What happens when you submit work to an Amazon EMR on EKS virtual cluster](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-how.html): Registering Amazon EMR with a Kubernetes namespace on Amazon EKS creates a virtual cluster.


## [Customizing Docker images](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/docker-custom-images.html)

### [How to customize Docker images](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/docker-custom-images-steps.html)

Follow these steps to customize Docker images for Amazon EMR on EKS.

- [Customize Docker images for interactive endpoints](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/docker-custom-images-managed-endpoint.html): You can also customize Docker images for interactive endpoints so that you can run customized base kernel images.
- [Work with multi-architecture images](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/docker-custom-images-multi-architecture.html): Amazon EMR on EKS supports multi-architecture container images for Amazon Elastic Container Registry (Amazon ECR).
- [Details for selecting a base image URI](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/docker-custom-images-tag.html): Learn how to select a base image URI.
- [Considerations for customizing images](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/docker-custom-images-considerations.html): Take these considerations when you use custom images with Amazon EMR on EKS.


## [Running Flink jobs](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/run-flink-jobs.html)

### [Flink Kubernetes operator](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-kubernetes-operator.html)

The following pages describe how to set up and use the Flink Kubernetes operator to run Flink jobs with Amazon EMR on EKS.

- [Setting up](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-kubernetes-operator-setup.html): Get set up for the Flink Kubernetes operator on Amazon EMR on EKS
- [Installing the Flink Kubernetes operator](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-kubernetes-operator-getting-started.html): This topic helps you start to use the Flink Kubernetes operator on Amazon EKS by preparing a Flink deployment.
- [Run a Flink application](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-kubernetes-operator-run-application.html): With Amazon EMR 6.13.0 and higher, you can run a Flink application with the Flink Kubernetes operator in Application mode on Amazon EMR on EKS.
- [Security role permissions for running a Flink application](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-kubernetes-security.html): This topic describes security roles for deploying and running a Flink application.
- [Uninstalling the operator](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-kubernetes-operator-uninstall.html): Follow these steps to uninstall the Flink Kubernetes operator.

### [Flink Native Kubernetes](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-native-kubernetes.html)

Amazon EMR releases 6.13.0 and higher support Flink Native Kubernetes as a command-line tool that you can use to submit and execute Flink applications to an Amazon EMR on EKS cluster.

- [Setting up](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-native-kubernetes-setup.html): Complete the following tasks to get set up before you can run an application with the Flink CLI on Amazon EMR on EKS.
- [Getting started](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-native-kubernetes-getting-started.html): These steps show you how to configure, set up a service account for, and run a Flink application.
- [Security requirements](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-native-kubernetes-security-requirements.html): The Flink JobManager pod uses a Kubernetes service account to access the Kubernetes API server to create and watch TaskManager pods.
- [Customizing Docker images for Flink and FluentD](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-docker-flink-fluentd.html): Take the following steps to customize Docker images for Amazon EMR on EKS with Apache Flink or FluentD images.

### [Monitoring](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-monitoring.html)

This section describes several ways that you can monitor your Flink jobs with Amazon EMR on EKS.

- [Using Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-monitoring-prometheus.html): You can integrate Apache Flink with Amazon Managed Service for Prometheus (management portal).
- [Using the Flink UI](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-monitoring-ui.html): To monitor the health and performance of a running Flink application, use the Flink Web Dashboard.
- [Using monitoring configuration](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-monitoring-configuration.html): Monitoring configuration lets you easily set up log archiving of your Flink application and operator logs to S3 and/or CloudWatch (you can choose either one or both).

### [How Flink supports high availability and job resiliency](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-resiliency.html)

The following sections outline how Flink makes jobs more reliable and highly available.

- [Using high availability](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-using-ha.html): This topic shows how to configure high availability and describes how it works for a few different use cases.
- [Optimizing restart times](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-restart.html): Flink with Amazon EMR on EKS can improve the job restart time during task recovery or scaling operations.
- [Graceful decommission](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-decommission.html): Flink with Amazon EMR on EKS can improve the job restart time during task recovery or scaling operations when you work with spot instances.

### [Using Autoscaler](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-autoscaler.html)

The operator autoscaler can help ease backpressure by collecting metrics from Flink jobs and automatically adjusting parallelism on a job vertex level.

- [Autoscaler parameter autotuning](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-autoscaler-parameter-autotuning.html): This section describes auto-tuning behavior for various Amazon EMR versions.

### [Maintenance and troubleshooting for Flink jobs on Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-troubleshooting.html)

The following sections outline how to maintain your long-running Flink jobs, and provide guidance on how to troubleshoot some common issues with Flink jobs.

- [Maintaining Flink applications](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-maintain.html): Topics
- [Troubleshooting](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-troubleshoot.html): This section describes how to troubleshoot problems with Amazon EMR on EKS.
- [Supported releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-security-release-versions.html): Apache Flink is available with the following Amazon EMR on EKS releases.


## [Running Spark jobs](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs-main.html)

### [StartJobRun](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs.html)

This section includes detailed setup steps to get your environment ready to run Spark jobs and then provides step-by-step instructions for submitting a job run with specified parameters.

### [Setting up](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/setting-up.html)

Complete Amazon EMR on EKS prerequisites like creating a new Amazon EKS cluster and namespace, and creating the required AWS and Kubernetes resources for your virtual cluster.

- [Enable cluster access for Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/setting-up-cluster-access.html): The following sections show a couple ways to enable cluster access.

### [Enable IAM Roles for the EKS cluster](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/setting-up-enable-IAM-roles.html)

The following topics detail options for enabling IAM roles.

- [Option 1: Enable EKS Pod Identity on the EKS Cluster](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/setting-up-enable-IAM.html): Amazon EKS Pod Identity associations provide the ability to manage credentials for your applications, similar to the way that Amazon EC2 instance profiles provide credentials to Amazon EC2 instances.

### [Option 2: Enable IAM Roles for Service Accounts (IRSA) on the EKS cluster](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/setting-up-enable-IAM-service-accounts.html)

The IAM roles for service accounts feature is available on Amazon EKS versions 1.14 and later and for EKS clusters that are updated to versions 1.13 or later on or after September 3rd, 2019.

- [Create a job execution role](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/creating-job-execution-role.html): To run workloads on Amazon EMR on EKS, you need to create an IAM role.
- [Update the trust policy of the job execution role](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/setting-up-trust-policy.html): When you use IAM Roles for Service Accounts (IRSA) to run jobs on a Kubernetes namespace, an administrator must create a trust relationship between the job execution role and the identity of the EMR managed service account.
- [Grant users access to Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/setting-up-iam.html): For any actions that you perform on Amazon EMR on EKS, you need a corresponding IAM permission for that action.
- [Register the Amazon EKS cluster with Amazon EMR](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/setting-up-registration.html): Registering your cluster is the final required step to set up Amazon EMR on EKS to run workloads.
- [Submit a job run with StartJobRun](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-jobs-submit.html)
- [Using job submitter classification](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-job-submitter.html)
- [Using Amazon EMR container defaults classification](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-job-submitter-container-defaults.html)

### [Spark operator](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-operator.html)

Run Spark jobs on Amazon EMR on EKS with the Spark operator.

- [Setting up](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-operator-setup.html): Get set up for the Spark operator on Amazon EKS
- [Getting started](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-operator-gs.html): Get started with the Spark operator on Amazon EKS
- [Vertical autoscaling](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-operator-vas.html): How to use vertical autoscaling with the Spark operator on Amazon EMR on EKS.
- [Uninstall](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-operator-uninstall.html): Uninstall the Spark operator.

### [Using monitoring configuration to monitor Spark](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-operator-monitoring-configuration.html)

Monitoring configuration lets you easily set up log archiving of your Spark application and operator logs to Amazon S3 or to Amazon CloudWatch.

- [Spark Operator Logs](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-operator-monitoring-configuration-logs.html): You can define monitoring configuration in the following way when doing helm install:
- [Spark Application Logs](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-operator-monitoring-application-logs.html): You can define this configuration in the following way.

### [Security](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-operator-security.html)

Understanding security and the Spark operator with Amazon EMR on EKS.

- [Role-based access control (RBAC)](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-operator-security-rbac.html): Using role-based access control (RBAC) with the Spark operator with Amazon EMR on EKS.
- [IAM roles for service accounts (IRSA)](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-operator-security-irsa.html): Using IAM roles for service accounts (IRSA) with the Spark operator and Amazon EMR on EKS.

### [spark-submit](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-submit.html)

Run Spark jobs on Amazon EMR on EKS with spark-submit.

- [Setting up](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-submit-setup.html): Get set up to use spark-submit with Amazon EMR on EKS
- [Getting started](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-submit-gs.html): Get started with spark-submit for Amazon EMR on EKS

### [Security](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-submit-security.html)

Spark driver service account requirements.

- [IAM roles for service roles for spark-submit](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-submit-security-irsa.html): The following sections explain how to set up IAM roles for service accounts (IRSA) to authenticate and authorize Kubernetes service accounts so you can run Spark applications stored in Amazon S3.

### [Apache Livy](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs-apache-livy.html)

With Amazon EMR releases 7.1.0 and higher, you can use Apache Livy to submit jobs on Amazon EMR on EKS.

- [Setting up](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs-apache-livy-setup.html): Before you can install Apache Livy on your Amazon EKS cluster, you must install and configure a set of prerequisite tools.
- [Getting started](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs-apache-livy-install.html): Complete the following steps to install Apache Livy.
- [Running a Spark application](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs-apache-livy-run-spark.html): Before you can run a Spark application with Apache Livy, make sure that you have completed the steps in Setting up Apache Livy for Amazon EMR on EKS and Getting started with Apache Livy for Amazon EMR on EKS.
- [Uninstalling](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs-apache-livy-uninstall.html): Follow these steps to uninstall Apache Livy.

### [Security](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs-apache-livy-security.html)

See the following topics to learn more about configuring security for Apache Livy with Amazon EMR on EKS.

- [Setting up a secure Apache Livy endpoint with TLS/SSL](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs-apache-livy-secure-endpoint.html): See the following sections to learn more about setting up Apache Livy for Amazon EMR on EKS with end-to-end TLS and SSL encryption.
- [Setting up the Spark application with RBAC](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs-apache-livy-rbac.html): To deploy Livy, Amazon EMR on EKS creates a server service account and role and a Spark service account and role.
- [IAM roles for service accounts (IRSA)](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs-apache-livy-irsa.html): By default, the Livy server and Spark application's driver and executors don't have access to AWS resources.
- [Installation properties](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs-apache-livy-installation-properties.html): Apache Livy installation allows you to select a version of the Livy Helm chart.
- [Troubleshoot common environment-variable format errors](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs-apache-livy-troubleshooting.html): When you input Livy and Spark configurations, there are environment-variable formats that aren't supported and can cause errors.

### [Managing job runs](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-jobs-manage.html)

Manage your Amazon EMR on EKS job runs.

### [Manage with CLI](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-jobs-CLI.html)

This topic covers how to manage job runs with the AWS Command Line Interface (AWS CLI).

- [Use S3 logs](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-jobs-s3.html): To be able to monitor the job progress and to troubleshoot failures, you must configure your jobs to send log information to Amazon S3, Amazon CloudWatch Logs, or both.
- [Use CloudWatch Logs](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-jobs-cloudwatch.html): To monitor job progress and to troubleshoot failures, you must configure your jobs to send log information to Amazon S3, Amazon CloudWatch Logs, or both.
- [Run Spark SQL scripts](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-jobs-spark-sql-parameters.html): Amazon EMR on EKS releases 6.7.0 and higher include a Spark SQL job driver so that you can run Spark SQL scripts through the StartJobRun API.
- [Job run states](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-jobs-states.html): When you submit a job run to an Amazon EMR on EKS job queue, the job run enters the PENDING state.
- [View jobs in the console](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-jobs-console.html): Job run data is avilable to view, so you can monitor each job as it passes through the states.
- [Common job run errors](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-jobs-error.html): The following errors may occur when you run StartJobRun API.

### [Using job templates](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-templates.html)

A job template stores values that can be shared across StartJobRun API invocations when starting a job run.

- [Create and using a job template to start a job run](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/create-job-template.html): This section describes creating a job template and using the template to start a job run with the AWS Command Line Interface (AWS CLI).
- [Defining job template parameters](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/use-job-template-parameters.html): Job template parameters allow you to specify variables in the job template.
- [Controlling access to job templates](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/iam-job-template.html): StartJobRun policy lets you enforce that a user or a role can only run jobs using job templates that you specify and cannot run StartJobRun operations without using the specified job templates.
- [Using pod templates](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/pod-templates.html): Beginning with Amazon EMR versions 5.33.0 or 6.3.0, Amazon EMR on EKS supports Sparkâs pod template feature.
- [Using retry policies](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-using-retry-policies.html): In Amazon EMR on EKS versions 6.9.0 and later, you can set a retry policy for your job runs.
- [Using Spark event log rotation](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-log-rotation.html): With Amazon EMR 6.3.0 and later, you can turn on the Spark event log rotation feature for Amazon EMR on EKS.
- [Using Spark container log rotation](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-log-rotation-container.html): With Amazon EMR 6.11.0 and later, you can turn on the Spark container log rotation feature for Amazon EMR on EKS.

### [Using vertical autoscaling](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-vas.html)

With vertical autoscaling, Amazon EMR on EKS automatically tunes memory and CPU resources to adapt to the needs of your Amazon EMR Spark application workload.

- [Setting up](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-vas-setup.html): Set up vertical autoscaling to let Amazon EMR on EKS automatically tune memory and CPU resources to adapt to the needs of your Amazon EMR Spark application workload.
- [Getting started](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-vas-gs.html): Use vertical autoscaling for Amazon EMR on EKS when you want automatic tuning of memory and CPU resources to adapt to your Amazon EMR Spark application workload.
- [Configuration](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-vas-configure.html): You can configure vertical autoscaling when you submit Amazon EMR Spark jobs through the StartJobRun API.
- [Monitoring the recommendations](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-vas-monitor.html): Use kubectl to monitor the vertical autoscaling-related recommendations for your cluster.
- [Uninstalling](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-vas-uninstall-operator.html): If you want to remove the vertical autoscaling operator from your Amazon EKS cluster, use the cleanup command with the Operator SDK CLI as shown in the following example.


## [Running interactive workloads](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/connect-emr-studio.html)

- [Overview of interactive endpoints](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/how-it-works.html): An interactive endpoint provides the capability for interactive clients like Amazon EMR Studio to connect to Amazon EMR on EKS clusters to run interactive workloads.
- [Interactive endpoints prerequisites](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/prereqs-for-studio.html): The following are prerequisites to set up an interactive endpoint that EMR Studio can use to connect to an Amazon EMR on EKS cluster and run interactive workloads.
- [Creating an interactive endpoint](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/create-managed-endpoint.html): This topic describes a couple ways to create an interactive endpoint using the AWS Command Line Interface (AWS CLI) and includes details on available configuration parameters.

### [Configuring settings for interactive endpoints](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/managed-endpoint-parameters.html)

This section contains a series of topics that cover various configurations for interactive endpoints and pod settings.

- [Monitoring Spark jobs](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/monitoring-spark-jobs.html): So that you can monitor and troubleshoot failures, configure your interactive endpoints so that the jobs initiated with the endpoint can send log information to Amazon S3, Amazon CloudWatch Logs, or both.
- [Custom pod templates](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/custom-pod-templates.html): You can create interactive endpoints where you specify custom pod templates for drivers and executors.
- [Deploying a JEG pod to a node group](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/managed-endpoint-nodegroups-setup.html): JEG (Jupyter Enterprise Gateway) pod placement is a feature that allows you to deploy an interactive endpoint on a specific node group.
- [JEG configuration options](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jeg-config-options.html): Amazon EMR on EKS uses Jupyter Enterprise Gateway (JEG) to turn on interactive endpoints.
- [Modifying PySpark parameters](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/modify-pyspark-parameters.html): Starting with Amazon EMR on EKS release 6.9.0, in Amazon EMR Studio you can adjust the Spark configuration associated with a PySpark session by executing the %%configure magic command in the EMR notebook cell.
- [Custom kernel image](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/custom-kernel.html): To ensure that you have the correct dependencies for your application when you run interactive workloads from Amazon EMR Studio, you can customize Docker images for interactive endpoints and run customized base kernel images.
- [Monitoring interactive endpoints](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/managed-endpoints-customer-metrics.html): With Amazon EMR on EKS version 6.10 and later, interactive endpoints emit Amazon CloudWatch metrics for monitoring and troubleshooting kernel lifecycle operations.
- [Using self-hosted Jupyter notebooks](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/managed-endpoints-self-hosted.html): Connect a self-hosted JupyterLab notebook to Amazon EMR on EKS virtual clusters through an interactive endpoint.

### [Getting information about interactive endpoints with CLI commands](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/other-operations.html)

This topic covers the supported operations on an interactive endpoint other than create-managed-endpoint.

- [Delete interactive endpoint](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/delete-managed-endpoint.html): To delete an interactive endpoint associated with an Amazon EMR on EKS virtual cluster, use the delete-managed-endpoint AWS CLI command.


## [Tutorials](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/tutorials.html)

- [Using Delta Lake](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/tutorial-delta-lake.html): Use Delta Lake with Amazon EMR on EKS
- [Using Iceberg](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/tutorial-iceberg.html): Use Apache Iceberg with Amazon EMR on EKS
- [Using PyFlink](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/pyflink-for-flink.html): Amazon EMR on EKS releases 6.15.0 and higher supports PyFlink.
- [Using AWS Glue with Flink](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/glue-for-flink.html): Amazon EMR on EKS with Apache Flink releases 6.15.0 and higher supports using the AWS Glue Data Catalog as a metadata store for streaming and batch SQL workflows.
- [Using Apache Hudi](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/tutorial-hudi-for-flink.html): Apache Hudi is an open-source data management framework with record-level operations such as insert, update, upsert, and delete that you can use to simplify data management and data pipeline development.
- [Using Spark RAPIDS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/tutorial-spark-rapids.html): Use RAPIDS Accelerator for Apache Spark with Amazon EMR on EKS.

### [Using Spark on Redshift](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-spark-redshift.html)

With Amazon EMR release 6.9.0 and later, every release image includes a connector between Apache Spark and Amazon Redshift.

- [Launch a Spark application](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-spark-redshift-launch.html): To use the integration, you must pass the required Spark Redshift dependencies with your Spark job.
- [Authenticate to Amazon Redshift](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-spark-redshift-auth.html): The following sections show authentication options with Amazon Redshift when you're integrating with Apache Spark.
- [Read and write to Amazon Redshift](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-spark-redshift-readwrite.html): The following code examples use PySpark to read and write sample data from and to an Amazon Redshift database with a data source API and with SparkSQL.
- [Considerations](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-spark-redshift-considerations.html): The Spark connector supports a variety of ways to manage credentials, to configure security, and to connect with other AWS services.
- [Using Volcano](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/tutorial-volcano.html): Use Volcano as a custom Spark scheduler with Amazon EMR on EKS.
- [Using YuniKorn](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/tutorial-yunikorn.html): Use YuniKorn as a custom Spark scheduler with Amazon EMR on EKS.


## [Security](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security.html)

- [Best practices](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security-best-practices.html): Amazon EMR on EKS provides a number of security features to consider as you develop and implement your own security policies.
- [Data protection](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/data-protection.html): The AWS shared responsibility model applies to data protection in Amazon EMR on EKS.

### [Identity and Access Management](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security-iam.html)

How to authenticate requests and manage access your Amazon EMR on EKS resources.

- [How Amazon EMR on EKS works with IAM](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon EMR on EKS, learn what IAM features are available to use with Amazon EMR on EKS.
- [Using Service-Linked Roles](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/using-service-linked-roles.html): How to use service-linked roles to give Amazon EMR on EKS access to resources in your AWS account.
- [Managed policies for Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-managed-polices.html): View details about updates to AWS managed policies for Amazon EMR on EKS since March 1, 2021.
- [Using job execution roles with Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/iam-execution-role.html): To use the StartJobRun command to submit a job run on an EKS cluster, you must first onboard a job execution role to be used with a virtual cluster.
- [Identity-based policy examples](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon EMR on EKS resources.
- [Policies for tag-based access control](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security_iam_TBAC.html): You can use conditions in your identity-based policy to control access to virtual clusters and job runs based on tags.
- [Troubleshooting](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon EMR on EKS and IAM.

### [Using Amazon EMR on EKS with AWS Lake Formation](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security_iam_fgac-lf.html)

With Amazon EMR release 7.7 and higher, you can leverage AWS Lake Formation to apply fine-grained access controls on AWS Glue Data Catalog tables that are backed by Amazon S3 buckets.

- [How Amazon EMR on EKS works with AWS Lake Formation](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security_iam_fgac-lf-works.html): Using Amazon EMR on EKS with Lake Formation lets you enforce a layer of permissions on each Spark Job to apply Lake Formation permission control when Amazon EMR on EKS executes jobs.
- [Enable Lake Formation with Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security_iam_fgac-lf-enable.html): With Amazon EMR release 7.7 and higher, you can leverage AWS Lake Formation to apply fine-grained access controls on Data Catalog tables that are backed by Amazon S3.
- [Considerations and limitations](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security_iam_fgac-considerations.html): Note the following considerations and limitations when you use Lake Formation with Amazon EMR on EKS:
- [Troubleshooting](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security_iam_fgac-troubleshooting.html)

### [Logging and monitoring](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security-logging-monitoring.html)

To detect incidents, receive alerts when incidents occur, and respond to them, use these options with Amazon EMR on EKS:

- [Encrypting logs](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security_iam_fgac-logging-kms.html): The sections that follow show you how to configure encryption for logs.
- [CloudTrail logs](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/logging-using-cloudtrail.html): Learn about logging Amazon EMR on EKS with AWS CloudTrail.
- [S3 Access Grants](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/access-grants.html): Launch an Amazon EMR on EKS cluster with S3 Access Grants for data access management.
- [Compliance Validation](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon EMR on EKS features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/infrastructure-security.html): Learn how Amazon EMR on EKS isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/configuration-vulnerability.html): AWS handles basic security tasks like guest operating system (OS) and database patching, firewall configuration, and disaster recovery.
- [Interface VPC endpoints](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security-vpc.html): You can connect directly to Amazon EMR on EKS using Interface VPC endpoints (AWS PrivateLink) in your Virtual Private Cloud (VPC) instead of connecting over the internet.
- [Cross-account access](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security-cross-account.html): You can set up cross-account access for Amazon EMR on EKS.


## [Troubleshooting](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/troubleshooting.html)

- [PVC job failures](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/permissions-for-pvc.html): If you need to create, list, or delete PersistentVolumeClaims (PVC) for a job but don't add PVC permissions to the default Kubernetes role emr-containers, the job fails when you submit it.
- [Vertical autoscaling failures](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/troubleshooting-vas.html): Refer to the following sections if you encounter problems when you set up the Amazon EMR on EKS vertical autoscaling operator on an Amazon EKS cluster with Operator Lifecycle Manager.
- [Spark operator failures](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/troubleshooting-sparkop.html): Refer to the following sections if you encounter problems with the Amazon EMR on EKS Spark operator.


## [Release versions](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-releases.html)

### [7.12.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.12.0.html)

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment.

- [emr-7.12.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.12.0-latest.html): Release notes: emr-7.12.0-latest currently points to emr-7.12.0-20251111.
- [emr-7.12.0-20251111](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.12.0-20251111.html): Release notes: emr-7.12.0-20251111 was released in November 2025.
- [emr-7.12.0-flink-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.12.0-flink-latest.html): Release notes: emr-7.12.0-flink-latest currently points to emr-7.12.0-flink-20251111
- [emr-7.12.0-flink-20251111](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-7.12.0-flink-20251111.html): Release notes: 7.12.0-flink-20251111 was released in November 2025.

### [7.11.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.11.0.html)

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment.

- [emr-7.11.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.11.0-latest.html): Release notes: emr-7.11.0-latest currently points to emr-7.11.0-20251020.
- [emr-7.11.0-20251020](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.11.0-20251020.html): Release notes: emr-7.11.0-20251020 was released in November 2025.
- [emr-7.11.0-flink-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.11.0-flink-latest.html): Release notes: emr-7.11.0-flink-latest currently points to emr-7.11.0-flink-20251020
- [emr-7.11.0-flink-20251020](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-7.11.0-flink-20251020.html): Release notes: 7.11.0-flink-20251020 was released in November 2025.

### [7.10.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.10.0.html)

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment.

- [emr-7.10.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.10.0-latest.html): Release notes: emr-7.10.0-latest currently points to emr-7.10.0-20250801.
- [emr-7.10.0-20250801](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.10.0-20250801.html): Release notes: emr-7.10.0-20250801 was released in February 2025.
- [emr-7.10.0-flink-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.10.0-flink-latest.html): Release notes: emr-7.10.0-flink-latest currently points to emr-7.10.0-flink-20250801
- [emr-7.10.0-flink-20250801](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-7.10.0-flink-20250801.html): Release notes: 7.10.0-flink-20250801 was released in February 2025.

### [7.9.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.9.0.html)

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment.

- [emr-7.9.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.9.0-latest.html): Release notes: emr-7.9.0-latest currently points to emr-7.9.0-20250425.
- [emr-7.9.0-20250425](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.9.0-20250425.html): Release notes: emr-7.9.0-20250425 was released in February 2025.
- [emr-7.9.0-flink-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.9.0-flink-latest.html): Release notes: emr-7.9.0-flink-latest currently points to emr-7.9.0-flink-20250425
- [emr-7.9.0-flink-20250425](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-7.9.0-flink-20250425.html): Release notes: 7.9.0-flink-20250425 was released in February 2025.

### [7.8.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.8.0.html)

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment.

- [emr-7.8.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.8.0-latest.html): Release notes: emr-7.8.0-latest currently points to emr-7.8.0-20250228.
- [emr-7.8.0-20250228](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.8.0-20250228.html): Release notes: emr-7.8.0-20250228 was released in February 2025.
- [emr-7.8.0-flink-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.8.0-flink-latest.html): Release notes: emr-7.8.0-flink-latest currently points to emr-7.8.0-flink-20250228
- [emr-7.8.0-flink-20250228](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-7.8.0-flink-20250228.html): Release notes: 7.8.0-flink-20250228 was released in February 2025.

### [7.7.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.7.0.html)

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment.

- [emr-7.7.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.7.0-latest.html): Release notes: emr-7.7.0-latest currently points to emr-7.7.0-20250131.
- [emr-7.7.0-20250131](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.7.0-20250131.html): Release notes: emr-7.7.0-20250131 was released in February 2025.
- [emr-7.7.0-flink-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.7.0-flink-latest.html): Release notes: emr-7.7.0-flink-latest currently points to emr-7.7.0-flink-20250131
- [emr-7.7.0-flink-20250131](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-7.7.0-flink-20250131.html): Release notes: 7.7.0-flink-20250131 was released in February 2025.

### [7.6.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.6.0.html)

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment.

- [emr-7.6.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.6.0-latest.html): Release notes: emr-7.6.0-latest currently points to emr-7.6.0-20241213.
- [emr-7.6.0-20241213](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.6.0-20241213.html): Release notes: 7.6.0-20241213 was released in January, 2024.
- [emr-7.6.0-flink-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.6.0-flink-latest.html): Release notes: emr-7.6.0-flink-latest currently points to emr-7.6.0-flink-20241213
- [emr-7.6.0-flink-20241213](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.6.0-flink-20241213.html): Release notes: 7.6.0-flink-20241213 was released in January 2024.
- [7.5.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.5.0.html): This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment.
- [7.4.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.4.0.html): This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment.

### [7.3.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.3.0.html)

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment.

- [emr-7.3.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.3.0-latest.html): Release notes: emr-7.3.0-latest currently points to emr-7.3.0-20240920.
- [emr-7.3.0-20240920](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.3.0-29240920.html): Release notes: 7.3.0-20240920 was released in December, 2023.
- [emr-7.3.0-flink-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.3.0-flink-latest.html): Release notes: emr-7.3.0-flink-latest currently points to emr-7.3.0-flink-29240920.
- [emr-7.3.0-flink-29240920](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.3.0-flink-29240920.html): Release notes: 7.3.0-flink-29240920 was released in December 2023.

### [7.2.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.2.0.html)

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment.

- [emr-7.2.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.2.0-latest.html): Release notes: emr-7.2.0-latest currently points to emr-7.2.0-20240610.
- [emr-7.2.0-20240610](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.2.0-20240610.html): Release notes: 7.2.0-20240610 was released in December, 2023.
- [emr-7.2.0-flink-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.2.0-flink-latest.html): Release notes: emr-7.2.0-flink-latest currently points to emr-7.2.0-flink-20240610.
- [emr-7.2.0-flink-20240610](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.2.0-flink-20240610.html): Release notes: 7.2.0-flink-20240610 was released in December 2023.

### [7.1.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.1.0.html)

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment.

- [emr-7.1.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.1.0-latest.html): Release notes: emr-7.1.0-latest currently points to emr-7.1.0-20240321.
- [emr-7.1.0-20240321](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.1.0-20240321.html): Release notes: 7.1.0-20240321 was released in December, 2023.
- [emr-7.1.0-flink-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.1.0-flink-latest.html): Release notes: emr-7.1.0-flink-latest currently points to emr-7.1.0-flink-20240321.
- [emr-7.1.0-flink-20240321](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.1.0-flink-20240321.html): Release notes: 7.1.0-flink-20240321 was released in December 2023.

### [7.0.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.0.0.html)

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment.

- [emr-7.0.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.0.0-latest.html): Release notes: emr-7.0.0-latest currently points to emr-7.0.0-2024321.
- [emr-7.0.0-2024321](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.0.0-2024321.html): Release notes: 7.0.0-2024321 was released on March 11, 2024.
- [emr-7.0.0-20231211](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.0.0-20231211.html): Release notes: 7.0.0-20231211 was released in December, 2023.
- [emr-7.0.0-flink-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.0.0-flink-latest.html): Release notes: emr-7.0.0-flink-latest currently points to emr-7.0.0-flink-2024321.
- [emr-7.0.0-flink-2024321](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.0.0-flink-2024321.html): Release notes: 7.0.0-flink-2024321 was released on March 11, 2024.
- [emr-7.0.0-flink-20231211](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.0.0-flink-20231211.html): Release notes: 7.0.0-flink-20231211 was released in December 2023.

### [6.15.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.15.0.html)

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment.

- [emr-6.15.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.15.0-latest.html): Release notes: emr-6.15.0-latest currently points to emr-6.15.0-20240105.
- [emr-6.15.0-20240105](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.15.0-20240105.html): Release notes: 6.15.0-20240105 was released on January 17, 2024.
- [emr-6.15.0-20231109](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.15.0-20231109.html): Release notes: 6.15.0-20231109 was released on November 17, 2023.
- [emr-6.15.0-flink-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.15.0-flink-latest.html): Release notes: emr-6.15.0-flink-latest currently points to emr-6.15.0-flink-20240105.
- [emr-6.15.0-flink-20240105](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.15.0-flink-20240105.html): Release notes: 6.15.0-flink-20240105 was released on January 17, 2024.
- [emr-6.15.0-flink-20231109](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.15.0-flink-20231109.html): Release notes: 6.15.0-flink-20231109 was released on November 17, 2023.

### [6.14.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.14.0.html)

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment.

- [emr-6.14.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.14.0-latest.html): Release notes: emr-6.14.0-latest currently points to emr-6.14.0-20231005.
- [emr-6.14.0-20231005](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.14.0-20231005.html): Release notes: 6.14.0-20231005 was released on October 17, 2023.

### [6.13.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.13.0.html)

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment.

- [emr-6.13.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.13.0-latest.html): Release notes: emr-6.13.0-latest currently points to emr-6.13.0-20230814.
- [emr-6.13.0-20230814](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.13.0-20230814.html): Release notes: 6.13.0-20230814 was released on September 7, 2023.

### [6.12.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.12.0.html)

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment.

- [emr-6.12.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.12.0-latest.html): Release notes: emr-6.12.0-latest currently points to emr-6.12.0-20240321.
- [emr-6.12.0-20240321](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.12.0-20240321.html): Release notes: 6.12.0-20240321 was released on March 11, 2024.
- [emr-6.12.0-20230701](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.12.0-20230701.html): Release notes: 6.12.0-20230701 was released on July 1, 2023.

### [6.11.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.11.0.html)

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment.

- [emr-6.11.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.11.0-latest.html): Release notes: emr-6.11.0-latest currently points to emr-20230905.
- [emr-6.11.0-20230905](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.11.0-20230905.html): Release notes: 6.11.0-20230905 was released on September 29, 2023.
- [emr-6.11.0-20230509](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.11.0-20230509.html): Release notes: 6.11.0-20230509 was released on May 9, 2023.

### [6.10.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.10.0.html)

The following Amazon EMR 6.10.0 releases are available for Amazon EMR on EKS.

- [emr-6.10.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.10.0-latest.html): Release notes: emr-6.10.0-latest currently points to emr-6.10.0-20230905.
- [emr-6.10.0-20230905](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.10.0-20230905.html): Release notes: 6.10.0-20230905 was released on September 29, 2023.
- [emr-6.10.0-20230624](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.10.0-20230624.html): Release notes: 6.10.0-20230624 was released on July 7, 2023.
- [emr-6.10.0-20230421](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.10.0-20230421.html): Release notes: 6.10.0-20230421 was released on April 28, 2023.
- [emr-6.10.0-20230403](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.10.0-20230403.html): Release notes: 6.10.0-20230403 was released on April 12, 2023.
- [emr-6.10.0-20230220](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.10.0-20230220.html): Release notes: emr-6.10.0-20230220 was released on February 20, 2023.

### [6.9.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.9.0.html)

The following Amazon EMR 6.9.0 releases are available for Amazon EMR on EKS.

- [emr-6.9.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.9.0-latest.html): Release notes: emr-6.9.0-latest currently points to emr-6.9.0-20230905.
- [emr-6.9.0-20230905](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.9.0-20230905.html): Release notes: emr-6.9.0-20230905.
- [emr-6.9.0-20230624](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.9.0-20230624.html): Release notes: emr-6.9.0-20230624 was released on July 7, 2023.
- [emr-6.9.0-20221108](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.9.0-20221108.html): Release notes: emr-6.9.0-20221108 was released on December 08, 2022.

### [6.8.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.8.0.html)

The following Amazon EMR 6.8.0 releases are available for Amazon EMR on EKS.

- [emr-6.8.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.8.0-latest.html): Release notes: emr-6.8.0-latest currently points to emr-6.8.0-20230624.
- [emr-6.8.0-20230905](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.8.0-20230905.html): Release notes: emr-6.8.0-20230905 was released on September 29, 2023.
- [emr-6.8.0-20230624](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.8.0-20230624.html): Release notes: emr-6.8.0-20230624 was released on July 7, 2023.
- [emr-6.8.0-20221219](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.8.0-20221219.html): Release notes: emr-6.8.0-20221219 was released on Jan 19, 2023.
- [emr-6.8.0-20220802](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.8.0-20220802.html): Release notes: emr-6.8.0-20220802 was released on Sep 27, 2022.

### [6.7.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.7.0.html)

The following Amazon EMR 6.7.0 releases are available for Amazon EMR on EKS.

- [emr-6.7.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.7.0-latest.html): Release notes: emr-6.7.0-latest currently points to emr-6.7.0-20240321.
- [emr-6.7.0-20240321](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.7.0-20240321.html): Release notes: emr-6.7.0-20240321 was released on March 11, 2024.
- [emr-6.7.0-20230624](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.7.0-20230624.html): Release notes: emr-6.7.0-20230624 was released on July 7, 2023.
- [emr-6.7.0-20221219](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.7.0-20221219.html): Release notes: emr-6.7.0-20221219 was released on Jan. 19, 2023.
- [emr-6.7.0-20220630](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.7.0-20220630.html): Release notes: emr-6.7.0-20220630 was released on July 12, 2022.

### [6.6.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.6.0.html)

The following Amazon EMR 6.6.0 releases are available for Amazon EMR on EKS.

- [emr-6.6.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.6.0-latest.html): Release notes: emr-6.6.0-latest currently points to emr-6.6.0-20240321.
- [emr-6.6.0-20240321](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.6.0-20240321.html): Release notes: emr-6.6.0-20240321 was released on March 11, 2024.
- [emr-6.6.0-20230624](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.6.0-20230624.html): Release notes: emr-6.6.0-20230624 was released on Jan 27, 2023.
- [emr-6.6.0-20221219](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.6.0-20221219.html): Release notes: emr-6.6.0-20221219 was released on Jan 27, 2023.
- [emr-6.6.0-20220411](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.6.0-20220411.html): Release notes: emr-6.6.0-20220411 was released on May 20, 2022.

### [6.5.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.5.0.html)

The following Amazon EMR 6.5.0 releases are available for Amazon EMR on EKS.

- [emr-6.5.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.5.0-latest.html): Release notes: emr-6.5.0-latest currently points to emr-6.5.0-20240321.
- [emr-6.5.0-20240321](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.5.0-20240321.html): Release notes: emr-6.5.0-20240321 was released on March 11, 2024.
- [emr-6.5.0-20221219](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.5.0-20221219.html): Release notes: emr-6.5.0-20221219 was released on Jan 19, 2023.
- [emr-6.5.0-20220802](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.5.0-20220802.html): Release notes: emr-6.5.0-20220802 was released on Aug 24, 2022.
- [emr-6.5.0-20211119](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.5.0-20211119.html): Release notes: emr-6.5.0-20211119 was released on Jan 20, 2022.

### [6.4.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.4.0.html)

The following Amazon EMR 6.4.0 releases are available for Amazon EMR on EKS.

- [emr-6.4.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.4.0-latest.html): Release notes: emr-6.4.0-latest currently points to emr-6.4.0-20240321.
- [emr-6.4.0-20240321](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.4.0-20240321.html): Release notes: emr-6.4.0-20240321 was released on March 11, 2024.
- [emr-6.4.0-20221219](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.4.0-20221219.html): Release notes: emr-6.4.0-20221219 was released on Jan 27, 2023.
- [emr-6.4.0-20210830](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.4.0-20210830.html): Release notes: emr-6.4.0-20210830 was released on Dec 9, 2021.

### [6.3.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.3.0.html)

The following Amazon EMR 6.3.0 releases are available for Amazon EMR on EKS.

- [emr-6.3.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.3.0-latest.html): Release notes: emr-6.3.0-latest currently points to emr-6.3.0-20240321.
- [emr-6.3.0-20240321](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.3.0-20240321.html): Release notes: emr-6.3.0-20240321 was released on March 11, 2024.
- [emr-6.3.0-20220802](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.3.0-20220802.html): Release notes: emr-6.3.0-20220802 was released on Sep 27, 2022.
- [emr-6.3.0-20211008](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.3.0-20211008.html): Release notes: emr-6.3.0-20211008 was released on Dec 9, 2021.
- [emr-6.3.0-20210802](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.3.0-20210802.html): Release notes: emr-6.3.0-20210802 was released on Aug 2, 2021.
- [emr-6.3.0-20210429](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.3.0-20210429.html): Release notes: emr-6.3.0-20210429 was released on April 29, 2021.

### [6.2.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.2.0.html)

The following Amazon EMR 6.2.0 releases are available for Amazon EMR on EKS.

- [emr-6.2.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.2.0-latest.html): Release notes: emr-6.2.0-latest currently points to emr-6.2.0-20240321.
- [emr-6.2.0-20240321](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.2.0-20240321.html): Release notes: emr-6.2.0-20240321 was released on March 11, 2024.
- [emr-6.2.0-20220802](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.2.0-20220802.html): Release notes: emr-6.2.0-20220802 was released on Sep 27, 2022.
- [emr-6.2.0-20211008](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.2.0-20211008.html): Release notes: emr-6.2.0-20211008 was released on Dec 9, 2021.
- [emr-6.2.0-20210802](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.2.0-20210802.html): Release notes: emr-6.2.0-20210802 was released on Aug 2, 2021.
- [emr-6.2.0-20210615](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.2.0-20210615.html): Release notes: emr-6.2.0-20210615 was released on June 15, 2021.
- [emr-6.2.0-20210129](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.2.0-20210129.html): Release notes: emr-6.2.0-20210129 was released on January 29, 2021.
- [emr-6.2.0-20201218](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.2.0-20201218.html): Release notes: emr-6.2.0-20201218 was released on December 18, 2020.
- [emr-6.2.0-20201201](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.2.0-20201201.html): Release notes: emr-6.2.0-20201201 was released on December 1, 2020.

### [5.36.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.36.0.html)

The following Amazon EMR 5.36.0 releases are available for Amazon EMR on EKS.

- [emr-5.36.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.36.0-latest.html): Release notes: emr-5.36.0-latest currently points to emr-5.36.0-20240321.
- [emr-5.36.0-20240321](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.36.0-20240321.html): Release notes: emr-5.36.0-20240321 was released on March 11, 2024.
- [emr-5.36.0-20221219](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.36.0-20221219.html): Release notes: emr-5.36.0-20221219 was released on Jan 27, 2023.
- [emr-5.36.0-20220620](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.36.0-20220620.html): Release notes: emr-5.36.0-20220620 was released on July 27, 2022.
- [emr-5.36.0-20220525](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.36.0-20220525.html): Release notes: emr-5.36.0-20220525 was released on June 16, 2022.

### [5.35.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.35.0.html)

The following Amazon EMR 5.35.0 releases are available for Amazon EMR on EKS.

- [emr-5.35.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.35.0-latest.html): Release notes: emr-5.35.0-latest currently points to emr-5.35.0-20240321.
- [emr-5.35.0-20240321](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.35.0-20240321.html): Release notes: emr-5.35.0-20240321 was released on March 11, 2024.
- [emr-5.35.0-20221219](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.35.0-20221219.html): Release notes: emr-5.35.0-20221219 was released on Jan 27, 2023.
- [emr-5.35.0-20220802](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.35.0-20220802.html): Release notes: emr-5.35.0-20220802 was released on Sep 27, 2022.
- [emr-5.35.0-20220307](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.35.0-20220307.html): Release notes: emr-5.35.0-20220307 was released on Mar 30, 2022.

### [5.34 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.34.0.html)

The following Amazon EMR 5.34.0 releases are available for Amazon EMR on EKS.

- [emr-5.34.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.34.0-latest.html): Release notes: emr-5.34.0-latest currently points to emr-5.34.0-20220802.
- [emr-5.34.0-20240321](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.34.0-20240321.html): Release notes: emr-5.34.0-20240321 was released on March 11, 2024.
- [emr-5.34.0-20220802](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.34.0-20220802.html): Release notes: emr-5.34.0-20220802 was released on Aug 24, 2022.
- [emr-5.34.0-20211208](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.34.0-20211208.html): Release notes: emr-5.34.0-20211208 was released on Jan 20, 2022.

### [5.33.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.33.0.html)

The following Amazon EMR 5.33.0 releases are available for Amazon EMR on EKS.

- [emr-5.33.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.33.0-latest.html): Release notes: emr-5.33.0-latest currently points to emr-5.33.0-20240321.
- [emr-5.33.0-20240321](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.33.0-20240321.html): Release notes: emr-5.33.0-20240321 was released on March 11, 2024.
- [emr-5.33.0-20221219](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.33.0-20221219.html): Release notes: emr-5.33.0-20221219 was released on Jan 19, 2023.
- [emr-5.33.0-20220802](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.33.0-20220802.html): Release notes: emr-5.33.0-20220802 was released on Aug 24, 2022.
- [emr-5.33.0-20211008](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.33.0-20211008.html): Release notes: emr-5.33.0-20211008 was released on Dec 9, 2021.
- [emr-5.33.0-20210802](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.33.0-20210802.html): Release notes: emr-5.33.0-20210802 was released on Aug 2, 2021.
- [emr-5.33.0-20210615](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.33.0-20210615.html): Release notes: emr-5.33.0-20210615 was released on June 15, 2021.
- [emr-5.33.0-20210323](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.33.0-20210323.html): Release notes: emr-5.33.0-20210323 was released on March 23, 2021.

### [5.32.0 releases](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.32.0.html)

The following Amazon EMR 5.32.0 releases are available for Amazon EMR on EKS.

- [emr-5.32.0-latest](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.32.0-latest.html): Release notes: emr-5.32.0-latest currently points to emr-5.32.0-20240321.
- [emr-5.32.0-20240321](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.32.0-20240321.html): Release notes: emr-5.32.0-20240321 was released on March 11, 2024.
- [emr-5.32.0-20220802](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.32.0-20220802.html): Release notes: emr-5.32.0-20220802 was released on Aug 24, 2022.
- [emr-5.32.0-20211008](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.32.0-20211008.html): Release notes: emr-5.32.0-20211008 was released on Dec 9, 2021.
- [emr-5.32.0-20210802](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.32.0-20210802.html): Release notes: emr-5.32.0-20210802 was released on Aug 2, 2021.
- [emr-5.32.0-20210615](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.32.0-20210615.html): Release notes: emr-5.32.0-20210615 was released on June 15, 2021.
- [emr-5.32.0-20210129](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.32.0-20210129.html): Release notes: emr-5.32.0-20210129 was released on January 29, 2021.
- [emr-5.32.0-20201218](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.32.0-20201218.html): Release notes: 5.32.0-20201218 was released on December 18, 2020.
- [emr-5.32.0-20201201](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-5.32.0-20201201.html): Release notes: 5.32.0-20201201 was released on December 1, 2020.
