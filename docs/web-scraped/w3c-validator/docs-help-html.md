# Source: https://validator.w3.org/docs/help.html

Title: Help for The W3C Markup Validation Service

URL Source: https://validator.w3.org/docs/help.html

Markdown Content:
Help for The W3C Markup Validation Service
===============

[![Image 1: W3C Logo](https://www.w3.org/assets/logos/w3c-2025/svg/margins/w3c-letters-bg-white.svg)](https://www.w3.org/)[Markup Validation Service](https://validator.w3.org/)
================================================================================================================================================================================

Check the markup (HTML, XHTML, …) of Web documents

Help and FAQ for the Markup Validator
-------------------------------------

Nothing wrong with the validator here, it just knows HTML better than you do. -- David Dorward, Validator's mailing-list.

### Table of contents

1.   About the Markup Validator 
    1.   [Help me! I clicked on an icon and ended up on this strange site!](https://validator.w3.org/docs/help.html#clickedandlost)
    2.   [What is _Markup Validation_?](https://validator.w3.org/docs/help.html#validation_basics)
    3.   [Is validation some kind of quality control? Does "valid" mean "quality approved by W3C"?](https://validator.w3.org/docs/help.html#validandquality)
    4.   [Is validity the same thing as conformance?](https://validator.w3.org/docs/help.html#validandconform)
    5.   **[What is the Markup Validator and what does it do?](https://validator.w3.org/docs/help.html#what-is-it)**
    6.   [Why validate?](https://validator.w3.org/docs/help.html#why-validate)
    7.   [Who owns/maintain the Markup Validator?](https://validator.w3.org/docs/help.html#who-does-validator)
    8.   [What other validators are there?](https://validator.w3.org/docs/help.html#others)
    9.   [How do I send feedback/bug reports about the Markup Validator?](https://validator.w3.org/docs/help.html#howto-feedback)

2.   Using this service 
    1.   **[How do I use the Markup validator?](https://validator.w3.org/docs/help.html#manual)**
    2.   [What is (are) this (these) error message(s)?](https://validator.w3.org/docs/help.html#errors)
    3.   [Many error messages? Don't panic.](https://validator.w3.org/docs/help.html#munged-doctype)
    4.   [I don't want error messages, I want you to clean up my page!](https://validator.w3.org/docs/help.html#cleanup)

3.   Miscellaneous (Very) Frequently Asked Questions 
    1.   [No DOCTYPE Declaration Found!](https://validator.w3.org/docs/help.html#faq-doctype)
    2.   [No Character Encoding Found!](https://validator.w3.org/docs/help.html#faq-charset)
    3.   [/check?uri=referer does not work](https://validator.w3.org/docs/help.html#faq-referer) or the validator says it does not support my ["undefined" URL scheme](https://validator.w3.org/docs/help.html#faq-referer)
    4.   [Can the validator check all the pages in my site in one batch?](https://validator.w3.org/docs/help.html#faq-batchvalidation)

[](https://validator.w3.org/docs/help.html)
### About the Markup Validator

#### Help me! I clicked on an icon and ended up on this strange site!

Don't panic!

The author of the Web page you come from once used our service to _validate_ that page, and the page passed validation. The author was then authorized to use the icon on that page, as a claim of _validity_. The icon is used as a link back to the validation service, so that the author can _revalidate_ whenever necessary. This is why, by clicking on the icon, you followed a link to the current _validation results_ for the page you came from.

The validation result was certainly positive ("this page is valid..."), but if it wasn't, you would probably do the author of the page where the icon was a favor if you could warn him/her of this abnormal situation.

If you are curious about Markup validation you may read this help document further, or you may simply use the back button of your Web browser to come back to the page where you found the "valid" icon.

#### What is _Markup Validation_?

Most pages on the World Wide Web are written in computer languages (such as HTML) that allow Web authors to structure text, add multimedia content, and specify what appearance, or style, the result should have.

As for every language, these have their own _grammar_, _vocabulary_ and _syntax_, and every document written with these computer languages are supposed to follow these rules. The (X)HTML languages, for all versions up to XHTML 1.1, are using machine-readable grammars called DTD s, a mechanism inherited from [SGML](https://validator.w3.org/docs/sgml.html).

However, Just as texts in a natural language can include spelling or grammar errors, documents using Markup languages may (for various reasons) not be following these rules. The process of verifying whether a document actually follows the rules for the language(s) it uses is called _validation_, and the tool used for that is a validator. A document that passes this process with success is called _valid_.

With these concepts in mind, we can define "markup validation" as the process of checking a Web document against the grammar (generally a DTD) it claims to be using.

#### Is validation some kind of quality control? Does "valid" mean "quality approved by W3C"?

Validity is one of the quality criteria for a Web page, but there are many others. In other words, a _valid_ Web page is not necessarily a good web page, but an _invalid_ Web page has little chance of being a good web page.

For that reason, the fact that the W3C Markup Validator says that one page passes validation does **not** mean that W3C assesses that it is a good page. It only means that a tool (not necessarily without flaws) has found the page to comply with a specific set of rules. No more, no less. This is also why the "valid ..." icons should never be considered as a "W3C seal of quality".

#### Is validity the same thing as conformance?

No, they are different concepts.

Markup languages are defined in _technical specifications_, which generally include a _formal grammar_. A document is valid when it is correctly written in accordance to the formal grammar, whereas conformance relates to the specification itself. The two _might_ be equivalent, but in most cases, some conformance requirements cannot be expressed in the grammar, making validity only a part of the conformance.

#### What is the Markup Validator and what does it do?

The Markup Validator is a free tool and service that [validates markup](https://validator.w3.org/docs/help.html#validation_basics): in other words, it checks the syntax of Web documents, written in formats such as (X)HTML.

The Validator is sort of like `lint` for C. It compares your HTML document to the defined syntax of HTML and reports any discrepancies.

[Learn more](https://validator.w3.org/about.html) about the Markup Validator and the languages it can validate.

#### Why should I validate my HTML pages?

One of the important maxims of computer programming is: Be conservative in what you produce; be liberal in what you accept.

Browsers follow the second half of this maxim by accepting Web pages and trying to display them even if they're not legal HTML. Usually this means that the browser will try to make educated guesses about what you probably meant. The problem is that different browsers (or even different versions of the same browser) will make different guesses about the same illegal construct; worse, if your HTML is _really_ pathological, the browser could get hopelessly confused and produce a mangled mess, or even crash.

That's why you want to follow the first half of the maxim by making sure your pages are legal HTML. The best way to do that is by running your documents through one or more HTML validators.

A [lengthier answer](https://validator.w3.org/docs/why.html) to this question is also available on this site if the explanation above did not satisfy you.

#### Who owns/maintain the Markup Validator?

The Markup Validator is maintained at W3C by W3C staff and benevolent collaborators, who receive a lot of help from contributors (read the [full credits](https://validator.w3.org/about.html#credits)).

#### What other validators are there?

Looking for validators at W3C, but not the Markup Validator? Check out the list of [validators at W3C](http://www.w3.org/QA/Tools/#validators), including well-known [CSS validator](http://jigsaw.w3.org/css-validator/), [link checker](https://validator.w3.org/checklink), etc.

#### How do I send feedback/bug reports about the Markup Validator?

Read the instructions on our [Feedback page](https://validator.w3.org/feedback.html).

### Using this service

#### How do I use this service?

Most probably, you will want to use the online Markup Validation service. The simple way to use this service to validate a Web page is to paste its address into the [text area](https://validator.w3.org/#uri) on the [validator's home page](https://validator.w3.org/), and press the "Check" button.

There are other possible uses and a few usage options, please read the [user's manual](https://validator.w3.org/docs/users.html) for further help with this service.

If, for some reason, you prefer running your own instance of the Markup Validator, check out our [developer's documentation](https://validator.w3.org/docs/devel.html).

#### What are these error messages?

The output of the Markup Validator may be hard to decipher for newcomers and experts alike, so we are maintaining a [list of error messages and their interpretation](https://validator.w3.org/docs/errors.html), which should help.

#### Many error messages? Don't panic.

Don't panic. Did The Validator complain about your `DOCTYPE` declaration (or lack thereof)? Make sure your document has a syntactically correct `DOCTYPE` declaration, as described in the [section on `DOCTYPE`](https://validator.w3.org/docs/sgml.html#doctype), and make sure it correctly identifies the type of HTML you're using. Then run it through The Validator again; if you're lucky, you should get a lot fewer errors.

If this doesn't help, then you may be experiencing a cascade failure — one error that gets The Validator so confused that it can't make sense of the rest of your page. Try correcting the first few errors and running your page through The Validator again.

Be patient, with a little time and experience you will learn to use the Markup Validator to clean up your HTML documents in no time.

#### I don't want error messages, I want you to clean up my page!

Have a look at tools such as [HTML Tidy](http://tidy.sourceforge.net/) and [tidyp](http://www.tidyp.com/). When selected, the "Clean up Markup with HTML-Tidy" option will output a "cleaned" version of the input document in case it was not valid, done with [HTML-Tidy](http://search.cpan.org/dist/HTML-Tidy/), using the Markup Validator's default HTML-Tidy configuration. Note that there are no guarantees about the validity or other aspects of that output, and there are many options to configure in these tools that may result in better clean up than the Validator's default options for your document, so you may want to try out them locally.

### Miscellaneous (Very) Frequently Asked Questions

#### No DOCTYPE Declaration Found!

A DOCTYPE Declaration is mandatory for HTML documents.

Unless you have very specific needs, you should use the following generic DOCTYPE: `<!DOCTYPE html>`. A typical HTML document looks like:

      <!DOCTYPE html>
      <html lang="en">
        <head>

          <title>Title</title>
        </head>

        <body>
          <!-- ... body of document ... -->
        </body>

      </html>
    
#### No Character Encoding Found!

An HTML document should be served along with its character encoding.

Specifying a character encoding is typically done by the web server configuration, by the scripts that put together pages, and inside the document itself. [IANA](http://www.iana.org/) maintains the list of [official names for character encodings](http://www.iana.org/assignments/character-sets) (called charsets in this context). You can choose from a number of encodings, though we recommend UTF-8 as particularly useful.

The W3C I18N Activity has collected a [few tips on how to do this](http://www.w3.org/International/O-charset).

To quickly check whether the document would validate after addressing the missing character encoding information, you can use the "Encoding" form control (accesskey "2") earlier in the page to force an encoding override to take effect. "iso-8859-1" (Western Europe and North America) and "utf-8" (Universal, and more commonly used in recent documents) are common encodings if you are not sure what encoding to choose.

#### /check?uri=referer does not work - or - the validator says it does not support my "undefined" URL scheme

Browsers and other Web agents usually send information about the page they come from, in a `Referer` header. The validator uses this information for a features that allows it to validate whatever page the browser last visited. The "valid" icons on some Web page usually point to the validation of the page using this feature.

Unfortunately, some zealous "security software" or Web proxies strip the referrer information from what the browser sends. Without this information the validator is not able to find what the URL of the document to validate is, and gives the same error message as when it is given a type of URL it does not understand.

Also, requests to non-secure HTTP resources from links in documents transferred with a secure protocol such as HTTPS should not include referrer information [per the HTTP/1.1 specification](http://www.w3.org/Protocols/rfc2616/rfc2616-sec15.html#sec15.1.3). As the validator at validator.w3.org is currently not available over HTTPS, this referrer feature will not work reliably for documents transferred over secure protocols (usually `https` URLs) with it.

**How to fix**:

*   Check that it is indeed the `Referer` issue. The validator should have redirected you to `https://validator.w3.org/check?uri=your_url_here`. Otherwise, check the address you have given the validator.
*   The validator cannot fix this issue. You will have to (ask your administrator to) reconfigure whichever zealous software is stripping this referrer info.
*   If you have a link on your page using the "/check?uri=referer" feature, you could replace them with the a link to the validator without this feature, e.g. `https://validator.w3.org/check?uri=http%3A%2F%2Fwww.example.com`
*   If you have no control over the page or annoying software, or your page's URL is a `https` one, simply append the address of the page you wanted validated (URI encoded) to the `https://validator.w3.org/check?uri=` address.

*   [Home](https://validator.w3.org/ "Go to the Home Page for The W3C Markup Validation Service") | 
*   [About...](https://validator.w3.org/about.html "Information About this Service") | 
*   [News](https://validator.w3.org/whatsnew.html "The changes made to this service recently") | 
*   [Docs](https://validator.w3.org/docs/ "Documentation for this Service") | 
*   [Help&FAQ](https://validator.w3.org/docs/help.html "Help and answers to frequently asked questions") | 
*   [Feedback](https://validator.w3.org/feedback.html "How to provide feedback on this service") | 
*   [Contribute](https://validator.w3.org/contribute.html "How to contribute to the validator project") | 

[![Image 2: W3C](https://www.w3.org/assets/logos/w3c/w3c-no-bars.svg)![Image 3: Open-Source](https://validator.w3.org/docs/images/opensource-55x48.png)](https://www.w3.org/Status "W3C's Open Source, bringing you free Web quality tools and more")

[![Image 4: I heart Validator logo](https://www.w3.org/QA/Tools/I_heart_validator)](https://www.w3.org/donate/)

Copyright © 2024 [World Wide Web Consortium](https://www.w3.org/). W3C®[liability](https://www.w3.org/policies/#disclaimers), [trademark](https://www.w3.org/policies/#trademarks) and [permissive license](https://www.w3.org/copyright/document-license/ "W3C Document License") rules apply.
