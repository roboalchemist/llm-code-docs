# Source: https://posthog.com/docs/workflows/import-customerio-optouts.md

# Import opt-out lists from Customer.io - Docs

In this guide we'll walk through importing your **opt-out lists from Customer.io** into PostHog. After following this guide, you will:

-   Create an API key in Customer.io
-   Export people with subscription preferences
-   Import opt-outs into PostHog

1.  1

    ## Create an app API key in Customer.io

    Required

    First, you'll need to create an app API key in Customer.io. This key will be used later to import all categories and generally unsubscribed customers.

    Go to **[Settings > Account Settings > App API Keys](https://fly.customer.io/settings/api_credentials?keyType=app)** in your Customer.io dashboard.

    Click **Create New App API Key** and give it a descriptive name (e.g. "PostHog Import").

    **Important**: Save this API key securely - you'll need it in step 3. Customer.io will only show it once.

2.  2

    ## Export people with subscription preferences

    Required

    Now you need to export a CSV of people who have opted out of specific categories.

    Go to the **People** page in your Customer.io dashboard.

    To filter for people with subscription preferences:

    1.  Click **conditions** at the top of the page
    2.  Select `cio_subscription_preferences` from the dropdown
    3.  Choose the **exists** operator
    4.  Confirm your choice

    ![Adding attribute filter for cio_subscription_preferences](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/1_a04d048af2.png)![Adding attribute filter for cio_subscription_preferences](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/1_a04d048af2.png)

    This will update the people list in the table below to show only those with subscription preferences.

    Now export this data:

    1.  Click **Export to CSV** in the top right corner
    2.  Click **Choose attributes**
    3.  Select only these two attributes:
        -   `cio_subscription_preferences`
        -   `email` (make sure it's `email` and **not** `$email`)

    ![Choosing export attributes](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/2_0cf22e73b9.png)![Choosing export attributes](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/2_0cf22e73b9.png)

    Customer.io will send you an email with a download link for the CSV file. Download this file - you'll upload it to PostHog in the next step.

3.  3

    ## Import into PostHog

    Required

    Go to your PostHog app and navigate to **Workflows > Opt-out list**.

    ![PostHog opt-out list page](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/3_9e79e42360.png)![PostHog opt-out list page](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/3_9e79e42360.png)

    Click **Import from Customer.io**.

    You'll see a two-step import process:

    ### Step 1: Import via API key

    Enter the API key you created in step 1. This will import:

    -   All available categories from Customer.io
    -   All customers who are generally unsubscribed (not subscribed to any category)

    ![Enter API key](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/4_18a3a268e3.png)![Enter API key](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/4_18a3a268e3.png)

    Due to rate limiting, we need to import customers that opted out of certain categories through the CSV.

    ### Step 2: Upload CSV

    Once step 1 is completed, you'll be prompted to upload the CSV file you downloaded in step 2.

    ![Upload CSV file](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/5_076d8fa46c.png)![Upload CSV file](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/5_076d8fa46c.png)

    1.  Click **Choose file** and select the CSV you downloaded from Customer.io
    2.  Click **Upload & process CSV**

    This will import customers who opted out of specific categories (those with granular subscription preferences).

    ![Processing CSV](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/6_d9c7957fcd.png)![Processing CSV](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/6_d9c7957fcd.png)

    Once complete, you'll see a success message with a summary of imported opt-outs.

    Your Customer.io opt-out lists are now imported into PostHog. These users will automatically be excluded from all future workflow campaigns based on their preferences.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better