:github_url: hide



# Mutex

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A binary [Semaphore<class_Semaphore>] for synchronization of multiple [Thread<class_Thread>]\ s.


## Description

A synchronization mutex (mutual exclusion). This is used to synchronize multiple [Thread<class_Thread>]\ s, and is equivalent to a binary [Semaphore<class_Semaphore>]. It guarantees that only one thread can access a critical section at a time.

This is a reentrant mutex, meaning that it can be locked multiple times by one thread, provided it also unlocks it as many times.

\ **Warning:** To ensure proper cleanup without crashes or deadlocks, the following conditions must be met:

- When a **Mutex**'s reference count reaches zero and it is therefore destroyed, no threads (including the one on which the destruction will happen) must have it locked.

- When a [Thread<class_Thread>]'s reference count reaches zero and it is therefore destroyed, it must not have any mutex locked.


## Tutorials

- [../tutorials/performance/using_multiple_threads](Using multiple threads .md)

- [../tutorials/performance/thread_safe_apis](Thread-safe APIs .md)


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+----------------------------------------------------+
> | |void|                  | :ref:`lock<class_Mutex_method_lock>`\ (\ )         |
> +-------------------------+----------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`try_lock<class_Mutex_method_try_lock>`\ (\ ) |
> +-------------------------+----------------------------------------------------+
> | |void|                  | :ref:`unlock<class_Mutex_method_unlock>`\ (\ )     |
> +-------------------------+----------------------------------------------------+
>

----


## Method Descriptions



|void| **lock**\ (\ ) [🔗<class_Mutex_method_lock>]

Locks this **Mutex**, blocks until it is unlocked by the current owner.

\ **Note:** This function returns without blocking if the thread already has ownership of the mutex.


----



[bool<class_bool>] **try_lock**\ (\ ) [🔗<class_Mutex_method_try_lock>]

Tries locking this **Mutex**, but does not block. Returns `true` on success, `false` otherwise.

\ **Note:** This function returns `true` if the thread already has ownership of the mutex.


----



|void| **unlock**\ (\ ) [🔗<class_Mutex_method_unlock>]

Unlocks this **Mutex**, leaving it to other threads.

\ **Note:** If a thread called [lock()<class_Mutex_method_lock>] or [try_lock()<class_Mutex_method_try_lock>] multiple times while already having ownership of the mutex, it must also call [unlock()<class_Mutex_method_unlock>] the same number of times in order to unlock it correctly.

\ **Warning:** Calling [unlock()<class_Mutex_method_unlock>] more times than [lock()<class_Mutex_method_lock>] on a given thread, thus ending up trying to unlock a non-locked mutex, is wrong and may causes crashes or deadlocks.

