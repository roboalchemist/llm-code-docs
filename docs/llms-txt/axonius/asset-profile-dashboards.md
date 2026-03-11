# Source: https://docs.axonius.com/docs/asset-profile-dashboards.md

# Asset Profile Dashboards

You can create a dashboard for each asset. Dashboards related to each asset type are displayed and they display charts related to a specific asset as a visual overview for that asset.

On the **Asset Profile** click the **Dashboards** tab on top of the page to see the available dashboards. There, you can display dashboards related to that asset type. The charts are displayed for the asset type and for any other related asset. All the asset profiles on that asset type have the same dashboard. The capabilities provided are similar to other dashboards, but the display for each asset profile dashboard is automatically filtered by the asset selected (asset ID).

<Callout icon="📘" theme="info">
  Note

  Add or edit dashboard permissions are required to add, duplicate, or edit a dashboard.
</Callout>

<Image alt="AssetProfileDashboard1" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetProfileDashboard1.png" />

The left pane displays the name of the dashboard.

The following options are available:

### Creating a New Dashboard

Click on the 3-dot Add Dashboard menu next to Dashboard Overview and select **Add Dashboard**.

The Create Dashboard dialog opens

<Image alt="CreateDashboardAssetProfile2" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateDashboardAssetProfile2.png" />

The dashboards are created in the same way as on the Axonius Dashboards. The relevant admin chooses who can edit the asset profile’s dashboard. For more information, refer to [Creating a New dashboard](/docs/working-with-dashboard-spaces#creating-a-new-dashboard)

### Dashboard Menu Actions

You can click the 3-dot  'More Dashboard Menu' either on the top left of the page, or on a specific dashboard to perform various actions about the name, permissions of a dashboard, and more.

<Image alt="MoreDashboard%20Actions" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MoreDashboard%20Actions.png" />

The following actions are available for users with the necessary permissions:

* [**Edit the dashboard**]() - Note that when you edit a dashboard, the changes you make apply to all dashboards on that asset. If you edit a dashboard for a specific asset profile - it changes for all assets for that profile.
* [**Delete the dashboard**](/docs/working-with-dashboard-spaces#deleting-dashboards)
* **[Duplicate Dashboard](/docs/working-with-dashboard-spaces#duplicating-a-dashboard)**
* **[Refresh Dashboard](/docs/working-with-dashboard-spaces#refreshing-dashboard-data)**

Note that exporting dashboards is not supported.

## Adding Charts to the Dashboard

Once you create a dashboard, you can add charts to it. You can create any of the charts that are available for regular Axonius dashboards (refer to [Working with Custom Charts](/docs/working-with-custom-panels)), however, the modules available are only those related to the asset profile on which you are creating the chart.

<Callout icon="📘" theme="info">
  Note

  Although you edit the dashboard while viewing a specific asset, changes are global. Any charts you add, edit, or delete will appear on the dashboard for all assets of this type.
</Callout>

### Relationship Selection in Asset Profile Charts

Asset Profile dashboards allow you to build charts that enrich a specific asset (e.g., a Device) with connected data from other asset types, such as Users, Security Findings, or Applications. This feature lets you visualize cross-asset connections directly on a profile.

When configuring charts that support multiple queries (such as the Query Comparison chart), you can specify the relationship for each query. This ensures the query returns only those assets connected to the profiled asset via that specific relationship type.

<Image align="center" alt="AssetProfileChartRelationships.png" border={false} width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/asset_profile/AssetProfileChartRelationships.png" />

**To select a relationship when creating a chart:**

1. Select the target Asset Type. For example, on a Device profile, select Users to include user data related to that device.
2. Select a Query. The system automatically applies the default relationship for the selected asset type.
3. Refine the Relationship. If you need a specific connection type (rather than the default), select the desired relationship from the dropdown menu.
4. Complete Configuration. Continue configuring the rest of your chart settings.

The chart will now filter data based on the selected relationship, ensuring the displayed metrics are strictly relevant to the profiled asset.

### Chart Actions

Chart actions are available for each chart. Refer to [Chart Actions](/docs/chart-actions)

### Filtering Charts

Click the filter on a chart to update it dynamically. This works in a similar way to [Chart filters for Dashboard Charts](chttps://docs.axonius.com/docs/update-chart-dynamically)

### Filtering Dashboards

You can filter a dashboard. Note that dashboards are prefiltered by the Asset unique ID, and this value cannot be changed. Add additional filters as required. When you create a filter for an Asset Profile dashboard while focused on a specific asset, it only affects the asset you are currently viewing.

**Filter by asset entity** - filters by a row in the table that is by an adapter connection

<br />