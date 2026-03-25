# Source: https://docs.jit.io/docs/plan-resources-exclusion.md

# Plan Resources Exclusion

## Overview

The Plan resources exclusion feature enables you to exclude specific resources from actions or changes initiated by plan items.

> ⚠️ Note
>
> Security Plan configuration is managed directly in the Jit platform.\
> As-code configuration is no longer the source of truth and is considered redundant.\
> If you previously used as-code configuration, it has been automatically synced to Jit.\
> Please contact us if anything is unclear or behaves differently than expected.

## Excluding resources

**Finding the plan resource data**

you will need the following plan item data:

* **<plan item slug>**: In the **jit/jit-plan** file (located in the repository selected for the integration), copy the slug (located in the **uses** section of **jit/jit-plan** of the plan item that contains the resources you want to exclude and add it to your **jit-config.yml** file.\
  Example: **item-cloud-security-posture-management**(AWS Security Hub plan item slug).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2c9e762-Clipboard_2023-06-07_at_5.03.29_PM.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

* **<resource identifier>**: Replace this with the name of the resource you wish to exclude. Copy the **resource identifier** to from [Settings -> Manage Resources](https://docs.jit.io/docs/manage-resources) in the Jit platform.

| Resource type           | Location of resource identifier in UI         |
| :---------------------- | :-------------------------------------------- |
| AWS Account, GCP, Azure | Under the Account column of your resource.    |
| Github repository       | Under the Repository column of your resource. |
| Github organization     | The organization's name.                      |

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/53deeb3-Clipboard_2023-06-07_at_5.03.44_PM.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

* (Optional) **Type**: This field is used to distinguish between two resources that are of different types but share the same identifier, like a GitHub repository named **Jit** under an organization named **Jit**. Enter one of the following values into the **Type** field:

| Value              | Description                    |
| :----------------- | :----------------------------- |
| **repo**           | A code repository.             |
| **org**            | Organization.                  |
| **aws\_account**   | AWS account.                   |
| **gcp\_account**   | Google Cloud Platform account. |
| **azure\_account** | Microsoft Azure account.       |
| **web**            | Web application resource.      |
| **api**            | API resource.                  |

**Excluding resources in GitHub**

> 🚧
>
> The contents of your jit-config.yml file will vary depending on your enabled features and integrations. Other features that may impact your jit-config.yml file are discussed in [Security as Code Configuration](https://docs.jit.io/docs/security-as-code-configuration).

1. Open the **jit-config.yml f**ile located in the .**jit** directory of the repository selected for [GitHub integration](https://docs.jit.io/docs/integrating-with-github).

2. Add the following section to the end of the file:

```yaml jit-config.yml
resource_management:
  exclude:
    plan_items:
      <plan item slug>:
        resources:
          - name: <resource identifier>
            type: <type [OPTIONAL]>
```

3. Save your changes to the **jit-config.yml** file.

**Excluding resources in other SCMs**

Use Jit's 'Update configuration file' API endpoint. For more information, please see [API: Update configuration file.](https://docs.jit.io/reference/tenant-7ddaef1e-4ba5-4c0d-964b-d62a699c9e2f)