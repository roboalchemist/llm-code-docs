# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor.PriorityThreadFactory.md.txt

# PriorityThreadPoolExecutor.PriorityThreadFactory

protected static final class **PriorityThreadPoolExecutor.PriorityThreadFactory** extends Object  
implements ThreadFactory  

### Public Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [PriorityThreadPoolExecutor.PriorityThreadFactory](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor.PriorityThreadFactory#PriorityThreadPoolExecutor.PriorityThreadFactory(int))(int threadPriority) |

### Public Method Summary

|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Thread | [newThread](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor.PriorityThreadFactory#newThread(java.lang.Runnable))(Runnable r) |

### Inherited Method Summary

From class java.lang.Object  

|------------------|---------------------------|
| Object           | clone()                   |
| boolean          | equals(Object arg0)       |
| void             | finalize()                |
| final Class\<?\> | getClass()                |
| int              | hashCode()                |
| final void       | notify()                  |
| final void       | notifyAll()               |
| String           | toString()                |
| final void       | wait(long arg0, int arg1) |
| final void       | wait(long arg0)           |
| final void       | wait()                    |

From interface java.util.concurrent.ThreadFactory  

|-----------------|--------------------------|
| abstract Thread | newThread(Runnable arg0) |

## Public Constructors

#### public
**PriorityThreadPoolExecutor.PriorityThreadFactory**
(int threadPriority)

<br />

##### Parameters

|----------------|---|
| threadPriority |   |

## Public Methods

#### public Thread
**newThread**
(Runnable r)

<br />

##### Parameters

|---|---|
| r |   |