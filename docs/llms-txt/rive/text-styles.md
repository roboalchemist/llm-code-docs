# Source: https://uat.rive.app/docs/editor/text/text-styles.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Text Styles

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

<YouTube id="FeUOLDzvSDw" />

A Text Style contains many of the familiar options that define how you'd like your text to be styled, and is applied to one or more runs. Currently, only Text Styles defined on a Text object can be applied to it. We'll introduce ways to share Text Styles across multiple Text objects or entire Rive files in future.

Each new Text object is created with a Text Style. Use the `+` action in the Inspector to create additional styles to be applied to specific Text Runs or to key between in an animation.

Each Text Style contains:

* Font
* Font Size
* Font Weight
* Line Height
* Fills
* Strokes

<img src="https://mintcdn.com/rive/t7xZuPf_MPCsV7Zu/images/editor/text/text-runs-styles.gif?s=fa762bf118fb1a812321408f845cbc21" alt="Add multiple styles to a single text object" width="1200" height="581" data-path="images/editor/text/text-runs-styles.gif" />

### Applying a style to a Text Run

There are two ways to apply a Text Style to a Text Run:

* Select the Text Run in the hierarchy, then use the Style dropdown in the Inspector.
* Select the `A+` icon alongside the style options in the Inspector, then use the popup menu to select the desired Text Run. Hovering each option will preview the result on the Stage.

<img src="https://mintcdn.com/rive/t7xZuPf_MPCsV7Zu/images/editor/text/text-runs-apply.gif?s=a091696075de561fea9b70ea3b335f6f" alt="Apply a style to a chosen run" width="1200" height="555" data-path="images/editor/text/text-runs-apply.gif" />

***

## Variables

Fonts that support variable axes or OpenType features will surface an options fly-out button on the Text Style within the Inspector. Use the fly-out to access and configure the available variables and features for the selected font.

Font variables can be animated in Rive. Open the variable fly-out in Animate mode to key the available axes.

<img src="https://mintcdn.com/rive/t7xZuPf_MPCsV7Zu/images/editor/text/text-runs-variable.gif?s=e058a937f81d30691c174e01bf173c13" alt="Animate font variables" width="1200" height="436" data-path="images/editor/text/text-runs-variable.gif" />
