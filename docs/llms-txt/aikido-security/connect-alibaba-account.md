# Source: https://help.aikido.dev/cloud-scanning/connect-your-cloud/alibaba-cloud-scanning/connect-alibaba-account.md

# Connect Alibaba Account

#### Why connect my Alibaba Cloud?

Securing your cloud infrastructure is crucial to protecting your user data. You can leverage Aikido's security checks to detect and address any misconfigurations in your infrastructure.

Aikido will surface critical cloud misconfigurations that allow hackers to get into your Alibaba Cloud environment. We focus on the risks that can have a truly big impact on your company's business and cut the noise.

To view the list of security checks performed by Aikido on your cloud environment, go to the 'checks' tab on the [cloud overview page](https://app.aikido.dev/clouds). Filter to Alibaba Cloud to see specific checks performed on your connected Alibaba Cloud account.

#### Features

After connecting, Aikido will perform the following monitoring:

* Perform a daily compliance scan on all checks listed here: <https://app.aikido.dev/clouds/checks>
* [**Container image scanning**](#container-image-scanning) for Alibaba Cloud registry or any other OCI-compatible registry
* [**Virtual machine scanning**](#virtual-machine-scanning) via the Local VM Scanner on Alibaba Cloud instances

#### Getting started

To get started, head to the [cloud overview page](https://app.aikido.dev/clouds) on Aikido and click 'Connect cloud.' Follow the step-by-step setup wizard to connect your Alibaba Cloud account to Aikido.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FnaVg9eHI78uNqEs2CZVF%2Fimage.png?alt=media&#x26;token=950b1b53-f3d9-4800-8bbb-d027b02918dc" alt=""><figcaption></figcaption></figure>

Aikido will require the creation of a new RAM role in your Alibaba Cloud account. The permissions for this role enable us to do a security audit of your cloud, but not edit your cloud infrastructure. This works by giving the Aikido Alibaba Cloud account a trust relationship with the newly created role in your account.

To view the exact ROS template used to create this role, [click here](https://aikido-cspm-templates.s3.eu-west-1.amazonaws.com/alibaba-ros-template-production.json). Inside the wizard, Aikido can also generate an equivalent Terraform template for you.

After creation of the role, Aikido only needs the specific ARN to get started. No AccessKey pairs or passwords are ever shared with Aikido.

Finally, you can name your connected project in Aikido and specify the environment it operates in. This information helps Aikido prioritize findings based on the severity and impact to your business.

<div data-full-width="false"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FM78ajm8wIknuIpLAQwtW%2Fimage.png?alt=media&#x26;token=c2e14925-5a64-4a3f-8ac8-d42198731c47" alt="" width="375"><figcaption></figcaption></figure></div>

Within a few minutes after connecting your account, Aikido will report misconfigurations that could pose a threat.

#### Container image scanning

Alibaba Cloud’s container registry and most third-party registries you use from Alibaba Cloud are OCI-compatible, so they can be scanned using Aikido.

Create a read-only or pull-only user in Alibaba Cloud registry: <https://www.alibabacloud.com/help/en/acr/user-guide/configure-access-credentials>

Follow the OCI guide below to configure container image scanning

{% content-ref url="../../../container-image-scanning/standalone-registries/generic-oci-compatible-registry" %}
[generic-oci-compatible-registry](https://help.aikido.dev/container-image-scanning/standalone-registries/generic-oci-compatible-registry)
{% endcontent-ref %}

#### Virtual Machine scanning

To scan Virtual Machines on Alibaba Cloud, use the Local VM Scanner. It inspects packages, system dependencies and configuration directly on the instance.

{% content-ref url="../../../virtual-machine-scanning/local-vm-scanning" %}
[local-vm-scanning](https://help.aikido.dev/virtual-machine-scanning/local-vm-scanning)
{% endcontent-ref %}

ECS machines can get the local scanner by [configuring the user data](https://www.alibabacloud.com/help/en/ecs/user-guide/customize-the-initialization-configuration-for-an-instance) to download and install the necessary binary.\
You can also roll this out centrally using your usual automation tooling (e.g. Ansible, Terraform-provisioned scripts, or cloud-init) so that new Alibaba Cloud instances are automatically enrolled.
