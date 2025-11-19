# Source: https://docs.pinecone.io/guides/organizations/manage-billing/standard-trial.md

# Standard trial

> Get $300 credits for 21 days with the Standard plan trial.

The Standard trial lets you evaluate Pinecone without requiring any up-front payment. You get \$300 in credits over 21 days with access to Standard plan [features](https://www.pinecone.io/pricing/) and [limits](/reference/api/database-limits) that are suitable for testing Pinecone at scale.

<Note>
  If you're building a small or personal project, consider the free [Starter plan](https://www.pinecone.io/pricing/) instead.
</Note>

## Key features

* \$300 in credits
* 21 days of access to Standard plan [features](https://www.pinecone.io/pricing/), including:
  * [Bulk import](/guides/index-data/import-data)
  * [Backup and restore](/guides/manage-data/backups-overview)
  * [RBAC (role-based access control)](/guides/production/security-overview#role-based-access-control)
* [Higher limits](/reference/api/database-limits) for testing at scale
* Access to all [cloud regions](/guides/index-data/create-an-index#cloud-regions)
* Access to [Developer Support](https://www.pinecone.io/pricing/?plans=support\&scrollTo=product-pricing-modal-section)

## Expiration

At the end of the trial, or when you've used up all your credits, you can add a payment method and continue on with the Standard plan, or you can upgrade to an Enterprise plan. Learn more about [pricing](https://www.pinecone.io/pricing/).

Before your Standard trial expires, you can downgrade to a Starter plan. To do so, you must first bring your usage within Starter plan limits:

* No more than 5 indexes, all serverless and in the `us-east-1` region of AWS
  * If you have serverless indexes in a region other than `us-east-1`, [create a new serverless index](/guides/index-data/create-an-index#create-a-serverless-index) in `us-east-1`, [re-upsert your data](/guides/index-data/upsert-data) into the new index, and [delete the old index](/guides/manage-data/manage-indexes#delete-an-index).
  * If you have more than 5 serverless indexes, [delete indexes](/guides/manage-data/manage-indexes#delete-an-index) until you have 5 or fewer.
  * If you have pod-based indexes, [save them as collections](/guides/manage-data/back-up-an-index#create-a-backup-using-a-collection) and then [delete them](/guides/manage-data/manage-indexes#delete-an-index).
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

After your Standard trial expires, you can downgrade to a Starter plan **only if** your account is already within Starter plan limits (that is, if you already reduced your usage to within Starter plan limits **before** the trial expired). Otherwise, you'll need to upgrade your account to a paid plan, or let it get deleted.

If you have questions, [contact Support](https://www.pinecone.io/contact/support/).

## Limits

* Each organization is allowed only one trial.
* To activate a Standard plan trial, you must select the trial when registering your account on [https://pinecone.io](https://pinecone.io).
* You cannot activate a Standard trial in the following cases:
  * You already signed up for an account on [https://pinecone.io](https://pinecone.io), and you selected another type of plan (Starter, Standard, or Enterprise).
  * Before registering your account on [https://pinecone.io](https://pinecone.io), your organization subscribed through marketplace partners.

If you have any questions, [contact Support](https://www.pinecone.io/contact/support/).
