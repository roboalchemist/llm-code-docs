# Source: https://uat.rive.app/docs/editor/layouts/layout-animation.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Animation

> Add animation to a Layout container to define how it interpolates when content reflows. When a Layout container needs to resize, its children may need to change their position. Adding Layout animation allows the reflowing of children to happen over time and with a chosen easing curve.

## Adding Layout Animation

To get started, select a Layout component and select the `+` action alongside `Layout Animation` in the inspector. Typically, you may want to set this on the parent Layout in the majority of cases.

<img src="https://mintcdn.com/rive/IMrXM-oXoMvrTV9Y/images/editor/layouts/d72ffb27-34c2-4703-8828-07d89e023cf6.webp?fit=max&auto=format&n=IMrXM-oXoMvrTV9Y&q=85&s=b9d61f63ff44f816f077ffbdafa67a7d" alt="Image" width="1280" height="720" data-path="images/editor/layouts/d72ffb27-34c2-4703-8828-07d89e023cf6.webp" />

Next, choose from one of 3 different modes:

* **None:** No animation.
* **Inherit:** Inherit the animation parameters from the parent Layout.
* **Custom:** Define the animation parameters for the selected Layout.

With the custom option selected, you can set a duration and interpolation type similar to that of a State Machine transition. All interpolation types except cubic value are supported.

<img src="https://mintcdn.com/rive/KnNrDuhU1mIj7cOb/images/editor/layouts/2de7450c-11b4-459d-a5a0-dabeae3c342c.webp?fit=max&auto=format&n=KnNrDuhU1mIj7cOb&q=85&s=4ebc47bac748c4510755a5bd353dfd0e" alt="Image" width="2560" height="1440" data-path="images/editor/layouts/2de7450c-11b4-459d-a5a0-dabeae3c342c.webp" />

With a custom animation applied to a parent Layout, setting the child Layouts to `inherit` means they'll all use the same parameters as those on the parent. Alternatively, you can choose to apply custom interpolation to child components individually.

<video width="640" controls>
  <source src="https://ucarecdn.com/377012bf-760a-48bc-baf8-6747efe3ad5d/" type="video/mp4" />

  Custom animation
</video>
