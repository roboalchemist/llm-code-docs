# Overview

In CreativeEditor SDK (CE.SDK), _outlines_ refer to visual enhancements added around design elements. They include strokes, shadows, and glows, each serving to emphasize, separate, or stylize content. Outlines help improve visibility, create visual contrast, and enhance the overall aesthetic of a design.

You can add, edit, and remove outlines both through the CE.SDK user interface and programmatically via the API.

[Launch Web Demo](https://img.ly/showcases/cesdk)[

Get Started

](vue/get-started/overview-e18f40/)

## Understanding Outlines[#](#understanding-outlines)

*   **Stroke (Outline):** A solid line that directly traces the border of an element. Strokes can vary in thickness, color, and style (such as dashed or dotted lines).
*   **Shadow:** A duplicate of the element rendered with an offset and blur effect, creating the illusion of depth.
*   **Glow:** A soft, diffused light that radiates outward from the element, typically used to create a luminous or halo effect.

We don’t support `glow` directly in our API, however, it can be achieved by using a brightly-colored shadow.

Each type of outline offers different visual styles and purposes, allowing you to tailor your design’s look and feel.

## Supported Elements[#](#supported-elements)

You can apply outlines to a wide range of elements in CE.SDK, including:

*   Text elements
*   Shapes
*   Images
*   Stickers

Some asset types or highly customized components may have limitations on which outline effects they support. Always check element capabilities if outline options appear unavailable.

## UI Editing[#](#ui-editing)

In the CE.SDK user interface, you can:

*   **Add outlines** by selecting an element and enabling stroke, shadow, or glow options in the properties panel.
*   **Edit outline properties** such as color, thickness, opacity, blur radius, and offset directly through the UI controls.
*   **Remove outlines** by disabling the stroke, shadow, or glow for a selected element.

These tools allow designers to quickly apply and adjust outlines without needing to write code.

## Programmatic Editing[#](#programmatic-editing)

Developers can also manage outlines programmatically using the CE.SDK API. This includes:

*   **Accessing and modifying properties** such as stroke color, stroke width, shadow blur, and shadow offset.
*   **Enabling or disabling outlines** for individual design blocks.
*   **Removing outlines** programmatically by disabling stroke or shadow effects on a block.

Programmatic control enables dynamic styling and automation for design generation workflows.

## Customizing Outline Properties[#](#customizing-outline-properties)

Outlines in CE.SDK offer a variety of customizable properties to fit different design needs:

*   **Color:** Define the stroke or glow color to match branding or design themes.
*   **Thickness (Stroke Width):** Adjust how bold or subtle the stroke appears around the element.
*   **Opacity:** Control the transparency of strokes, shadows, or glows for subtle or strong effects.
*   **Blur (for Shadows and Glows):** Soften the appearance of shadows or glows by adjusting their blur radius.
*   **Offset (for Shadows):** Set how far a shadow is displaced from the element to control the sense of depth.

---



[Source](https:/img.ly/docs/cesdk/vue/open-the-editor/uri-resolver-36b624)