# Source: https://img.ly/docs/cesdk/android/filters-and-effects/chroma-key-green-screen-1e3e99/

---
title: "Chroma Key (Green Screen) in Android (Kotlin)"
description: "Use CE.SDK's green/blue screen keyer to replace backgrounds, tune edges & spill, and composite subjects over virtual scenes."
platform: android
url: "https://img.ly/docs/cesdk/android/filters-and-effects/chroma-key-green-screen-1e3e99/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Filters and Effects](https://img.ly/docs/cesdk/android/filters-and-effects-6f88ac/) > [Apply Chroma Key (Green Screen)](https://img.ly/docs/cesdk/android/filters-and-effects/chroma-key-green-screen-1e3e99/)

---

Chroma keying removes a uniform background color (often green or blue) from a video or image so you can composite the foreground over a new scene. In CE.SDK for Android, chroma keying is an **effect** you attach to an image or video block, with parameters for **color selection**, **similarity threshold**, **edge smoothing**, and **spill suppression**. This guide walks you through applying the effect in Kotlin, dialing it in for clean edges, and composing the keyed result with a replacement background.

## What You'll Learn

- How to add the **Green Screen** effect to **image** and **video** blocks.
- How to set the key color (green by default, but any color works).
- How to tune **colorMatch** (similarity), **smoothness** (edge falloff), and **spill** (desaturating color cast).
- How to layer a new background behind the keyed subject.
- How to persist, export, and protect templates that include chroma key.

## When to Use It

Use chroma key when your source contains a uniform backdrop (green, blue, or a solid brand color) and you want to:

- Replace the background with a **virtual set**, branded plate, or blurred depth backdrop.
- Place talent over **slides** or **product footage**.
- Standardize a team's talking‑head videos with consistent backgrounds.
- Composite when using an asset formats such as MP4, H.264 or, JPEG that don't support transparency.

Avoid chroma key if the subject's clothing, props, or lighting contains the same hue as your key color, or if the background is highly textured.

> **Chroma Key vs. Background Removal:** The `effect/green_screen` shader operates on color similarity directly on the GPU. Unlike AI-based background removal, chroma keying provides predictable, real‑time control for studio footage where lighting and backdrop color are controlled.

## Apply the Green Screen Effect In a Prebuilt Editor

Chroma key is one of the standard effects available for images and video clips in the prebuilt editors, such as the Design Editor and the Video Editor. Use it as follows:

1. Select a key image or video clip.
2. Look for the `Effects` button in the inspector and tap it.

![Location of the Effect button in the Inspector](assets/chroma-key-ios-159-0.png)

Scroll through the effects until you find "Green Screen". Once you tap it, the effect implements immediately.

![Arrow pointing to the Green Screen effect button](assets/chroma-key-ios-159-1.png)

An options indicator appears for the effect. Tap it to show the options.

![Green screen effect button showing options indicator](assets/chroma-key-ios-159-2.png)

Use the sliders and the color wheel, to change the settings for:

- key color
- color match
- smoothness
- spill

![Effect controls for key color, color match, smoothness and, spill](assets/chroma-key-ios-159-3.png)

The "Tuning the Effect" section below explains each of these in detail.

## Apply the Green Screen Effect In Code

CE.SDK exposes chroma key as the `EffectType.GreenScreen` effect type with the following key properties:

- `effect/green_screen/fromColor` the color to key out (default green).
- `effect/green_screen/colorMatch` similarity threshold \[0…1].
- `effect/green_screen/smoothness` edge falloff \[0…1].
- `effect/green_screen/spill` desaturates remaining color spill \[0…1].

### Key an Image Block

```kotlin
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.Color
import ly.img.engine.EffectType
import ly.img.engine.Engine

fun applyGreenScreenToImage(
    engine: Engine,
    imageBlock: Int
) = CoroutineScope(Dispatchers.Main).launch {
    // 1) Create the effect and attach it to the block
    val keyer = engine.block.createEffect(type = EffectType.GreenScreen)
    engine.block.appendEffect(imageBlock, effectBlock = keyer)
    
    // 2) Choose the key color (here: pure green); any color works
    engine.block.setColor(
        keyer,
        property = "effect/green_screen/fromColor",
        color = Color.fromRGBA(r = 0.0f, g = 1.0f, b = 0.0f, a = 1.0f)
    )
    
    // 3) Tune similarity, smoothness, and spill
    engine.block.setFloat(keyer, property = "effect/green_screen/colorMatch", value = 0.40f)
    engine.block.setFloat(keyer, property = "effect/green_screen/smoothness", value = 0.08f)
    engine.block.setFloat(keyer, property = "effect/green_screen/spill", value = 0.15f)
}
```

### Key a Video Block

Video blocks use video fills instead of image fills, but the rest of the workflow is identical.

```kotlin
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.Color
import ly.img.engine.EffectType
import ly.img.engine.Engine

fun applyGreenScreenToVideo(
    engine: Engine,
    videoBlock: Int
) = CoroutineScope(Dispatchers.Main).launch {
    val keyer = engine.block.createEffect(type = EffectType.GreenScreen)
    engine.block.appendEffect(videoBlock, effectBlock = keyer)
    
    // Blue screen example
    engine.block.setColor(
        keyer,
        property = "effect/green_screen/fromColor",
        color = Color.fromRGBA(r = 0.0f, g = 0.25f, b = 1.0f, a = 1.0f)
    )
    
    engine.block.setFloat(keyer, property = "effect/green_screen/colorMatch", value = 0.35f)
    engine.block.setFloat(keyer, property = "effect/green_screen/smoothness", value = 0.10f)
    engine.block.setFloat(keyer, property = "effect/green_screen/spill", value = 0.25f)
}
```

Order matters: if you add other effects, like color adjustments, place the **keyer first** in the stack so later effects operate on the premultiplied result.

### Pick the Key Color from the Image

Hard‑coding `fromColor` works for controlled shoots. In general, sample the background color under the user's tap.

> **Note:** CE.SDK doesn't provide a built-in API to read a pixel at a screen coordinate. In your Android app, map the tap location to the image/video buffer you control and sample the pixel using APIs such as `Bitmap.getPixel()` or `Canvas`. Convert the sampled RGBA to `Color.fromRGBA()` and set `effect/green_screen/fromColor`. If you embed the `DesignEditor`, keep an app-level copy of the media to sample from, since the editor's preview is GPU-rendered.

Tie the sampled color back to the effect:

```kotlin
import ly.img.engine.Color
import ly.img.engine.Engine

fun setKeyColor(engine: Engine, keyer: Int, r: Float, g: Float, b: Float) {
    engine.block.setColor(
        keyer,
        property = "effect/green_screen/fromColor",
        color = Color.fromRGBA(r = r, g = g, b = b, a = 1.0f)
    )
}
```

For polished UIs, show a zoomed loupe and a live matte preview as the user drags.

### Composite over a Replacement Background

A keyed subject is transparent where the background was, so you **layer a background block beneath** the keyed block.

```kotlin
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType

fun addBackgroundBehind(engine: Engine, page: Int, subject: Int, imageUrl: String) {
    val bg = engine.block.create(DesignBlockType.Graphic)
    val shape = engine.block.createShape(ShapeType.Rect)
    engine.block.setShape(bg, shape = shape)
    
    val fill = engine.block.createFill(FillType.Image)
    engine.block.setString(fill, property = "fill/image/imageFileURI", value = imageUrl)
    
    engine.block.setFill(bg, fill = fill)
    
    // Make background full‑bleed on the page
    // Place background **behind** subject
    engine.block.insertChild(parent = page, child = bg, index = 0)
    engine.block.fillParent(bg)
    engine.block.sendToBack(bg)
}
```

For video, create a video fill instead of an image fill and align durations in your export.

## Tuning the Effect

The three parameters for tuning chroma key composition are:

- color match
- spill
- smoothness

Knowing what they impact can help decide your strategy when the composition doesn't look correct. The examples below all show how these values can change this chroma key image.

![Example composited image.](assets/chroma-key-ios-159-4.png)

> **Recommended Starting Values:** | Background | colorMatch | smoothness | spill |
> |-------------|-------------|------------|--------|
> | **Green Screen** | 0.35–0.45 | 0.08–0.12 | 0.15–0.25 |
> | **Blue Screen** | 0.30–0.40 | 0.10–0.15 | 0.25–0.35 |
> | **Custom Color** | 0.40–0.50 | 0.08–0.12 | 0.10–0.20 |Tune `colorMatch` first for coverage, then refine edge softness with `smoothness`, and finally correct color tint with `spill`.

### Color Match

Color Match determines how close a pixel's color has to be to the key color to be considered *background*. When the value is low, only exact matches are removed. When the value is high, a larger range of colors similar to the key color get removed.

What to watch for when the value is wrong:

- Too low: you may see patches of the green screen still visible around edges, especially if lighting is uneven or shadows present.
- Too high: you risk keying out part of the subject (hair strands, clothing edges, reflective items) creating holes or transparency because the effect is too aggressive.

![Color match range examples.](assets/color-match-range-ios.jpg)

The preceding image shows color match values of 0.0, 0.5 and 1.0.

### Smoothness

Smoothness controls how gradually or sharply the transitions occur, how soft the matte edges of the gradients are. A low value produces sharp transition between keyed and un-keyed areas. When the value is high, there is softer transition.

What to watch for when the value is wrong:

- Too low: harsh edges, visible fringes around hair or "hard cutouts" that look unnatural.
- Too high: a halo effect or the subject blends into the background.

![Smoothness range examples.](assets/smoothness-range-ios.jpg)

The preceding image shows smoothness values of 0.0, 0.5 and 1.0.

### Spill

Spill impacts the unwanted "color spill", when your key color reflects or bleeds onto the subject. This is especially noticeable around edges, hair and, shiny objects.

What to watch for when the value is wrong:

- Too low: you may see green reflection on the subject (especially edges/hair/shoulders) that doesn't get cleaned up, making it look unnatural or floating.
- Too high: the subject's actual color edges are desaturated, making hair or detail look gray, faded or too soft.

![Spill range examples.](assets/spill-range-ios.jpg)

The preceding image shows spill values of 0.0, 0.5 and 1.0.

## Lighting & Capture Tips

- Keep your backdrop evenly lit and 1–2 stops brighter than your subject.
- Avoid shadows or wrinkles. Uneven color creates transparency artifacts.
- Separate your subject from the background by at least 1 m to reduce spill.

## Template & Scope Considerations

If you ship templates that include a keyer, you might want to lock down parameters to protect quality:

- Use **Scopes/Permissions** to limit which effect properties the end‑user can change.
- Store platform‑tested defaults (match, smoothness, spill) in the template.
- Provide preset chips like **"Green Screen"**, **"Blue Screen"**, **"Brand Cyan"** to switch `fromColor` quickly.

## Performance and Rendering Pipeline

CE.SDK runs chroma keying directly on the graphics card for smooth, real-time results. Place the keyer near the start of your effect list so that later effects, like color or tone adjustments, apply correctly to the transparent areas. To keep playback fast, avoid heavy effects such as blur or LUTs before the keyer.

## Export Tips

- Prefer **ProRes 4444** (or other alpha‑carrying formats) when exporting an intermediate keyed asset to reuse elsewhere.
- For final composites, export with the background enabled and a standard delivery codec/format.

## Testing Checklist

- Verify background color is uniform and well lit.
- Check for reflective surfaces that might cause spill.
- Test both **720p** and **4K** previews to compare performance.
- Try different wardrobe colors. Avoid those close to the key color.
- Examine edges on hair or fine detail under motion.
- Validate output formats (e.g., MP4 with solid background vs. ProRes with alpha).

## Troubleshooting

**❌ Holes in the matte (background not fully removed)**:

- Increase `colorMatch` slightly. If edges get harsh, bump `smoothness` too.

**❌ Foreground punched out (you lose subject detail)**:

- Lower `colorMatch` until detail returns; then reduce `spill` if the subject appears tinted.

**❌ Green/blue color cast on edges**:

- Raise `spill` (try 0.2–0.4). If it looks gray, back it down.

**❌ Jagged edges**:

- Increase `smoothness` in small steps (0.05–0.15).
- Consider adding a light `effect/blur` **after** the keyer for video.

**❌ Uneven backgrounds / shadows**:

- Sample a darker patch of the backdrop or increase `colorMatch` and compensate with `spill`.

**❌ Nothing turns transparent:**

- Verify the effect is attached to the **right block** and not to the page.
- Check `fromColor` is close to the actual backdrop hue (sample it!).
- Ensure your block type supports effects (graphic, video are supported).

**❌ Performance drops with 4K video**:

- Avoid stacking extra heavy effects **before** the keyer.
- Render proxies or downscale the preview while tuning; export at full res.

**❌ Skin tones look dull**:

- Reduce `spill` and re‑tune `colorMatch`.

**❌ Hair/fur looks crunchy:**

- Raise `smoothness` incrementally (and consider light post‑blur).

## Next Steps

With the core of chroma key compositing mastered, here are some other topics that may be interesting:

- Learn about other [Filters & Effects](https://img.ly/docs/cesdk/android/filters-and-effects/overview-299b15/) and try combining the keyer with adjustments for color matching.



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
