# Using the Web editor

Work in progress
The content of this page was not yet updated for Godot4.6and may beoutdated. If you know how to improve this page or you can confirm
        that it's up to date, feel free toopen a pull request.

# Using the Web editor
There is aWeb editoryou can use to work
on new or existing projects.
Note
The web editor is in a preliminary stage. While its feature set may be
sufficient for educational purposes, it is currentlynot recommended for
production work. SeeLimitationsbelow.

## Browser support
The Web editor requires support for WebAssembly's SharedArrayBuffer. This
is in turn required to support threading in the browser.
SeeSystem requirementsfor a list of supported web browsers.
Mobile browsers are supported, but won't provide an ideal experience
due to performance and input limitations.
The web editor only supports the Compatibility renderer, as there is no
stable way to run Vulkan applications on the web yet.
Note
If you run into performance issues on Firefox, try using a Chromium-based
browser as these may perform better in WebGL applications.

## Limitations
Due to limitations on the Godot or Web platform side, the following features
are currently missing:
- No C#/Mono support.
No C#/Mono support.
- No GDExtension support.
No GDExtension support.
- No debugging support. This means GDScript debugging/profiling, live scene
editing, the Remote Scene tree dock and other features that rely on the debugger
protocol will not work.
No debugging support. This means GDScript debugging/profiling, live scene
editing, the Remote Scene tree dock and other features that rely on the debugger
protocol will not work.
- No project exporting. As a workaround, you can download the project source
usingProject > Tools > Download Project Sourceand export it using anative version of the Godot editor.
No project exporting. As a workaround, you can download the project source
usingProject > Tools > Download Project Sourceand export it using anative version of the Godot editor.
- The editor won't warn you when closing the tab with unsaved changes.
The editor won't warn you when closing the tab with unsaved changes.
- No lightmap baking support. You can still use existing lightmaps if they were
baked with a native version of the Godot editor
(e.g. by importing an existing project).
No lightmap baking support. You can still use existing lightmaps if they were
baked with a native version of the Godot editor
(e.g. by importing an existing project).
The following features are unlikely to be supported due to inherent limitations
of the Web platform:
- No support for external script editors.
No support for external script editors.
- No support for Android one-click deploy.
No support for Android one-click deploy.
See also
See thelist of open issues on GitHub related to the web editorfor a list of known bugs.

## Importing a project
To import an existing project, the current process is as follows:
- Specify a ZIP file to preload on the HTML5 filesystem using thePreload project ZIPinput.
Specify a ZIP file to preload on the HTML5 filesystem using thePreload project ZIPinput.
- Run the editor by clickingStart Godot editor.
The Godot Project Manager should appear after 10-20 seconds.
On slower machines or connections, loading may take up to a minute.
Run the editor by clickingStart Godot editor.
The Godot Project Manager should appear after 10-20 seconds.
On slower machines or connections, loading may take up to a minute.
- In the dialog that appears at the middle of the window, specify a name for
the folder to create then click theCreate Folderbutton
(it doesn't have to match the ZIP archive's name).
In the dialog that appears at the middle of the window, specify a name for
the folder to create then click theCreate Folderbutton
(it doesn't have to match the ZIP archive's name).
- ClickInstall & Editand the project will open in the editor.
ClickInstall & Editand the project will open in the editor.
Attention
It's important to place the project folder somewhere in/home/web_user/.
If your project folder is placed outside/home/web_user/, you will
lose your project when closing the editor!
When you follow the steps described above, the project folder will always be
located in/home/web_user/projects, keeping it safe.

## Editing and running a project
Unlike the native version of Godot, the web editor is constrained to a single
window. Therefore, it cannot open a new window when running the project.
Instead, when you run the project by clicking the Run button or pressingF5, it will appear to "replace" the editor window.
The web editor offers an alternative way to deal with the editor and game
windows (which are now "tabs"). You can switch between theEditorandGametabs using the buttons on the top. You can also close the running game
or editor by clicking the×button next to those tabs.

## Where are my project files?
Due to browser security limitations, the editor will save the project files to
the browser's IndexedDB storage. This storage isn't accessible as a regular folder
on your machine, but is abstracted away in a database.
You can download the project files as a ZIP archive by usingProject > Tools > Download Project Source. This can be used to export the
project using anative Godot editor,
since exporting from the web editor isn't supported yet.
In the future, it may be possible to use theHTML5 FileSystem APIto store the project files on the user's filesystem as the native editor would do.
However, this isn't implemented yet.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.