# Source: https://cssnano.github.io/cssnano/

Title: /

URL Source: https://cssnano.github.io/cssnano/

Published Time: Fri, 06 Mar 2026 17:48:11 GMT

Markdown Content:
![Image 1: CSSNANO](https://cssnano.github.io/cssnano/img/logo.svg)

Deliver your website's styles, faster.

Plug in cssnano into your build step for modern CSS compression.

[Get Started](https://cssnano.github.io/cssnano/docs/introduction)

What it does
------------

cssnano takes your nicely formatted CSS and runs it through many focused optimisations, to ensure that the final result is as small as possible for a production environment.

### Input

```
/* normalize selectors */
h1::before, h1:before {
    /* reduce shorthand even further */
    margin: 10px 20px 10px 20px;
    /* reduce color values */
    color: #ff0000;
    /* remove duplicated properties */
    font-weight: 400;
    font-weight: 400;
    /* reduce position values */
    background-position: bottom right;
    /* normalize wrapping quotes */
    quotes: '«' "»";
    /* reduce gradient parameters */
    background: linear-gradient(to bottom, #ffe500 0%, #ffe500 50%, #121 50%, #121 100%);
    /* replace initial values */
    min-width: initial;
}
/* correct invalid placement */
@charset "utf-8";
```

### Output

`@charset "utf-8";h1:before{margin:10px 20px;color:red;font-weight:400;background-position:100% 100%;quotes:"«" "»";background:linear-gradient(180deg,#ffe500,#ffe500 50%,#121 0,#121);min-width:0}`
The semantics of this CSS have been kept the same, but the extraneous whitespace has been removed, the identifiers compressed, and unnecessary definitions purged from the stylesheet. This gives you a much smaller CSS for production use.

By default, cssnano performs safe optimisations on your CSS file, but we also offer an advanced preset with techniques that you can use to maximise compression. For more details, see our [optimisations](https://cssnano.github.io/cssnano/docs/what-are-optimisations/) guide.

Original (gzip)325 B
Minified (gzip)177 B
Difference 148 B
Percent 54.46%

Features
--------

![Image 2](https://cssnano.github.io/cssnano/img/postcss.svg)

### PostCSS Based

CSSNANO is built upon postcss plugins and environments

![Image 3](https://cssnano.github.io/cssnano/img/undraw_settings.svg)

### 30+ Plugins

CSSNANO has more than 30 plugins for optimizing your css

![Image 4](https://cssnano.github.io/cssnano/img/undraw_config.svg)

### Configurable

CSSNANO supports custom configs using presets which controls the level of optimization

Technology
----------

cssnano is powered by PostCSS, a tool for transforming styles with JavaScript. Specifically, its plugin architecture allows us to compose cssnano out of small modules with limited responsibilities. It also allows you to easily insert cssnano into your build step, along with other processors that can lint your CSS for errors, or transpile future syntax. ![Image 5](https://cssnano.github.io/cssnano/img/postcss.svg)
