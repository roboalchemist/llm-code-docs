# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue.md.txt

# DependencyPriorityBlockingQueue

public class **DependencyPriorityBlockingQueue** extends PriorityBlockingQueue\<E extends [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency) \& [Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task) \& [PriorityProvider](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityProvider)\>  
The DependencyPriorityBlockingQueue provides all functionality of a [PriorityBlockingQueue](https://firebase.google.com/docs/reference/androidreference/java/util/concurrent/PriorityBlockingQueue)
while simultaneously supporting task dependencies using the [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency)
interface.
An independent worker is guaranteed to complete before the dependent worker that specifies it.
Priorities are specified by the worker extending the [Priority](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Priority)
class.
When Priorities and Dependencies conflict, the expectation in a dependency chain is that the
entire chain will run at the priority specified by the independent worker.
No effort is made to guarantee all dependencies are satisfied. Responsibility falls on outside
components to validate the dependency graph for complete execution.  

### Public Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [DependencyPriorityBlockingQueue](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue#DependencyPriorityBlockingQueue())() |

### Public Method Summary

|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void        | [clear](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue#clear())()                                                                                                           |
| boolean     | [contains](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue#contains(java.lang.Object))(Object o)                                                                             |
| int         | [drainTo](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue#drainTo(java.util.Collection<? super E>, int))(Collection\<? super E\> c, int maxElements)                         |
| int         | [drainTo](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue#drainTo(java.util.Collection<? super E>))(Collection\<? super E\> c)                                               |
| E           | [peek](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue#peek())()                                                                                                             |
| E           | [poll](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue#poll(long, java.util.concurrent.TimeUnit))(long timeout, TimeUnit unit)                                               |
| E           | [poll](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue#poll())()                                                                                                             |
| void        | [recycleBlockedQueue](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue#recycleBlockedQueue())() Removes all items from blocked Queue and inserts into primary queue to retry. |
| boolean     | [remove](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue#remove(java.lang.Object))(Object o)                                                                                 |
| boolean     | [removeAll](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue#removeAll(java.util.Collection<?>))(Collection\<?\> collection)                                                  |
| int         | [size](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue#size())()                                                                                                             |
| E           | [take](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue#take())()                                                                                                             |
| \<T\> T\[\] | [toArray](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue#toArray(T[]))(T\[\] a)                                                                                             |
| Object\[\]  | [toArray](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/DependencyPriorityBlockingQueue#toArray())()                                                                                                       |

### Inherited Method Summary

From class java.util.concurrent.PriorityBlockingQueue  

|-------------------------|-------------------------------------------------|
| boolean                 | add(E arg0)                                     |
| void                    | clear()                                         |
| Comparator\<? super E\> | comparator()                                    |
| boolean                 | contains(Object arg0)                           |
| int                     | drainTo(Collection\<? super E\> arg0, int arg1) |
| int                     | drainTo(Collection\<? super E\> arg0)           |
| Iterator\<E\>           | iterator()                                      |
| boolean                 | offer(E arg0)                                   |
| boolean                 | offer(E arg0, long arg1, TimeUnit arg2)         |
| E                       | peek()                                          |
| E                       | poll(long arg0, TimeUnit arg1)                  |
| E                       | poll()                                          |
| void                    | put(E arg0)                                     |
| int                     | remainingCapacity()                             |
| boolean                 | remove(Object arg0)                             |
| int                     | size()                                          |
| Spliterator\<E\>        | spliterator()                                   |
| E                       | take()                                          |
| \<T\> T\[\]             | toArray(T\[\] arg0)                             |
| Object\[\]              | toArray()                                       |
| String                  | toString()                                      |

From class java.util.AbstractQueue  

|---------|----------------------------------------|
| boolean | add(E arg0)                            |
| boolean | addAll(Collection\<? extends E\> arg0) |
| void    | clear()                                |
| E       | element()                              |
| E       | remove()                               |

From class java.util.AbstractCollection  

|------------------------|----------------------------------------|
| boolean                | add(E arg0)                            |
| boolean                | addAll(Collection\<? extends E\> arg0) |
| void                   | clear()                                |
| boolean                | contains(Object arg0)                  |
| boolean                | containsAll(Collection\<?\> arg0)      |
| boolean                | isEmpty()                              |
| abstract Iterator\<E\> | iterator()                             |
| boolean                | remove(Object arg0)                    |
| boolean                | removeAll(Collection\<?\> arg0)        |
| boolean                | retainAll(Collection\<?\> arg0)        |
| abstract int           | size()                                 |
| \<T\> T\[\]            | toArray(T\[\] arg0)                    |
| Object\[\]             | toArray()                              |
| String                 | toString()                             |

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

From interface java.util.concurrent.BlockingQueue  

|------------------|-------------------------------------------------|
| abstract boolean | add(E arg0)                                     |
| abstract boolean | contains(Object arg0)                           |
| abstract int     | drainTo(Collection\<? super E\> arg0)           |
| abstract int     | drainTo(Collection\<? super E\> arg0, int arg1) |
| abstract boolean | offer(E arg0)                                   |
| abstract boolean | offer(E arg0, long arg1, TimeUnit arg2)         |
| abstract E       | poll(long arg0, TimeUnit arg1)                  |
| abstract void    | put(E arg0)                                     |
| abstract int     | remainingCapacity()                             |
| abstract boolean | remove(Object arg0)                             |
| abstract E       | take()                                          |

From interface java.util.Queue  

|------------------|---------------|
| abstract boolean | add(E arg0)   |
| abstract E       | element()     |
| abstract boolean | offer(E arg0) |
| abstract E       | peek()        |
| abstract E       | poll()        |
| abstract E       | remove()      |

From interface java.util.Collection  

|------------------------|----------------------------------------|
| abstract boolean       | add(E arg0)                            |
| abstract boolean       | addAll(Collection\<? extends E\> arg0) |
| abstract void          | clear()                                |
| abstract boolean       | contains(Object arg0)                  |
| abstract boolean       | containsAll(Collection\<?\> arg0)      |
| abstract boolean       | equals(Object arg0)                    |
| abstract int           | hashCode()                             |
| abstract boolean       | isEmpty()                              |
| abstract Iterator\<E\> | iterator()                             |
| Stream\<E\>            | parallelStream()                       |
| abstract boolean       | remove(Object arg0)                    |
| abstract boolean       | removeAll(Collection\<?\> arg0)        |
| boolean                | removeIf(Predicate\<? super E\> arg0)  |
| abstract boolean       | retainAll(Collection\<?\> arg0)        |
| abstract int           | size()                                 |
| Spliterator\<E\>       | spliterator()                          |
| Stream\<E\>            | stream()                               |
| abstract \<T\> T\[\]   | toArray(T\[\] arg0)                    |
| abstract Object\[\]    | toArray()                              |

From interface java.lang.Iterable  

|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| void                                                                                                                                                                                                                                                                                                                                                                                                                           | forEach(Consumer\<? super T\> arg0) |
| abstract Iterator\<E extends [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency) \& [Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task) \& [PriorityProvider](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityProvider)\> | iterator()                          |
| Spliterator\<E extends [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency) \& [Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task) \& [PriorityProvider](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityProvider)\>       | spliterator()                       |

## Public Constructors

#### public
**DependencyPriorityBlockingQueue**
()

<br />

## Public Methods

#### public void
**clear**
()

<br />

#### public boolean
**contains**
(Object o)

<br />

##### Parameters

|---|---|
| o |   |

#### public int
**drainTo**
(Collection\<? super E\> c, int maxElements)

<br />

##### Parameters

|-------------|---|
| c           |   |
| maxElements |   |

#### public int
**drainTo**
(Collection\<? super E\> c)

<br />

##### Parameters

|---|---|
| c |   |

#### public E
**peek**
()

<br />

#### public E
**poll**
(long timeout, TimeUnit unit)

<br />

##### Parameters

|---------|---|
| timeout |   |
| unit    |   |

##### Throws

|----------------------|---|
| InterruptedException |   |

#### public E
**poll**
()

<br />

#### public void
**recycleBlockedQueue**
()

Removes all items from blocked Queue and inserts into primary queue to retry.  

#### public boolean
**remove**
(Object o)

<br />

##### Parameters

|---|---|
| o |   |

#### public boolean
**removeAll**
(Collection\<?\> collection)

<br />

##### Parameters

|------------|---|
| collection |   |

#### public int
**size**
()

<br />

#### public E
**take**
()

<br />

##### Throws

|----------------------|---|
| InterruptedException |   |

#### public T\[\]
**toArray**
(T\[\] a)

<br />

##### Parameters

|---|---|
| a |   |

#### public Object\[\]
**toArray**
()

<br />