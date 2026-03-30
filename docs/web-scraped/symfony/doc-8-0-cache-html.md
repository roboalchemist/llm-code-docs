# Source: https://symfony.com/doc/8.0/cache.html

Title: Cache (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/cache.html

Markdown Content:
Cache (Symfony Docs)
===============

[Skip to content](https://symfony.com/doc/8.0/cache.html#main-content)

[Symfony Hub](https://symfony.com/doc/8.0/cache.html# "Toggle Symfony menu")[SF H](https://symfony.com/doc/8.0/cache.html# "Toggle Symfony menu")

[![Image 1](https://connect.symfony.com/uploads/sln/1c5498dd-0649-4d42-af4b-1de957825f62/8a08e0e0-cc2d-490f-9a2f-882979624a7f.png) Blackfire.io](https://www.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler)[![Image 2](https://connect.symfony.com/uploads/sln/1c5498dd-0649-4d42-af4b-1de957825f62/8a08e0e0-cc2d-490f-9a2f-882979624a7f.png) Blackfire.io: Fire up your PHP apps performance](https://www.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler)[![Image 3](https://connect.symfony.com/uploads/sln/1c5498dd-0649-4d42-af4b-1de957825f62/8a08e0e0-cc2d-490f-9a2f-882979624a7f.png) Blackfire.io: Fire up your PHP apps performance](https://www.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler)

[](https://symfony.com/doc/8.0/cache.html# "Search")

[](https://symfony.com/doc/8.0/cache.html# "Search")Search

[Connect](https://symfony.com/connect/login?target=https://symfony.com/doc/current/cache.html)

![Image 4: SensioLabs](https://connect.symfony.com/assets/images/sln-v2/sensiolabs-9Agct9D.png)
SensioLabs is the creator of Symfony and plays a pivotal role in supporting its growth. With a passionate team pushing the boundaries of PHP, SensioLabs helps organizations get the most out of Symfony through quality, high-performance, software vendor-level training and consulting services.

* [International](https://sensiolabs.com/en)
* [France](https://sensiolabs.com/fr)

In the Spotlight
----------------

[![Image 5: SymfonyInsight](https://connect.symfony.com/assets/images/sln-v2/symfonyinsight-HwpmiQ3.png)](https://insight.symfony.com/)

[![Image 6: Blackfire](https://connect.symfony.com/assets/images/sln-v2/blackfire-ca6NfRp.png)](https://www.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler)

Open Source
-----------

* [Symfony - Web framework](https://symfony.com/)
* [Twig - Templating](https://twig.symfony.com/)
* [PHP Polyfills](https://github.com/symfony/polyfill)

Products
--------

* [Insight: PHP Quality](https://insight.symfony.com/)
* [Blackfire: Web App performance](https://www.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler)
* [SymfonyCloud powered by Upsun](https://symfony.com/cloud)

Solutions & Services
--------------------

* [Training](https://training.sensiolabs.com/)
* [Certification](https://certification.symfony.com/)
* [Technical Solutions](https://sensiolabs.com/solutions)
* [SensioLabs University](https://university.sensiolabs.com/)
* [Experts](https://expert.sensiolabs.com/)

Community
---------

* [Community](https://connect.symfony.com/)
* [Conferences](https://live.symfony.com/)
* [Videos](https://www.youtube.com/symfonytv)
* [Partners](https://network.sensiolabs.com/en/partenaires)

Blogs
-----

[Symfony](https://symfony.com/blog/), [SensioLabs](https://blog.sensiolabs.com/), [Insight](https://blog.insight.symfony.com/), and [Blackfire](https://blog.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler).

[](https://symfony.com/)

Close

* About

  * [What is Symfony?](https://symfony.com/what-is-symfony)
  * [Community](https://symfony.com/community)
  * [News](https://symfony.com/blog/)
  * [Contributing](https://symfony.com/doc/current/contributing/index.html)
  * [Support](https://symfony.com/support)

* Documentation

  * [Symfony Docs](https://symfony.com/doc)
  * [Symfony Book](https://symfony.com/book)
  * [Screencasts](https://symfonycasts.com/)
  * [Symfony Bundles](https://symfony.com/bundles)
  * [Symfony Cloud](https://symfony.com/doc/cloud/)
  * [Training](https://sensiolabs.com/training?utm_source=symfony&utm_medium=symfony_submenu&utm_campaign=permanent_referral)

* Services

  * [Upsun for Symfony](https://symfony.com/cloud/)Best platform to deploy Symfony apps
  * [SymfonyInsight](https://insight.symfony.com/)Automatic quality checks for your apps
  * [Symfony Certification](https://certification.symfony.com/)Prove your knowledge and boost your career
  * [SensioLabs](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_submenu&utm_campaign=permanent_referral)Professional services to help you with Symfony
  * [Blackfire](https://www.blackfire.io/?utm_source=symfony&utm_medium=symfonycom_footer&utm_campaign=profiler)Profile and monitor performance of your apps

* Other
* [Blog](https://symfony.com/blog/)
* [Download](https://symfony.com/download)

sponsored by[](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_sponsoredby&utm_campaign=permanent_referral "SensioLabs, PHP services and software solutions for enterprise and community.")

[SymfonyLive Berlin 2026](https://live.symfony.com/2026-berlin)

April 23 – 24, 2026

+20 talks and workshops

Register now

1. [Home](https://symfony.com/)
2. [Documentation](https://symfony.com/doc)
3. Cache

 Search Symfony Docs

Version:

Table of Contents

* [Configuring Cache with FrameworkBundle](https://symfony.com/doc/8.0/cache.html#configuring-cache-with-frameworkbundle)
* [Creating Custom (Namespaced) Pools](https://symfony.com/doc/8.0/cache.html#creating-custom-namespaced-pools)
* [Custom Provider Options](https://symfony.com/doc/8.0/cache.html#custom-provider-options)
* [Creating a Cache Chain](https://symfony.com/doc/8.0/cache.html#creating-a-cache-chain)
* [Using Cache Tags](https://symfony.com/doc/8.0/cache.html#using-cache-tags)
* [Clearing the Cache](https://symfony.com/doc/8.0/cache.html#clearing-the-cache)
* [Encrypting the Cache](https://symfony.com/doc/8.0/cache.html#encrypting-the-cache)
* [Computing Cache Values Asynchronously](https://symfony.com/doc/8.0/cache.html#computing-cache-values-asynchronously)

Cache
=====

[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/cache.rst)

Using a cache is a great way of making your application run quicker. The Symfony cache component ships with many adapters to different storages. Every adapter is developed for high performance.

The following example shows a typical usage of the cache:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16

```
use Symfony\Contracts\Cache\ItemInterface;

// The callable will only be executed on a cache miss.
$value = $pool->get('my_cache_key', function (ItemInterface $item): string {
    $item->expiresAfter(3600);

    // ... do some HTTP request or heavy computations
    $computedValue = 'foobar';

    return $computedValue;
});

echo $value; // 'foobar'

// ... and to remove the cache key
$pool->delete('my_cache_key');
```

Symfony supports Cache Contracts and PSR-6/16 interfaces. You can read more about these at the [component documentation](https://symfony.com/doc/8.0/components/cache.html).

[Configuring Cache with FrameworkBundle](https://symfony.com/doc/8.0/cache.html#configuring-cache-with-frameworkbundle "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------

When configuring the cache component there are a few concepts you should know:

**Pool** This is a service that you will interact with. Each pool will always have its own namespace and cache items. There are never conflicts between pools. **Adapter** An adapter is a _template_ that you use to create pools. **Provider** A provider is a service that some adapters use to connect to the storage. Redis and Memcached are examples of such adapters. If a DSN is used as the provider then a service is automatically created.
There are two pools that are always enabled by default. They are `cache.app` and `cache.system`. The system cache is used for things like the serializer, and validation. The `cache.app` can be used in your code. You can configure which adapter (template) they use by using the `app` and `system` key like:

YAML PHP

1
2
3
4
5

```
# config/packages/cache.yaml
framework:
    cache:
        app: cache.adapter.filesystem
        system: cache.adapter.system
```

1
2
3
4
5
6
7
8
9
10
11

```
// config/packages/cache.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'framework' => [
        'cache' => [
            'app' => 'cache.adapter.filesystem',
            'system' => 'cache.adapter.system',
        ],
    ],
]);
```

Tip

While it is possible to reconfigure the `system` cache, it's recommended to keep the default configuration applied to it by Symfony.

The Cache component comes with a series of adapters pre-configured:

* [cache.adapter.apcu](https://symfony.com/doc/8.0/components/cache/adapters/apcu_adapter.html)
* [cache.adapter.array](https://symfony.com/doc/8.0/components/cache/adapters/array_cache_adapter.html)
* [cache.adapter.doctrine_dbal](https://symfony.com/doc/8.0/components/cache/adapters/doctrine_dbal_adapter.html)
* [cache.adapter.filesystem](https://symfony.com/doc/8.0/components/cache/adapters/filesystem_adapter.html)
* [cache.adapter.memcached](https://symfony.com/doc/8.0/components/cache/adapters/memcached_adapter.html)
* [cache.adapter.pdo](https://symfony.com/doc/8.0/components/cache/adapters/pdo_adapter.html)
* [cache.adapter.psr6](https://symfony.com/doc/8.0/components/cache/adapters/proxy_adapter.html)
* [cache.adapter.redis](https://symfony.com/doc/8.0/components/cache/adapters/redis_adapter.html)
* [cache.adapter.redis_tag_aware](https://symfony.com/doc/8.0/components/cache/adapters/redis_adapter.html#redis-tag-aware-adapter) (Redis adapter optimized to work with tags)

Note

There's also a special `cache.adapter.system` adapter. It's recommended to use it for the [system cache](https://symfony.com/doc/8.0/cache.html#cache-app-system). This adapter uses some logic to dynamically select the best possible storage based on your system (either PHP files or APCu).

Some of these adapters could be configured via shortcuts.

YAML PHP

1
2
3
4
5
6
7
8
9
10

```
# config/packages/cache.yaml
framework:
    cache:
        directory: '%kernel.cache_dir%/pools' # Only used with cache.adapter.filesystem

        default_doctrine_dbal_provider: 'doctrine.dbal.default_connection'
        default_psr6_provider: 'app.my_psr6_service'
        default_redis_provider: 'redis://localhost'
        default_memcached_provider: 'memcached://localhost'
        default_pdo_provider: 'pgsql:host=localhost'
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15

```
// config/packages/cache.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'framework' => [
        'cache' => [
            'directory' => '%kernel.cache_dir%/pools', // Only used with cache.adapter.filesystem
            'default_doctrine_dbal_provider' => 'doctrine.dbal.default_connection',
            'default_psr6_provider' => 'app.my_psr6_service',
            'default_redis_provider' => 'redis://localhost',
            'default_memcached_provider' => 'memcached://localhost',
            'default_pdo_provider' => 'pgsql:host=localhost',
        ],
    ],
]);
```

[Creating Custom (Namespaced) Pools](https://symfony.com/doc/8.0/cache.html#creating-custom-namespaced-pools "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------

You can also create more customized pools:

YAML PHP

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31

```
# config/packages/cache.yaml
framework:
    cache:
        default_memcached_provider: 'memcached://localhost'

        pools:
            # creates a "custom_thing.cache" service
            # autowireable via "CacheInterface $customThingCache"
            # uses the "app" cache configuration
            custom_thing.cache:
                adapter: cache.app

            # creates a "my_cache_pool" service
            # autowireable via "CacheInterface $myCachePool"
            my_cache_pool:
                adapter: cache.adapter.filesystem

            # uses the default_memcached_provider from above
            acme.cache:
                adapter: cache.adapter.memcached

            # control adapter's configuration
            foobar.cache:
                adapter: cache.adapter.memcached
                provider: 'memcached://user:password@example.com'

            # uses the "foobar.cache" pool as its backend but controls
            # the lifetime and (like all pools) has a separate cache namespace
            short_cache:
                adapter: foobar.cache
                default_lifetime: 60
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38

```
// config/packages/cache.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'framework' => [
        'cache' => [
            'default_memcached_provider' => 'memcached://localhost',
            'pools' => [
                // creates a "custom_thing.cache" service
                // autowireable via "CacheInterface $customThingCache"
                // uses the "app" cache configuration
                'custom_thing.cache' => [
                    'adapter' => 'cache.app',
                ],
                // creates a "my_cache_pool" service
                // autowireable via "CacheInterface $myCachePool"
                'my_cache_pool' => [
                    'adapter' => 'cache.adapter.filesystem',
                ],
                // uses the default_memcached_provider from above
                'acme.cache' => [
                    'adapter' => 'cache.adapter.memcached',
                ],
                // control adapter's configuration
                'foobar.cache' => [
                    'adapter' => 'cache.adapter.memcached',
                    'provider' => 'memcached://user:password@example.com',
                ],
                // uses the "foobar.cache" pool as its backend but controls
                // the lifetime and (like all pools) has a separate cache namespace
                'short_cache' => [
                    'adapter' => 'foobar.cache',
                    'default_lifetime' => 60,
                ],
            ],
        ],
    ],
]);
```

Each pool manages a set of independent cache keys: keys from different pools _never_ collide, even if they share the same backend. This is achieved by prefixing keys with a namespace that's generated by hashing the name of the pool, the name of the cache adapter class and a [configurable seed](https://symfony.com/doc/8.0/reference/configuration/framework.html#reference-cache-prefix-seed) that defaults to the project directory and compiled container class.

Each custom pool becomes a service whose service ID is the name of the pool (e.g. `custom_thing.cache`). An autowiring alias is also created for each pool using the camel case version of its name - e.g. `custom_thing.cache` can be injected automatically by naming the argument `$customThingCache` and type-hinting it with either [CacheInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Contracts/Cache/CacheInterface.php "Symfony\Contracts\Cache\CacheInterface") or `Psr\Cache\CacheItemPoolInterface`:

1
2
3
4
5
6
7
8
9
10
11
12
13
14

```
use Symfony\Contracts\Cache\CacheInterface;
// ...

// from a controller method
public function listProducts(CacheInterface $customThingCache): Response
{
    // ...
}

// in a service
public function __construct(private CacheInterface $customThingCache)
{
    // ...
}
```

Tip

If you need the namespace to be interoperable with a third-party app, you can take control over auto-generation by setting the `namespace` attribute of the `cache.pool` service tag. For example, you can override the service definition of the adapter:

YAML

1
2
3
4
5
6
7
8

```
# config/services.yaml
services:
    # ...

    app.cache.adapter.redis:
        parent: 'cache.adapter.redis'
        tags:
            - { name: 'cache.pool', namespace: 'my_custom_namespace' }
```

[Custom Provider Options](https://symfony.com/doc/8.0/cache.html#custom-provider-options "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------

Some providers have specific options that can be configured. The [RedisAdapter](https://symfony.com/doc/8.0/components/cache/adapters/redis_adapter.html) allows you to create providers with the options `timeout`, `retry_interval`. etc. To use these options with non-default values you need to create your own `\Redis` provider and use that when configuring the pool.

YAML PHP

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15

```
# config/packages/cache.yaml
framework:
    cache:
        pools:
            cache.my_redis:
                adapter: cache.adapter.redis
                provider: app.my_custom_redis_provider

services:
    app.my_custom_redis_provider:
        class: \Redis
        factory: ['Symfony\Component\Cache\Adapter\RedisAdapter', 'createConnection']
        arguments:
            - 'redis://localhost'
            - { retry_interval: 2, timeout: 10 }
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24

```
// config/packages/cache.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use Symfony\Component\Cache\Adapter\RedisAdapter;

return App::config([
    'framework' => [
        'cache' => [
            'pools' => [
                'cache.my_redis' => [
                    'adapter' => 'cache.adapter.redis',
                    'provider' => 'app.my_custom_redis_provider',
                ],
            ],
        ],
    ],
    'services' => [
        'app.my_custom_redis_provider' => [
            'class' => \Redis::class,
            'factory' => [RedisAdapter::class, 'createConnection'],
            'arguments' => ['redis://localhost', ['retry_interval' => 2, 'timeout' => 10]],
        ],
    ],
]);
```

[Creating a Cache Chain](https://symfony.com/doc/8.0/cache.html#creating-a-cache-chain "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------

Different cache adapters have different strengths and weaknesses. Some might be really quick but optimized to store small items and some may be able to contain a lot of data but are quite slow. To get the best of both worlds you may use a chain of adapters.

A cache chain combines several cache pools into a single one. When storing an item in a cache chain, Symfony stores it in all pools sequentially. When retrieving an item, Symfony tries to get it from the first pool. If it's not found, it tries the next pools until the item is found or an exception is thrown. Because of this behavior, it's recommended to define the adapters in the chain in order from fastest to slowest.

If an error happens when storing an item in a pool, Symfony stores it in the other pools and no exception is thrown. Later, when the item is retrieved, Symfony stores the item automatically in all the missing pools.

YAML PHP

1
2
3
4
5
6
7
8
9
10

```
# config/packages/cache.yaml
framework:
    cache:
        pools:
            my_cache_pool:
                default_lifetime: 31536000  # One year
                adapters:
                  - cache.adapter.array
                  - cache.adapter.apcu
                  - {name: cache.adapter.redis, provider: 'redis://user:password@example.com'}
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19

```
// config/packages/cache.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'framework' => [
        'cache' => [
            'pools' => [
                'my_cache_pool' => [
                    'default_lifetime' => 31536000, // One year
                    'adapters' => [
                        'cache.adapter.array',
                        'cache.adapter.apcu',
                        ['name' => 'cache.adapter.redis', 'provider' => 'redis://user:password@example.com'],
                    ],
                ],
            ],
        ],
    ],
]);
```

[Using Cache Tags](https://symfony.com/doc/8.0/cache.html#using-cache-tags "Permalink to this headline")
--------------------------------------------------------------------------------------------------------

In applications with many cache keys it could be useful to organize the data stored to be able to invalidate the cache more efficiently. One way to achieve that is to use cache tags. One or more tags could be added to the cache item. All items with the same tag could be invalidated with one function call:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29

```
use Symfony\Contracts\Cache\ItemInterface;
use Symfony\Contracts\Cache\TagAwareCacheInterface;

class SomeClass
{
    // using autowiring to inject the cache pool
    public function __construct(
        private TagAwareCacheInterface $myCachePool,
    ) {
    }

    public function someMethod(): void
    {
        $value0 = $this->myCachePool->get('item_0', function (ItemInterface $item): string {
            $item->tag(['foo', 'bar']);

            return 'debug';
        });

        $value1 = $this->myCachePool->get('item_1', function (ItemInterface $item): string {
            $item->tag('foo');

            return 'debug';
        });

        // Remove all cache keys tagged with "bar"
        $this->myCachePool->invalidateTags(['bar']);
    }
}
```

The cache adapter needs to implement [TagAwareCacheInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Contracts/Cache/TagAwareCacheInterface.php "Symfony\Contracts\Cache\TagAwareCacheInterface") to enable this feature. This could be added by using the following configuration.

YAML PHP

1
2
3
4
5
6
7

```
# config/packages/cache.yaml
framework:
    cache:
        pools:
            my_cache_pool:
                adapter: cache.adapter.redis_tag_aware
                tags: true
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15

```
// config/packages/cache.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'framework' => [
        'cache' => [
            'pools' => [
                'my_cache_pool' => [
                    'adapter' => 'cache.adapter.redis_tag_aware',
                    'tags' => true,
                ],
            ],
        ],
    ],
]);
```

Tags are stored in the same pool by default. This is good in most scenarios. But sometimes it might be better to store the tags in a different pool. That could be achieved by specifying the adapter.

YAML PHP

1
2
3
4
5
6
7
8
9

```
# config/packages/cache.yaml
framework:
    cache:
        pools:
            my_cache_pool:
                adapter: cache.adapter.redis
                tags: tag_pool
            tag_pool:
                adapter: cache.adapter.apcu
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18

```
// config/packages/cache.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'framework' => [
        'cache' => [
            'pools' => [
                'my_cache_pool' => [
                    'adapter' => 'cache.adapter.redis',
                    'tags' => 'tag_pool',
                ],
                'tag_pool' => [
                    'adapter' => 'cache.adapter.apcu',
                ],
            ],
        ],
    ],
]);
```

Note

The interface [TagAwareCacheInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Contracts/Cache/TagAwareCacheInterface.php "Symfony\Contracts\Cache\TagAwareCacheInterface") is autowired to the `cache.app` service.

[Clearing the Cache](https://symfony.com/doc/8.0/cache.html#clearing-the-cache "Permalink to this headline")
------------------------------------------------------------------------------------------------------------

To clear the cache you can use the `bin/console cache:pool:clear [pool]` command. That will remove all the entries from your storage and you will have to recalculate all the values. You can also group your pools into "cache clearers". There are 3 cache clearers by default:

* `cache.global_clearer`
* `cache.system_clearer`
* `cache.app_clearer`

The global clearer clears all the cache items in every pool. The system cache clearer is used in the `bin/console cache:clear` command. The app clearer is the default clearer.

To see all available cache pools:

1`$ php bin/console cache:pool:list`

Clear one pool:

1`$ php bin/console cache:pool:clear my_cache_pool`

Clear all custom pools:

1`$ php bin/console cache:pool:clear cache.app_clearer`

Clear all cache pools:

1`$ php bin/console cache:pool:clear --all`

Clear all cache pools except some:

1`$ php bin/console cache:pool:clear --all --exclude=my_cache_pool --exclude=another_cache_pool`

Clear all caches everywhere:

1`$ php bin/console cache:pool:clear cache.global_clearer`

Clear cache by tag(s):

1
2
3
4
5
6
7
8
9
10
11

```
# invalidate tag1 from all taggable pools
$ php bin/console cache:pool:invalidate-tags tag1

# invalidate tag1 & tag2 from all taggable pools
$ php bin/console cache:pool:invalidate-tags tag1 tag2

# invalidate tag1 & tag2 from cache.app pool
$ php bin/console cache:pool:invalidate-tags tag1 tag2 --pool=cache.app

# invalidate tag1 & tag2 from cache1 & cache2 pools
$ php bin/console cache:pool:invalidate-tags tag1 tag2 -p cache1 -p cache2
```

[Encrypting the Cache](https://symfony.com/doc/8.0/cache.html#encrypting-the-cache "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------

To encrypt the cache using `libsodium`, you can use the [SodiumMarshaller](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Cache/Marshaller/SodiumMarshaller.php "Symfony\Component\Cache\Marshaller\SodiumMarshaller").

First, you need to generate a secure key and add it to your [secret store](https://symfony.com/doc/8.0/configuration/secrets.html) as `CACHE_DECRYPTION_KEY`:

1`$ php -r 'echo base64_encode(sodium_crypto_box_keypair());'`

Then, register the `SodiumMarshaller` service using this key:

YAML PHP

1
2
3
4
5
6
7
8
9
10
11

```
# config/packages/cache.yaml

# ...
services:
    Symfony\Component\Cache\Marshaller\SodiumMarshaller:
        decorates: cache.default_marshaller
        arguments:
            - ['%env(base64:CACHE_DECRYPTION_KEY)%']
            # use multiple keys in order to rotate them
            #- ['%env(base64:CACHE_DECRYPTION_KEY)%', '%env(base64:OLD_CACHE_DECRYPTION_KEY)%']
            - '@.inner'
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18

```
// config/packages/cache.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use Symfony\Component\Cache\Marshaller\SodiumMarshaller;

return App::config([
    'services' => [
        SodiumMarshaller::class => [
            'decorates' => 'cache.default_marshaller',
            'arguments' => [
                [env('CACHE_DECRYPTION_KEY')->base64()],
                // use multiple keys in order to rotate them
                // [env('CACHE_DECRYPTION_KEY')->base64(), env('OLD_CACHE_DECRYPTION_KEY')->base64()]
                service('.inner'),
            ],
        ],
    ],
]);
```

Danger

This will encrypt the values of the cache items, but not the cache keys. Be careful not to leak sensitive data in the keys.

When configuring multiple keys, the first key will be used for reading and writing, and the additional key(s) will only be used for reading. Once all cache items encrypted with the old key have expired, you can completely remove `OLD_CACHE_DECRYPTION_KEY`.

[Computing Cache Values Asynchronously](https://symfony.com/doc/8.0/cache.html#computing-cache-values-asynchronously "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------

The Cache component uses the [probabilistic early expiration](https://en.wikipedia.org/wiki/Cache_stampede#Probabilistic_early_expiration) algorithm to protect against the [cache stampede](https://symfony.com/doc/8.0/components/cache.html#cache_stampede-prevention) problem. This means that some cache items are elected for early-expiration while they are still fresh.

By default, expired cache items are computed synchronously. However, you can compute them asynchronously by delegating the value computation to a background worker using the [Messenger component](https://symfony.com/doc/8.0/components/messenger.html). In this case, when an item is queried, its cached value is immediately returned and a [EarlyExpirationMessage](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Cache/Messenger/EarlyExpirationMessage.php "Symfony\Component\Cache\Messenger\EarlyExpirationMessage") is dispatched through a Messenger bus.

When this message is handled by a message consumer, the refreshed cache value is computed asynchronously. The next time the item is queried, the refreshed value will be fresh and returned.

First, create a service that will compute the item's value:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16

```
// src/Cache/CacheComputation.php
namespace App\Cache;

use Psr\Cache\CacheItemInterface;
use Symfony\Contracts\Cache\CallbackInterface;

class CacheComputation implements CallbackInterface
{
    public function __invoke(CacheItemInterface $item, bool &$save): string
    {
        $item->expiresAfter(5);

        // this is just a random example; here you must do your own calculation
        return sprintf('#%06X', mt_rand(0, 0xFFFFFF));
    }
}
```

This cache value will be requested from a controller, another service, etc. In the following example, the value is requested from a controller:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

```
// src/Controller/CacheController.php
namespace App\Controller;

use App\Cache\CacheComputation;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Contracts\Cache\CacheInterface;
use Symfony\Contracts\Cache\ItemInterface;

class CacheController extends AbstractController
{
    #[Route('/cache', name: 'cache')]
    public function index(CacheInterface $asyncCache, CacheComputation $cacheComputation): Response
    {
        // pass to the cache the service method that refreshes the item
        $cachedValue = $asyncCache->get('my_value', $cacheComputation)

        // ...
    }
}
```

Finally, configure a new cache pool (e.g. called `async.cache`) that will use a message bus to compute values in a worker:

YAML PHP

1
2
3
4
5
6
7
8
9
10
11
12

```
# config/packages/framework.yaml
framework:
    cache:
        pools:
            async.cache:
                early_expiration_message_bus: messenger.default_bus

    messenger:
        transports:
            async_bus: '%env(MESSENGER_TRANSPORT_DSN)%'
        routing:
            'Symfony\Component\Cache\Messenger\EarlyExpirationMessage': async_bus
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24

```
// config/framework/framework.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use Symfony\Component\Cache\Messenger\EarlyExpirationMessage;

return App::config([
    'framework' => [
        'cache' => [
            'pools' => [
                'async.cache' => [
                    'early_expiration_message_bus' => 'messenger.default_bus',
                ],
            ],
        ],
        'messenger' => [
            'transports' => [
                'async_bus' => env('MESSENGER_TRANSPORT_DSN'),
            ],
            'routing' => [
                EarlyExpirationMessage::class => 'async_bus',
            ],
        ],
    ],
]);
```

You can now start the consumer:

1`$ php bin/console messenger:consume async_bus`

That's it! Now, whenever an item is queried from this cache pool, its cached value will be returned immediately. If it is elected for early-expiration, a message will be sent through to bus to schedule a background computation to refresh the value.

 This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.

 TOC

 Search

 Version

**Symfony 8.0**[backers](https://symfony.com/backers)

[](https://sulu.io/)

[](https://jb.gg/fbsk8y)

[![Image 7: ads via Carbon](https://srv.carbonads.net/static/30242/bb0b2a898008ba2d4ba0898af490dde617c4c7bb)](https://srv.carbonads.net/ads/click/x/GTND427UCKYILKQNF67LYKQUCA7I523YCVYITZ3JCASIC53UF6YIVKJKCYSDP5QEC6SI4KJMCY7IC27UF6SI4Z3JCASICKQ7CTADTK3K2JWNABY)[Get the APM insights you need without enterprise price tags. Built for dev teams, not Fortune 500s](https://srv.carbonads.net/ads/click/x/GTND427UCKYILKQNF67LYKQUCA7I523YCVYITZ3JCASIC53UF6YIVKJKCYSDP5QEC6SI4KJMCY7IC27UF6SI4Z3JCASICKQ7CTADTK3K2JWNABY)[ads via Carbon](http://carbonads.net/?utm_source=symfonycom&utm_medium=ad_via_link&utm_campaign=in_unit&utm_term=carbon)

[![Image 8: Peruse our complete Symfony & PHP solutions catalog for your web development needs.](https://symfony.com/images/network/slsolutions_01.webp)](https://sensiolabs.com/services?utm_source=symfony&utm_medium=ad_visual&utm_campaign=permanent_referral)
[Peruse our complete Symfony & PHP solutions catalog for your web development needs.](https://sensiolabs.com/services?utm_source=symfony&utm_medium=ad_visual&utm_campaign=permanent_referral)

[![Image 9: Be safe against critical risks to your projects and businesses](https://symfony.com/images/network/sfinsight_02.png)](https://insight.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=insight&utm_content=safe)
[Be safe against critical risks to your projects and businesses](https://insight.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=insight&utm_content=safe)

Symfony footer
--------------

![Image 10: Avatar of Denis Zunke, a Symfony contributor](https://connect.symfony.com/api/images/350a0535-c157-4901-9039-a1ccfc66e88d.png?format=48x48)

Thanks **[Denis Zunke](https://connect.symfony.com/profile/donalberto)** (**@donalberto**) for being a Symfony contributor

[**2** commits](https://github.com/symfony/symfony/commits?author=DZunke) • **27** lines changed

[View all contributors](https://symfony.com/contributors) that help us make Symfony

### Become a Symfony contributor

Be an active part of the community and contribute ideas, code and bug fixes. Both experts and newcomers are welcome.

[Learn how to contribute](https://symfony.com/doc/current/contributing/index.html)

![Image 11](https://symfony.com/assets/icons/logos/sf-20years-wordmark-dark--dFsFxh.webp)
[Celebrating 20 years of Symfony](https://symfony.com/20years)

**Symfony**™ is a trademark of Symfony SAS. [All rights reserved](https://symfony.com/trademark).

* [What is Symfony?](https://symfony.com/what-is-symfony)

  * [What is Symfony?](https://symfony.com/what-is-symfony)
  * [Symfony at a Glance](https://symfony.com/at-a-glance)
  * [Symfony Packages](https://symfony.com/packages)
  * [Symfony Releases](https://symfony.com/releases)
  * [Security Policy](https://symfony.com/doc/current/contributing/code/security.html)
  * [Logo & Screenshots](https://symfony.com/logo)
  * [Trademark & Licenses](https://symfony.com/license)
  * [symfony1 Legacy](https://symfony.com/legacy)

* [Learn Symfony](https://symfony.com/doc)

  * [Symfony Docs](https://symfony.com/doc)
  * [Symfony Book](https://symfony.com/book)
  * [Reference](https://symfony.com/doc/current/reference/index.html)
  * [Bundles](https://symfony.com/bundles)
  * [Best Practices](https://symfony.com/doc/current/best_practices.html)
  * [Training](https://sensiolabs.com/training/courses?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
  * [eLearning Platform](https://university.sensiolabs.com/e-learning-platform?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
  * [Certification](https://certification.symfony.com/)

* [Screencasts](https://symfonycasts.com/)

  * [Learn Symfony](https://symfonycasts.com/tracks/symfony)
  * [Learn PHP](https://symfonycasts.com/tracks/php)
  * [Learn JavaScript](https://symfonycasts.com/tracks/javascript)
  * [Learn Drupal](https://symfonycasts.com/tracks/drupal)
  * [Learn RESTful APIs](https://symfonycasts.com/tracks/rest)

* [Community](https://symfony.com/community)

  * [Symfony Community](https://symfony.com/community)
  * [SymfonyConnect](https://connect.symfony.com/)
  * [Events & Meetups](https://symfony.com/events/)
  * [Projects using Symfony](https://symfony.com/projects)
  * [Contributors](https://symfony.com/contributors)
  * [Symfony Jobs](https://symfony.com/jobs)
  * [Backers](https://symfony.com/backers)
  * [Code of Conduct](https://symfony.com/doc/current/contributing/code_of_conduct/code_of_conduct.html)
  * [Downloads Stats](https://symfony.com/stats/downloads)
  * [Support](https://symfony.com/support)

* [Blog](https://symfony.com/blog/)

  * [All Blog Posts](https://symfony.com/blog/)
  * [A Week of Symfony](https://symfony.com/blog/category/a-week-of-symfony)
  * [Case Studies](https://symfony.com/blog/category/case-studies)
  * [Cloud](https://symfony.com/blog/category/cloud)
  * [Community](https://symfony.com/blog/category/community)
  * [Conferences](https://symfony.com/blog/category/conferences)
  * [Diversity](https://symfony.com/blog/category/diversity)
  * [Living on the edge](https://symfony.com/blog/category/living-on-the-edge)
  * [Releases](https://symfony.com/blog/category/releases)
  * [Security Advisories](https://symfony.com/blog/category/security-advisories)
  * [Symfony Insight](https://symfony.com/blog/category/symfony-insight)
  * [Twig](https://symfony.com/blog/category/twig)
  * [SensioLabs Blog](https://sensiolabs.com/blog?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)

* [Services](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)

  * [SensioLabs services](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
  * [Train developers](https://sensiolabs.com/training?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
  * [Manage your project quality](https://insight.symfony.com/)
  * [Improve your project performance](https://www.blackfire.io/?utm_source=symfony&utm_medium=symfonycom_footer&utm_campaign=profiler)
  * [Host Symfony projects](https://symfony.com/cloud/)

[Powered by](https://symfony.com/cloud/)

[](https://symfony.com/cloud/ "Upsun, a Platform-as-a-Service optimized for Symfony developers")

### Follow Symfony

[](https://github.com/symfony "Symfony on GitHub")[](https://symfony.com/slack "Symfony on Slack")[](https://twitter.com/symfony "Symfony on Twitter")[](https://mastodon.social/@symfony "Symfony on Mastodon")[](https://www.linkedin.com/company/symfony-sas/ "Symfony on LinkedIn")[](https://www.facebook.com/SymfonyFramework "Symfony on Facebook")[](https://www.youtube.com/symfonytv "Symfony on YouTube")[](https://bsky.app/profile/symfony.com "Symfony on BlueSky")[](https://www.threads.net/@symfony "Symfony on Threads")[](https://symfonycasts.com/ "Symfony Screencasts")[](https://feeds.feedburner.com/symfony/blog "Symfony Blog RSS")

Site appearance:

CLOSE

Search Symfony Docs

Search
