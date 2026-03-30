# Source: https://help.aikido.dev/virtual-machine-scanning/aws/aws-ec2-virtual-machine-scanning-setup.md

# AWS EC2 Virtual Machine Scanning Setup

{% hint style="info" %}
This functionality is available for **Pro** and **Advanced** plans only. [Contact us](https://www.aikido.dev/contact) for more information.
{% endhint %}

### Why should I scan my virtual machines? <a href="#why-should-i-scan-my-virtual-machines" id="why-should-i-scan-my-virtual-machines"></a>

With virtual machine scanning, Aikido scans the disks of your virtual machines for vulnerable packages, outdated runtimes and risky licenses.

### Getting started <a href="#getting-started" id="getting-started"></a>

To enable the scanning of your Amazon EC2 instances, you should first start by connecting your AWS account to Aikido. To do this you can follow the steps outlined in [this article](https://help.aikido.dev/cloud-scanning/connect-your-cloud/aws/connect-aws-account-to-aikido).

Once your cloud is connected, you'll see a tab appear on the detail page called 'Virtual Machines'.

![Activate VM scanning for AWS EC2 instances to detect open-source dependency issues.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-b1ff4ee64a6904ff2058d2d17a57b41090113884%2Faws-ec2-virtual-machine-scanning-setup_5009bb66-9945-408a-a7c5-37fd3c8bc531.png?alt=media)

When you click on 'Set Up VM Scanning' we'll take you to the following page:

![AWS EC2 volume scanning setup with IAM role and policy creation instructions.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-50373f3f9b53fa12cdff94d558dfd543dc1eef3d%2Faws-ec2-virtual-machine-scanning-setup_c0f27d23-d8bc-4379-85d1-d6b3ac77d3ab.png?alt=media)

On this page, you can set up the virtual machine scanning via an AWS CloudFormation template that should be applied in the account of the virtual machines that you'd like to have scanned. The CloudFormation template will create a role with limited access to your AWS account. It's important to **KEEP** any permissions from the role as this is the absolute minimum that Aikido needs to perform the scans.

Once the CloudFormation resources have been created, you'll see the ARN of the role in AWS that was created. Copy it and add into the input field on the set up screen. Once you click 'save', Aikido will immediately start to discover any virtual machines in your account and scan them.

## VM Grouping <a href="#getting-started" id="getting-started"></a>

To optimize scanning efficiency, Aikido groups certain EC2 instances and scans only one instance from each group. Grouping works as follows:

* **Auto Scaling Groups (ASG)**: All EC2 instances in the same AWS Auto Scaling Group are shown as a single VM group in Aikido. The VM group’s name matches the ASG name.
* **Karpenter Node Pools**: All EC2 instances that belong to the same Karpenter node pool within an EKS cluster are grouped together. The VM group’s name matches the instance name pattern used by Karpenter.
* **No grouping**: EC2 instances that are not part of an ASG or Karpenter node pool are treated as standalone VMs and scanned individually.

## Managing which VM's are scanned <a href="#managing-which-vms-are-scanned" id="managing-which-vms-are-scanned"></a>

Aikido supports [inclusion and exclusion model for VM scanning](https://help.aikido.dev/virtual-machine-scanning/aws/managing-which-vms-are-scanned).&#x20;
