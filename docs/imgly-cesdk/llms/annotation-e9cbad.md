# Source: https://img.ly/docs/cesdk/android/edit-video/annotation-e9cbad/

---
title: "Annotation in Android (Kotlin)"
description: "Add timed text, shapes, and highlights to videos programmatically in Android using Kotlin."
platform: android
url: "https://img.ly/docs/cesdk/android/edit-video/annotation-e9cbad/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Edit Videos](https://img.ly/docs/cesdk/android/create-video-c41a08/) > [Annotation](https://img.ly/docs/cesdk/android/edit-video/annotation-e9cbad/)

---

Annotations are on-screen callouts:

- text notes
- shapes
- highlights
- icons

that appear at precise moments in your video. With CE.SDK you can **create, update, and remove overlays programmatically** when building your Android interface. This guide shows how to add timed annotations to video scenes using Kotlin.

## What You'll Learn

- Add text and shape annotations to a video scene.
- Control **when** annotations appear with `timeOffset` and `duration`.
- Read and set the **current playback time** to sync your UI.
- Detect whether an annotation is **visible at the current time** and jump the playhead.
- Build annotation UI with coroutines and Flow.

## When to Use It

Use annotations for tutorials, sports analysis, education, product demos, and any workflow where viewers should notice specific moments without scrubbing manually.

> **Note:** When creating scenes and pages programmatically, set `width = 1080F` and `height = 1920F` to match standard video dimensions. Otherwise, text or video clips may appear oddly sized relative to the canvas.

## Add a Text Annotation

The following code:

- Creates a text block.
- Positions it.
- Makes it visible from 5–10 seconds on the timeline.

The code is the same as for any other block except for the addition of `timeOffset` and `duration` properties.

```kotlin
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.SizeMode

fun addTextAnnotation(engine: Engine, page: Int): Int {
    val text = engine.block.create(DesignBlockType.Text)
    engine.block.replaceText(text, text = "Watch this part!")
    engine.block.setTextFontSize(text, fontSize = 32F)
    
    // Auto-size + place it visibly
    engine.block.setWidthMode(text, mode = SizeMode.AUTO)
    engine.block.setHeightMode(text, mode = SizeMode.AUTO)
    engine.block.setPositionX(text, value = 160F)
    engine.block.setPositionY(text, value = 560F)
    
    // Timeline: show between 5s and 10s
    engine.block.setTimeOffset(text, offset = 5.0)
    engine.block.setDuration(text, duration = 5.0)
    
    engine.block.appendChild(parent = page, child = text)
    return text
}
```

Any visual block (text, shapes, stickers) can serve as an annotation. Time properties control when it's active on the page timeline.

## Add a Shape Annotation

Use a graphic block with a vector shape for pointers or highlights.

```kotlin
import ly.img.engine.Color
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType

fun addStarAnnotation(engine: Engine, page: Int): Int {
    val star = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(star, shape = engine.block.createShape(ShapeType.Star))
    val fill = engine.block.createFill(FillType.Color)
    engine.block.setColor(
        fill,
        property = "fill/color/value",
        color = Color.fromRGBA(r = 1F, g = 0F, b = 0F, a = 1F)
    )
    engine.block.setFill(star, fill = fill)
    
    engine.block.setPositionX(star, value = 320F)
    engine.block.setPositionY(star, value = 420F)
    engine.block.setTimeOffset(star, offset = 12.0)
    engine.block.setDuration(star, duration = 4.0)
    
    engine.block.appendChild(parent = page, child = star)
    return star
}
```

## Timeline Sync: React to Playback & Highlight Active Annotations

Below is a Kotlin pattern using coroutines and Flow to keep your UI in sync with the timeline. It:

1. Retrieves the current page's playback time on an interval.
2. Marks an annotation as **active** when it's visible at that time.
3. Lets you **seek** the playhead to an annotation's start time.

```kotlin
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.Job
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch
import ly.img.engine.Engine

class TimelineSync(
    private val engine: Engine,
    private val page: Int
) {
    private val _currentTime = MutableStateFlow(0.0)
    val currentTime: StateFlow<Double> = _currentTime.asStateFlow()
    
    private val _activeAnnotation = MutableStateFlow<Int?>(null)
    val activeAnnotation: StateFlow<Int?> = _activeAnnotation.asStateFlow()
    
    private var pollingJob: Job? = null
    
    fun start(annotations: List<Int>, scope: CoroutineScope = CoroutineScope(Dispatchers.Main)) {
        pollingJob?.cancel()
        pollingJob = scope.launch {
            while (true) {
                // 1) Read the page's current playback time
                val time = engine.block.getPlaybackTime(page)
                _currentTime.value = time
                
                // 2) Determine which annotation is currently visible
                var foundActive: Int? = null
                for (id in annotations) {
                    if (engine.block.isVisibleAtCurrentPlaybackTime(id)) {
                        foundActive = id
                        break
                    }
                }
                _activeAnnotation.value = foundActive
                
                // Poll at ~5 fps (200ms)
                delay(200)
            }
        }
    }
    
    fun stop() {
        pollingJob?.cancel()
        pollingJob = null
    }
    
    fun seek(toSeconds: Double) {
        engine.block.setPlaybackTime(page, time = toSeconds)
    }
}
```

> **Note:** * Use a modest polling rate, start with 5–10 Hz (100-200ms delay). It keeps UI responsive.
> * For tighter coupling, combine this with the SDK's event subscriptions elsewhere in your app.

**Wire it into your UI (Jetpack Compose example)**:

```kotlin
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import ly.img.engine.Engine

@Composable
fun AnnotationListView(
    sync: TimelineSync,
    engine: Engine,
    annotations: List<Int>
) {
    val activeAnnotation by sync.activeAnnotation.collectAsState()
    
    DisposableEffect(Unit) {
        sync.start(annotations)
        onDispose { sync.stop() }
    }
    
    LazyColumn {
        items(annotations) { id ->
            val isActive = (activeAnnotation == id)
            Row(
                modifier = Modifier
                    .padding(8.dp)
                    .clickable {
                        // Seek to this annotation's start
                        val start = engine.block.getTimeOffset(id)
                        sync.seek(start)
                    },
                verticalAlignment = Alignment.CenterVertically
            ) {
                Surface(
                    modifier = Modifier.padding(end = 8.dp),
                    shape = CircleShape,
                    color = if (isActive) Color.Red else Color.Gray
                ) {
                    Box(
                        modifier = Modifier.padding(4.dp)
                    )
                }
                Text(
                    text = "Annotation $id",
                    color = if (isActive) Color.Black else Color.Gray
                )
            }
        }
    }
}
```

The list:

- Highlights active annotations with a red indicator
- Jumps the playhead when you tap an annotation.

This example doesn't include:

- The main UI
- The video clips
- Playback controls.

## Controlling Playback (Play/Pause, Loop)

You can perform actions such as:

- Play/pause the page timeline
- Set looping
- Play solo playback for a single block when previewing.

```kotlin
import ly.img.engine.Engine

fun play(engine: Engine, page: Int) {
    engine.block.setPlaying(page, enabled = true)
}

fun pause(engine: Engine, page: Int) {
    engine.block.setPlaying(page, enabled = false)
}

fun setLooping(engine: Engine, blockId: Int, enabled: Boolean) {
    engine.block.setLooping(blockId, looping = enabled)
}

fun isPlaying(engine: Engine, page: Int): Boolean {
    return engine.block.isPlaying(page)
}
```

## Edit & Remove Annotations

Following code shows the functions for:

- Updating text
- Moving an annotation
- Deleting an annotation entirely.

```kotlin
import ly.img.engine.Engine

fun updateAnnotationText(engine: Engine, annotationId: Int, newText: String) {
    engine.block.replaceText(annotationId, text = newText)
}

fun moveAnnotation(engine: Engine, annotationId: Int, x: Float, y: Float) {
    engine.block.setPositionX(annotationId, value = x)
    engine.block.setPositionY(annotationId, value = y)
}

fun removeAnnotation(engine: Engine, annotationId: Int) {
    engine.block.destroy(annotationId)
}
```

## Complete Example

Here's a complete example that creates a video scene with multiple annotations:

```kotlin
import android.content.Context
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.Color
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType
import ly.img.engine.SizeMode

fun createVideoWithAnnotations(
    context: Context,
    license: String,
    userId: String
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.annotations")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)
    
    try {
        // Create video scene
        val scene = engine.scene.createForVideo()
        val page = engine.block.create(DesignBlockType.Page)
        engine.block.appendChild(parent = scene, child = page)
        engine.block.setWidth(page, value = 1080F)
        engine.block.setHeight(page, value = 1920F)
        engine.block.setDuration(page, duration = 30.0)
        
        // Add video track
        val track = engine.block.create(DesignBlockType.Track)
        engine.block.appendChild(parent = page, child = track)
        
        // Add video clip
        val videoBlock = engine.block.create(DesignBlockType.Graphic)
        engine.block.setShape(videoBlock, shape = engine.block.createShape(ShapeType.Rect))
        val videoFill = engine.block.createFill(FillType.Video)
        engine.block.setString(
            block = videoFill,
            property = "fill/video/fileURI",
            value = "https://cdn.img.ly/assets/demo/v1/ly.img.video/videos/pexels-drone-footage-of-a-surfer-barrelling-a-wave-12715991.mp4"
        )
        engine.block.setFill(videoBlock, fill = videoFill)
        engine.block.appendChild(parent = track, child = videoBlock)
        engine.block.fillParent(track)
        
        // Add annotation 1: Intro text (0-5 seconds)
        val introText = engine.block.create(DesignBlockType.Text)
        engine.block.replaceText(introText, text = "Welcome!")
        engine.block.setTextFontSize(introText, fontSize = 48F)
        engine.block.setWidthMode(introText, mode = SizeMode.AUTO)
        engine.block.setHeightMode(introText, mode = SizeMode.AUTO)
        engine.block.setPositionX(introText, value = 100F)
        engine.block.setPositionY(introText, value = 100F)
        engine.block.setTimeOffset(introText, offset = 0.0)
        engine.block.setDuration(introText, duration = 5.0)
        engine.block.appendChild(parent = page, child = introText)
        
        // Add annotation 2: Highlight shape (5-10 seconds)
        val star = engine.block.create(DesignBlockType.Graphic)
        engine.block.setShape(star, shape = engine.block.createShape(ShapeType.Star))
        val starFill = engine.block.createFill(FillType.Color)
        engine.block.setColor(
            starFill,
            property = "fill/color/value",
            color = Color.fromRGBA(r = 1F, g = 0.84F, b = 0F, a = 1F) // Gold
        )
        engine.block.setFill(star, fill = starFill)
        engine.block.setPositionX(star, value = 400F)
        engine.block.setPositionY(star, value = 300F)
        engine.block.setWidth(star, value = 100F)
        engine.block.setHeight(star, value = 100F)
        engine.block.setTimeOffset(star, offset = 5.0)
        engine.block.setDuration(star, duration = 5.0)
        engine.block.appendChild(parent = page, child = star)
        
        // Add annotation 3: Detail text (10-15 seconds)
        val detailText = engine.block.create(DesignBlockType.Text)
        engine.block.replaceText(detailText, text = "Check this out! 👀")
        engine.block.setTextFontSize(detailText, fontSize = 32F)
        engine.block.setWidthMode(detailText, mode = SizeMode.AUTO)
        engine.block.setHeightMode(detailText, mode = SizeMode.AUTO)
        engine.block.setPositionX(detailText, value = 100F)
        engine.block.setPositionY(detailText, value = 800F)
        engine.block.setTimeOffset(detailText, offset = 10.0)
        engine.block.setDuration(detailText, duration = 5.0)
        engine.block.appendChild(parent = page, child = detailText)
        
        // Start playback
        engine.block.setPlaying(page, enabled = true)
        
        println("Video with annotations created successfully!")
        println("Total annotations: 3")
        println("Video duration: ${engine.block.getDuration(page)}s")
        
    } finally {
        // Note: Don't stop the engine here if you want to keep using it
        // engine.stop()
    }
}
```

## Design Tips (Quick Wins)

- **Readable contrast:** Light text over dark video (or add a translucent background for the text block).
- **Consistent rhythm:** Align callout durations to beats/phrases; use 2–5s for most labels.
- **Safe zones:** Keep annotations away from edges (device notches, social crop areas). Pair with your existing Rules/Scopes.
- **Hierarchy:** Title (bolder), detail (smaller). Reserve color for emphasis.
- **Motion restraint:** Prefer fades and basic transforms over heavy effects for legibility.

## Testing & QA Checklist

- **Device playback:** Verify on physical devices; long H.265 exports may differ from emulator previews.
- **Performance:** Poll timeline at ~5–10 Hz for UI sync; avoid tight loops.
- **Edge timing:** Test annotations starting at `0.0` and ending at page duration; confirm no off-by-one visibility.
- **Layer order:** Ensure annotations render above background clips; append after media or bring to front when needed.
- **Export parity:** Compare in-app preview vs `.mp4` export for small text and any blurs.

## Troubleshooting

**❌ Annotation doesn't show up**:

- Confirm you appended it to the **page** (or a track on the page).
- Ensure its `timeOffset`/`duration` place it within the page's total duration.
- If hidden behind media, append it **after** the background or bring to front using layer management.

**❌ Jumps don't seem to work**:

- Seek on the **page** block with `setPlaybackTime(page, time)`, not on the annotation itself.
- Verify the page supports playback time with `engine.block.supportsPlaybackTime(page)`.

**❌ Performance stutters**:

- Poll the timeline at 5–10 Hz (100-200ms delay). Avoid tight loops.
- Use coroutines with proper dispatchers (Dispatchers.Main for UI updates).

**❌ Exported video looks different**:

- Make sure the scene mode is **Video** and the page duration property has the correct value.
- Long blurs/glows may differ depending on codec settings.

## Next Steps

Now that you've explored annotation basics, these topics can deepen your understanding:

- [Add Captions & Subtitles](https://img.ly/docs/cesdk/android/edit-video/add-captions-f67565/) to your clips.
- [Variables for Dynamic Labels](https://img.ly/docs/cesdk/android/create-templates/add-dynamic-content/text-variables-7ecb50/) for displaying information like usernames or scores.
- [Control Audio and Video](https://img.ly/docs/cesdk/android/create-video/control-daba54/) for advanced playback control.
- [Timeline Editor](https://img.ly/docs/cesdk/android/create-video/timeline-editor-912252/) for creating multi-track video compositions.



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
