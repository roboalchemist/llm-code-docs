# Source: https://docs.gitguardian.com/platform/configure-alerting/notifiers-integrations/splunk.md

# Splunk

> Configure Splunk integration to forward GitGuardian incident events via HTTP Event Collector.

To receive GitGuardian notifications on Splunk, you need a Splunk instance and must generate an HTTP Event Collector (HEC) token. Follow the instructions below to set it up.

Once you have your webhook URL and token, enter them on the Integrations page.

:::caution
This integration works with all paid Splunk plans but is not supported on the free plan.
:::

### How to integrate

1. Open the Splunk web interface and navigate to **Settings** > **Data inputs**.
   ![splunk1](/img/platform/configure-alerting/notifiers-integrations/splunk/1.png)
   ![splunk2](/img/platform/configure-alerting/notifiers-integrations/splunk/2.png)

2. Add a new **HTTP Event Collector** and click the button to create a new token.
   ![splunk3](/img/platform/configure-alerting/notifiers-integrations/splunk/3.png)
   ![splunk4](/img/platform/configure-alerting/notifiers-integrations/splunk/4.png)

3. Provide a name (and optionally a description) for your Event Collector, then click **Next**.
   ![splunk5](/img/platform/configure-alerting/notifiers-integrations/splunk/5.png)

4. Select an existing index or create a new one, then click **Review**.
   ![splunk6](/img/platform/configure-alerting/notifiers-integrations/splunk/6.png)
   ![splunk6.1](/img/platform/configure-alerting/notifiers-integrations/splunk/6bis.png)

5. Verify the settings and click **Submit** to create your token.
   ![splunk7](/img/platform/configure-alerting/notifiers-integrations/splunk/7.png)

6. Go back to **Settings** > **Data inputs**. Tokens are disabled by default, so click **Global Settings** to enable it.
   ![splunk8](/img/platform/configure-alerting/notifiers-integrations/splunk/8.png)
   ![splunk9](/img/platform/configure-alerting/notifiers-integrations/splunk/9.png)
   ![splunk10](/img/platform/configure-alerting/notifiers-integrations/splunk/10.png)

7. If your instance URL is `https://prd-p-xxxxxxxxxxxx.cloud.splunk.com/`, your webhook URL will be:
   `https://input-prd-p-xxxxxxxxxxxx.cloud.splunk.com:8088/services/collector/event`.
   ![splunk11](/img/platform/configure-alerting/notifiers-integrations/splunk/11.png)

8. Enter your webhook URL and token into the [Splunk integration section](https://dashboard.gitguardian.com/settings/integrations/splunk) of your dashboard settings.

9. **Team Configurations:**
   For business workspaces, you can configure the Splunk integration per team:
   - Create a single configuration under the `All-incidents` team to send all GitGuardian incidents to the same Splunk project.
   - Alternatively, create separate configurations for each team to send incidents to specific projects.
     ![Splunk team](/img/platform/configure-alerting/notifiers-integrations/splunk/team-notifiers-splunk.png)
