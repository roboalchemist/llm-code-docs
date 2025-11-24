# Source: https://docs.datafold.com/integrations/databases/bigquery.md

# BigQuery

**Steps to complete:**

1. [Create a Service Account](/integrations/databases/bigquery#create-a-service-account)
2. [Give the Service Account BigQuery Data Viewer, BigQuery Job User, BigQuery Resource Viewer access](/integrations/databases/bigquery#service-account-access-and-permissions)
3. [Create a temporary dataset and give BiqQuery Data Editor access to the service account](/integrations/databases/bigquery#create-a-temporary-dataset)
4. [Generate a Service Account JSON key](/integrations/databases/bigquery#generate-a-service-account-key)
5. [Configure your data connection in Datafold](/integrations/databases/bigquery#configure-in-datafold)

## Create a Service Account

To connect Datafold to your BigQuery project, you will need to create a *service account* for Datafold to use.

* Navigate to the [Google Developers Console](https://console.developers.google.com/), click on the drop-down to the left of the search bar, and select the project you want to connect to.
  * *Note: If you do not see your project, you may need to switch accounts.*
* Click on the hamburger menu in the upper left, then select **IAM & Admin** followed by **Service Accounts**.
* Create a service account named `Datafold`.

## Service Account Access and Permissions

The Datafold service account requires the following roles and permissions:

* **BigQuery Data Viewer** for read access on all the datasets in the project.
* **BigQuery Job User** to run queries.
* **BigQuery Resource Viewer** to fetch the query logs for parsing lineage.

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_permissions-a7a43ded62c06a55f0337cf36924dcf5.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=d519e227abd888a332872e582764c3c3" data-og-width="1632" width="1632" data-og-height="1080" height="1080" data-path="images/bigquery_permissions-a7a43ded62c06a55f0337cf36924dcf5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_permissions-a7a43ded62c06a55f0337cf36924dcf5.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=51fd294a51129d4c58c48030d39f68be 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_permissions-a7a43ded62c06a55f0337cf36924dcf5.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=f5b37ca01498895ee6214b4c42988edf 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_permissions-a7a43ded62c06a55f0337cf36924dcf5.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=8a93d315df5aa90f2f2774311a5c95c1 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_permissions-a7a43ded62c06a55f0337cf36924dcf5.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=216434403ab8d42368e76cc5c7b55930 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_permissions-a7a43ded62c06a55f0337cf36924dcf5.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=bec30f822676a52428d61e5e82de1469 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_permissions-a7a43ded62c06a55f0337cf36924dcf5.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=213d9b15664c6924c53f9bdd14dd65c5 2500w" />
</Frame>

## Create a Temporary Dataset

Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in your warehouse.

**Caution** - Make sure that the dataset lives in the same region as the rest of the data, otherwise, the dataset will not be found.

Let's navigate to BigQuery in the console and create a new dataset.

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_tempdataset-b7d4da9e04f4239b90067a7d4858f183.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=80e39c735cf8b56cb83911e5b89bd29f" data-og-width="1632" width="1632" data-og-height="1080" height="1080" data-path="images/bigquery_tempdataset-b7d4da9e04f4239b90067a7d4858f183.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_tempdataset-b7d4da9e04f4239b90067a7d4858f183.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6df91c1c6119ad83e48f072d4f18cfad 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_tempdataset-b7d4da9e04f4239b90067a7d4858f183.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=387a99b64f99a91a69f9dd055b05c126 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_tempdataset-b7d4da9e04f4239b90067a7d4858f183.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a6b8f7dc3852a90f5b35160e08e7be16 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_tempdataset-b7d4da9e04f4239b90067a7d4858f183.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0920bafeaad7a67472f868f74baf327e 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_tempdataset-b7d4da9e04f4239b90067a7d4858f183.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0c59f9877e2d49ab39a4eee644b03920 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/bigquery_tempdataset-b7d4da9e04f4239b90067a7d4858f183.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=d6045097feb58d974bbe7c09d8ca3203 2500w" />
</Frame>

* Give the dataset a name like `datafold_tmp` and grant the Datafold service account the **BigQuery Data Editor** role.

## Generate a Service Account Key

Next, go back to the **IAM & Admin** page to generate a key for Datafold.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/bigquery_key-368911548a71c512d065b1a227dace96.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8507cf5601ad67bf1757082daee45bf9" data-og-width="1632" width="1632" data-og-height="1080" height="1080" data-path="images/bigquery_key-368911548a71c512d065b1a227dace96.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/bigquery_key-368911548a71c512d065b1a227dace96.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=18b2b546fd64d40c1261cb66d072844f 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/bigquery_key-368911548a71c512d065b1a227dace96.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=b8a730cd3879954da974790fc9047304 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/bigquery_key-368911548a71c512d065b1a227dace96.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=9254addd372c20c779d0dd3ba2590437 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/bigquery_key-368911548a71c512d065b1a227dace96.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d00fe16de4302197e6c174abb1e226de 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/bigquery_key-368911548a71c512d065b1a227dace96.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=99d9d2490db846e5d2e75e65a51dc78a 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/bigquery_key-368911548a71c512d065b1a227dace96.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=fb26fd122245d0151cfb3d7643a3161d 2500w" />
</Frame>

We recommend using the json formatted key. After creating the key, it will be saved on your local machine.

## Configure in Datafold

| Field Name                  | Description                                                                                                                                                                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Name                        | A name given to the data connection within Datafold                                                                                                                                                                                                    |
| Project ID                  | Your BigQuery project ID. It can be found in the URL of your Google Developers Console: [https://console.developers.google.com/apis/library?project=MY\\\_PROJECT\\\_ID](https://console.developers.google.com/apis/library?project=MY\\_PROJECT\\_ID) |
| JSON Key File               | The key file generated in the [Generate a Service Account JSON key](/integrations/databases/bigquery#generate-a-service-account-key) step                                                                                                              |
| Schema for temporary tables | The schema name that was created in [Create a temporary dataset](/integrations/databases/bigquery#create-a-temporary-dataset). It should be formatted as \<project\_id>.datafold\_tmp                                                                  |
| Processing Location         | Which processing zone your project uses                                                                                                                                                                                                                |

Click **Create**. Your data connection is ready!
