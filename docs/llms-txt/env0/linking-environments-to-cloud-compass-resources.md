# Source: https://docs.envzero.com/guides/cloud-compass/cloud-compass/linking-environments-to-cloud-compass-resources.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Linking Environments to Cloud Compass Resources

> Map env zero environments to discovered cloud resources in Cloud Compass for full visibility

To fully leverage the functionality of Cloud Compass and gain visibility into your existing cloud resources,\
env zero performs an identification and cataloging process for your resources at the end of each run. This lets you immediately view, directly from the Cloud Compass table, which environments these resources belong to.

<img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/87f70c07f0dbc1489d3ba17d366ada52a6d938d0142012b694e189a666ec429d-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=da20a5c6da841095f3b488967ddb2419" alt="" width="1126" height="90" data-path="images/guides/cloud-compass/cloud-compass/87f70c07f0dbc1489d3ba17d366ada52a6d938d0142012b694e189a666ec429d-image.png" />

You can see it under the 'Environment' column.

<Tip>
  Supported Providers

  AWS - [https://search.opentofu.org/provider/hashicorp/aws/latest](https://search.opentofu.org/provider/hashicorp/aws/latest)

  Azure - [https://search.opentofu.org/provider/hashicorp/azurerm/latest](https://search.opentofu.org/provider/hashicorp/azurerm/latest)

  GCP - [https://registry.terraform.io/providers/hashicorp/google/latest](https://registry.terraform.io/providers/hashicorp/google/latest)
</Tip>

## Resource Matching

Identifying and matching resources is no simple task, and we’ve developed a specialized engine to perform these matches and ensure unique identification. However, we may not be able to match all resources. If you encounter any gaps, feel free to contact our support team.

### Tips for Improving Resource Identification

#### AWS

For each provider block add those data resources blocks

```yaml  theme={null}
provider "aws" {
  region  = "us-east-1"
}

provider "aws" {
  alias = "eu-west-1"
  region  = "eu-west-1"
}

data "aws_region" "current" {}
data "aws_caller_identity" "current" {}

data "aws_region" "west" {
 provider = aws.eu-west-1
}
data "aws_caller_identity" "west" {
 provider = aws.eu-west-1
}
```

Built with [Mintlify](https://mintlify.com).
