# Source: https://img.ly/docs/cesdk/android/animation/create/text-d6f4aa/

---
title: "Text Animations"
description: "Animate text elements with effects like fade, typewriter, and bounce for dynamic visual presentation."
platform: android
url: "https://img.ly/docs/cesdk/android/animation/create/text-d6f4aa/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Animation](https://img.ly/docs/cesdk/android/animation-ce900c/) > [Create Animations](https://img.ly/docs/cesdk/android/animation/create-15cf50/) > [Text Animations](https://img.ly/docs/cesdk/android/animation/create/text-d6f4aa/)

---

```kotlin file=@cesdk_android_examples/engine-guides-using-animations/UsingAnimations.kt reference-only
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.AnimationType
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType
import ly.img.engine.SizeMode

fun usingAnimations(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)

    val scene = engine.scene.createForVideo()

    val page = engine.block.create(DesignBlockType.Page)
    engine.block.setWidth(page, value = 800F)
    engine.block.setHeight(page, value = 600F)
    engine.block.appendChild(parent = scene, child = page)

    engine.scene.zoomToBlock(
        page,
        paddingLeft = 40F,
        paddingTop = 40F,
        paddingRight = 40F,
        paddingBottom = 40F,
    )

    val block = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(block, shape = engine.block.createShape(ShapeType.Rect))
    engine.block.setPositionX(block, value = 100F)
    engine.block.setPositionY(block, value = 50F)
    engine.block.setWidth(block, value = 300F)
    engine.block.setHeight(block, value = 300F)
    engine.block.appendChild(parent = page, child = block)
    val fill = engine.block.createFill(FillType.Image)
    engine.block.setString(
        block = fill,
        property = "fill/image/imageFileURI",
        value = "https://img.ly/static/ubq_samples/sample_1.jpg",
    )
    engine.block.setFill(block, fill = fill)

    if (!engine.block.supportsAnimation(block)) {
        engine.stop()
        return@launch
    }

    val slideInAnimation = engine.block.createAnimation(AnimationType.Slide)
    val breathingLoopAnimation = engine.block.createAnimation(AnimationType.BreathingLoop)
    val fadeOutAnimation = engine.block.createAnimation(AnimationType.Fade)
    engine.block.setInAnimation(block, slideInAnimation)
    engine.block.setLoopAnimation(block, breathingLoopAnimation)
    engine.block.setOutAnimation(block, fadeOutAnimation)
    val animation = engine.block.getLoopAnimation(block)
    val animationType = engine.block.getType(animation)

    val squeezeLoopAnimation = engine.block.createAnimation(AnimationType.SqueezeLoop)
    engine.block.destroy(engine.block.getLoopAnimation(block))
    engine.block.setLoopAnimation(block, squeezeLoopAnimation)
    // The following line would also destroy all currently attached animations
    // engine.block.destroy(block)

    val allAnimationProperties = engine.block.findAllProperties(slideInAnimation)
    engine.block.setFloat(slideInAnimation, "animation/slide/direction", 0.5F * Math.PI.toFloat())
    engine.block.setDuration(slideInAnimation, 0.6)
    engine.block.setEnum(slideInAnimation, "animationEasing", "EaseOut")
    println("Available easing options: ${engine.block.getEnumValues("animationEasing")}")

    val text = engine.block.create(DesignBlockType.Text)
    val textAnimation = engine.block.createAnimation(AnimationType.Baseline)
    engine.block.setInAnimation(text, textAnimation)
    engine.block.appendChild(page, text)
    engine.block.setPositionX(text, 100F)
    engine.block.setPositionY(text, 100F)
    engine.block.setWidthMode(text, SizeMode.AUTO)
    engine.block.setHeightMode(text, SizeMode.AUTO)
    engine.block.replaceText(text, "You can animate text\nline by line,\nword by word,\nor character by character\nwith CE.SDK")
    engine.block.setEnum(textAnimation, "textAnimationWritingStyle", "Word")
    engine.block.setDuration(textAnimation, 2.0)
    engine.block.setEnum(textAnimation, "animationEasing", "EaseOut")

    val text2 = engine.block.create(DesignBlockType.Text)
    val textAnimation2 = engine.block.createAnimation(AnimationType.Pan)
    engine.block.setInAnimation(text2, textAnimation2)
    engine.block.appendChild(page, text2)
    engine.block.setPositionX(text2, 100F)
    engine.block.setPositionY(text2, 500F)
    engine.block.setWidth(text2, 500F)
    engine.block.setHeightMode(text2, SizeMode.AUTO)
    engine.block.replaceText(text2, "You can use the textAnimationOverlap property to control the overlap between text animation segments.")
    engine.block.setFloat(textAnimation2, "textAnimationOverlap", 0.4F)
    engine.block.setDuration(textAnimation2, 1.0)
    engine.block.setEnum(textAnimation2, "animationEasing", "EaseOut")

    engine.stop()
}
```

When applied to text blocks, some animations allow you to control whether the animation should be applied to the entire text at once, line by line, word by word or character by character.

We can use the `fun setEnum(block: DesignBlock, property: String, value: String)` API in order to change the text writing style. Call `engine.block.getEnumValues("textAnimationWritingStyle")` in order to get a list of currently supported text writing style options. The default writing style is `Line`.

In this example, we set the easing to `Word` so that the text animates in one word at a time.

```kotlin highlight-textAnimationWritingStyle
val text = engine.block.create(DesignBlockType.Text)
val textAnimation = engine.block.createAnimation(AnimationType.Baseline)
engine.block.setInAnimation(text, textAnimation)
engine.block.appendChild(page, text)
engine.block.setPositionX(text, 100F)
engine.block.setPositionY(text, 100F)
engine.block.setWidthMode(text, SizeMode.AUTO)
engine.block.setHeightMode(text, SizeMode.AUTO)
engine.block.replaceText(text, "You can animate text\nline by line,\nword by word,\nor character by character\nwith CE.SDK")
engine.block.setEnum(textAnimation, "textAnimationWritingStyle", "Word")
engine.block.setDuration(textAnimation, 2.0)
engine.block.setEnum(textAnimation, "animationEasing", "EaseOut")
```

Together with the writing style, you can also configure the overlap between the individual segments of a text animation using the `textAnimationOverlap` property.

With an overlap value of `0`, the next segment only starts its animation once the previous segment's animation has finished. With an overlap value of `1`, all segments animate at the same time.

```kotlin highlight-textAnimationOverlap
val text2 = engine.block.create(DesignBlockType.Text)
val textAnimation2 = engine.block.createAnimation(AnimationType.Pan)
engine.block.setInAnimation(text2, textAnimation2)
engine.block.appendChild(page, text2)
engine.block.setPositionX(text2, 100F)
engine.block.setPositionY(text2, 500F)
engine.block.setWidth(text2, 500F)
engine.block.setHeightMode(text2, SizeMode.AUTO)
engine.block.replaceText(text2, "You can use the textAnimationOverlap property to control the overlap between text animation segments.")
engine.block.setFloat(textAnimation2, "textAnimationOverlap", 0.4F)
engine.block.setDuration(textAnimation2, 1.0)
engine.block.setEnum(textAnimation2, "animationEasing", "EaseOut")
```

## Full Code

Here's the full code:

```kotlin
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.AnimationType
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType
import ly.img.engine.SizeMode

fun usingAnimations(
    license: String,
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)

    val scene = engine.scene.createForVideo()

    val page = engine.block.create(DesignBlockType.Page)
    engine.block.setWidth(page, value = 800F)
    engine.block.setHeight(page, value = 600F)
    engine.block.appendChild(parent = scene, child = page)

    engine.scene.zoomToBlock(
        page,
        paddingLeft = 40F,
        paddingTop = 40F,
        paddingRight = 40F,
        paddingBottom = 40F,
    )

    val text = engine.block.create(DesignBlockType.Text)
    val textAnimation = engine.block.createAnimation(AnimationType.Baseline)
    engine.block.setInAnimation(text, textAnimation)
    engine.block.appendChild(page, text)
    engine.block.setPositionX(text, 100F)
    engine.block.setPositionY(text, 100F)
    engine.block.setWidthMode(text, SizeMode.AUTO)
    engine.block.setHeightMode(text, SizeMode.AUTO)
    engine.block.replaceText(text, "You can animate text\nline by line,\nword by word,\nor character by character\nwith CE.SDK")
    engine.block.setEnum(textAnimation, "textAnimationWritingStyle", "Word")
    engine.block.setDuration(textAnimation, 2.0)
    engine.block.setEnum(textAnimation, "animationEasing", "EaseOut")

    val text2 = engine.block.create(DesignBlockType.Text)
    val textAnimation2 = engine.block.createAnimation(AnimationType.Pan)
    engine.block.setInAnimation(text2, textAnimation2)
    engine.block.appendChild(page, text2)
    engine.block.setPositionX(text2, 100F)
    engine.block.setPositionY(text2, 500F)
    engine.block.setWidth(text2, 500F)
    engine.block.setHeightMode(text2, SizeMode.AUTO)
    engine.block.replaceText(text2, "You can use the textAnimationOverlap property to control the overlap between text animation segments.")
    engine.block.setFloat(textAnimation2, "textAnimationOverlap", 0.4F)
    engine.block.setDuration(textAnimation2, 1.0)
    engine.block.setEnum(textAnimation2, "animationEasing", "EaseOut")

    engine.stop()
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
