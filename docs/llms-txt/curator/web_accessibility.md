# Source: https://docs.curator.interworks.com/site_administration/standards_compliance/web_accessibility.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Accessibility

> Scan and evaluate Curator portal for WCAG web accessibility compliance using browser extensions and tools.

This document provides instructions on how to scan your Curator portal for compliance with the Web Content
Accessibility Guidelines (WCAG)

## Prerequisites

Install the [WAVE Accessibility Extension for Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/wave-accessibility-tool/).

Similar extensions may exist in other browsers, but those are outside of the scope of this document.

## What to Scan

There are 3 main sections you'll need to check about when scanning your Curator portal.

1. Login Page
2. Global Structure
3. Page Content

### Login Page

Depending on which authentication type your Curator portal uses, you will likely need to scan the login page
and any related pages shown during the authentication process.  If you utilize a third-party authentication
source, any accessibility issues found with it will need to be fixed within that third-party product.

### Global Structure

Once authenticated to Curator, there are elements shared across all pages, such navigation, search, theme,
logo, and footer.  Any issues found with these elements will be found on each page you test, so it's worth
tracking these separately.

### Page Content

Each page on your site is by nature unique in some aspect.  Whether a page has simple static text, images,
embedded content, or multiple elements of varying content types, each page will need to be checked
individually to verify that all of the content on the page meets accessibility standards.

It should be noted that any issues found with embedded content will need to be addressed in their source
system.  For instance, if you determine there are accessibility issues with a Tableau Dashboard, you'll need
to correct those issues within your Tableau workbook and then republish it.

## How to Scan

Loop through each section and page listed above in Mozilla Firefox.  For each one, right-click on the page
and select **WAVE this page**.

As of the time of this writing, a pane will show up in your browser that lists errors, alerts, contrast
errors, and other elements that were checked for WCAG compliance.  Address the errors and contrast errors
first by clicking on the **Details** tab.  After addressing those, then focus on the alerts.

You should be able to click on each issue to show the element in question and a description of the issue.  If
the element is covered by the WAVE pane, you may need to toggle the styles off.

Most of the issues you may encounter will likely be:

* **Missing alternative text for images:** Each image should have some sort of alternative text to describe
  the image for people with visual impairments.  For instance, an image may just be a logo, but it also might
  be a chart with important information being conveyed.
* **Missing title/label text for page elements:** Some elements on a page, such as buttons, form fields, etc.
  require title text (often displayed as tooltips) or an explicit label in order for people to understand their
  use.  For instance, have you ever tried to use an app where the buttons only show an icon you've never seen
  before?  This issue is exacerbated if you must consume the entire page through a screen reader.
* **Low contrast:** Certain visual impairments make it difficult to discern elements that are too similar
  with respect to contrast.  For instance, try reading light grey text on a white background.
* **Tab order:** The order that elements are highlighted when tabbing through the site makes a big difference
  of how usable or frustrating your site is.  Imagine that your mouse stopped working and you had to use your
  site with nothing more than your keyboard's tab key.  This is how many people must navigate the web.

## Implementation vs. Core Issues

Curator provides a content management platform.  Accessibility issues may exist in the core Curator
functionality or in your actual content or implementation.  Issues found related to your content or
implementation will need to be fixed in your portal.  The Curator development staff make a good faith effort
to routinely check that core features meet accessibility standards, but issues may still slip through.  If
you find an accessibility issue in a core feature, please report it to Curator support so we can address it
in a future version.
