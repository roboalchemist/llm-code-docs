# Source: https://docs.rootly.com/integrations/google-cloud-monitoring.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Cloud Monitoring

> Receive alerts from Google Cloud Monitoring to trigger incidents, route to Slack, or page on-call teams.

Google Cloud Monitoring can be configured as an alert source to send events into Rootly as alerts. The alerts received on Rootly can then be routed to a Slack channel, used to initiate incidents, or used to page Rootly On-Call targets.

## Configure Webhook in GCP

Navigate to Google Cloud Console and click on the VIEW ALL PRODUCTS button in the left pane to access the complete list of products.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/PTQsS2VTzmCsSwYt/images/integrations/google-cloud-monitoring/images-1.webp?fit=max&auto=format&n=PTQsS2VTzmCsSwYt&q=85&s=f3ef4e09c595b3a35ba0efce4e6c2bcd" width="866" height="434" data-path="images/integrations/google-cloud-monitoring/images-1.webp" />
</Frame>

In the left pane, find and select the **Observability** category, then choose **Monitoring**.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/PTQsS2VTzmCsSwYt/images/integrations/google-cloud-monitoring/images-2.webp?fit=max&auto=format&n=PTQsS2VTzmCsSwYt&q=85&s=576b6896f9a9d51adc479a2ab89c8f4e" width="866" height="428" data-path="images/integrations/google-cloud-monitoring/images-2.webp" />
</Frame>

In the **Monitoring** section, select **Alerting** from the left pane and click on the **EDIT NOTIFICATION CHANNELS** button at the top.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/PTQsS2VTzmCsSwYt/images/integrations/google-cloud-monitoring/images-3.webp?fit=max&auto=format&n=PTQsS2VTzmCsSwYt&q=85&s=44c0f8c43a4d1fc9eae55d1f9aae2741" width="863" height="279" data-path="images/integrations/google-cloud-monitoring/images-3.webp" />
</Frame>

Find the **Webhooks** channel and click on the **ADD NEW** button next to it.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/PTQsS2VTzmCsSwYt/images/integrations/google-cloud-monitoring/images-4.webp?fit=max&auto=format&n=PTQsS2VTzmCsSwYt&q=85&s=18471352d585b936d79e7b6c7b5d5796" width="853" height="137" data-path="images/integrations/google-cloud-monitoring/images-4.webp" />
</Frame>

Fill in the form with the required details:

`**Display Name**` - give your webhook a description name

Check the `**Use HTTP Basic Auth**` checkbox.

Enter the following URL into the `**Endpoint URL**` field.

<Note>
  Rootly is able to receive two types of alerts: *paging* and *non-paging*.

  * *Paging* alerts will page the notification target specified in the `**Endpoint URL**` field.
  * *Non-Paging* alerts will simply appear in the [Alerts page](https://rootly.com/account/alerts "Alerts page"), but will not page anyone.
</Note>

The inclusion of a notification target determines whether the alert is a paging or non-paging alert.

Enter the following URL into the `**Endpoint URL**` for a *paging* alert.

```txt Endpoint URL theme={null}
https://webhooks.rootly.com/webhooks/incoming/google_cloud_webhooks/notify/<TYPE>/<ID>  
```

<Warning>
  You need to replace the \<TYPE> and \<ID> placeholders with the following values:

  * `TYPE` - this defines the Rootly resource type that will be used for paging.
    * The following are the available values: `User` | `Group` (Team) | `EscalationPolicy` | `Service`
  * `ID` - this specifies the exact resource that will be targeted for the page.
    * The id of the resource can be found when editing each resource.
</Warning>

Enter the following URL into the `**Endpoint URL**` for a *non-paging* alert.

```txt Endpoint URL theme={null}
https://webhooks.rootly.com/webhooks/incoming/google_cloud_webhooks  
```

Enter the following value into the `**Auth Username**` field.

```txt Auth Username theme={null}
rootly  
```

You can pick up your organization-specific `**Auth Password**` from the [Alert Sources page](https://rootly.com/account/alert-sources/new "Alert Sources page"). Click on the **Google Cloud Platform (GCP)** option and enter a descriptive name for your GCP alert source.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/PTQsS2VTzmCsSwYt/images/integrations/google-cloud-monitoring/images-5.webp?fit=max&auto=format&n=PTQsS2VTzmCsSwYt&q=85&s=cea4f9418059463648cf8a1366a8b21d" width="862" height="193" data-path="images/integrations/google-cloud-monitoring/images-5.webp" />
</Frame>

Copy your organization-specific `**Auth Password**` from the 5th step.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/PTQsS2VTzmCsSwYt/images/integrations/google-cloud-monitoring/images-6.webp?fit=max&auto=format&n=PTQsS2VTzmCsSwYt&q=85&s=f53a18eb421be510d8701a1907070622" width="876" height="695" data-path="images/integrations/google-cloud-monitoring/images-6.webp" />
</Frame>

Click on the **TEST CONNECTION** button to verify the webhook configuration. A successful test will enable the **SAVE** button.

Once the connection test is successful, click the **SAVE** button to finalize the webhook setup.


Built with [Mintlify](https://mintlify.com).