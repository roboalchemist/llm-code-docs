# Source: https://docs.getint.io/support-legal-and-others/faq.md

# FAQ

### Frequently Asked Questions (FAQs) <a href="#frequently-asked-questions-faqs" id="frequently-asked-questions-faqs"></a>

**1. What is the correct syntax for using a field in Java?**

The correct syntax is `${left.issuekey}` or `${left.id}`. You can use the `${left."fieldname"}` format for any field.

**2. How do I map the hierarchy between DevOps and Jira?**

Use the integration plugin to map the hierarchy between DevOps and Jira. Go to the type field mapped and select hierarchy. Enable the option and select the relationship (epic to task, task to subtask, and subtask to task) Ensure to follow the steps for all the types mapped.

**3. How do I sync a ticket from Zendesk to Jira?**

Modify the ticket in Zendesk or create a new one, and wait 3-4 minutes to see if it syncs with Jira. If issues persist, check the configuration and integration settings.

**4. Can I import TFS items into Jira?**

Migration from Azure to Jira is fully supported, ensuring a smooth transition. Additionally, TFS migration is supported for versions 2015 and above, providing enhanced capabilities and features.

**5. How do I integrate Jira and Azure DevOps to have reference IDs between the systems?**

Create custom fields in Jira and Azure DevOps and map them. For example, map Jira native links to custom fields in DevOps and vice versa. Please see our documentation [here](https://docs.getint.io/getintio-platform/workflows/jira-integrations-storing-reference-id-url-of-counterpart) for more details.

**6. How do I trigger the sync of a GitLab issue to Jira using a specific label or field?**

Use the Items Filtering feature to trigger the sync of GitLab issues to Jira based on specific labels or fields.

**7. Should I migrate first and then set up a sync between Jira instances?**

From a configuration perspective, it's a single setup where you decide if it will be used for ongoing integration or migration. Should you migrate first and then sync? It depends on your business case. If you want to move over historical tasks and keep the instances in sync, then yes, create the integration first, migrate the issues, and set up the sync to keep future issues synced between the Jira instances. If you only need to integrate newly created and recently updated tasks, use the default integration mode without triggering the migration.

**8. Is it possible to sync "time tracking" from Jira with "effort" in Azure DevOps?**

Certain fields like "Time Tracking - Remaining Estimate" in Jira are read-only and cannot be set up for sync. A workaround is to create custom fields and map them instead.

**9. How can I automatically create labels in Jira Work Management based on fields from Monday.com?**

The integration of Jira Monday does not support the automatic creation of labels directly. However, you can map fields from Monday.com to custom fields in Jira and use automation to assign values accordingly.

**10. What should I do if I encounter an "invalid Jira License" error during sync?**

This error frequently occurs when the trial ends or your license expires. Please ensure that you have the correct license, extend the trial through Atlassian and our support, or obtain a dedicated license key.

**11. How do I sync the “Original Estimate” field?**

To synchronize the "original estimate" field, you need to set up the mapping in the integration settings. Go to the integration, search for "mapped," and choose the original estimate field from the fields section. After mapping, the integration will synchronize the field if it is supported by the app you are integrating with.

**12. How to set a default assignee/reporter if the value is empty or unknown?**

Go to the integration and select the type mapping field (task, subtask). Choose the assignee/reporter and create a custom value for the reporter of the tickets.

**13. How do I map Asana tasks to the correct Jira issue type (bugs, stories, tasks)?**

Map Asana issues to the appropriate Jira issue type by configuring the issue type mappings in the integration settings.

**14. How do I migrate all information from** [**Monday.com**](http://monday.com/) **to Jira?**

Please remember the following instructions:

To create a new integration, choose "Migration." Then, select "Migrate data" from the menu on the left side of the screen and set it up. The Migration guide can assist you in setting up and migrating your data properly. After the migration is complete, the tasks will automatically appear in Jira.

**15. Can we customize the format for the author and timestamp added to comments during synchronization?**

It is not possible to customize the format for the author and timestamp in the comments. The author will always be the account set up for the creation of the customization. Please see more under [Service Account](https://docs.getint.io/guides/quickstart/connection#role-of-the-service-account).

**16. How do I select a board in Azure DevOps using a query language for integration with Jira?**

Ensure your query syntax is correct. For example, use `[System.AreaPath] In "Social Analytics"`. Verify the correct syntax and test it directly in Azure DevOps if it does not work in the plugin.

**17. How do I map linked issues from Azure DevOps into Jira for dependencies and hierarchy?**

Follow the guide on [syncing dependencies](https://docs.getint.io/guides/integration-synchronization/jira-azure-devops-integration/syncing-dependencies-between-jira-and-azure-devops-using-getint)and hierarchy between Jira and Azure DevOps provided in the documentation.

**18. Can I buy one license for different kinds of integrations?**

To accommodate different kinds of integrations, you will need to obtain more than one license. However, you can also benefit from a network of flexible licenses that cater to various integration needs, providing a comprehensive and adaptable solution. Please check more information [here](https://docs.getint.io/billing-and-services/licensing#jira-related-integrations) or contact our support for assistance.

**19. Is there a way to remove unwanted tags during the load process into Jira?**

There is no built-in feature to remove unwanted tags during the load process into Jira. However, you can remove the hyperlink to minimize the issue. Further improvements are being investigated.

**20. What should I do if I encounter an error when selecting a project after selecting the connection?**

Try debugging the connection or recreating the connection. Go to Workflows -> Connections, and use the debug resists option to check the connection. If the issue persists, delete and recreate the connection.

**21. What does the warning "\[WARN ] 2023-08-16T18:29:22.731Z - \[zd210c2cb-347-6679-3] Failed to transform '${left.id}' to real value" mean?**

This warning indicates that the integration could not transform the `${left.id}` placeholder into an actual value. Ensure that the field mappings are correctly configured and that the `${left.id}` field exists and has a valid value in the source system.

**22. Why did my integration stop working, showing an error "Failed to fetch flow triggers: Invalid response status code received (expected: 200 but got 503)"?**

This error suggests that the API was temporarily unavailable. Check the Application status page for any outages or scheduled maintenance. If the issue persists, try reconnecting the integration after some time.

**23. How to resolve the error "Failed to fetch flow triggers: Invalid response status code received (expected: 200 but got 400)" in Jira-Jira integration?**

This error indicates that the specified field value does not exist in the Jira project. Verify that the field value exists in the project's field configuration and mapping settings.

**24. Does the post update work both ways in Jira and Asana integration?**

Post updates should work both ways if correctly configured. If only Jira updates are reflected and not Asana updates, check the integration logs and ensure that Asana update actions are configured and enabled.

**25. How do I understand and use relationship mapping, specifically Dependencies, and Hierarchy, in Azure to the Jira CI tool?**

Dependencies refer to relationships such as "blocked by" or "relates to," while Hierarchy refers to Parent/Child relationships like subtasks. Ensure these mappings are correctly configured in the integration settings.

**26. Is it possible to have links to synced items or vice versa using Dependencies?**

Yes, you can use Dependencies to link synced items. Configure the dependencies mapping in the integration settings to reflect these links.

**27. What to write in the "Items that should be migrated" field during Asana to Jira migration?**

Specify the ID of the items to be migrated if not all items are required. Ensure that the date range or criteria specified includes the items you wish to migrate.28. Can I migrate Asana hierarchy levels more than 2 levels deep, such as Task->Subtask->Subtask of Subtask?

Currently, only the first level of hierarchy (Task->Subtask) can be mapped. Subtask of a subtask is not supported for migration.

**29. How to prevent tasks created in Asana from syncing to Jira while allowing Jira tasks to sync to Asana?**

In the integration settings, under the "Advanced" option, disable the trigger for task creation from Asana to Jira. Ensure that only Jira tasks trigger sync to Asana.

**30. How can I prepend/postpone custom text to issue/task titles during synchronization from Jira to Asana?**

Use the Advanced (Scripting) section in the workflow settings to customize the issue/task titles. Log the state objects to the sync run file to inspect and modify them as needed. Contact support for further assistance if issues arise.

**31. How to link the start date (issue opened) between Jira and GitHub?**

Ensure that both fields are mapped correctly in the integration settings. Check the field configurations in both systems to ensure they are compatible and correctly set up for synchronization.

**32. Why is my status field in Notion not syncing back to Getint for mapping with Jira?**

Ensure the integration is properly set up, and follow the [Jira Notion integration](https://docs.getint.io/guides/integration-synchronization/jira-notion-integration) guide for a proper setup. Consider refreshing the connection or re-integrating the status field. If the issue persists, contact support.

**33. Why am I receiving 503 service unavailable errors in the logs for GIS Tasking sync?**

The 503 error indicates a temporary issue with the server. Check the status of the services being integrated. If the problem persists, it might be due to service outages or server issues. Contact our support for further assistance.

**34. Why can't I map the Priority fields and attachments between Jira and ClickUp?**

Ensure that these fields are correctly configured and visible in both systems. If they are not showing up, it might be an issue with field visibility or permissions.

**35. Receiving error 504: Server timed out with your request in Asana-Jira integration.**

This error suggests the server timed out due to a large request. Try paginating your requests or reducing the scope of the request. Refer to the API documentation for handling such errors.

**36. Why is the app not showing all fields from ClickUp in Jira integration?**

Ensure that all fields in ClickUp are correctly configured, visible, and supported. Sometimes, not all fields are fetched automatically. Verify the field settings and refresh the integration settings. Refer to the [integration documentation](https://docs.getint.io/guides/integration-synchronization/jira-clickup-integration) for detailed steps.

**37. Is data at rest fully encrypted in the Integration?**

Ensure that the platform meets the Atlassian marketplace requirements for full disk encryption at rest. Contact our support for detailed information on data encryption policies and compliance with Atlassian standards.

**38. Why is the app not loading in Jira after creating a new Monday to Jira integration?**

The issue might be related to a new version release of the app. Refresh the page, try accessing from different accounts, or wait for a while and try again. If the problem persists, open a [support ticket](https://getintio.atlassian.net/servicedesk/customer/portals) for further assistance.

**39. Why am I getting a 401 error when setting up a connection to Azure DevOps after upgrading to a paid plan?**

A 401 error indicates a connection issue. Please ensure that the URL to DevOps is correct. Remove any unnecessary segments from the URL, and then retry the connection. If the problem persists, verify the connection settings and credentials.

**40. How to resolve field mapping errors when syncing Jira with Freshservice?**

Ensure that the status field is not mapped in both the main and status tabs, and remove redundant mappings to avoid conflicts. Test the integration by running a few test syncs to ensure all required fields are correctly mapped. Check the logs and error retrieval, and contact our support for assistance if the issue persists.

**41. Do you support moving synced Azure DevOps work items between projects?**

Getint supports moving synced Azure DevOps work items between projects. Ensure that the integration settings allow for such movements and that the target projects are properly configured.

**42. How to resolve the error `{"errorMessages":[],"errors":{"issuelinks":"Field does not support update 'issuelinks'"}}`?**

This error indicates that the issue links field does not support updates, as it is a read-only field. Check if the field is properly mapped to a text field (customer text field) and ensure that it is not locked in the project settings.

**43. How to limit comment sync to only public comments between Jira and Wrike?**

It is possible to configure the comments by selecting the integration and selecting the “Comments & Attachments” tab in your type mapping. Then check the box to make all comments public.

**44. Why are some Zendesk tickets not synchronized with Jira when created?**

Please make sure to review the integration logs for any errors or issues and fix any problems with the integration. Double-check that all the required fields are mapped correctly and that there are no conflicts or filter limitations. Follow the Jira Zendesk guide for the proper setup of the integration.

**45. Why are images not being synced in comments?**

Currently, only Jira - Azure DevOps integration supports inline image sync. If you're experiencing this issue, please ensure to check the file size and the configuration under comments in the type mapping. Enable the inline images and attempt the process again. If the problem continues, please reach out to our support team for assistance.

**46. How to test the integration and connect Freshdesk to Jira, ensuring multiple Freshdesk issues can be associated with one Jira ticket?**

Follow the integration guide steps to set up Freshdesk and Jira integration. Ensure the mapping settings link to a Jira ticket and test by creating tickets to verify the sync.

**47. How to resolve the error "Invalid response status code received (expected: 200 but got 401)" in Jira and Azure DevOps integration?**

This error indicates an authentication problem. Please ensure that the credentials and API tokens used for the integration are correct and have the necessary permissions. Double-check the connection settings and try again.

**48. Why am I getting the error "Cannot read property 'issuetypes' from undefined" when creating a Jira ticket from ServiceNow?**

This error occurs when the integration cannot find the `issuetypes` property. Ensure that integration is properly configured and that the `issuetypes` field exists and is accessible in Jira. Follow the[Jira ServiceNow integration](https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration)guides to ensure seamless integration.

**49. How to continuously sync Jira tickets that are manually created in Jira with Freshdesk, ensuring specific fields are updated?**

Follow the guide [Jira Freshdesk](https://docs.getint.io/guides/integration-synchronization/jira-freshdesk) and ensure the sync is set up for continuous updates. You can also use the integration's filter settings to define criteria for [syncing specific fields](https://docs.getint.io/getintio-platform/workflows/filtering-items-for-integration-in-getint).

**50. What to do if new tickets created in Jira are not syncing with another Jira instance?**

Check the integration [guide](https://docs.getint.io/guides/integration-synchronization/jira-jira-integration) to ensure that the sync is configured correctly. Verify that the mandatory fields are mapped and that there are no errors in the sync process. Ensure that both Jira instances are accessible and properly connected. If the problem persists, please reach out to our support.

**51. How to set the reporter in Jira to be the same as the reporter during integration?**

Ensure that the reporter field is correctly mapped in the integration settings. The reporter in Jira is often set to the integration owner's account by default. Adjust the field mappings to use the reporter information from the app that you are trying to integrate.

**52. How to resolve the error "Invalid Jira license: JSONObject text must begin with '{' at 1 \[character 2 line 1]" when syncing Jira and DevOps?**

This error indicates a problem with the Jira license or the integration setup. Please ensure that your Jira license is active and correctly configured and that it is the correct license for your integration. If the issue persists, contact support.

**53. What to do if I encounter a permissions error while setting up an integration?**

Ensure that the token permissions are correctly configured for the integration. Follow the [Connection guides](https://docs.getint.io/guides/quickstart/connection) on setting up connections and token permissions.

**54. How to sync task statuses without performing a "hard sync" every time in Jira and Azure DevOps integration?**

Regular synchronization should work without requiring a hard sync. Check the integration settings to ensure that the status fields are correctly mapped and that the sync is enabled.

**55. Why is my HubSpot task not syncing with Jira?**

Check the integration logs and review any errors that might be appearing. Fix the integration and ensure that the field mappings are correct and that the necessary permissions are set. Contact support if the problem persists.

**56. Why is my Jira-Jira integration not updated, showing a trial or subscription error?**

Verify that the subscription is active and that the app is installed on both Jira instances. Ensure that billing is handled correctly for both instances. Review our "[Start Trial](https://docs.getint.io/getting-started-with-the-platform/starting-the-free-trial-and-accessing-the-getint-app)" guide.

**57. How to map Jira Service Management status and organization fields to text fields in another Jira instance?**

Mapping these fields to text fields can be done by selecting them in the fields mapping tab and matching them. Make sure that the fields are properly configured and that the mapping is set up correctly. If you cannot see the fields or encounter any errors, please reach out to our support team.

**58. How to resolve the error "TenantCreationFailed" when initializing ClickUp/Jira integration?**

This error may occur during app updates. Try refreshing the page or wait for the update to complete. If the issue persists, [open a support ticket](https://getintio.atlassian.net/servicedesk/customer/portals) for further assistance.

**61. Can Getint integrate two different Asana spaces?**

Yes, the app can integrate two different Asana spaces. Make sure that both spaces are properly configured and that you have the correct license.

**62. How to automatically create a card in Jira after updating a Trello card?**

Once Trello and Jira are correctly connected, create a mapping between Trello cards and Jira tasks. This will automatically replicate updates from Trello to Jira. For old cards, use the migration option or update the cards to sync them.

**63. What does the error "Expecting comparison operator" mean in Azure DevOps and Jira integration?**

This error typically indicates a problem with the query or filter settings in Azure DevOps. Please ensure that the query syntax is accurate and that all mandatory fields are properly configured.

**64. Why are comments not syncing from Azure DevOps to Jira and showing a 302 error?**

This error might occur if the Jira Cloud URL has recently been changed. Please verify the URL and update it if necessary. If the issue persists, [open a support ticket](https://getintio.atlassian.net/servicedesk/customer/portals) for further assistance.

**65. How to handle pictures from Azure DevOps to Jira that appear in the attachment section but not in the comments?**

Ensure that the integration settings are enabled for images to be included in comments and that the file size does not exceed the limit permitted on both applications. If issues persist, create a support ticket for further investigation.

**66. How to resolve "Invalid response status code received (expected: 201 but got 400)"?**

The error suggests a missing required field, such as the summary field in Jira. Ensure all required fields are correctly mapped and filled.
