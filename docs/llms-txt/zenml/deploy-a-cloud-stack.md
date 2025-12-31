# Source: https://docs.zenml.io/stacks/deployment/deploy-a-cloud-stack.md

# 1-click Deployment

In ZenML, the [stack](https://docs.zenml.io/user-guides/production-guide/understand-stacks) is a fundamental concept that represents the configuration of your infrastructure. In a normal workflow, creating a stack requires you to first deploy the necessary pieces of infrastructure and then define them as stack components in ZenML with proper authentication.

Especially in a remote setting, this process can be challenging and time-consuming, and it may create multi-faceted problems. This is why we implemented a feature that allows you to **deploy the necessary pieces of infrastructure on your selected cloud provider and get you started on a remote stack with a single click**.

{% hint style="info" %}
If you prefer to have more control over where and how resources are provisioned in your cloud, you can [use one of our Terraform modules](https://docs.zenml.io/stacks/deployment/deploy-a-cloud-stack-with-terraform) to manage your infrastructure as code yourself.

If you have the required infrastructure pieces already deployed on your cloud, you can also use [the stack wizard to seamlessly register your stack](https://docs.zenml.io/how-to/infrastructure-deployment/stack-deployment/register-a-cloud-stack).
{% endhint %}

## How to use the 1-click deployment tool?

The first thing that you need in order to use this feature is a deployed instance of ZenML (not a local server via `zenml login --local`). If you do not already have it set up for you, feel free to learn how to do so [here](https://docs.zenml.io/getting-started/deploying-zenml).

Once you are connected to your deployed ZenML instance, you can use the 1-click deployment tool either through the dashboard or the CLI:

{% tabs %}
{% tab title="Dashboard" %}
In order to create a remote stack over the dashboard, go to the stacks page\
on the dashboard and click "+ New Stack".

![The new stacks page](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-a7a2cfa4371821001a4136a18e53a3db038b5e1c%2Fregister_stack_button.png?alt=media)

Since we will be deploying it from scratch, select "New Infrastructure" on the\
next page:

![Options for registering a stack](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-e70d30a102bd18b0008985e0530e374a2e859fd7%2Fregister_stack_page.png?alt=media)

![Choosing a cloud provider](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-c788edec6587ffb1dd71d099a3916329174b33c7%2Fdeploy_stack_selection.png?alt=media)

<details>

<summary>AWS</summary>

If you choose `aws` as your provider, you will see a page where you will have to select a region and a name for your new stack:

<img src="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-d0fb71198d35ccdd6bec1278bdcfd34cacfcffbb%2Fdeploy_stack_aws.png?alt=media" alt="Configuring the new stack" data-size="original">

Once the configuration is finished, you will see a deployment page:

<img src="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-38c704c148e67d726646a625a382721e85c56060%2Fdeploy_stack_aws_2.png?alt=media" alt="Deploying the new stack" data-size="original">

Clicking on the "Deploy in AWS" button will redirect you to a Cloud Formation page on AWS Console.

<img src="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-39bb6642cf681b720a3d0203507584fe1ddc1d14%2Fdeploy_stack_aws_cloudformation_intro.png?alt=media" alt="Cloudformation page" data-size="original">

You will have to log in to your AWS account, review and confirm the pre-filled configuration, and create the stack.

<img src="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-43c5b4531752fbecde53bf61e9653a56cdfa3158%2Fdeploy_stack_aws_cloudformation.png?alt=media" alt="Finalizing the new stack" data-size="original">

</details>

<details>

<summary>GCP</summary>

If you choose `gcp` as your provider, you will see a page where you will have to select a region and a name for your new stack:

![Deploy GCP Stack - Step 1](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-d5ce639f20d519ba9156c7d4323f0db1e8322fc4%2Fdeploy_stack_gcp.png?alt=media) ![Deploy GCP Stack - Step 1 Continued](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-e71025b5d9a7e7f12b8f8c24223feed49ee45adb%2Fdeploy_stack_gcp_2.png?alt=media)

Once the configuration is finished, you will see a deployment page:

<img src="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-7ddf5841e2efd6749fe847be98c864145693a551%2Fdeploy_stack_gcp_3.png?alt=media" alt="Deploy GCP Stack - Step 2" data-size="original">

Make a note of the configuration values provided to you in the ZenML dashboard. You will need these in the next step.

Clicking on the "Deploy in GCP" button will redirect you to a Cloud Shell session on GCP.

<img src="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-ed8f73a3a937ade18b481f62bea5a338f3ca1393%2Fdeploy_stack_gcp_cloudshell_start.png?alt=media" alt="GCP Cloud Shell start page" data-size="original">

{% hint style="warning" %}
The Cloud Shell session will warn you that the ZenML GitHub repository is untrusted. We recommend that you review [the contents of the repository](https://github.com/zenml-io/zenml/tree/main/infra/gcp) and then check the `Trust repo` checkbox to proceed with the deployment, otherwise, the Cloud Shell session will not be authenticated to access your GCP projects. You will also get a chance to review the scripts that will be executed in the Cloud Shell session before proceeding.
{% endhint %}

<img src="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-e99f5a086f392992950b64ff90d15cde3be26fe7%2Fdeploy_stack_gcp_cloudshell_intro.png?alt=media" alt="GCP Cloud Shell intro" data-size="original">

After the Cloud Shell session starts, you will be guided through the process of authenticating with GCP, configuring your deployment, and finally provisioning the resources for your new GCP stack using Deployment Manager.

First, you will be asked to create or choose an existing GCP project with billing enabled and to configure your terminal with the selected project:

<img src="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-04d01c4e1bff0bf4c9b26bbabcac9c096d4f3bca%2Fdeploy_stack_gcp_cloudshell_step_1.png?alt=media" alt="GCP Cloud Shell tutorial step 1" data-size="original">

Next, you will be asked to configure your deployment by pasting the configuration values that were provided to you earlier in the ZenML dashboard. You may need to switch back to the ZenML dashboard to copy these values if you did not do so earlier:

![GCP Cloud Shell tutorial step 2](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-906643c778c72b6f3161f277f488cf39d5c0bd5a%2Fdeploy_stack_gcp_cloudshell_step_2.png?alt=media) ![Deploy GCP Stack pending](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-2b99461b66a00fe65214b9aa6e1ef6be3fcbf6f3%2Fdeploy_stack_pending.png?alt=media)

You can take this opportunity to review the script that will be executed at the next step. You will notice that this script starts by enabling some necessary GCP service APIs and configuring some basic permissions for the service accounts involved in the stack deployment, and then deploys the stack using a GCP Deployment Manager template. You can proceed with the deployment by running the script in your terminal:

<img src="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-569033b1401b1c356efcda3d691819d423e0499e%2Fdeploy_stack_gcp_cloudshell_step_3.png?alt=media" alt="GCP Cloud Shell tutorial step 3" data-size="original">

The script will deploy a GCP Deployment Manager template that provisions the necessary resources for your new GCP stack and automatically registers the stack with your ZenML server. You can monitor the progress of the deployment in your GCP console:

<img src="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-f2a81aedc1f42ef2ce3fec55798ad78c1725997b%2Fdeploy_stack_gcp_dm_progress.png?alt=media" alt="GCP Deployment Manager progress" data-size="original">

Once the deployment is complete, you may close the Cloud Shell session and return to the ZenML dashboard to view the newly created stack:

![GCP Cloud Shell tutorial step 4](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-6a67ac24ab6d61d6e038680a06ac0b071b499e8c%2Fdeploy_stack_gcp_cloudshell_step_4.png?alt=media) ![GCP Stack dashboard output](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-61b26e935b8aa73c46187797e7121fbafdbb93de%2Fdeploy_stack_gcp_dashboard_output.png?alt=media)

</details>

<details>

<summary>Azure</summary>

If you choose `azure` as your provider, you will see a page where you will have to select a location and a name for your new stack:

<img src="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-924cb5b954c560575b7ce1c9283d4a32dc3c6d19%2Fdeploy_stack_azure_location.png?alt=media" alt="Deploy Azure Stack - Step 1" data-size="original">

You will also find a list of resources that will be deployed as part of the stack:

<img src="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-dbaa5a7bd347f62f02412855de6b4892c6cb042d%2Fdeploy_stack_azure_resources.png?alt=media" alt="Deploy Azure Stack - Step 1 Continued" data-size="original">

Once the configuration is finished, you will see a deployment page. Make a note of the values in the `main.tf` file that is provided to you.

<img src="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-0365c2eca95a0c23cf9c982a2f2b98ecbc7920b5%2Fdeploy_stack_azure_deployment_page.png?alt=media" alt="Deploy Azure Stack - Step 2" data-size="original">

Clicking on the "Deploy in Azure" button will redirect you to a Cloud Shell session on Azure.

<img src="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-cc4d6cae2db79eeb7280398926f2180dc6c07f43%2Fdeploy_stack_azure_cloud_shell.png?alt=media" alt="Azure Cloud Shell start page" data-size="original">

You should now paste the content of the `main.tf` file into a file in the Cloud Shell session and run the `terraform init --upgrade` and `terraform apply` commands.

The `main.tf` file uses the `zenml-io/zenml-stack/azure` module hosted on the Terraform registry to deploy the necessary resources for your Azure stack and then automatically registers the stack with your ZenML server. You can check out the module documentation [here](https://registry.terraform.io/modules/zenml-io/zenml-stack/azure).

<img src="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-347ec9ebd69059facfd85c02da931d8f59b0f6fc%2Fdeploy_stack_azure_cloud_shell_terraform_outputs.png?alt=media" alt="Azure Cloud Shell Terraform Outputs" data-size="original">

Once the Terraform deployment is complete, you may close the Cloud Shell session and return to the ZenML Dashboard to view the newly created stack:

<img src="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-0ca4b347ad559ec16d6071c9f378bcb3b79743d0%2Fdeploy_stack_azure_dashboard_output.png?alt=media" alt="Azure Stack Dashboard output" data-size="original">

</details>
{% endtab %}

{% tab title="CLI" %}
In order to create a remote stack over the CLI, you can use the following\
command:

```shell
zenml stack deploy -p {aws|gcp|azure}
```

**AWS**

If you choose `aws` as your provider, the command will walk you through deploying a Cloud Formation stack on AWS. It will start by showing some information about the stack that will be created:

![CLI AWS stack deploy](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-b3d5c3b09b1ce6b5355ad6c74c6433b39a703039%2Fdeploy_stack_aws_cli.png?alt=media)

Upon confirmation, the command will redirect you to a Cloud Formation page on AWS Console where you will have to deploy the stack:

![Cloudformation page](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-39bb6642cf681b720a3d0203507584fe1ddc1d14%2Fdeploy_stack_aws_cloudformation_intro.png?alt=media)

You will have to log in to your AWS account, have permission to deploy an AWS Cloud Formation stack, review and confirm the pre-filled configuration and create the stack.

![Finalizing the new stack](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-43c5b4531752fbecde53bf61e9653a56cdfa3158%2Fdeploy_stack_aws_cloudformation.png?alt=media)

The Cloud Formation stack will provision the necessary resources for your new\
AWS stack and automatically register the stack with your ZenML server. You can\
monitor the progress of the stack in your AWS console:

![AWS Cloud Formation progress](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-b1d2ba25ecb5d6a87991fc6f91f37bc111c19b79%2Fdeploy_stack_aws_cf_progress.png?alt=media)

Once the provisioning is complete, you may close the AWS Cloud Formation page\
and return to the ZenML CLI to view the newly created stack:

![AWS Stack CLI output](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-fd71bd5a4835b2b4013388b2d44f89598fd031d4%2Fdeploy_stack_aws_cli_output.png?alt=media)

**GCP**

If you choose `gcp` as your provider, the command will walk you through deploying a Deployment Manager template on GCP. It will start by showing some information about the stack that will be created:

![CLI GCP stack deploy](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-c4b36e83a68271dcf85c08d6988210f8d2b4aee4%2Fdeploy_stack_gcp_cli.png?alt=media)

Upon confirmation, the command will redirect you to a Cloud Shell session on GCP.

![GCP Cloud Shell start page](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-ed8f73a3a937ade18b481f62bea5a338f3ca1393%2Fdeploy_stack_gcp_cloudshell_start.png?alt=media)

{% hint style="warning" %}
The Cloud Shell session will warn you that the ZenML GitHub repository is untrusted. We recommend that you review [the contents of the repository](https://github.com/zenml-io/zenml/tree/main/infra/gcp) and then check the `Trust repo` checkbox to proceed with the deployment, otherwise the Cloud Shell session will not be authenticated to access your GCP projects. You will also get a chance to review the scripts that will be executed in the Cloud Shell session before proceeding.
{% endhint %}

![GCP Cloud Shell intro](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-e99f5a086f392992950b64ff90d15cde3be26fe7%2Fdeploy_stack_gcp_cloudshell_intro.png?alt=media)

After the Cloud Shell session starts, you will be guided through the process of authenticating with GCP, configuring your deployment, and finally provisioning the resources for your new GCP stack using Deployment Manager.

First, you will be asked to create or choose an existing GCP project with billing enabled and to configure your terminal with the selected project:

![GCP Cloud Shell tutorial step 1](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-04d01c4e1bff0bf4c9b26bbabcac9c096d4f3bca%2Fdeploy_stack_gcp_cloudshell_step_1.png?alt=media)

Next, you will be asked to configure your deployment by pasting the configuration values that were provided to you in the ZenML CLI. You may need to switch back to the ZenML CLI to copy these values if you did not do so earlier:

![GCP Cloud Shell tutorial step 2](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-906643c778c72b6f3161f277f488cf39d5c0bd5a%2Fdeploy_stack_gcp_cloudshell_step_2.png?alt=media)

You can take this opportunity to review the script that will be executed at the next step. You will notice that this script starts by enabling some necessary GCP service APIs and configuring some basic permissions for the service accounts involved in the stack deployment, and then deploys the stack using a GCP Deployment Manager template. You can proceed with the deployment by running the script in your terminal:

![GCP Cloud Shell tutorial step 3](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-569033b1401b1c356efcda3d691819d423e0499e%2Fdeploy_stack_gcp_cloudshell_step_3.png?alt=media)

The script will deploy a GCP Deployment Manager template that provisions the necessary resources for your new GCP stack and automatically registers the stack with your ZenML server. You can monitor the progress of the deployment in your GCP console:

![GCP Deployment Manager progress](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-f2a81aedc1f42ef2ce3fec55798ad78c1725997b%2Fdeploy_stack_gcp_dm_progress.png?alt=media)

Once the deployment is complete, you may close the Cloud Shell session and return to the ZenML CLI to view the newly created stack:

![GCP Cloud Shell tutorial step 4](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-6a67ac24ab6d61d6e038680a06ac0b071b499e8c%2Fdeploy_stack_gcp_cloudshell_step_4.png?alt=media)

![GCP Stack CLI output](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-1054d6bb51f00adcfc0594e99f235a60409e90c9%2Fdeploy_stack_gcp_cli_output.png?alt=media)

**Azure**

If you choose `azure` as your provider, the command will walk you through deploying [the ZenML Azure Stack Terraform module](https://registry.terraform.io/modules/zenml-io/zenml-stack/azure). It will start by showing some information about the stack that will be created:

![CLI Azure stack deploy](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-d1a81e7856b5dae36f06c3208bc7ba04225f45eb%2Fdeploy_stack_azure_cli.png?alt=media)

Upon confirmation, the command will redirect you to a Cloud Shell session on Azure.

![Azure Cloud Shell page](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-a48febc0f78e4d27be00598a7194350e09010fe1%2Fdeploy_stack_azure_cloudshell.png?alt=media)

After the Cloud Shell session starts, you will have to use Terraform to deploy the stack, as instructed by the CLI.

First, you will have to open a file named `main.tf` in the Cloud Shell session using the editor of your choice (e.g. `vim`, `nano`) and paste in the Terraform configuration provided by the CLI. You may need to switch back to the ZenML CLI to copy these values if you did not do so earlier:

![Azure Cloud Shell Terraform Configuration File](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-75c3b33cb4e462e6a39d5cd50d7451f7ef66940d%2Fdeploy_stack_azure_cloudshell_create_file.png?alt=media)

The Terraform file is a simple configuration that uses [the ZenML Azure Stack Terraform module](https://registry.terraform.io/modules/zenml-io/zenml-stack/azure) to deploy the necessary resources for your Azure stack and then automatically register the stack with your ZenML server. You can read more about the module and its configuration options in the module's documentation.

You can proceed with the deployment by running the `terraform init` and`terraform apply` Terraform commands in your terminal:

![Azure Cloud Shell Terraform Init](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-31d9f0f3b86a24c45da042b6e476b3aa7ea0bffc%2Fdeploy_stack_azure_cloudshell_terraform_init.png?alt=media) ![Azure Cloud Shell Terraform Apply](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-5f3bf869adaebfdd3d385e345701e8a8b1add57d%2Fdeploy_stack_azure_cloudshell_terraform_apply.png?alt=media)

Once the Terraform deployment is complete, you may close the Cloud Shell session and return to the ZenML CLI to view the newly created stack:

![Azure Cloud Shell Terraform Outputs](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-436957ee170798ad4673c956dd1e022528bf0dd9%2Fdeploy_stack_azure_cloudshell_terraform_ouputs.png?alt=media) ![Azure Stack CLI output](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-f3caea4651d6ba426af2cbf58acc246e8582d5ad%2Fdeploy_stack_azure_cli_output.png?alt=media)
{% endtab %}
{% endtabs %}

## What will be deployed?

Here is an overview of the infrastructure that the 1-click deployment will prepare for you based on your cloud provider:

{% tabs %}
{% tab title="AWS" %}
**Resources**

* An S3 bucket that will be used as a ZenML Artifact Store.
* An ECR container registry that will be used as a ZenML Container Registry.
* A CloudBuild project that will be used as a ZenML Image Builder.
* Permissions to use SageMaker as a ZenML Orchestrator and Step Operator.
* An IAM user and IAM role with the minimum necessary permissions to access the resources listed above.
* An AWS access key used to give access to ZenML to connect to the above resources through a ZenML service connector.

**Permissions**

The configured IAM service account and AWS access key will grant ZenML the following AWS permissions in your AWS account:

* S3 Bucket:
  * s3:ListBucket
  * s3:GetObject
  * s3:PutObject
  * s3:DeleteObject
  * s3:GetBucketVersioning
  * s3:ListBucketVersions
  * s3:DeleteObjectVersion
* ECR Repository:
  * ecr:DescribeRepositories
  * ecr:ListRepositories
  * ecr:DescribeRegistry
  * ecr:BatchGetImage
  * ecr:DescribeImages
  * ecr:BatchCheckLayerAvailability
  * ecr:GetDownloadUrlForLayer
  * ecr:InitiateLayerUpload
  * ecr:UploadLayerPart
  * ecr:CompleteLayerUpload
  * ecr:PutImage
  * ecr:GetAuthorizationToken
* CloudBuild (Client):
  * codebuild:CreateProject
  * codebuild:BatchGetBuilds
* CloudBuild (Service):
  * s3:GetObject
  * s3:GetObjectVersion
  * logs:CreateLogGroup
  * logs:CreateLogStream
  * logs:PutLogEvents
  * ecr:BatchGetImage
  * ecr:DescribeImages
  * ecr:BatchCheckLayerAvailability
  * ecr:GetDownloadUrlForLayer
  * ecr:InitiateLayerUpload
  * ecr:UploadLayerPart
  * ecr:CompleteLayerUpload
  * ecr:PutImage
  * ecr:GetAuthorizationToken
* SageMaker (Client):
  * sagemaker:CreatePipeline
  * sagemaker:StartPipelineExecution
  * sagemaker:DescribePipeline
  * sagemaker:DescribePipelineExecution
* SageMaker (Jobs):
  * AmazonSageMakerFullAccess
    {% endtab %}

{% tab title="GCP" %}
**Resources**

* A GCS bucket that will be used as a ZenML Artifact Store.
* A GCP Artifact Registry that will be used as a ZenML Container Registry.
* Permissions to use Vertex AI as a ZenML Orchestrator and Step Operator.
* Permissions to use GCP Cloud Builder as a ZenML Image Builder.
* A GCP Service Account with the minimum necessary permissions to access the resources listed above.
* An GCP Service Account access key used to give access to ZenML to connect to the above resources through a ZenML service connector.

**Permissions**

The configured GCP service account and its access key will grant ZenML the following GCP permissions in your GCP project:

* GCS Bucket:
  * roles/storage.objectUser
* GCP Artifact Registry:
  * roles/artifactregistry.createOnPushWriter
* Vertex AI (Client):
  * roles/aiplatform.user
* Vertex AI (Jobs):
  * roles/aiplatform.serviceAgent
* Cloud Build (Client):
  * roles/cloudbuild.builds.editor
    {% endtab %}

{% tab title="Azure" %}
**Resources**

* An Azure Resource Group to contain all the resources required for the ZenML stack
* An Azure Storage Account and Blob Storage Container that will be used as a ZenML Artifact Store.
* An Azure Container Registry that will be used as a ZenML Container Registry.
* An AzureML Workspace that will be used as a ZenML Orchestrator and ZenML Step Operator. A Key Vault and Application Insights instance will also be created in the same Resource Group and used to construct the AzureML Workspace.
* An Azure Service Principal with the minimum necessary permissions to access the above resources.
* An Azure Service Principal client secret used to give access to ZenML to connect to the above resources through a ZenML service connector.

**Permissions**

The configured Azure service principal and its client secret will grant ZenML the following permissions in your Azure subscription:

* Permissions granted for the created Storage Account:
  * Storage Blob Data Contributor
* Permissions granted for the created Container Registry:
  * AcrPull
  * AcrPush
  * Contributor
* Permissions granted for the created AzureML Workspace:
  * AzureML Compute Operator
  * AzureML Data Scientist
    {% endtab %}
    {% endtabs %}

There you have it! With a single click, you just deployed a cloud stack, and you can start running your pipelines in a remote setting.

<figure><img src="https://static.scarf.sh/a.png?x-pxid=f0b4f458-0a54-4fcd-aa95-d5ee424815bc" alt="ZenML Scarf"><figcaption></figcaption></figure>
