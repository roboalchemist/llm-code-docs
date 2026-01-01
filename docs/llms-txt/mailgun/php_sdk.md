# Source: https://documentation.mailgun.com/docs/mailgun/sdk/php_sdk.md

# PHP

a
img

    Official Mailgun PHP SDK

### Installation

**Required minimum php version**

- minimum php version 7.3


To install the SDK, you will need to be using [Composer](http://getcomposer.org/)
in your project.
If you aren't using Composer yet, it's really simple! Here's how to install
composer:


```bash
curl -sS https://getcomposer.org/installer | php
```

The Mailgun API Client is not hard coupled to Guzzle, Buzz or any other library that sends
HTTP messages. Instead, it uses the [PSR-18](https://www.php-fig.org/psr/psr-18/) client abstraction.
This will give you the flexibility to choose what
[PSR-7 implementation](https://packagist.org/providers/psr/http-factory-implementation)
and [HTTP client](https://packagist.org/providers/psr/http-client-implementation)
you want to use.

If you want to get started quickly use PHP's package manager, [Composer](https://getcomposer.org/doc/00-intro.md) to get the SDK pulled into your project.

If you have Composer installed globally run:


```bash
composer require mailgun/mailgun-php symfony/http-client nyholm/psr7
```

If Composer is not installed globally or if you are using a local version of Composer


```bash
php composer.phar require mailgun/mailgun-php symfony/http-client nyholm/psr7
```

### Usage

Here's a simple example on how to send an email. As always, please consult the repository readme for full details.

You should always use Composer autoloader in your application to automatically load
your dependencies. All the examples below assume you've already included this in your
file:


```php
require 'vendor/autoload.php';
use Mailgun\Mailgun;
```

Here's how to send a message using the SDK:


```php
// First, instantiate the SDK with your API credentials
$mg = Mailgun::create('key-example'); // For US servers
$mg = Mailgun::create('key-example', 'https://api.eu.mailgun.net'); // For EU servers

// Now, compose and send your message.
// $mg->messages()->send($domain, $params);
$mg->messages()->send('example.com', [
  'from'    => 'bob@example.com',
  'to'      => 'sally@example.com',
  'subject' => 'The PHP SDK is awesome!',
  'text'    => 'It is so simple to send a message.'
]);
```