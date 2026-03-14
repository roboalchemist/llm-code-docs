# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/external-api-action-info-tab.md

# Trigger External API Actions

## Overview

‘Trigger External API’ Actions allow Enate to call out to an external system, passing a static structure containing information information about a Work Item (i.e. a Case, Action or Ticket). This Action type also includes an optional **callbackURL**, which allows the external system to update custom data and pass it back into Enate.

For information on how 'Trigger External API' Actions are shown at runtime, check out this [Work Manager](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-an-action/trigger-external-api-actions) section.&#x20;

The external API will be called as a POST method, and will be sent the following information:

```
{"Action":[ActionPacketJSONIncludingCurlyBraces],"CallBackURL":""}
```

The \[ActionPacketJSONIncludingCurlyBraces] will be an Actionpacket, as per the response from the Enate **getAction** API.

Enate supports this with a 'Trigger External API' Action type that you can add to your Case flows.&#x20;

For detailed information on how Trigger External APIs work at runtime, see the dedicated [Work Manager](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-an-action/trigger-external-api-actions) section.

## Creating a Trigger External API Action Type

You can either create a Trigger External API Action type in the Service Line section of Builder, or directly from your Case flow.

### From the Service Lines Page

Creating a Trigger External API Action type from the Service Lines section of Builder adds the Action to your menu of available Actions when you're building flows subsequently in Cases.&#x20;

To do this, in the Service Lines page select which service line you would like to add the Trigger External API Action to and then click on the plus symbol next to the 'process Search' box and then select 'Action.&#x20;

This will open up a new Action for you to create.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F1QEciw7D50eqCRviS8O5%2Fimage.png?alt=media&#x26;token=95132aeb-0c9a-475f-9c46-1417d8a138ec" alt=""><figcaption></figcaption></figure>

Add a name and description to your Action and then in the 'type' drop down select 'Trigger External API Action'.&#x20;

You can then choose to add a global checklist to the Action. This contains a standard checklist of activities that will be added any time this Action type is added to a Case flow. See here for more information on [checklists](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/checklists-on-actions).

Once you are happy with your Action, hit save to create it. This Action can now be added to new and existing business processes by selecting it from the dropdown list when adding a new Action to a Case.

### From a Case Flow

Alternatively, you can add a Trigger External API Action type directly from the Case flow itself.

To do this, open your desired Case flow in edit mode, click on an Action's menu and then instead of clicking to add an existing Action, select to create a new Action by clicking the '+' icon.

Give the Action a name, add a description if you wish and for its 'type', select 'Trigger External API Action'. This will add the Action to the Case flow.

## Configuring a Trigger External API Action

You now need to configure the settings for the new Action you have added to your Case. Click on the Action in the flow to highlight it in the info section.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fi9tCMDnYJIKey6cGassk%2Fimage.png?alt=media&#x26;token=a56a9950-7bb2-4a71-b0b2-5acffa0b549c" alt=""><figcaption></figcaption></figure>

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

Additionally, once a Trigger External Action has been added to your Case flow, a new 'External API' tab will display in the info grid.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fk65SIIgDzOQrUHHRcpOv%2Fimage.png?alt=media&#x26;token=08d2c4e8-c190-42eb-bb6c-3f89b33aadc4" alt=""><figcaption></figcaption></figure>

| Setting                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Notes                                                                                                       |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| API Integration URL             | Enter the API Integration URL in this column.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                             |
| Response Expected               | <p>Switching this setting on means that the Action will only be marked as complete when the external system to calls back to Enate with the supplied call-back URL. </p><p></p><p>Leaving the setting off means that the Action will call the external system and close the Action, in a "fire and forget" manner.</p>                                                                                                                                                                         | Please note that 1 minute is the minimum value that you can enter in the 'Response Expected Within' column. |
| Response Expected Within (Mins) | <p>Set how many minutes you would like Enate to  to wait for a response before the Action would 'time out' and flip over to a human to progress. </p><p></p><p>If you set the 'Response Expected' slider to On but no value is entered in the 'Response Expected Within' column, the Action will call the external system and wait either until the Due Date for the Action, or indefinitely. This will depend on the General Settings flavour for the Action, see below for more details.</p> |                                                                                                             |
|                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                             |

#### &#x20;<a href="#additional-setting-response-expected-and-associated-timeout" id="additional-setting-response-expected-and-associated-timeout"></a>

### If 'Response Expected Within' is left blank - further details <a href="#if-response-expected-within-is-left-blank" id="if-response-expected-within-is-left-blank"></a>

If you set the 'Response Expected' slider to On but no value is entered in the 'Response Expected Within' column, the Action will call the external system and wait either until the Due Date for the Action, or indefinitely.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Me9Y-upsl54g8Q5-w4S%2F-Me9YXCZyCDzAdcOItlg%2Fimage.png?alt=media\&token=f8234372-f79f-4f8d-8c6d-ad9a21350d23)

The decision on whether the Action will wait indefinitely or not is determined based on the 'Autocomplete on Timeout' setting in the General Settings flavour set for the Action.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Me9Y-upsl54g8Q5-w4S%2F-Me9Y_r_CKIsqhg-THx5%2Fimage.png?alt=media\&token=359d957d-d016-471d-93a2-019ee0ec5090)

* If Auto-complete in General settings is set to On, the system will time the Action out when it hits the Due Date / Time.
* If Auto-complete in General settings is set to Off, the Action will wait indefinitely.

If / When the Action DOES time out at the point of reaching the Due Date, the Action will moved to a state of 'Closed' with a reason of 'No response returned'.&#x20;

Note: If you have both these settings filled (i.e. a 'Response expected minutes' value AND  the 'Auto-complete on Timeout' flag set), the system will act on whichever time comes first - most likely after the 'Response expected minutes' time has been reached.

{% hint style="info" %}
Please note that the Case owner will not be notified in this scenario.&#x20;
{% endhint %}

## Behaviour in various scenarios

There are a number of possible ways the system will behave, dependant upon how you have configured the various timeout settings AND how the external API actually responds. For detailed information on this, see the following attachment which lays out each combination of settings and behaviour, and the eventual result.

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MfrHZIhuibXO4hcTq20%2F-MfrIpNGUD4Hdvn2xfDt%2FTrigger%20External%20API%20Action%20-%20Behaviour.xlsx?alt=media&token=a21a9e73-04f1-47cc-a9de-09d5dd6e1dd9>" %}
