# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/peer-review-action-info-tab.md

# Peer Review Actions

## Overview

Peer Review Actions are a great way for different members of a team to crosscheck each other's work for key actions within a case, letting you embed quality checks into your processes without having to add in feedback flows.

Enate supports this with a 'Manual with Peer Review' Action type that you can add to your Case flows. These are like 'Manual' Action types, except that once the initial manual activity is carried out by a user, Enate will route the Action to be picked up by a different user to check the work, passing or failing it. If failed, it will route back to the original user to resolve the issues.

Watch this video to find out more about how to set up a Peer Review Action:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM1MjkwMg==>" %}

Click [here ](https://docs.enate.net/enate-help/implementation/enate-implementations-2/solutioning-in-enate/using-peer-review-actions)for more information and examples about when and why you would user Peer Review Actions.

For detailed information on how Peer Review Actions work at runtime, see the dedicated [Work Manager](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-an-action/peer-review-actions) section.

#### Creating a Peer Review Action Type

You can either create a Peer Review Action type in the Service Line section of Builder, or directly from your Case flow.

#### From the Service Lines Page

Creating a Peer Review Action type from the Service Lines page adds the Action type to your menu of available Actions when you're building flows subsequently in Cases.&#x20;

To do this, in the Service Line page, select which service line you would like to add the peer review Action to and then click on the plus symbol next to the 'Process Search' box. This will bring up a drop down menu where you can select an Action.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FpDeZfDFSpRIfiefQu4Dy%2Fimage.png?alt=media&#x26;token=4e43ffe1-0abd-4e26-ab9e-d2161dd847e0" alt=""><figcaption></figcaption></figure>

This will open up a new Action for you to create. &#x20;

Add a name and description to your Action and then in the type drop down select 'Manual Action with Peer Review'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FtEoqZuRuT6V8d1JseBJQ%2Fimage.png?alt=media&#x26;token=db2f6f4b-868d-4743-90e0-6aa49a2569b8" alt=""><figcaption></figcaption></figure>

You can then choose to add a global checklist to the Action. This contains a standard checklist of activities that will be added any time this Action type is added to a Case flow. See here for more information on [checklists](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/checklists-on-actions).

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F0vh3C6neNnpnN5eg71Qu%2Fimage.png?alt=media&#x26;token=2a344972-0512-4045-954b-3ae3c6bba070" alt=""><figcaption></figcaption></figure>

You can also choose to add a Peer Reviewer global checklist to the Action. This contains a standard checklist of activities for the peer reviewer to complete that will be added any time this Action type is added to a Case flow. See here for more information on [peer review checklists](#adding-a-peer-review-checklist).&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FCQ6muJ4NtxLxVVfymUIZ%2Fimage.png?alt=media&#x26;token=1dea0b4c-e3ea-4962-b331-22f201e770bc" alt=""><figcaption></figcaption></figure>

Once you are happy with your Action, hit save to create it. This Action can now be added to new and existing business processes by selecting it from the dropdown list when adding a new Action to a Case.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FZzK3ADsTjo6pFNJjsuZQ%2Fimage.png?alt=media&#x26;token=feb249fe-41c4-46df-87c9-c2e9c23b39f5" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F4b9Ynf2VxcdqjkZgI1OE%2Fimage.png?alt=media&#x26;token=ad36cd8b-eff0-49ed-a697-427942c4be0f" alt=""><figcaption></figcaption></figure>

#### From a Case Flow

Alternatively you can add an Peer Review Action type directly from the Case flow itself.

To do this, open a Case flow in edit mode, click on an Action's menu and then instead of clicking to add an existing Action, select to create a new Action by clicking the '+' icon.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FShSTCrdu8z9j35e42YT4%2Fimage.png?alt=media&#x26;token=e15838eb-5435-4a32-b2cc-294cbb8f7809" alt=""><figcaption></figcaption></figure>

Give the Action a name, add a description if you wish and for its type, select 'Manual with Peer Review Action'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FXba1s5NqOncwUFfgC1Ib%2Fimage.png?alt=media&#x26;token=e18600e0-a208-42f2-a43f-bb821df1146c" alt=""><figcaption></figcaption></figure>

This will add the Peer Review Action to the Case flow.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F3HoZFqxM9EDg1x3IBvmv%2Fimage.png?alt=media&#x26;token=66494806-c3a2-488b-9006-afaa81b49f59" alt=""><figcaption></figcaption></figure>

#### Configuring Peer Review Actions

You now need to configure the settings for the new Action you have added to your Case. Click on the Action in the flow to highlight it in the info section.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FrCHk5USQXC95P7KQUtpu%2Fimage.png?alt=media&#x26;token=5a59c676-57ae-4abc-bfea-4ea51efe77df" alt=""><figcaption></figcaption></figure>

In the Action Info tab, you need to add the usual following information for an Action:

| Setting            | Description                                                                                                                                                                                                       | Notes                                                                                                                                                                                                                                                                                          |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| When is it due?    | This is for the initial 'completion' stage of the Action. Select a value from the dropdown menu of Due Date ‘flavours’                                                                                            | <p>Mandatory to set live.</p><p>(See <a href="../../shared-standardised-settings-flavours/due-date-flavours">Due Date Flavours Settings</a> for more information).</p>                                                                                                                         |
| Who does it go to? | This is for the initial 'completion' stage of the Action. Select a value from the dropdown menu of Allocation ‘flavours’                                                                                          | <p>Mandatory to set live.</p><p>(See <a href="../../shared-standardised-settings-flavours/allocation-flavours">Allocation Flavours Settings</a> for more information). Note that the system will not allow the user who carried out the manual activity to also carry out the peer review.</p> |
| General Settings   | Select a value from the dropdown menu of Follow Up ‘flavours’                                                                                                                                                     | <p>Mandatory to set live.</p><p>(See <a href="../../shared-standardised-settings-flavours/general-settings-flavours-action-only">General Settings Flavours Settings</a> for more information).</p>                                                                                             |
| Main Card          | You can select a Custom Card to display on the main section of the Action screen.                                                                                                                                 | Optional. See here for more information about [Custom Cards](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration).                                                                                                                              |
| Side Card          | You can select a Custom Card to display on the side panel of the Action screen.                                                                                                                                   | Optional. See here for more information about [Custom Cards](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration).                                                                                                                              |
| Manual Creation    | Switching this setting on allows the Action to be started manually in Work Manager.                                                                                                                               | Optional. See [Adding Ad-hoc Actions](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/adding-ad-hoc-actions) section for more information.                                                                                                |
| Checklist          | Here you can add local checks to the Action that help support 'custom' activities that take place for that specific Action. You can also edit the global checks for the Action type from here too, if it has any. | Optional. See here for more information about [adding checklists](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/checklists-on-actions).                                                                                                 |

Additionally, once a Peer Review Action has been added to your Case flow, a new 'Peer Review' tab will display in the info grid.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FY2CzrcFQZyZkEjf4e2VU%2Fimage.png?alt=media&#x26;token=82ad5e40-e246-4dc3-b245-9b9b52316f9c" alt=""><figcaption></figcaption></figure>

Here you need to add the following settings that are only relevant for the Action once it is in its 'Peer Review' stage.

| Setting               | Description                                                                                                                                | Notes                                                                                                                                                                                                                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| When is it due?       | This is for the peer review stage of the Action. Select a value from the dropdown menu of Due Date ‘flavours’                              | <p>Mandatory to set live.</p><p>(See <a href="../../shared-standardised-settings-flavours/due-date-flavours">Due Date Flavours Settings</a> for more information).</p>                                                                                                                         |
| Who does it go to?    | This is for the peer review stage of the Action. Select a value from the dropdown menu of Allocation ‘flavours’                            | <p>Mandatory to set live.</p><p>(See <a href="../../shared-standardised-settings-flavours/allocation-flavours">Allocation Flavours Settings</a> for more information). Note that the system will not allow the user who carried out the manual activity to also carry out the peer review.</p> |
| Peer Review Checklist | Here you can add local checks for the peer reviewer to complete and edit the global peer review checks for the Action type, if it has any. | Optional. See [here](#adding-a-peer-review-checklist) for more information.                                                                                                                                                                                                                    |

#### Peer Review Checklists

You can set up Peer Review Actions to display a dedicated checklist for the peer review section of the Action. These checks must be carried out and confirmed by the peer reviewer before the Action can be marked as resolved, allowing you to enforce procedure in how Peer Review Actions should be completed by agents at runtime.&#x20;

In Work Manager, users will then have to confirm for each item in the checklist whether they have completed it (the options are Yes, No, N/A) and they can even add a note for each check.

You can create two different levels of peer review checklists:

* **'Global' checklists** - these are added to the Action type and contain a standard checklist of activities must be carried out and confirmed by the peer reviewer before the Action can be marked as resolved. Global checks will be added any time this Action type is added to a Case flow. Global peer review checks can be added/edited at Service Line level or from the Peer Review Checklist setting in the Case screen.&#x20;
* **'Local' checklists -** these help support 'custom' activities that take place for that specific Action that must be carried out and confirmed by the peer reviewer before the Action can be marked as resolved. Local checks will only apply to the specific Action they have been added to. Local peer review checks are added to the Peer Review Action itself from the Peer Review Checklist setting in the Case screen.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FjqPGKY6Mph5uSUnIihGs%2Fimage.png?alt=media&#x26;token=329382d7-33a2-4525-9ae6-f81cce745d14" alt=""><figcaption></figcaption></figure>

Once important feature to note is that once you've created a local checklist item, you can drag it up to LINK it to a global check, specifying whether it should run before or after a standard global check. You'll see the colour-coding denoting which global check it's linked to. If ever the order of global checks is adjusted, all the linked 'local' checks will move with it. Once you're happy with your overall checklist you can OK this and the checklist for this Action is saved.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FE5iIwd0gY3NRs54DqlcT%2Fimage.png?alt=media&#x26;token=f6829f8c-0a41-4ada-9426-fd820c83c530" alt=""><figcaption></figcaption></figure>

At runtime, users reviewing the Action in Work Manager will just see a single list of the checks they must complete, with no differentiation between global and local checks. They'll have to complete all of the checks in order to mark their Action as resolved.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FSl3CgHIARIuC9oM9R30q%2Fimage.png?alt=media&#x26;token=39542107-941d-463b-abef-13ef6aebbf7d" alt=""><figcaption></figcaption></figure>

#### Adding Conditions to Bypass a Peer Review

You can also choose to automatically bypass a peer review by adding a condition to a Peer Review Action in your Case configuration. If that condition is met, the peer review part of the Action will no longer be required. This gives you more flexibility when using Peer Review Actions and allows you to avoid any unnecessary peer reviews.

To set a condition for a peer review, in your Case flow screen select the relevant Peer Review Action and, on the Peer Review tab, click the 'Bypass if' icon.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F1uZlLlDoJSCVYbdIfTgx%2Fimage.png?alt=media&#x26;token=29236495-a8fa-4fa1-b9e7-a3000fbae96d" alt=""><figcaption></figcaption></figure>

In the resulting popup, set your condition - choosing a data field (which can be standard or one of your own custom data items), then a condition and a value.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FuBJ2ACEnHgfpoFblKoyo%2Fimage.png?alt=media&#x26;token=bcf430c7-67c0-4967-a3a4-59cf0356b493" alt=""><figcaption></figcaption></figure>

Selecting the 'Advanced' option lets you create a more complex condition with a combination of multiple criteria, adding a plus symbol between each part. You can check the validity of your expression via the external DotNetfiddle link. Once you're happy with your settings here, apply the condition.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FFEyJQyvhZruHYWa3qqj5%2Fimage.png?alt=media&#x26;token=ad21263b-5ca9-47f2-b5bd-b52b205ca124" alt=""><figcaption></figcaption></figure>

The 'Bypass if' icon will the be highlighted, showing that a condition has been added.&#x20;

Save the update to your Case and set the new version live.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVXfjvnN8QTLrvdfUL3N8%2Fimage.png?alt=media&#x26;token=87691169-b653-4276-ae1f-78874dbe0fbd" alt=""><figcaption></figcaption></figure>

Over in Work Manager, if the condition you have added is met, at runtime the activity will move straight from the manual activity onto the next Action, bypassing the peer review stage. A note will subsequently be displayed in the Actions list on the Case screen, showing that the peer review activity was not required.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FI7VPlAVQs1qDotdRV0e6%2Fimage.png?alt=media&#x26;token=d5fef531-a42d-4f03-b360-d7e54320dae0" alt=""><figcaption></figcaption></figure>
