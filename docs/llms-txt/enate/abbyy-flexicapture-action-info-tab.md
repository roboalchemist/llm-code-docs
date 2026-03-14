# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/abbyy-flexicapture-action-info-tab.md

# IDP Data Extraction Actions

## Overview

The Document Extraction component automatically extracts the relevant data from files attached to incoming emails so that this data can be used in further processing of the work item, saving your agents time and effort. This also means that documents such as PDFs can be scanned and used both to start Cases in Enate and to form part of the ongoing process's activities.&#x20;

When a Document Extraction Action runs for a Case, documents attached to the Case can be submitted to your desired technology for scanning and the processed output files will be returned and automatically attached to the Case.

If at any point the technology you're using is not confident enough of the results, based on a confidence threshold that you can set, Enate will instantly transfer the work to an agent in Work Manager to look over and verify, giving you that 'human in the loop' support.

Enate supports this with an 'IDP Data Extraction' Action type that you can add to your Case flows. You'll need to  before you can use IDP Data Extraction Actions in your flows.

For detailed information on how IDP Data Extraction Actions work at runtime, see the dedicated [Work Manager](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-an-action/abbyy-flexicapture-actions) section.

## Creating an IDP Data Extraction Action Type

To create an IDP Data Extraction Action, you first need to have activated the Data Extraction component in Enate Marketplace. See [this article](https://docs.enate.net/enate-help/integrations/enate-integrations/auto-extract-document-data-document-extraction) for more information.

You'll then need to set up your Case flow to support the Document Extraction component. This involves adding an 'IDP Data Extraction' Action in Enate Builder to use in your desired Case flows.&#x20;

You can either add an existing one from the Actions list if one has already been created, or you can create a brand new one.&#x20;

IDP Data Extraction Actions can be created in the same way any other Action is created in Enate: either from the Service Line page, or directly from within your Case flow.

To create an IDP Data Extraction Action from the Service Line page, select to create a new Action under the desired service line, give the action a name and a description and choose approval action from the type drop down.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FXLeu1DtB3LBDdKGdbi8c%2Fimage.png?alt=media&#x26;token=bf2ddd11-a209-42ab-a430-e7ec565db3d3" alt=""><figcaption></figcaption></figure>

You can also give the Action a global checklist if you wish. This contains a standard checklist of activities that will be added any time this Action type is added to a Case flow. See here for more information on [checklists](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/checklists-on-actions).

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FGLf8o2avn5ptIyNWEQ6e%2Fimage.png?alt=media&#x26;token=7b120fd0-1063-4be7-8f44-c9789325c8d2" alt=""><figcaption></figcaption></figure>

To create an IDP Document Extraction Action directly from the Case flow itself, open a Case flow in edit mode, click on an Action's menu and then instead of clicking to add an existing Action, select to create a new Action by clicking the '+' icon.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FyhgZ6jYhl4mcOuU16YG9%2Fimage.png?alt=media&#x26;token=903727f6-5085-4bae-878f-0a8490a2147d" alt=""><figcaption></figcaption></figure>

Give the Action a name, add a description if you wish and for its type, select 'Approval'. When you click 'OK, the Action will be created and added to the Case flow.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FX1Pl0b90t3qvqReWna9h%2Fimage.png?alt=media&#x26;token=0ad95bff-28be-4e34-a3ed-e8d1d4a5b826" alt=""><figcaption></figcaption></figure>

Once you have added your approval action to your flow, you will then need to fill out its settings.

On the Action Info tab you will need to set when it's due and set an Allocation rule.&#x20;

{% hint style="info" %}
Note that this Allocation should be who the Action should go to to review if the extraction technology is not confident enough in its data extraction results. If the technology you're using is confident enough about its data extraction results, this Action won't even need to be seen by a human user, it will simply be completed automatically and the Case will move on to the next Action.
{% endhint %}

There's also general settings for the Action too, and ability to set a custom card, again only really for use in the unlikely event that someone needs to intervene and view the action in Work Manager.

Next, go to the IDP Document Extraction tab to define the settings which specifically relate to the approval activities.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FpiWtJqusXuhvZ9r6NUNk%2Fimage.png?alt=media&#x26;token=b88ecfd4-9f40-4af5-8cbb-cdfdb2259fd3" alt=""><figcaption></figcaption></figure>

You'll need to fill in the Extraction Model - this is the ID of the model you want to use for that process.

You'll also need to fill in the input and output tags. The input tag is the tag that the file/document must be tagged with in Work Manager in order to be eligible for document extraction processing and output tags. The output tag is the tag that will be assigned to the file/document in Work Manager once the document extraction process has completed.&#x20;

Once you have filled in the above settings details, set the Case live.

## Configuring an IDP Data Extraction Action

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

Additionally, once an IDP Document Extraction Action has been added to your Case flow, a new 'IDP Data Extraction' tab will display in the info grid.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FDsadcOpTQyaTemKQUfQ1%2Fimage.png?alt=media&#x26;token=47264ba4-153b-4e2f-a177-d507a4ac1ebc" alt=""><figcaption></figcaption></figure>

Here you need to add the following settings that are only relevant for IDP Document Extraction Actions:

| Setting          | Description                                                                                                                            | Notes                                                                                                                                        |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Extraction Model | The ID of the Infrrd model you want to use for that process                                                                            | Mandatory                                                                                                                                    |
| Input File Tag   | Only documents with this File Tag will be passed to Infrrd for processing with this Action.                                            | Mandatory                                                                                                                                    |
| Output File Tag  | When Infrrd has finished processing documents as part of this Action, it will pass them back to Enate marking them with this File Tag. | Mandatory. All files processed by this Action will be tagged with the Output File Tag value when they are transferred back through to Enate. |

Your IDP Document Extraction Action is now ready to be used in your Case flows.
