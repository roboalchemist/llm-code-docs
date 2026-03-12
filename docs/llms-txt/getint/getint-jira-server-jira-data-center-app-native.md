# Source: https://docs.getint.io/getting-started-with-the-platform/deployment-options/getting-started-with-the-platform-deployment-options-getint-for-jira-data-center-jira-server/getint-jira-server-jira-data-center-app-native.md

# Getint Jira Server / Jira Data Center App (native)

**Introduction to Getint.io Native Apps for Jira Server and Jira Data Center**

In December 2022, we proudly launched our first "native" applications for Jira Server and Jira Data Center. Developed using the Atlassian Plugins SDK, these apps integrate seamlessly within your Jira environment, alongside other applications. They are designed to facilitate comprehensive integration and synchronization between Jira and various collaboration software tools such as ServiceNow, Azure DevOps, Asana, Monday.com, GitLab, and more.

## Installation Guide

1. Log in with Administrator credentials and navigate to the **'Manage Apps'** section in your Jira instance.

![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FC5GlNTqq8PQDWOGQkbvZ%2FScreenshot%202022-12-18%20at%2013.35.48.png?alt=media\&token=28797e01-fed3-4faf-9720-eb31b682d5e8)

1. Search for our integration apps, selecting the one that suits your needs (e.g., Azure DevOps Jira integration), and initiate the Free Trial.

![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGLzmKVo5I5mm7hXCPyaB%2FScreenshot%202022-12-18%20at%2013.36.49.png?alt=media\&token=022593c7-6499-416f-850b-78dc3ea1cff9)

1. After installation, access 'Manage Apps' from the left sidebar to ensure a valid license is active for the newly installed app.\
   \
   ![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FKdxXAG4ijA3sKo3bXJlu%2FScreenshot%202023-02-16%20at%2009.38.04.png?alt=media\&token=95d8de57-771c-4438-9ee3-e0ce6bf5d28e)<br>
2. Post-installation, a Getint section will appear on the left vertical menu. Clicking on this link will direct you to the app’s dedicated page, where you can begin creating your integrations.

![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvRM8yOlMabsaINADLXPi%2FScreenshot%202022-12-18%20at%2021.11.37.png?alt=media\&token=1f518a99-3486-4f5a-8022-2368be7d6af8)

You will be navigated to a dedicated page of the app.&#x20;

You can start building your integrations!&#x20;

## Starting the synchronisation

Immediately after installation, the app initiates a scheduled job responsible for executing integrations and performing data cleanups.

**Jira Data Center Consideration:** For instances running on more than one node, a cluster lock ensures Getint operates on a single node at a time.

## App Data and Database

Getint stores configuration details and synced item information within the database. It also generates detailed log files for each sync, aiding in error analysis and support. The app creates several tables for storing data, including configurations, syncs, runs, and error logs.

**Database**

Getint creates the following tables to store configuration details and data related to synchronization processes:

* getint\_connections
* getint\_integrations
* getint\_runs
* getint\_syncs
* getint\_steps
* getint\_artifacts
* getint\_per\_artifacts
* getint\_syncs\_errors
* getint\_tenant\_info

**Log files**

Logs capture valuable details on the actions undertaken to synchronize specific items. The directory for these logs is located at:

* If the JIRA\_HOME directory includes a log directory, a 'getint' directory will be created within it.
* If the JIRA\_HOME directory lacks a log directory, the 'getint' directory will be directly created within the JIRA\_HOME directory.

**Clean up**

Each integration run is meticulously recorded in the database and accompanied by a log file. With numerous integrations potentially executing hundreds of times daily, this can lead to an accumulation of extensive files and database records. Getint.io offers a solution to manage this data efficiently by allowing users to specify a retention period for these records.

To set a data retention limit, follow these three steps:

1. Navigate to the Settings page via the main menu.
2. Enter the desired maximum number of days for data retention.
3. Confirm your settings by clicking 'Save'.

![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fx1BBOZFNr1Fv1znz2zcM%2FScreenshot%202022-12-18%20at%2021.13.55.png?alt=media\&token=b0ddecb2-6703-4ee6-b461-57585137d858)

After defining the retention period, a scheduled cleanup task will automatically run every 8 hours to remove outdated data, ensuring your system remains efficient and clutter-free. Please note, the initiation of the first cleanup might be delayed following the setup.

## Differences in features&#x20;

The native apps for Jira Server/Data Center currently do not support a few features that are available in other versions. These include:

* Bulk Resynchronization
* Advanced Scripting Capabilities
* Preview of Background Job Status
* Notifications

**Integration Interval Configuration**

The integration interval for Server/Data Center apps, as specified in the settings, represents the intended frequency for integration executions. However, the actual scheduling of these integration jobs is managed by Jira's internal logic, which determines when the jobs are permitted to run. Consequently, the practical interval between integration runs may exceed the predefined settings.

![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FOawnU17huSjZOrPAccqy%2FScreenshot%202023-04-03%20at%2022.39.10.png?alt=media\&token=c0c486da-eeca-4b73-ad3e-3e928f40489c)

## Testing Recommendations

It's best practice to conduct testing in a development or local environment rather than directly in a production setting. To facilitate this, you have the option to download Jira and install it on a temporary machine or your personal computer. Alternatively, a dockerized version of Jira is available at <https://hub.docker.com/r/atlassian/jira-software>. For licensing during setup, Timebomb licenses can be utilized, accessible at <https://developer.atlassian.com/platform/marketplace/timebomb-licenses-for-testing-server-apps>, simplifying the entire setup process.

## Uninstall

Upon uninstallation, Getint will halt all scheduled jobs, stopping further synchronizations. However, log files generated during the app's operation will remain intact.

This guide aims to streamline the installation, operation, and management of Getint native apps within your Jira Server or Data Center environment, ensuring a smooth integration process with other collaboration tools.

###
