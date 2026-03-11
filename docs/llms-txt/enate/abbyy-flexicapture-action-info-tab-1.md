# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/abbyy-flexicapture-action-info-tab-1.md

# ABBYY OCR FlexiCapture Actions

## Overview

Enate is able to provide integration with [ABBYY FlexiCapture](https://www.abbyy.com/flexicapture/) to allow intelligent document processing to be part of your Enate processes. This means that documents such as PDFs can be scanned by ABBYY FlexiCapture both to start and to form part of your Enate processes.

When an ABBYY Action runs for a Case, documents attached to the Case can be submitted to ABBYY FlexiCapture for OCR Scanning and the processed output files will be returned and automatically attached to the Case.

Furthermore, if ABBYY FlexiCapture highlights that additional manual verification may be needed (i.e. if confidence levels in the scanned output is below threshold), the work is transferred over to an Enate agent in Work Manager to verify and adjust the data via ABBYY FlexiCapture's dedicated screen, surfaced directly within an Enate Action.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FnTghTY7k1OhrSJqp0Imw%2FABBYY%20Action.png?alt=media&#x26;token=3c917941-a69f-4ac9-ba43-4a9c84d89140" alt=""><figcaption></figcaption></figure>

Enate supports this with an 'ABBYY OCR' Action type that you can add to your Case flows.&#x20;

For detailed information on how ABBYY Actions work at runtime, see the dedicated [Work Manager](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-an-action/abbyy-flexicapture-actions) section.

## Creating an ABBYY Action Type

To create an ABBYY FlexiCapture Action, you first need to set up an ABBYY FlexiCapture connection.

See this article for more information about how to set up an ABBYY FlexiCapture connection:

{% content-ref url="../../../../integrations/enate-integrations/abbyy-integration/setting-up-an-abbyy-flexicapture-integration" %}
[setting-up-an-abbyy-flexicapture-integration](https://docs.enate.net/enate-help/integrations/enate-integrations/abbyy-integration/setting-up-an-abbyy-flexicapture-integration)
{% endcontent-ref %}

Once you have successfully set up an ABBYY connection, you then need to create an ABBYY FlexiCapture Action type.

You can either do this in the Service Line section of Builder, or directly from your Case flow.

### From the Service Lines Page

Creating an ABBYY FlexiCapture Action type from the Service Lines section of Builder adds the Action to your menu of available Actions when you're building flows subsequently in Cases.&#x20;

To do this, in the Service Lines page select, which service line you would like to add the ABBYY Action to and then click on the plus symbol next to the 'Process Search' box. This will bring up a drop down menu where you can select an Action.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FJxCVI2j1Opd6tUM38SEj%2Fimage.png?alt=media&#x26;token=b9d97f01-11cd-4b51-9486-1f1ebf0e1797" alt=""><figcaption></figcaption></figure>

This will open up a new Action for you to create. &#x20;

Add a name and description to your Action and then in the 'type' drop down select 'ABBYY OCR'.

You can then choose to add a global checklist to your ABBYY FlexiCapture Action. This contains a standard checklist of activities that will be added any time this Action type is added to a Case flow. See here for more information on [checklists](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/checklists-on-actions).

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FGLf8o2avn5ptIyNWEQ6e%2Fimage.png?alt=media&#x26;token=7b120fd0-1063-4be7-8f44-c9789325c8d2" alt=""><figcaption></figcaption></figure>

Once you are happy with your Action, hit save to create it. This Action can now be added to new and existing business processes by selecting it from the dropdown list when adding a new Action to a Case.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FGkTub5LoJKU5w7CqDwYh%2Fimage.png?alt=media&#x26;token=d867eb01-1808-4783-b92f-8d33b31dc134" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FV6EdNY63Fy8tP9TAzNFI%2Fimage.png?alt=media&#x26;token=9c8f1baa-618d-4506-9f2d-3c20b9cb61e2" alt=""><figcaption></figcaption></figure>

### From a Case Flow

Alternatively, you can add an ABBYY FlexiCapture Action type directly from the Case flow itself.

To do this, open your desired Case flow in edit mode, click on an Action's menu and then instead of clicking to add an existing Action, select to create a new Action by clicking the '+' icon.

Give the Action a name, add a description if you wish and for its 'type', select 'ABBYY OCR'. This will add the ABBYY FlexiCapture Action to the Case flow.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWjf2RyMA-Z_kc_TTUe%2F-MWjfvVAi2Mzy71oXtZW%2FAdding-ABBYY-Type-Action-to-Case.gif?alt=media\&token=14626cfe-294f-4f72-95ce-f104b4ea48d5)

## Configuring an ABBYY Action

You now need to configure the settings for the new Action you have added to your Case. Click on the Action in the flow to highlight it in the info section.

In the Action Info tab, you need to add the following information:

| Setting            | Description                                                                                                                                                                                                       | Notes                                                                                                                                                                                              |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| When is it due?    | Select a due date from the dropdown menu of Due Date ‘flavours’                                                                                                                                                   | <p>Mandatory to set live.</p><p>(See <a href="../../shared-standardised-settings-flavours/due-date-flavours">Due Date Flavours Settings</a> for more information).</p>                             |
| Who does it go to? | Select a value from the dropdown menu of Allocation ‘flavours’                                                                                                                                                    | <p>Mandatory to set live.</p><p>(See <a href="../../shared-standardised-settings-flavours/allocation-flavours">Allocation Flavours Settings</a> for more information). </p>                        |
| General Settings   | Select a value from the dropdown menu of Follow Up ‘flavours’                                                                                                                                                     | <p>Mandatory to set live.</p><p>(See <a href="../../shared-standardised-settings-flavours/general-settings-flavours-action-only">General Settings Flavours Settings</a> for more information).</p> |
| Main Card          | You can select a Custom Card to display on the main section of the Action screen.                                                                                                                                 | Optional. See here for more information about [Custom Cards](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration).                                  |
| Side Card          | You can select a Custom Card to display on the side panel of the Action screen.                                                                                                                                   | Optional. See here for more information about [Custom Cards](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration).                                  |
| Manual Creation    | Switching this setting on allows the Action to be started manually in Work Manager.                                                                                                                               | Optional. See [Adding Ad-hoc Actions](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/adding-ad-hoc-actions) section for more information.    |
| Checklist          | Here you can add local checks to the Action that help support 'custom' activities that take place for that specific Action. You can also edit the global checks for the Action type from here too, if it has any. | Optional. See here for more information about [adding checklists](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/checklists-on-actions).     |

Additionally, once an ABBYY Action has been added to your Case flow, a new 'ABBYY FlexiCapture' tab will display in the info grid.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpaP-7H9QReEXdkc06%2F-MWpbMw28oUjpryvTgIQ%2Fimage.png?alt=media\&token=84d26c23-77c1-4427-b335-2c910921aba0)

Here you need to add the following settings that are only relevant for ABBYY Actions:

| Setting         | Description                                                                                                                          | Notes                                                                                                                                                                                                                                                                               |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Platform        | The ABBYY Platform being used for this Action                                                                                        | Mandatory                                                                                                                                                                                                                                                                           |
| Project         | The ABBYY project this is part of.                                                                                                   | Mandatory                                                                                                                                                                                                                                                                           |
| Input File Tag  | Only documents with this File Tag will be passed to ABBYY for processing with this Action.                                           | Optional. If an Input File Tag has been specified then only files on this Action marked with this tag will be included in the ABBYY batch. If no Input File Tag is selected then all files attached to the Case will be included for scanning and processing by ABBYY FlexiCapture. |
| Output File Tag | When ABBYY is finished processing documents as part of this Action, it will pass them back to Enate marking them with this File Tag. | Optional. If an Output File Tag has been specified then all files processed by this Action will be tagged with the Output File Tag value when they are transferred back through to Enate.                                                                                           |

{% hint style="info" %}
Note : As an additional validation check, when configuring Case flows that includes ABBYY Actions, if any of the referenced platform are now deleted, the system will prompt you to replace this with an active ABBYY Platform.
{% endhint %}

Your ABBYY FlexiCapture Action is now ready to be used in your Case flows.
