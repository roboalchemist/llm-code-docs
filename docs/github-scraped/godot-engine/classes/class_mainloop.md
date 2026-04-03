:github_url: hide



# MainLoop

**Inherits:** [Object<class_Object>]

**Inherited By:** [SceneTree<class_SceneTree>]

Abstract base class for the game's main loop.


## Description

**MainLoop** is the abstract base class for a Godot project's game loop. It is inherited by [SceneTree<class_SceneTree>], which is the default game loop implementation used in Godot projects, though it is also possible to write and use one's own **MainLoop** subclass instead of the scene tree.

Upon the application start, a **MainLoop** implementation must be provided to the OS; otherwise, the application will exit. This happens automatically (and a [SceneTree<class_SceneTree>] is created) unless a **MainLoop** [Script<class_Script>] is provided from the command line (with e.g. `godot -s my_loop.gd`) or the [ProjectSettings.application/run/main_loop_type<class_ProjectSettings_property_application/run/main_loop_type>] project setting is overwritten.

Here is an example script implementing a simple **MainLoop**:


> **TABS**
>

    class_name CustomMainLoop
    extends MainLoop

    var time_elapsed = 0

    func _initialize():
        print("Initialized:")
        print("  Starting time: %s" % str(time_elapsed))

    func _process(delta):
        time_elapsed += delta
        # Return true to end the main loop.
        return Input.get_mouse_button_mask() != 0 || Input.is_key_pressed(KEY_ESCAPE)

    func _finalize():
        print("Finalized:")
        print("  End time: %s" % str(time_elapsed))


    using Godot;

    [GlobalClass]
    public partial class CustomMainLoop : MainLoop
    {
        private double _timeElapsed = 0;

        public override void _Initialize()
        {
            GD.Print("Initialized:");
            GD.Print($"  Starting Time: {_timeElapsed}");
        }

        public override bool _Process(double delta)
        {
            _timeElapsed += delta;
            // Return true to end the main loop.
            return Input.GetMouseButtonMask() != 0 || Input.IsKeyPressed(Key.Escape);
        }

        private void _Finalize()
        {
            GD.Print("Finalized:");
            GD.Print($"  End Time: {_timeElapsed}");
## }




## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+----------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`_finalize<class_MainLoop_private_method__finalize>`\ (\ ) |virtual|                                                  |
> +-------------------------+----------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`_initialize<class_MainLoop_private_method__initialize>`\ (\ ) |virtual|                                              |
> +-------------------------+----------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`_physics_process<class_MainLoop_private_method__physics_process>`\ (\ delta\: :ref:`float<class_float>`\ ) |virtual| |
> +-------------------------+----------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`_process<class_MainLoop_private_method__process>`\ (\ delta\: :ref:`float<class_float>`\ ) |virtual|                 |
> +-------------------------+----------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**on_request_permissions_result**\ (\ permission\: [String<class_String>], granted\: [bool<class_bool>]\ ) [🔗<class_MainLoop_signal_on_request_permissions_result>]

Emitted when a user responds to a permission request.


----


## Constants



**NOTIFICATION_OS_MEMORY_WARNING** = `2009` [🔗<class_MainLoop_constant_NOTIFICATION_OS_MEMORY_WARNING>]

Notification received from the OS when the application is exceeding its allocated memory.

Specific to the iOS platform.



**NOTIFICATION_TRANSLATION_CHANGED** = `2010` [🔗<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>]

Notification received when translations may have changed. Can be triggered by the user changing the locale. Can be used to respond to language changes, for example to change the UI strings on the fly. Useful when working with the built-in translation support, like [Object.tr()<class_Object_method_tr>].



**NOTIFICATION_WM_ABOUT** = `2011` [🔗<class_MainLoop_constant_NOTIFICATION_WM_ABOUT>]

Notification received from the OS when a request for "About" information is sent.

Specific to the macOS platform.



**NOTIFICATION_CRASH** = `2012` [🔗<class_MainLoop_constant_NOTIFICATION_CRASH>]

Notification received from Godot's crash handler when the engine is about to crash.

Implemented on desktop platforms if the crash handler is enabled.



**NOTIFICATION_OS_IME_UPDATE** = `2013` [🔗<class_MainLoop_constant_NOTIFICATION_OS_IME_UPDATE>]

Notification received from the OS when an update of the Input Method Engine occurs (e.g. change of IME cursor position or composition string).

Implemented on desktop and web platforms.



**NOTIFICATION_APPLICATION_RESUMED** = `2014` [🔗<class_MainLoop_constant_NOTIFICATION_APPLICATION_RESUMED>]

Notification received from the OS when the application is resumed.

Specific to the Android and iOS platforms.



**NOTIFICATION_APPLICATION_PAUSED** = `2015` [🔗<class_MainLoop_constant_NOTIFICATION_APPLICATION_PAUSED>]

Notification received from the OS when the application is paused.

Specific to the Android and iOS platforms.

\ **Note:** On iOS, you only have approximately 5 seconds to finish a task started by this signal. If you go over this allotment, iOS will kill the app instead of pausing it.



**NOTIFICATION_APPLICATION_FOCUS_IN** = `2016` [🔗<class_MainLoop_constant_NOTIFICATION_APPLICATION_FOCUS_IN>]

Notification received from the OS when the application is focused, i.e. when changing the focus from the OS desktop or a thirdparty application to any open window of the Godot instance.

Implemented on desktop and mobile platforms.



**NOTIFICATION_APPLICATION_FOCUS_OUT** = `2017` [🔗<class_MainLoop_constant_NOTIFICATION_APPLICATION_FOCUS_OUT>]

Notification received from the OS when the application is defocused, i.e. when changing the focus from any open window of the Godot instance to the OS desktop or a thirdparty application.

Implemented on desktop and mobile platforms.



**NOTIFICATION_TEXT_SERVER_CHANGED** = `2018` [🔗<class_MainLoop_constant_NOTIFICATION_TEXT_SERVER_CHANGED>]

Notification received when text server is changed.


----


## Method Descriptions



|void| **_finalize**\ (\ ) |virtual| [🔗<class_MainLoop_private_method__finalize>]

Called before the program exits.


----



|void| **_initialize**\ (\ ) |virtual| [🔗<class_MainLoop_private_method__initialize>]

Called once during initialization.


----



[bool<class_bool>] **_physics_process**\ (\ delta\: [float<class_float>]\ ) |virtual| [🔗<class_MainLoop_private_method__physics_process>]

Called each physics tick. `delta` is the logical time between physics ticks in seconds and is equal to [Engine.time_scale<class_Engine_property_time_scale>] / [Engine.physics_ticks_per_second<class_Engine_property_physics_ticks_per_second>]. Equivalent to [Node._physics_process()<class_Node_private_method__physics_process>].

If implemented, the method must return a boolean value. `true` ends the main loop, while `false` lets it proceed to the next step.

\ **Note:** [_physics_process()<class_MainLoop_private_method__physics_process>] may be called up to [Engine.max_physics_steps_per_frame<class_Engine_property_max_physics_steps_per_frame>] times per (idle) frame. This step limit may be reached when the engine is suffering performance issues.

\ **Note:** Accumulated `delta` may diverge from real world seconds.


----



[bool<class_bool>] **_process**\ (\ delta\: [float<class_float>]\ ) |virtual| [🔗<class_MainLoop_private_method__process>]

Called on each idle frame, prior to rendering, and after physics ticks have been processed. `delta` is the time between frames in seconds. Equivalent to [Node._process()<class_Node_private_method__process>].

If implemented, the method must return a boolean value. `true` ends the main loop, while `false` lets it proceed to the next frame.

\ **Note:** When the engine is struggling and the frame rate is lowered, `delta` will increase. When `delta` is increased, it's capped at a maximum of [Engine.time_scale<class_Engine_property_time_scale>] \* [Engine.max_physics_steps_per_frame<class_Engine_property_max_physics_steps_per_frame>] / [Engine.physics_ticks_per_second<class_Engine_property_physics_ticks_per_second>]. As a result, accumulated `delta` may not represent real world time.

\ **Note:** When `--fixed-fps` is enabled or the engine is running in Movie Maker mode (see [MovieWriter<class_MovieWriter>]), process `delta` will always be the same for every frame, regardless of how much time the frame took to render.

\ **Note:** Frame delta may be post-processed by [OS.delta_smoothing<class_OS_property_delta_smoothing>] if this is enabled for the project.

