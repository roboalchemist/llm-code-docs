# Actions API

The Actions API provides a centralized way to manage and customize actions for various user interactions in CE.SDK.

The Actions API is available after CE.SDK initialization through `cesdk.actions`.

CE.SDK also provides a Utils API (`cesdk.utils`) with utility functions for common operations like exporting, file handling, and UI dialogs. These utilities can be used directly or within your custom actions.

## API Methods[#](#api-methods)

The Actions API provides four methods:

*   `register(actionId, handler)` - Register an action function for a specific event
*   `get(actionId)` - Retrieve a registered action function
*   `run(actionId, ...args)` - Execute a registered action with the provided arguments (throws if not registered)
*   `list(matcher)` - Lists registered action IDs, optionally filtered by wildcard pattern

## Getting Started[#](#getting-started)

Register actions after initializing CE.SDK:

```
import CreativeEditorSDK from '@cesdk/cesdk-js';
const cesdk = await CreativeEditorSDK.create(container, {  // license: 'YOUR_CESDK_LICENSE_KEY',});
// Register an actioncesdk.actions.register('actionType', async (...args) => {  // Your custom implementation  return result;});
// Execute a registered actionawait cesdk.actions.run('actionType', arg1, arg2);
// Or retrieve an action to call it laterconst action = cesdk.actions.get('actionType');
// List all registered actionsconst allActions = cesdk.actions.list();
// List actions matching a patternconst exportActions = cesdk.actions.list({ matcher: 'export*' });
```

## Default Actions[#](#default-actions)

CE.SDK automatically registers the following default actions:

### Action Handlers[#](#action-handlers)

*   `saveScene` - Saves the current scene (default: downloads scene file)
*   `shareScene` - Shares the current scene (no default implementation)
*   `exportDesign` - Exports design in various formats (default: downloads the exported file)
*   `importScene` - Imports scene or archive files (default: opens file picker)
*   `exportScene` - Exports scene or archive (default: downloads the file)
*   `uploadFile` - Uploads files to asset sources (default: local upload for development)
*   `onUnsupportedBrowser` - Handles unsupported browsers (no default implementation)

### Zoom Actions[#](#zoom-actions)

*   `zoom.toBlock` - Zoom to a specific block with configurable padding
*   `zoom.toPage` - Zoom to the current page with auto-fit support
*   `zoom.toSelection` - Zoom to currently selected blocks
*   `zoom.in` - Zoom in by one step with configurable maximum
*   `zoom.out` - Zoom out by one step with configurable minimum
*   `zoom.toLevel` - Set zoom to a specific level

### Scroll Actions[#](#scroll-actions)

*   `scroll.toPage` - Scroll the viewport to center on a specific page with optional animation

### Video Timeline Zoom Actions[#](#video-timeline-zoom-actions)

*   `timeline.zoom.in` - Zoom in the video timeline by one step
*   `timeline.zoom.out` - Zoom out the video timeline by one step
*   `timeline.zoom.fit` - Fit the video timeline to show all content
*   `timeline.zoom.toLevel` - Set the video timeline zoom to a specific level
*   `timeline.zoom.reset` - Reset the video timeline zoom to default (1.0)

The `shareScene` and `onUnsupportedBrowser` actions do not have default implementations and must be registered manually.

CE.SDK provides both an Actions API for handling user actions and a Utils API for utility functions. See the Utils API section below for details on available utilities.

### Scene Management Actions[#](#scene-management-actions)

#### `saveScene`[#](#savescene)

Handles saving the current scene. Default implementation downloads the scene file.

```
// Basic implementationcesdk.actions.register('saveScene', async () => {  const scene = await cesdk.engine.scene.saveToString();  console.log('Scene saved:', scene.length, 'characters');
  // Production:  // await yourAPI.saveScene(scene);
  cesdk.ui.showNotification('Scene saved successfully');});
// With loading dialogcesdk.actions.register('saveScene', async () => {  const dialogController = cesdk.utils.showLoadingDialog({    title: 'Saving Scene',    message: 'Please wait...',    progress: 'indeterminate',  });
  try {    const scene = await cesdk.engine.scene.saveToString();    console.log('Scene saved:', scene.length, 'characters');
    // Production:    // await yourAPI.saveScene(scene);
    dialogController.showSuccess({      title: 'Saved',      message: 'Scene saved successfully',    });  } catch (error) {    dialogController.showError({      title: 'Save Failed',      message: 'Could not save the scene',    });    throw error;  }});
```

#### `shareScene`[#](#sharescene)

Handles scene sharing. No default implementation.

```
// Register share functionalitycesdk.actions.register('shareScene', async () => {  const scene = await cesdk.engine.scene.saveToString();  const shareUrl = 'https://example.com/shared-scene-placeholder';  console.log('Scene ready to share:', scene.length, 'characters');
  // Production:  // const shareUrl = await yourAPI.createShareableLink(scene);
  await navigator.share({ url: shareUrl });});
```

#### `importScene` and `exportScene`[#](#importscene-and-exportscene)

Handle scene import/export operations with support for both scene files and archives.

```
// Import scene or archivecesdk.actions.register('importScene', async ({ format }) => {  if (format === 'archive') {    console.log('Archive import requested');
    // Production:    // const archive = await yourAPI.loadArchive();    // await cesdk.engine.scene.loadFromArchiveURL(archive);  } else {    console.log('Scene import requested');
    // Production:    // const scene = await yourAPI.loadScene();    // await cesdk.engine.scene.loadFromString(scene);  }});
// Export scene or archivecesdk.actions.register('exportScene', async ({ format }) => {  if (format === 'archive') {    const archive = await cesdk.engine.scene.saveToArchive();    console.log('Archive ready for export:', archive.length, 'bytes');
    // Production:    // await yourAPI.uploadArchive(archive);  } else {    const scene = await cesdk.engine.scene.saveToString();    console.log('Scene ready for export:', scene.length, 'characters');
    // Production:    // await yourAPI.uploadScene(scene);  }});
```

### Export Operations[#](#export-operations)

#### `exportDesign`[#](#exportdesign)

Handles all export operations (images, PDFs, videos). Default implementation downloads the exported file.

```
// Basic implementationcesdk.actions.register('exportDesign', async options => {  // Use the utils API to perform the export with loading dialog  const { blobs, options: exportOptions } = await cesdk.utils.export(options);  console.log('Exported', blobs.length, 'files');  blobs.forEach((blob, i) => console.log(`File ${i + 1}:`, blob.size, 'bytes'));
  // Production:  // await Promise.all(blobs.map(blob => yourCDN.upload(blob)));
  cesdk.ui.showNotification('Export completed successfully');});
// Direct engine export with custom loading dialog (bypassing utils)cesdk.actions.register('exportDesign', async options => {  const dialogController = cesdk.utils.showLoadingDialog({    title: 'Exporting',    message: 'Processing your export...',  });
  try {    const page = cesdk.engine.scene.getCurrentPage();    if (page === null) {      throw new Error('No page selected for export');    }    let result;
    if (options?.mimeType?.startsWith('video/')) {      // Video export with progress      result = await cesdk.engine.block.exportVideo(page, {        ...options,        onProgress: (rendered, encoded, total) => {          dialogController.updateProgress({            value: rendered,            max: total,          });        },      });    } else {      // Static export (image/PDF)      result = await cesdk.engine.block.export(page, options);    }
    console.log('File ready for export:', result.size, 'bytes');
    // Production:    // await yourCDN.upload(result);
    dialogController.showSuccess({      title: 'Export Complete',      message: 'Files uploaded successfully',    });  } catch (error) {    dialogController.showError({      title: 'Export Failed',      message: 'Could not complete the export',    });    throw error;  }});
```

### File Upload Action[#](#file-upload-action)

#### `uploadFile`[#](#uploadfile)

Handles file uploads to asset sources. Default implementation uses local upload for development.

```
// Register production upload handlercesdk.actions.register('uploadFile', async (file, onProgress, context) => {  console.log('Uploading file:', file.name, file.size, 'bytes');  onProgress(50); // Simulate progress  await new Promise(resolve => setTimeout(resolve, 500));  onProgress(100);
  // Production:  // const asset = await yourStorageService.upload(file, {  //   onProgress: (percent) => onProgress(percent),  //   context  // });
  // Return AssetDefinition  return {    id: 'local-' + Date.now(),    label: { en: file.name },    meta: {      uri: URL.createObjectURL(file),      thumbUri: URL.createObjectURL(file),      kind: 'image',      width: 1920,      height: 1080,      // Production:      // uri: asset.url,      // thumbUri: asset.thumbnailUrl,      // width: asset.width,      // height: asset.height    },  };});
```

You can control which file types users can upload by setting the `upload/supportedMimeTypes` setting:

```
// Example 1: Only allow imagescesdk.engine.editor.setSettingString(  'upload/supportedMimeTypes',  'image/png,image/jpeg,image/gif,image/svg+xml',);
// Example 2: Allow images and videoscesdk.engine.editor.setSettingString(  'upload/supportedMimeTypes',  'image/png,image/jpeg,image/gif,video/mp4,video/quicktime',);
// Example 3: Allow specific document typescesdk.engine.editor.setSettingString(  'upload/supportedMimeTypes',  'application/pdf,image/png,image/jpeg',);
```

The default `uploadFile` implementation uses local upload for development only. Always register a proper upload handler for production.

### Unsupported Browser Action[#](#unsupported-browser-action)

#### `onUnsupportedBrowser`[#](#onunsupportedbrowser)

Handles unsupported browser detection. No default implementation is provided.

```
// Register handler for unsupported browserscesdk.actions.register('onUnsupportedBrowser', () => {  // Redirect to a custom compatibility page  window.location.href = '/browser-not-supported';});
```

### Zoom Actions[#](#zoom-actions-1)

CE.SDK provides built-in zoom actions for controlling the viewport zoom level and focus. These actions are automatically registered and can be customized or called programmatically.

#### Available Zoom Actions[#](#available-zoom-actions)

*   `zoom.toBlock` - Zoom to a specific block with configurable padding
*   `zoom.toPage` - Zoom to the current page (or a specified page)
*   `zoom.toSelection` - Zoom to the currently selected blocks
*   `zoom.in` - Zoom in by one step
*   `zoom.out` - Zoom out by one step
*   `zoom.toLevel` - Set zoom to a specific level

#### `zoom.toBlock`[#](#zoomtoblock)

Zooms the viewport to fit a specific block.

```
// Zoom to a block with default settingsawait cesdk.actions.run('zoom.toBlock', blockId);
// Zoom with custom padding and animationawait cesdk.actions.run('zoom.toBlock', blockId, {  padding: 50, // Uniform padding on all sides  animate: true,  autoFit: false});
// Different padding for each sideawait cesdk.actions.run('zoom.toBlock', blockId, {  padding: { top: 20, bottom: 20, left: 40, right: 40 },  animate: {    duration: 0.3,    easing: 'EaseInOut'  }});
```

#### `zoom.toPage`[#](#zoomtopage)

Zooms to the current page or a specified page. If no options are provided, defaults to the current page.

```
// Zoom to current page with auto-fitawait cesdk.actions.run('zoom.toPage', {  autoFit: true,  animate: false});
// Zoom with custom paddingawait cesdk.actions.run('zoom.toPage', {  padding: { x: 40, y: 80 },  animate: true});
```

#### `zoom.toSelection`[#](#zoomtoselection)

Zooms to fit all currently selected blocks in the viewport.

```
// Zoom to selection with animationawait cesdk.actions.run('zoom.toSelection', {  padding: 40,  animate: true});
// Auto-fit to selectionawait cesdk.actions.run('zoom.toSelection', {  autoFit: true,  padding: { x: 20, y: 20 }});
```

#### `zoom.in` and `zoom.out`[#](#zoomin-and-zoomout)

Step-based zoom controls with configurable limits.

```
// Zoom in with default settingsawait cesdk.actions.run('zoom.in');
// Zoom in with custom maximumawait cesdk.actions.run('zoom.in', {  maxZoom: 4, // Maximum zoom level  animate: true});
// Zoom out with custom minimumawait cesdk.actions.run('zoom.out', {  minZoom: 0.25, // Minimum zoom level  animate: {    duration: 0.2,    easing: 'EaseOut'  }});
```

#### `zoom.toLevel`[#](#zoomtolevel)

Sets the zoom to a specific level.

```
// Set zoom to 100%await cesdk.actions.run('zoom.toLevel', 1.0);
// Set zoom to 200% with animationawait cesdk.actions.run('zoom.toLevel', 2.0, {  animate: true,  minZoom: 0.125,  maxZoom: 32});
// Fit to width (50% zoom)await cesdk.actions.run('zoom.toLevel', 0.5, {  animate: {    duration: 0.3,    easing: 'EaseInOut'  }});
```

#### Padding Options[#](#padding-options)

Padding can be specified in multiple ways:

```
// Uniform padding on all sides{ padding: 20 }
// Different horizontal and vertical padding{ padding: { x: 40, y: 20 } }
// Individual padding for each side{ padding: { top: 10, bottom: 20, left: 30, right: 40 } }
```

#### Animation Options[#](#animation-options)

Animation can be a boolean or an object with detailed settings:

```
// Simple animation toggle{ animate: true }  // Uses default duration and easing{ animate: false } // No animation
// Detailed animation configuration{  animate: {    duration: 0.3,        // Duration in seconds    easing: 'EaseInOut',  // 'Linear', 'EaseIn', 'EaseOut', or 'EaseInOut'    interruptible: true   // Whether the animation can be interrupted  }}
```

#### Auto-Fit Mode[#](#auto-fit-mode)

The `autoFit` option enables automatic zoom adjustment when the viewport resizes:

```
// Enable auto-fit to maintain proper framingawait cesdk.actions.run('zoom.toPage', {  autoFit: true,  padding: { x: 40, y: 80 }});
```

When auto-fit is enabled, the zoom level will automatically adjust to keep the target properly framed when the viewport size changes.

#### Custom Zoom Action Example[#](#custom-zoom-action-example)

You can override the default zoom actions with custom implementations:

```
// Custom zoom to page with analyticscesdk.actions.register('zoom.toPage', async (options) => {  // Track zoom event  console.log('User zoomed to page');
  // Get current page  const currentPage = cesdk.engine.scene.getCurrentPage();  if (!currentPage) return;
  // Apply custom zoom logic  await cesdk.engine.scene.zoomToBlock(currentPage, {    padding: options?.padding ?? { x: 50, y: 100 },    animate: options?.animate ?? true  });
  // Custom post-zoom behavior  cesdk.ui.showNotification('Zoomed to page');});
```

### Video Timeline Zoom Actions[#](#video-timeline-zoom-actions-1)

The video timeline has its own set of zoom controls for managing the timeline view. These actions are registered when the video timeline component is active and provide instant zoom without animation.

#### `timeline.zoom.in`[#](#timelinezoomin)

Zooms in the video timeline by one step (multiplies current zoom level by 1.25).

```
// Zoom in the timelineawait cesdk.actions.run('timeline.zoom.in');
```

#### `timeline.zoom.out`[#](#timelinezoomout)

Zooms out the video timeline by one step (divides current zoom level by 1.25).

```
// Zoom out the timelineawait cesdk.actions.run('timeline.zoom.out');
```

#### `timeline.zoom.fit`[#](#timelinezoomfit)

Automatically adjusts the timeline zoom to fit all content in the visible area.

```
// Fit timeline to show all contentawait cesdk.actions.run('timeline.zoom.fit');
```

#### `timeline.zoom.toLevel`[#](#timelinezoomtolevel)

Sets the timeline zoom to a specific level.

```
// Set timeline zoom to 100%await cesdk.actions.run('timeline.zoom.toLevel', 1.0);
// Set timeline zoom to 150%await cesdk.actions.run('timeline.zoom.toLevel', 1.5);
// Set timeline zoom to 50%await cesdk.actions.run('timeline.zoom.toLevel', 0.5);
```

#### `timeline.zoom.reset`[#](#timelinezoomreset)

Resets the timeline zoom to the default level (1.0 or 100%).

```
// Reset timeline zoom to defaultawait cesdk.actions.run('timeline.zoom.reset');
```

### Scroll Actions[#](#scroll-actions-1)

CE.SDK provides a scroll action for panning the viewport to different pages without changing the zoom level. This is useful for multi-page navigation where you want to maintain the current zoom.

#### `scroll.toPage`[#](#scrolltopage)

Scrolls the viewport to center on a specific page without changing the zoom level.

```
// Scroll to current page without animationawait cesdk.actions.run('scroll.toPage');
// Scroll to current page with smooth animationawait cesdk.actions.run('scroll.toPage', {  animate: true});
// Scroll to a specific pageawait cesdk.actions.run('scroll.toPage', {  pageId: myPageId,  animate: true});
```

#### Parameters[#](#parameters)

The `scroll.toPage` action accepts an optional options object:

*   `pageId` (optional): The ID of the page to scroll to. If not provided, scrolls to the current page.
*   `animate` (optional): Whether to animate the scroll transition. Default is `false`.

#### Scroll vs Zoom[#](#scroll-vs-zoom)

The key difference between `scroll.toPage` and `zoom.toPage`:

*   **`scroll.toPage`**: Pans the viewport to center on the page while maintaining the current zoom level
*   **`zoom.toPage`**: Adjusts the zoom level to fit the page within the viewport with padding

Use `scroll.toPage` when you want to navigate between pages in a multi-page document while keeping the same zoom level. Use `zoom.toPage` when you want to frame a page properly within the viewport.

## Utils API[#](#utils-api)

CE.SDK provides a Utils API with utility functions for common operations. These utilities are available through `cesdk.utils`:

### Loading Dialogs[#](#loading-dialogs)

```
// Create and manage loading dialogsconst dialogController = cesdk.utils.showLoadingDialog({  title: 'Processing...',  message: 'Please wait', // Can also be an array of strings  progress: 0, // Initial progress value or 'indeterminate'  cancelLabel: 'Cancel',  abortTitle: 'Abort Operation?',  abortMessage: 'Are you sure you want to abort?',  abortLabel: 'Abort',  size: 'large', // 'regular' or 'large'  clickOutsideToClose: false,  onAbort: () => console.log('User cancelled'),  onDone: () => console.log('Dialog closed'),});
// Update progressdialogController.updateProgress({ value: 50, max: 100 });
// Show success or errordialogController.showSuccess({  title: 'Done!',  message: 'Operation completed',});dialogController.showError({ title: 'Error', message: 'Something went wrong' });
// Close dialogdialogController.close();
```

### Export Utility[#](#export-utility)

The export utility automatically handles both static (images, PDFs) and video exports:

```
// Export image or PDFconst { blobs, options } = await cesdk.utils.export({  mimeType: 'image/png',  pngCompressionLevel: 7,});
// Export video (automatically detected by MIME type)const { blobs, options } = await cesdk.utils.export({  mimeType: 'video/mp4',  onProgress: (rendered, encoded, total) => {    console.log(`Progress: ${rendered}/${total} frames`);  },});
```

### File Operations[#](#file-operations)

```
// Load file from userconst file = await cesdk.utils.loadFile({  accept: 'image/*',  returnType: 'File', // 'dataURL', 'text', 'blob', 'arrayBuffer', or 'File'});
// Download file to user's deviceawait cesdk.utils.downloadFile(blob, 'image/png');
// Local upload (development only)const asset = await cesdk.utils.localUpload(file, context);
```

## Implementation Examples[#](#implementation-examples)

### Environment-Based Upload Strategy[#](#environment-based-upload-strategy)

```
// Use local upload in development, CDN in productioncesdk.actions.register('uploadFile', async (file, onProgress, context) => {  if (process.env.NODE_ENV === 'development') {    // Use utils for local upload    return await cesdk.utils.localUpload(file, context);  } else {    console.log('Production upload for:', file.name);    onProgress(100);
    // Production:    // const asset = await yourCDNService.upload(file, {    //   onProgress: onProgress    // });
    return {      id: 'prod-' + Date.now(),      label: { en: file.name },      meta: {        uri: URL.createObjectURL(file),        thumbUri: URL.createObjectURL(file),        // Production:        // uri: asset.url,        // thumbUri: asset.thumbnailUrl      },    };  }});
```

### Combining Utils with Custom Logic[#](#combining-utils-with-custom-logic)

```
// Use utils for heavy lifting, add custom business logiccesdk.actions.register('exportDesign', async options => {  console.log('Export started:', { format: options?.mimeType });
  // Production:  // analytics.track('export_started', { format: options?.mimeType });
  // Use utils to handle the export with loading dialog  const { blobs, options: exportOptions } = await cesdk.utils.export(options);
  // Custom post-processing  if (exportOptions.mimeType === 'application/pdf') {    console.log('PDF ready for watermarking:', blobs[0].size, 'bytes');
    // Production:    // const watermarkedBlob = await addWatermark(blobs[0]);    // await cesdk.utils.downloadFile(watermarkedBlob, 'application/pdf');
    await cesdk.utils.downloadFile(blobs[0], 'application/pdf');  } else {    // Direct download for other formats    await cesdk.utils.downloadFile(blobs[0], exportOptions.mimeType);  }
  console.log('Export completed:', { format: exportOptions.mimeType });
  // Production:  // analytics.track('export_completed', { format: exportOptions.mimeType });});
```

## Registering Custom Actions with Custom IDs[#](#registering-custom-actions-with-custom-ids)

Beyond the predefined action types, you can register actions with custom IDs for your own application-specific needs:

```
// Register a custom actioncesdk.actions.register('myCustomAction', async data => {  console.log('Custom action triggered with:', data);  return { success: true, processedData: data };});
// Execute the custom action using runconst result = await cesdk.actions.run('myCustomAction', { someData: 'value' });
// Or retrieve it for conditional executionconst customAction = cesdk.actions.get('myCustomAction');if (customAction) {  const result = await customAction({ someData: 'value' });}
```

## Discovering Registered Actions[#](#discovering-registered-actions)

Use `list()` to get all registered action IDs or find actions matching a pattern:

```
// Get all registered action IDsconst registeredActions = cesdk.actions.list();console.log('Available actions:', registeredActions);
// Find actions matching a patternconst exportActions = cesdk.actions.list({ matcher: 'export*' });console.log('Export actions:', exportActions);
```

## Using Actions with Navigation Actions[#](#using-actions-with-navigation-actions)

The navigation bar actions in CE.SDK automatically use the registered actions:

### Default Navigation Bar Actions[#](#default-navigation-bar-actions)

The default navigation bar actions map to actions:

*   Save action → `saveScene` action
*   Share action → `shareScene` action
*   Export actions → `exportDesign` action
*   Import scene/archive → `importScene` action
*   Export scene/archive → `exportScene` action

---



[Source](https:/img.ly/docs/cesdk/sveltekit/user-interface/ui-extensions-d194d1)