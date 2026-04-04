# Source: https://docs.datafold.com/integrations/bi-data-apps/tableau.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tableau

> Visualize downstream Tableau dependencies and understand how warehouse changes impact your BI layer.

## Overview

Our Tableau integration can help you visualise column-level lineage dependencies between warehouse tables and Tableau entities using [Data Explorer](/data-explorer/how-it-works).

<Info>
  **Note:** Lineage is only supported for Tableau assets in **Live** mode. Assets in **Extract** mode will not appear in Datafold lineage or dependency views.
</Info>

Lineage from upstream data warehouses into Tableau is supported for the following data warehouse types:

* Snowflake
* Redshift
* Databricks
* BigQuery

Potentially impacted Tableau entity names are also automatically identified in the Datafold CI printout.

The following Tableau entities types will appear in Data Explorer, data diff results, and the Datafold CI printout:

* Tableau **Data Connections** and related fields;
* **Workbooks** and related fields;
* **Dashboards**.

<Info>
  To declutter <Icon icon="sparkles" /> the Datafold lineage, Datafold filters out Tableau Data Connections and Data Connections fields that have no downstream dependencies.
</Info>

If you're interested in learning more about the Datafold integration, [please reach out to our team](https://www.datafold.com/booktime).

## Set up your Tableau instance

To connect Datafold to Tableau, you will require the following credentials from your Tableau site:

* Server URL,
* Site Name,
* Token Name,
* Token Value.

## If you are using Tableau Server

**Tableau Server** is an installation of Tableau that you are managing on your company's own infrastructure and domain. This is an alternative to using a Tableau Cloud subscription.

* Make sure that the [metadata-services](https://help.tableau.com/current/server/en-us/cli%5Fmaintenance%5Ftsm.htm#cat%5Fenable) are enabled by running the following command:

```
tsm maintenance metadata-services enable

```

* Ensure that your Tableau Server instance is accessible to Datafold. Please get in touch with our team to set this up.

## Obtaining server URL & Site Name

These can be found from URL of your Tableau home page. For instance, if your home page is:

```
https://eu-west-1a.online.tableau.com/#/site/mysupersite/home

```

Then:

* **Server URL** is `https://eu-west-1a.online.tableau.com` (the hostname with `https` in front)
* **Site Name** is `mysupersite` (the part directly after `#/site/` and until the next `/`)

## Obtaining Token Name & Token Value[](#obtaining-token-name--token-value "Direct link to Obtaining Token Name & Token Value")

Ensure that **Personal Access Tokens** are enabled on your Tableau site. For that, navigate to **Settings** and there, on the **General** tab, search for `Personal Access Tokens`. That feature needs to be enabled — not necessarily for everyone but for the user for whom we will be creating the token Datafold will use.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/tableau_enable_personal_access_tokens-a099600ff7a46573c1a2a34cd805323f.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9147e3ad4b9630086b4b2a15094fe672" alt="Enable Personal Access Tokens" data-og-width="4152" width="4152" data-og-height="2260" height="2260" data-path="images/tableau_enable_personal_access_tokens-a099600ff7a46573c1a2a34cd805323f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/tableau_enable_personal_access_tokens-a099600ff7a46573c1a2a34cd805323f.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=61703e834866aa0f644f6327f10030db 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/tableau_enable_personal_access_tokens-a099600ff7a46573c1a2a34cd805323f.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b94c052f038e27e9ea686f69ed2b9e64 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/tableau_enable_personal_access_tokens-a099600ff7a46573c1a2a34cd805323f.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=845a7fc83e6b2fac8fc0d09e976cafcf 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/tableau_enable_personal_access_tokens-a099600ff7a46573c1a2a34cd805323f.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=839cadd96b3255caf253f3905b5535e6 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/tableau_enable_personal_access_tokens-a099600ff7a46573c1a2a34cd805323f.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=11657c4aebc7313be52033c558956a57 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/tableau_enable_personal_access_tokens-a099600ff7a46573c1a2a34cd805323f.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=8c2afd4c26429bd332f19b7d442eaf2b 2500w" />
</Frame>

Now that Personal Access Tokens are enabled, click on your user’s avatar in the top right, choose **My Account Settings** in the pop-up menu, and then search for **Personal Access Tokens** on your settings page.

<Frame>
  <img src="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_personal_access_token-c39d6a9b98100f46a893e473dd8608f9.png?fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=70570c0c794fc6664c8ed6febd7fb95d" alt="Personal Access Token" data-og-width="4152" width="4152" data-og-height="2260" height="2260" data-path="images/tableau_personal_access_token-c39d6a9b98100f46a893e473dd8608f9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_personal_access_token-c39d6a9b98100f46a893e473dd8608f9.png?w=280&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=26a0b77aa78e1696eb0cb8151ceeff75 280w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_personal_access_token-c39d6a9b98100f46a893e473dd8608f9.png?w=560&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=2e3db19e49035cf91f69e5e5241df4d5 560w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_personal_access_token-c39d6a9b98100f46a893e473dd8608f9.png?w=840&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=d79c59740cfd51aa58be6c0e67f56d8d 840w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_personal_access_token-c39d6a9b98100f46a893e473dd8608f9.png?w=1100&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=6ee36de0e9148448313842543a1094f8 1100w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_personal_access_token-c39d6a9b98100f46a893e473dd8608f9.png?w=1650&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=d78e0f48dfa13785633663915f498621 1650w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_personal_access_token-c39d6a9b98100f46a893e473dd8608f9.png?w=2500&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=31c439ef3bb28b25c212755889944166 2500w" />
</Frame>

Input a desired name, say `datafold`, into the **Token Name** field, and click **Create Token**.

This will open a popup window. Click **Copy Secret** and save the copied value somewhere — you will use this when setting up Datafold. You can read more about personal access tokens on the official Tableau documentation [here](https://help.tableau.com/current/server/en-us/security%5Fpersonal%5Faccess%5Ftokens.htm).

## Create a Tableau Integration

Navigate to **<Icon icon="gear" /> Settings** → **Integrations** → **Data Apps**. Click **<Icon icon="plus" /> Add new integration**.

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=bd09718379ccede369a6e1b6738524c4" alt="Add New Integration" data-og-width="2102" width="2102" data-og-height="646" height="646" data-path="images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=83919832e4b23599314017b45690d2c1 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=1414d4d3bb1c055da9b1c52341916473 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b8f0350c0caf989153ac7c824fc516df 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=fd39b2c1819b171dcbab2fd23bee84d3 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=710aebc070a215d8943c9cf7321b8406 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_apps_add_new_integration-8fa569d0d0beb7191934287bdcdda2f1.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3558cfab5dc27eff9323d9e64d4902b7 2500w" />
</Frame>

A click on **Tableau** will lead you to the integration creation screen. Fill in the fields with data we obtained earlier. See the screenshot for hints.

<Frame>
  <img src="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_settings-a8bedc87ed42a07c156b097ddca43779.png?fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=99a0ac07d9cf4d1c93d6301663773993" alt="Tableau Integration Settings" data-og-width="4152" width="4152" data-og-height="2260" height="2260" data-path="images/tableau_settings-a8bedc87ed42a07c156b097ddca43779.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_settings-a8bedc87ed42a07c156b097ddca43779.png?w=280&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=7ac8a831e722ccb0aeb3493b9ed7d7c3 280w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_settings-a8bedc87ed42a07c156b097ddca43779.png?w=560&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=837dbea1c86db2cd6191a62c73ead900 560w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_settings-a8bedc87ed42a07c156b097ddca43779.png?w=840&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=82c984a8d119b70831679f974be9620e 840w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_settings-a8bedc87ed42a07c156b097ddca43779.png?w=1100&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=0f40f9ef8e9e536b398c955705d3e8a0 1100w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_settings-a8bedc87ed42a07c156b097ddca43779.png?w=1650&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=57470c8ec01687f50bd8d5294f53f197 1650w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tableau_settings-a8bedc87ed42a07c156b097ddca43779.png?w=2500&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=0272092dec7b91e1d6e4bcad7e426034 2500w" />
</Frame>

…and click **Save**.

## What's next?

The initial sync might take some time; it depends on the number of objects at your Tableau site. Eventually, Tableau entities — **Data Connections**, **Workbooks**, and **Dashboards** should appear at your **Lineage** tab.

<Tip>
  **TIP**

  [Tracking Jobs](/integrations/bi-data-apps/tracking-jobs) explains how to find out when your data app integration is ready.
</Tip>

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/search-4538ec5be9e0ecce0829e7e7eee94bd9.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=5c50a2f796a1b466fe221383084af2bc" alt="Search Tableau Entities" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/search-4538ec5be9e0ecce0829e7e7eee94bd9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/search-4538ec5be9e0ecce0829e7e7eee94bd9.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=26d31ae71d4396e9f41492ca3ddc93f9 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/search-4538ec5be9e0ecce0829e7e7eee94bd9.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=764c6f049e78c350c444967ff78b576f 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/search-4538ec5be9e0ecce0829e7e7eee94bd9.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ef01f54fdc4a078f33843d80c236d3e2 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/search-4538ec5be9e0ecce0829e7e7eee94bd9.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=0f8f3a9981eb9523b427e7c128fce4c4 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/search-4538ec5be9e0ecce0829e7e7eee94bd9.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9f451b2233ba03700748f084d6924e91 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/search-4538ec5be9e0ecce0829e7e7eee94bd9.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f1e3ce5b6c7a4135a177556c8d5a055d 2500w" />
</Frame>

Clicking on a Tableau entity will lead you to the Lineage screen:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage-cbcb37952c6d09346c7877038c9f3e39.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a47f739973d5178eba9b9d1b9160e034" alt="Tableau Lineage Screen" data-og-width="2056" width="2056" data-og-height="915" height="915" data-path="images/lineage-cbcb37952c6d09346c7877038c9f3e39.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage-cbcb37952c6d09346c7877038c9f3e39.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8cff9920b5413823694c2513f9c90b74 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage-cbcb37952c6d09346c7877038c9f3e39.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8985891daae8f58656eb4cd208441e73 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage-cbcb37952c6d09346c7877038c9f3e39.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=e240416086ff4eaff8ffee6826d22888 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage-cbcb37952c6d09346c7877038c9f3e39.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0523d2936aa81b4501449255c3d46b41 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage-cbcb37952c6d09346c7877038c9f3e39.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=03e340e89f327ce4da9473f937fd305b 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage-cbcb37952c6d09346c7877038c9f3e39.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=479546b7f2f99b1088b3cbaeec21eb9b 2500w" />
</Frame>

<Tip>
  **TIP**

  As you might have noticed on the screenshots above, Datafold does not display Tableau **Sheets**. Instead, we group, and deduplicate, all **Fields** of all **Sheets** within a **Workbook** and display them as **Fields** of the **Workbook**.

  On the screenshot directly above, `Demo Workbook` might include one **Sheet** with `Created At` field and another with `Sub Plan` field, but for our purposes we unite all of those fields beneath the **Workbook** — which makes the Lineage graph much less cluttered, and much easier to browse <Icon icon="face-smirking" />
</Tip>

## FAQ

<AccordionGroup>
  <Accordion title="Why aren't my Tableau Extracts showing up in Datafold?">
    Lineage is only supported for Tableau assets in <strong>Live</strong> mode. Assets in <strong>Extract</strong> mode will not appear in Datafold lineage or dependency views.
  </Accordion>

  <Accordion title="I changed something in Tableau — but Datafold does not reflect my changes">
    Datafold retrieves Tableau metadata using the Tableau API, which may not immediately reflect recent changes due to internal caching. If your updates aren’t showing up in Datafold, give it a few hours — they should appear once Tableau refreshes its metadata.
  </Accordion>
</AccordionGroup>
