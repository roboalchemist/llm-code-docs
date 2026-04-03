:github_url: hide



# OpenXRAndroidThreadSettingsExtension

**Inherits:** [OpenXRExtensionWrapper<class_OpenXRExtensionWrapper>] **<** [Object<class_Object>]

Wraps the [XR_KHR_android_thread_settings ](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_android_thread_settings)_ extension.


## Description

For XR to be comfortable, it is important for applications to deliver frames quickly and consistently. In order to make sure the important application threads get their full share of time, these threads must be identified to the system, which will adjust their scheduling priority accordingly.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`set_application_thread_type<class_OpenXRAndroidThreadSettingsExtension_method_set_application_thread_type>`\ (\ thread_type\: :ref:`ThreadType<enum_OpenXRAndroidThreadSettingsExtension_ThreadType>`, thread_id\: :ref:`int<class_int>` = 0\ ) |
> +-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **ThreadType**: [🔗<enum_OpenXRAndroidThreadSettingsExtension_ThreadType>]



[ThreadType<enum_OpenXRAndroidThreadSettingsExtension_ThreadType>] **THREAD_TYPE_APPLICATION_MAIN** = `0`

Hints to the XR runtime that the thread is doing time critical CPU tasks.



[ThreadType<enum_OpenXRAndroidThreadSettingsExtension_ThreadType>] **THREAD_TYPE_APPLICATION_WORKER** = `1`

Hints to the XR runtime that the thread is doing background CPU tasks.



[ThreadType<enum_OpenXRAndroidThreadSettingsExtension_ThreadType>] **THREAD_TYPE_RENDERER_MAIN** = `2`

Hints to the XR runtime that the thread is doing time critical graphics device tasks.



[ThreadType<enum_OpenXRAndroidThreadSettingsExtension_ThreadType>] **THREAD_TYPE_RENDERER_WORKER** = `3`

Hints to the XR runtime that the thread is doing background graphics device tasks.


----


## Method Descriptions



[bool<class_bool>] **set_application_thread_type**\ (\ thread_type\: [ThreadType<enum_OpenXRAndroidThreadSettingsExtension_ThreadType>], thread_id\: [int<class_int>] = 0\ ) [🔗<class_OpenXRAndroidThreadSettingsExtension_method_set_application_thread_type>]

Sets the thread type of the given thread, so that the XR runtime can adjust its scheduling priority accordingly.

\ `thread_id` refers to the OS thread id (ie from `gettid()`). When `thread_id` is `0`, it will set the thread type of the current thread.

\ **NOTE:** The id returned by [Thread.get_id()<class_Thread_method_get_id>] is incompatible with `thread_id`.

