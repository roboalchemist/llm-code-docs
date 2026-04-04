# Source: https://docs.vespa.ai/en/operations/zones.html.md

# Zones

 

An application is deployed to a _zone_, which is a combination of an [environment](environments.html) and a _region_, like `vespa deploy -z dev.aws-us-east-1c`.

If an application requires zone-specific configuration (e.g., different capacity requirements per zone), use [environment and region variants](deployment-variants.html#services.xml-variants). Also see [deployment.xml](../reference/applications/deployment.html).

`dev` zones for development and performance testing:

| Environment | Default | Region | AWS Zone ID |
| --- | --- | --- | --- |
| [dev](environments.html#dev) | Yes | aws-us-east-1c | use1-az6 |
| [dev](environments.html#dev) | No | aws-euw1-az1 | euw1-az1 |
| [dev](environments.html#dev) | No | azure-eastus-az1 | |
| [dev](environments.html#dev) | No | gcp-us-central1-f | |

`prod` zones for production serving, with a [CD pipeline](automated-deployments.html):

| Environment | Region | AWS Zone ID |
| --- | --- | --- |
| [prod](environments.html#prod) | aws-us-east-1c | use1-az6 |
| [prod](environments.html#prod) | aws-use1-az4 | use1-az4 |
| [prod](environments.html#prod) | aws-use2-az1 | use2-az1 |
| [prod](environments.html#prod) | aws-use2-az3 | use2-az3 |
| [prod](environments.html#prod) | aws-us-west-2a | usw2-az1 |
| [prod](environments.html#prod) | aws-usw2-az3 | usw2-az3 |
| [prod](environments.html#prod) | aws-eu-west-1a | euw1-az2 |
| [prod](environments.html#prod) | aws-euw1-az1 | euw1-az1 |
| [prod](environments.html#prod) | aws-euc1-az1 | euc1-az1 |
| [prod](environments.html#prod) | aws-euc1-az3 | euc1-az3 |
| [prod](environments.html#prod) | aws-cac1-az1 | cac1-az1 |
| [prod](environments.html#prod) | aws-cac1-az2 | cac1-az2 |
| [prod](environments.html#prod) | aws-ap-northeast-1a | apne1-az4 |
| [prod](environments.html#prod) | aws-apne1-az1 | apne1-az1 |
| [prod](environments.html#prod) | gcp-europe-west3-b | |
| [prod](environments.html#prod) | gcp-us-central1-a | |
| [prod](environments.html#prod) | gcp-us-central1-b | |
| [prod](environments.html#prod) | gcp-us-central1-c | |
| [prod](environments.html#prod) | gcp-us-central1-f | |

The `prod` zones use ephemeral instances for system tests and staging tests, running in [test](environments.html#test) and [staging](environments.html#staging) environments. These are internal zones, and never directly deployed to, included here for reference:

| Environment | Region | AWS Zone ID |
| --- | --- | --- |
| [test](environments.html#test) | aws-us-east-1c | use1-az6 |
| [test](environments.html#test) | gcp-us-central1-f | |
| [staging](environments.html#staging) | aws-us-east-1c | use1-az6 |
| [staging](environments.html#staging) | gcp-us-central1-f | |

Contact [Support](https://vespa.ai/support/) to request more zones.

 Copyright © 2026 - [Cookie Preferences](#)

