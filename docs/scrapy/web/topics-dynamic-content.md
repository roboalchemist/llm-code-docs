# Selecting dynamically-loaded content

Some webpages show the desired data when you load them in a web browser.
However, when you download them using Scrapy, you cannot reach the desired data
using selectors.

When this happens, the recommended approach is to
find the data source and extract the data
from it.

If you fail to do that, and you can nonetheless access the desired data through
the DOM from your web browser, see
Using a headless browser.

## Finding the data source

To extract the desired data, you must first find its source location.

If the data is in a non-text-based format, such as an image or a PDF document,
use the network tool of your web browser to find
the corresponding request, and reproduce it.

If your web browser lets you select the desired data as text, the data may be
defined in embedded JavaScript code, or loaded from an external resource in a
text-based format.

In that case, you can use a tool like wgrep [https://github.com/stav/wgrep] to find the URL of that resource.

If the data turns out to come from the original URL itself, you must
inspect the source code of the webpage to
determine where the data is located.

If the data comes from a different URL, you will need to reproduce the
corresponding request.

## Inspecting the source code of a webpage

Sometimes you need to inspect the source code of a webpage (not the
DOM) to determine where some desired data is located.

Use Scrapy’s `fetch` command to download the webpage contents as seen
by Scrapy:

```
scrapy fetch --nolog https://example.com > response.html

```