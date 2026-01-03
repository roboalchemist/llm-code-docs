# Source: https://docs.lunary.ai/docs/more/data-warehouse/bigquery.md

# BigQuery Connector

## Setup Google Cloud

### Enable APIs

If not already done, enable the following APIs for the project where you want to install the Google BigQuery instance:

* [Datastream API](https://console.cloud.google.com/marketplace/product/google/datastream.googleapis.com)
* [BigQuery API](https://console.cloud.google.com/marketplace/product/google-cloud-platform/bigquery)

### Get your API Key

1. Go to [Create Service Account](https://console.cloud.google.com/iam-admin/serviceaccounts/create).
2. Give it the name `Lunary Data Warehouse Account`.
3. Click on **Create and continue**.
4. Click on **Select a role** and choose the `Datastream Admin` role.
5. Click on **Add another role**.
6. Click on **Select a role** and choose the `BigQuery Admin` role.
7. Click on **Continue**.
8. Click on **Done**.
9. Click on the `Lunary Data Warehouse Account`.
10. Click on **Keys**.
11. Click on **Add Key** and select the `Create new key` option from the drop-down menu.
12. Make sure `JSON` is selected for the **Key Type**, and click on **Create**.
13. Your private key will be downloaded to your computer. Save this private key.

## Setup PostgreSQL source

### Cloud SQL

1. Go to the [Cloud SQL](https://console.cloud.google.com/sql/instances) Instances page in the Google Cloud Console.
2. Select the instance to which you want Datastream to connect.
3. Click **Edit**.
4. Scroll down to the **Flags** section.
5. Click **ADD FLAG**.
6. Choose the `cloudsql.logical_decoding` flag from the drop-down menu.
7. Set its flag value to `on`.
8. Click `SAVE` to save your changes. You'll need to restart your instance to update it with the changes. Once your instance has been restarted, confirm your changes under **Database flags** on the Overview page.

### Amazon RDS

1. Launch your Amazon RDS Dashboard.
2. In the **Navigation Drawer**, click **Parameter Groups**, and then click **Create Parameter Group**. The **Create Parameter Group** page appears.
3. Select `PostgreSQL` for the database family, provide a name and description for the parameter group, and then click **Create**.
4. Select the check box to the left of your newly created parameter group, and then, under **Parameter Group Actions**, click **Edit**.
5. Set `logical_replication` to `1`.
6. Click **Save changes**.
7. In the **Navigation drawer**, click **Databases**.
8. Select your source, and then click **Modify**.
9. Scroll down to the **Additional configuration** section.
10. Select the parameter group that you created.
11. Click **Continue**.
12. Under **Scheduling of modifications**, select `Apply immediately`.

Because you've modified your source, you must wait until the changes to your parameter group are applied before proceeding.

13. In the **Navigation drawer**, click **Databases**, and then select your database instance.
14. Click the **Configurations** tab.
15. Verify that you see the parameter group that you created, and that its status is `pending-reboot`.
16. From the **Instance Actions** menu, select `Reboot`.

### Self-hosted PostgreSQL

1. Add `wal_level=logical` to the postgresql.conf file, or do this on the server command line.
2. Restart the server.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt