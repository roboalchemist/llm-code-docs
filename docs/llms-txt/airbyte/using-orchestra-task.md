# Source: https://docs.airbyte.com/platform/operator-guides/using-orchestra-task.md

# Source: https://docs.airbyte.com/platform/2.0/operator-guides/using-orchestra-task.md

# Source: https://docs.airbyte.com/platform/1.8/operator-guides/using-orchestra-task.md

# Source: https://docs.airbyte.com/platform/1.7/operator-guides/using-orchestra-task.md

# Source: https://docs.airbyte.com/platform/1.6/operator-guides/using-orchestra-task.md

# Using an Orchestra Task

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

[Orchestra](https://getorchestra.io) supports both Airbyte Cloud and Airbyte server instances. This guide will show you how to trigger Airbyte jobs with Orchestra in seconds.

## 1. Connect to Airbyte[​](#1-connect-to-airbyte "Direct link to 1. Connect to Airbyte")

Navigate to [Orchestra](https://app.getorchestra.io/integrations) and create a new integration credential. Select Airbyte Cloud or Airbyte Server, depending on your setup. You will need to create a Client ID and Client Secret to authenticate with Airbyte. Instructions for this can be found [here](/platform/using-airbyte/configuring-api-access.md).

![orchestra\_airbyte\_integration](/assets/images/OrchestraAirbyteIntegration-3c6779bcb720fd39406588fe66390dc6.png)

## 2. Create an Orchestra Task[​](#2-create-an-orchestra-task "Direct link to 2. Create an Orchestra Task")

Create an Orchestra pipeline containing an Airbyte task. You can trigger both 'Sync' and 'Reset' jobs with the Airbyte task. The task requires the following parameters:

* **Connection ID**: The ID of the connection you want to trigger.
* **Job Type**: The type of job you want to trigger. This can be either 'Sync' or 'Reset'.

![orchestra\_airbyte\_task](/assets/images/OrchestraAirbyteTask-1f8e8a78e1d9414f4399ea2ccf43160a.png)

## 3. Run the Pipeline[​](#3-run-the-pipeline "Direct link to 3. Run the Pipeline")

You can manually run your pipeline from the Orchestra UI. Alternatively, you can trigger the pipeline on a cron schedule or via an API call. Once the job is triggered, you can monitor the status of the job in the Orchestra UI.

![orchestra\_airbyte\_run](/assets/images/OrchestraAirbyteRun-4079de8fd97eb6e62583772df1cfba0c.png)

## Next Steps[​](#next-steps "Direct link to Next Steps")

You can now trigger Airbyte jobs using Orchestra. For more information on using Orchestra, check out the [Orchestra documentation](https://orchestra-1.gitbook.io/orchestra-portal/integrations/ingestion-elt/airbyte-cloud).
