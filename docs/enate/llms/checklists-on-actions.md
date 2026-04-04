# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/checklists-on-actions.md

# Adding Action Checklists

## Overview

You can set up Actions to display dedicated checklists of activities which must be carried out and confirmed before the Action can be marked as resolved, allowing you to enforce procedure in how Actions should be completed by Agents at runtime.&#x20;

In Work Manager, users will then have to confirm for each item in the checklist whether they have completed it (the options are Yes, No, N/A) and they can even add a note for each check.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FGLy3A9dHWUstLF0ayRYB%2Fimage.png?alt=media&#x26;token=c288819a-bb7e-4dd7-9395-ba1aff463bc0" alt=""><figcaption></figcaption></figure>

You can create two different levels of Action checklists:

* **'Global' checklists** - these are added to the Action type and contain a standard checklist of activities that will be added any time this Action type is added to a Case flow. [See below for more details on how to configure global checklists](#defining-global-checklists).
* **Local Checks -** these are added to Actions already in a Case flow to help support 'custom' activities that take place for that specific Action.  [See below for more details on how to configure global checklists](#defining-local-checklists).

At runtime, users processing the Action in Work Manager will just see a single list of the checks they must complete, with no differentiation between global and local checks. They'll have to complete all of the checks in order to mark their Action as resolved.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FkP2caOrkbRMr9EVPqgCX%2Fimage.png?alt=media&#x26;token=7b827b25-76d7-49dd-8dc0-64b10dc48bdc" alt=""><figcaption></figcaption></figure>

See [here ](https://docs.enate.net/enate-help/implementation/enate-implementations-2/solutioning-in-enate/combining-consecutive-actions)for more detailed information and examples about when you would use checklists on Actions.

## Defining Checklists

### Defining Global Checklists

Global checklists contain a standard checklist of activities that are added to an Action type and will be added any time this Action type is added to a Case flow.&#x20;

You can add a global checklist either from Global Checklist section on the Service Lines screen or from within a Case screen (from the Action's checklist popup).&#x20;

To add a global checklist from the Services Line screen, go to the Service Lines screen and open the Action type you want to add the global checklist to. Add the desired checks, re-order them if necessary and click to save. These checks will be added any time the Action type is used in a Case flow.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZNu3Mf75e3C3Jlugwd%2F-MZO25gXXkvuRjw7uVhO%2Fimage.png?alt=media\&token=23d202a8-0c57-4eca-8ca2-813594ba562d)

You can also add global checks from within an Action in the Case screen itself. Simply click on the checklist icon link of an Action in a Case flow, select 'Global Checklists' from the resulting pop-up and then add the desired global checks. You can re-order them as necessary. Then click to save.

{% hint style="warning" %}
Be aware that any changes you make at a global level for checklists will also update ALL other locations where this Action is being used, and the change will take effect instantly.
{% endhint %}

### Defining Local Checklists

Local checklists are added to Actions already in a Case flow to help support 'custom' activities that take place for that specific Action.

You can add a local checklist from the Action's checklist popup on the Case screen.&#x20;

To do this, click on the checklist icon link of an Action in a Case flow. You'll know if there's already a checklist set to the Action as the checklist icon will be highlighted.&#x20;

Clicking the icon will bring up a popup where you can create your checks. Simply click to add, then enter your description.&#x20;

Once created, individual checks can be re-ordered by clicking on the drag icon then dragging and dropping. Then click to save.

Any checks created here are specific to this Action.

Once important feature to note is that once you've created a local checklist item, you can drag it up to LINK it to a global check, specifying whether it should run before or after a standard global check. You'll see the colour-coding denoting which global check it's linked to. If ever the order of global checks is adjusted, all the linked 'local' checks will move with it. Once you're happy with your overall checklist you can OK this and the checklist for this Action is saved.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZNu3Mf75e3C3Jlugwd%2F-MZO4WSDeqILqwDWeZ6y%2FGIF-Setting-a-Checklist-Item.gif?alt=media\&token=36c4ea22-daf7-4bb6-b7c3-08f435b803fe)
