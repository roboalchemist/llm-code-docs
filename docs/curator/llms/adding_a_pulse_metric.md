# Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_metric/adding_a_pulse_metric.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding a Pulse Metric

> Add and configure Tableau Pulse metrics for real-time dashboard performance monitoring and alerts.

In December 2023, Tableau Cloud introduced an innovative feature known as Pulse,
**which is not available in Tableau Server**.
This significant update ushered in the era of Metrics. With Pulse Metrics, users gain the ability to track individual
metrics and leverage guided exploration to gain deeper insights into their data.

Beyond just viewing metrics within Curator, you can also immediately send or subscribe to insightful digests via email.
These digests highlight crucial data changes, ensuring users always stay informed and updated.

Metrics from Tableau Pulse can be added easily to Curator using your existing
[Tableau Cloud connection](/creating_integrations/tableau_connection/creating_a_connection).

You can either create a new Metric within Curator, or add an existing one that has already been created in Tableau Pulse.

## Adding a Metric to Curator

### Create a new Metric

1. Navigate to the backend of the system (e.g. [http://curatorexample.com/backend](http://curatorexample.com/backend))
   and log in if prompted.
2. Navigate to **Tableau** > **Metrics**.
3. Click on the "New Metric" button.
4. Select the respective **Tableau Server** and **Site** drop-downs.
5. Set the **Metric Definition** dropdown to "Create New", then select the **Project** and **Data Source** you'd like to
   use.
6. Fill out the **Definition** selections in the **Details** tab to follow the specific metric.
7. Be sure to save!

### Add an existing Metric (already created on Tableau Pulse)

1. Navigate to the backend of the system (e.g. [http://curatorexample.com/backend](http://curatorexample.com/backend))
   and log in if prompted.
2. Navigate to **Tableau** > **Metrics**.
3. Click on the "New Metric" button.
4. Select the respective **Tableau Server** and **Site** and **Metric Definition** drop-downs.
5. Confirm the **Definition** selections in the **Details** tab to follow the specific metric.
6. Be sure to save!

## Embedding a Metric in Curator

By default, Metrics will have their own standalone pre-built template page that you can link to - this link can be found
on the edit-Metric page in the backend.

### Adding a Metric to a page

In addition to Curator's standalone templates, you can also add metrics to pages along side other content like images,
forms, Tableau Dashboards and even other metrics.  To add a metric to a page:

1. Navigate to the backend of the system (e.g. [http://curatorexample.com/backend](http://curatorexample.com/backend))
   and log in if prompted.
2. Navigate to **Content** > **Pages**.
3. Either find your page in the list you want to add your metric to or click "+ New Page" to create a new page.
4. Hover over the area of the page you'd like to add the Metric to, or click an element and click the "Change Element"
   button to display the element selection options.  Then select the Analytic Elements tab and click on "Tableau Metric":
   <img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/tableau_metric/adding_pulse_metric_page_builder.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=b849154cf2a3a72bc7fe0e79c1b6872c" alt="Modal showing analytic elements and highlighting Tableau metric option" data-og-width="1046" width="1046" data-og-height="795" height="795" data-path="assets/images/embedding_using_analytics/tableau_metric/adding_pulse_metric_page_builder.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/tableau_metric/adding_pulse_metric_page_builder.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=6dba6a31df67707518c2a8c62845a027 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/tableau_metric/adding_pulse_metric_page_builder.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=fa21f2a6d9e5f819ad1a0c4a506f9c7c 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/tableau_metric/adding_pulse_metric_page_builder.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=72eb1a6bf55941473f714d5fc67975ee 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/tableau_metric/adding_pulse_metric_page_builder.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=b31133ed7bdb4fd67a5348455cff313b 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/tableau_metric/adding_pulse_metric_page_builder.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=867ea9582f93bd8b3f15d270f44576b3 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/tableau_metric/adding_pulse_metric_page_builder.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=2d9683d2203b69f68b17230162b1d97c 2500w" />
5. Use the left-hand Page Styles controls to select the metric you want to embed.
6. Be sure to save!

## Accessing a Metric

In order to access a Metric on Curator, you must have a valid connection to Tableau Cloud.  The username you log in with
to the front-end of Curator *must match exactly* with the associated username on Tableau in order to properly determine
permissions.

The permissions for Metrics on Curator are based on access to the datasource that the Pulse Metric is connected to on
Tableau Cloud, or the datasource you selected on the create-Metric page. If the user you're logged in has no associated
account on Tableau, they will not be able to access the metric by default.  You can further restrict these permissions
by using the **[Restrict Access](/site_content_design/menus/restrict_access)**
menu permissions.
