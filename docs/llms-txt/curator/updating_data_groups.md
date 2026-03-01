# Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/updating_data_groups.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Updating Data Groups

> Modify existing Data Groups to add new fields and information requirements while preserving previously collected data.

If you have been using your Data Group and frontend users have input information diligently, you might find out that you
need extra pieces of information on top of what you are gathering to drive your analysis.

No problem, we have you covered by allowing you to simply add or remove the fields as required. Just follow these steps:

## Adding new Data Manager Attribute

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to **Settings > Data Manager > Data Group** section from the left-hand menu.
3. Click on the Data Group you want to alter.
4. Check more attributes (aka form fields) as required.
5. Click Save
6. Click on **Regenerate Summary Table** to reflect the changes in the respective database table.

Existing data entries will have an empty value in the newly added column.

## Remove an existing Data Manager Attribute

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to **Settings > Data Manager > Data Group** section from the left-hand menu.
3. Click on the Data Group you want to alter.
4. Uncheck attributes (aka form fields) as required.
5. Check **Permanently delete attribute data from items when unlinking from group?** underneath the Attributes selection
   section.
6. Check **Confirm permanently deleting attribute data from items** if you are sure you want to delete the attribute
   from your table.
7. Click Save
8. Click on **Regenerate Summary Table** to reflect the changes in the respective database table.

Existing data in the removed attributes will be lost after this process!
