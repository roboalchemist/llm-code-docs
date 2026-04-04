# Timer

# Timer

Inherits:Node<Object
A countdown timer.

## Description

TheTimernode is a countdown timer and is the simplest way to handle time-based logic in the engine. When a timer reaches the end of itswait_time, it will emit thetimeoutsignal.
After a timer enters the scene tree, it can be manually started withstart(). A timer node is also started automatically ifautostartistrue.
Without requiring much code, a timer node can be added and configured in the editor. Thetimeoutsignal it emits can also be connected through the Signals dock in the editor:

```
func _on_timer_timeout():
    print("Time to attack!")
```

Note:To create a one-shot timer without instantiating a node, useSceneTree.create_timer().
Note:Timers are affected byEngine.time_scaleunlessignore_time_scaleistrue. The higher the time scale, the sooner timers will end. How often a timer processes may depend on the framerate orEngine.physics_ticks_per_second.

## Tutorials

- 2D Dodge The Creeps Demo
2D Dodge The Creeps Demo

## Properties

| bool | autostart | false |
|---|---|---|
| bool | ignore_time_scale | false |
| bool | one_shot | false |
| bool | paused |  |
| TimerProcessCallback | process_callback | 1 |
| float | time_left |  |
| float | wait_time | 1.0 |

bool
autostart
false
bool
ignore_time_scale
false
bool
one_shot
false
bool
paused
TimerProcessCallback
process_callback
float
time_left
float
wait_time

## Methods

| bool | is_stopped()const |
|---|---|
| void | start(time_sec:float= -1) |
| void | stop() |

bool
is_stopped()const
void
start(time_sec:float= -1)
void
stop()

## Signals

timeout()🔗
Emitted when the timer reaches the end.

## Enumerations

enumTimerProcessCallback:🔗
TimerProcessCallbackTIMER_PROCESS_PHYSICS=0
Update the timer every physics process frame (seeNode.NOTIFICATION_INTERNAL_PHYSICS_PROCESS).
TimerProcessCallbackTIMER_PROCESS_IDLE=1
Update the timer every process (rendered) frame (seeNode.NOTIFICATION_INTERNAL_PROCESS).

## Property Descriptions

boolautostart=false🔗

- voidset_autostart(value:bool)
voidset_autostart(value:bool)
- boolhas_autostart()
boolhas_autostart()
Iftrue, the timer will start immediately when it enters the scene tree.
Note:After the timer enters the tree, this property is automatically set tofalse.
Note:This property does nothing when the timer is running in the editor.
boolignore_time_scale=false🔗
- voidset_ignore_time_scale(value:bool)
voidset_ignore_time_scale(value:bool)
- boolis_ignoring_time_scale()
boolis_ignoring_time_scale()
Iftrue, the timer will ignoreEngine.time_scaleand update with the real, elapsed time.
boolone_shot=false🔗
- voidset_one_shot(value:bool)
voidset_one_shot(value:bool)
- boolis_one_shot()
boolis_one_shot()
Iftrue, the timer will stop after reaching the end. Otherwise, as by default, the timer will automatically restart.
boolpaused🔗
- voidset_paused(value:bool)
voidset_paused(value:bool)
- boolis_paused()
boolis_paused()
Iftrue, the timer is paused. A paused timer does not process until this property is set back tofalse, even whenstart()is called. See alsostop().
TimerProcessCallbackprocess_callback=1🔗
- voidset_timer_process_callback(value:TimerProcessCallback)
voidset_timer_process_callback(value:TimerProcessCallback)
- TimerProcessCallbackget_timer_process_callback()
TimerProcessCallbackget_timer_process_callback()
Specifies when the timer is updated during the main loop.
floattime_left🔗
- floatget_time_left()
floatget_time_left()
The timer's remaining time in seconds. This is always0if the timer is stopped.
Note:This property is read-only and cannot be modified. It is based onwait_time.
floatwait_time=1.0🔗
- voidset_wait_time(value:float)
voidset_wait_time(value:float)
- floatget_wait_time()
floatget_wait_time()
The time required for the timer to end, in seconds. This property can also be set every timestart()is called.
Note:Timers can only process once per physics or process frame (depending on theprocess_callback). An unstable framerate may cause the timer to end inconsistently, which is especially noticeable if the wait time is lower than roughly0.05seconds. For very short timers, it is recommended to write your own code instead of using aTimernode. Timers are also affected byEngine.time_scale.

## Method Descriptions

boolis_stopped()const🔗
Returnstrueif the timer is stopped or has not started.
voidstart(time_sec:float= -1)🔗
Starts the timer, or resets the timer if it was started already. Fails if the timer is not inside the scene tree. Iftime_secis greater than0, this value is used for thewait_time.
Note:This method does not resume a paused timer. Seepaused.
voidstop()🔗
Stops the timer. See alsopaused. Unlikestart(), this can safely be called if the timer is not inside the scene tree.
Note:Callingstop()does not emit thetimeoutsignal, as the timer is not considered to have timed out. If this is desired, use$Timer.timeout.emit()after callingstop()to manually emit the signal.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
