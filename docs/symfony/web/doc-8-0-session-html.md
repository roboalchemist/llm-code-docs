# Source: https://symfony.com/doc/8.0/session.html

Title: Sessions (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/session.html

Markdown Content:
Sessions (Symfony Docs)
===============

[Skip to content](https://symfony.com/doc/8.0/session.html#main-content)

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

1. [Home](https://symfony.com/)
2. [Documentation](https://symfony.com/doc)
3. Sessions

 Search Symfony Docs

Version:

Table of Contents

* [Installation](https://symfony.com/doc/8.0/session.html#installation)
* [Basic Usage](https://symfony.com/doc/8.0/session.html#basic-usage)
* [Session Attributes](https://symfony.com/doc/8.0/session.html#session-attributes)
* [Flash Messages](https://symfony.com/doc/8.0/session.html#flash-messages)
* [Configuration](https://symfony.com/doc/8.0/session.html#configuration)
  * [Session Idle Time/Keep Alive](https://symfony.com/doc/8.0/session.html#session-idle-time-keep-alive)
  * [Configuring Garbage Collection](https://symfony.com/doc/8.0/session.html#configuring-garbage-collection)

* [Store Sessions in a Database](https://symfony.com/doc/8.0/session.html#store-sessions-in-a-database)
  * [Store Sessions in a key-value Database (Redis)](https://symfony.com/doc/8.0/session.html#store-sessions-in-a-key-value-database-redis)
  * [Store Sessions in a Relational Database (MariaDB, MySQL, PostgreSQL)](https://symfony.com/doc/8.0/session.html#store-sessions-in-a-relational-database-mariadb-mysql-postgresql)
  * [Store Sessions in a NoSQL Database (MongoDB)](https://symfony.com/doc/8.0/session.html#store-sessions-in-a-nosql-database-mongodb)
  * [Migrating Between Session Handlers](https://symfony.com/doc/8.0/session.html#migrating-between-session-handlers)
  * [Configuring the Session TTL](https://symfony.com/doc/8.0/session.html#configuring-the-session-ttl)

* [Making the Locale "Sticky" during a User's Session](https://symfony.com/doc/8.0/session.html#making-the-locale-sticky-during-a-user-s-session)
  * [Creating a LocaleSubscriber](https://symfony.com/doc/8.0/session.html#creating-a-localesubscriber)
  * [Setting the Locale Based on the User's Preferences](https://symfony.com/doc/8.0/session.html#setting-the-locale-based-on-the-user-s-preferences)

* [Session Proxies](https://symfony.com/doc/8.0/session.html#session-proxies)
  * [Encryption of Session Data](https://symfony.com/doc/8.0/session.html#encryption-of-session-data)
  * [Read-only Guest Sessions](https://symfony.com/doc/8.0/session.html#read-only-guest-sessions)

* [Integrating with Legacy Applications](https://symfony.com/doc/8.0/session.html#integrating-with-legacy-applications)

Sessions
========

[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/session.rst)

The Symfony HttpFoundation component has a very powerful and flexible session subsystem which is designed to provide session management that you can use to store information about the user between requests through a clear object-oriented interface using a variety of session storage drivers.

Symfony sessions are designed to replace the usage of the `$_SESSION` super global and native PHP functions related to manipulating the session like `session_start()`, `session_regenerate_id()`, `session_id()`, `session_name()`, and `session_destroy()`.

Note

Sessions are only started if you read or write from it.

[Installation](https://symfony.com/doc/8.0/session.html#installation "Permalink to this headline")
--------------------------------------------------------------------------------------------------

You need to install the HttpFoundation component to handle sessions:

1`$ composer require symfony/http-foundation`

[Basic Usage](https://symfony.com/doc/8.0/session.html#basic-usage "Permalink to this headline")
------------------------------------------------------------------------------------------------

The session is available through the `Request` object and the `RequestStack` service. Symfony injects the `request_stack` service in services and controllers if you type-hint an argument with [RequestStack](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/RequestStack.php "Symfony\Component\HttpFoundation\RequestStack"):

Framework Use Standalone Use

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
use Symfony\Component\HttpFoundation\RequestStack;

class SomeService
{
    public function __construct(
        private RequestStack $requestStack,
    ) {
        // Accessing the session in the constructor is *NOT* recommended, since
        // it might not be accessible yet or lead to unwanted side-effects
        // $this->session = $requestStack->getSession();
    }

    public function someMethod(): void
    {
        $session = $this->requestStack->getSession();

        // ...
    }
}
```

1
2
3
4

```
use Symfony\Component\HttpFoundation\Session\Session;

$session = new Session();
$session->start();
```

From a Symfony controller, you can also type-hint an argument with [Request](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/Request.php "Symfony\Component\HttpFoundation\Request"):

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
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

public function index(Request $request): Response
{
    $session = $request->getSession();

    // ...
}
```

[Session Attributes](https://symfony.com/doc/8.0/session.html#session-attributes "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------

PHP's session management requires the use of the `$_SESSION` super-global. However, this interferes with code testability and encapsulation in an OOP paradigm. To help overcome this, Symfony uses _session bags_ linked to the session to encapsulate a specific dataset of **attributes**.

This approach mitigates namespace pollution within the `$_SESSION` super-global because each bag stores all its data under a unique namespace. This allows Symfony to peacefully co-exist with other applications or libraries that might use the `$_SESSION` super-global and all data remains completely compatible with Symfony's session management.

A session bag is a PHP object that acts like an array:

1
2
3
4
5
6
7
8

```
// stores an attribute for reuse during a later user request
$session->set('attribute-name', 'attribute-value');

// gets an attribute by name
$foo = $session->get('foo');

// the second argument is the value returned when the attribute doesn't exist
$filters = $session->get('filters', []);
```

Stored attributes remain in the session for the remainder of that user's session. By default, session attributes are key-value pairs managed with the [AttributeBag](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/Session/Attribute/AttributeBag.php "Symfony\Component\HttpFoundation\Session\Attribute\AttributeBag") class.

Sessions are automatically started whenever you read, write or even check for the existence of data in the session. This may hurt your application performance because all users will receive a session cookie. In order to prevent starting sessions for anonymous users, you must _completely_ avoid accessing the session.

Note

Sessions will also be started when using features that rely on them internally, such as the [stateful CSRF protection in forms](https://symfony.com/doc/8.0/security/csrf.html#csrf-protection-forms).

[Flash Messages](https://symfony.com/doc/8.0/session.html#flash-messages "Permalink to this headline")
------------------------------------------------------------------------------------------------------

You can store special messages, called "flash" messages, on the user's session. By design, flash messages are meant to be used exactly once: they vanish from the session automatically as soon as you retrieve them. This feature makes "flash" messages particularly great for storing user notifications.

For example, imagine you're processing a [form](https://symfony.com/doc/8.0/forms.html) submission:

Framework Use Standalone Use

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

```
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
// ...

public function update(Request $request): Response
{
    // ...

    if ($form->isSubmitted() && $form->isValid()) {
        // do some sort of processing

        $this->addFlash(
            'notice',
            'Your changes were saved!'
        );
        // $this->addFlash() is equivalent to $request->getSession()->getFlashBag()->add()

        return $this->redirectToRoute(/* ... */);
    }

    return $this->render(/* ... */);
}
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

```
use Symfony\Component\HttpFoundation\Session\Session;

$session = new Session();
$session->start();

// retrieve the flash messages bag
$flashes = $session->getFlashBag();

// add flash messages
$flashes->add(
    'notice',
    'Your changes were saved'
);
```

After processing the request, the controller sets a flash message in the session and then redirects. The message key (`notice` in this example) can be anything. You'll use this key to retrieve the message.

In the template of the next page (or even better, in your base layout template), read any flash messages from the session using the `flashes()` method provided by the [Twig global app variable](https://symfony.com/doc/8.0/templates.html#twig-app-variable). Alternatively, you can use the [peek()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/Session/Flash/FlashBagInterface.php#:~:text=function%20peek "Symfony\Component\HttpFoundation\Session\Flash\FlashBagInterface::peek()") method to retrieve the message while keeping it in the bag:

Twig Standalone Use

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
39
40
41
42

```
{# templates/base.html.twig #}

{# read and display just one flash message type #}
{% for message in app.flashes('notice') %}
    <div class="flash-notice">
        {{ message }}
    </div>
{% endfor %}

{# same but without clearing them from the flash bag #}
{% for message in app.session.flashbag.peek('notice') %}
    <div class="flash-notice">
        {{ message }}
    </div>
{% endfor %}

{# read and display several types of flash messages #}
{% for label, messages in app.flashes(['success', 'warning']) %}
    {% for message in messages %}
        <div class="flash-{{ label }}">
            {{ message }}
        </div>
    {% endfor %}
{% endfor %}

{# read and display all flash messages #}
{% for label, messages in app.flashes %}
    {% for message in messages %}
        <div class="flash-{{ label }}">
            {{ message }}
        </div>
    {% endfor %}
{% endfor %}

{# or without clearing the flash bag #}
{% for label, messages in app.session.flashbag.peekAll() %}
    {% for message in messages %}
        <div class="flash-{{ label }}">
            {{ message }}
        </div>
    {% endfor %}
{% endfor %}
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

```
// display warnings
 foreach ($session->getFlashBag()->get('warning', []) as $message) {
     echo '<div class="flash-warning">'.$message.'</div>';
 }

 // display warnings without clearing them from the flash bag
 foreach ($session->getFlashBag()->peek('warning', []) as $message) {
     echo '<div class="flash-warning">'.$message.'</div>';
}

 // display errors
 foreach ($session->getFlashBag()->get('error', []) as $message) {
     echo '<div class="flash-error">'.$message.'</div>';
 }

 // display all flashes at once
 foreach ($session->getFlashBag()->all() as $type => $messages) {
     foreach ($messages as $message) {
         echo '<div class="flash-'.$type.'">'.$message.'</div>';
     }
 }

 // display all flashes at once without clearing the flash bag
 foreach ($session->getFlashBag()->peekAll() as $type => $messages) {
     foreach ($messages as $message) {
         echo '<div class="flash-'.$type.'">'.$message.'</div>';
     }
 }
```

It's common to use `notice`, `warning` and `error` as the keys of the different types of flash messages, but you can use any key that fits your needs.

Tip

Accessing flash messages requires starting the session, which in turn causes Symfony to mark the response as `private`. In general, because flash messages are meant to be displayed only once, pages that might show them cannot reasonably be cached by HTTP caches.

As an alternative, you can load flash messages asynchronously through another HTTP request (for example, using a [Twig Live Component](https://symfony.com/bundles/ux-live-component/current/index.html)), making the original page fully cacheable.

[Configuration](https://symfony.com/doc/8.0/session.html#configuration "Permalink to this headline")
----------------------------------------------------------------------------------------------------

In the Symfony framework, sessions are enabled by default. Session storage and other configuration can be controlled under the [framework.session configuration](https://symfony.com/doc/8.0/reference/configuration/framework.html#config-framework-session) in `config/packages/framework.yaml`:

YAML PHP Standalone Use

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
    # Enables session support. Note that the session will ONLY be started if you read or write from it.
    # Remove or comment this section to explicitly disable session support.
    session:
        # ID of the service used for session storage
        # NULL means that Symfony uses PHP default session mechanism
        handler_id: null
        # improves the security of the cookies used for sessions
        cookie_secure: auto
        cookie_samesite: lax
        storage_factory_id: session.storage.factory.native
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

```
// config/packages/framework.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use Symfony\Component\HttpFoundation\Cookie;

return App::config([
    'framework' => [
        'session' => [
            // Enables session support. Note that the session will ONLY be started if you read or write from it.
            // Remove or comment this section to explicitly disable session support.
            'enabled' => true,
            // ID of the service used for session storage
            // NULL means that Symfony uses PHP default session mechanism
            'handler_id' => null,
            // improves the security of the cookies used for sessions
            'cookie_secure' => 'auto',
            'cookie_samesite' => Cookie::SAMESITE_LAX,
            'storage_factory_id' => 'session.storage.factory.native',
        ],
    ],
]);
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

```
use Symfony\Component\HttpFoundation\Cookie;
use Symfony\Component\HttpFoundation\Session\Attribute\AttributeBag;
use Symfony\Component\HttpFoundation\Session\Session;
use Symfony\Component\HttpFoundation\Session\Storage\NativeSessionStorage;

$storage = new NativeSessionStorage([
    'cookie_secure' => 'auto',
    'cookie_samesite' => Cookie::SAMESITE_LAX,
]);
$session = new Session($storage);
```

Setting the `handler_id` config option to `null` means that Symfony will use the native PHP session mechanism. The session metadata files will be stored outside of the Symfony application, in a directory controlled by PHP. Although this usually simplifies things, some session expiration related options may not work as expected if other applications that write to the same directory have short max lifetime settings.

If you prefer, you can use the `session.handler.native_file` service as `handler_id` to let Symfony manage the sessions itself. Another useful option is `save_path`, which defines the directory where Symfony will store the session metadata files:

YAML PHP Standalone Use

1
2
3
4
5
6

```
# config/packages/framework.yaml
framework:
    session:
        # ...
        handler_id: 'session.handler.native_file'
        save_path: '%kernel.project_dir%/var/sessions/%kernel.environment%'
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

```
// config/packages/framework.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'framework' => [
        'session' => [
            // ...
            'handler_id' => 'session.handler.native_file',
            'save_path' => '%kernel.project_dir%/var/sessions/%kernel.environment%',
        ],
    ],
]);
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

```
use Symfony\Component\HttpFoundation\Cookie;
use Symfony\Component\HttpFoundation\Session\Attribute\AttributeBag;
use Symfony\Component\HttpFoundation\Session\Session;
use Symfony\Component\HttpFoundation\Session\Storage\Handler\NativeFileSessionHandler;
use Symfony\Component\HttpFoundation\Session\Storage\NativeSessionStorage;

$handler = new NativeFileSessionHandler('/var/sessions');
$storage = new NativeSessionStorage([], $handler);
$session = new Session($storage);
```

Check out the Symfony config reference to learn more about the other available [Session configuration options](https://symfony.com/doc/8.0/reference/configuration/framework.html#config-framework-session).

Warning

Symfony sessions are incompatible with `php.ini` directive `session.auto_start = 1` This directive should be turned off in `php.ini`, in the web server directives or in `.htaccess`.

The session cookie is also available in [the Response object](https://symfony.com/doc/8.0/components/http_foundation.html#component-http-foundation-response). This is useful to get that cookie in the CLI context or when using PHP runners like Roadrunner or Swoole.

### [Session Idle Time/Keep Alive](https://symfony.com/doc/8.0/session.html#session-idle-time-keep-alive "Permalink to this headline")

There are often circumstances where you may want to protect, or minimize unauthorized use of a session when a user steps away from their terminal while logged in by destroying the session after a certain period of idle time. For example, it is common for banking applications to log the user out after just 5 to 10 minutes of inactivity. Setting the cookie lifetime here is not appropriate because that can be manipulated by the client, so we must do the expiry on the server side. The easiest way is to implement this via [session garbage collection](https://symfony.com/doc/8.0/session.html#session-garbage-collection) which runs reasonably frequently. The `cookie_lifetime` would be set to a relatively high value, and the garbage collection `gc_maxlifetime` would be set to destroy sessions at whatever the desired idle period is.

The other option is specifically check if a session has expired after the session is started. The session can be destroyed as required. This method of processing can allow the expiry of sessions to be integrated into the user experience, for example, by displaying a message.

Symfony records some metadata about each session to give you fine control over the security settings:

1
2

```
$session->getMetadataBag()->getCreated();
$session->getMetadataBag()->getLastUsed();
```

Both methods return a Unix timestamp (relative to the server).

This metadata can be used to explicitly expire a session on access:

1
2
3
4
5

```
$session->start();
if (time() - $session->getMetadataBag()->getLastUsed() > $maxIdleTime) {
    $session->invalidate();
    throw new SessionExpired(); // redirect to expired session page
}
```

It is also possible to tell what the `cookie_lifetime` was set to for a particular cookie by reading the `getLifetime()` method:

1`$session->getMetadataBag()->getLifetime();`

The expiry time of the cookie can be determined by adding the created timestamp and the lifetime.

### [Configuring Garbage Collection](https://symfony.com/doc/8.0/session.html#configuring-garbage-collection "Permalink to this headline")

When a session opens, PHP will call the `gc` handler randomly according to the probability set by `session.gc_probability` / `session.gc_divisor`. For example if these were set to `5/100` respectively, it would mean a probability of 5%. Similarly, `3/4` would mean a 3 in 4 chance of being called, i.e. 75%.

If the garbage collection handler is invoked, PHP will pass the value stored in the `php.ini` directive `session.gc_maxlifetime`. The meaning in this context is that any stored session that was saved more than `gc_maxlifetime` ago should be deleted. This allows one to expire records based on idle time.

However, some operating systems (e.g. Debian) manage session handling differently and set the `session.gc_probability` variable to `0` to prevent PHP from performing garbage collection. By default, Symfony uses the value of the `gc_probability` directive set in the `php.ini` file. If you can't modify this PHP setting, you can configure it directly in Symfony:

1
2
3
4
5

```
# config/packages/framework.yaml
framework:
    session:
        # ...
        gc_probability: 1
```

Alternatively, you can configure these settings by passing `gc_probability`, `gc_divisor` and `gc_maxlifetime` in an array to the constructor of [NativeSessionStorage](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/Session/Storage/NativeSessionStorage.php "Symfony\Component\HttpFoundation\Session\Storage\NativeSessionStorage") or to the [setOptions()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/Session/Storage/NativeSessionStorage.php#:~:text=function%20setOptions "Symfony\Component\HttpFoundation\Session\Storage\NativeSessionStorage::setOptions()") method.

[Store Sessions in a Database](https://symfony.com/doc/8.0/session.html#store-sessions-in-a-database "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------

Symfony stores sessions in files by default. If your application is served by multiple servers, you'll need to use a database instead to make sessions work across different servers.

Symfony can store sessions in all kinds of databases (relational, NoSQL and key-value) but recommends key-value databases like Redis to get best performance.

### [Store Sessions in a key-value Database (Redis)](https://symfony.com/doc/8.0/session.html#store-sessions-in-a-key-value-database-redis "Permalink to this headline")

This section assumes that you have a fully-working Redis server and have also installed and configured the [phpredis extension](https://github.com/phpredis/phpredis).

You have two different options to use Redis to store sessions:

The first PHP-based option is to configure Redis session handler directly in the server `php.ini` file:

1
2
3

```
; php.ini
session.save_handler = redis
session.save_path = "tcp://192.168.0.178:6379?auth=REDIS_PASSWORD"
```

The second option is to configure Redis sessions in Symfony. First, define a Symfony service for the connection to the Redis server:

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

```
# config/services.yaml
services:
    # ...
    Symfony\Component\HttpFoundation\Session\Storage\Handler\RedisSessionHandler:
        arguments:
            - '@Redis'
            # you can optionally pass an array of options. The only options are 'prefix' and 'ttl',
            # which define the prefix to use for the keys to avoid collision on the Redis server
            # and the expiration time for any given entry (in seconds), defaults are 'sf_s' and null:
            # - { 'prefix': 'my_prefix', 'ttl': 600 }

    Redis:
        # you can also use \RedisArray, \RedisCluster, \Relay\Relay or \Predis\Client classes
        class: \Redis
        calls:
            - connect:
                - '%env(REDIS_HOST)%'
                - '%env(int:REDIS_PORT)%'

            # uncomment the following if your Redis server requires a password
            # - auth:
            #     - '%env(REDIS_PASSWORD)%'

            # uncomment the following if your Redis server requires a user and a password (when user is not default)
            # - auth:
            #     - ['%env(REDIS_USER)%','%env(REDIS_PASSWORD)%']
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

```
// config/services.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use Symfony\Component\HttpFoundation\Session\Storage\Handler\RedisSessionHandler;

return App::config([
    'services' => [
        // ...
        RedisSessionHandler::class => [
            'arguments' => [
                service('Redis'),
                // you can optionally pass an array of options. The only options are 'prefix' and 'ttl',
                // which define the prefix to use for the keys to avoid collision on the Redis server
                // and the expiration time for any given entry (in seconds), defaults are 'sf_s' and null:
                // ['prefix' => 'my_prefix', 'ttl' => 600],
            ],
        ],
        \Redis::class => [
            // you can also use \RedisArray, \RedisCluster, \Relay\Relay or \Predis\Client classes
            'class' => \Redis::class,
            'calls' => [
                'connect' => [env('REDIS_HOST'), env('REDIS_PORT')->int()],
                // uncomment the following if your Redis server requires a password:
                // 'auth' => [env('REDIS_PASSWORD')],
                // uncomment the following if your Redis server requires a user and a password (when user is not default):
                // 'auth' => [env('REDIS_USER'), env('REDIS_PASSWORD')],
            ],
        ],
    ],
]);
```

Next, use the [handler_id](https://symfony.com/doc/8.0/reference/configuration/framework.html#config-framework-session-handler-id) configuration option to tell Symfony to use this service as the session handler:

YAML PHP

1
2
3
4
5

```
# config/packages/framework.yaml
framework:
    # ...
    session:
        handler_id: Symfony\Component\HttpFoundation\Session\Storage\Handler\RedisSessionHandler
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

```
// config/packages/framework.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use Symfony\Component\HttpFoundation\Session\Storage\Handler\RedisSessionHandler;

return App::config([
    'framework' => [
        // ...
        'session' => [
            'handler_id' => RedisSessionHandler::class,
        ],
    ],
]);
```

Symfony will now use your Redis server to read and write the session data. The main drawback of this solution is that Redis does not perform session locking, so you can face _race conditions_ when accessing sessions. For example, you may see an _"Invalid CSRF token"_ error because two requests were made in parallel and only the first one stored the CSRF token in the session.

See also

If you use Memcached instead of Redis, follow a similar approach but replace `RedisSessionHandler` by [MemcachedSessionHandler](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/Session/Storage/Handler/MemcachedSessionHandler.php "Symfony\Component\HttpFoundation\Session\Storage\Handler\MemcachedSessionHandler").

Tip

When using Redis with a DSN in the [handler_id](https://symfony.com/doc/8.0/reference/configuration/framework.html#config-framework-session-handler-id) config option, you can add the `prefix` and `ttl` options as query string parameters in the DSN.

Tip

When using [Valkey](https://valkey.io/) servers, you can use the `valkey:` or `valkeys:` DSN schemes instead of `redis:` or `rediss:` in the session handler configuration.

### [Store Sessions in a Relational Database (MariaDB, MySQL, PostgreSQL)](https://symfony.com/doc/8.0/session.html#store-sessions-in-a-relational-database-mariadb-mysql-postgresql "Permalink to this headline")

Symfony includes a [PdoSessionHandler](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/Session/Storage/Handler/PdoSessionHandler.php "Symfony\Component\HttpFoundation\Session\Storage\Handler\PdoSessionHandler") to store sessions in relational databases like MariaDB, MySQL and PostgreSQL. To use it, first register a new handler service with your database credentials:

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
# config/services.yaml
services:
    # ...

    Symfony\Component\HttpFoundation\Session\Storage\Handler\PdoSessionHandler:
        arguments:
            - '%env(DATABASE_URL)%'

            # you can also use PDO configuration, but requires passing two arguments
            # - 'mysql:dbname=mydatabase; host=myhost; port=myport'
            # - { db_username: myuser, db_password: mypassword }
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
// config/services.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use Symfony\Component\HttpFoundation\Session\Storage\Handler\PdoSessionHandler;

return App::config([
    'services' => [
        // ...
        PdoSessionHandler::class => [
            'arguments' => [
                env('DATABASE_URL'),
                // you can also use PDO configuration, but requires passing two arguments
                // 'mysql:dbname=mydatabase; host=myhost; port=myport',
                // ['db_username' => 'myuser', 'db_password' => 'mypassword'],
            ],
        ],
    ],
]);
```

Tip

When using MySQL as the database, the DSN defined in `DATABASE_URL` can contain the `charset` and `unix_socket` options as query string parameters.

Next, use the [handler_id](https://symfony.com/doc/8.0/reference/configuration/framework.html#config-framework-session-handler-id) configuration option to tell Symfony to use this service as the session handler:

YAML PHP

1
2
3
4
5

```
# config/packages/framework.yaml
framework:
    session:
        # ...
        handler_id: Symfony\Component\HttpFoundation\Session\Storage\Handler\PdoSessionHandler
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

```
// config/packages/framework.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use Symfony\Component\HttpFoundation\Session\Storage\Handler\PdoSessionHandler;

return App::config([
    'framework' => [
    // ...
        'session' => [
            'handler_id' => PdoSessionHandler::class,
        ],
    ],
]);
```

#### [Configuring the Session Table and Column Names](https://symfony.com/doc/8.0/session.html#configuring-the-session-table-and-column-names "Permalink to this headline")

The table used to store sessions is called `sessions` by default and defines certain column names. You can configure these values with the second argument passed to the `PdoSessionHandler` service:

YAML PHP

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

    Symfony\Component\HttpFoundation\Session\Storage\Handler\PdoSessionHandler:
        arguments:
            - '%env(DATABASE_URL)%'
            - { db_table: 'customer_session', db_id_col: 'guid' }
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

```
// config/services.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use Symfony\Component\HttpFoundation\Session\Storage\Handler\PdoSessionHandler;

return App::config([
    'services' => [
        // ...
        PdoSessionHandler::class => [
            'arguments' => [
                env('DATABASE_URL'),
                ['db_table' => 'customer_session', 'db_id_col' => 'guid'],
            ],
        ],
    ],
]);
```

These are parameters that you can configure:

`db_table` (default `sessions`): The name of the session table in your database; `db_username`: (default: `''`) The username used to connect when using the PDO configuration (when using the connection based on the `DATABASE_URL` env var, it overrides the username defined in the env var). `db_password`: (default: `''`) The password used to connect when using the PDO configuration (when using the connection based on the `DATABASE_URL` env var, it overrides the password defined in the env var). `db_id_col` (default `sess_id`): The name of the column where to store the session ID (column type: `VARCHAR(128)`); `db_data_col` (default `sess_data`): The name of the column where to store the session data (column type: `BLOB`); `db_time_col` (default `sess_time`): The name of the column where to store the session creation timestamp (column type: `INTEGER`); `db_lifetime_col` (default `sess_lifetime`): The name of the column where to store the session lifetime (column type: `INTEGER`); `db_connection_options` (default: `[]`) An array of driver-specific connection options; `lock_mode` (default: `LOCK_TRANSACTIONAL`) The strategy for locking the database to avoid _race conditions_. Possible values are `LOCK_NONE` (no locking), `LOCK_ADVISORY` (application-level locking) and `LOCK_TRANSACTIONAL` (row-level locking).

#### [Preparing the Database to Store Sessions](https://symfony.com/doc/8.0/session.html#preparing-the-database-to-store-sessions "Permalink to this headline")

Before storing sessions in the database, you must create the table that stores the information.

With Doctrine installed, the session table will be automatically generated when you run the `make:migration` command if the database targeted by doctrine is identical to the one used by this component.

Or if you prefer to create the table yourself and the table has not already been created, the session handler provides a method called [createTable()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/Session/Storage/Handler/PdoSessionHandler.php#:~:text=function%20createTable "Symfony\Component\HttpFoundation\Session\Storage\Handler\PdoSessionHandler::createTable()") to set up this table for you according to the database engine used:

1
2
3
4
5

```
try {
    $sessionHandlerService->createTable();
} catch (\PDOException $exception) {
    // the table could not be created for some reason
}
```

If the table already exists an exception will be thrown.

If you would rather set up the table yourself, it's recommended to generate an empty database migration with the following command:

1`$ php bin/console doctrine:migrations:generate`

Then, find the appropriate SQL for your database below, add it to the migration file and run the migration with the following command:

1`$ php bin/console doctrine:migrations:migrate`

If needed, you can also add this table to your schema by calling [configureSchema()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/Session/Storage/Handler/PdoSessionHandler.php#:~:text=function%20configureSchema "Symfony\Component\HttpFoundation\Session\Storage\Handler\PdoSessionHandler::configureSchema()") method in your code.

##### [MariaDB/MySQL](https://symfony.com/doc/8.0/session.html#mariadb-mysql "Permalink to this headline")

1
2
3
4
5
6
7

```
CREATE TABLE `sessions` (
    `sess_id` VARBINARY(128) NOT NULL PRIMARY KEY,
    `sess_data` BLOB NOT NULL,
    `sess_lifetime` INTEGER UNSIGNED NOT NULL,
    `sess_time` INTEGER UNSIGNED NOT NULL,
    INDEX `sess_lifetime_idx` (`sess_lifetime`)
) COLLATE utf8mb4_bin, ENGINE = InnoDB;
```

Note

A `BLOB` column type (which is the one used by default by `createTable()`) stores up to 64 kb. If the user session data exceeds this, an exception may be thrown or their session will be silently reset. Consider using a `MEDIUMBLOB` if you need more space.

##### [PostgreSQL](https://symfony.com/doc/8.0/session.html#postgresql "Permalink to this headline")

1
2
3
4
5
6
7

```
CREATE TABLE sessions (
    sess_id VARCHAR(128) NOT NULL PRIMARY KEY,
    sess_data BYTEA NOT NULL,
    sess_lifetime INTEGER NOT NULL,
    sess_time INTEGER NOT NULL
);
CREATE INDEX sess_lifetime_idx ON sessions (sess_lifetime);
```

##### [Microsoft SQL Server](https://symfony.com/doc/8.0/session.html#microsoft-sql-server "Permalink to this headline")

1
2
3
4
5
6
7

```
CREATE TABLE sessions (
    sess_id VARCHAR(128) NOT NULL PRIMARY KEY,
    sess_data NVARCHAR(MAX) NOT NULL,
    sess_lifetime INTEGER NOT NULL,
    sess_time INTEGER NOT NULL,
    INDEX sess_lifetime_idx (sess_lifetime)
);
```

### [Store Sessions in a NoSQL Database (MongoDB)](https://symfony.com/doc/8.0/session.html#store-sessions-in-a-nosql-database-mongodb "Permalink to this headline")

Symfony includes a [MongoDbSessionHandler](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/Session/Storage/Handler/MongoDbSessionHandler.php "Symfony\Component\HttpFoundation\Session\Storage\Handler\MongoDbSessionHandler") to store sessions in the MongoDB NoSQL database. First, make sure to have a working MongoDB connection in your Symfony application as explained in the [DoctrineMongoDBBundle configuration](https://symfony.com/doc/master/bundles/DoctrineMongoDBBundle/config.html) article.

Then, register a new handler service for `MongoDbSessionHandler` and pass it the MongoDB connection as argument, and the required parameters:

`database`: The name of the database `collection`: The name of the collection

YAML PHP

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

    Symfony\Component\HttpFoundation\Session\Storage\Handler\MongoDbSessionHandler:
        arguments:
            - '@doctrine_mongodb.odm.default_connection'
            - { database: '%env(MONGODB_DB)%', collection: 'sessions' }
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

```
// config/services.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use Symfony\Component\HttpFoundation\Session\Storage\Handler\MongoDbSessionHandler;

return App::config([
    'services' => [
        // ...
        MongoDbSessionHandler::class => [
            'arguments' => [
                service('doctrine_mongodb.odm.default_connection'),
                ['database' => env('MONGODB_DB'), 'collection' => 'sessions'],
            ],
        ],
    ],
]);
```

Next, use the [handler_id](https://symfony.com/doc/8.0/reference/configuration/framework.html#config-framework-session-handler-id) configuration option to tell Symfony to use this service as the session handler:

YAML PHP

1
2
3
4
5

```
# config/packages/framework.yaml
framework:
    session:
        # ...
        handler_id: Symfony\Component\HttpFoundation\Session\Storage\Handler\MongoDbSessionHandler
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

```
// config/packages/framework.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use Symfony\Component\HttpFoundation\Session\Storage\Handler\MongoDbSessionHandler;

return App::config([
    'framework' => [
        // ...
        'session' => [
            'handler_id' => MongoDbSessionHandler::class,
        ],
    ],
]);
```

That's all! Symfony will now use your MongoDB server to read and write the session data. You do not need to do anything to initialize your session collection. However, you may want to add an index to improve garbage collection performance. Run this from the [MongoDB shell](https://docs.mongodb.com/manual/mongo/):

1
2

```
use session_db
db.session.createIndex( { "expires_at": 1 }, { expireAfterSeconds: 0 } )
```

#### [Configuring the Session Field Names](https://symfony.com/doc/8.0/session.html#configuring-the-session-field-names "Permalink to this headline")

The collection used to store sessions defines certain field names. You can configure these values with the second argument passed to the `MongoDbSessionHandler` service:

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
# config/services.yaml
services:
    # ...

    Symfony\Component\HttpFoundation\Session\Storage\Handler\MongoDbSessionHandler:
        arguments:
            - '@doctrine_mongodb.odm.default_connection'
            -
                database: '%env(MONGODB_DB)%'
                collection: 'sessions'
                id_field: '_guid'
                expiry_field: 'eol'
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

```
// config/services.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use Symfony\Component\HttpFoundation\Session\Storage\Handler\MongoDbSessionHandler;

return App::config([
    'services' => [
        // ...
        MongoDbSessionHandler::class => [
            'arguments' => [
                service('doctrine_mongodb.odm.default_connection'),
                [
                    'database' => env('MONGODB_DB'),
                    'collection' => 'sessions',
                    'id_field' => '_guid',
                    'expiry_field' => 'eol',
                ],
            ],
        ],
    ],
]);
```

These are parameters that you can configure:

`id_field` (default `_id`): The name of the field where to store the session ID; `data_field` (default `data`): The name of the field where to store the session data; `time_field` (default `time`): The name of the field where to store the session creation timestamp; `expiry_field` (default `expires_at`): The name of the field where to store the session lifetime.

### [Migrating Between Session Handlers](https://symfony.com/doc/8.0/session.html#migrating-between-session-handlers "Permalink to this headline")

If your application changes the way sessions are stored, use the [MigratingSessionHandler](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/Session/Storage/Handler/MigratingSessionHandler.php "Symfony\Component\HttpFoundation\Session\Storage\Handler\MigratingSessionHandler") to migrate between old and new save handlers without losing session data.

This is the recommended migration workflow:

1. Switch to the migrating handler, with your new handler as the write-only one. The old handler behaves as usual and sessions get written to the new one:

1`$sessionStorage = new MigratingSessionHandler($oldSessionStorage, $newSessionStorage);`  
2.   After your session gc period, verify that the data in the new handler is correct.
3.   Update the migrating handler to use the old handler as the write-only one, so the sessions will now be read from the new handler. This step allows easier rollbacks:

1`$sessionStorage = new MigratingSessionHandler($newSessionStorage, $oldSessionStorage);`  
4.   After verifying that the sessions in your application are working, switch from the migrating handler to the new handler.

### [Configuring the Session TTL](https://symfony.com/doc/8.0/session.html#configuring-the-session-ttl "Permalink to this headline")

Symfony by default will use PHP's ini setting `session.gc_maxlifetime` as session lifetime. When you store sessions in a database, you can also configure your own TTL in the framework configuration or even at runtime.

Note

Changing the ini setting is not possible once the session is started so if you want to use a different TTL depending on which user is logged in, you must do it at runtime using the callback method below.

#### [Configure the TTL](https://symfony.com/doc/8.0/session.html#configure-the-ttl "Permalink to this headline")

You need to pass the TTL in the options array of the session handler you are using:

YAML PHP

1
2
3
4
5
6
7

```
# config/services.yaml
services:
    # ...
    Symfony\Component\HttpFoundation\Session\Storage\Handler\RedisSessionHandler:
        arguments:
            - '@Redis'
            - { 'ttl': 600 }
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

```
// config/services.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use Symfony\Component\HttpFoundation\Session\Storage\Handler\RedisSessionHandler;

return App::config([
    'services' => [
        // ...
        RedisSessionHandler::class => [
            'arguments' => [
                service('Redis'),
                ['ttl' => 600],
            ],
        ],
    ],
]);
```

#### [Configure the TTL Dynamically at Runtime](https://symfony.com/doc/8.0/session.html#configure-the-ttl-dynamically-at-runtime "Permalink to this headline")

If you would like to have a different TTL for different users or sessions for whatever reason, this is also possible by passing a callback as the TTL value. The callback will be called right before the session is written and has to return an integer which will be used as TTL.

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

```
# config/services.yaml
services:
    # ...
    Symfony\Component\HttpFoundation\Session\Storage\Handler\RedisSessionHandler:
        arguments:
            - '@Redis'
            - { 'ttl': !closure '@my.ttl.handler' }

    my.ttl.handler:
        class: Some\InvokableClass # some class with an __invoke() method
        arguments:
            # Inject whatever dependencies you need to be able to resolve a TTL for the current session
            - '@security'
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

```
// config/services.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use App\Some\InvokableClass;
use Symfony\Component\HttpFoundation\Session\Storage\Handler\RedisSessionHandler;

return App::config([
    'services' => [
        // ...
        RedisSessionHandler::class => [
            'arguments' => [
                service('Redis'),
                ['ttl' => closure(service('my.ttl.handler'))],
            ],
        ],
        'my.ttl.handler' => [
            'class' => InvokableClass::class,
            // Inject whatever dependencies you need to be able to resolve a TTL for the current session
            'arguments' => [service('security')],
        ],
    ],
]);
```

[Making the Locale "Sticky" during a User's Session](https://symfony.com/doc/8.0/session.html#making-the-locale-sticky-during-a-user-s-session "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Symfony stores the locale setting in the Request, which means that this setting is not automatically saved ("sticky") across requests. But, you _can_ store the locale in the session, so that it's used on subsequent requests.

### [Creating a LocaleSubscriber](https://symfony.com/doc/8.0/session.html#creating-a-localesubscriber "Permalink to this headline")

Create a [new event subscriber](https://symfony.com/doc/8.0/event_dispatcher.html#events-subscriber). Typically, `_locale` is used as a routing parameter to signify the locale, though you can determine the correct locale however you want:

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
// src/EventSubscriber/LocaleSubscriber.php
namespace App\EventSubscriber;

use Symfony\Component\EventDispatcher\EventSubscriberInterface;
use Symfony\Component\HttpKernel\Event\RequestEvent;
use Symfony\Component\HttpKernel\KernelEvents;

class LocaleSubscriber implements EventSubscriberInterface
{
    public function __construct(
        private string $defaultLocale = 'en',
    ) {
    }

    public function onKernelRequest(RequestEvent $event): void
    {
        $request = $event->getRequest();
        if (!$request->hasPreviousSession()) {
            return;
        }

        // try to see if the locale has been set as a _locale routing parameter
        if ($locale = $request->attributes->get('_locale')) {
            $request->getSession()->set('_locale', $locale);
        } else {
            // if no explicit locale has been set on this request, use one from the session
            $request->setLocale($request->getSession()->get('_locale', $this->defaultLocale));
        }
    }

    public static function getSubscribedEvents(): array
    {
        return [
            // must be registered before (i.e. with a higher priority than) the default Locale listener
            KernelEvents::REQUEST => [['onKernelRequest', 20]],
        ];
    }
}
```

If you're using the [default services.yaml configuration](https://symfony.com/doc/8.0/service_container.html#service-container-services-load-example), you're done! Symfony will automatically know about the event subscriber and call the `onKernelRequest` method on each request.

To see it working, either set the `_locale` key on the session manually (e.g. via some "Change Locale" route & controller), or create a route with the [_locale default](https://symfony.com/doc/8.0/translation.html#translation-locale-url).

Explicitly Configure the Subscriber

You can also explicitly configure it, in order to pass in the [default_locale](https://symfony.com/doc/8.0/reference/configuration/framework.html#config-framework-default_locale):

YAML PHP

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

    App\EventSubscriber\LocaleSubscriber:
        arguments: ['%kernel.default_locale%']
        # uncomment the next line if you are not using autoconfigure
        # tags: [kernel.event_subscriber]
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
// config/services.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use App\EventSubscriber\LocaleSubscriber;

return App::config([
    'services' => [
        // ...
        LocaleSubscriber::class => [
            'arguments' => [param('kernel.default_locale')],
            // uncomment the next line if you are not using autoconfigure
            // 'tags' => ['kernel.event_subscriber'],
        ],
    ],
]);
```

Now celebrate by changing the user's locale and seeing that it's sticky throughout the request.

Remember, to get the user's locale, always use the [Request::getLocale](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/Request.php#:~:text=function%20getLocale "Symfony\Component\HttpFoundation\Request::getLocale()") method:

1
2
3
4
5
6
7

```
// from a controller...
use Symfony\Component\HttpFoundation\Request;

public function index(Request $request): void
{
    $locale = $request->getLocale();
}
```

### [Setting the Locale Based on the User's Preferences](https://symfony.com/doc/8.0/session.html#setting-the-locale-based-on-the-user-s-preferences "Permalink to this headline")

You might want to improve this technique even further and define the locale based on the user entity of the logged in user. However, since the `LocaleSubscriber` is called before the `FirewallListener`, which is responsible for handling authentication and setting the user token on the `TokenStorage`, you have no access to the user which is logged in.

Suppose you have a `locale` property on your `User` entity and want to use this as the locale for the given user. To accomplish this, you can hook into the login process and update the user's session with this locale value before they are redirected to their first page.

To do this, you need an event subscriber on the `LoginSuccessEvent::class` event:

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

```
// src/EventSubscriber/UserLocaleSubscriber.php
namespace App\EventSubscriber;

use Symfony\Component\EventDispatcher\EventSubscriberInterface;
use Symfony\Component\HttpFoundation\RequestStack;
use Symfony\Component\Security\Http\Event\LoginSuccessEvent;

/**
 * Stores the locale of the user in the session after the
 * login. This can be used by the LocaleSubscriber afterwards.
 */
class UserLocaleSubscriber implements EventSubscriberInterface
{
    public function __construct(
        private RequestStack $requestStack,
    ) {
    }

    public function onLoginSuccess(LoginSuccessEvent $event): void
    {
        $user = $event->getUser();

        if (null !== $user->getLocale()) {
            $this->requestStack->getSession()->set('_locale', $user->getLocale());
        }
    }

    public static function getSubscribedEvents(): array
    {
        return [
            LoginSuccessEvent::class => 'onLoginSuccess',
        ];
    }
}
```

Warning

In order to update the language immediately after a user has changed their language preferences, you also need to update the session when you change the `User` entity.

[Session Proxies](https://symfony.com/doc/8.0/session.html#session-proxies "Permalink to this headline")
--------------------------------------------------------------------------------------------------------

The session proxy mechanism has a variety of uses and this article demonstrates two common ones. Rather than using the regular session handler, you can create a custom save handler by defining a class that extends the [SessionHandlerProxy](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/Session/Storage/Proxy/SessionHandlerProxy.php "Symfony\Component\HttpFoundation\Session\Storage\Proxy\SessionHandlerProxy") class.

Then, define the class as a [service](https://symfony.com/doc/8.0/service_container.html#service-container-creating-service). If you're using the [default services.yaml configuration](https://symfony.com/doc/8.0/service_container.html#service-container-services-load-example), that happens automatically.

Finally, use the `framework.session.handler_id` configuration option to tell Symfony to use your session handler instead of the default one:

YAML PHP

1
2
3
4
5

```
# config/packages/framework.yaml
framework:
    session:
        # ...
        handler_id: App\Session\CustomSessionHandler
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

```
// config/packages/framework.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use App\Session\CustomSessionHandler;

return App::config([
    'framework' => [
    // ...
    'session' => [
            'handler_id' => CustomSessionHandler::class,
        ],
    ],
]);
```

Keep reading the next sections to learn how to use the session handlers in practice to solve two common use cases: encrypt session information and define read-only guest sessions.

### [Encryption of Session Data](https://symfony.com/doc/8.0/session.html#encryption-of-session-data "Permalink to this headline")

If you want to encrypt the session data, you can use the proxy to encrypt and decrypt the session as required. The following example uses the [php-encryption](https://github.com/defuse/php-encryption) library, but you can adapt it to any other library that you may be using:

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

```
// src/Session/EncryptedSessionProxy.php
namespace App\Session;

use Defuse\Crypto\Crypto;
use Defuse\Crypto\Key;
use Symfony\Component\HttpFoundation\Session\Storage\Proxy\SessionHandlerProxy;

class EncryptedSessionProxy extends SessionHandlerProxy
{
    public function __construct(
        private \SessionHandlerInterface $handler,
        private Key $key
    ) {
        parent::__construct($handler);
    }

    public function read($id): string
    {
        $data = parent::read($id);

        return Crypto::decrypt($data, $this->key);
    }

    public function write($id, $data): string
    {
        $data = Crypto::encrypt($data, $this->key);

        return parent::write($id, $data);
    }
}
```

Another possibility to encrypt session data is to decorate the `session.marshaller` service, which points out to [MarshallingSessionHandler](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/HttpFoundation/Session/Storage/Handler/MarshallingSessionHandler.php "Symfony\Component\HttpFoundation\Session\Storage\Handler\MarshallingSessionHandler"). You can decorate this handler with a marshaller that uses encryption, like the [SodiumMarshaller](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Cache/Marshaller/SodiumMarshaller.php "Symfony\Component\Cache\Marshaller\SodiumMarshaller").

First, you need to generate a secure key and add it to your [secret store](https://symfony.com/doc/8.0/configuration/secrets.html) as `SESSION_DECRYPTION_FILE`:

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

```
# config/services.yaml
services:

    # ...
    Symfony\Component\Cache\Marshaller\SodiumMarshaller:
        decorates: 'session.marshaller'
        arguments:
            - ['%env(file:resolve:SESSION_DECRYPTION_FILE)%']
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

```
// config/services.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use Symfony\Component\Cache\Marshaller\SodiumMarshaller;

return App::config([
    'services' => [
        // ...
        SodiumMarshaller::class => [
            'decorates' => 'session.marshaller',
            'arguments' => [
                [env('SESSION_DECRYPTION_FILE')->resolve()->file()],
                service('.inner'),
            ],
        ],
    ],
]);
```

Danger

This will encrypt the values of the cache items, but not the cache keys. Be careful not to leak sensitive data in the keys.

### [Read-only Guest Sessions](https://symfony.com/doc/8.0/session.html#read-only-guest-sessions "Permalink to this headline")

There are some applications where a session is required for guest users, but where there is no particular need to persist the session. In this case you can intercept the session before it is written:

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

```
// src/Session/ReadOnlySessionProxy.php
namespace App\Session;

use App\Entity\User;
use Symfony\Bundle\SecurityBundle\Security;
use Symfony\Component\HttpFoundation\Session\Storage\Proxy\SessionHandlerProxy;

class ReadOnlySessionProxy extends SessionHandlerProxy
{
    public function __construct(
        private \SessionHandlerInterface $handler,
        private Security $security
    ) {
        parent::__construct($handler);
    }

    public function write($id, $data): string
    {
        if ($this->getUser() && $this->getUser()->isGuest()) {
            return;
        }

        return parent::write($id, $data);
    }

    private function getUser(): ?User
    {
        $user = $this->security->getUser();
        if (is_object($user)) {
            return $user;
        }

        return null;
    }
}
```

[Integrating with Legacy Applications](https://symfony.com/doc/8.0/session.html#integrating-with-legacy-applications "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------

If you're integrating the Symfony full-stack Framework into a legacy application that starts the session with `session_start()`, you may still be able to use Symfony's session management by using the PHP Bridge session.

If the application has its own PHP save handler, you can specify `null` for the `handler_id`:

YAML PHP Standalone Use

1
2
3
4
5

```
# config/packages/framework.yaml
framework:
    session:
        storage_factory_id: session.storage.factory.php_bridge
        handler_id: ~
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
// config/packages/framework.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'framework' => [
        'session' => [
            'storage_factory_id' => 'session.storage.factory.php_bridge',
            'handler_id' => null,
        ],
    ],
]);
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

```
use Symfony\Component\HttpFoundation\Session\Session;
use Symfony\Component\HttpFoundation\Session\Storage\PhpBridgeSessionStorage;

// legacy application configures session
ini_set('session.save_handler', 'files');
ini_set('session.save_path', '/tmp');
session_start();

// Get Symfony to interface with this existing session
$session = new Session(new PhpBridgeSessionStorage());

// symfony will now interface with the existing PHP session
$session->start();
```

Otherwise, if the problem is that you cannot avoid the application starting the session with `session_start()`, you can still make use of a Symfony based session save handler by specifying the save handler as in the example below:

YAML PHP

1
2
3
4
5

```
# config/packages/framework.yaml
framework:
    session:
        storage_factory_id: session.storage.factory.php_bridge
        handler_id: session.handler.native_file
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
// config/packages/framework.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'framework' => [
        'session' => [
            'storage_factory_id' => 'session.storage.factory.php_bridge',
            'handler_id' => 'session.handler.native_file',
        ],
    ],
]);
```

Note

If the legacy application requires its own session save handler, do not override this. Instead set `handler_id: ~`. Note that a save handler cannot be changed once the session has been started. If the application starts the session before Symfony is initialized, the save handler will have already been set. In this case, you will need `handler_id: ~`. Only override the save handler if you are sure the legacy application can use the Symfony save handler without side effects and that the session has not been started before Symfony is initialized.

 This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.

 TOC

 Search

 Version

**Symfony 8.0**[backers](https://symfony.com/backers)

[](https://sulu.io/)

[](https://jb.gg/fbsk8y)

[![Image 1: Become certified from home](https://symfony.com/images/network/sy1certif_01.webp)](https://certification.symfony.com/exams/sylius.html?utm_source=ad&utm_medium=banner&utm_campaign=certification&utm_content=syliuscertifiedathome)
[Become certified from home](https://certification.symfony.com/exams/sylius.html?utm_source=ad&utm_medium=banner&utm_campaign=certification&utm_content=syliuscertifiedathome)

[![Image 2: Be trained by SensioLabs experts (2 to 6 day sessions -- French or English).](https://symfony.com/images/network/sltraining_01.webp)](https://sensiolabs.com/training/courses?utm_source=symfony&utm_medium=symfony_ads&utm_campaign=permanent_referral)
[Be trained by SensioLabs experts (2 to 6 day sessions -- French or English).](https://sensiolabs.com/training/courses?utm_source=symfony&utm_medium=symfony_ads&utm_campaign=permanent_referral)

Symfony footer
--------------

![Image 3: Avatar of Viacheslav Demianov, a Symfony contributor](https://connect.symfony.com/api/images/44c73465-3e1d-483b-9b99-36cbd1647845.png?format=48x48)

Thanks **[Viacheslav Demianov](https://connect.symfony.com/profile/sdem)** (**@sdem**) for being a Symfony contributor

[**2** commits](https://github.com/symfony/symfony/commits?author=demyanovs) • **3** lines changed

[View all contributors](https://symfony.com/contributors) that help us make Symfony

### Become a Symfony contributor

Be an active part of the community and contribute ideas, code and bug fixes. Both experts and newcomers are welcome.

[Learn how to contribute](https://symfony.com/doc/current/contributing/index.html)

![Image 4](https://symfony.com/assets/icons/logos/sf-20years-wordmark-dark--dFsFxh.webp)
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
