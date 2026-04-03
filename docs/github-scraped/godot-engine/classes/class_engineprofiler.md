:github_url: hide



# EngineProfiler

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Base class for creating custom profilers.


## Description

This class can be used to implement custom profilers that are able to interact with the engine and editor debugger.

See [EngineDebugger<class_EngineDebugger>] and [EditorDebuggerPlugin<class_EditorDebuggerPlugin>] for more information.


## Methods

> **TABLE**
> :widths: auto
>
> +--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`_add_frame<class_EngineProfiler_private_method__add_frame>`\ (\ data\: :ref:`Array<class_Array>`\ ) |virtual|                                                                                                                                 |
> +--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`_tick<class_EngineProfiler_private_method__tick>`\ (\ frame_time\: :ref:`float<class_float>`, process_time\: :ref:`float<class_float>`, physics_time\: :ref:`float<class_float>`, physics_frame_time\: :ref:`float<class_float>`\ ) |virtual| |
> +--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`_toggle<class_EngineProfiler_private_method__toggle>`\ (\ enable\: :ref:`bool<class_bool>`, options\: :ref:`Array<class_Array>`\ ) |virtual|                                                                                                  |
> +--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **_add_frame**\ (\ data\: [Array<class_Array>]\ ) |virtual| [🔗<class_EngineProfiler_private_method__add_frame>]

Called when data is added to profiler using [EngineDebugger.profiler_add_frame_data()<class_EngineDebugger_method_profiler_add_frame_data>].


----



|void| **_tick**\ (\ frame_time\: [float<class_float>], process_time\: [float<class_float>], physics_time\: [float<class_float>], physics_frame_time\: [float<class_float>]\ ) |virtual| [🔗<class_EngineProfiler_private_method__tick>]

Called once every engine iteration when the profiler is active with information about the current frame. All time values are in seconds. Lower values represent faster processing times and are therefore considered better.


----



|void| **_toggle**\ (\ enable\: [bool<class_bool>], options\: [Array<class_Array>]\ ) |virtual| [🔗<class_EngineProfiler_private_method__toggle>]

Called when the profiler is enabled/disabled, along with a set of `options`.

