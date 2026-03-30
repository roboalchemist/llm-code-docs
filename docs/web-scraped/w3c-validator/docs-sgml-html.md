# Source: https://validator.w3.org/docs/sgml.html

Title: Introduction To SGML for The W3C Markup Validation Service

URL Source: https://validator.w3.org/docs/sgml.html

Markdown Content:
### What is SGML?

SGML stands for Standard Generalized Markup Language. This is actually a slight misnomer, since SGML is actually a _meta-language_ — that is, a language for writing markup languages. HTML is a markup language written in SGML — an "SGML application", to use the terminology.

You don't actually have to know much about SGML to use The Validator successfully. If you're interested, though, I recommend TEI's ["A Gentle Introduction to SGML"](http://www.tei-c.org/P4X/SG.html) as a good starting point. For in-depth treatment of SGML and HTML we recommend Martin Bryan's "[Web SGML and HTML 4.0 Explained](http://www.is-thought.co.uk/book/home.htm)".

### What is a DTD?

For our purposes, a DTD, or Document Type Definition, is simply a file that defines the syntax of a [SGML](https://validator.w3.org/docs/sgml.html#sgml)-based language. The DTDs for [HTML 2.0](http://www.w3.org/MarkUp/html-spec/) and [HTML 3.2](http://www.w3.org/TR/REC-html32) were written by the HTML Working Group of the [IETF](http://www.ietf.org/), in collaboration with the [W3C](http://www.w3.org/). From [HTML 4.0](http://www.w3.org/TR/html4/) on (this includes [XHTML](http://www.w3.org/TR/xhtml1/)), the standards (both prose and DTDs) have been written by the [W3C](http://www.w3.org/).

### What is this `DOCTYPE` thing The Validator keeps pestering me for?

A `DOCTYPE` is a [SGML](https://validator.w3.org/docs/sgml.html#sgml) document type declaration. Its purpose is to tell an SGML parser what [DTD](https://validator.w3.org/docs/sgml.html#dtd) it should use to parse the document. It appears as the first line of the document, and has the form: `<!DOCTYPE html PUBLIC "quoted string">`

The "quoted string" is called a public identifier; it refers to the desired DTD by a "well-known" name, usually defined by an associated standard.

#### Why add a DOCTYPE declaration?

The Validator uses an SGML parser, and a `DOCTYPE` declaration is the most, if not the only way to know which markup language it should validate documents against.

Note that most Web browsers don't actually use an SGML parser, many of them display the documents differently based on the document's `DOCTYPE` declaration, or lack thereof. This alone is a good reason to always add a `DOCTYPE` declaration to Web documents.

So now you're preparing to add a `DOCTYPE` to your document. Be sure that the syntax is as described above, and that you use the correct public identifier; otherwise, The Validator will use the wrong DTD, or will be unable to find a DTD at all, and will produce a huge list of absolutely meaningless errors.

#### How do I add a DOCTYPE declaration?

The W3C QA Activity maintains a [List of Doctypes](http://www.w3.org/QA/2002/04/valid-dtd-list.html) that you can choose from, and the WDG maintains a document on "[Choosing a DOCTYPE](http://www.htmlhelp.com/tools/validator/doctype.html)".

**WARNING:** Some HTML editors will insert a `DOCTYPE` declaration for you. Unfortunately, sometimes thia `DOCTYPE` does not correspond to the generated HTML, which can sometimes confuse The Validator. If your editor adds a `DOCTYPE` to your page, you may need to correct it as described above before running your documents through The Validator.
