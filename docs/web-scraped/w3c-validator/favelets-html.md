# Source: https://validator.w3.org/favelets.html

Title: Favelets For The W3C Markup Validation Service

URL Source: https://validator.w3.org/favelets.html

Markdown Content:
Favelets For The W3C Markup Validation Service
===============

[![Image 1: W3C Logo](https://www.w3.org/assets/logos/w3c-2025/svg/margins/w3c-letters-bg-white.svg)](https://www.w3.org/)[Markup Validation Service](https://validator.w3.org/)
================================================================================================================================================================================

Check the markup (HTML, XHTML, …) of Web documents

[](https://validator.w3.org/favelets.html)
[Favelets](http://favelets.com/) For The Validator
--------------------------------------------------

[Favelets](http://favelets.com/) are small snippets of JavaScript embedded in a Bookmark URL that allow Bookmarks in browsers to do various advanced things. Popular [Favelets](http://favelets.com/) include variants that prompt the user for a phrase and search the web for that phrase, or that finds older versions of the currently viewed page in the [WayBack Machine](http://www.archive.org/ "The Internet Archive WayBack Machine"). More Favelets can be found from <[http://favelets.com/](http://favelets.com/)>.

[Favelets](http://favelets.com/) depend on support for `javascript:`URLs in your browser's Bookmarks feature, and each [Favelet](http://favelets.com/) may depend on support for a specific part of the JavaScript specification to work properly. MSIE versions 5.0 and later, and Mozilla 1.0 and later — including browsers using the embedded version of Mozilla, such as Netscape 7.0 — are known to support most [Favelets](http://favelets.com/).

Most browsers that have support for basic JavaScript and DOM also support basic [Favelets](http://favelets.com/), but more advanced [Favelets](http://favelets.com/) may require more complete DOM1 and DOM2 support. Netscape 4.x is a lost cause in this regard, and with its poor support for standards in general it is probably better to avoid it altogether.

"[Validate _This_ Page](javascript:void(window.location='https://validator.w3.org/check?uri='+encodeURIComponent(window.location)) "Validate This Page")" This is the basic "Validate This Page" [Favelet](http://favelets.com/). It simply submits the URL for the currently viewed page to the Validator for processing. Results appear in the same window. "[Validate _This_ Page In New Window](javascript:window.open('https://validator.w3.org/check?uri='+encodeURIComponent(window.location));void%200 "Validate This Page In New Window")" Like the last [Favelet](http://favelets.com/), this also submits the URL of the current page to the Validator for processing, but this version will show the results in a new window. "[Validate Page...](javascript:void(q=prompt('Validate%20Page:',''));if(q)void(window.location='https://validator.w3.org/check?uri='+encodeURIComponent(q)) "Validate Page...")" Puts up a dialog with a text entry field where you can type in the URL of a page you would like to Validate. The results appear in the current window. "[Validate Page In New Window...](javascript:void(q=prompt('Validate%20Page:',''));if(q)window.open('https://validator.w3.org/check?uri='+encodeURIComponent(q));void%200 "Validate Page In New Window...")"Same as above but shows results in a new window.

*   [Home](https://validator.w3.org/ "Go to the Home Page for The W3C Markup Validation Service") | 
*   [About...](https://validator.w3.org/about.html "Information About this Service") | 
*   [News](https://validator.w3.org/whatsnew.html "The changes made to this service recently") | 
*   [Docs](https://validator.w3.org/docs/ "Documentation for this Service") | 
*   [Help&FAQ](https://validator.w3.org/docs/help.html "Help and answers to frequently asked questions") | 
*   [Feedback](https://validator.w3.org/feedback.html "How to provide feedback on this service") | 
*   [Contribute](https://validator.w3.org/contribute.html "How to contribute to the validator project") | 

[![Image 2: W3C](https://www.w3.org/assets/logos/w3c/w3c-no-bars.svg)![Image 3: Open-Source](https://validator.w3.org/images/opensource-55x48.png)](https://www.w3.org/Status "W3C's Open Source, bringing you free Web quality tools and more")

[![Image 4: I heart Validator logo](https://www.w3.org/QA/Tools/I_heart_validator)](https://www.w3.org/donate/)

Copyright © 2024 [World Wide Web Consortium](https://www.w3.org/). W3C®[liability](https://www.w3.org/policies/#disclaimers), [trademark](https://www.w3.org/policies/#trademarks) and [permissive license](https://www.w3.org/copyright/document-license/ "W3C Document License") rules apply.
