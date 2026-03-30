# Manipulating the DOM

**Orpheus Development Papers #8 - Manipulating the DOM**
Version 1 | From: Spine | Date: 2021-10-31

## Overview

Traditional Gazelle markup blithely mixes HTML and JavaScript together, e.g.:

```html
<input type="button" value="Preview" onclick="Quick_Preview();" />
```

This is not a good practice and prevents using CSP nonces to prevent unwanted
code injection into the site. An attempt is made to tackle this problem,
in the guise of the Dominator.

## The Dominator Pattern

At its simplest, the Dominator is the caching of JavaScript actions
(`onclick`, `onchange`) that need to be attached to DOM elements, which are
dumped at the end of the page and loaded by a DocumentReady event.

This usually involves adding an `id` to an element in order to be able to
attach to the element afterwards. For instance in `templates/staffpm/message.twig`:

Before:

```html
<input type="button" onclick="Assign();" value="Assign" />
```

After:

```twig
{{- dom.click('#assign', "Assign();") -}}
<input type="button" id="assign" value="Assign" />
```

The theory is that it is important to keep the JavaScript action close to the
HTML element that requires it (principle of locality), while not emitting the
action until the page has been loaded.

Sometimes there is a JS file that is pulled in from the `header()` method,
in which case a DocumentReady handler can be added there (when in fact there
is not one already present). In such cases it may be clearer to add the action
there.

Actions that are only actionable by staff should preferably use the Dominator.
The less code that is sent to the client, the better.

## Torrent Detail Pages

Of particular note, the torrent detail pages have a number of subsections
that are pulled in via Ajax (the lists of downloaders, snatchers and seeders).
All of these lists are subject to pagination. As such, the HTML result that is
returned from the Ajax call (to be attached to the DOM) itself needs onclick
events attached to it in order to make pagination work. The present code works,
but is a bit cumbersome and possibly over complex.
