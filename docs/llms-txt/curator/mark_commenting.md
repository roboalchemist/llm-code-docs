# Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/mark_commenting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Mark Commenting

> Enable mark-based commenting functionality for data points and visualization elements to enhance collaborative analysis.

Curator can allow you to capture input from a user after they select a specific data point on your Dashboard.  Once you
associate a Data Group with a specific field/column from your Dashboard, any time a user clicks on a data-point that
contains that field, a pop-up will display asking the user to input information about that data-point.  This feature
allows you to capture comments on specific data points, projections or estimates, and even the ability to capture
feedback about the data itself.

This functionality requires that Data Manager management is enabled and at least one Data Group has been created.  See
the [Data Manager Basics](/embedding_using_analytics/data_manager/data_manager_basics)
section for more information on how to get things set up if you haven't already.

## Enable Mark-Commenting on a Dashboard

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Tableau** > **Dashboard** section from the left-hand menu.
3. From the list view, find the Dashboard you wish to add Mark Commenting to.
4. On the edit Dashboard page, click the "Mark Commenting" tab.
5. Select the Data Group you have created from the "Data Manager Group" dropdown you would like to display when the user
   clicks on your Dashboard.
6. In the "Mark Details" section, choose as many fields as you'd like from your Dashboard to trigger the
   "Mark Commenting" pop-up.  The logic here is that it must contain *all* fields you have chosen.
7. Click the "Save" button.

**Note:** Make sure the **dimension** name matches the spelling from your Dashboard. Measures or *Measure Names* cannot
be used as a connecting field.

Do you want a step-by-step guide with screenshots? Take a look [here](https://interworks.com/blog/jlyons/2018/10/01/portals-for-tableau-101-inline-commenting-on-dashboards/).

Once you've set up Mark Commenting on your Dashboard, you may want to connect to this data.  See the
[Connecting to Data Manager](/embedding_using_analytics/data_manager/connecting_to_data_manager)
section for more info on how to get started there.
