# Source: https://screenshotone.com/docs/guides/full-page-screenshots/

# Full-page screenshots

By default, the only thing you need to do is to set the `full_page` parameter to `true`:

```
https://api.screenshotone.com/take?url=https://example.com&full_page=true&access_key=...
```

The API tuned to balance performance and quality for the full-page screenshots. However, if you need to improve the quality of rendering, for the full-page screenshots, there is a few things you can do:

1. [Understand how viewport dimensions affect full-page screenshots.](#viewport-dimensions)
2. [Try different rendering algorithms.](#different-rendering-algorithms)
3. [Tune scrolling of the page.](#tune-scrolling)
4. [Reduce animations.](#reduce-animations)
5. [Wait more.](#wait-more)

However, improving the quality of rendering might lead to a performance degradation.

## Viewport dimensions

The `viewport_width` and `viewport_height` options play an important role in full-page screenshots:

### Viewport width and height 

The `viewport_width` option directly determines the **width of your final full-page screenshot** because:

- **Responsive design**: Different viewport widths trigger different layouts and CSS breakpoints. A mobile viewport (e.g., 375px) will render a mobile layout, while a desktop viewport (e.g., 1920px) will render a desktop layout.
- **Content visibility**: Wider viewports may show navigation menus, sidebars, or multi-column layouts that are hidden or stacked differently on narrower viewports.

By default, the viewport width is `1280` pixels.

The `viewport_height` option affects full-page screenshots differently depending on the algorithm used:

**For the default algorithm:**
- The viewport height is temporarily stretched to match the full page height during rendering.
- Your specified `viewport_height` is less relevant as it gets overridden.

**For the "by_sections" algorithm:**
- The `viewport_height` determines the **size of each section** that is captured.
- The API scrolls by the viewport height, captures a screenshot, then scrolls again.
- This affects lazy-loaded content: elements that load when they enter the viewport are triggered as the page scrolls through each section.
- Smaller viewport heights mean more sections and more scroll events, which can trigger more lazy-loaded content but takes longer.

By default, the viewport height is `1024` pixels.

### Capturing beyond viewport

The `capture_beyond_viewport` option works together with viewport dimensions to control how content is captured:

**Default behavior (`capture_beyond_viewport=true`):**

- The browser can capture content that extends beyond your `viewport_width` and `viewport_height`.
- This is the default for full-page screenshots and is essential for capturing the entire page height.
- The viewport dimensions still control the initial page layout and width of the screenshot.

**When set to `false`:**
```
capture_beyond_viewport=false
```
- Content is clipped to the exact viewport dimensions.
- For full-page screenshots, this usually produces undesired results as it clips the page.
- Only useful in specific cases where you want to limit the capture area strictly to the viewport.

**Important note for "by_sections" algorithm:**
- When using `full_page_algorithm=by_sections`, the `capture_beyond_viewport` option is automatically set to `false` internally.
- This is because the algorithm captures each section within the viewport and stitches them together.
- You don't need to worry about this option when using the "by_sections" algorithm.

## Different rendering algorithms

By default, the API uses the `full_page` uses a simple algorithm to screenshot the full page—it asks the browser to render it and usually that means that the browser just stretches the viewport to render the full-page screenshot. It rarely but leads to rendering issues.

You can try to use a different algorithm instead—by_sections:

```
full_page_algorithm=by_sections
```

It might be better in most cases. Since it will try to scroll the page and render it section by section, and then stitch all the sections into one image.

But while scrolling the page, not every element might triggered due the speed of the scrolling and the delay between the scrolls. Try to tune scrolling.

## Tune scrolling

Try to decrease or increase the size of the scroll step:  

```
full_page_scroll_by=500
```

And increase the delay between the scrolls, it might help to render the page correctly

```
full_page_scroll_delay=1500
```

It might help to render the page better and trigger more lazy-loaded elements.

## Reduce animations

Request websites to reduce the number of animations by adding the `reduced_motion` parameter: 

```
reduced_motion=true
```

## Wait more

Add from 5 to 10 seconds to wait for the page to load:

```
delay=5
```

## Block ads, trackers, banners and other elements

Request the API to block ads, trackers, banners and other elements by use the following parameters: 

```
block_ads=true&block_trackers=true&block_cookie_banners=true&block_chats=true&block_banners_by_heuristics=true
```

## Summary 

Combining all the tips above, you might try to get the best results with something like that: 

```
https://api.screenshotone.com/take?access_key=...&url=https://example.com&full_page=true&full_page_algorithm=by_sections&full_page_scroll_by=500&full_page_scroll_delay=1500&reduced_motion=true&delay=5&block_ads=true&block_trackers=true&block_cookie_banners=true&block_chats=true&block_banners_by_heuristics=true
```

## Support 

Rendering full-page screenshots reliably is a real challenge. And even after a lot of tuning, it might not work for all the pages.

If you have any questions or suggestions, please contact us at [support@screenshotone.com](mailto:support@screenshotone.com).