# Source: https://fivetran.com/docs/getting-started/quickstart

Title: Get Started with Fivetran | Fivetran data pipelines

URL Source: https://fivetran.com/docs/getting-started/quickstart

Markdown Content:
Quickstart Guide to Fivetran[](https://fivetran.com/docs/getting-started/quickstart#quickstartguidetofivetran)
--------------------------------------------------------------------------------------------------------------

Set up a new account with Fivetran.

* * *

Overview[](https://fivetran.com/docs/getting-started/quickstart#overview)
-------------------------------------------------------------------------

This quickstart guide shows you how to create, configure, and navigate your new Fivetran account. We offer a 14-day free trial for all new accounts that begins after your [initial sync](https://fivetran.com/docs/getting-started/glossary#initialsync) is complete. During the trial period, you can try the features included in the [Business Critical plan](https://www.fivetran.com/pricing/features) to see if Fivetran meets your business needs.

* * *

Setup instructions[](https://fivetran.com/docs/getting-started/quickstart#setupinstructions)
--------------------------------------------------------------------------------------------

### Sign up for Fivetran [](https://fivetran.com/docs/getting-started/quickstart#signupforfivetran)

Go to [https://fivetran.com/signup](https://fivetran.com/signup) to sign up. Once you enter your information and verify your email, you enter a guided setup wizard.

### Connect source [](https://fivetran.com/docs/getting-started/quickstart#connectsource)

On the **Select your data source** page, select your data source from our [supported connectors list](https://fivetran.com/docs/connectors). Fill out the setup form using the instructions embedded in the dashboard, then click **Save & test** to create your connection.

### Connect destination [](https://fivetran.com/docs/getting-started/quickstart#connectdestination)

On the **Select your data’s destination** page, select your destination from our [supported destinations list](https://fivetran.com/docs/destinations). If you do not have a destination, go to the **I don't have one** tab and click **Get started with Snowflake**. This will redirect you to the **Create a New Snowflake Trial Account** page. Fill out Fivetran's Snowflake setup form using the instructions embedded in the dashboard, then click **Save & test** to connect your destination.

### Add more connections (optional) [](https://fivetran.com/docs/getting-started/quickstart#addmoreconnectionsoptional)

If you want to try out additional connectors, follow our [Add a new connection](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/connectors#addanewconnection) instructions. You can add as many connections using as many connectors as you'd like.

Add all of your connections _before_ you begin syncing data. The free trial does not begin until your first initial sync is complete, so you'll have the most time possible to try these connections.

### Start initial sync [](https://fivetran.com/docs/getting-started/quickstart#startinitialsync)

Click **Start initial sync** to begin your connection's [initial sync](https://fivetran.com/docs/getting-started/glossary#initialsync). Fivetran notifies you once the sync is complete. Your free trial begins once a connection starts an [incremental sync](https://fivetran.com/docs/getting-started/glossary#incrementalsync).

### Add transformations (optional) [](https://fivetran.com/docs/getting-started/quickstart#addtransformationsoptional)

On the **Transformations** tab, click **Get started** to learn how to set up a new transformation, use our [Quickstart data models](https://fivetran.com/docs/transformations/quickstart), or connect our pre-built [data models](https://fivetran.com/docs/transformations/data-models). Our transformations run in your destination after we load your data in, so your raw data is always available alongside your transformed data. Learn more in our [Transformations for dbt Core* documentation](https://fivetran.com/docs/transformations/dbt).

### Add users (optional)[](https://fivetran.com/docs/getting-started/quickstart#addusersoptional)

On the **Users** tab, follow our [Add or remove users](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings#addorremoveusers) instructions to add teammates to your account. Learn about Fivetran's user roles and permissions in our [Role-Based Access Control documentation](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control).

### Monitor usage & purchase [](https://fivetran.com/docs/getting-started/quickstart#monitorusagepurchase)

Seven days into your trial, go to the **Billing** page to view your estimated usage to see what Fivetran may cost for you. Fivetran notifies you once the estimate is ready. Learn how we calculate the estimate in our [Account Trial documentation](https://fivetran.com/docs/getting-started/free-trials/account-trial#usageestimate).

Once your trial ends, choose a plan to continue using Fivetran. You can either choose a plan on your [Billing page](https://fivetran.com/dashboard/account/billing-usage/billing) and add a credit card (if applicable) or speak with a Fivetran salesperson for an annual commitment.

* * *

* dbt Core is a trademark of dbt Labs, Inc. All rights therein are reserved to dbt Labs, Inc. Fivetran Transformations is not a product or service of or endorsed by dbt Labs, Inc.

Thanks for your feedback!

Was this page helpful?
