# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-security/eks.md

# EKS

{% hint style="success" %}
**At a glance:** Connect your EKS clusters to OX Security so we can map your organization's security vulnerabilities from code to cloud.
{% endhint %}

{% hint style="warning" %}
**Important!** Your OX organization must be connected to AWS before connecting to EKS.
{% endhint %}

## Overview

For the **OX Attack Path** feature to provide a full code-to-cloud map of your organization's security vulnerabilities, OX must be able to query individual Kubernetes clusters. To facilitate this integration for EKS, we have provided a Python utility (the **OX EKS connector script**) that executes the required conﬁguration processes.

For a description of the supported Kubernetes connection models, including direct cloud integration and Inspector-based access, see [Kubernetes Reachability](https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-security/kubernetes-reachability).

{% hint style="info" %}
**Best practices for using the script**

This article describes the steps for running the **OX EKS connector script**, which is downloadable from the OX platform. The script as provided is fully functional, but we recommend that you **don’t run it “as-is.”** Instead, provide it to your DevOps team to use as a reference for adapting the configuration to your environment or IaC (infrastructure as code) framework.
{% endhint %}

### What does the OX EKS connector script do? <a href="#what-does-the-script-do" id="what-does-the-script-do"></a>

The script performs the following key operations:

* Creates a dedicated namespace named `oxsecurity`.
* Creates a service account named `ox-service-account` within the `oxsecurity` namespace.
* Creates a read-only **ClusterRole** named `ox-security-read-only`.​
* Establishes a **ClusterRoleBinding** to link the `ox-security-read-only` role to the `ox-service-account`**.**
* Updates the **aws-auth conﬁgMap** to ensure proper IAM identity mapping between the `ox-security-read-only` role and the `ox-service-account`.

Note that the script:

* Does not install workloads into the cluster itself.
* Requires separate execution on each cluster.

## Running the **script** <a href="#running-the-ox-eks-connector-script" id="running-the-ox-eks-connector-script"></a>

{% hint style="warning" %}
Before you continue:

1. Ensure your OX organization is connected to AWS.
2. Install the following standard command-line utilities if they are not already installed:
   * AWS CLI
   * eksctl
   * kubectl

Additional details about these utilities are available on the [AWS documentation site](https://docs.aws.amazon.com/eks/latest/userguide/setting-up.html).
{% endhint %}

{% hint style="success" %}
**Tip:** The process for downloading and connecting using the **OX EKS connector script** includes steps in the OX platform and the AWS CLI. We recommend keeping both open as you complete the connection.
{% endhint %}

**To run the OX EKS connector script:**

**Part 1: Download the script**

1. From the OX side navigation menu, go to the **Connectors** page.
2. Search for `EKS` using the **Search** field in the upper-right corner of the page or scroll down to the **Kubernetes** section.
3. Click the EKS connector square <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-7e7f54334dcd7498820175769c890c50d43c82a9%2FEKS.png?alt=media" alt="" data-size="line">.
4. In the **Configure your EKS credentials** dialog, click the <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5cfbe47b27905786148d232186cc5b2cb445af80%2Fdownload_script_button.png?alt=media" alt="" data-size="line"> button.

**Part 2: Copy the AWS CLI command**

1. In the same dialog, click **INSTRUCTIONS: EKS CONNECTION.**
2. In the instructions that open, scroll down to find the command to run in the AWS CLI.\
   \
   ![](https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-33b1548ca5cb7bf81e301c1eb30b120a7b8bb19f%2Feks_script_command.png?alt=media)
   * The command looks similar to the following: `python eks_ox_onboarding.py --cluster {CLUSTER_NAME} --arn {YOUR_ORGANIZATION'S_ARN_VALUE} --region {REGION}`
3. Copy the command to a code or text editor.
4. In the command you copied:
   * Change `{CLUSTER_NAME}`and `{REGION}` to the correct values for the EKS cluster you're connecting.
   * We've already provided the value for the `--arn` parameter based on your OX AWS connection, so you shouldn't need to change it **except in the following circumstances:**
     * **Important!** If your OX AWS connection was set up using the **Organization** option *(see image below),* replace the AWS Account ID in the provided `--arn` parameter with the AWS Account ID of the EKS cluster you are connecting.\
       \
       ![](https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-11cad409a356eef7661cad6fa56f2d34162d34a4%2Faws_connector_organization_option.png?alt=media)

**Part 3: Connect your EKS clusters**

1. From the AWS CLI command prompt, run the command you copied (as modified according to the instructions above).
2. Run the script individually for each EKS cluster you are connecting, making the appropriate changes each time to the `{CLUSTER_NAME}`and `{REGION}` values (and, if necessary, to the `--arn` parameter, as discussed above).

**Part 4: Finalize the connection**

1. Once you've run the script for all relevant EKS clusters, return to the **Configure your EKS credentials** dialog in the OX platform.
   * If you've closed the dialog, reopen it by following steps 1-3 of Part 1, above.
2. Click the <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0ec8f1a7b795a6ca3e306fc07ae4608d1b0ee162%2Fconnect_button.png?alt=media" alt="" data-size="line"> button.
