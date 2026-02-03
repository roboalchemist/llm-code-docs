# Source: https://resend.com/docs/send-with-php.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send emails with PHP

> Learn how to send your first email using the Resend PHP SDK.

export const YouTube = ({id}) => {
  return <iframe className="w-full aspect-video rounded-xl" src={`https://www.youtube.com/embed/${id}`} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>;
};

## Prerequisites

To get the most out of this guide, you will need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

Prefer watching a video? Check out this video walkthrough below.

<YouTube id="vJRJ7b4QJHw" />

## 1. Install

Get the Resend PHP SDK.

```bash Composer theme={"theme":{"light":"github-light","dark":"vesper"}}
composer require resend/resend-php
```

## 2. Send email using HTML

The easiest way to send an email is by using the `html` parameter.

```php index.php theme={"theme":{"light":"github-light","dark":"vesper"}}
<?php

require __DIR__ . '/vendor/autoload.php';

$resend = Resend::client('re_xxxxxxxxx');

$resend->emails->send([
  'from' => 'Acme <onboarding@resend.dev>',
  'to' => ['delivered@resend.dev'],
  'subject' => 'hello world',
  'html' => '<strong>it works!</strong>',
]);
```

## 3. Try it yourself

<Card title="PHP Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-php-example">
  See the full source code.
</Card>
