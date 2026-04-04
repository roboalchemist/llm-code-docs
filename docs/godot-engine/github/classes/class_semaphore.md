:github_url: hide



# Semaphore

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A synchronization mechanism used to control access to a shared resource by [Thread<class_Thread>]\ s.


## Description

A synchronization semaphore that can be used to synchronize multiple [Thread<class_Thread>]\ s. Initialized to zero on creation. For a binary version, see [Mutex<class_Mutex>].

\ **Warning:** Semaphores must be used carefully to avoid deadlocks.

\ **Warning:** To guarantee that the operating system is able to perform proper cleanup (no crashes, no deadlocks), these conditions must be met:

- When a **Semaphore**'s reference count reaches zero and it is therefore destroyed, no threads must be waiting on it.

- When a [Thread<class_Thread>]'s reference count reaches zero and it is therefore destroyed, it must not be waiting on any semaphore.


## Tutorials

- [../tutorials/performance/using_multiple_threads](Using multiple threads .md)

- [../tutorials/performance/thread_safe_apis](Thread-safe APIs .md)


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+-----------------------------------------------------------------------------------+
> | |void|                  | :ref:`post<class_Semaphore_method_post>`\ (\ count\: :ref:`int<class_int>` = 1\ ) |
> +-------------------------+-----------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`try_wait<class_Semaphore_method_try_wait>`\ (\ )                            |
> +-------------------------+-----------------------------------------------------------------------------------+
> | |void|                  | :ref:`wait<class_Semaphore_method_wait>`\ (\ )                                    |
> +-------------------------+-----------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **post**\ (\ count\: [int<class_int>] = 1\ ) [🔗<class_Semaphore_method_post>]

Lowers the **Semaphore**, allowing one thread in, or more if `count` is specified.


----



[bool<class_bool>] **try_wait**\ (\ ) [🔗<class_Semaphore_method_try_wait>]

Like [wait()<class_Semaphore_method_wait>], but won't block, so if the value is zero, fails immediately and returns `false`. If non-zero, it returns `true` to report success.


----



|void| **wait**\ (\ ) [🔗<class_Semaphore_method_wait>]

Waits for the **Semaphore**, if its value is zero, blocks until non-zero.

