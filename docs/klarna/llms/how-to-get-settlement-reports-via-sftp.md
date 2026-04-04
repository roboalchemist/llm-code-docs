# Source: https://docs.klarna.com/payments/after-payments/settlements/additional-resources/how-to-get-settlement-reports-via-sftp.md

# How to get settlement reports via SFTP

==Learn how to create SFTP credentials and connect to the Klarna SFTP. Once you have set up your credentials, the next settlement CSV reports will be automatically uploaded to your account. Optionally you can use the “Configure Reports” option in the Settlements App to additionally receive PDF reports or customize your CSV reports. Additionally, you can choose to receive the reports of all your merchant IDs (MIDs) in the same SFTP account, by changing the SFTP target directories.

Settlement reports are kept in the SFTP account for 90 days. After that period, they are deleted automatically.==

### Manage SFTP Credentials

Visit the [Settings App](https://docs.klarna.com/resources/business-tools/merchant-portal-guide/payments/settings) in the Merchant Portal and create credentials for the merchant ID. Make sure to save the .txt file which contains the username, password and ports.

| Regional Merchant Portal | Link to the SFTP credential service |
|----|----|
| Europe | [<https: portal.klarna.com="" settings="" sftp-credentials="">](https://portal.klarna.com/settings/sftp-credentials) |
| United States of America and Canada | [<https: portal.klarna.com="" settings="" sftp-credentials="">](https://portal.klarna.com/settings/sftp-credentials) |
| Australia and Asia Pacific | [<https: portal.klarna.com="" settings="" sftp-credentials="">](https://portal.klarna.com/settings/sftp-credentials) |


![klarna docs image](69410f6a-fc5f-460d-8496-acf232b03519_FIRE-sftp-credentials.gif)image

Once you have set up your credentials, the next settlement reports will be automatically uploaded to your account.

### Configuration

Use the below settings for connecting to the Klarna SFTP in production and playground (testing environment).

| Option | Production | Playground |
|----|----|----|
| Address | merchants.sftp.klarna.com | sftp.playground.klarna.net |
| Protocol | SFTP | SFTP |
| Port | 4001 | 4001 |
| Username & Password | As provided by the SFTP credential self-service in the Merchant Portal Settings App. [See section above.](https://docs.klarna.com/settlement-reports/tutorials/how-to-get-settlement-reports-via-sftp) | As provided by the SFTP credential self-service in the Merchant Portal Settings App. [See section above.](https://docs.klarna.com/settlement-reports/tutorials/how-to-get-settlement-reports-via-sftp) |

### File names

The file name of the Settlement Report from the SFTP includes the unique Payment Reference for the payout, and the timestamp of report generation day (00:00:00) in UTC: paymentReference.TimeStamp.format Example: 123456789_20180809T000226_0.csv In this example, 123456789, is the Payment Reference for this payout. This payment reference is also included in the Settlement Report’s header. The second part 20180809T000000+0000, is the timestamp of the report generation day. It is in UTC and bound to the start of the day. **Note:** The Merchant Portal and Settlements API are using a different naming convention: settlement.paymentReference.format **Temporary files:** Please Ignore `.tmp` suffixed files, for <example:1>`23456789_20180809`T000226_0.csv These are reports that are currently being created.

### Manually upload settlement reports to your SFTP account

You might want to manually upload a CSV or PDF report to your SFTP account. For example, after changing the report structure with the Report Configurator. Simply click on the respective payment reference in the Settlements table and choose to "Send to SFTP".


![klarna docs image](7f853bf8-bb1b-4ad6-a9be-59f6ecb2681c_fire-send-to-sftp.gif)image</example:1></https:></https:></https:>