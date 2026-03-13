# Source: https://uat.rive.app/docs/editor/text/text-runs.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Text Runs

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

<YouTube id="UE23Agn1DZ0" />

Runs allow you break your text up into sections — typically, they're used to apply a variety of styles to a single block of text. Whilst most tools manage text runs behind the scenes, Rive exposes them for greater control when dynamically changing text at runtime.

You may want to split your text into multiple runs to apply a different style (such as font, font size, color etc.) to a certain part of your text, where you can then [update your text runs at runtime](/runtimes/text#read-update-text-runs-at-runtime).

<Info>
  A Text Run may only have one Text Style applied at a time.
</Info>

For example, an animation welcoming a user to an app or website may greet them by their name. In the Rive Editor, you may design and animate the text to read "Welcome back, username". Defining "username" as it's own run means you can target it with the Rive Runtimes and replace it with the user's name.

<img src="https://mintcdn.com/rive/iAAe8nJlAD_vtESu/images/editor/text/text-runs-update-run.gif?s=00c9a1f51b8232a68d2c82427fb46de1" alt="Update text for a specific run" width="1200" height="410" data-path="images/editor/text/text-runs-update-run.gif" />

***

## Creating a Text Run

To create a Run, select the desired portion of text and select the 'Run from Selection' button in the Inspector. You can see Text Runs listed beneath the text object in the hierarchy.

Double click or press `Enter` with the text box selected to start editing text.

Toggle the 'Highlight Text Runs' option in the inspector for a visual guide of your current Text Runs. Hovering a run in the hierarchy also highlights its location within the text.

<img src="https://mintcdn.com/rive/iAAe8nJlAD_vtESu/images/editor/text/text-runs-create-run.gif?s=e4606199b795d478d937d4275e1d2360" alt="Split text into multiple runs" width="1198" height="482" data-path="images/editor/text/text-runs-create-run.gif" />

***

## Managing Text Runs

Select a Text Run in the hierarchy for inspector options:

* **Text Value:** Update the text value for the run. Key this value in animate mode.
* **Edit Text Run:** Initiate the text editor with the run pre-selected.
* **Merge with Next:** Combine the selected run with the next run.
* **Merge with Previous:** Combine the selected run with the previous run.
* **Delete text Run:** Delete the run and its contents.
* **Style:** Assign one of the Text Styles defined on the text object. Key this value in animate mode.

<img src="https://mintcdn.com/rive/iAAe8nJlAD_vtESu/images/editor/text/text-runs-managing-run.gif?s=7fc27758d6bbd6fdb393359e53bc5897" alt="Assign a Text Style to a Text Run" width="1200" height="557" data-path="images/editor/text/text-runs-managing-run.gif" />
