---
id: Zabbix
title: Zabbix
---
For monitoring IT components, like servers, networks, virtual machines and cloud services use Zabbix's open-source monitoring software tool. To integrate Zabbix with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Zabbix integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Zabbix" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the API KEY generated.

## In Zabbix

1. Clone [this Repository](https://github.com/Zenduty/zabbix-zenduty-script.git)

    git clone https://github.com/Zenduty/zabbix-zenduty-script.git

2. Copy the Script file(zabbix_zenduty_integration.sh) and paste it into Zabbix server's AlertScriptsPath. You can see your AlertScriptsPath path from Zabbix server configuration file. Give executable permission to this file for the Zabbix user.

```
chmod 555 zabbix_zenduty_integration.sh
```

![](/img/Integrations/Zabbix/1.png)

**Create the Zenduty media type:**

1. In Zabbix Go to the Administration tab.

![](/img/Integrations/Zabbix/2.png)

1. Under Administration, go to the Media types page and click the Create Media Type button.

![](/img/Integrations/Zabbix/3.png)

1. On the following Media Type configuration page, enter “Zenduty” for Name, Select script in "type" and write the name of the file which you have pasted in AlertScriptPath.

2. Click the Add link in the Script parameters box two times to create two configurable parameters for the script, and enter the following template values for the two parameters in exactly the following order:

  ```
  {ALERT.SENDTO}
  {ALERT.MESSAGE}
  ```
1. Click the Add button at the bottom to save and create the Zenduty media type.

**Create the Zenduty user and user group for alerting:**

1. Go to the Administration tab.

![](/img/Integrations/Zabbix/4.png)

1. Under Administration, go to the Users Groups page and click the Create user group button.

![](/img/Integrations/Zabbix/5.png)

1. Enter a name in the Group name field that identifies it as part of the integration. In this guide, we use “Zenduty Service”.

![](/img/Integrations/Zabbix/6.png)

1. Grant read permissions on Host Groups to the user group, to choose which hosts will produce Zenduty notifications when they have alerts, as follows:

1. Click to the Permissions tab.

1. Select the Read permission level and click on the Select button.

1. Select which Host Groups you would like the Zenduty to have read access to for monitoring, then click the Select button. In this example, we grant the Zenduty group read access to the Linux servers group.

![](/img/Integrations/Zabbix/7.png)

1. Click on Add to save your new user group.

2. Click on the Users tab (under Administration) and click the Create User button.

3. Fill in the details of this new user, and call it “Zenduty User”. The default settings for Zenduty User should suffice as this user will not be logging into Zabbix.

![](/img/Integrations/Zabbix/8.png)

1. Click the Select button next to Groups.

![](/img/Integrations/Zabbix/9.png)

1. Click on the Media tab and, inside of the Media box, click the Add button.

![](/img/Integrations/Zabbix/10.png)

1. Select the type that you have created in step 7, paste the key that you have copied from Zenduty in "Send to".

![](/img/Integrations/Zabbix/11.png)

**Create the alert action:**

1. Go to the Configuration tab.

2. Under Configuration, go to the Actions page, and click on Create Action.

3. Give the action a Name such as Zenduty Notifications.

4. Go to the Operations tab, and configure as follows:

    1. Delete the contents of the Default message field, and insert the following:

    ```
    {"problem":"{TRIGGER.NAME}", "problem_started_at": "{EVENT.TIME} on {EVENT.DATE}", "problem_name": "{TRIGGER.NAME}", "host": "{HOST.NAME}", "severity": "{TRIGGER.SEVERITY}", "original_problem_id": "{TRIGGER.ID}", "event_status":"{EVENT.STATUS}", "host_ip":"{HOST.IP1}", "trigger_description":"{TRIGGER.DESCRIPTION}", "trigger_expression":"{TRIGGER.EXPRESSION}", "trigger_status":"{TRIGGER.STATUS}", "trigger_url":"{TRIGGER.URL}", "trigger_value":"{TRIGGER.VALUE}"}
    ```

    1. Under Operations, click New, and in the resulting operation details configuration, under Send to User groups, click Add. In the pop-up window, check the box by the Zenduty service user group, click Select, and then click Add at the bottom of the Operations section.

![](/img/Integrations/Zabbix/12.png)

1. Go to the Recovery Operations tab and configure the rest of the options in the same way as in steps I-II in the Operations configuration (see above). For instance, the content of the Recovery message should be the same as the Default message.

2. Go to the Acknowledgment Operations tab and configure the rest of the options in the same way as with the Operations and Recovery operations, above.

![](/img/Integrations/Zabbix/13.png)

1. Click the Add button at the bottom of any of the action tabs to save your action.

2. Zabbix is now be integrated with Zenduty.
