# Using your browser’s Developer Tools for scraping

Here is a general guide on how to use your browser’s Developer Tools
to ease the scraping process. Today almost all browsers come with
built in Developer Tools [https://en.wikipedia.org/wiki/Web_development_tools] and although we will use Firefox in this
guide, the concepts are applicable to any other browser.

In this guide we’ll introduce the basic tools to use from a browser’s
Developer Tools by scraping quotes.toscrape.com [https://quotes.toscrape.com].

## Caveats with inspecting the live browser DOM

Since Developer Tools operate on a live browser DOM, what you’ll actually see
when inspecting the page source is not the original HTML, but a modified one
after applying some browser clean up and executing JavaScript code.  Firefox,
in particular, is known for adding `<tbody>` elements to tables.  Scrapy, on
the other hand, does not modify the original page HTML, so you won’t be able to
extract any data if you use `<tbody>` in your XPath expressions.

Therefore, you should keep in mind the following things:

- 

Disable JavaScript while inspecting the DOM looking for XPaths to be
used in Scrapy (in the Developer Tools settings click Disable JavaScript)

- 

Never use full XPath paths, use relative and clever ones based on attributes
(such as `id`, `class`, `width`, etc) or any identifying features like
`contains(@href, 'image')`.

- 

Never include `<tbody>` elements in your XPath expressions unless you
really know what you’re doing

## Inspecting a website

By far the most handy feature of the Developer Tools is the Inspector
feature, which allows you to inspect the underlying HTML code of
any webpage. To demonstrate the Inspector, let’s look at the
quotes.toscrape.com [https://quotes.toscrape.com]-site.

On the site we have a total of ten quotes from various authors with specific
tags, as well as the Top Ten Tags. Let’s say we want to extract all the quotes
on this page, without any meta-information about authors, tags, etc.

Instead of viewing the whole source code for the page, we can simply right click
on a quote and select `Inspect Element (Q)`, which opens up the Inspector.
In it you should see something like this:

The interesting part for us is this:

```
<div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
  <span class="text" itemprop="text">(...)</span>
  <span>(...)</span>
  <div class="tags">(...)</div>
</div>

```