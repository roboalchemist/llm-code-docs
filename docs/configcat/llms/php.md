# Source: https://configcat.com/docs/sdk-reference/php.md

# Source: https://configcat.com/docs/sdk-reference/openfeature/php.md

# OpenFeature Provider for PHP

Copy page

[![Build Status](https://github.com/configcat/openfeature-php/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/configcat/openfeature-php/actions/workflows/ci.yml) [![Latest Stable Version](https://poser.pugx.org/configcat/openfeature-provider/version)](https://packagist.org/packages/configcat/openfeature-provider) [![Total Downloads](https://poser.pugx.org/configcat/openfeature-provider/downloads)](https://packagist.org/packages/configcat/openfeature-provider)

[ConfigCat OpenFeature Provider for PHP on GitHub](https://github.com/configcat/openfeature-php)

## Requirements[​](#requirements "Direct link to Requirements")

* PHP >= 8.1

## Getting started[​](#getting-started "Direct link to Getting started")

### 1. Install the provider with [Composer](https://getcomposer.org/)[​](#1-install-the-provider-with-composer "Direct link to 1-install-the-provider-with-composer")

```bash
composer require configcat/openfeature-provider

```

### 2. Initialize the provider[​](#2-initialize-the-provider "Direct link to 2. Initialize the provider")

The `ConfigCatProvider` constructor takes the SDK key and an optional `array` argument containing the additional configuration options for the [ConfigCat PHP SDK](https://configcat.com/docs/sdk-reference/php.md#creating-the-configcat-client):

```php
use ConfigCat\ClientOptions;
use ConfigCat\Log\LogLevel;
use ConfigCat\OpenFeature\ConfigCatProvider;
use OpenFeature\implementation\flags\Attributes;
use OpenFeature\implementation\flags\EvaluationContext;
use OpenFeature\OpenFeatureAPI;

// Acquire an OpenFeature API instance.
$api = OpenFeatureAPI::getInstance();

// Build options for the ConfigCat SDK.
$options = [
  ClientOptions::LOG_LEVEL => LogLevel::WARNING,
  ClientOptions::CACHE_REFRESH_INTERVAL => 5,
  //...
];

// Configure the provider.
$api->setProvider(new ConfigCatProvider('#YOUR-SDK-KEY#', $options));

// Create a client.
$client = $api->getClient();

```

For more information about all the configuration options, see the [PHP SDK documentation](https://configcat.com/docs/sdk-reference/php.md#creating-the-configcat-client).

### 3. Evaluate your feature flag[​](#3-evaluate-your-feature-flag "Direct link to 3. Evaluate your feature flag")

```php
$isAwesomeFeatureEnabled = $client->getBooleanValue('isAwesomeFeatureEnabled', false);
if (is_bool($isAwesomeFeatureEnabled) && $isAwesomeFeatureEnabled) {
    doTheNewThing();
} else {
    doTheOldThing();
}

```

## Evaluation Context[​](#evaluation-context "Direct link to Evaluation Context")

An [evaluation context](https://openfeature.dev/docs/reference/concepts/evaluation-context) in the OpenFeature specification is a container for arbitrary contextual data that can be used as a basis for feature flag evaluation. The ConfigCat provider translates these evaluation contexts to ConfigCat [User Objects](https://configcat.com/docs/sdk-reference/php.md#user-object).

The following table shows how the different context attributes are mapped to User Object attributes.

| Evaluation context | User Object  | Required |
| ------------------ | ------------ | -------- |
| `targetingKey`     | `identifier` | ☑        |
| `Email`            | `email`      |          |
| `Country`          | `country`    |          |
| Any other          | `custom`     |          |

To evaluate feature flags for a context, use the [OpenFeature Evaluation API](https://openfeature.dev/docs/reference/concepts/evaluation-api/):

```php
$context = new EvaluationContext('#SOME-USER-ID#', new Attributes([
    'Email' => 'configcat@example.com',
    'Country' => 'CountryID',
    'Rating' => 4.5,
    'RegisteredAt' => new DateTimeImmutable('2023-11-22T12:34:56.0000000Z'),
    'Roles' => ['Role1', 'Role2']
]));

$isAwesomeFeatureEnabled = $client->getBooleanValue('isAwesomeFeatureEnabled', false, $context);

```

## Look under the hood[​](#look-under-the-hood "Direct link to Look under the hood")

* [Sample PHP App](https://github.com/configcat/openfeature-php/tree/main/samples/ConfigCatProvider)
* [ConfigCat OpenFeature Provider's repository on GitHub](https://github.com/configcat/php-openfeature)
* [ConfigCat OpenFeature Provider on packagist.org](https://packagist.org/packages/configcat/openfeature-provider)
