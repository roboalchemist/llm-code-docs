# Source: https://docs.pinecone.io/guides/organizations/manage-billing/downgrade-billing-plan.md

# Source: https://docs.pinecone.io/guides/assistant/admin/downgrade-billing-plan.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Downgrade your plan

> Downgrade from a paid plan to the free Starter plan.

<Note>
  To change your billing plan, you must be an [organization owner or billing admin](/guides/organizations/understanding-organizations#organization-roles).
</Note>

## Requirements

Before you can downgrade, your organization must be under the [Starter plan quotas](/reference/api/database-limits):

* No more than 5 indexes, all serverless and in the `us-east-1` region of AWS
  * If you have serverless indexes in a region other than `us-east-1`, [create a new serverless index](/guides/index-data/create-an-index#create-a-serverless-index) in `us-east-1`, [re-upsert your data](/guides/index-data/upsert-data) into the new index, and [delete the old index](/guides/manage-data/manage-indexes#delete-an-index).
  * If you have more than 5 serverless indexes, [delete indexes](/guides/manage-data/manage-indexes#delete-an-index) until you have 5 or fewer.
  * If you have pod-based indexes, [delete them](/guides/manage-data/manage-indexes#delete-an-index).
* No more than 1 project
  * If you have more than 1 project, [delete all but 1 project](/guides/projects/manage-projects#delete-a-project).
  * Before you can delete a project, you must [delete all indexes](/guides/manage-data/manage-indexes#delete-an-index) and [delete all collections](/guides/manage-data/back-up-an-index#delete-a-collection) in the project.
* No more than 2 GB of data across all of your serverless indexes
  * If you are storing more than 2 GB of data, [delete records](/guides/manage-data/delete-data) until you're storing less than 2 GB.
* No more than 100 namespaces per serverless index
  * If any serverless index has more than 100 namespaces, [delete namespaces](/guides/manage-data/delete-data#delete-all-records-from-a-namespace) until it has 100 or fewer remaining.
* No more than 3 [assistants](/guides/assistant/overview)
  * If you have more than 3 assistants, [delete assistants](/guides/assistant/manage-assistants#delete-an-assistant) until you have 3 or fewer.
* No more than 10 files per assistant
  * If you have more than 10 files uploaded to an assistant, [delete files](/guides/assistant/manage-files#delete-a-file) until the assistant has 10 or fewer.
* No more than 1 GB of assistant storage
  * If you have more than 1 GB of assistant storage, [delete files](https://docs.pinecone.io/guides/assistant/manage-files#delete-a-file) until you're storing less than 1 GB.
* No more than 2 users
* No collections or backups (these are automatically deleted as part of the downgrade process)

## Downgrade to the Starter plan

The downgrade process is different depending on how you are paying for Pinecone.

<Warning>
  It is important to start the downgrade process in the Pinecone console, as described below. When you do so, Pinecone checks that you are under the [Starter plan quotas](#requirements) before allowing you to downgrade. In contrast, if you start the downgrade process in one of the cloud marketplaces, Pinecone cannot check that you are under these quotas before allowing you to downgrade. If you are over the quotas, Pinecone will deactivate your account, and you will need to [contact support](https://www.pinecone.io/contact/support/).
</Warning>

<Tabs>
  <Tab title="Credit card">
    If you are paying with a credit card, downgrade as follows:

    1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
    2. Click **Downgrade** in the **Starter** plan section.

    Your billing will end immediately. However, you will receive a final invoice for any charges accrued in the current month.
  </Tab>

  <Tab title="Google Cloud Marketplace">
    If you are paying through the Google Cloud Marketplace, downgrade as follows:

    1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
    2. In the **Starter** section, click **Downgrade**.
    3. Click **Confirm downgrade**.
    4. On the **Continue your downgrade on the GCP marketplace** modal, click **Continue to marketplace**. This takes you to your orders page in Google Cloud Marketplace.
    5. [Cancel the order](https://cloud.google.com/marketplace/docs/manage-billing#saas-products) for your Pinecone subscription.

       <Tip>
         If you don't see the order, check that the correct billing account is selected.
       </Tip>

    Your billing will end immediately. However, you will receive a final invoice for any charges accrued in the current month.
  </Tab>

  <Tab title="AWS Marketplace">
    If you are paying through the AWS Marketplace, downgrade as follows:

    1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
    2. In the **Starter** section, click **Downgrade**.
    3. Click **Confirm downgrade**.
    4. On the **Continue your downgrade on the AWS marketplace** modal, click **Continue to marketplace**. This takes you to the [Manage subscriptions](https://console.aws.amazon.com/marketplace) page in the AWS Marketplace.
    5. [Cancel the subscription](https://docs.aws.amazon.com/marketplace/latest/buyerguide/cancel-subscription.html#cancel-saas-subscription) to Pinecone.

    Your billing will end immediately. However, you will receive a final invoice for any charges accrued in the current month.
  </Tab>

  <Tab title="Microsoft Marketplace">
    If you are paying through the Microsoft Marketplace, downgrade as follows:

    1. In the Pinecone console, go to [**Settings > Billing > Plans**](https://app.pinecone.io/organizations/-/settings/billing/plans).
    2. In the **Starter** section, click **Downgrade**.
    3. Click **Confirm downgrade**.
    4. On the **Continue your downgrade on Microsoft marketplace** modal, click **Continue to marketplace**.
    5. On the **SaaS** page, click your subscription to Pinecone.
    6. Click **Cancel subscription**.
    7. Confirm the cancellation.

    Your billing will end immediately. However, you will receive a final invoice for any charges accrued in the current month.
  </Tab>
</Tabs>
