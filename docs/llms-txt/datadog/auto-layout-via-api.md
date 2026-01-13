# Source: https://docs.datadoghq.com/cloudcraft/advanced/auto-layout-via-api.md

---
title: Automate Snapshots of Cloud Accounts via the Cloudcraft API
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Cloudcraft (Standalone) > Advanced > Automate Snapshots of Cloud
  Accounts via the Cloudcraft API
source_url: https://docs.datadoghq.com/advanced/auto-layout-via-api/index.html
---

# Automate Snapshots of Cloud Accounts via the Cloudcraft API

## Overview{% #overview %}

Cloudcraft's **Auto Layout** feature, accessible through the web application, is a powerful tool for automatically generating diagrams of your AWS environment. This functionality can significantly streamline documentation processes and facilitate the onboarding of new team members.

This guide provides a step-by-step approach to utilizing this feature via common command-line utilities and the Cloudcraft developer API.

{% alert level="info" %}
The ability to add and scan AWS and Azure accounts, as well as to use Cloudcraft's developer API, is only available to Pro subscribers. Check out [Cloudcraft's pricing page](https://www.cloudcraft.co/pricing) for more information.
{% /alert %}

## Prerequisites{% #prerequisites %}

- An active [Cloudcraft Pro subscription](https://www.cloudcraft.co/pricing).
- An API key with read-write permissions.
- The account ID of the AWS or Azure account you wish to scan.
- Access to a Unix-like environment (Linux, macOS, or Windows Subsystem for Linux).
- Familiarity with command-line operations.
- Basic knowledge of API usage.

## Take a snapshot of the account{% #take-a-snapshot-of-the-account %}

Start by creating a snapshot of your AWS or Azure account using the [Snapshot AWS account](https://docs.datadoghq.com/cloudcraft/api/aws-accounts/#snapshot-aws-account) or [Snapshot Azure account](https://docs.datadoghq.com/cloudcraft/api/azure-accounts/#snapshot-an-azure-account) endpoints. This process mirrors the functionality of the **Scan Now** button in the Cloudcraft UI and outputs the snapshot in JSON format.

Execute the following command in your terminal:

```shell
curl \
  --url 'https://api.cloudcraft.co/PROVIDER/account/ACCOUNT_ID/REGION/json' \
  --tlsv1.2 \
  --proto '=https' \
  --silent \
  --header "Authorization: Bearer API_KEY"
```

Replace `PROVIDER` with the cloud provider, for example, `azure` or `aws`, `ACCOUNT_ID` with the ID of your AWS or Azure account in Cloudcraft, `REGION` with your desired scan region, and `API_KEY` with your Cloudcraft API key.

After executing the command, the JSON representation of your AWS account snapshot is displayed. To save this output directly to a file, use the following command:

```shell
curl \
  --url 'https://api.cloudcraft.co/PROVIDER/account/ACCOUNT_ID/REGION/json' \
  --tlsv1.2 \
  --proto '=https' \
  --silent \
  --header "Authorization: Bearer API_KEY" > '/tmp/account-infra.json'
```

The snapshot is saved with the filename `account-infra.json` in your temporary directory.

## Generate a new blueprint{% #generate-a-new-blueprint %}

Next, create a new blueprint in your Cloudcraft account using the [Create blueprint](https://docs.datadoghq.com/cloudcraft/api/blueprints/#create-a-blueprint) API endpoint. The saved snapshot data serves as the payload for this request.

Execute the following command in your terminal:

```shell
curl \
  --request 'POST' \
  --url 'https://api.cloudcraft.co/blueprint' \
  --tlsv1.2 \
  --proto '=https' \
  --silent \
  --header 'Content-Type: application/json' \
  --header "Authorization: Bearer API_KEY" \
  --data '@/tmp/account-infra.json'
```

Remember to replace `API_KEY` with your actual Cloudcraft API key.

Upon completion, a new blueprint reflecting your cloud infrastructure is created in your Cloudcraft account, replicating the effect of manually using the **Scan Now** and **Auto Layout** buttons.

If you have any questions or trouble with the process, [contact Cloudcraft's support team](https://app.cloudcraft.co/app/support).
