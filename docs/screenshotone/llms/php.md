# Source: https://screenshotone.com/docs/code-examples/php/

# PHP SDK and Code Examples

import Alert from "@/components/Alert.astro";

<Alert>
    If you have any questions, please, reach out at `support@screenshotone.com`.
</Alert>

### Installation

Run the next command to install the PHP SDK to take screenshots:

```shell
composer require screenshotone/sdk:^1.0
```

### Usage

Don't forget to [sign up](https://dash.screenshotone.com/sign-up) to get access and secret keys.

Generate a screenshot URL without executing the request. Or download the screenshot. It is up to you:

```php
<?php

use ScreenshotOne\Sdk\Client;
use ScreenshotOne\Sdk\TakeOptions;

$client = new Client('<access key>', '<secret key>');

$options = TakeOptions::url("https://example.com")
    ->fullPage(true)
    ->delay(2)
    ->geolocationLatitude(48.857648)
    ->geolocationLongitude(2.294677)
    ->geolocationAccuracy(50);

$url = $client->generateTakeUrl($options);
echo $url.PHP_EOL;
// expected output: https://api.screenshotone.com/take?url=https%3A%2F%2Fexample.com...

$image = $client->take($options);
file_put_contents('example.png', $image);
// the screenshot is stored in the example.png file
```

Check out [other SDKs and code examples](/docs/code-examples/).