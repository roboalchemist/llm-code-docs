# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/hold-case-action-info-tab.md

# Wait for Sub-Cases to Complete Actions

## Overview

A ‘Wait for Sub-Cases to Complete’ Action (also known as a Hold Case Action) will wait for a specific Sub-Case to reach completion before allowing the Case to move on to the next Action.

For detailed information on how ABBYY Actions work at runtime, see the dedicated Work Manager section:

{% content-ref url="../../../../work-manager/work-manager-2021.1/processing-an-action/wait-for-sub-case-actions" %}
[wait-for-sub-case-actions](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-an-action/wait-for-sub-case-actions)
{% endcontent-ref %}

## Creating a Wait for Sub-Cases to Complete Action Type

You can either create a Wait for Sub-Cases to Complete Action type in the Service Line section of Builder, or directly from your Case flow.

### From the Service Lines Page

Creating a Wait for Sub-Cases to Complete Action type from the Service Lines page adds the Action type to your menu of available Actions when you're building flows subsequently in Cases.

To do this, in the Service Line page, select which service line you would like to add the Wait for Sub-Cases to Complete Action to and then click on the plus symbol next to the 'process Search' box and then select 'Action'.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FE6aT3P3B85ELRemyAQki%2Fimage.png?alt=media&#x26;token=32e56432-375b-45c7-b49e-f7e782fae874" alt=""><figcaption></figcaption></figure>

This will open up a new Action for you to create.

Add a name and description to your Action and then in the ‘type’ drop down select 'Wait for Sub-Cases to Complete'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FIJrY7MLuSKNklgtWJuzz%2Fimage.png?alt=media&#x26;token=e6c75def-fbcc-4be3-b72f-e5deb770fecb" alt=""><figcaption></figcaption></figure>

You can then choose to add a global checklist to the Action. This contains a standard checklist of activities that will be added any time this Action type is added to a Case flow. See here for more information on [checklists](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/checklists-on-actions).

Once you are happy with your Action, hit save to create it. This Action can now be added to new and existing business processes by selecting it from the dropdown list when adding a new Action to a Case.

### From a Case Flow

Alternatively, you can add a Wait for Sub-Cases to Complete Action type directly from the Case flow itself.

To do this, open a Case flow in edit mode, click on an Action's menu and then instead of clicking to add an existing Action, select to create a new Action by clicking the '+' icon.

Give the Action a name, add a description if you wish and for its ‘type’, select 'Wait for Sub-Cases to Complete'. This will add the Wait for Sub-Cases to Complete Action to the Case flow.

## Configuring Wait for Sub-Cases to Complete Actions

You now need to configure the settings for the new Action you have added to your Case. Click on the Action in the flow to highlight it in the info section.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FsIwbG1Of91MkxM4VQEky%2Fimage.png?alt=media&#x26;token=111075b8-5e21-4e57-92bb-3096ce7ef487" alt=""><figcaption></figcaption></figure>

In the Action Info tab, you need to add the usual following information for an Action:

| Setting            | Description                                                                                                                                                                                                       | Notes                                                                                                                                                                                              |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| When is it due?    | Select a value from the dropdown menu of Due Date ‘flavours’                                                                                                                                                      | <p>Mandatory to set live.</p><p>(See <a href="../../shared-standardised-settings-flavours/due-date-flavours">Due Date Flavours Settings</a> for more information).</p>                             |
| Who does it go to? | Select a value from the dropdown menu of Allocation ‘flavours’                                                                                                                                                    | <p>Mandatory to set live.</p><p>(See <a href="../../shared-standardised-settings-flavours/allocation-flavours">Allocation Flavours Settings</a> for more information).</p>                         |
| General Settings   | Select a value from the dropdown menu of Follow Up ‘flavours’                                                                                                                                                     | <p>Mandatory to set live.</p><p>(See <a href="../../shared-standardised-settings-flavours/general-settings-flavours-action-only">General Settings Flavours Settings</a> for more information).</p> |
| Main Card          | You can select a Custom Card to display on the main section of the Action screen.                                                                                                                                 | Optional. See here for more information about [Custom Cards](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration).                                  |
| Side Card          | You can select a Custom Card to display on the side panel of the Action screen.                                                                                                                                   | Optional. See here for more information about [Custom Cards](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration).                                  |
| Manual Creation    | Switching this setting on allows the Action to be started manually in Work Manager.                                                                                                                               | Optional. See [Adding Ad-hoc Actions](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/adding-ad-hoc-actions) section for more information.    |
| Checklist          | Here you can add local checks to the Action that help support 'custom' activities that take place for that specific Action. You can also edit the global checks for the Action type from here too, if it has any. | Optional. See here for more information about [adding checklists](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/checklists-on-actions).     |

Additionally, once a 'Wait for Sub-Cases to Complete' Action has been added to your Case flow, a new 'Hold Case' tab will display in the info grid.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F9i1cBYRtcvy9Ul7bsjcW%2Fimage.png?alt=media&#x26;token=7ca36e8b-3f8f-4853-9087-7f185a9e98bc" alt=""><figcaption></figcaption></figure>

| Setting    | Description                                                                                                                                                                                                                                                                                | Notes                                             |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- |
| Hold Case  | <p>If you want the Action to wait for a specific Sub-Case to finish before moving on to the next Action, add that Sub-Case here.  </p><p>If you want the Action to wait for any of the Case's Sub-Cases to close before moving on to the next Action, leave the Hold Case field blank.</p> |                                                   |
| Auto-Close | This setting lets you automatically close the Action if no available Sub-Case is running for it.                                                                                                                                                                                           | See below for [more details](#auto-close-option). |
|            |                                                                                                                                                                                                                                                                                            |                                                   |

### Auto-Close Option - Further Details

If the 'Auto-Close' setting is off, the ‘Wait for Sub-Cases to Complete’ Action will be assigned to a Queue where a user will pick it up and decide how to proceed if the Sub-Case the 'Wait for Sub-Cases to Complete’ Action it is set to wait for is not available - either because it has not been launched or because it was resolved before the ‘Wait for Sub-Cases to Complete’ Action was launched.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F3rR4TWCPKFBBIvdNNUgd%2Fimage.png?alt=media\&token=f54f84f2-9259-4617-a469-60d844f5306f)

If you switch the 'Auto-Close' toggle on, instead of assigning the Action to a user to proceed, the ‘Wait for Sub-Cases to Complete’ Action will automatically close if the Sub-Case the 'Wait for Sub-Cases to Complete’ Action it is set to wait for is not running.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FfEzEFzbubkSibbdjPPgN%2Fimage.png?alt=media\&token=3f5c82c4-2c94-4cf3-a690-be6b37bb2c62)

If the Hold Case column is left blank, the ‘Wait for Sub-Cases to Complete’ Action will wait for any Sub-Case of the Case to close before continuing and if there is no Sub Case available, the ‘Wait for Sub-Cases to Complete’ Action will automatically close.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FiUu8Q4yTSVbEyFUocEDv%2Fimage.png?alt=media\&token=942adcde-15cb-4ad3-b1f9-db32f21ef346)
