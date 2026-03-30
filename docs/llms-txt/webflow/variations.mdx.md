# Source: https://developers.webflow.com/browser/optimize/variations.mdx

***

title: Variations
slug: optimize/variations
description: >-
Learn about applying and recording variations to send to third-party tracking
tools.
hidden: false
'og:title': Variations
'og:description': >-
Learn about applying and recording variations to send to third-party tracking
tools.
------

Variations are alternate versions of a webpage shown to some visitors. By showing different variations to different visitors, you can test which version resonates best and drives more engagement. Variations are always part of either a test or personalization optimization.

For example, to test three new homepage headlines, you'd create an optimization for the homepage with three variations—one for each headline. To learn more about variations in Webflow Optimize, visit [the support documentation](https://help.webflow.com/hc/en-us/articles/33776880496275-Create-or-edit-optimization-variations).

## API callbacks

After each variation is recorded, the applied variation is passed to callback functions registered via [`onVariationRecorded()`](/browser/optimize/onVariationRecorded). Note that each time a variation is recorded, the callback fires (as opposed to just once per page).

Use the [`onVariationRecorded()`](/browser/optimize/onVariationRecorded) method to capture variation data and send it to custom in-house analytics tools.

## Looking for more information?

Visit the [Webflow Help Center](https://help.webflow.com/hc/en-us/articles/33776880496275-Create-or-edit-optimization-variations) to learn more about variations in Webflow Optimize, including:

* Creating and editing variations
* Setting variation strengths and traffic allocation
* Previewing variations before publishing
* Best practices for variation design
* Troubleshooting common variation issues
