# Batch Processing

This guide shows you how to use CE.SDK to create and manage batch processing workflows in the browser. Batch processing automates creative operations at scale, from enabling template population and multi-format exports, to bulk transformations and production pipelines.

In the browser, batch processing means automating the same CreativeEngine workflow while the tab stays open. Instead of the user editing/exporting items one by one, your front-end:

1.  Loops through a dataset.
2.  Produces a series of outputs.

This guides helps you understand how the CE.SDK can work in a batch process workflow.

## What You’ll Learn[#](#what-youll-learn)

*   Two different batch processing approaches:
    
    *   Sequential
    *   Parallel
*   How to batch:
    
    *   Templates population with data.
    *   Exports to different formats (PNG, JPEG, PDF, MP4).
    *   Thumbnails generation.
*   How to optimize memory usage.
    

## Batch Processing Strategies[#](#batch-processing-strategies)

You can run batch operations in two ways:

*   **Sequential:** a single engine loop.
*   **Parallel:** multiple workers spinning up.

The following examples show both approaches when running a batch export in the browser:

[

Sequential (single core)

](#tab-panel-131)[

Parallel (2 cores)

](#tab-panel-132)

```
// ... downloadBlob logic//Start the engine and download the sceneconst engine = await CreativeEngine.init({ license: LICENSE_KEY });
for (const record of records) {  await engine.scene.loadFromString(record.scene);  const blob = await engine.block.export(engine.scene.getPages()[0], 'image/png');  await downloadBlob(blob, `${record.id}.png`);}
engine.dispose();
```

1.  `CreativeEngine.init` spins up a single engine instance for the tab.
2.  The loop iterates over the `record` dataset.
3.  The Engine loads the scene.
4.  The `export` call renders the first page as a PNG blob.
5.  The code disposes of the engine to free resources.

```
const workers = [new Worker('worker.js'), new Worker('worker.js')];
await Promise.all(  records.map((record, idx) =>    workers[idx % workers.length].postMessage({ type: 'PROCESS', record })  ));
```

In this code:

1.  2 workers run in separate threads.
2.  Each worker receives a different data set.
3.  Each worker runs the heavier CreativeEngine work off the main thread.
4.  `Promise.all` waits for every worker call to finish before moving on.

The following table summarizes the pros and cons of each approach:

| Approach | When to use | Pros | Cons |
| --- | --- | --- | --- |
| **Sequential** | \- Default browser workload  
\- Small batch sizes  
\- Limited RAM on user devices | \- Lower memory footprint  
\- Simpler code path  
\- Easy cleanup | \- Slower total runtime  
\- UI can feel locked if not chunked  
 |
| **Parallel** | \- Big datasets  
Enough resources in user devices  
 | \- Higher throughput  
\- Can keep UI responsive  
 | \- More memory consumption per tab  
Coordination complexity  
\- Throttling risk |

## How To Batch Template Population[#](#how-to-batch-template-population)

For this operation, you generate personalized outputs at scale by combining:

*   Templates
*   Structured data

### Set the Data Sources[#](#set-the-data-sources)

Batch workflows can use a variety of data sources to populate a template, such as:

*   CSV files with parsing libraries
*   JSON from REST APIs
*   Databases (SQL, NoSQL)
*   Stream data

The following examples show how to set three different data sources:

[

JSON file

](#tab-panel-128)[

API

](#tab-panel-129)[

Inline JavaScript object

](#tab-panel-130)

```
await fetch('path/to/dataset.json').then((r) => r.json());
```

```
await fetch('https://api.example.com/dataset').then((r) => r.json());
```

```
// Define key variableslet textVariables = {  first_name: '',  last_name: '',  address: '',  city: '',};
```

### Update the Template[#](#update-the-template)

You can automate template population, update media, and show conditional content based on data. Find some examples in existing guides:

| Action | EngineAPI function | Related guide |
| --- | --- | --- |
| Set text variables | `engine.variable.setString(variableId, value)` | [Text Variables](vue/create-templates/add-dynamic-content/text-variables-7ecb50/) |
| Update image fills | `engine.block.setString(block, 'fill/image/imageFileURI', url)` | [Insert Images](vue/insert-media/images-63848a/) |
| Edit block properties | `engine.block.setFloat(block, key, value)` / `engine.block.setColor(block, key, color)` | [Apply Effects](vue/filters-and-effects/apply-2764e4/) |

### Batch Export the Design[#](#batch-export-the-design)

The CE.SDK provides a set of format options when exporting the edited designs:

| Format | EngineAPI function | Related guide |
| --- | --- | --- |
| PNG | `engine.block.export(block, 'image/png')` | [PNG](vue/export-save-publish/export/to-png-f87eaf/) |
| JPEG | `engine.block.export(block, 'image/jpeg', 0.95)` | [JPEG](vue/export-save-publish/export/to-jpeg-6f88e9/) |
| PDF | `engine.block.export(block, 'application/pdf')` | [PDF](vue/export-save-publish/export/to-pdf-95e04b/) |
| MP4 | `engine.block.exportVideo(block, MimeType.Mp4)` | [MP4](vue/export-save-publish/export/to-mp4-c998a8/) |

Check all the export options in the [Export section](vue/export-save-publish/export/overview-9ed3a8/) .

### Batch Thumbnail Generation from Static Scenes[#](#batch-thumbnail-generation-from-static-scenes)

The export feature allows you to automate thumbnails generation by tweaking the format and the size of the design, for example:

```
// Example: Real-time thumbnail generationconst thumbnailEngine = await CreativeEngine.init({ container: null });
async function generateThumbnail(sceneData) {  await thumbnailEngine.scene.loadFromString(sceneData);  const page = thumbnailEngine.scene.getPages()[0];
  // Generate small preview  const thumbnail = await thumbnailEngine.block.export(page, 'image/jpeg', {    targetWidth: 200,    targetHeight: 200,    quality: 0.7,  });
  return thumbnail;}
```

Read more about thumbnails generation in [the Engine guide](vue/engine-interface-6fb7cf/) .

The CE.SDK also provides over 20 pre-designed text layouts to apply on thumbnails. Check the [relevant guide](vue/text/font-combinations-a1b2c3/) to use them.

### Batch Thumbnail Generation from Video Scenes[#](#batch-thumbnail-generation-from-video-scenes)

Extract representative frames from videos efficiently, and automate this action using the dedicated CE.SDK features:

| Action | EngineAPI function | Related guide |
| --- | --- | --- |
| Load video source | `engine.scene.createFromVideo()` | [Create from Video](vue/create-video/control-daba54/) |
| Seek to timestamp | `engine.block.setPlaybackTime()` | [Control Audio and Video](vue/create-video/control-daba54/) |
| Export single frame | `engine.block.export(block, options)` | [To PNG](vue/export-save-publish/export/to-png-f87eaf/)  
[Font Combinations](vue/text/font-combinations-a1b2c3/) |
| Generate sequence thumbnails | `engine.block.generateVideoThumbnailSequence()` | [Trim Video Clips](vue/edit-video/trim-4f688b/) |
| Size thumbnails consistently | `targetWidth / targetHeight` export options | [To PNG](vue/export-save-publish/export/to-png-f87eaf/) |

The following code shows how to **generate thumbnails from a video**:

```
import CreativeEngine from '@cesdk/engine';
const engine = await CreativeEngine.init({ license: LICENSE_KEY });await engine.scene.loadFromURL('/assets/video-scene.scene');
const [page] = engine.scene.getPages();const videoBlock = engine.block  .getChildren(page)  .find((child) => engine.block.getType(child) === 'video');
if (videoBlock) {  const videoFill = engine.block.getFill(videoBlock);  await engine.block.setPlaybackTime(videoFill, 4.2);
  const thumbnail = await engine.block.export(page, {    mimeType: 'image/png',    targetWidth: 640,    targetHeight: 360  });
  await downloadBlob(thumbnail, 'scene-thumb.png');}
engine.dispose();
```

The preceding code:

1.  Loads a scene containing a video.
2.  Seeks to 4.2 s.
3.  Exports the page as a PNG.
4.  Saves the thumbnail.

## Optimize Memory Usage[#](#optimize-memory-usage)

Every export produces and accumulates:

*   Blobs
*   URLs
*   Engine state

Proper **cleanup** ensures batch processes complete without resource exhaustion. Without proper cleanup, the browser might:

*   Hits memory ceiling.
*   Crash.
*   Slow down.

Consider the following actions to **avoid exhausting the client**:

| Strategy | Code |
| --- | --- |
| Revoke blob URLs immediately after use | `URL.revokeObjectURL()` |
| Dispose engine instances when finished | `engine.dispose()` |
| Chunk large datasets into smaller batches |  |
| Consider garbage collection timing |  |

Treat cleanup as part of **each loop** iteration, by either:

*   Freeing resources **after each item**.
*   Chunking resources, by loading smaller parts of your datasets at a time.

To **handle large batches**, consider the following workflows:

*   Split into smaller chunks.
*   Log progress.
*   Monitor status.

## Apply Error Handling[#](#apply-error-handling)

Batch runs often work with **large records of data**. Some factors can make the job crash, such as:

*   A malformed asset
*   Timeouts

When your job encounters one of these errors, you can proactively **avoid the job’s failure** using the following patterns:

*   Catch errors inside each loop iteration.
*   Log failing records so you can retry them later.
*   Decide whether to keep going or stop when an error happens.
*   Collect a summary of all failures for post-run review.

For example, the preceding code to generate thumbnails now handles errors gracefully to avoid crashes:

```
import CreativeEngine from '@cesdk/engine';
let engine;try {  engine = await CreativeEngine.init({ license: LICENSE_KEY });  await engine.scene.loadFromURL('/assets/video-scene.scene');
  const [page] = engine.scene.getPages();  if (!page) throw new Error('Scene has no pages.');
  const videoBlock = engine.block    .getChildren(page)    .find((child) => engine.block.getType(child) === 'video');  if (!videoBlock) throw new Error('No video block found.');
  const videoFill = engine.block.getFill(videoBlock);  if (!videoFill) throw new Error('Video block is missing its fill.');
  await engine.block.setPlaybackTime(videoFill, 4.2);
  const thumbnail = await engine.block.export(page, {    mimeType: 'image/png',    targetWidth: 640,    targetHeight: 360  });
  await downloadBlob(thumbnail, 'scene-thumb.png');} catch (error) {  console.error('Failed to generate thumbnail', error);} finally {  engine?.dispose();}
```

### Use Retry Logic[#](#use-retry-logic)

Some errors are temporary due to factors such as:

*   Network hiccup
*   Rate limits
*   Busy CDN

To avoid saturating the related service, you can use smart retries after a short delay. If the error persist:

1.  Double the delay.
2.  Retry
3.  Double again the delay exponentially after each retry.

This strategy allows you to identify temporary failures that could be resolved later.

For **API failures**, consider using circuit breaking patterns that:

*   Pause the calls on repeated errors.
*   Test again after a delay.

### Check the Input Data Before Processing[#](#check-the-input-data-before-processing)

Lightweight checks can help you with:

*   Catching bad inputs early.
*   Preventing waste of time and compute on batches that’ll fail.

Add checks **before**:

*   Launching the CE.SDK.
*   Loading scenes.
*   Exporting large scenes.

The following table contains some checks **examples**:

| Check | Example |
| --- | --- |
| Check input data structure | `if (!isValidRecord(record)) throw new Error('Invalid payload');` |
| Check file existence and accessibility | `await fs.promises.access(filePath, fs.constants.R_OK);` |
| Verify templates load correctly | `await engine.scene.loadFromURL(templateUrl);` |
| Use dry-run mode for testing | `if (options.dryRun) return simulate(record);` |

For example, the following **data validation function** checks:

*   The record type
*   The `id`
*   The HTTPS template URL
*   The presence of variants

It throws descriptive errors if any of these elements are missing.

```
function validateRecord(record) {  if (typeof record !== 'object' || record === null) {    throw new Error('Record must be an object');  }  if (typeof record.id !== 'string') {    throw new Error('Missing record id');  }  if (!record.templateUrl?.startsWith('https://')) {    throw new Error('Invalid template URL');  }  if (!Array.isArray(record.variants) || record.variants.length === 0) {    throw new Error('Record requires at least one variant');  }  return true;}
```

## Batch Process on Production[#](#batch-process-on-production)

When running on production, enhance browser-based batch processes with architecture and UX decisions that help the user run the workflow, such as:

*   **User-initiated batches**: keep work tied to explicit user actions; show confirmation dialogs for large jobs.
*   **Chunked processing**: split datasets into small slices (for example, 20 records) to avoid blocking the main thread.
*   **Resource caps**: document safe limits (for example, 50–100 exports per session) and enforce them in the UI.
*   **Persistence**: use `localStorage` or IndexedDB to cache progress so reloads can resume work.

### Monitor the Process[#](#monitor-the-process)

Give users visibility inside the tab and send lightweight telemetry upstream.

*   Render UI elements that show the state, such as:
    
    *   Progress bars
    *   Per-item status chips
*   Send `fetch` calls to your backend for:
    
    *   Error logs
    *   Aggregated stats
*   When a chunk fails:
    
    1.  Show in-app notifications/snackbars.
    2.  Offer retries.

For example, the following code:

*   Structures logging.
*   Renders it with timestamps.

```
function reportBatchMetrics(batchMetrics) {  const entry = {    timestamp: new Date().toISOString(),    ...batchMetrics,  };  console.table([entry]);  return fetch('/api/logs', {    method: 'POST',    headers: { 'Content-Type': 'application/json' },    body: JSON.stringify(entry),  });}
```

## Troubleshooting[#](#troubleshooting)

| Issue | Cause | Solution |
| --- | --- | --- |
| Out of memory errors | Blob URLs not revoked, engine not disposed | Call `URL.revokeObjectURL()` and `engine.dispose()` |
| Slow processing speed | Template loaded each iteration | Load template once, modify variables only |
| Items fail silently | Missing error handling | Wrap processing in try-catch blocks |
| Inconsistent outputs | Shared state between iterations | Reset state or reload template each iteration |
| Process hangs indefinitely | Uncaught promise rejection | Use error handling and timeouts |
| Performance bottlenecks | Multiple | \- Profile batch operations  
\- Identify slow operations  
\- Optimize export settings  
\- Reduce template complexity  
 |

### Debugging Strategies[#](#debugging-strategies)

Effective troubleshooting techniques for batch processing in web apps include:

*   Retry with small batches.
*   Console log detailed error information.
*   Isolate problematic items.

## Next Steps[#](#next-steps)

*   [Headless Mode](vue/concepts/headless-mode/browser-24ab98/) \- Learn headless engine operation basics
*   [Design Generation](vue/automation/design-generation-98a99e/) \- Automate single design generation workflows
*   [Export Designs](vue/export-save-publish/export/overview-9ed3a8/) \- Deep dive into export options and formats
*   [Text Variables](vue/create-templates/add-dynamic-content/text-variables-7ecb50/) \- Work with dynamic text content in templates
*   [Source Sets](vue/import-media/source-sets-5679c8/) \- Specify assets sources for each block.

---



[Source](https:/img.ly/docs/cesdk/vue/automation/auto-resize-4c2d58)