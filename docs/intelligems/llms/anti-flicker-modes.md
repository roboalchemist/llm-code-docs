# Source: https://docs.intelligems.io/performance-optimization/anti-flicker-modes.md

# Anti-Flicker Modes

Intelligems adds an anti-flicker functionality to reduce the performance impacts of our JavaScript by default. Therefore, please do not `async` or `defer` your Intelligems script; this is handled internally and will cause flashing on your site if added.

### Anti-flicker Modes

Intelligems offers two anti-flicker modes:

1. Element-specific anti-flicker (default). This will temporarily hide all price elements selected during your integration.
2. Page anti-flicker. This will temporarily hide all site content.

The best mode will likely depend on your individual site; try out both and see which works best. Add the below snippet **above** the Intelligems script tag to enable mode (2).

```html
<head>
  ...
    <script>
    window.igSettings = {
        hideBody: true
    }
    </script>

    // Script must below:
    <script src="https://cdn.intelligems.io/<your_customer_id>.js"></script>
  ...
</head>
```

## My Site is Still Flashing

The default configuration above works for most sites. However, if you are still experiencing flashing on your site, please [reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request). We have several internal tools we can use to help reduce flashing.
