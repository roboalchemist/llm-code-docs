# Source: https://docs.curator.interworks.com/embedding_using_analytics/power_bi_reports/adding_a_power_bi_report.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding a Power BI Report

> Add and configure Power BI reports in Curator for seamless access via embedding.

export const BackendNavPath = ({levelOne, levelTwo, levelThree, tab, section}) => {
  const levels = [levelOne, levelTwo, levelThree].filter(Boolean);
  const lastLevel = levels.length ? levels[levels.length - 1] : '';
  return <span>
      In the <a href="/setup/installation/linux_installation">backend of Curator</a> using the left-hand navigation,
      navigate to the
      {levelOne && <strong>{" " + levelOne}</strong>}
      {levelOne && levelTwo && " > "}
      {levelTwo && <strong>{levelTwo}</strong>}
      {levelTwo && levelThree && " > "}
      {levelThree && <strong>{levelThree}</strong>} page.
      {(tab || section) && <>
          {" "}On the {lastLevel} page
          {tab && <> click the <strong>{tab}</strong> tab</>}
          {tab && section && " and"}
          {section && <> expand the <strong>{section}</strong> section</>}.
        </>}
    </span>;
};

Curator enables you to embed Power BI reports as a seamless part of your portal, providing your users with a unified
analytics experience, streamlining access to critical insights.

## Prerequisites

Before adding Power BI reports to Curator, ensure you have
[established your Power BI connection](/creating_integrations/power_bi_connection/curator_connection) and have reports
published to a Power BI workspace.

## Creating a Power BI Report in Curator

To add a new Power BI report to your Curator portal follow the steps below:

### Navigate to Power BI Reports

1. <BackendNavPath levelOne="Power BI" levelTwo="Reports" />
2. Click the **New Report** button
   <Frame>
     <img className="rounded-xl" src="https://mintcdn.com/interworks/g2o1CqLP2qwX5o12/assets/images/embedding_using_analytics/power_bi_reports/pbi_report_new_report_empty_list_page.png?fit=max&auto=format&n=g2o1CqLP2qwX5o12&q=85&s=2afa52b381f27109792bfe5ade13b7e0" alt="Add new Power BI report from list page" data-og-width="4320" width="4320" data-og-height="2688" height="2688" data-path="assets/images/embedding_using_analytics/power_bi_reports/pbi_report_new_report_empty_list_page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/g2o1CqLP2qwX5o12/assets/images/embedding_using_analytics/power_bi_reports/pbi_report_new_report_empty_list_page.png?w=280&fit=max&auto=format&n=g2o1CqLP2qwX5o12&q=85&s=23821b721fc28ca645af45331ec6bcbc 280w, https://mintcdn.com/interworks/g2o1CqLP2qwX5o12/assets/images/embedding_using_analytics/power_bi_reports/pbi_report_new_report_empty_list_page.png?w=560&fit=max&auto=format&n=g2o1CqLP2qwX5o12&q=85&s=4acd0e476aa3ba074fcaaee2392a18bb 560w, https://mintcdn.com/interworks/g2o1CqLP2qwX5o12/assets/images/embedding_using_analytics/power_bi_reports/pbi_report_new_report_empty_list_page.png?w=840&fit=max&auto=format&n=g2o1CqLP2qwX5o12&q=85&s=93bbeba396ac45d3bc96ac6d095e476e 840w, https://mintcdn.com/interworks/g2o1CqLP2qwX5o12/assets/images/embedding_using_analytics/power_bi_reports/pbi_report_new_report_empty_list_page.png?w=1100&fit=max&auto=format&n=g2o1CqLP2qwX5o12&q=85&s=5dce89202c32413487e745fb4b99ae5b 1100w, https://mintcdn.com/interworks/g2o1CqLP2qwX5o12/assets/images/embedding_using_analytics/power_bi_reports/pbi_report_new_report_empty_list_page.png?w=1650&fit=max&auto=format&n=g2o1CqLP2qwX5o12&q=85&s=8c5ad7582dc0b2d69f2656ea12fab741 1650w, https://mintcdn.com/interworks/g2o1CqLP2qwX5o12/assets/images/embedding_using_analytics/power_bi_reports/pbi_report_new_report_empty_list_page.png?w=2500&fit=max&auto=format&n=g2o1CqLP2qwX5o12&q=85&s=31d607dbc6348650d958679426fd5a9f 2500w" />
   </Frame>
3. Fill out the details in the **Create Power BI Report** form:

   <Frame>
     <img className="rounded-xl" src="https://mintcdn.com/interworks/g2o1CqLP2qwX5o12/assets/images/embedding_using_analytics/power_bi_reports/pbi_create_new_report_edit_report_page.png?fit=max&auto=format&n=g2o1CqLP2qwX5o12&q=85&s=4e31984c27f6b002260ef81020e05504" alt="Create new Power BI report" data-og-width="4320" width="4320" data-og-height="2688" height="2688" data-path="assets/images/embedding_using_analytics/power_bi_reports/pbi_create_new_report_edit_report_page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/g2o1CqLP2qwX5o12/assets/images/embedding_using_analytics/power_bi_reports/pbi_create_new_report_edit_report_page.png?w=280&fit=max&auto=format&n=g2o1CqLP2qwX5o12&q=85&s=261e53d2e0cf94f657375a34f702914a 280w, https://mintcdn.com/interworks/g2o1CqLP2qwX5o12/assets/images/embedding_using_analytics/power_bi_reports/pbi_create_new_report_edit_report_page.png?w=560&fit=max&auto=format&n=g2o1CqLP2qwX5o12&q=85&s=aa627d1508b63e9b7e6dfe8acab87b36 560w, https://mintcdn.com/interworks/g2o1CqLP2qwX5o12/assets/images/embedding_using_analytics/power_bi_reports/pbi_create_new_report_edit_report_page.png?w=840&fit=max&auto=format&n=g2o1CqLP2qwX5o12&q=85&s=118b94b101f15546eeb7f41a461db2ba 840w, https://mintcdn.com/interworks/g2o1CqLP2qwX5o12/assets/images/embedding_using_analytics/power_bi_reports/pbi_create_new_report_edit_report_page.png?w=1100&fit=max&auto=format&n=g2o1CqLP2qwX5o12&q=85&s=369e13224a2fe05ef7b613f6aa5a4d67 1100w, https://mintcdn.com/interworks/g2o1CqLP2qwX5o12/assets/images/embedding_using_analytics/power_bi_reports/pbi_create_new_report_edit_report_page.png?w=1650&fit=max&auto=format&n=g2o1CqLP2qwX5o12&q=85&s=c7b76a045891a1f9652658f02640ee06 1650w, https://mintcdn.com/interworks/g2o1CqLP2qwX5o12/assets/images/embedding_using_analytics/power_bi_reports/pbi_create_new_report_edit_report_page.png?w=2500&fit=max&auto=format&n=g2o1CqLP2qwX5o12&q=85&s=a75cf55444eaf6d0c4647b49e7549a33 2500w" />
   </Frame>

   * **Workspace**: Select the Power BI workspace containing the report.
   * **Report**: Select the specific report to embed.
   * **Title**: This appears in navigation menus and page titles - can be different from the Power BI report name.

The display options will allow you to control the appearance of the toolbar, the persistence of filters, the appearance
of the filter pane as well as the Power BI report Page Navigation.

Optionally, explore the Discovery and Display tabs to further customize how the report appears and is found by users
or linked to other content across your site.

Be sure to save your report before navigating away from the page.

## Adding Reports to Navigation

After creating a report, [add it to your site's menu](/site_content_design/menus/menu_items) for easy access and
automated authorization.

## Adding Reports to Pages

Once a Power BI Report has been added to Curator it can also be added to pages for a more dynamic layout.  Embed Power
BI reports in custom pages [using the Page Builder](/site_content_design/pages/power_bi_report).

## Security Considerations

Curator utilizes the permissions set within your Power BI tenant including both workspace-level permissions as well as
direct-access permissions.

### Workspace-Level Access

When a user has access to a workspace, they automatically have access to all reports within that workspace.
Curator checks workspace access to determine report visibility.  Due to performance concerns we strongly recommend
utilizing workspace-level access whenever possible.

### Direct Report Access

If a user does not have access to a workspace, Curator will check for direct access permissions to individual reports. This
allows for more granular control over report access but can lead to performance issues due to limitations in the Power
BI APIs.
