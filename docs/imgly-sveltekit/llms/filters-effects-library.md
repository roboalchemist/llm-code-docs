# Filters & Effects Library

In CreativeEditor SDK (CE.SDK), _filters_ and _effects_ refer to visual modifications that enhance or transform the appearance of design elements. Filters typically adjust an element’s overall color or tone, while effects add specific visual treatments like blur, sharpness, or distortion.

You can apply both filters and effects through the user interface or programmatically using the CE.SDK API. They allow you to refine the look of images, videos, and graphic elements in your designs with precision and flexibility.

[Launch Web Demo](https://img.ly/showcases/cesdk)[

Get Started

](sveltekit/get-started/overview-e18f40/)

## Understanding Filters vs. Effects[#](#understanding-filters-vs-effects)

*   **Filters** are broad transformations that modify the entire appearance of an element. Common examples include:
    
    *   Color adjustments (e.g., brightness, contrast)
    *   Lookup Table (LUT) filters for advanced color grading
    *   Duotone color schemes
*   **Effects** apply targeted visual modifications to an element. Typical examples include:
    
    *   Blurring an area to soften details
    *   Sharpening to enhance clarity
    *   Distorting shapes for creative transformations

**Key Differences:**

| Aspect | Filters | Effects |
| --- | --- | --- |
| Scope | Alters the entire visual appearance | Applies a specific modification |
| Examples | LUTs, duotone, adjustments | Blur, sharpen, distortion |
| Use Case | Color grading, mood setting | Stylizing or emphasizing parts |

Understanding the distinction helps you choose the right tool depending on whether you want broad tonal changes or focused visual alterations.

## Supported Filters and Effects[#](#supported-filters-and-effects)

CE.SDK offers a range of built-in filters and effects ready to use out of the box.

**Available Filters:**

*   **Adjustment Filters:** Modify brightness, contrast, saturation, and more.
*   **LUT (Lookup Table) Filters:** Apply professional-grade color transformations.
*   **Duotone Filters:** Map the shadows and highlights of an image to two custom colors.

**Available Effects:**

*   **Blur:** Soften an area for background separation or artistic focus.
*   **Sharpen:** Enhance fine details for a crisper appearance.
*   **Distortion:** Warp the geometry of an element for creative effects.
*   **Chroma Key (Green Screen):** Remove a background color, often used for compositing images.

**Supported Element Types:**

*   Images
*   Videos
*   Shapes
*   Graphic blocks

Before applying a filter or effect programmatically, you can verify support by checking the element type.

## Custom Filters and LUTs[#](#custom-filters-and-luts)

CE.SDK supports creating **custom filters** to meet specific visual requirements.

One powerful method of creating a custom filter is by using a **LUT (Lookup Table)**:

*   A LUT is a preset map that transforms input colors to output colors, allowing for sophisticated color grading.
*   By importing a custom LUT, you can apply unique color styles across your designs consistently.
*   LUTs are especially useful for achieving cinematic tones, brand color consistency, or specific visual moods.

You can create your own LUT files externally and integrate them into CE.SDK, giving you full control over the look and feel of your projects.

---



[Source](https:/img.ly/docs/cesdk/sveltekit/filters-and-effects/gradients-0ff079)