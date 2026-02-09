# Creating and managing instances -

Source: https://docs.lambda.ai/public-cloud/on-demand/creating-managing-instances/

---

[on-demand cloud](../../../tags/#tag:on-demand-cloud)

# Creating and managing instances

This doc outlines how to create and manage On-Demand Cloud (ODC) instances. For general guidance on managing your ODC instance's system environment, see [Managing your system environment](../managing-system-environment/).

## Viewing available instance types

To view available instance types, navigate to the [Instances page](https://cloud.lambda.ai/instances) in the Lambda Cloud console and click **Launch instance** to start the instance creation wizard. The first page of the wizard dialog lists all of the instance types Lambda currently offers.

You can also programmatically view available instance types by using the Lambda Cloud API. For details, see [List available instance types](https://docs.lambda.ai/api/cloud#listInstanceTypes) in the Lambda Cloud API browser.

## Launching instances

To launch a new instance, navigate to the [Instances page](https://cloud.lambda.ai/instances) in the Lambda Cloud console, click **Launch instance**, and then follow the steps in the instance creation wizard.

You can also launch instances programmatically by using the Lambda Cloud API. For details, see [Launch instances](https://docs.lambda.ai/api/cloud#launchInstance) in the Lambda Cloud API browser.

Instances might take several minutes to launch.

Note

New accounts have a limit on the number of instances you can launch. This quota helps prevent abuse and increases automatically as you pay your invoices. If you attempt to launch an instance that exceeds this limit, you will see a notification that your quota has been reached.
