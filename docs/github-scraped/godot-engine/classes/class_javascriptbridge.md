:github_url: hide



# JavaScriptBridge

**Inherits:** [Object<class_Object>]

Singleton that connects the engine with the browser's JavaScript context in Web export.


## Description

The JavaScriptBridge singleton is implemented only in the Web export. It's used to access the browser's JavaScript context. This allows interaction with embedding pages or calling third-party JavaScript APIs.

\ **Note:** This singleton can be disabled at build-time to improve security. By default, the JavaScriptBridge singleton is enabled. Official export templates also have the JavaScriptBridge singleton enabled. See [../engine_details/development/compiling/compiling_for_web](Compiling for the Web .md) in the documentation for more information.


## Tutorials

- [../tutorials/platform/web/javascript_bridge](The JavaScriptBridge singleton .md)


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`JavaScriptObject<class_JavaScriptObject>` | :ref:`create_callback<class_JavaScriptBridge_method_create_callback>`\ (\ callable\: :ref:`Callable<class_Callable>`\ )                                                                                                                  |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                   | :ref:`create_object<class_JavaScriptBridge_method_create_object>`\ (\ object\: :ref:`String<class_String>`, ...\ ) |vararg|                                                                                                              |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`download_buffer<class_JavaScriptBridge_method_download_buffer>`\ (\ buffer\: :ref:`PackedByteArray<class_PackedByteArray>`, name\: :ref:`String<class_String>`, mime\: :ref:`String<class_String>` = "application/octet-stream"\ ) |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                   | :ref:`eval<class_JavaScriptBridge_method_eval>`\ (\ code\: :ref:`String<class_String>`, use_global_execution_context\: :ref:`bool<class_bool>` = false\ )                                                                                |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`force_fs_sync<class_JavaScriptBridge_method_force_fs_sync>`\ (\ )                                                                                                                                                                  |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`JavaScriptObject<class_JavaScriptObject>` | :ref:`get_interface<class_JavaScriptBridge_method_get_interface>`\ (\ interface\: :ref:`String<class_String>`\ )                                                                                                                         |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`is_js_buffer<class_JavaScriptBridge_method_is_js_buffer>`\ (\ javascript_object\: :ref:`JavaScriptObject<class_JavaScriptObject>`\ )                                                                                               |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>`   | :ref:`js_buffer_to_packed_byte_array<class_JavaScriptBridge_method_js_buffer_to_packed_byte_array>`\ (\ javascript_buffer\: :ref:`JavaScriptObject<class_JavaScriptObject>`\ )                                                           |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`pwa_needs_update<class_JavaScriptBridge_method_pwa_needs_update>`\ (\ ) |const|                                                                                                                                                    |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`           | :ref:`pwa_update<class_JavaScriptBridge_method_pwa_update>`\ (\ )                                                                                                                                                                        |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**pwa_update_available**\ (\ ) [🔗<class_JavaScriptBridge_signal_pwa_update_available>]

Emitted when an update for this progressive web app has been detected but is waiting to be activated because a previous version is active. See [pwa_update()<class_JavaScriptBridge_method_pwa_update>] to force the update to take place immediately.


----


## Method Descriptions



[JavaScriptObject<class_JavaScriptObject>] **create_callback**\ (\ callable\: [Callable<class_Callable>]\ ) [🔗<class_JavaScriptBridge_method_create_callback>]

Creates a reference to a [Callable<class_Callable>] that can be used as a callback by JavaScript. The reference must be kept until the callback happens, or it won't be called at all. See [JavaScriptObject<class_JavaScriptObject>] for usage.

\ **Note:** The callback function must take exactly one [Array<class_Array>] argument, which is going to be the JavaScript [arguments object ](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)_ converted to an array.


----



[Variant<class_Variant>] **create_object**\ (\ object\: [String<class_String>], ...\ ) |vararg| [🔗<class_JavaScriptBridge_method_create_object>]

Creates a new JavaScript object using the `new` constructor. The `object` must a valid property of the JavaScript `window`. See [JavaScriptObject<class_JavaScriptObject>] for usage.


----



|void| **download_buffer**\ (\ buffer\: [PackedByteArray<class_PackedByteArray>], name\: [String<class_String>], mime\: [String<class_String>] = "application/octet-stream"\ ) [🔗<class_JavaScriptBridge_method_download_buffer>]

Prompts the user to download a file containing the specified `buffer`. The file will have the given `name` and `mime` type.

\ **Note:** The browser may override the [MIME type ](https://en.wikipedia.org/wiki/Media_type)_ provided based on the file `name`'s extension.

\ **Note:** Browsers might block the download if [download_buffer()<class_JavaScriptBridge_method_download_buffer>] is not being called from a user interaction (e.g. button click).

\ **Note:** Browsers might ask the user for permission or block the download if multiple download requests are made in a quick succession.


----



[Variant<class_Variant>] **eval**\ (\ code\: [String<class_String>], use_global_execution_context\: [bool<class_bool>] = false\ ) [🔗<class_JavaScriptBridge_method_eval>]

Execute the string `code` as JavaScript code within the browser window. This is a call to the actual global JavaScript function `eval()`.

If `use_global_execution_context` is `true`, the code will be evaluated in the global execution context. Otherwise, it is evaluated in the execution context of a function within the engine's runtime environment.


----



|void| **force_fs_sync**\ (\ ) [🔗<class_JavaScriptBridge_method_force_fs_sync>]

Force synchronization of the persistent file system (when enabled).

\ **Note:** This is only useful for modules or extensions that can't use [FileAccess<class_FileAccess>] to write files.


----



[JavaScriptObject<class_JavaScriptObject>] **get_interface**\ (\ interface\: [String<class_String>]\ ) [🔗<class_JavaScriptBridge_method_get_interface>]

Returns an interface to a JavaScript object that can be used by scripts. The `interface` must be a valid property of the JavaScript `window`. The callback must accept a single [Array<class_Array>] argument, which will contain the JavaScript `arguments`. See [JavaScriptObject<class_JavaScriptObject>] for usage.


----



[bool<class_bool>] **is_js_buffer**\ (\ javascript_object\: [JavaScriptObject<class_JavaScriptObject>]\ ) [🔗<class_JavaScriptBridge_method_is_js_buffer>]

Returns `true` if the given `javascript_object` is of type [[code]ArrayBuffer[/code] ](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)_, [[code]DataView[/code] ](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView)_, or one of the many [typed array objects ](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)_.


----



[PackedByteArray<class_PackedByteArray>] **js_buffer_to_packed_byte_array**\ (\ javascript_buffer\: [JavaScriptObject<class_JavaScriptObject>]\ ) [🔗<class_JavaScriptBridge_method_js_buffer_to_packed_byte_array>]

Returns a copy of `javascript_buffer`'s contents as a [PackedByteArray<class_PackedByteArray>]. See also [is_js_buffer()<class_JavaScriptBridge_method_is_js_buffer>].


----



[bool<class_bool>] **pwa_needs_update**\ (\ ) |const| [🔗<class_JavaScriptBridge_method_pwa_needs_update>]

Returns `true` if a new version of the progressive web app is waiting to be activated.

\ **Note:** Only relevant when exported as a Progressive Web App.


----



[Error<enum_@GlobalScope_Error>] **pwa_update**\ (\ ) [🔗<class_JavaScriptBridge_method_pwa_update>]

Performs the live update of the progressive web app. Forcing the new version to be installed and the page to be reloaded.

\ **Note:** Your application will be **reloaded in all browser tabs**.

\ **Note:** Only relevant when exported as a Progressive Web App and [pwa_needs_update()<class_JavaScriptBridge_method_pwa_needs_update>] returns `true`.

