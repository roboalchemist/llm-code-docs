# Source: https://resend.com/docs/send-with-laravel-smtp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send emails using Laravel with SMTP

> Learn how to send your first email using Laravel with SMTP.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Setup your environment

First, configure your Resend SMTP details in your application's `.env` file:

```ini .env theme={"theme":{"light":"github-light","dark":"vesper"}}
MAIL_MAILER=smtp
MAIL_HOST=smtp.resend.com
MAIL_PORT=587
MAIL_USERNAME=resend
MAIL_PASSWORD=re_xxxxxxxxx
MAIL_ENCRYPTION=tls
MAIL_FROM_ADDRESS=onboarding@resend.dev
MAIL_FROM_NAME=Acme
```

## 2. Send an email

Now you're ready to send emails with Laravel's powerful email service. Here's an example of how you could send your first email using Resend SMTP:

```php OrderShipmentController.php theme={"theme":{"light":"github-light","dark":"vesper"}}
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

## 3. Try it yourself

<Card title="Laravel Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-laravel-example">
  See the full source code.
</Card>
