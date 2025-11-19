# Source: https://loops.so/docs/guides/email-dark-mode.md

# Dark mode support in emails

> Understanding dark mode support in email clients and best practices for consistent rendering.

It can be difficult to ensure consistent email rendering in both light and dark modes across different email clients. Dark mode is now a default setting for many email clients (on both desktop and mobile devices) and it's important to ensure your emails look good in both modes.

Email clients handle dark mode quite differently, making it challenging to maintain consistent branding and design. Some clients automatically invert colors, while others respect dark mode preferences through CSS media queries.

This guide explores the current state of dark mode support and provides practical solutions for maintaining brand consistency.

<Tip>
  While we don't currently support a dark mode version when creating emails in our editor, we automatically enable dark mode support in email clients that can handle it. Note that this doesn't include image handling, as dark mode support for images varies significantly across different email clients.
</Tip>

## Best practices

Ultimately, after experimenting with a number of techniques, the following combination of techniques can enhance consistency across clients while respecting dark mode preferences:

1. **Logo color**: use either grey or a colorful brand color that works on both light/dark backgrounds
2. **Image stroke**: apply a stroke to the logo that matches the light-mode email background
3. **Dark mode optimization**: Progressively enhance clients that support `prefers-color-scheme` with a specific dark mode logo

### Logo color

When designing logos for emails, try to use a color that works well in both light and dark modes. Consider using grey or brand colors that maintain visibility in dark mode.

Try to avoid dark or black logos that might disappear in dark mode. Make sure to test your emails in dark mode in different email clients to ensure the logo is visible.

<Frame caption="Use grey and colors to make your logo visible in both light and dark modes">
    <img src="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/dark-mode-logo.png?fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=cfc45606b8376c04691fa3edeeb1415a" alt="Use grey or colored logos" data-og-width="2280" width="2280" data-og-height="1137" height="1137" data-path="images/dark-mode-logo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/dark-mode-logo.png?w=280&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=0fe1773d5af967e33f91a68c53eedc21 280w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/dark-mode-logo.png?w=560&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=ce9d1190bef58f285d40a5d21fb5755b 560w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/dark-mode-logo.png?w=840&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=f2d1c6ab62f779e8a7c27095b9202963 840w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/dark-mode-logo.png?w=1100&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=b69f27a256aee90c17584509ea5e462e 1100w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/dark-mode-logo.png?w=1650&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=4d2d0c6cd39383f6707e6d134da146a0 1650w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/dark-mode-logo.png?w=2500&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=dd1bb4f4fb53f09764b950c86f043b3c 2500w" />
</Frame>

Some email clients (like Gmail on Android 14) automatically invert small images under \~50px if they detect poor contrast in dark mode. This behavior varies across clients and versions, so it's crucial to test your specific logo in different clients.

### Image stroke

For logos that need to maintain their original colors, consider adding a stroke in the colour of your light mode background. This stays invisible in light mode, but becomes visible in dark mode and highlights the logo.

Using thicker strokes usually improves visibility when scaled down. And ideally the change is made to the image itself rather than using a CSS filter.

Limitations to this technique:

* May not meet your brand or design guidelines
* You may need to make kerning or spacing changes for optimal appearance
* Stroke thickness might be limited by your logo's design
* Image scaling can affect stroke appearance and visibility

<Frame caption="A stroke or outline will make a dark logo visible in dark mode but may not suit your design or brand guidelines">
    <img src="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/dark-mode-stroke.png?fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=4bfaa67b8b0a7cec249f8f6a33172430" alt="Stroked logo" data-og-width="2280" width="2280" data-og-height="726" height="726" data-path="images/dark-mode-stroke.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/dark-mode-stroke.png?w=280&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=77755c12bb8aa88a4f1902a9385c1286 280w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/dark-mode-stroke.png?w=560&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=e7d402d9a48ad76fc13280b32e4d7b40 560w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/dark-mode-stroke.png?w=840&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=207760b43ddac66f10fc049627199e37 840w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/dark-mode-stroke.png?w=1100&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=e75867e22ef86dfd6cc04c6fbd5d718d 1100w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/dark-mode-stroke.png?w=1650&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=1de308b2a376a80baa9a63ba255ec1ba 1650w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/dark-mode-stroke.png?w=2500&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=5dd5357f815ee95fc74c13a8e5a1d7c1 2500w" />
</Frame>

### CSS

While [support](https://www.caniemail.com/features/css-at-media-prefers-color-scheme/) for the `prefers-color-scheme` media query is limited—with Gmail being the main barrier for mass adoption—you can still optimize for dark mode.

<Warning>
  Loops does not currently support custom CSS in our editor. You can still use this technique by adding the CSS to [imported MJML templates](/creating-emails/uploading-custom-email).
</Warning>

With this technique you can use different image assets for dark mode in supported clients and have more control over text colors.

Apple Mail has the best dark mode support so it makes sense to test there first. Just make sure to also view your emails in Gmail and Outlook to ensure the dark mode is working as expected.

Here's a very basic example of how to use this technique:

```html  theme={"dark"}
<style>
body {
  color: #000;
  background-color: #fff;
}
.light-logo {
  display: block;
}
.dark-logo {
  display: none;
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  body {
    color: #fff;
    background-color: #000;
  }
  .light-logo {
    display: none;
  }
  .dark-logo {
    display: block;
  }
}
</style>

<img src="https://example.com/logo-light.png" alt="Logo" class="light-logo">
<img src="https://example.com/logo-dark.png" alt="Logo" class="dark-logo">
```

## Read more

<CardGroup>
  <Card title="Improve your inbox placement" icon="inbox" href="/deliverability/improving-inbox-placement" />

  <Card title="Understanding email open rates" icon="envelope-open-text" href="/deliverability/understanding-email-open-rates" />

  <Card title="Delivery optimization" icon="chart-line" href="/deliverability/optimization" />
</CardGroup>
