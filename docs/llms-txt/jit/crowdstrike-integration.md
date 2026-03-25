# Source: https://docs.jit.io/docs/crowdstrike-integration.md

# CrowdStrike Integration

## Overview

The CrowdStrike integration enables Jit to automatically retrieve data from your CrowdStrike Falcon platform.\
Once connected, Jit ingests posture findings, misconfigurations, alerts, and asset data through the Falcon API, enriching your security context and powering automated agent workflows.

By default, CrowdStrike data is used to enrich Jit's context graph without adding standalone findings to your Findings page. If you'd like CrowdStrike findings to appear directly in your Jit findings page, contact Jit Support to enable that.

***

## How It Works

### Default: Context Enrichment

CrowdStrike data enriches Jit's context graph, powering risk prioritization and correlation across all your connected tools. No standalone CrowdStrike findings appear in the Findings page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b072b00f920cd3f32d488d959dac70b63afe6dd938356418b9728101187df787-Screenshot_2026-03-08_at_19.36.24.png",
        "",
        ""
      ],
      "align": "center",
      "caption": "CrowdStrike context enrichment in Jit context graph"
    }
  ]
}
[/block]

### Optional: Findings Import

When enabled, CrowdStrike findings appear directly in Jit's Findings page alongside findings from other connected tools, where they can be triaged, assigned, and remediated through Jit's standard workflows.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/deaf4291688996d544264802f471b2a4b7b2d6f85ba6ec5243052cd4b7155e2a-Screenshot_2026-03-08_at_19.50.19.png",
        "",
        ""
      ],
      "align": "center",
      "caption": "CrowdStrike findings in Jit findings page"
    }
  ]
}
[/block]

To enable Findings Import, contact **Jit Support**.

> **Note:** Enabling Findings Import replaces Context Enrichment - the two modes are mutually exclusive.\
> Keep in mind that importing CrowdStrike findings directly may significantly increase the number of findings in your Findings page.

***

## Setup Requirements

Before connecting the integration, ensure:

* You have a **CrowdStrike Falcon** account
* You can create or edit **API Clients and Keys**
* You are logged in to the correct **Falcon region**
* You have a **Jit** account with admin permissions

This integration uses **Client ID**, **Client Secret**, and **API Region** for authentication.

***

## Required API Permissions

To allow Jit to retrieve data from CrowdStrike, your API Client must include the following permissions, all set to **Read**:

| Permission                        | Required Access |
| --------------------------------- | --------------- |
| **Alerts**                        | Read            |
| **CSPM Registration**             | Read            |
| **Cloud Security API Detections** | Read            |
| **ASPM Read-Only**                | Read            |

> **Important:** Missing any required permission will prevent Jit from retrieving the relevant data and may cause partial or failed syncs.

***

## How to Retrieve Credentials in CrowdStrike

Follow these steps in the Falcon Console:

1. Log in to your Falcon Console at\
   `https://falcon.<region>.crowdstrike.com`

2. Navigate to **☰ Menu → Support & Resources → API Clients and Keys**

3. Click **Create API Client** (or open an existing client)

4. Give it a descriptive name, e.g. **"Jit Integration"**

5. Under **Permissions**, enable the following (all with **Read** access):
   * **Alerts**
   * **ASPM Read-Only**
   * **CSPM Registration**
   * **Cloud Security API Detections**

6. Save the client to generate:
   * **Client ID**
   * **Client Secret** (shown only once — copy immediately)

7. Determine your **API Region** from your console URL:

   | Console URL                         | Region Value     |
   | ----------------------------------- | ---------------- |
   | `falcon.crowdstrike.com`            | `api`            |
   | `falcon.us-2.crowdstrike.com`       | `api.us-2`       |
   | `falcon.eu-1.crowdstrike.com`       | `api.eu-1`       |
   | `falcon.laggar.gcw.crowdstrike.com` | `api.laggar.gcw` |

***

## Connecting CrowdStrike to Jit

1. Go to the **Integrations** page in Jit
2. Select **CrowdStrike**
3. Fill in:
   * **Client ID**
   * **Client Secret**
   * **API Region**
4. Click **Continue**
5. Jit will validate the credentials and activate the integration

Once connected, Jit will begin syncing data automatically.

***

## Need Help?

If you need assistance configuring the integration or enabling Findings Import, contact **Jit Support**.