# Source: https://docs.acceldata.io/documentation/dataplane-installation.md

# Data Plane Installation Guide

The **Data Plane** is the execution layer of ADOC that connects to your data sources and securely carries out tasks such as metadata crawling, data profiling, quality checks, and Spark job execution. It works in alignment with the access policies defined in the control plane, ensuring security and consistency. The Data Plane guide walks you through the complete installation process, from infrastructure setup to deployment and monitoring, so you can reliably extract insights and enforce data quality across your systems.

Before you begin, ensure all the [Data Plane Installation Prerequisites](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/dataplane-installation-prerequisites) are met.

Note **Data Plane V1** is deprecated and controlled by a feature flag. New instances cannot be created once the flag is deactivated. Existing instances can still be deleted. The UI defaults to the **Nextgen Data Plane**.

To begin setting up a Data Plane, follow these steps:

1. From the left navigation panel, click **Register**.
2. Select the **Data Planes** tab.
3. Click **Set Up Data Plane**.

After this, follow the on-screen steps to complete the configuration and deployment of your Data Plane.

## 1. Set Up Kubernetes Cluster

The Data Plane needs compute resources to run its services, such as data crawlers and Spark jobs. These services are deployed as pods inside a Kubernetes cluster. This step sets up that cluster in your cloud environment.

The Kubernetes cluster acts as a scalable, isolated, and managed compute layer for Data Plane operations. If you do not already have a cluster, you must create one before proceeding with Data Plane installation.

**Supported Cloud Providers**

| Cloud | Cluster Type | Why This Matters | 
| ---- | ---- | ---- | 
| AWS | EKS | Native integration with IAM, VPCs, and scalable auto-scaling groups. | 
| Azure | AKS | Simplifies RBAC configuration and integrates well with enterprise identity providers. | 
| GCP | GKE | Streamlined setup using service accounts and native GCP networking. | 
| Local | Minikube | Useful for testing, demos, or evaluating Data Plane in a local environment. Not recommended for production use. | 


Note To provision your Kubernetes cluster, refer to the cloud-specific guides below:

| Cloud Provider | Setup Documentation | 
| ---- | ---- | 
| AWS (EKS) | [Amazon EKS Setup Guide](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) | 
| Azure (AKS) | [Azure AKS Setup Guide](https://learn.microsoft.com/en-us/azure/aks/kubernetes-walkthrough-portal) | 
| GCP (GKE) | [Google GKE Setup Guide](https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster) | 
| Local (Minikube) | [Minikube Installation Guide](https://minikube.sigs.k8s.io/docs/start/) | 


**What You’re Doing**: You are provisioning the foundational infrastructure — including virtual machines, networking, and IAM or service account controls — that will host your Data Plane services.

## 2. Configure Data Plane

Once your Kubernetes cluster is ready, the next step is to register and configure your Data Plane in the control plane. This links your Data Plane to your selected environment and sets the foundation for deployment.

This step ensures that the control plane knows where and how to deploy your Data Plane services, and what version and container registry to use. These inputs define your compute environment, namespace, and versioned deployment strategy.

With ADOC v4.10.0, dataplanes now authenticate using **Service Users**, ensuring long-term stability and eliminating dependency on individual user credentials.

Dataplanes now use a **dedicated service user** for authentication instead of personal user API keys.
 This ensures:

- Dataplane connectivity remains stable
- User lifecycle changes (role changes, deactivation, key expiry) do not affect deployments
- Credentials can be rotated safely without interrupting running workloads

The “Service User” field is now required when configuring or updating a dataplane.

You will also see a key-expiry warning and a checkbox to rotate keys if needed.

**Steps to Configure your Data Plane:**

1. **Enter a unique Data Plane Name:** This name will help you identify and manage your Data Plane across environments.
2. **Specify the Namespace Name:** By default, this is set to default. You should change it if your Data Plane components are deployed in a different Kubernetes namespace, as the secret must exist in the same namespace where Data Plane is running.
3. **Select or enter the Version to install:** Choose a supported Data Plane release version. This ensures compatibility and avoids deployment issues.
4. **(Optional) Enter your own registry URL:** If you are hosting Data Plane container images in a private registry such as AWS ECR, enter the full registry path here. This supports internal security and DevSecOps compliance.
5. **(Optional) Enter a registry prefix:** This prefix is used to namespace the container image within your registry, especially useful when using shared repositories.
6. **Select a Service User**: Provide the service user that will authenticate the dataplane.
    - This replaces the use of personal API keys.
    - The system will show key expiry warnings and allow key rotation when needed.

7. **(Optional) Enable Rotate Keys**: Select this option if you want to regenerate dataplane API keys during the update. Rotation is safe and does not disrupt running pipelines.
8. Click **Create Data Plane**.

**What You’re Doing:** You are connecting your Kubernetes infrastructure with the control plane, providing key metadata like environment, namespace, and container image location. This prepares the system for actual deployment in the next step.

## 3. Deployment Config

Once the Data Plane has been registered, you must configure deployment-specific parameters. This step generates the _**values.yaml**_ file that defines runtime settings, including component behavior, network connectivity, observability, and log configurations.

This file is essential because it drives how the Helm chart will install Dataplane components into your Kubernetes cluster.

In the UI, you will be presented with a code editor to edit or paste in your custom YAML. By default, the editor is empty ({}), but you can enter the values specific to your environment.

To proceed:

1. Edit or paste the desired configuration in the values.yaml editor.
2. Click **Validate** to confirm that the YAML syntax is correct.
3. Click **Save and Next** to continue to the installation step.

If you're unsure what values to include, contact your DevOps administrator or refer to your environment-specific deployment checklist. The **values.yaml** file supports fine-tuning logs, autoscaling, observability options, and custom DNS/network policies.

**What You’re Doing:** You are preparing the core configuration file that instructs the installer how to deploy the Data Plane inside your Kubernetes environment. This ensures your setup is tailored to your infrastructure, compliance, and monitoring needs.

## 4. Install Data Plane

In this step, you will deploy the Data Plane components into your Kubernetes cluster. Based on your previous configuration, the platform generates a Kubernetes manifest file that defines all the necessary workloads and services.

You can choose between two installation types:

| Installation Type | Description | 
| ---- | ---- | 
| Automatic | The platform automatically applies the manifest file into your cluster. Recommended for users with direct CLI access and configured kubectl. | 
| Manual | You manually apply the generated manifest file using your terminal. Choose this if your access is restricted or managed through pipelines. | 


The system auto-detects your namespace. If it doesn’t exist, the command will create it before applying the deployment.

**Option 1: Automatic Installation**

1. Download the Manifest File

Click the **Copy** button to copy the generated Kubernetes manifest.

2. Apply the Manifest File
Use the following command to apply the manifest to your cluster. This command checks for the required namespace and creates it if it doesn’t exist, then deploys the Data Plane resources.

```bash
(kubectl get namespace default || kubectl create namespace default) && kubectl apply -f manifest.yaml -n default
```



This installs all required services like the Data Plane operator, Spark job handler, data crawlers, and metrics agents.

**Option 2: Manual Installation**

If you prefer manual installation using Helm, follow these steps:

1. Download the values.yaml file
This file contains configuration values for your Data Plane installation. It defines image sources, environment settings, and runtime options.
2. Download the Data Plane Helm chart
You will need the packaged Helm chart archive (acceldata-dataplane-2.0.0.tgz). This archive includes all Kubernetes manifests required to deploy the Data Plane services.
3. Run the Helm install command. 
4. Apply the Helm chart using the command below. This command ensures the Kubernetes namespace exists, and then installs the Data Plane:

```bash
(kubectl get namespace default || kubectl create namespace default) && \ helm install -f values.yaml dataplane acceldata-dataplane-2.0.0.tgz -n default
```



You can replace default with your own namespace if needed.

**What You’re Doing:** You are deploying the core services of the Data Plane into your Kubernetes environment. This step turns your YAML configuration into real workloads that crawl, scan, and process data from your registered sources.

## 5. Application Config

In this step, you configure how the Data Plane services should behave. These settings include which modules are enabled, how they connect to storage or secrets managers, and how Spark jobs run.

Application configuration defines the operational behavior of the Data Plane after its been deployed. You can update these settings anytime, but the initial configuration ensures that the Data Plane starts with the right setup for your environment.

**Global Configuration Overview**

| Setting | Value (Example) | Description | 
| ---- | ---- | ---- | 
| Global Storage | gcs | Defines where metadata files like DQ results and profiling reports are stored. \n\nFor information about how policy execution results are organized within the configured storage bucket (including suffix templates introduced in ADOC v26.3.0), see [Persistence Configuration](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/persistence-configuration). | 
| Secrets Manager Config Count | 3 | Indicates how many secrets managers are configured for the Dataplane. | 
| Spark Runtime | kubernetes | Specifies where Spark jobs will run. | 
| HDFS Enabled | Yes | HDFS access is enabled in the Dataplane. | 
| Hive Enabled | Yes | Hive metastore is supported and enabled. | 
| HBase Enabled | No | HBase integration is turned off. | 
| Kerberos Enabled | No | Kerberos authentication is not used. | 


**Configuration Types**

You can click to expand each category and modify specific fields. Here’s what each configuration type controls:

| Configuration Type | Description | 
| ---- | ---- | 
| Crawler | Controls how metadata is extracted from source systems. | 
| Profile | Defines thresholds and features for column-level profiling. | 
| Data Quality | Enables validation rules for datasets and fields. | 
| Reader | Configures how data is read from source systems. | 
| Asset Monitor | Tracks the health and availability of data assets. | 
| Secret Manager | Stores and retrieves credentials securely from supported secret managers. | 
| Global Storage | Defines file-based result storage for profile and quality outputs. | 
| Kerberos | Enables Kerberos-based access for secured Hadoop environments (if enabled earlier). | 
| Spark | Configures how Spark jobs run, including executor memory and CPU tuning. | 
| Others | Includes general-purpose and system-wide flags. | 
| Cluster Config | Advanced cluster-level configurations, such as logging or custom agents. | 


**What You’re Doing:** You are setting up how the Data Plane will behave in production. These configurations control how your Data Plane connects to data sources, processes metadata, runs Spark jobs, and manages results securely. Click **Apply Config** to finalize this step.