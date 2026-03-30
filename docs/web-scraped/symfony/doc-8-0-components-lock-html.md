# Source: https://symfony.com/doc/8.0/components/lock.html

Title: The Lock Component (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/components/lock.html

Markdown Content:
> The Lock Component creates and manages [locks](https://en.wikipedia.org/wiki/Lock_(computer_science)), a mechanism to provide exclusive access to a shared resource.

If you're using the Symfony Framework, read the [Symfony Framework Lock documentation](https://symfony.com/doc/current/lock.html).

[Installation](https://symfony.com/doc/8.0/components/lock.html#installation "Permalink to this headline")
----------------------------------------------------------------------------------------------------------

Note

If you install this component outside of a Symfony application, you must require the `vendor/autoload.php` file in your code to enable the class autoloading mechanism provided by Composer. Read [this article](https://symfony.com/doc/current/components/using_components.html) for more details.

[Usage](https://symfony.com/doc/8.0/components/lock.html#usage "Permalink to this headline")
--------------------------------------------------------------------------------------------

Locks are used to guarantee exclusive access to some shared resource. In Symfony applications, you can use locks for example to ensure that a command is not executed more than once at the same time (on the same or different servers).

Locks are created using a [LockFactory](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/LockFactory.php "Symfony\Component\Lock\LockFactory") class, which in turn requires another class to manage the storage of locks:

The lock is created by calling the [createLock()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/LockFactory.php#:~:text=function%20createLock "Symfony\Component\Lock\LockFactory::createLock()") method. Its first argument is an arbitrary string that represents the locked resource. Then, a call to the [acquire()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/LockInterface.php#:~:text=function%20acquire "Symfony\Component\Lock\LockInterface::acquire()") method will try to acquire the lock:

If the lock can not be acquired, the method returns `false`. The `acquire()` method can be safely called repeatedly, even if the lock is already acquired.

Note

Unlike other implementations, the Lock Component distinguishes lock instances even when they are created for the same resource. It means that for a given scope and resource one lock instance can be acquired multiple times. If a lock has to be used by several services, they should share the same `Lock` instance returned by the `LockFactory::createLock` method.

Tip

If you don't release the lock explicitly, it will be released automatically upon instance destruction. In some cases, it can be useful to lock a resource across several requests. To disable the automatic release behavior, set the third argument of the `createLock()` method to `false`.

[Serializing Locks](https://symfony.com/doc/8.0/components/lock.html#serializing-locks "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------

The [Key](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/Key.php "Symfony\Component\Lock\Key") contains the state of the [Lock](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/Lock.php "Symfony\Component\Lock\Lock") and can be serialized. This allows the user to begin a long job in a process by acquiring the lock, and continue the job in another process using the same lock.

First, you may create a serializable class containing the resource and the key of the lock:

Then, you can use this class to dispatch all that's needed for another process to handle the rest of the job:

Note

Don't forget to set the `autoRelease` argument to `false` in the `Lock` instantiation to avoid releasing the lock when the destructor is called.

Not all stores are compatible with serialization and cross-process locking: for example, the kernel will automatically release semaphores acquired by the [SemaphoreStore](https://symfony.com/doc/current/components/lock.html#lock-store-semaphore) store. If you use an incompatible store (see [lock stores](https://symfony.com/doc/current/components/lock.html#lock-stores) for supported stores), an exception will be thrown when the application tries to serialize the key.

Locks can be serialized using both the native PHP serialization system and its [serialize](https://secure.php.net/manual/en/function.serialize.php "serialize") function, or using the Serializer component.

[Blocking Locks](https://symfony.com/doc/8.0/components/lock.html#blocking-locks "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------

By default, when a lock cannot be acquired, the `acquire` method returns `false` immediately. To wait (indefinitely) until the lock can be created, pass `true` as the argument of the `acquire()` method. This is called a **blocking lock** because the execution of your application stops until the lock is acquired:

When the store does not support blocking locks by implementing the [BlockingStoreInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/BlockingStoreInterface.php "Symfony\Component\Lock\BlockingStoreInterface") interface (see [lock stores](https://symfony.com/doc/current/components/lock.html#lock-stores) for supported stores), the `Lock` class will retry to acquire the lock in a non-blocking way until the lock is acquired.

[Expiring Locks](https://symfony.com/doc/8.0/components/lock.html#expiring-locks "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------

Locks created remotely are difficult to manage because there is no way for the remote `Store` to know if the locker process is still alive. Due to bugs, fatal errors or segmentation faults, it cannot be guaranteed that the `release()` method will be called, which would cause the resource to be locked infinitely.

The best solution in those cases is to create **expiring locks**, which are released automatically after some amount of time has passed (called TTL for _Time To Live_). This time, in seconds, is configured as the second argument of the `createLock()` method. If needed, these locks can also be released early with the `release()` method.

The trickiest part when working with expiring locks is choosing the right TTL. If it's too short, other processes could acquire the lock before finishing the job; if it's too long and the process crashes before calling the `release()` method, the resource will stay locked until the timeout:

Tip

To avoid leaving the lock in a locked state, it's recommended to wrap the job in a try/catch/finally block to always try to release the expiring lock.

In case of long-running tasks, it's better to start with a not too long TTL and then use the [refresh()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/LockInterface.php#:~:text=function%20refresh "Symfony\Component\Lock\LockInterface::refresh()") method to reset the TTL to its original value:

Tip

Another useful technique for long-running tasks is to pass a custom TTL as an argument of the `refresh()` method to change the default lock TTL:

This component also provides two useful methods related to expiring locks: `getRemainingLifetime()` (which returns `null` or a `float` as seconds) and `isExpired()` (which returns a boolean).

### [Automatically Releasing The Lock](https://symfony.com/doc/8.0/components/lock.html#automatically-releasing-the-lock "Permalink to this headline")

Locks are automatically released when their Lock objects are destroyed. This is an implementation detail that is important when sharing Locks between processes. In the example below, `pcntl_fork()` creates two processes and the Lock will be released automatically as soon as one process finishes:

Note

In order for the above example to work, the [PCNTL](https://www.php.net/manual/book.pcntl.php) extension must be installed.

To disable this behavior, set the `autoRelease` argument of `LockFactory::createLock()` to `false`. That will make the lock acquired for 3600 seconds or until `Lock::release()` is called:

A shared or [readers-writer lock](https://en.wikipedia.org/wiki/Readers%E2%80%93writer_lock) is a synchronization primitive that allows concurrent access for read-only operations, while write operations require exclusive access. This means that multiple threads can read the data in parallel but an exclusive lock is needed for writing or modifying data. They are used for example for data structures that cannot be updated atomically and are invalid until the update is complete.

Use the [acquireRead()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/SharedLockInterface.php#:~:text=function%20acquireRead "Symfony\Component\Lock\SharedLockInterface::acquireRead()") method to acquire a read-only lock, and [acquire()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/LockInterface.php#:~:text=function%20acquire "Symfony\Component\Lock\LockInterface::acquire()") method to acquire a write lock:

Similar to the `acquire()` method, pass `true` as the argument of `acquireRead()` to acquire the lock in a blocking mode:

Note

The [priority policy](https://en.wikipedia.org/wiki/Readers%E2%80%93writer_lock#Priority_policies) of Symfony's shared locks depends on the underlying store (e.g. Redis store prioritizes readers vs writers).

When a read-only lock is acquired with the `acquireRead()` method, it's possible to **promote** the lock, and change it to a write lock, by calling the `acquire()` method:

In the same way, it's possible to **demote** a write lock, and change it to a read-only lock by calling the `acquireRead()` method.

When the provided store does not implement the [SharedLockStoreInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/SharedLockStoreInterface.php "Symfony\Component\Lock\SharedLockStoreInterface") interface (see [lock stores](https://symfony.com/doc/current/components/lock.html#lock-stores) for supported stores), the `Lock` class will fallback to a write lock by calling the `acquire()` method.

[The Owner of The Lock](https://symfony.com/doc/8.0/components/lock.html#the-owner-of-the-lock "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------

Locks that are acquired for the first time are [owned](https://symfony.com/doc/current/components/lock.html#lock-owner-technical-details) by the `Lock` instance that acquired it. If you need to check whether the current `Lock` instance is (still) the owner of a lock, you can use the `isAcquired()` method:

Because some lock stores have expiring locks, it is possible for an instance to lose the lock it acquired automatically:

Warning

A common pitfall might be to use the `isAcquired()` method to check if a lock has already been acquired by any process. As you can see in this example you have to use `acquire()` for this. The `isAcquired()` method is used to check if the lock has been acquired by the **current process** only.

Note

Technically, the true owners of the lock are the ones that share the same instance of `Key`, not `Lock`. But from a user perspective, `Key` is internal and you will likely only be working with the `Lock` instance so it's easier to think of the `Lock` instance as being the one that is the owner of the lock.

[Available Stores](https://symfony.com/doc/8.0/components/lock.html#available-stores "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------

Locks are created and managed in `Stores`, which are classes that implement [PersistingStoreInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/PersistingStoreInterface.php "Symfony\Component\Lock\PersistingStoreInterface") and, optionally, [BlockingStoreInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/BlockingStoreInterface.php "Symfony\Component\Lock\BlockingStoreInterface").

The component includes the following built-in store types:

| Store | Scope | Blocking | Expiring | Sharing | Serialization |
| --- | --- | --- | --- | --- | --- |
| [DoctrineDbalPostgreSqlStore](https://symfony.com/doc/current/components/lock.html#lock-store-dbal-pgsql) | remote | yes | no | yes | no |
| [DoctrineDbalStore](https://symfony.com/doc/current/components/lock.html#lock-store-dbal) | remote | retry | yes | no | yes |
| [DynamoDbStore](https://symfony.com/doc/current/components/lock.html#lock-store-dynamodb) | remote | retry | yes | no | yes |
| [FlockStore](https://symfony.com/doc/current/components/lock.html#lock-store-flock) | local | yes | no | yes | no |
| [MemcachedStore](https://symfony.com/doc/current/components/lock.html#lock-store-memcached) | remote | retry | yes | no | yes |
| [MongoDbStore](https://symfony.com/doc/current/components/lock.html#lock-store-mongodb) | remote | retry | yes | no | yes |
| [PdoStore](https://symfony.com/doc/current/components/lock.html#lock-store-pdo) | remote | retry | yes | no | yes |
| [PostgreSqlStore](https://symfony.com/doc/current/components/lock.html#lock-store-pgsql) | remote | yes | no | yes | no |
| [RedisStore](https://symfony.com/doc/current/components/lock.html#lock-store-redis) | remote | retry | yes | yes | yes |
| [SemaphoreStore](https://symfony.com/doc/current/components/lock.html#lock-store-semaphore) | local | yes | no | no | no |
| [ZookeeperStore](https://symfony.com/doc/current/components/lock.html#lock-store-zookeeper) | remote | retry | no | no | no |

When the store does not support blocking locks, the Lock class will retry to acquire the lock in a non-blocking way until the lock is acquired.

Tip

Symfony includes two other special stores that are mostly useful for testing:

* `InMemoryStore` (`LOCK_DSN=in-memory`), which saves locks in memory during a process;
* `NullStore` (`LOCK_DSN=null`) which doesn't persist anything.

### [FlockStore](https://symfony.com/doc/8.0/components/lock.html#flockstore "Permalink to this headline")

The FlockStore uses the file system on the local computer to create the locks. It does not support expiration, but the lock is automatically released when the lock object goes out of scope and is freed by the garbage collector (for example when the PHP process ends):

Warning

Beware that some file systems (such as some types of NFS) do not support locking. In those cases, it's better to use a directory on a local disk drive or a remote store.

### [MemcachedStore](https://symfony.com/doc/8.0/components/lock.html#memcachedstore "Permalink to this headline")

The MemcachedStore saves locks on a Memcached server, it requires a Memcached connection implementing the `\Memcached` class. This store does not support blocking, and expects a TTL to avoid stalled locks:

Note

Memcached does not support TTL lower than 1 second.

### [MongoDbStore](https://symfony.com/doc/8.0/components/lock.html#mongodbstore "Permalink to this headline")

The MongoDbStore saves locks on a MongoDB server `>=2.2`, it requires a `\MongoDB\Collection` or `\MongoDB\Client` from [mongodb/mongodb](https://packagist.org/packages/mongodb/mongodb) or a [MongoDB Connection String](https://docs.mongodb.com/manual/reference/connection-string/). This store does not support blocking and expects a TTL to avoid stalled locks:

The `MongoDbStore` takes the following `$options` (depending on the first parameter type):

| Option | Description |
| --- | --- |
| collection | The name of the collection |
| database | The name of the database |
| driverOptions | Array of driver options for [MongoDBClient::__construct](https://docs.mongodb.com/php-library/current/reference/method/MongoDBClient__construct/) |
| gcProbability | Should a TTL Index be created expressed as a probability from 0.0 to 1.0 (Defaults to `0.001`) |
| uriOptions | Array of URI options for [MongoDBClient::__construct](https://docs.mongodb.com/php-library/current/reference/method/MongoDBClient__construct/) |

When the first parameter is a:

`MongoDB\Collection`:

* `$options['database']` is ignored
* `$options['collection']` is ignored

`MongoDB\Client`:

* `$options['database']` is mandatory
* `$options['collection']` is mandatory

MongoDB Connection String:

* `$options['database']` is used otherwise `/path` from the DSN, at least one is mandatory
* `$options['collection']` is used otherwise `?collection=` from the DSN, at least one is mandatory

### [PdoStore](https://symfony.com/doc/8.0/components/lock.html#pdostore "Permalink to this headline")

The PdoStore saves locks in an SQL database. It requires a [PDO](https://www.php.net/pdo) connection or a [Data Source Name (DSN)](https://en.wikipedia.org/wiki/Data_source_name). This store does not support blocking, and expects a TTL to avoid stalled locks:

Note

This store does not support TTL lower than 1 second.

The table where values are stored is created automatically on the first call to the [save()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/Store/PdoStore.php#:~:text=function%20save "Symfony\Component\Lock\Store\PdoStore::save()") method. You can also create this table explicitly by calling the [createTable()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/Store/PdoStore.php#:~:text=function%20createTable "Symfony\Component\Lock\Store\PdoStore::createTable()") method in your code.

### [DoctrineDbalStore](https://symfony.com/doc/8.0/components/lock.html#doctrinedbalstore "Permalink to this headline")

The DoctrineDbalStore saves locks in an SQL database. It is identical to PdoStore but requires a [Doctrine DBAL Connection](https://github.com/doctrine/dbal/blob/master/src/Connection.php), or a [Doctrine DBAL URL](https://www.doctrine-project.org/projects/doctrine-dbal/en/latest/reference/configuration.html#connecting-using-a-url). This store does not support blocking, and expects a TTL to avoid stalled locks:

Note

This store does not support TTL lower than 1 second.

The table where values are stored will be automatically generated when your run the command:

If you prefer to create the table yourself and it has not already been created, you can create this table explicitly by calling the [createTable()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/Store/DoctrineDbalStore.php#:~:text=function%20createTable "Symfony\Component\Lock\Store\DoctrineDbalStore::createTable()") method. You can also add this table to your schema by calling [configureSchema()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/Store/DoctrineDbalStore.php#:~:text=function%20configureSchema "Symfony\Component\Lock\Store\DoctrineDbalStore::configureSchema()") method in your code

If the table has not been created upstream, it will be created automatically on the first call to the [save()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/Store/DoctrineDbalStore.php#:~:text=function%20save "Symfony\Component\Lock\Store\DoctrineDbalStore::save()") method.

### [PostgreSqlStore](https://symfony.com/doc/8.0/components/lock.html#postgresqlstore "Permalink to this headline")

The PostgreSqlStore uses [Advisory Locks](https://www.postgresql.org/docs/current/explicit-locking.html) provided by PostgreSQL. It requires a [PDO](https://www.php.net/pdo) connection or a [Data Source Name (DSN)](https://en.wikipedia.org/wiki/Data_source_name). It supports native blocking, as well as sharing locks:

In opposite to the `PdoStore`, the `PostgreSqlStore` does not need a table to store locks and it does not expire.

### [DoctrineDbalPostgreSqlStore](https://symfony.com/doc/8.0/components/lock.html#doctrinedbalpostgresqlstore "Permalink to this headline")

The DoctrineDbalPostgreSqlStore uses [Advisory Locks](https://www.postgresql.org/docs/current/explicit-locking.html) provided by PostgreSQL. It is identical to PostgreSqlStore but requires a [Doctrine DBAL Connection](https://github.com/doctrine/dbal/blob/master/src/Connection.php) or a [Doctrine DBAL URL](https://www.doctrine-project.org/projects/doctrine-dbal/en/latest/reference/configuration.html#connecting-using-a-url). It supports native blocking, as well as sharing locks:

In opposite to the `DoctrineDbalStore`, the `DoctrineDbalPostgreSqlStore` does not need a table to store locks and does not expire.

### [RedisStore](https://symfony.com/doc/8.0/components/lock.html#redisstore "Permalink to this headline")

The RedisStore saves locks on a Redis server, it requires a Redis connection implementing the `\Redis`, `\RedisArray`, `\RedisCluster`, `\Relay\Relay`, `\Relay\Cluster` or `\Predis` classes. This store does not support blocking, and expects a TTL to avoid stalled locks:

### [CombinedStore](https://symfony.com/doc/8.0/components/lock.html#combinedstore "Permalink to this headline")

The CombinedStore is designed for High Availability applications because it manages several stores in sync (for example, several Redis servers). When a lock is acquired, it forwards the call to all the managed stores, and it collects their responses. If a simple majority of stores have acquired the lock, then the lock is considered acquired:

Instead of the simple majority strategy (`ConsensusStrategy`) an `UnanimousStrategy` can be used to require the lock to be acquired in all the stores:

Warning

In order to get high availability when using the `ConsensusStrategy`, the minimum cluster size must be three servers. This allows the cluster to keep working when a single server fails (because this strategy requires that the lock is acquired for more than half of the servers).

### [ZookeeperStore](https://symfony.com/doc/8.0/components/lock.html#zookeeperstore "Permalink to this headline")

The ZookeeperStore saves locks on a [ZooKeeper](https://zookeeper.apache.org/) server. It requires a ZooKeeper connection implementing the `\Zookeeper` class. This store does not support blocking and expiration but the lock is automatically released when the PHP process is terminated:

Note

Zookeeper does not require a TTL as the nodes used for locking are ephemeral and die when the PHP process is terminated.

### [DynamoDbStore](https://symfony.com/doc/8.0/components/lock.html#dynamodbstore "Permalink to this headline")

The DynamoDbStore saves locks on a Amazon DynamoDB table. Install it by running:

It requires a [DynamoDbClient](https://async-aws.com/clients/dynamodb.html) instance or a [Data Source Name (DSN)](https://en.wikipedia.org/wiki/Data_source_name). This store does not support blocking, and expects a TTL to avoid stalled locks:

The table where values are stored is created automatically on the first call to the [save()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/Bridge/DynamoDb/Store/DynamoDbStore.php#:~:text=function%20save "Symfony\Component\Lock\Bridge\DynamoDb\Store\DynamoDbStore::save()") method. You can also create this table explicitly by calling the [createTable()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/Bridge/DynamoDb/Store/DynamoDbStore.php#:~:text=function%20createTable "Symfony\Component\Lock\Bridge\DynamoDb\Store\DynamoDbStore::createTable()") method in your code.

[Reliability](https://symfony.com/doc/8.0/components/lock.html#reliability "Permalink to this headline")
--------------------------------------------------------------------------------------------------------

The component guarantees that the same resource can't be locked twice as long as the component is used in the following way.

### [Remote Stores](https://symfony.com/doc/8.0/components/lock.html#remote-stores "Permalink to this headline")

Remote stores ([MemcachedStore](https://symfony.com/doc/current/components/lock.html#lock-store-memcached), [MongoDbStore](https://symfony.com/doc/current/components/lock.html#lock-store-mongodb), [PdoStore](https://symfony.com/doc/current/components/lock.html#lock-store-pdo), [PostgreSqlStore](https://symfony.com/doc/current/components/lock.html#lock-store-pgsql), [RedisStore](https://symfony.com/doc/current/components/lock.html#lock-store-redis) and [ZookeeperStore](https://symfony.com/doc/current/components/lock.html#lock-store-zookeeper)) use a unique token to recognize the true owner of the lock. This token is stored in the [Key](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Lock/Key.php "Symfony\Component\Lock\Key") object and is used internally by the `Lock`.

Every concurrent process must store the `Lock` on the same server. Otherwise two different machines may allow two different processes to acquire the same `Lock`.

Warning

To guarantee that the same server will always be safe, do not use Memcached behind a LoadBalancer, a cluster or round-robin DNS. Even if the main server is down, the calls must not be forwarded to a backup or failover server.

### [Expiring Stores](https://symfony.com/doc/8.0/components/lock.html#expiring-stores "Permalink to this headline")

Expiring stores ([MemcachedStore](https://symfony.com/doc/current/components/lock.html#lock-store-memcached), [MongoDbStore](https://symfony.com/doc/current/components/lock.html#lock-store-mongodb), [PdoStore](https://symfony.com/doc/current/components/lock.html#lock-store-pdo) and [RedisStore](https://symfony.com/doc/current/components/lock.html#lock-store-redis)) guarantee that the lock is acquired only for the defined duration of time. If the task takes longer to be accomplished, then the lock can be released by the store and acquired by someone else.

The `Lock` provides several methods to check its health. The `isExpired()` method checks whether or not its lifetime is over and the `getRemainingLifetime()` method returns its time to live in seconds.

Using the above methods, a robust code would be:

Warning

Choose wisely the lifetime of the `Lock` and check whether its remaining time to live is enough to perform the task.

Warning

Storing a `Lock` usually takes a few milliseconds, but network conditions may increase that time a lot (up to a few seconds). Take that into account when choosing the right TTL.

By design, locks are stored on servers with a defined lifetime. If the date or time of the machine changes, a lock could be released sooner than expected.

Warning

To guarantee that date won't change, the NTP service should be disabled and the date should be updated when the service is stopped.

### [FlockStore](https://symfony.com/doc/8.0/components/lock.html#flockstore-1 "Permalink to this headline")

By using the file system, this `Store` is reliable as long as concurrent processes use the same physical directory to store locks.

Processes must run on the same machine, virtual machine or container. Be careful when updating a Kubernetes or Swarm service because, for a short period of time, there can be two containers running in parallel.

The absolute path to the directory must remain the same. Be careful of symlinks that could change at anytime: Capistrano and blue/green deployment often use that trick. Be careful when the path to that directory changes between two deployments.

Some file systems (such as some types of NFS) do not support locking.

Warning

All concurrent processes must use the same physical file system by running on the same machine and using the same absolute path to the lock directory.

Using a `FlockStore` in an HTTP context is incompatible with multiple front servers, unless to ensure that the same resource will always be locked on the same machine or to use a well configured shared file system.

Files on the file system can be removed during a maintenance operation. For instance, to clean up the `/tmp` directory or after a reboot of the machine when a directory uses `tmpfs`. It's not an issue if the lock is released when the process ended, but it is in case of `Lock` reused between requests.

Danger

Do not store locks on a volatile file system if they have to be reused in several requests.

### [MemcachedStore](https://symfony.com/doc/8.0/components/lock.html#memcachedstore-1 "Permalink to this headline")

The way Memcached works is to store items in memory. That means that by using the [MemcachedStore](https://symfony.com/doc/current/components/lock.html#lock-store-memcached) the locks are not persisted and may disappear by mistake at any time.

If the Memcached service or the machine hosting it restarts, every lock would be lost without notifying the running processes.

Warning

To avoid that someone else acquires a lock after a restart, it's recommended to delay service start and wait at least as long as the longest lock TTL.

By default Memcached uses a LRU mechanism to remove old entries when the service needs space to add new items.

Warning

The number of items stored in Memcached must be under control. If it's not possible, LRU should be disabled and Lock should be stored in a dedicated Memcached service away from Cache.

When the Memcached service is shared and used for multiple usage, Locks could be removed by mistake. For instance some implementation of the PSR-6 `clear()` method uses the Memcached's `flush()` method which purges and removes everything.

Danger

The method `flush()` must not be called, or locks should be stored in a dedicated Memcached service away from Cache.

### [MongoDbStore](https://symfony.com/doc/8.0/components/lock.html#mongodbstore-1 "Permalink to this headline")

Warning

The locked resource name is indexed in the `_id` field of the lock collection. Beware that an indexed field's value in MongoDB can be [a maximum of 1024 bytes in length](https://docs.mongodb.com/manual/reference/limits/#Index-Key-Limit) including the structural overhead.

A TTL index must be used to automatically clean up expired locks. Such an index can be created manually:

Alternatively, the method `MongoDbStore::createTtlIndex(int $expireAfterSeconds = 0)` can be called once to create the TTL index during database setup. Read more about [Expire Data from Collections by Setting TTL](https://docs.mongodb.com/manual/tutorial/expire-data/) in MongoDB.

Tip

`MongoDbStore` will attempt to automatically create a TTL index. It's recommended to set constructor option `gcProbability` to `0.0` to disable this behavior if you have manually dealt with TTL index creation.

Warning

This store relies on all PHP application and database nodes to have synchronized clocks for lock expiry to occur at the correct time. To ensure locks don't expire prematurely; the lock TTL should be set with enough extra time in `expireAfterSeconds` to account for any clock drift between nodes.

`writeConcern` and `readConcern` are not specified by MongoDbStore meaning the collection's settings will take effect. `readPreference` is `primary` for all queries. Read more about [Replica Set Read and Write Semantics](https://docs.mongodb.com/manual/applications/replication/) in MongoDB.

### [PdoStore](https://symfony.com/doc/8.0/components/lock.html#pdostore-1 "Permalink to this headline")

The PdoStore relies on the [ACID](https://en.wikipedia.org/wiki/ACID) properties of the SQL engine.

Warning

In a cluster configured with multiple primaries, ensure writes are synchronously propagated to every node, or always use the same node.

Warning

Some SQL engines like MySQL allow disabling the unique constraint check. Ensure that this is not the case `SET unique_checks=1;`.

In order to purge old locks, this store uses a current datetime to define an expiration date reference. This mechanism relies on all server nodes to have synchronized clocks.

Warning

To ensure locks don't expire prematurely; the TTLs should be set with enough extra time to account for any clock drift between nodes.

### [PostgreSqlStore](https://symfony.com/doc/8.0/components/lock.html#postgresqlstore-1 "Permalink to this headline")

The PostgreSqlStore relies on the [Advisory Locks](https://www.postgresql.org/docs/current/explicit-locking.html) properties of the PostgreSQL database. That means that by using [PostgreSqlStore](https://symfony.com/doc/current/components/lock.html#lock-store-pgsql) the locks will be automatically released at the end of the session in case the client cannot unlock for any reason.

If the PostgreSQL service or the machine hosting it restarts, every lock would be lost without notifying the running processes.

If the TCP connection is lost, the PostgreSQL may release locks without notifying the application.

### [RedisStore](https://symfony.com/doc/8.0/components/lock.html#redisstore-1 "Permalink to this headline")

The way Redis works is to store items in memory. That means that by using the [RedisStore](https://symfony.com/doc/current/components/lock.html#lock-store-redis) the locks are not persisted and may disappear by mistake at any time.

If the Redis service or the machine hosting it restarts, every locks would be lost without notifying the running processes.

Warning

To avoid that someone else acquires a lock after a restart, it's recommended to delay service start and wait at least as long as the longest lock TTL.

Tip

Redis can be configured to persist items on disk, but this option would slow down writes on the service. This could go against other uses of the server.

When the Redis service is shared and used for multiple usages, locks could be removed by mistake.

Danger

The command `FLUSHDB` must not be called, or locks should be stored in a dedicated Redis service away from Cache.

### [CombinedStore](https://symfony.com/doc/8.0/components/lock.html#combinedstore-1 "Permalink to this headline")

Combined stores allow the storage of locks across several backends. It's a common mistake to think that the lock mechanism will be more reliable. This is wrong. The `CombinedStore` will be, at best, as reliable as the least reliable of all managed stores. As soon as one managed store returns erroneous information, the `CombinedStore` won't be reliable.

Warning

All concurrent processes must use the same configuration, with the same amount of managed stored and the same endpoint.

Tip

Instead of using a cluster of Redis or Memcached servers, it's better to use a `CombinedStore` with a single server per managed store.

### [SemaphoreStore](https://symfony.com/doc/8.0/components/lock.html#semaphorestore-1 "Permalink to this headline")

Semaphores are handled by the Kernel level. In order to be reliable, processes must run on the same machine, virtual machine or container. Be careful when updating a Kubernetes or Swarm service because for a short period of time, there can be two running containers in parallel.

Warning

All concurrent processes must use the same machine. Before starting a concurrent process on a new machine, check that other processes are stopped on the old one.

Warning

When running on systemd with non-system user and option `RemoveIPC=yes` (default value), locks are deleted by systemd when that user logs out. Check that process is run with a system user (UID <= SYS_UID_MAX) with `SYS_UID_MAX` defined in `/etc/login.defs`, or set the option `RemoveIPC=off` in `/etc/systemd/logind.conf`.

### [ZookeeperStore](https://symfony.com/doc/8.0/components/lock.html#zookeeperstore-1 "Permalink to this headline")

The way ZookeeperStore works is by maintaining locks as ephemeral nodes on the server. That means that by using [ZookeeperStore](https://symfony.com/doc/current/components/lock.html#lock-store-zookeeper) the locks will be automatically released at the end of the session in case the client cannot unlock for any reason.

If the ZooKeeper service or the machine hosting it restarts, every lock would be lost without notifying the running processes.

Tip

To use ZooKeeper's high-availability feature, you can set up a cluster of multiple servers so that in case one of the server goes down, the majority will still be up and serving the requests. All the available servers in the cluster will see the same state.

Note

As this store does not support multi-level node locks, since the clean up of intermediate nodes becomes an overhead, all locks are maintained at the root level.

### [Overall](https://symfony.com/doc/8.0/components/lock.html#overall "Permalink to this headline")

Changing the configuration of stores should be done very carefully. For instance, during the deployment of a new version. Processes with new configuration must not be started while old processes with old configuration are still running.

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
