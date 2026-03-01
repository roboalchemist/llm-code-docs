# Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection

Title: collection package - go.temporal.io/server/common/collection - Go Packages

URL Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection

Markdown Content:
*   [Constants](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#pkg-constants)
*   [func UUIDHashCode(input interface{}) uint32](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#UUIDHashCode)
*   [type ActionFunc](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ActionFunc)
*   [type ConcurrentTxMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ConcurrentTxMap)
*       *   [func NewShardedConcurrentTxMap(initialCap int, hashfn HashFunc) ConcurrentTxMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#NewShardedConcurrentTxMap)

*   [type FallibleOnceMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#FallibleOnceMap)
*       *   [func NewFallibleOnceMap[K comparable, T any](construct func(K) (T, error)) *FallibleOnceMap[K, T]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#NewFallibleOnceMap)

*       *   [func (p *FallibleOnceMap[K, T]) Get(key K) (T, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#FallibleOnceMap.Get)
    *   [func (p *FallibleOnceMap[K, T]) Pop(key K) (T, bool)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#FallibleOnceMap.Pop)

*   [type HashFunc](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#HashFunc)
*   [type IndexedTakeList](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#IndexedTakeList)
*       *   [func NewIndexedTakeList[K comparable, V any](values []V, indexer func(V) K) *IndexedTakeList[K, V]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#NewIndexedTakeList)

*       *   [func (itl *IndexedTakeList[K, V]) Take(key K) (V, bool)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#IndexedTakeList.Take)
    *   [func (itl *IndexedTakeList[K, V]) TakeRemaining() []V](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#IndexedTakeList.TakeRemaining)

*   [type Iterator](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#Iterator)
*       *   [func NewPagingIterator[V any](paginationFn PaginationFn[V]) Iterator[V]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#NewPagingIterator)
    *   [func NewPagingIteratorWithToken[V any](paginationFn PaginationFn[V], pageToken []byte) Iterator[V]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#NewPagingIteratorWithToken)

*   [type MapEntry](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#MapEntry)
*   [type MapIterator](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#MapIterator)
*   [type OnceMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#OnceMap)
*       *   [func NewOnceMap[K comparable, T any](construct func(K) T) *OnceMap[K, T]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#NewOnceMap)

*       *   [func (m *OnceMap[K, T]) Get(key K) T](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#OnceMap.Get)

*   [type PaginationFn](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#PaginationFn)
*   [type PagingIteratorImpl](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#PagingIteratorImpl)
*       *   [func (iter *PagingIteratorImpl[V]) HasNext() bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#PagingIteratorImpl.HasNext)
    *   [func (iter *PagingIteratorImpl[V]) Next() (V, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#PagingIteratorImpl.Next)

*   [type PredicateFunc](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#PredicateFunc)
*   [type Queue](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#Queue)
*       *   [func NewPriorityQueue[T any](compareLess func(this T, other T) bool) Queue[T]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#NewPriorityQueue)
    *   [func NewPriorityQueueWithItems[T any](compareLess func(this T, other T) bool, items []T) Queue[T]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#NewPriorityQueueWithItems)

*   [type ShardedConcurrentTxMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap)
*       *   [func (cmap *ShardedConcurrentTxMap) Contains(key interface{}) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap.Contains)
    *   [func (cmap *ShardedConcurrentTxMap) Get(key interface{}) (interface{}, bool)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap.Get)
    *   [func (cmap *ShardedConcurrentTxMap) GetAndDo(key interface{}, fn ActionFunc) (interface{}, bool, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap.GetAndDo)
    *   [func (cmap *ShardedConcurrentTxMap) Iter() MapIterator](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap.Iter)
    *   [func (cmap *ShardedConcurrentTxMap) Len() int](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap.Len)
    *   [func (cmap *ShardedConcurrentTxMap) Put(key interface{}, value interface{})](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap.Put)
    *   [func (cmap *ShardedConcurrentTxMap) PutIfNotExist(key interface{}, value interface{}) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap.PutIfNotExist)
    *   [func (cmap *ShardedConcurrentTxMap) PutOrDo(key interface{}, value interface{}, fn ActionFunc) (interface{}, bool, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap.PutOrDo)
    *   [func (cmap *ShardedConcurrentTxMap) Remove(key interface{})](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap.Remove)
    *   [func (cmap *ShardedConcurrentTxMap) RemoveIf(key interface{}, fn PredicateFunc) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap.RemoveIf)

*   [type SortedSetManager](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SortedSetManager)
*       *   [func NewSortedSetManager[S ~[]E, E, K any](cmp func(E, K) int, key func(E) K) SortedSetManager[S, E, K]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#NewSortedSetManager)

*       *   [func (m SortedSetManager[S, E, K]) Add(set S, e E) (S, bool)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SortedSetManager.Add)
    *   [func (m SortedSetManager[S, E, K]) Get(set S, key K) int](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SortedSetManager.Get)
    *   [func (m SortedSetManager[S, E, K]) Paginate(set S, gtKey K, n int) (S, *K)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SortedSetManager.Paginate)
    *   [func (m SortedSetManager[S, E, K]) Remove(set S, key K) (S, bool)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SortedSetManager.Remove)

*   [type SyncMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SyncMap)
*       *   [func NewSyncMap[K comparable, V any]() SyncMap[K, V]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#NewSyncMap)

*       *   [func (m *SyncMap[K, V]) Delete(key K)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SyncMap.Delete)
    *   [func (m *SyncMap[K, V]) Get(key K) (value V, ok bool)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SyncMap.Get)
    *   [func (m *SyncMap[K, V]) GetOrSet(key K, value V) (v V, exist bool)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SyncMap.GetOrSet)
    *   [func (m *SyncMap[K, V]) Pop(key K) (value V, ok bool)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SyncMap.Pop)
    *   [func (m *SyncMap[K, V]) PopAll() map[K]V](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SyncMap.PopAll)
    *   [func (m *SyncMap[K, V]) Set(key K, value V)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SyncMap.Set)

This section is empty.

func UUIDHashCode(input interface{}) [uint32](https://pkg.go.dev/builtin#uint32)

UUIDHashCode is a hash function for hashing string uuid if the uuid is malformed, then the hash function always returns 0 as the hash value

type ActionFunc func(key interface{}, value interface{}) [error](https://pkg.go.dev/builtin#error)

ActionFunc take a key and value, do calculation and return err

type ConcurrentTxMap interface {
	Get(key interface{}) (interface{}, [bool](https://pkg.go.dev/builtin#bool))
	Contains(key interface{}) [bool](https://pkg.go.dev/builtin#bool)
	Put(key interface{}, value interface{})
	
	PutIfNotExist(key interface{}, value interface{}) [bool](https://pkg.go.dev/builtin#bool)
	Remove(key interface{})
	
	GetAndDo(key interface{}, fn [ActionFunc](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ActionFunc)) (interface{}, [bool](https://pkg.go.dev/builtin#bool), [error](https://pkg.go.dev/builtin#error))
	
	PutOrDo(key interface{}, value interface{}, fn [ActionFunc](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ActionFunc)) (interface{}, [bool](https://pkg.go.dev/builtin#bool), [error](https://pkg.go.dev/builtin#error))
	
	RemoveIf(key interface{}, fn [PredicateFunc](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#PredicateFunc)) [bool](https://pkg.go.dev/builtin#bool)
	Iter() MapIterator
	Len() [int](https://pkg.go.dev/builtin#int)
}

ConcurrentTxMap is a generic interface for any implementation of a dictionary or a key value lookup table that is thread safe, and providing functionality to modify key / value pair inside within a transaction

func NewShardedConcurrentTxMap(initialCap [int](https://pkg.go.dev/builtin#int), hashfn HashFunc) ConcurrentTxMap

NewShardedConcurrentTxMap returns an instance of ShardedConcurrentMap

ShardedConcurrentMap is a thread safe map that maintains upto nShards number of maps internally to allow nShards writers to be acive at the same time. This map *does not* use re-entrant locks, so access to the map during iterator can cause a dead lock.

@param initialSz

The initial size for the map

@param hashfn

The hash function to use for sharding

FallibleOnceMap is a concurrent map which lazily constructs its values. Map values are initialized on-the-fly, using a provided construction function only when a key is accessed for the first time. If the construct function returns an error, the value is not cached.

NewFallibleOnceMap creates a [FallibleOnceMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#FallibleOnceMap) from a given construct function. construct should be kept light as it is called while holding a lock on the entire map.

func (p *[FallibleOnceMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#FallibleOnceMap)[K, T]) Get(key K) (T, [error](https://pkg.go.dev/builtin#error))

func (p *[FallibleOnceMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#FallibleOnceMap)[K, T]) Pop(key K) (T, [bool](https://pkg.go.dev/builtin#bool))

type HashFunc func(interface{}) [uint32](https://pkg.go.dev/builtin#uint32)

HashFunc represents a hash function for string

IndexedTakeList holds a set of values that can only be observed by being removed from the set. It is possible for this set to contain duplicate values as long as each value maps to a distinct index.

func NewIndexedTakeList[K [comparable](https://pkg.go.dev/builtin#comparable), V [any](https://pkg.go.dev/builtin#any)](
	values []V,
	indexer func(V) K,
) *[IndexedTakeList](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#IndexedTakeList)[K, V]

NewIndexedTakeList constructs a new IndexedTakeSet by applying the provided indexer to each of the provided values.

func (itl *[IndexedTakeList](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#IndexedTakeList)[K, V]) Take(key K) (V, [bool](https://pkg.go.dev/builtin#bool))

Take finds a value in this set by its key and removes it, returning the value.

#### func (*IndexedTakeList[K, V]) [TakeRemaining](https://github.com/temporalio/temporal/blob/v1.30.0/common/collection/indexedtakelist.go#L52)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#IndexedTakeList.TakeRemaining "Go to IndexedTakeList.TakeRemaining")added in v1.21.0

func (itl *[IndexedTakeList](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#IndexedTakeList)[K, V]) TakeRemaining() []V

TakeRemaining removes all remaining values from this set and returns them.

type Iterator[V [any](https://pkg.go.dev/builtin#any)] interface {
	HasNext() [bool](https://pkg.go.dev/builtin#bool)
	Next() (V, [error](https://pkg.go.dev/builtin#error))
}

Iterator represents the interface for iterator

func NewPagingIterator[V [any](https://pkg.go.dev/builtin#any)](
	paginationFn [PaginationFn](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#PaginationFn)[V],
) [Iterator](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#Iterator)[V]

NewPagingIterator create a new paging iterator

func NewPagingIteratorWithToken[V [any](https://pkg.go.dev/builtin#any)](
	paginationFn [PaginationFn](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#PaginationFn)[V],
	pageToken [][byte](https://pkg.go.dev/builtin#byte),
) [Iterator](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#Iterator)[V]

NewPagingIteratorWithToken create a new paging iterator with initial token

type MapEntry struct {
	Key interface{}
	Value interface{}
}

MapEntry represents a key-value entry within the map

type MapIterator interface {
	
	Close()
	
	Entries() <-chan *MapEntry
}

MapIterator represents the interface for map iterators

OnceMap is a concurrent map which lazily constructs its values. Map values are initialized on-the-fly, using a provided construction function only when a key is accessed for the first time.

NewOnceMap creates a [OnceMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#OnceMap) from a given construct function. construct should be kept light as it is called while holding a lock on the entire map.

func (m *[OnceMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#OnceMap)[K, T]) Get(key K) T

PaginationFn is the function which get a page of results

type PagingIteratorImpl[V [any](https://pkg.go.dev/builtin#any)] struct {
	
}

PagingIteratorImpl is the implementation of PagingIterator

func (iter *PagingIteratorImpl[V]) HasNext() [bool](https://pkg.go.dev/builtin#bool)

HasNext return whether has next item or err

func (iter *PagingIteratorImpl[V]) Next() (V, [error](https://pkg.go.dev/builtin#error))

Next return next item or err

type PredicateFunc func(key interface{}, value interface{}) [bool](https://pkg.go.dev/builtin#bool)

PredicateFunc take a key and value, do calculation and return boolean

type Queue[T [any](https://pkg.go.dev/builtin#any)] interface {
	Peek() T
	Add(item T)
	Remove() T
	IsEmpty() [bool](https://pkg.go.dev/builtin#bool)
	Len() [int](https://pkg.go.dev/builtin#int)
}

Queue is the interface for queue

func NewPriorityQueue[T [any](https://pkg.go.dev/builtin#any)](
	compareLess func(this T, other T) [bool](https://pkg.go.dev/builtin#bool),
) [Queue](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#Queue)[T]

NewPriorityQueue create a new priority queue

func NewPriorityQueueWithItems[T [any](https://pkg.go.dev/builtin#any)](
	compareLess func(this T, other T) [bool](https://pkg.go.dev/builtin#bool),
	items []T,
) [Queue](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#Queue)[T]

NewPriorityQueueWithItems creats a new priority queue with the provided list of items. PriorityQueue will take ownership of the passed in items, so caller should stop modifying it. The complexity is O(n) where n is the number of items

type ShardedConcurrentTxMap struct {
	
}

ShardedConcurrentTxMap is an implementation of ConcurrentMap that internally uses multiple sharded maps to increase parallelism

func (cmap *[ShardedConcurrentTxMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap)) Contains(key interface{}) [bool](https://pkg.go.dev/builtin#bool)

Contains returns true if the key exist and false otherwise

func (cmap *[ShardedConcurrentTxMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap)) Get(key interface{}) (interface{}, [bool](https://pkg.go.dev/builtin#bool))

Get returns the value corresponding to the key, if it exist

#### func (*ShardedConcurrentTxMap) [GetAndDo](https://github.com/temporalio/temporal/blob/v1.30.0/common/collection/concurrent_tx_map.go#L127)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap.GetAndDo "Go to ShardedConcurrentTxMap.GetAndDo")

func (cmap *[ShardedConcurrentTxMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap)) GetAndDo(key interface{}, fn ActionFunc) (interface{}, [bool](https://pkg.go.dev/builtin#bool), [error](https://pkg.go.dev/builtin#error))

GetAndDo returns the value corresponding to the key, and apply fn to key value before return value return (value, value exist or not, error when evaluation fn)

func (cmap *[ShardedConcurrentTxMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap)) Iter() MapIterator

Iter returns an iterator to the map. This map does not use re-entrant locks, so access or modification to the map during iteration can cause a dead lock.

Len returns the number of items in the map

func (cmap *[ShardedConcurrentTxMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap)) Put(key interface{}, value interface{})

Put records the given key value mapping. Overwrites previous values

func (cmap *[ShardedConcurrentTxMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap)) PutIfNotExist(key interface{}, value interface{}) [bool](https://pkg.go.dev/builtin#bool)

PutIfNotExist records the mapping, if there is no mapping for this key already Returns true if the mapping was recorded, false otherwise

func (cmap *[ShardedConcurrentTxMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap)) PutOrDo(key interface{}, value interface{}, fn ActionFunc) (interface{}, [bool](https://pkg.go.dev/builtin#bool), [error](https://pkg.go.dev/builtin#error))

PutOrDo put the key value in the map, if key does not exists, otherwise, call fn with existing key and value return (value, fn evaluated or not, error when evaluation fn)

func (cmap *[ShardedConcurrentTxMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap)) Remove(key interface{})

Remove deletes the given key from the map

func (cmap *[ShardedConcurrentTxMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#ShardedConcurrentTxMap)) RemoveIf(key interface{}, fn PredicateFunc) [bool](https://pkg.go.dev/builtin#bool)

RemoveIf deletes the given key from the map if fn return true

type SortedSetManager[S ~[]E, E, K [any](https://pkg.go.dev/builtin#any)] struct {
	
}

SortedSetManager provides CRUD functionality for in-memory sorted sets. Note that there's no Update method because you can just use the [SortedSetManager.Get](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SortedSetManager.Get) method and update that index directly.

func NewSortedSetManager[S ~[]E, E, K [any](https://pkg.go.dev/builtin#any)](cmp func(E, K) [int](https://pkg.go.dev/builtin#int), key func(E) K) [SortedSetManager](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SortedSetManager)[S, E, K]

NewSortedSetManager returns a new SortedSetManager with the given comparison function and key function.

func (m [SortedSetManager](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SortedSetManager)[S, E, K]) Add(set S, e E) (S, [bool](https://pkg.go.dev/builtin#bool))

Add adds a new element to the set. If the element is already in the set, it returns the set unchanged and false.

func (m [SortedSetManager](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SortedSetManager)[S, E, K]) Get(set S, key K) [int](https://pkg.go.dev/builtin#int)

Get returns the index of the element in the set that compares equal to key or -1 if no such element exists.

func (m [SortedSetManager](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SortedSetManager)[S, E, K]) Paginate(set S, gtKey K, n [int](https://pkg.go.dev/builtin#int)) (S, *K)

Paginate returns up to n elements in the set that compare greater than gtKey. If there are more than n such elements, it also returns the key of the last element in the page. Otherwise, the second return value is nil.

func (m [SortedSetManager](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SortedSetManager)[S, E, K]) Remove(set S, key K) (S, [bool](https://pkg.go.dev/builtin#bool))

Remove removes an element from the set. If the element is not in the set, it returns the set unchanged and false.

SyncMap implements a simple mutex-wrapped map. SyncMap is copyable like a normal map[K]V.

func (m *[SyncMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SyncMap)[K, V]) Delete(key K)

func (m *[SyncMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SyncMap)[K, V]) Get(key K) (value V, ok [bool](https://pkg.go.dev/builtin#bool))

func (m *[SyncMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SyncMap)[K, V]) GetOrSet(key K, value V) (v V, exist [bool](https://pkg.go.dev/builtin#bool))

func (m *[SyncMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SyncMap)[K, V]) Pop(key K) (value V, ok [bool](https://pkg.go.dev/builtin#bool))

func (m *[SyncMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SyncMap)[K, V]) PopAll() map[K]V

func (m *[SyncMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/collection#SyncMap)[K, V]) Set(key K, value V)
