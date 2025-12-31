# Source: https://docs.aporia.com/data-sources/big-query.md

# BigQuery

This guide describes how to connect Aporia to a BigQuery data source in order to monitor your ML Model in production.&#x20;

We will assume that your model inputs, outputs and optionally delayed actuals can be queried with SQL. This data source may also be used to connect to your model's training set to be used as a baseline for model monitoring.

### Create a materialization dataset for Aporia queries

Create a materialization dataset for Aporia to use to perform queries, see instructions [here](https://cloud.google.com/bigquery/docs/datasets#create-dataset).

A separate materialization dataset location, to which query results will be written, must be designated for each project from which you want to query.

### Update the Aporia Service Account for BigQuery access

In order to provide access to BigQuery, you'll need to update your Aporia service account with the necessary API permissions.

#### Step 1: Obtain your aporia service account

Use the same service account used for the Aporia deployment. If someone else on your team has deployed Aporia, please reach out to them to obtain it.

#### Step 2: Grant read access to the relevant project

1. Go to the [IAM console](https://console.cloud.google.com/iam-admin/) and login.
2. Find the Aporia service account you obtain in the previous step and click on 🖋 **Edit Principle**<br>

   <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FoyGqcuJUNqwSagV4mBTI%2Fimage.png?alt=media&#x26;token=48fd35fa-ed3b-4cb2-a3c2-33a2d96721aa" alt=""><figcaption></figcaption></figure>
3. In the "Edit access" window click on **ADD ANOTHER ROLE**<br>

   <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FOxCIRvkqCRYU5ZWbFkG9%2Fimage.png?alt=media&#x26;token=0dd0e13a-d6da-4b15-81ba-c3fab444e3e6" alt=""><figcaption></figcaption></figure>
4. Add the `BigQuery Data Viewer` and `BigQuery Job User` roles and click **Save**<br>

   <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2F5oHuIXXxdd38qmVSLlOB%2Fimage.png?alt=media&#x26;token=e603e9aa-b39e-4da2-88a2-13f37175aab9" alt=""><figcaption></figcaption></figure>

#### Step 3: Grant access to the materialization dataset

1. Go to the [BigQuery console](https://console.cloud.google.com/bigquery) and login.
2. In the left-hand panel, expand the relevant project and find the materialization dataset you created in the previous steps.<br>

   <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FerW3P1DCbZPEputlVJ2c%2Fimage.png?alt=media&#x26;token=2daec3a1-c34c-4126-9186-99954964339b" alt=""><figcaption></figcaption></figure>
3. Click on "**...**" by the dataset name, then click on **Share**
4. In the "Share permissions" window click on **Add Principal**<br>

   <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FZ1NBLqHjwYDKZjnwWkWN%2Fimage.png?alt=media&#x26;token=009b0c71-ef54-45bd-b9b7-f2cb2a5f7366" alt=""><figcaption></figcaption></figure>
5. In the "New principal" box, enter the email of the Aporia service account you have obtained. Choose the `BigQuery Data Editor` role and click **Save**.<br>

   <figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FfWgUeqKTrJBzMDSt8Imo%2Fimage.png?alt=media&#x26;token=a8ab4455-d96e-4471-82f6-d62373a837a8" alt=""><figcaption></figcaption></figure>

Now Aporia has the permission it needs to connect to the BigQuery datasets and tables you have specified in the policy.

### Create a BigQuery data source in Aporia

1. Go to [Aporia platform](https://platform.aporia.com/) and login to your account.
2. Go to **Integrations** page and click on the **Data Connectors** tab
3. Scroll to **Connect New Data Source** section
4. Click **Connect** on the BigQuery card and follow the instructions

Bravo! :clap: now you can use the data source you've created across all your models in Aporia.
