:github_url: hide



# EditorExportPlatformWeb

**Inherits:** [EditorExportPlatform<class_EditorExportPlatform>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Exporter for the Web.


## Description

The Web exporter customizes how a web build is handled. In the editor's "Export" window, it is created when adding a new "Web" preset.

\ **Note:** Godot on Web is rendered inside a `<canvas>` tag. Normally, the canvas cannot be positioned or resized manually, but otherwise acts as the main [Window<class_Window>] of the application.


## Tutorials

- [../tutorials/export/exporting_for_web](Exporting for the Web .md)

- [../tutorials/platform/web/index](Web documentation index .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`custom_template/debug<class_EditorExportPlatformWeb_property_custom_template/debug>`                                                                         |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`custom_template/release<class_EditorExportPlatformWeb_property_custom_template/release>`                                                                     |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`html/canvas_resize_policy<class_EditorExportPlatformWeb_property_html/canvas_resize_policy>`                                                                 |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`html/custom_html_shell<class_EditorExportPlatformWeb_property_html/custom_html_shell>`                                                                       |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`html/experimental_virtual_keyboard<class_EditorExportPlatformWeb_property_html/experimental_virtual_keyboard>`                                               |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`html/export_icon<class_EditorExportPlatformWeb_property_html/export_icon>`                                                                                   |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`html/focus_canvas_on_start<class_EditorExportPlatformWeb_property_html/focus_canvas_on_start>`                                                               |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`html/head_include<class_EditorExportPlatformWeb_property_html/head_include>`                                                                                 |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Color<class_Color>`   | :ref:`progressive_web_app/background_color<class_EditorExportPlatformWeb_property_progressive_web_app/background_color>`                                           |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`progressive_web_app/display<class_EditorExportPlatformWeb_property_progressive_web_app/display>`                                                             |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`progressive_web_app/enabled<class_EditorExportPlatformWeb_property_progressive_web_app/enabled>`                                                             |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`progressive_web_app/ensure_cross_origin_isolation_headers<class_EditorExportPlatformWeb_property_progressive_web_app/ensure_cross_origin_isolation_headers>` |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`progressive_web_app/icon_144x144<class_EditorExportPlatformWeb_property_progressive_web_app/icon_144x144>`                                                   |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`progressive_web_app/icon_180x180<class_EditorExportPlatformWeb_property_progressive_web_app/icon_180x180>`                                                   |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`progressive_web_app/icon_512x512<class_EditorExportPlatformWeb_property_progressive_web_app/icon_512x512>`                                                   |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`progressive_web_app/offline_page<class_EditorExportPlatformWeb_property_progressive_web_app/offline_page>`                                                   |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`progressive_web_app/orientation<class_EditorExportPlatformWeb_property_progressive_web_app/orientation>`                                                     |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`threads/emscripten_pool_size<class_EditorExportPlatformWeb_property_threads/emscripten_pool_size>`                                                           |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`threads/godot_pool_size<class_EditorExportPlatformWeb_property_threads/godot_pool_size>`                                                                     |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`variant/extensions_support<class_EditorExportPlatformWeb_property_variant/extensions_support>`                                                               |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`variant/thread_support<class_EditorExportPlatformWeb_property_variant/thread_support>`                                                                       |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`vram_texture_compression/for_desktop<class_EditorExportPlatformWeb_property_vram_texture_compression/for_desktop>`                                           |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`vram_texture_compression/for_mobile<class_EditorExportPlatformWeb_property_vram_texture_compression/for_mobile>`                                             |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[String<class_String>] **custom_template/debug** [🔗<class_EditorExportPlatformWeb_property_custom_template/debug>]

File path to the custom export template used for debug builds. If left empty, the default template is used.


----



[String<class_String>] **custom_template/release** [🔗<class_EditorExportPlatformWeb_property_custom_template/release>]

File path to the custom export template used for release builds. If left empty, the default template is used.


----



[int<class_int>] **html/canvas_resize_policy** [🔗<class_EditorExportPlatformWeb_property_html/canvas_resize_policy>]

Determines how the canvas should be resized by Godot.

- **None:** The canvas is not automatically resized.

- **Project:** The size of the canvas is dependent on the [ProjectSettings<class_ProjectSettings>].

- **Adaptive:** The canvas is automatically resized to fit as much of the web page as possible.


----



[String<class_String>] **html/custom_html_shell** [🔗<class_EditorExportPlatformWeb_property_html/custom_html_shell>]

The custom HTML page that wraps the exported web build. If left empty, the default HTML shell is used.

For more information, see the [../tutorials/platform/web/customizing_html5_shell](Customizing HTML5 Shell .md) tutorial.


----



[bool<class_bool>] **html/experimental_virtual_keyboard** [🔗<class_EditorExportPlatformWeb_property_html/experimental_virtual_keyboard>]

**Experimental:** This property may be changed or removed in future versions.

If `true`, embeds support for a virtual keyboard into the web page, which is shown when necessary on touchscreen devices.


----



[bool<class_bool>] **html/export_icon** [🔗<class_EditorExportPlatformWeb_property_html/export_icon>]

If `true`, the project icon will be used as the favicon for this application's web page.


----



[bool<class_bool>] **html/focus_canvas_on_start** [🔗<class_EditorExportPlatformWeb_property_html/focus_canvas_on_start>]

If `true`, the canvas will be focused as soon as the application is loaded, if the browser window is already in focus.


----



[String<class_String>] **html/head_include** [🔗<class_EditorExportPlatformWeb_property_html/head_include>]

Additional HTML tags to include inside the `<head>`, such as `<meta>` tags.

\ **Note:** You do not need to add a `<title>` tag, as it is automatically included based on the project's name.


----



[Color<class_Color>] **progressive_web_app/background_color** [🔗<class_EditorExportPlatformWeb_property_progressive_web_app/background_color>]

The background color used behind the web application.


----



[int<class_int>] **progressive_web_app/display** [🔗<class_EditorExportPlatformWeb_property_progressive_web_app/display>]

The [display mode ](https://developer.mozilla.org/en-US/docs/Web/Manifest/display/)_ to use for this progressive web application. Different browsers and platforms may not behave the same.

- **Fullscreen:** Displays the app in fullscreen and hides all of the browser's UI elements.

- **Standalone:** Displays the app in a separate window and hides all of the browser's UI elements.

- **Minimal UI:** Displays the app in a separate window and only shows the browser's UI elements for navigation.

- **Browser:** Displays the app as a normal web page.


----



[bool<class_bool>] **progressive_web_app/enabled** [🔗<class_EditorExportPlatformWeb_property_progressive_web_app/enabled>]

If `true`, turns this web build into a [progressive web application ](https://en.wikipedia.org/wiki/Progressive_web_app)_ (PWA).


----



[bool<class_bool>] **progressive_web_app/ensure_cross_origin_isolation_headers** [🔗<class_EditorExportPlatformWeb_property_progressive_web_app/ensure_cross_origin_isolation_headers>]

When enabled, the progressive web app will make sure that each request has cross-origin isolation headers (COEP/COOP).

This can simplify the setup to serve the exported game.


----



[String<class_String>] **progressive_web_app/icon_144x144** [🔗<class_EditorExportPlatformWeb_property_progressive_web_app/icon_144x144>]

File path to the smallest icon for this web application. If not defined, defaults to the project icon.

\ **Note:** If the icon is not 144×144, it will be automatically resized for the final build.


----



[String<class_String>] **progressive_web_app/icon_180x180** [🔗<class_EditorExportPlatformWeb_property_progressive_web_app/icon_180x180>]

File path to the small icon for this web application. If not defined, defaults to the project icon.

\ **Note:** If the icon is not 180×180, it will be automatically resized for the final build.


----



[String<class_String>] **progressive_web_app/icon_512x512** [🔗<class_EditorExportPlatformWeb_property_progressive_web_app/icon_512x512>]

File path to the largest icon for this web application. If not defined, defaults to the project icon.

\ **Note:** If the icon is not 512×512, it will be automatically resized for the final build.


----



[String<class_String>] **progressive_web_app/offline_page** [🔗<class_EditorExportPlatformWeb_property_progressive_web_app/offline_page>]

The page to display, should the server hosting the page not be available. This page is saved in the client's machine.


----



[int<class_int>] **progressive_web_app/orientation** [🔗<class_EditorExportPlatformWeb_property_progressive_web_app/orientation>]

The orientation to use when the web application is run through a mobile device.

- **Any:** No orientation is forced.

- **Landscape:** Forces a horizontal layout (wider than it is taller).

- **Portrait:** Forces a vertical layout (taller than it is wider).


----



[int<class_int>] **threads/emscripten_pool_size** [🔗<class_EditorExportPlatformWeb_property_threads/emscripten_pool_size>]

The number of threads that emscripten will allocate at startup. A smaller value will allocate fewer threads and consume fewer system resources, but you may run the risk of running out of threads in the pool and needing to allocate more threads at run time which may cause a deadlock.

\ **Note:** Some browsers have a hard cap on the number of threads that can be allocated, so it is best to be cautious and keep this number low.


----



[int<class_int>] **threads/godot_pool_size** [🔗<class_EditorExportPlatformWeb_property_threads/godot_pool_size>]

Override for the default size of the [WorkerThreadPool<class_WorkerThreadPool>]. This setting is used when [ProjectSettings.threading/worker_pool/max_threads<class_ProjectSettings_property_threading/worker_pool/max_threads>] size is set to `-1` (which it is by default). This size must be smaller than [threads/emscripten_pool_size<class_EditorExportPlatformWeb_property_threads/emscripten_pool_size>] otherwise deadlocks may occur.

When using threads, this size needs to be large enough to accommodate features that rely on having a dedicated thread like [ProjectSettings.physics/2d/run_on_separate_thread<class_ProjectSettings_property_physics/2d/run_on_separate_thread>] or [ProjectSettings.rendering/driver/threads/thread_model<class_ProjectSettings_property_rendering/driver/threads/thread_model>]. In general, it is best to ensure that this is at least `4` and is at least `2` or `3` less than [threads/emscripten_pool_size<class_EditorExportPlatformWeb_property_threads/emscripten_pool_size>].


----



[bool<class_bool>] **variant/extensions_support** [🔗<class_EditorExportPlatformWeb_property_variant/extensions_support>]

If `true` enables [GDExtension<class_GDExtension>] support for this web build.


----



[bool<class_bool>] **variant/thread_support** [🔗<class_EditorExportPlatformWeb_property_variant/thread_support>]

If `true`, the exported game will support threads. It requires [a "cross-origin isolated" website ](https://web.dev/articles/coop-coep)_, which may be difficult to set up and is limited for security reasons (such as not being able to communicate with third-party websites).

If `false`, the exported game will not support threads. As a result, it is more prone to performance and audio issues, but will only require to be run on an HTTPS website.


----



[bool<class_bool>] **vram_texture_compression/for_desktop** [🔗<class_EditorExportPlatformWeb_property_vram_texture_compression/for_desktop>]

If `true`, allows textures to be optimized for desktop through the S3TC/BPTC algorithm.


----



[bool<class_bool>] **vram_texture_compression/for_mobile** [🔗<class_EditorExportPlatformWeb_property_vram_texture_compression/for_mobile>]

If `true` allows textures to be optimized for mobile through the ETC2/ASTC algorithm.

