# Source: https://docs.roboflow.com/roboflow/roboflow-ko/annotate/use-roboflow-annotate/keyboard-shortcuts.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/anotto/use-roboflow-annotate/keyboard-shortcuts.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/annotate/use-roboflow-annotate/keyboard-shortcuts.md

# Source: https://docs.roboflow.com/annotate/use-roboflow-annotate/keyboard-shortcuts.md

# Keyboard Shortcuts

The following keyboard shortcuts are available to speed up your labeling flow. The **meta** key is usually the **command** key on macOS and the **ctrl** key on Linux and Windows.

## Shortcuts without a Selected Annotation

If no annotation is selected, the following keyboard shortcuts apply:

* **meta** - temporarily switches between the **Drag/Select** and **Bounding Box (B)** or **Polygon (P)** tools while held down. (For example, if you are in **Bounding Box** mode, hold down the meta key and click an existing bounding box to select it.)
* **b** - Switches to the **Bounding Box** tool.<img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-29d6fbd9d8d26c24329379c580d108bb4e1243ed%2Fimage.png?alt=media" alt="" data-size="line"><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-12a3ea5b23853f9ae19f43aaff618766ec422169%2Fimage.png?alt=media" alt="" data-size="line">
* **p** - Switches to the **Polygon** tool.<img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-9241944de3bfef86cb5f6088248bc3ace6cb2a11%2Fimage.png?alt=media" alt="" data-size="line"><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-675f63845216c5050ada3d6fc558a37e8b563e5b%2Fimage.png?alt=media" alt="" data-size="line">
* **d** - Switches to the **Drag/Select** tool. <img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-a9dd119f2024f36cd158ab3d7a369a5d6c6dd5ff%2Fimage.png?alt=media" alt="" data-size="line"><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-8e0a90ff0bfbd6f0d94dff5791227087bdb01ca6%2Fimage.png?alt=media" alt="" data-size="line">
* **n** - Switches to the **Mark Null** tool.<img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-1c8dccc51ae0d76312a3f38f6b35f92f3293b1ef%2Fimage.png?alt=media" alt="" data-size="line"><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-4edfd1556ff4343343fdbe729c9079b2710565b5%2Fimage.png?alt=media" alt="" data-size="line">
  * entering **n** while annotating an image that is already marked as *Null* will mark that image as *Unannotated* if it is currently in the *Annotating* queue.
* **s** - switches to the **Smart Polygon** tool.<img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-b11ebcacb3e2f4e8b68e7a1b069016c47aa76b47%2Fimage.png?alt=media" alt="" data-size="line"><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-f42d6c2e3808b85ad20611621ceb84a1917329ae%2Fimage.png?alt=media" alt="" data-size="line">
* **plus** - Zooms In.
* **minus** - Zooms Out.
* **zero** - Returns to Default Zoom (fits image into the viewport).
* **one** - Zooms to 100%.
* **escape** (esc) - Exits the Labeling Tool.
* **left arrow** - Navigates to the previous image.
  * In Classification projects, **left arrow** + **cmd**.
* **right arrow** - Navigates to the next image.
  * In Classification projects, **right arrow** + **cmd**.

## Shortcuts with a Selected Annotation

Once an annotation is selected and the class selector is visible, the shortcuts are as follows:

* **enter** - Saves the Active Option (highlighted in purple) as the current class, or label, for the selected bounding box.
* **escape** (esc) - Cancels and deselects the current box without changing its label (if the currently selected box was just drawn it will be deleted).
* **up arrow** - Changes the Active Option (class/label) to the previous one.
* **down arrow** - Changes the Active Option (class/label) to the next one.
* **backspace** - Deletes the current bounding box if there is no text in the text field (this means you will usually have to *push backspace twice to delete a box after selecting it*; one time to delete the highlighted text and a second time to confirm deletion).

## Shortcuts in Review Mode

Review mode is the interface that lets a reviewer approve or reject an annotation.

If you are in review mode, the following shortcuts are available:

* **a** (in Review Mode) Approve annotation or label
* **r** (in Review Mode) Rejects annotation or label

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-0efed8f11f36374c09ccbcb9c9536c285daffbc5%2Fimage.png?alt=media" alt="Preview of Review Mode"><figcaption><p>Preview of Review Mode</p></figcaption></figure>
