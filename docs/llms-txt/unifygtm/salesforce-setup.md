# Source: https://docs.unifygtm.com/reference/integrations/orum/salesforce-setup.md

# Source: https://docs.unifygtm.com/reference/integrations/nooks/salesforce-setup.md

# Source: https://docs.unifygtm.com/reference/integrations/orum/salesforce-setup.md

# Source: https://docs.unifygtm.com/reference/integrations/nooks/salesforce-setup.md

# Source: https://docs.unifygtm.com/reference/integrations/orum/salesforce-setup.md

# Source: https://docs.unifygtm.com/reference/integrations/nooks/salesforce-setup.md

# Nooks Salesforce Setup

> Configure Nooks integration with Salesforce for call task synchronization.

# Salesforce Setup for Nooks Integration

This guide walks you through the steps required to set up call tasks in Salesforce and configure the Nooks integration for seamless call campaign management.

## Overview

You can bidirectionally sync your call tasks between Unify and Nooks using a Salesforce report. The instructions below will help you build a report to successfully set up the sync.

## Salesforce Report Setup

### Call Report Setup in Salesforce

To create call tasks in Salesforce, set up a new report with the following criteria:

1. Navigate to your Salesforce Reports tab
2. Click **New Report**
3. Configure the report with these settings:
   * **Category**: Activities (Activities with Contacts)
   * **Show Me**: All activities
   * **Date**: All Time
   * **Show**: Open Activities
   * **Show**: Tasks
   * **Assigned**: equals \$USER
   * **Task Subtype**: equals Call

<Note>
  These report filters ensure that each user in Nooks only sees their own open call tasks
</Note>

<Frame><img src="https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=5b1e59e21b44231d0bda66e623728092" alt="salesforce-report-filters.png" data-og-width="387" width="387" data-og-height="640" height="640" data-path="images/reference/integrations/orum/salesforce-report-filters.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?w=280&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=21a820992314f94b9d74c0f6ac644164 280w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?w=560&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=edb8a19385ebee1cdaa12b8590126159 560w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?w=840&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=8a237b0702b5356918800df34dbbded2 840w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?w=1100&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=8f09aa5bea90a81b3b990c46b143b36b 1100w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?w=1650&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=5506bbd4c5f3b855c9895e78d56f8e3e 1650w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?w=2500&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=26b160ab0db565c745904cd78a7e94e1 2500w" /></Frame>

### Best Practices for Report Columns

We recommend including the following columns in your report for better visibility and alignment with Unify sequences:

1. Click **Customize** on your report
2. Add the following columns:
   * Subject
   * First Name
   * Last Name
   * Unify Sequence

<Frame><img src="https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=b44857af3ebb733b9880615ed3e9176c" alt="salesforce-column-setup.png" data-og-width="418" width="418" data-og-height="640" height="640" data-path="images/reference/integrations/orum/salesforce-column-setup.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?w=280&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=d983866fa604a227ce99edafe347acb7 280w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?w=560&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=cd802fb66106d991db90fc22d74b73d4 560w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?w=840&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=a9c0f33d842106aa5a84fbb1a78c79c7 840w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?w=1100&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=40d31b55a1d796d926fc7d9e73feecde 1100w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?w=1650&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=4ed0c5852f172a55ee57baa895724135 1650w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?w=2500&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=0e662e08fd1cd4955ecc3e269252d51a 2500w" /></Frame>

## Nooks Integration Setup

<Info>
  **Sep 2025 Update: Installing Nooks as a Trusted App in Salesforce**

  In September 2025, Salesforce made security changes regarding which apps can be connected to Salesforce (via OAuth) by individual reps. This can impact Nooks users who are connecting to Salesforce for the first time, or reconnecting Salesforce. They might see an "OAuth Error" like this:

  <Frame>  <img src="https://mintcdn.com/unify-19/SMh_isreZvLK6DBw/images/reference/integrations/nooks/salesforce-oauth-error.png?fit=max&auto=format&n=SMh_isreZvLK6DBw&q=85&s=a1ebaeb24ed30aab2ed88e3efea4bc2c" alt="salesforce-oauth-error.png" data-og-width="764" width="764" data-og-height="788" height="788" data-path="images/reference/integrations/nooks/salesforce-oauth-error.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/SMh_isreZvLK6DBw/images/reference/integrations/nooks/salesforce-oauth-error.png?w=280&fit=max&auto=format&n=SMh_isreZvLK6DBw&q=85&s=9bb77abc9abdd32edc2f4c1c62c02581 280w, https://mintcdn.com/unify-19/SMh_isreZvLK6DBw/images/reference/integrations/nooks/salesforce-oauth-error.png?w=560&fit=max&auto=format&n=SMh_isreZvLK6DBw&q=85&s=1c47d6180098971aae3ac41f91c06965 560w, https://mintcdn.com/unify-19/SMh_isreZvLK6DBw/images/reference/integrations/nooks/salesforce-oauth-error.png?w=840&fit=max&auto=format&n=SMh_isreZvLK6DBw&q=85&s=8009ee2a2b0e524f9c5b25397a5049c9 840w, https://mintcdn.com/unify-19/SMh_isreZvLK6DBw/images/reference/integrations/nooks/salesforce-oauth-error.png?w=1100&fit=max&auto=format&n=SMh_isreZvLK6DBw&q=85&s=17ba9540bcebc4f639da37da353da2b7 1100w, https://mintcdn.com/unify-19/SMh_isreZvLK6DBw/images/reference/integrations/nooks/salesforce-oauth-error.png?w=1650&fit=max&auto=format&n=SMh_isreZvLK6DBw&q=85&s=d26fd5af55f5e88685cf9c11d85dc3f7 1650w, https://mintcdn.com/unify-19/SMh_isreZvLK6DBw/images/reference/integrations/nooks/salesforce-oauth-error.png?w=2500&fit=max&auto=format&n=SMh_isreZvLK6DBw&q=85&s=0e9207211e926bf376293590b3e69931 2500w" /></Frame>

  Your Salesforce administrator will need to install Nooks as a trusted app in your Salesforce org. For more information, see: [Installing Nooks as a Trusted App in SFDC](https://support.devrev.ai/nooks/article/ART-115-getting-started-with-salesforce-sfdc#Sep%202025%20Update%3A%20Installing%20Nooks%20as%20a%20Trusted%20App%20in%20SFDC).
</Info>

Once your Salesforce report is ready, connect Nooks to Salesforce:

1. Navigate to **Settings** in Nooks
2. Select **Integrations**
3. Select **Connect Salesforce** and authorize the connection
4. Install Nooks as an OAuth app. Nooks should appear as an app in the Salesforce Setup settings in the "Connected Apps OAuth Usage" section. Click "Install".
5. \[Recommended] Configure field mappings to optimize your call tasks:
   * Navigate to **Settings** > **Salesforce** > **Field Mappings**
   * Add your specific SFDC fields such as:
     * Current Unify Sequence
     * Current Unify Play
     * Relevant prospect information for call tasks

<Note>
  You will need admin access to Salesforce to authorize this connection. For more information, see: [Nooks admin setup](https://support.devrev.ai/nooks/article/ART-115-getting-started-with-salesforce-sfdc) or reach our to your CSM.
</Note>

## Next Steps

With your Salesforce integration configured and Nooks connected, you're ready to [launch your first call campaign](/reference/integrations/orum/call-campaigns)!
