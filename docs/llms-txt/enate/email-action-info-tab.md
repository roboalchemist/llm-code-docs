# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/email-action-info-tab.md

# Send Email Actions

## Overview

Enate allows the automatic sending of emails by the system.

A 'Send Email' Action type that you can add to your Case flows will automatically send out an email and then immediately close the Action and progress on the the next Action without waiting for a response.

If you want to automatically send out an email and wait for a reply to the email before closing and progressing to the next Action, you should instead select a 'Send Email and Wait' Action - see here for more information on that Action type:

{% content-ref url="send-email-and-wait-actions" %}
[send-email-and-wait-actions](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/send-email-and-wait-actions)
{% endcontent-ref %}

For detailed information on how Send Email and Wait Actions work at runtime, see the dedicated Work Manager section:

{% content-ref url="../../../../work-manager/work-manager-2021.1/processing-an-action/send-email-and-wait-actions" %}
[send-email-and-wait-actions](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-an-action/send-email-and-wait-actions)
{% endcontent-ref %}

## Creating a Send Email Action Type

You can either create a Send Email Action type in the Service Line section of Builder, or directly from your Case flow.

### From the Service Lines Page

Creating a Send Email Action type from the Service Lines page adds the Action type to your menu of available Actions when you're building flows subsequently in Cases.&#x20;

To do this, in the Service Line page, select which service line you would like to add the Send Email Action to and then click on the plus symbol next to the 'Process Search' box. This will bring up a drop down menu where you can select an Action.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FJp1yrAaBkAVm0QNnAgIa%2Fimage.png?alt=media&#x26;token=464c4f7c-7881-40cb-ba4a-ae79e94f5056" alt=""><figcaption></figcaption></figure>

This will open up a new Action for you to create. &#x20;

Add a name and description to your Action and then in the type drop down select 'Manual Action with Peer Review'.&#x20;

Once you are happy with your Action, hit save to create it. This Action can now be added to new and existing business processes by selecting it from the dropdown list when adding a new Action to a Case.

### From a Case Flow

Alternatively you can add an Send Email Action type directly from the Case flow itself.

To do this, open a Case flow in edit mode, click on an Action's menu and then instead of clicking to add an existing Action, select to create a new Action by clicking the '+' icon.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FN4hHRy8IINdDAEfq10O6%2Fimage.png?alt=media&#x26;token=9f8477ce-4b5f-4f93-9d90-5b9e0412c7ca" alt=""><figcaption></figcaption></figure>

Give the Action a name, add a description if you wish and for its type, select 'Send Email Action'.

This will add the Send Email Action to the Case flow.

## Configuring Send Email Actions

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

Additionally, once a Send Email Action has been added to your Case flow, a new 'Email info' tab will display in the info grid.

Here you need to add the following settings that are only relevant for Manual, Send Email and Send Email and Wait Actions.&#x20;

| Setting            | Description                                                                                                                                                                                                                                  | Notes                                                                                                                                                                      |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| From Email Address | <p>Enter email address to be used as the from address.<br></p>                                                                                                                                                                               | Mandatory for a Send Email Action. Only one email address can be used.                                                                                                     |
| Email To           | Enter the address to where the email will be sent from the Action.                                                                                                                                                                           | Mandatory for a Send Email Action. Only one email address can be used.                                                                                                     |
| Email CC           | Enter email addresses where the email should be CC’d. If you do not enter a CC address on the Email Info tab, but have entered a CC address on the Case Info tab, at run time the Action will use the CC address from the Case Info tab.     | Optional.                                                                                                                                                                  |
| Email BCC          | Enter email addresses where the email should be BCC’d. If you do not enter a BCC address on the Email Info tab, but have entered a BCC address on the Case Info tab, at run time the Action will use the BCC address from the Case Info tab. | Optional.                                                                                                                                                                  |
| Email Template     | Select the desired Email Template from the dropdown list                                                                                                                                                                                     | See [Email Template](https://docs.enate.net/enate-help/builder/builder-2021.1/email-template-configuration) section for more information on how to create Email Templates. |
