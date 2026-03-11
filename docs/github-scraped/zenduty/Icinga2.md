---
id: Icinga2 
title: Icinga2
---

Icinga 2 is an open source monitoring system which checks the availability of your network resources, notifies users of outages and generates performance data for reporting. Scalable and extensible, Icinga 2 can monitor large, complex environments across multiple locations. To integrate Icinga2 with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Icinga2 integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Icinga2" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Icinga2

1. Install the Icinga2 software on your system.

[IMPORTANT] Make sure you have Python2 installed on your system.

1. After this, add an integration to your Zenduty account. This is NOT the integration automatically provided to you.

2. Then download the Zenduty-Icinga2 files by following the steps given below:
 ```
 cd /tmp
 git clone https://github.com/Zenduty/icinga-zenduty-script.git
 cd icinga-zenduty-script
 ```
3. Now open the Zenduty-Icinga2 configuration file and enter the provided integration key into the "pager" field.

4. Now move the files into their respective folders inside "/etc/icinga2/."

5. The Zenduty-Icinga2.conf file must go to the conf.d folder (or the objects.d folder, whichever exists).

 ```
 $ mv zenduty-icinga2.conf /etc/icinga2/conf.d/
 OR
 $ mv zenduty-icinga2.conf /etc/icinga2/objects.d/
 ```
6. The zenduty-webhook-notification.py file must go to the scripts folder.
 ```
 mv zenduty-webhook-notification.py /etc/icinga2/scripts/
 ```
7. Ensure that ‘ICINGAADMINS’ exists as a user group. If not, define it as follows in the users.conf file in conf.d folder.
 ```
 $ object UserGroup "icingaadmins" {
 $ display_name = "Icinga 2 Admin Group"
 }
 ```
8. Now add the custom attribute "enable_zenduty" to your configuration’s host and service configuration objects for all hosts and services you wish to receive alerts from.
 ```
 vars.enable_zenduty = true
 ```

For example:
 
 ```
 object Host "wp1.example.com" {
   import "web-server"
   import "wp-server"
   vars.ssh_port = 2222
   address = "192.168.56.201"

   vars.enable_zenduty = true # Add this line for each host
 }
 
14. If the number of objects is large then you can add the above line to the generic-host and generic-service templates in the templates.conf file in the conf.d folder.

1. Finally you can import this template to your objects.

2. Restarting Icinga2 service:
 ```
 /etc/init.d/icinga2 restart
 ```
3. Icinga2 is now integrated.
