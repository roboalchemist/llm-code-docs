# Source: https://picocss.com/docs

Title: Documentation • Pico CSS

URL Source: https://picocss.com/docs

Markdown Content:
There are 4 ways to get started with pico.css:

Install manually[#](https://picocss.com/docs#install-manually)
--------------------------------------------------------------

[Download Pico](https://github.com/picocss/pico/archive/refs/heads/main.zip)and link `/css/pico.min.css` in the `<head>`of your website.

[](https://picocss.com/docs)`<link rel="stylesheet" href="css/pico.min.css">`

Usage from CDN[#](https://picocss.com/docs#usage-from-cdn)
----------------------------------------------------------

Alternatively, you can use [jsDelivr CDN](https://cdn.jsdelivr.net/npm/@picocss/pico@2/) to link`pico.min.css`.

[](https://picocss.com/docs)
```
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"
>
```

Install with NPM[#](https://picocss.com/docs#install-with-npm)
--------------------------------------------------------------

[](https://picocss.com/docs)`npm install @picocss/pico`

Or

[](https://picocss.com/docs)`yarn add @picocss/pico`

Then, import Pico into your SCSS file with[@use](https://sass-lang.com/documentation/at-rules/use):

[](https://picocss.com/docs)`@use "pico";`

Learn more about the [customization with Sass](https://picocss.com/docs/sass).

Install with Composer[#](https://picocss.com/docs#install-with-composer)
------------------------------------------------------------------------

[](https://picocss.com/docs)`composer require picocss/pico`

Starter HTML template[#](https://picocss.com/docs#starter-html-template)
------------------------------------------------------------------------

[](https://picocss.com/docs)
```
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="color-scheme" content="light dark">
    <link rel="stylesheet" href="css/pico.min.css">
    <title>Hello world!</title>
  </head>
  <body>
    <main class="container">
      <h1>Hello world!</h1>
    </main>
  </body>
</html>
```

[Edit this page on GitHub](https://github.com/picocss/picocss.com/blob/main/app/routes/docs._index.jsx)
