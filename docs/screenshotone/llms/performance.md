# Source: https://screenshotone.com/docs/guides/performance/

# Rendering performance

> "You are never done working on performance."
>
> Guillermo Rauch

ScreenshotOne's API is optimized for performance on permanent basis. However, due to a huge set of parameters that can be used to customize the rendering, there are some use cases where the default performance is not optimal.

The goal of this guide is to help you to tune the rendering parameters for your specific use case.

Of course, if you have any questions or need more help or assistance in performance tuning, please, reach out at `support@screenshotone.com`.

## Disable blocking ads and banners

Blocking ads, banners and other content seriously affects the performance of rendering since the API starts to listen for all the requests, waiting for elements to be shown, and many more tricks and heuristics are used to hide this type of content from the rendering.

In case if you render pages that do not contain any ads, banners or the pages belong to you and you can hide that content for the API, make sure to disable blocking ads, banners, and other content:

```
block_ads=false
block_cookie_banners=false
block_banners_by_heuristics=false
block_chats=false
```

Set these parameters explicitly to `false`, otherwise you rely on the default values that are not optimal for your use case and might be even changed in the future.

## Disable or enable tracking scripts

There is a lot of analytics and tracking scripts that might downgrade the performance of rendering. You can disable them by:

```
block_tracking=true
```

**However!** If you know that the websites you render doesn't have tracking scripts, you can disable them by:

```
block_tracking=true
```

If you do not need them, disable blocking tracking scripts:

```
block_tracking=false
```

Because, to block tracking scripts, the API needs to sniff all the requests, analyze them and block.

This is a parameter that you need to play with for use case, and see what works the best.

## Image format and quality

Use either `JPEG` or `WebP` format for images:

```
format=jpeg or format=webp
```

It is faster to generate, the size is usually smaller than other formats, so it is also faster to transfer these.

The limitation of the `WebP` format is that you can't use it for the huge full page screenshots. In general, it is not recommended to use it for the full page screenshots,
or if you do you use it make sure to set `full_page_max_height` and check that the rendering is not broken for your use case.

In many cases, especially if you generate just tiny previews of the websites, you also don't need high quality images. Try to set lower image quality for the images:

```
image_quality=80
```

And see if it satisfies your needs. However, for some formats reducing the quality might degrade performance. It is better to play with it.

## Viewport size and device scale factor

For huge viewport size, screenshot rendering will take more time. But one of the critical parameters is the `device_scale_factor`.

When you set its value to more than `1`, you double the size of the screenshot. If you are screenshots are not planned to be used for the high DPI displays, you can set it to `1` to reduce the size of the screenshot and rendering time.

```
device_scale_factor=1
```

Make sure to check that the quality fits your needs.

It is also changed automatically to higher values if you use the `viewport_device` parameter with a device that automatically increases it:

```
viewport_device=iphone_16
```

`device_scale_factor` will be set to 3. Try to set it explicitly to `1` and see if it works for your use case:

```
viewport_device=iphone_16
device_scale_factor=1
```

## Wait options

Try to play with the `wait_until` option. Start with `load` and see if it works for your case. Set it explicitly:

```
wait_until=load
```

If you anyway plan to render to full page screenshots and use scrolling, you don't need to wait for everything to loaded since
the page anyway will be scrolled to the bottom and likely this will cover and load all the content.

## Full page screenshots

### Try different algorithms

There are two algorithms for the full page screenshots: `by_sections` and `default`.

The default algorithm is the best one for the most of the cases. Try to use it first with disabled `full_page_scroll` and see if it works for your use case.

```
full_page_algorithm=default
```

However, if you need to try to use the `by_sections` algorithm:

```
full_page_algorithm=by_sections
```

It will render the page by sections, and will scroll anyway. It might be better algorithm if you need to trigger lazy loaded.

### Disable full page scrolling

If you do not need full page scrolling, disable it by:

```
full_page_scroll=false
```

It will dramatically reduce the rendering time. However, if your page contains lazy loaded content, it won't be loaded.

### Tune full page scrolling

If you anyway need to scroll pages, try to play with the settings of the scrolling algorithm:

```
full_page_scroll_delay=100
```

If that still allows to render most of the images for your use case, go for it.

## Summary

It is hard to make the API product to satisfies all the use cases and still be performant. But with some tuning, it is achievable.

Please, feel free to reach out at `support@screenshotone.com` if you have any questions or need more help or assistance in performance tuning.