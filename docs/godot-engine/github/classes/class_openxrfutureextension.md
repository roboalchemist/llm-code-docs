:github_url: hide



# OpenXRFutureExtension

**Inherits:** [OpenXRExtensionWrapper<class_OpenXRExtensionWrapper>] **<** [Object<class_Object>]

The OpenXR Future extension allows for asynchronous APIs to be used.


## Description

This is a support extension in OpenXR that allows other OpenXR extensions to start asynchronous functions and get a callback after this function finishes. It is not intended for consumption within GDScript but can be accessed from GDExtension.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`cancel_future<class_OpenXRFutureExtension_method_cancel_future>`\ (\ future\: :ref:`int<class_int>`\ )                                                                |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`is_active<class_OpenXRFutureExtension_method_is_active>`\ (\ ) |const|                                                                                                |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`OpenXRFutureResult<class_OpenXRFutureResult>` | :ref:`register_future<class_OpenXRFutureExtension_method_register_future>`\ (\ future\: :ref:`int<class_int>`, on_success\: :ref:`Callable<class_Callable>` = Callable()\ ) |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **cancel_future**\ (\ future\: [int<class_int>]\ ) [🔗<class_OpenXRFutureExtension_method_cancel_future>]

Cancels an in-progress future. `future` must be an `XrFutureEXT` value previously returned by an API that started an asynchronous function.


----



[bool<class_bool>] **is_active**\ (\ ) |const| [🔗<class_OpenXRFutureExtension_method_is_active>]

Returns `true` if futures are available in the OpenXR runtime used. This function will only return a usable result after OpenXR has been initialized.


----



[OpenXRFutureResult<class_OpenXRFutureResult>] **register_future**\ (\ future\: [int<class_int>], on_success\: [Callable<class_Callable>] = Callable()\ ) [🔗<class_OpenXRFutureExtension_method_register_future>]

Register an OpenXR Future object so we monitor for completion. `future` must be an `XrFutureEXT` value previously returned by an API that started an asynchronous function.

You can optionally specify `on_success`, it will be invoked on successful completion of the future.

Or you can use the returned [OpenXRFutureResult<class_OpenXRFutureResult>] object to `await` its [OpenXRFutureResult.completed<class_OpenXRFutureResult_signal_completed>] signal.

::

    var future_result = OpenXRFutureExtension.register_future(future)
    await future_result.completed
    if future_result.get_status() == OpenXRFutureResult.RESULT_FINISHED:
        # Handle your success
        pass

