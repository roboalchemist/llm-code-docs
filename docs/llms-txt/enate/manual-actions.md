# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/manual-actions.md

# Manual Actions

## Overview

'Manual' Actions let users send out manual emails to service recipients.&#x20;

To use 'Manual' Actions, you need to create a 'Manual' Action type and then add the Action into your Case flows.&#x20;

## Creating a Manual Action Type

You can either create a Manual Action type in the Service Line section of Builder, or directly from your Case flow.

### From the Service Lines Page

Creating a Manual Action type from the Service Lines page adds the Action type to your menu of available Actions when you're building flows subsequently in Cases.&#x20;

To do this, in the Service Line page, select which service line you would like to add the Manual Action to and then click on the plus symbol next to the 'Process Search' box. This will bring up a drop down menu where you can select an Action.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FJp1yrAaBkAVm0QNnAgIa%2Fimage.png?alt=media&#x26;token=464c4f7c-7881-40cb-ba4a-ae79e94f5056" alt=""><figcaption></figcaption></figure>

This will open up a new Action for you to create. &#x20;

Add a name and description to your Action and then in the type drop down select 'Manual Action with Peer Review'.&#x20;

Once you are happy with your Action, hit save to create it. This Action can now be added to new and existing business processes by selecting it from the dropdown list when adding a new Action to a Case.

### From a Case Flow

Alternatively you can add a Manual Action type directly from the Case flow itself.

To do this, open a Case flow in edit mode, click on an Action's menu and then instead of clicking to add an existing Action, select to create a new Action by clicking the '+' icon.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FN4hHRy8IINdDAEfq10O6%2Fimage.png?alt=media&#x26;token=9f8477ce-4b5f-4f93-9d90-5b9e0412c7ca" alt=""><figcaption></figcaption></figure>

Give the Action a name, add a description if you wish and for its type, select 'Manual'.

This will add the Manual Action to the Case flow.

## Configuring Manual Actions

You now need to configure the settings for the new Action you have added to your Case. Click on the Action in the flow to highlight it in the info section.

In the Action Info tab, you need to add the usual following information for an Action:

| Setting            | Description                                                                                                                                                                                                       | Notes                                                                                                                                                                                              |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| When is it due?    | Select a value from the dropdown menu of Due Date ‘flavours’                                                                                                                                                      | <p>Mandatory to set live.</p><p>(See <a href="../../shared-standardised-settings-flavours/due-date-flavours">Due Date Flavours Settings</a> for more information).</p>                             |
| Who does it go to? | Select a value from the dropdown menu of Allocation ‘flavours’                                                                                                                                                    | <p>Mandatory to set live.</p><p>(See <a href="../../shared-standardised-settings-flavours/allocation-flavours">Allocation Flavours Settings</a> for more information). </p>                        |
| General Settings   | Select a value from the dropdown menu of Follow Up ‘flavours’                                                                                                                                                     | <p>Mandatory to set live.</p><p>(See <a href="../../shared-standardised-settings-flavours/general-settings-flavours-action-only">General Settings Flavours Settings</a> for more information).</p> |
| Main Card          | You can select a Custom Card to display on the main section of the Action screen.                                                                                                                                 | Optional. See here for more information about [Custom Cards](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration).                                  |
| Side Card          | You can select a Custom Card to display on the side panel of the Action screen.                                                                                                                                   | Optional. See here for more information about [Custom Cards](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration).                                  |
| Manual Creation    | Switching this setting on allows the Action to be started manually in Work Manager.                                                                                                                               | Optional. See [Adding Ad-hoc Actions](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/adding-ad-hoc-actions) section for more information.    |
| Checklist          | Here you can add local checks to the Action that help support 'custom' activities that take place for that specific Action. You can also edit the global checks for the Action type from here too, if it has any. | Optional. See here for more information about [adding checklists](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/checklists-on-actions).     |

Additionally, once a Manual Action has been added to your Case flow, a new 'Email info' tab will display in the info grid.

Here you need to add the following settings that are only relevant for Manual, Send Email and Send Email and Wait Actions.&#x20;

| Setting            | Description                                                        | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------ | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| From Email Address | <p>Enter email address to be used as the from address.<br></p>     | Optional for Manual Actions. Multiple addresses can be set - at runtime users will be presented with a dropdown in the email section to choose a from address. f you set one of the addresses as the Default, this will be populated automatically but users will still be able to select alternatives. Only one email address can be set as the Default.                                                                                                              |
| Email To           | Enter the address to where the email will be sent from the Action. | Optional for Manual Actions. Multiple addresses can be set - at runtime users will be presented with a dropdown in the email section to choose a from address. If you set one of the addresses as the Default, this will be populated automatically but users will still be able to select alternatives. Only one email address can be set as the Default. If no email address is added, the ‘To’ value will be auto-populated as the Primary Contact’s email address. |
| Email CC           | Enter email addresses where the email should be cc’d               | Optional. If no email address is added and there is a CC address on the Action, the ‘CC’ value will be auto-populated as the CC contact’s email address.                                                                                                                                                                                                                                                                                                               |
| Email BCC          | Enter email addresses where the email should be bcc’d              | Optional.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Email Template     | Select the desired Email Template from the dropdown list           | See [Email Template](https://docs.enate.net/enate-help/builder/builder-2021.1/email-template-configuration) section for more information on how to create Email Templates.                                                                                                                                                                                                                                                                                             |
