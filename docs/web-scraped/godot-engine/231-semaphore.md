# Semaphore

# Semaphore
Inherits:RefCounted<Object
A synchronization mechanism used to control access to a shared resource byThreads.

## Description
A synchronization semaphore that can be used to synchronize multipleThreads. Initialized to zero on creation. For a binary version, seeMutex.
Warning:Semaphores must be used carefully to avoid deadlocks.
Warning:To guarantee that the operating system is able to perform proper cleanup (no crashes, no deadlocks), these conditions must be met:
- When aSemaphore's reference count reaches zero and it is therefore destroyed, no threads must be waiting on it.
When aSemaphore's reference count reaches zero and it is therefore destroyed, no threads must be waiting on it.
- When aThread's reference count reaches zero and it is therefore destroyed, it must not be waiting on any semaphore.
When aThread's reference count reaches zero and it is therefore destroyed, it must not be waiting on any semaphore.

## Tutorials
- Using multiple threads
Using multiple threads
- Thread-safe APIs
Thread-safe APIs

## Methods

| void | post(count:int= 1) |
|---|---|
| bool | try_wait() |
| void | wait() |

void
post(count:int= 1)
bool
try_wait()
void
wait()

## Method Descriptions
voidpost(count:int= 1)🔗
Lowers theSemaphore, allowing one thread in, or more ifcountis specified.
booltry_wait()🔗
Likewait(), but won't block, so if the value is zero, fails immediately and returnsfalse. If non-zero, it returnstrueto report success.
voidwait()🔗
Waits for theSemaphore, if its value is zero, blocks until non-zero.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.