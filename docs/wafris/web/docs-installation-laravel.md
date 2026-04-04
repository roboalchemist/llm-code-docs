# Source: https://wafris.org/docs/installation/laravel/

Title: Laravel

URL Source: https://wafris.org/docs/installation/laravel/

Markdown Content:
[](https://wafris.org/docs/installation/laravel/#wafris-for-laravel) Wafris for Laravel
---------------------------------------------------------------------------------------

[](https://wafris.org/docs/installation/laravel/#installation) Installation
---------------------------------------------------------------------------

### [](https://wafris.org/docs/installation/laravel/#1-connect-on-wafris-hub) 1. Connect on Wafris Hub

Go to [https://wafris.org/hub](https://wafris.org/hub) to create a new account and follow the instructions to link your Redis instance.

**Note:** In Step 3, you’ll use this same Redis URL in your app configuration.

### [](https://wafris.org/docs/installation/laravel/#2-install-this-library-via-composer) 2. Install this library via Composer

```
composer require wafris/laravel-wafris
```

### [](https://wafris.org/docs/installation/laravel/#3-publish-and-configure-wafris) 3. Publish and configure Wafris

You can publish the config file with:

```
php artisan vendor:publish --tag="wafris-config"
```

We recommend creating a separate Redis configuration for Wafris. That can be done in `config/database.php` with a new entry like this:

```
'redis' => [

    'client' => env('REDIS_CLIENT', 'predis'), // Make sure to set your Redis client to predis

    'options' => [
        ...
    ],

    'default' => [
        ...
    ],

    'cache' => [
        ...
    ],

    'wafris' => [
        'url' => env('REDIS_URL'),
        'host' => env('REDIS_HOST', '127.0.0.1'),
        'username' => env('REDIS_USERNAME'),
        'password' => env('REDIS_PASSWORD'),
        'port' => env('REDIS_PORT', '6379'),
        'database' => env('REDIS_CACHE_DB', '3'),
        'read_write_timeout' => 1, // Timeout in seconds
    ],

],
```

[](https://wafris.org/docs/installation/laravel/#usage) Usage
-------------------------------------------------------------

Add the `Wafris\AllowRequestMiddleware` middleware to routes that you want to have protected by Wafris.

### [](https://wafris.org/docs/installation/laravel/#protecting-all-routes) Protecting all routes

To protect all routes in your Laravel application, add the `Wafris\AllowRequestMiddleware` globally.

#### [](https://wafris.org/docs/installation/laravel/#laravel-11) Laravel 11

[Starting in Laravel 11](https://laravel.com/docs/11.x/middleware#global-middleware), middleware are registered in `bootstrap/app.php`. Add the following line in the `withMiddleware` section of that file:

```
Application::configure(basePath: dirname(__DIR__))
    // ...
    ->withMiddleware(function (Middleware $middleware) {
        // ... other middleware
        $middleware->append(\Wafris\AllowRequestMiddleware::class);
    });
```

### [](https://wafris.org/docs/installation/laravel/#laravel-10) Laravel 10

To protect all routes in your Laravel application, add `Wafris\AllowRequestMiddleware` to the `$middleware` property of your `app/Http/Kernel.php` class.

```
// app/Http/Kernel.php

/**
 * The application's global HTTP middleware stack.
 *
 * These middleware are run during every request to your application.
 *
 * @var array<int, class-string|string>
 */
protected $middleware = [
    // \App\Http\Middleware\TrustHosts::class,
    \App\Http\Middleware\TrustProxies::class,
    \Illuminate\Http\Middleware\HandleCors::class,
    \App\Http\Middleware\PreventRequestsDuringMaintenance::class,
    \Illuminate\Foundation\Http\Middleware\ValidatePostSize::class,
    \App\Http\Middleware\TrimStrings::class,
    \Illuminate\Foundation\Http\Middleware\ConvertEmptyStringsToNull::class,
    \Wafris\AllowRequestMiddleware::class,
];
```

### [](https://wafris.org/docs/installation/laravel/#protecting-specific-middleware-groups) Protecting specific middleware groups

To protect specific middleware groups, such as the `web` or `api` groups, add `Wafris\AllowRequestMiddleware` to each desired middleware group in your `app/Http/Kernel.php` class.

```
// app/Http/Kernel.php

/**
 * The application's route middleware groups.
 *
 * @var array<string, array<int, class-string|string>>
 */
protected $middlewareGroups = [
    'web' => [
        \App\Http\Middleware\EncryptCookies::class,
        \Illuminate\Cookie\Middleware\AddQueuedCookiesToResponse::class,
        \Illuminate\Session\Middleware\StartSession::class,
        \Illuminate\View\Middleware\ShareErrorsFromSession::class,
        \App\Http\Middleware\VerifyCsrfToken::class,
        \Illuminate\Routing\Middleware\SubstituteBindings::class,
        \Wafris\AllowRequestMiddleware::class,
    ],

    'api' => [
        // \Laravel\Sanctum\Http\Middleware\EnsureFrontendRequestsAreStateful::class,
        \Illuminate\Routing\Middleware\ThrottleRequests::class.':api',
        \Illuminate\Routing\Middleware\SubstituteBindings::class,
        \Wafris\AllowRequestMiddleware::class,
    ],
];
```

### [](https://wafris.org/docs/installation/laravel/#protecting-individual-routes) Protecting individual routes

Use the `Wafris\AllowRequestMiddleware` middleware when defining your route.

```
// routes/web.php

Route::get('/signup', function () {
    // ...
})->middleware(\Wafris\AllowRequestMiddleware::class);
```

* * *
