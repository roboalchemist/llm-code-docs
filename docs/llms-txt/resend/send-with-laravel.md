# Source: https://resend.com/docs/send-with-laravel.md

# Send emails with Laravel

> Learn how to send your first email using Laravel.

export const YouTube = ({id}) => {
  return <iframe className="w-full aspect-video rounded-xl" src={`https://www.youtube.com/embed/${id}`} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>;
};

## Prerequisites

To get the most out of this guide, you will need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

Prefer watching a video? Check out this video walkthrough below.

<YouTube id="xUTeIIt982w" />

## 1. Install

First, install Resend for Laravel using the Composer package manager:

```bash Composer theme={null}
composer require resend/resend-laravel
```

## 2. Configuration

### API key

Next, you should configure your Resend API key in your application's `.env` file:

```ini .env theme={null}
RESEND_API_KEY=re_xxxxxxxxx
```

### Mail driver

To use Resend as your mail driver, first create a new mailer definition, in the `mailers` array within your application's `config/mail.php` configuration file:

```php mail.php theme={null}
'resend' => [
    'transport' => 'resend',
],
```

Next, update your application's `.env` file to use the Resend mail driver:

```ini .env theme={null}
MAIL_MAILER=resend
MAIL_FROM_ADDRESS=onboarding@resend.dev
MAIL_FROM_NAME=Acme
```

## 3. Send an email

Resend for Laravel provides two convenient ways to send emails, using Laravel's email service or the `Resend` API facade.

### Using the Mail Facade

```php OrderShipmentController.php theme={null}
<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use App\Mail\OrderShipped;
use App\Models\Order;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Mail;

class OrderShipmentController extends Controller
{
    /**
     * Ship the given order.
     */
    public function store(Request $request): RedirectResponse
    {
        $order = Order::findOrFail($request->order_id);

        // Ship the order...

        Mail::to($request->user())->send(new OrderShipped($order));

        return redirect('/orders');
    }
}
```

### Using the Resend Facade

```php OrderShipmentController.php theme={null}
<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use App\Mail\OrderShipped;
use App\Models\Order;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Resend\Laravel\Facades\Resend;

class OrderShipmentController extends Controller
{
    /**
     * Ship the given order.
     */
    public function store(Request $request): RedirectResponse
    {
        $order = Order::findOrFail($request->order_id);

        // Ship the order...

        Resend::emails()->send([
            'from' => 'Acme <onboarding@resend.dev>',
            'to' => [$request->user()->email],
            'subject' => 'hello world',
            'html' => (new OrderShipped($order))->render(),
        ])

        return redirect('/orders');
    }
}
```

## 4. Receiving webhook requests

By default, Resend for Laravel includes a webhook controller to respond to the `/resend/webhook` URL path. The controller will dispatch a Laravel event that corresponds to a Resend event. For example, an `email.delivered` event type will send an `EmailDelivered` Laravel event.

### Register the webhook endpoint

Register your publicly accessible HTTPS URL in the Resend dashboard.

<Tip>
  For develoment, you can create a tunnel to your localhost server using a tool like
  [ngrok](https://ngrok.com/download) or [VS Code Port Forwarding](https://code.visualstudio.com/docs/debugtest/port-forwarding). These tools serve your local dev environment at a public URL you can use to test your local webhook endpoint.

  Example: `https://example123.ngrok.io/api/webhook`
</Tip>

<img alt="Add Webhook" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/laravel-create-webhook.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=f551f634ded549840bc894726ca3483b" data-og-width="1280" width="1280" data-og-height="800" height="800" data-path="images/laravel-create-webhook.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/laravel-create-webhook.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=360f7e12e311bd1f1b7747e656c1ce17 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/laravel-create-webhook.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=e221eecabbcc0ccd2494207863146cea 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/laravel-create-webhook.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=9d867a496fa10b89be8484d93a5bf3a6 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/laravel-create-webhook.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=c72a9f30742ce39b7f452d5b4b8a1f27 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/laravel-create-webhook.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=52f996384831162a7d3346adb58bd064 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/laravel-create-webhook.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=749ebd5c46b77a32cfce9a66cdd805f0 2500w" />

### CSRF protection

Webhook requests from Resend need to bypass Laravel's CSRF protection. Be sure to list the URI as an exception in your application's `App\Http\Middleware\VerifyCsrfToken` middleware or list the route outside of the web middleware group:

```php  theme={null}
protected $except = [
    'resend/*',
];
```

### Verifying webhook signatures

To enable webhook verification, ensure that the `RESEND_WEBHOOK_SECRET` environment variable is set in your application's `.env` file. The **Signing secret** can be retrieved from your [Resend dashboard](https://resend.com/webhooks).

## 5. Try it yourself

<Card title="Laravel Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-laravel-example">
  See the full source code.
</Card>
