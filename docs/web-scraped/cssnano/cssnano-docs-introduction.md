# Source: https://cssnano.github.io/cssnano/docs/introduction

Title: Introduction/

URL Source: https://cssnano.github.io/cssnano/docs/introduction

Markdown Content:
[What is minification?](https://cssnano.github.io/cssnano/docs/introduction#what-is-minification%3F)
----------------------------------------------------------------------------------------------------

Minification is the process of taking some code and using various methods to reduce its size on disk. Unlike techniques such as gzip, which preserve the original semantics of the CSS file, and are therefore lossless, minification is an inherently lossy process, where values can be replaced with smaller equivalents, or selectors merged together, for example.

The end result of a minification step is that the resulting code will behave the same as the original file, but some parts will be altered to reduce the size as much as possible. Combining gzip compression with minification leads to the best reduction in file size.

[What is cssnano?](https://cssnano.github.io/cssnano/docs/introduction#what-is-cssnano%3F)
------------------------------------------------------------------------------------------

cssnano is one such minifier, which is written in [Node.js](https://nodejs.org/). It's a [PostCSS](http://postcss.org/) plugin which you can add to your build process, to ensure that the resulting stylesheet is as small as possible for a production environment.

If you don't know what a build process is, don't worry as we cover this in [our getting started guide](https://cssnano.github.io/cssnano/docs/getting-started).

[How does it benefit me?](https://cssnano.github.io/cssnano/docs/introduction#how-does-it-benefit-me%3F)
--------------------------------------------------------------------------------------------------------

### [Numerous optimisations](https://cssnano.github.io/cssnano/docs/introduction#numerous-optimisations)

We offer many different optimisations, ranging from simple transforms such as whitespace removal, to complex transforms that can merge identical keyframes with different names. See [the presets guide](https://cssnano.github.io/cssnano/docs/presets) for more information.

### [Unified CSS processing](https://cssnano.github.io/cssnano/docs/introduction#unified-css-processing)

cssnano uses [PostCSS](http://postcss.org/) to process the CSS under the hood. Because a lot of modern CSS tools use [PostCSS](http://postcss.org/), you can compose them together to work on a single abstract syntax tree (AST). This means that the overall processing time is reduced because the CSS does not have to be parsed multiple times.

### [Modern architecture & modularity](https://cssnano.github.io/cssnano/docs/introduction#modern-architecture-%26-modularity)

Because we use [PostCSS](http://postcss.org/), we can divide cssnano's responsibilities between many plugins, each performing a small optimisation. And many optimisations are scoped to a certain subset of CSS properties, which is much safer compared to minifying CSS globally using regular expressions.

Last updated on Tue, 28 Oct 2025 13:54:40 GMT
