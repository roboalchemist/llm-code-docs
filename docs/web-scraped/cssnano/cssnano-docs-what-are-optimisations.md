# Source: https://cssnano.github.io/cssnano/docs/what-are-optimisations/

Title: Optimisations/

URL Source: https://cssnano.github.io/cssnano/docs/what-are-optimisations/

Markdown Content:
[What are optimisations?](https://cssnano.github.io/cssnano/docs/what-are-optimisations/#what-are-optimisations%3F)
-------------------------------------------------------------------------------------------------------------------

An optimisation is a module that performs a transform on some CSS code in order to reduce its size, or failing this, the final gzip size of the CSS. Each optimisation is performed by either one module or a few modules working together.

Due to the nature of dividing cssnano's responsibilities across several modules, there will be some cases where using a transform standalone will not produce the most optimal output. For example, postcss-colormin will not trim whitespace inside color functions as this is handled by postcss-normalize-whitespace.

[What optimisations do you support?](https://cssnano.github.io/cssnano/docs/what-are-optimisations/#what-optimisations-do-you-support%3F)
-----------------------------------------------------------------------------------------------------------------------------------------

The optimisations are different depending on which preset cssnano is configured with; with the default preset, we offer safe transforms only.

| Optimisation | default | advanced | lite |
| --- | --- | --- | --- |
| [autoprefixer](https://cssnano.github.io/cssnano/docs/optimisations/autoprefixer) | ❌ | ✅ | ❌ |
| [cssDeclarationSorter](https://cssnano.github.io/cssnano/docs/optimisations/cssdeclarationsorter) | ✅ | ✅ | ❌ |
| [calc](https://cssnano.github.io/cssnano/docs/optimisations/calc) | ✅ | ✅ | ❌ |
| [colormin](https://cssnano.github.io/cssnano/docs/optimisations/colormin) | ✅ | ✅ | ❌ |
| [convertValues](https://cssnano.github.io/cssnano/docs/optimisations/convertvalues) | ✅ | ✅ | ❌ |
| [discardComments](https://cssnano.github.io/cssnano/docs/optimisations/discardcomments) | ✅ | ✅ | ✅ |
| [discardDuplicates](https://cssnano.github.io/cssnano/docs/optimisations/discardduplicates) | ✅ | ✅ | ❌ |
| [discardEmpty](https://cssnano.github.io/cssnano/docs/optimisations/discardempty) | ✅ | ✅ | ✅ |
| [discardOverridden](https://cssnano.github.io/cssnano/docs/optimisations/discardoverridden) | ✅ | ✅ | ❌ |
| [discardUnused](https://cssnano.github.io/cssnano/docs/optimisations/discardunused) | ❌ | ✅ | ❌ |
| [mergeIdents](https://cssnano.github.io/cssnano/docs/optimisations/mergeidents) | ❌ | ✅ | ❌ |
| [mergeLonghand](https://cssnano.github.io/cssnano/docs/optimisations/mergelonghand) | ✅ | ✅ | ❌ |
| [mergeRules](https://cssnano.github.io/cssnano/docs/optimisations/mergerules) | ✅ | ✅ | ❌ |
| [minifyFontValues](https://cssnano.github.io/cssnano/docs/optimisations/minifyfontvalues) | ✅ | ✅ | ❌ |
| [minifyGradients](https://cssnano.github.io/cssnano/docs/optimisations/minifygradients) | ✅ | ✅ | ❌ |
| [minifyParams](https://cssnano.github.io/cssnano/docs/optimisations/minifyparams) | ✅ | ✅ | ❌ |
| [minifySelectors](https://cssnano.github.io/cssnano/docs/optimisations/minifyselectors) | ✅ | ✅ | ❌ |
| [normalizeCharset](https://cssnano.github.io/cssnano/docs/optimisations/normalizecharset) | ✅ | ✅ | ❌ |
| [normalizeDisplayValues](https://cssnano.github.io/cssnano/docs/optimisations/normalizedisplayvalues) | ✅ | ✅ | ❌ |
| [normalizePositions](https://cssnano.github.io/cssnano/docs/optimisations/normalizepositions) | ✅ | ✅ | ❌ |
| [normalizeRepeatStyle](https://cssnano.github.io/cssnano/docs/optimisations/normalizerepeatstyle) | ✅ | ✅ | ❌ |
| [normalizeString](https://cssnano.github.io/cssnano/docs/optimisations/normalizestring) | ✅ | ✅ | ❌ |
| [normalizeTimingFunctions](https://cssnano.github.io/cssnano/docs/optimisations/normalizetimingfunctions) | ✅ | ✅ | ❌ |
| [normalizeUnicode](https://cssnano.github.io/cssnano/docs/optimisations/normalizeunicode) | ✅ | ✅ | ❌ |
| [normalizeUrl](https://cssnano.github.io/cssnano/docs/optimisations/normalizeurl) | ✅ | ✅ | ❌ |
| [normalizeWhitespace](https://cssnano.github.io/cssnano/docs/optimisations/normalizewhitespace) | ✅ | ✅ | ✅ |
| [orderedValues](https://cssnano.github.io/cssnano/docs/optimisations/orderedvalues) | ✅ | ✅ | ❌ |
| [reduceIdents](https://cssnano.github.io/cssnano/docs/optimisations/reduceidents) | ❌ | ✅ | ❌ |
| [reduceInitial](https://cssnano.github.io/cssnano/docs/optimisations/reduceinitial) | ✅ | ✅ | ❌ |
| [reduceTransforms](https://cssnano.github.io/cssnano/docs/optimisations/reducetransforms) | ✅ | ✅ | ❌ |
| [svgo](https://cssnano.github.io/cssnano/docs/optimisations/svgo) | ✅ | ✅ | ❌ |
| [uniqueSelectors](https://cssnano.github.io/cssnano/docs/optimisations/uniqueselectors) | ✅ | ✅ | ❌ |
| [zindex](https://cssnano.github.io/cssnano/docs/optimisations/zindex) | ❌ | ✅ | ❌ |

You can read more about presets in our [presets guide](https://cssnano.github.io/cssnano/docs/presets).

Last updated on Tue, 28 Oct 2025 13:54:40 GMT
