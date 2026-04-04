---
id: SplunkLegacy
title: Splunk Legacy
---
Use legacy mode to temporarily work around issues introduced by the new integration of the user interface with the main splunkd service. To integrate Splunk Legacy with Zenduty, complete the following steps:

## On the Zenduty Dashboard

1. To add a new Splunk Legacy integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.
2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.
3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Splunk (Legacy)" from the dropdown menu.
4. Go to "Configure" under your integrations and copy the API KEY generated.

## In Splunk

5. Go to "$SPLUNK_HOME/bin/" and open "setSplunkEnv" file and create one variable "$ZENDUTY_KEY" and the value of this variable will be API KEY that you have copied earlier. So it will look like

 ```export $ZENDUTY_KEY= < API KEY >```.

2. Clone [this](https://github.com/Zenduty/splunk_legacy_scripts.git) Repository:

https://github.com/Zenduty/splunk_legacy_scripts.git

1. Copy the Python Script file and paste it into "$SPLUNK_HOME/bin/scripts".

2. Sign In to Splunk. In the "Search and Report" app, search for the monitor metrics for Zenduty incidents to report on.

![](/img/Integrations/SplunkLegacy/1.png)

1. Save this as an "Alert" from the "Save As" window in the top right corner.

2. Fill in the form and Click the "Add Actions" button under "Trigger Actions", select "Run a script" and write the name of the file which you have pasted in "$SPLUNK_HOME/bin/scripts" and save this Alert.

![](/img/Integrations/SplunkLegacy/2.png)

![](/img/Integrations/SplunkLegacy/3.png)

1. Splunk Legacy is now integrated.
