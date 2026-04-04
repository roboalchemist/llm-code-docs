# Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_dashboards/adding_a_dashboard.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding a Dashboard

> Learn how to create and configure Tableau dashboards in Curator for seamless embedding and display.

Curator excels at showcasing embedded Tableau dashboards as a seamless part of your Curator site.

\***Note:** Due to limitations in Tableau's JS API we do not support embedding worksheets.  We recommend adding a
worksheet to a Dashboard instead.

## Create a Dashboard

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`) and log in if prompted.
2. Navigate to **Tableau** > **Dashboards**.
3. Click on the "New Dashboard" button.
4. Fill out the **Tableau Server**, **Site**, **Project**, **Workbook** and **Dashboard** drop-downs to select the
   Dashboard you'd like to embed.
5. Populate the remainder of the fields as desired and click on the "Create" button.

## Dashboard Sizes

Curator respects the Dashboard sizes applied in Tableau. We experience that a fixed size ensures consistency in design
throughout many screen sizes. You wonder what the best suitable size is? Consider the size of your users' screens. How
much space do you need for navigation, titles, toolbar buttons and margins you want to apply.
Do you have dashboards that should take up the full remaining screen? Go to Tableau and set its size to *automatic* and
the Dashboard will stretch to all ends in Curator.
