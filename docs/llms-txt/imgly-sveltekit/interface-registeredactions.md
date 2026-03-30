# Interface: RegisteredActions

Represents a collection of action functions used throughout the application. Each property corresponds to a specific UI action or event that can be customized.

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| `saveScene` | [`SaveSceneAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/savesceneaction/) | Action invoked to handle scene saving. |
| `shareScene` | [`ShareSceneAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/sharesceneaction/) | Action invoked to handle scene sharing. |
| `exportDesign` | [`ExportAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/exportaction/) | Action invoked to handle export actions. |
| `importScene` | [`ImportSceneAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/importsceneaction/) | Action invoked to handle import actions. |
| `exportScene` | [`ExportSceneAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/exportsceneaction/) | Action invoked to handle scene export actions. |
| `uploadFile` | [`UploadAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/uploadaction/) | Action invoked to handle file uploads. |
| `onUnsupportedBrowser` | [`OnUnsupportedBrowserAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/onunsupportedbrowseraction/) | Action invoked when an unsupported browser is detected. |
| `addClip` | `VoidFunction` | Action invoked when the add clip button is pressed in the video timeline |
| `zoom.toBlock` | [`ZoomToBlockAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/zoomtoblockaction/) | Action for zooming to a specific block |
| `zoom.toPage` | [`ZoomToPageAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/zoomtopageaction/) | Action for zooming to a page (current, first, last, or by index) with optional padding |
| `zoom.toSelection` | [`ZoomToSelectionAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/zoomtoselectionaction/) | Action for zooming to the current selection |
| `zoom.in` | [`ZoomInAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/zoominaction/) | Action for zooming in by one step |
| `zoom.out` | [`ZoomOutAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/zoomoutaction/) | Action for zooming out by one step |
| `zoom.toLevel` | [`ZoomToLevelAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/zoomtolevelaction/) | Action for setting zoom to a specific level |
| `scroll.toPage` | [`ScrollToPageAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/scrolltopageaction/) | Action for scrolling to a specific page |
| `scroll.toBlock` | [`ScrollToBlockAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/scrolltoblockaction/) | Action for scrolling to a specific block |
| `timeline.zoom.in` | [`TimelineZoomInAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/timelinezoominaction/) | Action for zooming in the video timeline |
| `timeline.zoom.out` | [`TimelineZoomOutAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/timelinezoomoutaction/) | Action for zooming out the video timeline |
| `timeline.zoom.fit` | [`TimelineZoomToFitAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/timelinezoomtofitaction/) | Action for fitting the video timeline to show all content |
| `timeline.zoom.toLevel` | [`TimelineZoomToLevelAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/timelinezoomtolevelaction/) | Action for setting the video timeline zoom to a specific level |
| `timeline.zoom.reset` | [`TimelineZoomResetAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/timelinezoomresetaction/) | Action for resetting the video timeline zoom to default |
| `timeline.expand` | [`TimelineExpandAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/timelineexpandaction/) | Action for expanding the video timeline |
| `timeline.collapse` | [`TimelineCollapseAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/timelinecollapseaction/) | Action for collapsing the video timeline |
| `copy` | [`CopyAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/copyaction/) | Action for copying selected blocks to the clipboard |
| `paste` | [`PasteAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/pasteaction/) | Action for pasting blocks from the clipboard |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/range)