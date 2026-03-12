# Source: https://docs.portainer.io/2.33-lts/admin/registries/add/ecr.md

# Source: https://docs.portainer.io/sts/admin/registries/add/ecr.md

# Source: https://docs.portainer.io/admin/registries/add/ecr.md

# Add an AWS ECR registry

From the menu select **Registries** then click **Add registry** and select **AWS ECR** as the registry provider.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/MkzfEPkUimvvQFWR6Btl/Add-registry-ECR.gif" alt=""><figcaption></figcaption></figure>

## Preparation

If your registry requires authentication to access, you must create an IAM user with access to the registry for Portainer to use. Instructions on creating an IAM user are available [from AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console). When you have created the user, make note of the **Access key ID** and **Secret access key**, as you will need these below.

{% hint style="info" %}
At present we do not support IAM users with MFA enabled. We recommend creating a user specifically for Portainer to use with MFA disabled.
{% endhint %}

When creating the user you will need to attach one or more policies to provide registry access. For full registry management functionality within Portainer, we recommend the `AmazonEC2ContainerRegistryFullAccess` policy.

## Add your registry

Complete the form, using the table below as a guide.

| Field/Option          | Overview                                                                                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                  | Enter the name you'd like to use in Portainer for your registry.                                                                                                    |
| Registry URL          | Enter the URL of your AWS ECR registry, including the account ID and region. You can find this in the AWS console under Amazon Container Services, ECR, Registries. |
| Authentication        | Enable this option if your registry requires authentication to access.                                                                                              |
| AWS Access Key        | Enter the Access key ID for the IAM user that will access the AWS ECR registry.                                                                                     |
| AWS Secret Access Key | Enter the Secret access key for the above IAM user.                                                                                                                 |
| Region                | Enter the region your registry is in, for example `us-west-1`.                                                                                                      |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/ybwDdbQC82qS2m25srOf/2.19-registries-add-ecr.png" alt=""><figcaption></figcaption></figure>

When the form is complete, click **Add registry**.
