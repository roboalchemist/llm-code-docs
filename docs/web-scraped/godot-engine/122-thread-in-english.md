# Thread in English

# Thread
Inherits:RefCounted<Object
A unit of execution in a process.

## Description
A unit of execution in a process. Can run methods onObjects simultaneously. The use of synchronization viaMutexorSemaphoreis advised if working with shared objects.
Warning:To ensure proper cleanup without crashes or deadlocks, when aThread's reference count reaches zero and it is therefore destroyed, the following conditions must be met:
- It must not have anyMutexobjects locked.
It must not have anyMutexobjects locked.
- It must not be waiting on anySemaphoreobjects.
It must not be waiting on anySemaphoreobjects.
- wait_to_finish()should have been called on it.
wait_to_finish()should have been called on it.

## Tutorials
- Using multiple threads
Using multiple threads
- Thread-safe APIs
Thread-safe APIs
- 3D Voxel Demo
3D Voxel Demo

## Methods

| String | get_id()const |
|---|---|
| bool | is_alive()const |
| bool | is_main_thread()static |
| bool | is_started()const |
| void | set_thread_safety_checks_enabled(enabled:bool)static |
| Error | start(callable:Callable, priority:Priority= 1) |
| Variant | wait_to_finish() |

String
get_id()const
bool
is_alive()const
bool
is_main_thread()static
bool
is_started()const
void
set_thread_safety_checks_enabled(enabled:bool)static
Error
start(callable:Callable, priority:Priority= 1)
Variant
wait_to_finish()

## Enumerations
enumPriority:🔗
PriorityPRIORITY_LOW=0
A thread running with lower priority than normally.
PriorityPRIORITY_NORMAL=1
A thread with a standard priority.
PriorityPRIORITY_HIGH=2
A thread running with higher priority than normally.

## Method Descriptions
Stringget_id()const🔗
Returns the currentThread's ID, uniquely identifying it among all threads. If theThreadhas not started running or ifwait_to_finish()has been called, this returns an empty string.
boolis_alive()const🔗
Returnstrueif thisThreadis currently running the provided function. This is useful for determining ifwait_to_finish()can be called without blocking the calling thread.
To check if aThreadis joinable, useis_started().
boolis_main_thread()static🔗
Returnstrueif the thread this method was called from is the main thread.
Note:This is a static method and isn't associated with a specificThreadobject.
boolis_started()const🔗
Returnstrueif thisThreadhas been started. Once started, this will returntrueuntil it is joined usingwait_to_finish(). For checking if aThreadis still executing its task, useis_alive().
voidset_thread_safety_checks_enabled(enabled:bool)static🔗
Sets whether the thread safety checks the engine normally performs in methods of certain classes (e.g.,Node) should happenon the current thread.
The default, for every thread, is that they are enabled (as if called withenabledbeingtrue).
Those checks are conservative. That means that they will only succeed in considering a call thread-safe (and therefore allow it to happen) if the engine can guarantee such safety.
Because of that, there may be cases where the user may want to disable them (enabledbeingfalse) to make certain operations allowed again. By doing so, it becomes the user's responsibility to ensure thread safety (e.g., by usingMutex) for those objects that are otherwise protected by the engine.
Note:This is an advanced usage of the engine. You are advised to use it only if you know what you are doing and there is no safer way.
Note:This is useful for scripts running on either arbitraryThreadobjects or tasks submitted to theWorkerThreadPool. It doesn't apply to code running duringNodegroup processing, where the checks will be always performed.
Note:Even in the case of having disabled the checks in aWorkerThreadPooltask, there's no need to re-enable them at the end. The engine will do so.
Errorstart(callable:Callable, priority:Priority= 1)🔗
Starts a newThreadthat callscallable.
If the method takes some arguments, you can pass them usingCallable.bind().
Thepriorityof theThreadcan be changed by passing a value from thePriorityenum.
Returns@GlobalScope.OKon success, or@GlobalScope.ERR_CANT_CREATEon failure.
Variantwait_to_finish()🔗
Joins theThreadand waits for it to finish. Returns the output of theCallablepassed tostart().
Should either be used when you want to retrieve the value returned from the method called by theThreador before freeing the instance that contains theThread.
To determine if this can be called without blocking the calling thread, check ifis_alive()isfalse.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.