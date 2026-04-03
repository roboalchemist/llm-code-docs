:github_url: hide



# OpenXRFutureResult

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Result object tracking the asynchronous result of an OpenXR Future object.


## Description

Result object tracking the asynchronous result of an OpenXR Future object, you can use this object to track the result status.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`cancel_future<class_OpenXRFutureResult_method_cancel_future>`\ (\ )                                                     |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                     | :ref:`get_future<class_OpenXRFutureResult_method_get_future>`\ (\ ) |const|                                                   |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                             | :ref:`get_result_value<class_OpenXRFutureResult_method_get_result_value>`\ (\ ) |const|                                       |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ResultStatus<enum_OpenXRFutureResult_ResultStatus>` | :ref:`get_status<class_OpenXRFutureResult_method_get_status>`\ (\ ) |const|                                                   |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`set_result_value<class_OpenXRFutureResult_method_set_result_value>`\ (\ result_value\: :ref:`Variant<class_Variant>`\ ) |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**completed**\ (\ result\: [OpenXRFutureResult<class_OpenXRFutureResult>]\ ) [🔗<class_OpenXRFutureResult_signal_completed>]

Emitted when the asynchronous function is finished or has been cancelled.


----


## Enumerations



enum **ResultStatus**: [🔗<enum_OpenXRFutureResult_ResultStatus>]



[ResultStatus<enum_OpenXRFutureResult_ResultStatus>] **RESULT_RUNNING** = `0`

The asynchronous function is running.



[ResultStatus<enum_OpenXRFutureResult_ResultStatus>] **RESULT_FINISHED** = `1`

The asynchronous function has finished.



[ResultStatus<enum_OpenXRFutureResult_ResultStatus>] **RESULT_CANCELLED** = `2`

The asynchronous function has been cancelled.


----


## Method Descriptions



|void| **cancel_future**\ (\ ) [🔗<class_OpenXRFutureResult_method_cancel_future>]

Cancel this future, this will interrupt and stop the asynchronous function.


----



[int<class_int>] **get_future**\ (\ ) |const| [🔗<class_OpenXRFutureResult_method_get_future>]

Return the `XrFutureEXT` value this result relates to.


----



[Variant<class_Variant>] **get_result_value**\ (\ ) |const| [🔗<class_OpenXRFutureResult_method_get_result_value>]

Returns the result value of our asynchronous function (if set by the extension). The type of this result value depends on the function being called. Consult the documentation of the relevant function.


----



[ResultStatus<enum_OpenXRFutureResult_ResultStatus>] **get_status**\ (\ ) |const| [🔗<class_OpenXRFutureResult_method_get_status>]

Returns the status of this result.


----



|void| **set_result_value**\ (\ result_value\: [Variant<class_Variant>]\ ) [🔗<class_OpenXRFutureResult_method_set_result_value>]

Stores the result value we expose to the user.

\ **Note:** This method should only be called by an OpenXR extension that implements an asynchronous function.

