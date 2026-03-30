# Source: https://docs.curator.interworks.com/site_content_design/menus/tagged_workbooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tagged Workbooks

> Organize and display workbooks in menus using tags to create dynamic, categorized content navigation.

The system can automatically create dashboards for any workbooks that have a matching tag on the associated Tableau Server.
It will poll the Tableau Server every 10 minutes to check for any newly tagged workbooks which match a tag navigational
item (see the [Navigation](/site_content_design/menus/managing_menus) section
for more information). A new Dashboard and corresponding navigation link will be created for each view in any workbooks
it finds.

Links to any new dashboards created through this process will be placed in the same location as the tag navigational item.
However, these links can be safely moved or deleted if desired.

This functionality requires that the REST API is enabled
(see the [Enabling the REST API](/creating_integrations/tableau_connection/creating_a_connection)
section for more information).
