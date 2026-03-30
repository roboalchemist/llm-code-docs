# Source: https://screenshotone.com/docs/guides/how-to-customize-any-website-before-screenshotting/

# Customize websites before screenshotting

ScreenshotOne supports a few options that can help you add any customizations to any website before rendering screenshots of it.

## Hide any element by CSS selectors

If you just need to quickly hide a few elements on the website, just use [the hide_selectors](https://screenshotone.com/docs/options/#hide_selectors) option and specify as many CSS selectors as you wish.

For example, let's hide the main header on the example.com website with:

```
https://api.screenshotone.com/take?url=https://example.com&hide_selectors=h1&access_key=<your API key>
```

Before hiding:

![A customized version of the example.com website](with_header.png)

After hiding:

![A customized version of the example.com website](without_header.png)

You can specify as many selectors as you wish, e.g.:

```
https://api.screenshotone.com/take?url=https://example.com&hide_selectors[]=h1&hide_selectors[]=p&access_key=<your API key>
```

## Add custom CSS styles

But often you want to do more than just hide a few elements. Maybe you want to change some colors of the elements, or font size, or whatever. Then you can simply add custom CSS styles with [the styles option](https://screenshotone.com/docs/options/#styles).

Don't forget to encode the code. And often, you must add a `!important` attribute to every property you use.

Let's try it with the example.com website:

```
https://api.screenshotone.com/take?url=https://example.com&styles=h1%20%7Bcolor%3A%20red%20%21important%3B%7D&access_key=<your API key>
```

Notice, that the styles parameter is URL-encoded. Let's look at the result:

![A customized version of the example.com website](example_com_with_styles.webp)

## Execute custom JavaScript code

But what if hiding elements and adding styles is not enough? We got you covered! You can any custom JavaScript code you want.

You can check out a more complex example of using scripting for integrating [Google Translate API when screenshotting websites](/docs/guides/how-to-translate-and-render-a-website-as-a-screenshot/).

:::caution
If your script causes navigation and makes the page reload, make sure to specify [the scripts_wait_until option](/docs/options/#scripts_wait_until) if you want to wait or large enough [delay](/docs/options/#delay).
:::

Let's execute an extreme example and just override the page content with:

```javascript
scripts = document.body.innerHTML = "Hello, world!";
```

The URL would look like:

```
https://api.screenshotone.com/take?scripts=document.body.innerHTML="Hello,%20world!"&url=https://example.com/&access_key=<your access key>
```

And the result is:

![A customized version of the example.com website](hello_world_example.webp)

## Click

If you use scripting to only click on some element by selector, there is a popular shortcut for that [the click option](/docs/options/#click).

```
https://api.screenshotone.com/take?click=.a-some-button-class-selector&url=https://example.com&access_key=<your access key>
```

Just specify any selector of any element and it will be clicked.