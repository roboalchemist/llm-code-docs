# Source: https://docs.port.io/guides/all/ingest-slack-data-via-airbyte-s3-and-webhook.md

# Ingest Slack channels data into Port via Airbyte, S3 and webhook

This guide will demonstrate how to ingest Slack channels and channel membership data into Port using [Airbyte](https://airbyte.com/), [S3](https://aws.amazon.com/s3/) and a [webhook integration](https://docs.port.io/build-your-software-catalog/custom-integration/webhook/).

Disclaimer

S3 integrations lack some of the features (such as reconciliation) found in Ocean or other Port integration solutions.

As a result, if a record ingested during the initial sync is later deleted in the data source, thereâs no automatic mechanism to remove it from Port. The record simply wonât appear in future syncs, but it will remain in Port indefinitely.

If the data includes a flag for deleted records (e.g., is\_deleted: "true"), you can configure a webhook delete operation in your [webhookâs mapping configuration](/build-your-software-catalog/custom-integration/webhook/.md#configuration-structure) to remove these records from Port automatically.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Ensure you have a Port account and have completed the [onboarding process](https://docs.port.io/quickstart).

* This feature is part of Port's limited-access offering. To obtain the required S3 bucket, please contact our team directly via chat, [Slack](https://www.getport.io/community), or the [support site](http://support.port.io/), and we will create and manage the bucket on your behalf.

* Access to an available Airbyte app (can be cloud or self-hosted) - for reference, follow the [quick start guide](https://docs.airbyte.com/using-airbyte/getting-started/oss-quickstart).

**Very short Quickstart Guide for macOS**

1. Download and Install [Docker Desktop](https://docs.docker.com/desktop/setup/install/mac-install/)

2. Install abctl:

```
curl -LsfS https://get.airbyte.com | bash -
```

3. Install Airbyte locally:

```
abctl local install
```

The application will be available by default in <http://localhost:8000/>

You can find your password by typing in a terminal (see screenshot):

```
abctl local credentials
```

![](/img/build-your-software-catalog/custom-integration/s3integrations/airbyteLocalSetupExample.png)

* Setup a Slack Airbyte exporter app - follow [Airbyte's guide for slack connector](https://docs.airbyte.com/integrations/sources/slack).

  Include email data

  If you wish to include email data, in addition to the permissions listed in the guide above, you will need to include `user.email:read` in the app's permissions.

## Data model setup[â](#data-model-setup "Direct link to Data model setup")

### Add Blueprints[â](#add-blueprints "Direct link to Add Blueprints")

Add the `Slack Channel Membership` blueprint:

1. Go to the [Builder page](https://app.getport.io/settings/data-model) of your portal.

2. Click on "+ Blueprint".

3. Click on the `{...}` button in the top right corner, and choose "Edit JSON".

4. Paste the following JSON schema into the editor:

**Slack Channel Membership (Click to expand)**

Create in Port

```
{
  "identifier": "slack_channel_membership",
  "description": "Slack Channel Membership",
  "title": "Slack Channel Membership",
  "icon": "Slack",
  "schema": {
    "properties": {
      "member_id": {
        "type": "string",
        "description": "ID of the user who is a member of the channel."
      },
      "channel_id": {
        "type": "string",
        "description": "ID of the channel the user belongs to."
      }
    },
    "required": [
      "member_id",
      "channel_id"
    ]
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {}
}
```

<br />

Add the `Slack Channel` blueprint in the same way:

**Slack Channel (Click to expand)**

Create in Port

```
{
  "identifier": "slack_channel",
  "description": "Slack Channel",
  "title": "Slack Channel",
  "icon": "Slack",
  "schema": {
    "properties": {
      "is_private": {
        "type": "boolean",
        "description": "Indicates if the channel is private."
      },
      "context_team_id": {
        "type": "string",
        "description": "ID of the team the channel belongs to."
      },
      "is_channel": {
        "type": "boolean",
        "description": "Indicates if this is a channel (true) or a direct message (false)."
      },
      "is_shared": {
        "type": "boolean",
        "description": "Indicates if the channel is shared across teams."
      },
      "previous_names": {
        "type": "array",
        "description": "List of previous names of the channel."
      },
      "creator": {
        "type": "string",
        "description": "ID of the user who created the channel."
      },
      "createdAt": {
        "type": "number",
        "description": "Timestamp of when the channel was created."
      },
      "is_ext_shared": {
        "type": "boolean",
        "description": "Indicates if the channel is externally shared."
      },
      "is_group": {
        "type": "boolean",
        "description": "Indicates if this is a group DM."
      },
      "is_archived": {
        "type": "boolean",
        "description": "Indicates if the channel is archived."
      },
      "shared_team_ids": {
        "type": "array",
        "description": "List of teams the channel is shared with."
      },
      "is_org_shared": {
        "type": "boolean",
        "description": "Indicates if the channel is shared across the entire organization."
      },
      "num_members": {
        "type": "number",
        "title": "num_members"
      },
      "purpose": {
        "type": "string",
        "description": "Information about the channel's purpose."
      },
      "topic": {
        "type": "string",
        "description": "Information about the channel's topic."
      }
    },
    "required": []
  },
  "mirrorProperties": {
    "member_id": {
      "title": "member_id",
      "path": "users.member_id"
    }
  },
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "users": {
      "title": "Users",
      "target": "slack_channel_membership",
      "required": false,
      "many": true
    }
  }
}
```

<br />

Add the `Slack User` blueprint in the same way:

**Slack User (Click to expand)**

Create in Port

```
{
  "identifier": "slack_user",
  "description": "Slack User",
  "title": "Slack User",
  "icon": "Slack",
  "schema": {
    "properties": {
      "tz": {
        "type": "string",
        "description": "The user's time zone."
      },
      "is_restricted": {
        "type": "boolean",
        "description": "Indicates if the user is restricted."
      },
      "is_primary_owner": {
        "type": "boolean",
        "description": "Indicates if the user is the primary owner."
      },
      "real_name": {
        "type": "string",
        "description": "The user's real name."
      },
      "team_id": {
        "type": "string",
        "description": "The user's team ID."
      },
      "is_admin": {
        "type": "boolean",
        "description": "Indicates if the user is an admin."
      },
      "is_app_user": {
        "type": "boolean",
        "description": "Indicates if the user is an app user."
      },
      "deleted": {
        "type": "boolean",
        "description": "Indicates if the user is deleted."
      },
      "is_bot": {
        "type": "boolean",
        "description": "Indicates if the user is a bot."
      },
      "email": {
        "type": "string",
        "title": "email"
      }
    },
    "required": []
  },
  "mirrorProperties": {
    "channel_id": {
      "title": "channel_id",
      "path": "membership.channel_id"
    }
  },
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "user": {
      "title": "User",
      "target": "_user",
      "required": false,
      "many": false
    },
    "membership": {
      "title": "membership",
      "target": "slack_channel_membership",
      "required": false,
      "many": true
    }
  }
}
```

### Create Webhook Integration[â](#create-webhook-integration "Direct link to Create Webhook Integration")

Create a webhook integration to ingest the data into Port:

1. Go to the [Data sources page](https://app.getport.io/settings/data-sources) of your portal.

2. Click on "+ Data source".

3. In the top selection bar, click on Webhook, then select `Custom Integration`.

4. Enter a **name** for your Integration (for example: "Hibob Integration"), enter a **description** (optional), then click on `Next`.

5. Copy the Webhook URL that was generated and include set up the airbyte connection (see Below).

6. Scroll down to the section titled "Map the data from the external system into Port" and paste the following mapping:

![](/img/build-your-software-catalog/custom-integration/s3integrations/customIntegrationMappingExample.png)

**Slack Webhook Mapping (Click to expand)**

```
[
  {
    "blueprint": "slack_channel",
    "operation": "create",
    "filter": "(.body | has(\"_PORT_SOURCE_OBJECT_KEY\")) and (.body._PORT_SOURCE_OBJECT_KEY | split(\"/\") | .[2] | IN(\"channels\"))",
    "entity": {
      "identifier": ".body.id | tostring",
      "title": ".body.name_normalized | tostring",
      "properties": {
        "is_private": ".body.is_private",
        "purpose": ".body.purpose.value",
        "context_team_id": ".body.context_team_id",
        "is_shared": ".body.is_shared",
        "previous_names": ".body.previous_names",
        "creator": ".body.creator",
        "createdAt": ".body.created",
        "is_ext_shared": ".body.is_ext_shared",
        "is_group": ".body.is_group",
        "is_archived": ".body.is_archived",
        "num_members": ".body.num_members | tonumber? // .",
        "topic": ".body.topic.value",
        "shared_team_ids": ".body.shared_team_ids",
        "is_org_shared": ".body.is_org_shared"
      },
      "relations": {
        "users": {
          "combinator": "'and'",
          "rules": [
            {
              "property": "'channel_id'",
              "operator": "'='",
              "value": ".body.id | tostring"
            }
          ]
        }
      }
    }
  },
  {
    "blueprint": "slack_user",
    "operation": "create",
    "filter": "(.body | has(\"_PORT_SOURCE_OBJECT_KEY\")) and (.body._PORT_SOURCE_OBJECT_KEY | split(\"/\") | .[2] | IN(\"users\"))",
    "entity": {
      "identifier": ".body.id | tostring",
      "title": ".body.name | tostring",
      "properties": {
        "tz": ".body.tz",
        "is_restricted": ".body.is_restricted",
        "is_primary_owner": ".body.is_primary_owner",
        "real_name": ".body.real_name",
        "team_id": ".body.team_id",
        "is_admin": ".body.is_admin",
        "is_app_user": ".body.is_app_user",
        "deleted": ".body.deleted",
        "is_bot": ".body.is_bot",
        "email": ".body.profile.email"
      },
      "relations": {
        "user": ".body.profile.email"
      }
    }
  },
  {
    "blueprint": "slack_channel_membership",
    "operation": "create",
    "filter": "(.body | has(\"_PORT_SOURCE_OBJECT_KEY\")) and (.body._PORT_SOURCE_OBJECT_KEY | split(\"/\") | .[2] | IN(\"channel_members\"))",
    "entity": {
      "identifier": ".body.channel_id + \"_\" + .body.member_id | tostring",
      "title": ".body.channel_id + \"_\" + .body.member_id | tostring",
      "properties": {
        "member_id": ".body.member_id",
        "channel_id": ".body.channel_id"
      }
    }
  }
]
```

## Airbyte Setup[â](#airbyte-setup "Direct link to Airbyte Setup")

### Set up S3 Destination[â](#set-up-s3-destination "Direct link to Set up S3 Destination")

If you haven't already set up S3 Destination for Port S3, follow these steps:

* UI
* Terraform

1. Login to your Airbyte application (cloud or self-hosted).

2. In the left-side pane, click on `Destinations`.

3. Click on `+ New Destination`.

4. Input the S3 Credentials provided to you by Port:

   * Under **S3 Key ID** enter your S3 Access Key ID.
   * Under **S3 Access Key** enter your S3 Access Key Secret.
   * Under **S3 Bucket Name** enter the bucket name (example: "org-xxx").
   * Under **S3 Bucket Path** enter "data/".
   * Under **S3 Bucket Region** enter the appropriate region.
   * For **output format**, choose "JSON Lines: Newline-delimited JSON".
   * For **compression**, choose "GZIP".
   * Under **Optional Fields**, enter the following in **S3 Path Format**: `${NAMESPACE}/${STREAM_NAME}/year=${YEAR}/month=${MONTH}/${DAY}_${EPOCH}_`

5. Click `Test and save` and wait for Airbyte to confirm the Destination is set up correctly.

![](/img/build-your-software-catalog/custom-integration/s3integrations/airbyteDestinationSetupExample.png)

```
terraform {
  required_providers {
    airbyte = {
      source = "airbytehq/airbyte"
      version = "0.6.5"
    }
  }
}

provider "airbyte" {
  username = "<AIRBYTE_USERNAME>"
  password = "<AIRBYTE_PASSWORD>"
  server_url = "<AIRBYTE_API_URL>"
}

resource "airbyte_destination_s3" "port-s3-destination" {
  configuration = {
    access_key_id     = "<S3_ACCESS_KEY>"
    secret_access_key = "<S3_SECRET_KEY>"
    s3_bucket_region  = "<S3_REGION>"
    s3_bucket_name    = "<S3_BUCKET>"
    s3_bucket_path    = "data/"
    format = {
      json_lines_newline_delimited_json = {
        compression = { gzip = {} }
        format_type = "JSONL"
      }
    }
    s3_path_format    = `$${NAMESPACE}/$${STREAM_NAME}/year=$${YEAR}/month=$${MONTH}/$${DAY}_$${EPOCH}_`
    destination_type = "s3"
  }
  name          = "port-s3-destination"
  workspace_id  = var.workspace_id
}

variable "workspace_id" {
  default     = "<AIRBYTE_WORKSPACE_ID>"
}
```

### Set up Slack Connection[â](#set-up-slack-connection "Direct link to Set up Slack Connection")

1. Follow Airbyte's guide to set up a [Slack connector](https://docs.airbyte.com/integrations/sources/slack).

   Private Channels

   Airbyte will not read information from private channels by default. If you wish to include private channels: tick the "include private channels" option, and manually add the Slack-export App to your desired private channels.

More information on [setting source connectors](http://docs.port.io/build-your-software-catalog/custom-integration/S3-integrations#set-up-data-source)

2. After the Source is set up, proceed to create a "+ New Connection".

3. For **Source**, choose the Slack source you have set up.

4. For **Destination**, choose the S3 Destination you have set up.

5. In the **Select Streams** step, make sure only "channel\_members", "channels" and "users" are marked for synchronization.

6. In the **Configuration** step, under "Destination Namespace", choose "Custom Format" and **enter the Webhook URL you have copied when setting up the webhook"**, for example: "wSLvwtI1LFwQzXXX".

7. **Click on Finish & Sync** to apply and start the Integration process!

Important

If for any reason you have entered different values than the ones specified in this guide, inform us so we can assist to ensure the integration will run smoothly.

## Additional relevant guides[â](#additional-relevant-guides "Direct link to Additional relevant guides")

* [Ingest Any data into port via Airbyte](https://docs.port.io/build-your-software-catalog/custom-integration/S3-integrations)
