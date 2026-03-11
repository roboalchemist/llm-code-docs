---
id: ServiceNow
title: ServiceNow 2-Way
---
ServiceNow is a Platform-as-a-service provider, providing technical management support, such as IT service management, to the IT operations of large corporations, including providing help desk functionality.

To integrate ServiceNow with Zenduty, complete the following steps:

## Prerequisites

* A ServiceNow user that has ITIL role or permissions similar to ITIL role.
* A seperate User for Zenduty is recommended as the Caller for the incident generated in ServiceNow will be taken as the User.

> To create a User follow this : [ServiceNow User Creation](https://docs.servicenow.com/bundle/orlando-platform-administration/page/administer/users-and-groups/task/t_CreateAUser.html)

> To give that User a ITIL role follow this : [ServiceNow Role Assignment](https://docs.servicenow.com/bundle/orlando-platform-administration/page/administer/users-and-groups/task/t_AssignARoleToAUser.html)

## In Zenduty

1. To add a new _ServiceNow_ integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Outgoing Integrations" and then "Add New Outgoing Integration". Give it a name and select the application "_ServiceNow_(Two-Way)" from the dropdown menu.

4. Go to "Configure" under your Outgoing Integrations.

5. There are Several fields to be added here, Starting off with the "_ServiceNow_ Username" and "_ServiceNow_ Password". These are the Username/Password for the Zenduty user that was created for integration(Recommended) or Any user that has the ITIL Role permissions or greater.

6. Then insert the _ServiceNow_ domain, which is obtained from your _ServiceNow_ instance URL.

>For example - https://**acmecorp**.service-now.com/

* Here, the domain to be entered would be "acmecorp".

1. Next, Select the point of origin, of the Incident.

* A 2-Way integration can only have 1 point of origin, either the incident is created in Zenduty and it creates a Incident in _ServiceNow_ Or, A incident is created in _ServiceNow_ and that triggers a Zenduty Incident to be created.
* This can be of your use case on how it should be behave.

![](/img/Integrations/ServiceNow/snow4.png)

1. Next, Incident Response Mapping is needed. Map the appropriate incident status to the loaded statuses that _ServiceNow_ can transition the Incident into.

2. Similarly, Incident mapping is also needed for 2-Way integration between Zenduty and _ServiceNow_. Map the _ServiceNow_ Incident statuses to the Zenduty Incident statuses.

>**Do watch out for _cyclic mapping_ of the incidents.**

![](/img/Integrations/ServiceNow/snow3.png)

1. Update the Changes and copy the generated Code to be added to ServiceNow Business Rules.

## In ServiceNow

1. Log in to your ServiceNow domain with your ServiceNow account.

>Make sure you have permissions to create a _Business rule_.

1. In your Instance, Open "Business rules" under "System Definitions" and click "New"

![](/img/Integrations/ServiceNow/snow5.png)

1. Enter an appropriate Name, Select the "Incident" Table and tick the "Advanced" Tickbox.

2. Under "When to run" tab, Choose "after" from the When dropdown.

3. Also tick the "Insert", "Update" and "Delete" tickboxes.

![](/img/Integrations/ServiceNow/snow1.png)

1. Then, Under the "Advanced" tab, paste the code that was provided in Zenduty and Submit the Business rule.

![](/img/Integrations/ServiceNow/snow2.png)

1. Your ServiceNow 2-Way Integration is now complete.
