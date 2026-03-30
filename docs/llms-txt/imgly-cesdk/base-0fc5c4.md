# Source: https://img.ly/docs/cesdk/android/animation/create/base-0fc5c4/

---
title: "Base Animations"
description: "Apply movement, scaling, rotation, or opacity changes to elements using timeline-based keyframes."
platform: android
url: "https://img.ly/docs/cesdk/android/animation/create/base-0fc5c4/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Animation](https://img.ly/docs/cesdk/android/animation-ce900c/) > [Create Animations](https://img.ly/docs/cesdk/android/animation/create-15cf50/) > [Base Animations](https://img.ly/docs/cesdk/android/animation/create/base-0fc5c4/)

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

CreativeEditor SDK supports many different types of configurable animations for animating the appearance of design blocks in video scenes.

Similarly to blocks, each animation object has a numeric id which can be used to query and [modify its properties](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/).

## Accessing Animation APIs

In order to query whether a block supports animations, you should call the `fun supportsAnimation(block: DesignBlock): Boolean` API.

```kotlin highlight-supportsAnimation
if (!engine.block.supportsAnimation(block)) {
    engine.stop()
    return@launch
}
```

## Animation Categories

There are three different categories of animations: *In*, *Out* and *Loop* animations.

### In Animations

*In* animations animate a block for a specified duration after the block first appears in the scene.
For example, if a block has a time offset of 4s in the scene and it has an *In* animation with a duration of 1s, then the appearance of the block will be animated between 4s and 5s with the *In* animation.

### Out Animations

*Out* animations animate a block for a specified duration before the block disappears from the scene.
For example, if a block has a time offset of 4s in the scene and a duration of 5s and it has an *Out* animation with a duration of 1s, then the appearance of the block will be animated between 8s and 9s with the *Out* animation.

### Loop Animations

*Loop* animations animate a block for the total duration that the block is visible in the scene. *Loop* animations also run simultaneously with *In* and *Out* animations, if those are present.

## Creating Animations

In order to create a new animation, we must call the `fun createAnimation(type: AnimationType): DesignBlock` API.

All `AnimationType` implementations below are nested in `AnimationType` sealed class.
We currently support the following *In* and *Out* animation types:

- `Slide - "//ly.img.ubq/animation/slide"`
- `Pan - "//ly.img.ubq/animation/pan"`
- `Fade - "//ly.img.ubq/animation/fade"`
- `Blur - "//ly.img.ubq/animation/blur"`
- `Grow - "//ly.img.ubq/animation/grow"`
- `Zoom - "//ly.img.ubq/animation/zoom"`
- `Pop - "//ly.img.ubq/animation/pop"`
- `Wipe - "//ly.img.ubq/animation/wipe"`
- `Baseline - "//ly.img.ubq/animation/baseline"`
- `CropZoom - "//ly.img.ubq/animation/crop_zoom"`
- `Spin - "//ly.img.ubq/animation/spin"`
- `KenBurns - "//ly.img.ubq/animation/ken_burns"`
- `TypewriterText - "//ly.img.ubq/animation/typewriter_text"` // text-ony
- `BlockSwipeText - "//ly.img.ubq/animation/block_swipe_text"` // text-ony
- `SpreadText - "//ly.img.ubq/animation/spread_text"` // text-only
- `MergeText - "//ly.img.ubq/animation/merge_text"` // text-only

and the following *Loop* animation types:

- `SpinLoop - "//ly.img.ubq/animation/spin_loop"`
- `FadeLoop - "//ly.img.ubq/animation/fade_loop"`
- `BlurLoop - "//ly.img.ubq/animation/blur_loop"`
- `PulsatingLoop - "//ly.img.ubq/animation/pulsating_loop"`
- `BreathingLoop - "//ly.img.ubq/animation/breathing_loop"`
- `JumpLoop - "//ly.img.ubq/animation/jump_loop"`
- `SqueezeLoop - "//ly.img.ubq/animation/squeeze_loop"`
- `SwayLoop - "//ly.img.ubq/animation/sway_loop"`

```kotlin highlight-createAnimation
val slideInAnimation = engine.block.createAnimation(AnimationType.Slide)
val breathingLoopAnimation = engine.block.createAnimation(AnimationType.BreathingLoop)
val fadeOutAnimation = engine.block.createAnimation(AnimationType.Fade)
```

## Assigning Animations

In order to assign an *In* animation to the block, call the `fun setInAnimation(block: DesignBlock, animation: DesignBlock)` API.

```kotlin highlight-setInAnimation
engine.block.setInAnimation(block, slideInAnimation)
```

In order to assign a *Loop* animation to the block, call the `fun setLoopAnimation(block: DesignBlock, animation: DesignBlock)` API.

```kotlin highlight-setLoopAnimation
engine.block.setLoopAnimation(block, breathingLoopAnimation)
```

In order to assign an *Out* animation to the block, call the `fun setOutAnimation(block: DesignBlock, animation: DesignBlock)` API.

```kotlin highlight-setOutAnimation
engine.block.setOutAnimation(block, fadeOutAnimation)
```

To query the current animation ids of a design block, call the `fun getInAnimation(block: DesignBlock): DesignBlock`, `fun getLoopAnimation(block: DesignBlock): DesignBlock` or `fun getInAnimation(block: DesignBlock): DesignBlock` API.
You can now pass the returned animation `DesignBlock` into other APIs in order to query more information about the animation,
e.g. its type via the `fun getType(block: DesignBlock): String` API.
In case the design block does not have animation, query will return an invalid design block. Make sure to check for `fun isValid(block: DesignBlock): Boolean` before running any API's on the animation design block.

```kotlin highlight-getAnimation
val animation = engine.block.getLoopAnimation(block)
val animationType = engine.block.getType(animation)
```

When replacing the animation of a design block, remember to destroy the previous animation object if you don't
intend to use it any further. Animation objects that are not attached to a design block will never be automatically destroyed.

Destroying a design block will also destroy all of its attached animations.

```kotlin highlight-replaceAnimation
val squeezeLoopAnimation = engine.block.createAnimation(AnimationType.SqueezeLoop)
engine.block.destroy(engine.block.getLoopAnimation(block))
engine.block.setLoopAnimation(block, squeezeLoopAnimation)
// The following line would also destroy all currently attached animations
// engine.block.destroy(block)
```

## Animation Properties

Just like design blocks, animations with different types have different properties that you can query and modify via the API. Use `fun findAllProperties(block: DesignBlock): List<String>` in order to get a list of all properties of a given animation.

For the slide animation in this example, the call would return
`["name", "animation/slide/direction", "animationEasing", "includedInExport", "playback/duration", "type", "uuid"]`.

Please refer to the [API docs](https://img.ly/docs/cesdk/android/animation/types-4e5f41/) for a complete list of all available properties for each type of animation.

```kotlin highlight-getProperties
val allAnimationProperties = engine.block.findAllProperties(slideInAnimation)
```

Once we know the property keys of an animation, we can use the same APIs as for design blocks in order to modify those properties. For example, we can use `fun setFloat(block: DesignBlock, property: String, value: Float)` in order to change the direction of the slide animation to make our block slide in from the top.

```kotlin highlight-modifyProperties
engine.block.setFloat(slideInAnimation, "animation/slide/direction", 0.5F * Math.PI.toFloat())
```

All animations have a duration. For *In* and *Out* animations, the duration defines the total length of the animation as described above. For *Loop* animations, the duration defines the length of each loop cycle.

We can use the `fun setDuration(block: DesignBlock, duration: Double)` API in order to change the animation duration.

Note that changing the duration of an *In* animation will automatically adjust the duration of the *Out* animation (and vice versa) in order to avoid overlaps between the two animations.

```kotlin highlight-changeDuration
engine.block.setDuration(slideInAnimation, 0.6)
```

Some animations allow you to configure their easing behavior by choosing from a list of common easing curves. The easing controls the acceleration throughout the animation.

We can use the `fun setEnum(block: DesignBlock, property: String, value: String)` API in order to change the easing curve. Call `engine.block.getEnumValues("animationEasing")` in order to get a list of currently supported easing options.

In this example, we set the easing to `EaseOut` so that the animation starts fast and then slows down towards the end. An `EaseIn` easing would start slow and then speed up, while `EaseInOut` starts slow, speeds up towards the middle of the animation and then slows down towards the end again.

```kotlin highlight-changeEasing
engine.block.setEnum(slideInAnimation, "animationEasing", "EaseOut")
println("Available easing options: ${engine.block.getEnumValues("animationEasing")}")
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

    engine.stop()
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
