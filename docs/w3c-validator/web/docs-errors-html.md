# Source: https://validator.w3.org/docs/errors.html

Title: Error Explanations for The W3C Markup Validation Service

URL Source: https://validator.w3.org/docs/errors.html

Markdown Content:
25: general entity X not defined and no default entity
This is usually a cascading error caused by a an undefined entity reference or use of an unencoded ampersand (&) in an URL or body text. See the previous message for further details.

[✉](https://validator.w3.org/feedback.html?errmsg_id=25#errormsg "Suggest improvements on this error message through our feedback channels")

28: unterminated comment: found end of entity inside comment
Check that you are using a proper syntax for your comments, e.g: <!-- comment here -->. This error may appear if you forget the last "--" to close one comment, therefore including the rest of the content in your comment.

[✉](https://validator.w3.org/feedback.html?errmsg_id=28#errormsg "Suggest improvements on this error message through our feedback channels")

38: literal is missing closing delimiter
Did you forget to close a (double) quote mark?

[✉](https://validator.w3.org/feedback.html?errmsg_id=38#errormsg "Suggest improvements on this error message through our feedback channels")

42: unknown declaration type X
This error may appear if you are using a bad syntax for your comments, such as "<!invalid comment>" The proper syntax for comments is <!-- your comment here -->.

[✉](https://validator.w3.org/feedback.html?errmsg_id=42#errormsg "Suggest improvements on this error message through our feedback channels")

47: end of document in prolog
This error may appear when the validator receives an empty document. Please make sure that the document you are uploading is not empty, and [report](https://validator.w3.org/feedback.html) any discrepancy.

[✉](https://validator.w3.org/feedback.html?errmsg_id=47#errormsg "Suggest improvements on this error message through our feedback channels")

63: character data is not allowed here

You have used character data somewhere it is not permitted to appear. Mistakes that can cause this error include:

*   putting text directly in the body of the document without wrapping it in a container element (such as a <p>aragraph</p>), or
*   forgetting to quote an attribute value (where characters such as "%" and "/" are common, but cannot appear without surrounding quotes), or
*   using XHTML-style self-closing tags (such as <meta ... />) in HTML 4.01 or earlier. To fix, remove the extra slash ('/') character. For more information about the reasons for this, see [Empty elements in SGML, HTML, XML, and XHTML](http://www.cs.tut.fi/~jkorpela/html/empty.html). 

[✉](https://validator.w3.org/feedback.html?errmsg_id=63#errormsg "Suggest improvements on this error message through our feedback channels")

64: document type does not allow element X here

The element named above was found in a context where it is not allowed. This could mean that you have incorrectly nested elements -- such as a "style" element in the "body" section instead of inside "head" -- or two elements that overlap (which is not allowed).

One common cause for this error is the use of XHTML syntax in HTML documents. Due to HTML's rules of implicitly closed elements, this error can create cascading effects. For instance, using XHTML's "self-closing" tags for "meta" and "link" in the "head" section of a HTML document may cause the parser to infer the end of the "head" section and the beginning of the "body" section (where "link" and "meta" are not allowed; hence the reported error).

[✉](https://validator.w3.org/feedback.html?errmsg_id=64#errormsg "Suggest improvements on this error message through our feedback channels")

65: document type does not allow element X here; missing one of Y start-tag

The mentioned element is not allowed to appear in the context in which you've placed it; the other mentioned elements are the only ones that are both allowed there _and_ can contain the element mentioned. This might mean that you need a containing element, or possibly that you've forgotten to close a previous element.

One possible cause for this message is that you have attempted to put a block-level element (such as "<p>" or "<table>") inside an inline element (such as "<a>", "<span>", or "<font>").

[✉](https://validator.w3.org/feedback.html?errmsg_id=65#errormsg "Suggest improvements on this error message through our feedback channels")

68: end tag for X omitted, but its declaration does not permit this

*   You forgot to close a tag, or
*   you used something inside this tag that was not allowed, and the validator is complaining that the tag should be closed before such content can be allowed.

The next message, "`start tag was here`" points to the particular instance of the tag in question); the positional indicator points to where the validator expected you to close the tag.

[✉](https://validator.w3.org/feedback.html?errmsg_id=68#errormsg "Suggest improvements on this error message through our feedback channels")

69: start tag was here
This is not an error, but rather a pointer to the start tag of the element the previous error referred to.

[✉](https://validator.w3.org/feedback.html?errmsg_id=69#errormsg "Suggest improvements on this error message through our feedback channels")

70: end tag for X omitted, but OMITTAG NO was specified
You may have neglected to close an element, or perhaps you meant to "self-close" an element, that is, ending it with "/>" instead of ">".

[✉](https://validator.w3.org/feedback.html?errmsg_id=70#errormsg "Suggest improvements on this error message through our feedback channels")

71: start tag was here
This is not an error, but rather a pointer to the start tag of the element the previous error referred to.

[✉](https://validator.w3.org/feedback.html?errmsg_id=71#errormsg "Suggest improvements on this error message through our feedback channels")

73: end tag for X which is not finished

Most likely, you nested tags and closed them in the wrong order. For example <p><em>...</p> is not acceptable, as <em> must be closed before <p>. Acceptable nesting is: <p><em>...</em></p>

Another possibility is that you used an element which requires a child element that you did not include. Hence the parent element is "not finished", not complete. For instance, in HTML the <head> element must contain a <title> child element, lists require appropriate list items (<ul> and <ol> require <li>; <dl> requires <dt> and <dd>), and so on.

[✉](https://validator.w3.org/feedback.html?errmsg_id=73#errormsg "Suggest improvements on this error message through our feedback channels")

76: element X undefined

You have used the element named above in your document, but the document type you are using does not define an element of that name. This error is often caused by:

*   incorrect use of the "Strict" document type with a document that uses frames (e.g. you must use the "Frameset" document type to get the "<frameset>" element),
*   by using vendor proprietary extensions such as "<spacer>" or "<marquee>" (this is usually fixed by using CSS to achieve the desired effect instead).
*   by using upper-case tags in XHTML (in XHTML attributes and elements must be all lower-case).

[✉](https://validator.w3.org/feedback.html?errmsg_id=76#errormsg "Suggest improvements on this error message through our feedback channels")

79: end tag for element X which is not open

The Validator found an end tag for the above element, but that element is not currently open. This is often caused by a leftover end tag from an element that was removed during editing, or by an implicitly closed element (if you have an error related to an element being used where it is not allowed, this is almost certainly the case). In the latter case this error will disappear as soon as you fix the original problem.

If this error occurred in a script section of your document, you should probably read this [FAQ entry](https://validator.w3.org/docs/help.html#faq-javascript).

[✉](https://validator.w3.org/feedback.html?errmsg_id=79#errormsg "Suggest improvements on this error message through our feedback channels")

82: an attribute value must be a literal unless it contains only name characters
You have used a character that is not considered a "name character" in an attribute value. Which characters are considered "name characters" varies between the different document types, but a good rule of thumb is that unless the value contains _only_ lower or upper case letters in the range a-z you must put quotation marks around the value. In fact, unless you have _extreme_ file size requirements it is a very very good idea to _always_ put quote marks around your attribute values. It is never wrong to do so, and very often it is absolutely necessary.

[✉](https://validator.w3.org/feedback.html?errmsg_id=82#errormsg "Suggest improvements on this error message through our feedback channels")

105: an attribute specification must start with a name or name token
An attribute name (and some attribute values) must start with one of a restricted set of characters. This error usually indicates that you have failed to add a closing quotation mark on a previous attribute value (so the attribute value looks like the start of a new attribute) or have used an attribute that is not defined (usually a typo in a common attribute name).

[✉](https://validator.w3.org/feedback.html?errmsg_id=105#errormsg "Suggest improvements on this error message through our feedback channels")

107: the name and VI delimiter can be omitted from an attribute specification only if SHORTTAG YES is specified

"VI delimiter" is a technical term for the equal sign. This error message means that the name of an attribute and the equal sign cannot be omitted when specifying an attribute. A common cause for this error message is the use of "Attribute Minimization" in document types where it is not allowed, in [XHTML](http://www.w3.org/TR/xhtml1/#h-4.5) for instance.

How to fix: For attributes such as compact, checked or selected, do not write e.g <option selected ... but rather <option selected="selected" ...

[✉](https://validator.w3.org/feedback.html?errmsg_id=107#errormsg "Suggest improvements on this error message through our feedback channels")

108: there is no attribute X

You have used the attribute named above in your document, but the document type you are using does not support that attribute for this element. This error is often caused by incorrect use of the "Strict" document type with a document that uses frames (e.g. you must use the "Transitional" document type to get the "target" attribute), or by using vendor proprietary extensions such as "marginheight" (this is usually fixed by using CSS to achieve the desired effect instead).

This error may also result if the element itself is not supported in the document type you are using, as an undefined element will have no supported attributes; in this case, see the element-undefined error message for further information.

How to fix: check the spelling and case of the element and attribute, (Remember XHTML is all lower-case) and/or check that they are both allowed in the chosen document type, and/or use CSS instead of this attribute. If you received this error when using the <embed> element to incorporate flash media in a Web page, see the [FAQ item on valid flash](https://validator.w3.org/docs/help.html#faq-flash).

[✉](https://validator.w3.org/feedback.html?errmsg_id=108#errormsg "Suggest improvements on this error message through our feedback channels")

111: an attribute value literal can occur in an attribute specification list only after a VI delimiter
Have you forgotten the "equal" sign marking the separation between the attribute and its declared value? Typical syntax is `attribute="value"`.

[✉](https://validator.w3.org/feedback.html?errmsg_id=111#errormsg "Suggest improvements on this error message through our feedback channels")

112: duplicate specification of attribute X
You have specified an attribute more than once. Example: Using the "`height`" attribute twice on the same "`img`" tag.

[✉](https://validator.w3.org/feedback.html?errmsg_id=112#errormsg "Suggest improvements on this error message through our feedback channels")

120: normalized length of attribute value literal must not exceed LITLEN (X); length was Y

This error almost always means that you've forgotten a closing quote on an attribute value. For instance, in:

```
<img src="fred.gif>
            <!-- 50 lines of stuff -->
            <img src="joe.gif">
```

The "`src`" value for the first `<img>` is the entire fifty lines of stuff up to the next double quote, which probably exceeds the [SGML](https://validator.w3.org/docs/sgml.html#sgml)-defined length limit for HTML string literals. Note that the position indicator in the error message points to where the attribute value _ended_ — in this case, the `"joe.gif"` line.

[✉](https://validator.w3.org/feedback.html?errmsg_id=120#errormsg "Suggest improvements on this error message through our feedback channels")

121: syntax of attribute value does not conform to declared value
The value of an attribute contained something that is not allowed by the specified syntax for that type of attribute. For instance, the “`selected`” attribute must be either minimized as “`selected`” or spelled out in full as “`selected="selected"`”; the variant “`selected=""`” is not allowed.

[✉](https://validator.w3.org/feedback.html?errmsg_id=121#errormsg "Suggest improvements on this error message through our feedback channels")

122: character X is not allowed in the value of attribute Y
It is possible that you violated the naming convention for this attribute. For example, `id` and `name` attributes must begin with a letter, not a digit.

[✉](https://validator.w3.org/feedback.html?errmsg_id=122#errormsg "Suggest improvements on this error message through our feedback channels")

123: value of attribute X must be a single token
This attribute cannot take a space-separated list of words as a value, but only one word ("token"). This may also be caused by the use of a space for the value of an attribute which does not permit it.

[✉](https://validator.w3.org/feedback.html?errmsg_id=123#errormsg "Suggest improvements on this error message through our feedback channels")

124: value of attribute Y invalid: X cannot start a number token
The value of this attribute should be a number, and you probably used a wrong syntax.

[✉](https://validator.w3.org/feedback.html?errmsg_id=124#errormsg "Suggest improvements on this error message through our feedback channels")

125: value of attribute Y invalid: X cannot start a name
It is possible that you violated the naming convention for this attribute. For example, `id` and `name` attributes must begin with a letter, not a digit.

[✉](https://validator.w3.org/feedback.html?errmsg_id=125#errormsg "Suggest improvements on this error message through our feedback channels")

127: required attribute X not specified

The attribute given above is required for an element that you've used, but you have omitted it. For instance, in most HTML and XHTML document types the "type" attribute is required on the "script" element and the "alt" attribute is required for the "img" element.

Typical values for `type` are `type="text/css"` for `<style>` and `type="text/javascript"` for `<script>`.

[✉](https://validator.w3.org/feedback.html?errmsg_id=127#errormsg "Suggest improvements on this error message through our feedback channels")

131: value of attribute Y cannot be X; must be one of Z
The value of the attribute is defined to be one of a list of possible values but in the document it contained something that is not allowed for that type of attribute. For instance, the “`selected`” attribute must be either minimized as “`selected`” or spelled out in full as “`selected="selected"`”; a value like “`selected="true"`” is not allowed.

[✉](https://validator.w3.org/feedback.html?errmsg_id=131#errormsg "Suggest improvements on this error message through our feedback channels")

137: invalid comment declaration: found character X outside comment but inside comment declaration
Check that you are using a proper syntax for your comments, e.g: <!-- comment here -->. This error may appear if you forget the last "--" to close one comment, and later open another.

[✉](https://validator.w3.org/feedback.html?errmsg_id=137#errormsg "Suggest improvements on this error message through our feedback channels")

139: non SGML character number X

You have used an illegal character in your text. HTML uses the standard [UNICODE Consortium](http://www.unicode.org/) character repertoire, and it leaves undefined (among others) 65 character codes (0 to 31 inclusive and 127 to 159 inclusive) that are sometimes used for typographical quote marks and similar in proprietary character sets. The validator has found one of these undefined characters in your document. The character may appear on your browser as a curly quote, or a trademark symbol, or some other fancy glyph; on a different computer, however, it will likely appear as a completely different character, or nothing at all.

Your best bet is to replace the character with the nearest equivalent ASCII character, or to use an appropriate [character entity](http://www.w3.org/MarkUp/html3/latin1.html).  For more information on Character Encoding on the web, see Alan Flavell's excellent [HTML Character Set Issues](http://web.archive.org/web/20060425191748/ppewww.ph.gla.ac.uk/~flavell/charset/) reference.

This error can also be triggered by formatting characters embedded in documents by some word processors. If you use a word processor to edit your HTML documents, be sure to use the "Save as ASCII" or similar command to save the document without formatting information.

[✉](https://validator.w3.org/feedback.html?errmsg_id=139#errormsg "Suggest improvements on this error message through our feedback channels")

141: ID X already defined
An "id" is a unique identifier. Each time this attribute is used in a document it must have a different value. If you are using this attribute as a hook for style sheets it may be more appropriate to use classes (which group elements) than id (which are used to identify exactly one element).

[✉](https://validator.w3.org/feedback.html?errmsg_id=141#errormsg "Suggest improvements on this error message through our feedback channels")

183: reference to non-existent ID X

This error can be triggered by:

*   A non-existent input, select or textarea element
*   A missing id attribute
*   A typographical error in the id attribute

Try to check the spelling and case of the id you are referring to.

[✉](https://validator.w3.org/feedback.html?errmsg_id=183#errormsg "Suggest improvements on this error message through our feedback channels")

187: no document type declaration; will parse without validation

The document type could not be determined, because the document had no correct DOCTYPE declaration. The document does not look like HTML, therefore automatic fallback could not be performed, and the document was only checked against basic markup syntax.

Learn [how to add a doctype to your document](https://validator.w3.org/docs/help.html#faq-doctype) from our FAQ, or use the validator's `Document Type` option to validate your document against a specific Document Type.

[✉](https://validator.w3.org/feedback.html?errmsg_id=187#errormsg "Suggest improvements on this error message through our feedback channels")

246: unclosed start-tag requires SHORTTAG YES
The construct <foo<bar> is valid in HTML (it is an example of the rather obscure “Shorttags” feature) but [its use is not recommended](http://www.w3.org/TR/html4/appendix/notes.html#h-B.3.7). In most cases, this is a typo that you will want to fix. If you really want to use shorttags, be aware that they are not well implemented by browsers.

[✉](https://validator.w3.org/feedback.html?errmsg_id=246#errormsg "Suggest improvements on this error message through our feedback channels")

247: NET-enabling start-tag requires SHORTTAG YES

For the current document, the validator interprets strings like `<FOO />` according to legacy rules that break the expectations of most authors and thus cause confusing warnings and error messages from the validator. This interpretation is triggered by HTML 4 documents or other SGML-based HTML documents. To avoid the messages, simply remove the "/" character in such contexts. NB: If you expect `<FOO />` to be interpreted as an XML-compatible "self-closing" tag, then you need to use XHTML or HTML5.

This warning and related errors may also be caused by an unquoted attribute value containing one or more "/". Example: `<a href=http://w3c.org>W3C</a>`. In such cases, the solution is to put quotation marks around the value.

[✉](https://validator.w3.org/feedback.html?errmsg_id=247#errormsg "Suggest improvements on this error message through our feedback channels")

248: unclosed end-tag requires SHORTTAG YES
The construct </foo<bar> is valid in HTML (it is an example of the rather obscure “Shorttags” feature) but [its use is not recommended](http://www.w3.org/TR/html4/appendix/notes.html#h-B.3.7). In most cases, this is a typo that you will want to fix. If you really want to use shorttags, be aware that they are not well implemented by browsers.

[✉](https://validator.w3.org/feedback.html?errmsg_id=248#errormsg "Suggest improvements on this error message through our feedback channels")

323: DTD did not contain element declaration for document type name

A DOCTYPE declares the version of the language used, as well as what the root (top) element of your document will be. For example, if the top element of your document is <html>, the DOCTYPE declaration will look like: "<!DOCTYPE html".

In most cases, it is safer not to type or edit the DOCTYPE declaration at all, and preferable to let a tool include it, or copy and paste it from a [trusted list of DTDs](http://www.w3.org/QA/2002/04/valid-dtd-list.html).

[✉](https://validator.w3.org/feedback.html?errmsg_id=323#errormsg "Suggest improvements on this error message through our feedback channels")

325: reference to entity X for which no system identifier could be generated
This is usually a cascading error caused by a an undefined entity reference or use of an unencoded ampersand (&) in an URL or body text. See the previous message for further details.

[✉](https://validator.w3.org/feedback.html?errmsg_id=325#errormsg "Suggest improvements on this error message through our feedback channels")

333: empty start-tag
The construct <> is sometimes valid in HTML (it is an example of the rather obscure “Shorttags” feature) but [its use is not recommended](http://www.w3.org/TR/html4/appendix/notes.html#h-B.3.7). In most cases, this is a typo that you will want to fix. If you really want to use shorttags, be aware that they are not well implemented by browsers.

[✉](https://validator.w3.org/feedback.html?errmsg_id=333#errormsg "Suggest improvements on this error message through our feedback channels")

334: empty end-tag
The construct </> is valid in HTML (it is an example of the rather obscure “Shorttags” feature) but [its use is not recommended](http://www.w3.org/TR/html4/appendix/notes.html#h-B.3.7). In most cases, this is a typo that you will want to fix. If you really want to use shorttags, be aware that they are not well implemented by browsers.

[✉](https://validator.w3.org/feedback.html?errmsg_id=334#errormsg "Suggest improvements on this error message through our feedback channels")

338: cannot generate system identifier for general entity X

An entity reference was found in the document, but there is no reference by that name defined. Often this is caused by misspelling the reference name, unencoded ampersands, or by leaving off the trailing semicolon (;). **The most common cause of this error is unencoded ampersands in URLs** as described by the [WDG](http://www.htmlhelp.com/) in "[Ampersands in URLs](http://www.htmlhelp.com/tools/validator/problems.html#amp)".

Entity references start with an ampersand (&) and end with a semicolon (;). If you want to use a literal ampersand in your document you must encode it as "&amp;" (_even inside URLs!_). Be careful to end entity references with a semicolon or your entity reference may get interpreted in connection with the following text. Also keep in mind that named entity references are case-sensitive; &Aelig; and &aelig; are different characters.

If this error appears in some markup generated by PHP's session handling code, [this article](http://www.w3.org/QA/2005/04/php-session "Ampersands, PHP Sessions and Valid HTML") has explanations and solutions to your problem.

Note that in most documents, errors related to entity references will trigger up to 5 separate messages from the Validator. Usually these will all disappear when the original problem is fixed.

[✉](https://validator.w3.org/feedback.html?errmsg_id=338#errormsg "Suggest improvements on this error message through our feedback channels")

344: no document type declaration; implying X
The checked page did not contain a document type ("DOCTYPE") declaration. The Validator has tried to validate with a fallback DTD, but this is quite likely to be incorrect and will generate a large number of incorrect error messages. It is highly recommended that you insert the proper DOCTYPE declaration in your document -- instructions for doing this are given above -- and it is necessary to have this declaration before the page can be declared to be valid.

[✉](https://validator.w3.org/feedback.html?errmsg_id=344#errormsg "Suggest improvements on this error message through our feedback channels")

378: no system id specified

Your document includes a DOCTYPE declaration with a public identifier (e.g. "-//W3C//DTD XHTML 1.0 Strict//EN") but no system identifier (e.g. "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"). This is authorized in HTML (based on SGML), but not in XML-based languages.

If you are using a standard XHTML document type, it is recommended to use exactly one of the DOCTYPE declarations from the [recommended list on the W3C QA Website](http://www.w3.org/QA/2002/04/valid-dtd-list.html).

[✉](https://validator.w3.org/feedback.html?errmsg_id=378#errormsg "Suggest improvements on this error message through our feedback channels")

387: S separator in comment declaration
This may happen if you have consecutive comments but did not close one of them properly. The proper syntax for comments is <!-- my comment -->.

[✉](https://validator.w3.org/feedback.html?errmsg_id=387#errormsg "Suggest improvements on this error message through our feedback channels")

394: reference not terminated by REFC delimiter
If you meant to include an entity that starts with "&", then you should terminate it with ";". Another reason for this error message is that you inadvertently created an entity by failing to escape an "&" character just before this text.

[✉](https://validator.w3.org/feedback.html?errmsg_id=394#errormsg "Suggest improvements on this error message through our feedback channels")

403: reference to external entity in attribute value
This is generally the sign of an ampersand that was not properly escaped for inclusion in an attribute, in a href for example. You will need to escape all instances of '&' into '&amp;'.

[✉](https://validator.w3.org/feedback.html?errmsg_id=403#errormsg "Suggest improvements on this error message through our feedback channels")

404: character X is the first character of a delimiter but occurred as data

This message may appear in several cases:

*   You tried to include the "<" character in your page: you should escape it as "&lt;"
*   You used an unescaped ampersand "&": this may be valid in some contexts, but it is recommended to use "&amp;", which is always safe.
*   Another possibility is that you forgot to close quotes in a previous tag.

[✉](https://validator.w3.org/feedback.html?errmsg_id=404#errormsg "Suggest improvements on this error message through our feedback channels")

407: NET-enabling start-tag not immediately followed by null end-tag
This error may occur when there is a mistake in how a self-closing tag is closed, e.g '.../ >'. The proper syntax is '... />' (note the position of the space).

[✉](https://validator.w3.org/feedback.html?errmsg_id=407#errormsg "Suggest improvements on this error message through our feedback channels")

410: reference to non-SGML character

You've included a character reference to a character that is not defined in the document type you've chosen. This is most commonly caused by numerical references to characters from vendor proprietary character repertoires. Often the culprit will be fancy or typographical quote marks from either the Windows or Macintosh character repertoires.

The solution is to reference UNICODE characters instead. A list of common characters from the Windows character repertoire and their UNICODE equivalents can be found in the document "[On the use of some MS Windows characters in HTML](http://www.cs.tut.fi/~jkorpela/www/windows-chars.html#list)" maintained by [Jukka Korpela](http://www.cs.tut.fi/~jkorpela/)<[jkorpela@cs.tut.fi](mailto:jkorpela@cs.tut.fi)>.

[✉](https://validator.w3.org/feedback.html?errmsg_id=410#errormsg "Suggest improvements on this error message through our feedback channels")

The following validation errors do not have an explanation yet. We invite you to use the [feedback channels](https://validator.w3.org/feedback.html#errormsg) to send your suggestions.

*   0: length of name must not exceed NAMELEN (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=0#errormsg "Suggest improvements on this error message through our feedback channels")

*   1: length of parameter entity name must not exceed NAMELEN less the length of the PERO delimiter (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=1#errormsg "Suggest improvements on this error message through our feedback channels")

*   2: length of number must not exceed NAMELEN (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=2#errormsg "Suggest improvements on this error message through our feedback channels")

*   3: length of attribute value must not exceed LITLEN less NORMSEP (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=3#errormsg "Suggest improvements on this error message through our feedback channels")

*   4: a name group is not allowed in a parameter entity reference in the prolog [✉](https://validator.w3.org/feedback.html?errmsg_id=4#errormsg "Suggest improvements on this error message through our feedback channels")

*   5: an entity end in a token separator must terminate an entity referenced in the same group [✉](https://validator.w3.org/feedback.html?errmsg_id=5#errormsg "Suggest improvements on this error message through our feedback channels")

*   6: character X invalid: only Y and token separators allowed [✉](https://validator.w3.org/feedback.html?errmsg_id=6#errormsg "Suggest improvements on this error message through our feedback channels")

*   7: a parameter separator is required after a number that is followed by a name start character [✉](https://validator.w3.org/feedback.html?errmsg_id=7#errormsg "Suggest improvements on this error message through our feedback channels")

*   8: character X invalid: only Y and parameter separators allowed [✉](https://validator.w3.org/feedback.html?errmsg_id=8#errormsg "Suggest improvements on this error message through our feedback channels")

*   9: an entity end in a parameter separator must terminate an entity referenced in the same declaration [✉](https://validator.w3.org/feedback.html?errmsg_id=9#errormsg "Suggest improvements on this error message through our feedback channels")

*   10: an entity end is not allowed in a token separator that does not follow a token [✉](https://validator.w3.org/feedback.html?errmsg_id=10#errormsg "Suggest improvements on this error message through our feedback channels")

*   11: X is not a valid token here [✉](https://validator.w3.org/feedback.html?errmsg_id=11#errormsg "Suggest improvements on this error message through our feedback channels")

*   12: a parameter entity reference can only occur in a group where a token could occur [✉](https://validator.w3.org/feedback.html?errmsg_id=12#errormsg "Suggest improvements on this error message through our feedback channels")

*   13: token X has already occurred in this group [✉](https://validator.w3.org/feedback.html?errmsg_id=13#errormsg "Suggest improvements on this error message through our feedback channels")

*   14: the number of tokens in a group must not exceed GRPCNT (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=14#errormsg "Suggest improvements on this error message through our feedback channels")

*   15: an entity end in a literal must terminate an entity referenced in the same literal [✉](https://validator.w3.org/feedback.html?errmsg_id=15#errormsg "Suggest improvements on this error message through our feedback channels")

*   16: character X invalid: only minimum data characters allowed [✉](https://validator.w3.org/feedback.html?errmsg_id=16#errormsg "Suggest improvements on this error message through our feedback channels")

*   18: a parameter literal in a data tag pattern must not contain a numeric character reference to a non-SGML character [✉](https://validator.w3.org/feedback.html?errmsg_id=18#errormsg "Suggest improvements on this error message through our feedback channels")

*   19: a parameter literal in a data tag pattern must not contain a numeric character reference to a function character [✉](https://validator.w3.org/feedback.html?errmsg_id=19#errormsg "Suggest improvements on this error message through our feedback channels")

*   20: a name group is not allowed in a general entity reference in a start tag [✉](https://validator.w3.org/feedback.html?errmsg_id=20#errormsg "Suggest improvements on this error message through our feedback channels")

*   21: a name group is not allowed in a general entity reference in the prolog [✉](https://validator.w3.org/feedback.html?errmsg_id=21#errormsg "Suggest improvements on this error message through our feedback channels")

*   22: X is not a function name [✉](https://validator.w3.org/feedback.html?errmsg_id=22#errormsg "Suggest improvements on this error message through our feedback channels")

*   23: X is not a character number in the document character set [✉](https://validator.w3.org/feedback.html?errmsg_id=23#errormsg "Suggest improvements on this error message through our feedback channels")

*   24: parameter entity X not defined [✉](https://validator.w3.org/feedback.html?errmsg_id=24#errormsg "Suggest improvements on this error message through our feedback channels")

*   26: RNI delimiter must be followed by name start character [✉](https://validator.w3.org/feedback.html?errmsg_id=26#errormsg "Suggest improvements on this error message through our feedback channels")

*   29: comment started here [✉](https://validator.w3.org/feedback.html?errmsg_id=29#errormsg "Suggest improvements on this error message through our feedback channels")

*   30: only one type of connector should be used in a single group [✉](https://validator.w3.org/feedback.html?errmsg_id=30#errormsg "Suggest improvements on this error message through our feedback channels")

*   31: X is not a reserved name [✉](https://validator.w3.org/feedback.html?errmsg_id=31#errormsg "Suggest improvements on this error message through our feedback channels")

*   32: X is not allowed as a reserved name here [✉](https://validator.w3.org/feedback.html?errmsg_id=32#errormsg "Suggest improvements on this error message through our feedback channels")

*   33: length of interpreted minimum literal must not exceed reference LITLEN (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=33#errormsg "Suggest improvements on this error message through our feedback channels")

*   34: length of tokenized attribute value must not exceed LITLEN less NORMSEP (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=34#errormsg "Suggest improvements on this error message through our feedback channels")

*   35: length of system identifier must not exceed LITLEN (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=35#errormsg "Suggest improvements on this error message through our feedback channels")

*   36: length of interpreted parameter literal must not exceed LITLEN (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=36#errormsg "Suggest improvements on this error message through our feedback channels")

*   37: length of interpreted parameter literal in data tag pattern must not exceed DTEMPLEN (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=37#errormsg "Suggest improvements on this error message through our feedback channels")

*   39: X invalid: only Y and parameter separators are allowed [✉](https://validator.w3.org/feedback.html?errmsg_id=39#errormsg "Suggest improvements on this error message through our feedback channels")

*   40: X invalid: only Y and token separators are allowed [✉](https://validator.w3.org/feedback.html?errmsg_id=40#errormsg "Suggest improvements on this error message through our feedback channels")

*   41: X invalid: only Y and token separators are allowed [✉](https://validator.w3.org/feedback.html?errmsg_id=41#errormsg "Suggest improvements on this error message through our feedback channels")

*   43: X declaration not allowed in DTD subset [✉](https://validator.w3.org/feedback.html?errmsg_id=43#errormsg "Suggest improvements on this error message through our feedback channels")

*   44: character X not allowed in declaration subset [✉](https://validator.w3.org/feedback.html?errmsg_id=44#errormsg "Suggest improvements on this error message through our feedback channels")

*   45: end of document in DTD subset [✉](https://validator.w3.org/feedback.html?errmsg_id=45#errormsg "Suggest improvements on this error message through our feedback channels")

*   46: character X not allowed in prolog [✉](https://validator.w3.org/feedback.html?errmsg_id=46#errormsg "Suggest improvements on this error message through our feedback channels")

*   48: X declaration not allowed in prolog [✉](https://validator.w3.org/feedback.html?errmsg_id=48#errormsg "Suggest improvements on this error message through our feedback channels")

*   49: X used both a rank stem and generic identifier [✉](https://validator.w3.org/feedback.html?errmsg_id=49#errormsg "Suggest improvements on this error message through our feedback channels")

*   50: omitted tag minimization parameter can be omitted only if OMITTAG NO is specified [✉](https://validator.w3.org/feedback.html?errmsg_id=50#errormsg "Suggest improvements on this error message through our feedback channels")

*   51: element type X already defined [✉](https://validator.w3.org/feedback.html?errmsg_id=51#errormsg "Suggest improvements on this error message through our feedback channels")

*   52: entity reference with no applicable DTD [✉](https://validator.w3.org/feedback.html?errmsg_id=52#errormsg "Suggest improvements on this error message through our feedback channels")

*   53: invalid comment declaration: found X outside comment but inside comment declaration [✉](https://validator.w3.org/feedback.html?errmsg_id=53#errormsg "Suggest improvements on this error message through our feedback channels")

*   54: comment declaration started here [✉](https://validator.w3.org/feedback.html?errmsg_id=54#errormsg "Suggest improvements on this error message through our feedback channels")

*   55: X declaration not allowed in instance [✉](https://validator.w3.org/feedback.html?errmsg_id=55#errormsg "Suggest improvements on this error message through our feedback channels")

*   56: non-SGML character not allowed in content [✉](https://validator.w3.org/feedback.html?errmsg_id=56#errormsg "Suggest improvements on this error message through our feedback channels")

*   57: no current rank for rank stem X [✉](https://validator.w3.org/feedback.html?errmsg_id=57#errormsg "Suggest improvements on this error message through our feedback channels")

*   58: duplicate attribute definition list for notation X [✉](https://validator.w3.org/feedback.html?errmsg_id=58#errormsg "Suggest improvements on this error message through our feedback channels")

*   59: duplicate attribute definition list for element X [✉](https://validator.w3.org/feedback.html?errmsg_id=59#errormsg "Suggest improvements on this error message through our feedback channels")

*   60: entity end not allowed in end tag [✉](https://validator.w3.org/feedback.html?errmsg_id=60#errormsg "Suggest improvements on this error message through our feedback channels")

*   61: character X not allowed in end tag [✉](https://validator.w3.org/feedback.html?errmsg_id=61#errormsg "Suggest improvements on this error message through our feedback channels")

*   62: X invalid: only S separators and TAGC allowed here [✉](https://validator.w3.org/feedback.html?errmsg_id=62#errormsg "Suggest improvements on this error message through our feedback channels")

*   66: document type does not allow element X here; assuming missing Y start-tag [✉](https://validator.w3.org/feedback.html?errmsg_id=66#errormsg "Suggest improvements on this error message through our feedback channels")

*   67: no start tag specified for implied empty element X [✉](https://validator.w3.org/feedback.html?errmsg_id=67#errormsg "Suggest improvements on this error message through our feedback channels")

*   72: start tag omitted for element X with declared content [✉](https://validator.w3.org/feedback.html?errmsg_id=72#errormsg "Suggest improvements on this error message through our feedback channels")

*   74: start tag for X omitted, but its declaration does not permit this [✉](https://validator.w3.org/feedback.html?errmsg_id=74#errormsg "Suggest improvements on this error message through our feedback channels")

*   75: number of open elements exceeds TAGLVL (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=75#errormsg "Suggest improvements on this error message through our feedback channels")

*   77: empty end tag but no open elements [✉](https://validator.w3.org/feedback.html?errmsg_id=77#errormsg "Suggest improvements on this error message through our feedback channels")

*   78: X not finished but containing element ended [✉](https://validator.w3.org/feedback.html?errmsg_id=78#errormsg "Suggest improvements on this error message through our feedback channels")

*   80: internal parameter entity X cannot be CDATA or SDATA [✉](https://validator.w3.org/feedback.html?errmsg_id=80#errormsg "Suggest improvements on this error message through our feedback channels")

*   81: character X not allowed in attribute specification list [✉](https://validator.w3.org/feedback.html?errmsg_id=81#errormsg "Suggest improvements on this error message through our feedback channels")

*   83: entity end not allowed in attribute specification list except in attribute value literal [✉](https://validator.w3.org/feedback.html?errmsg_id=83#errormsg "Suggest improvements on this error message through our feedback channels")

*   84: external parameter entity X cannot be CDATA, SDATA, NDATA or SUBDOC [✉](https://validator.w3.org/feedback.html?errmsg_id=84#errormsg "Suggest improvements on this error message through our feedback channels")

*   85: duplicate declaration of entity X [✉](https://validator.w3.org/feedback.html?errmsg_id=85#errormsg "Suggest improvements on this error message through our feedback channels")

*   86: duplicate declaration of parameter entity X [✉](https://validator.w3.org/feedback.html?errmsg_id=86#errormsg "Suggest improvements on this error message through our feedback channels")

*   87: a reference to a PI entity is allowed only in a context where a processing instruction could occur [✉](https://validator.w3.org/feedback.html?errmsg_id=87#errormsg "Suggest improvements on this error message through our feedback channels")

*   88: a reference to a CDATA or SDATA entity is allowed only in a context where a data character could occur [✉](https://validator.w3.org/feedback.html?errmsg_id=88#errormsg "Suggest improvements on this error message through our feedback channels")

*   89: a reference to a subdocument entity or external data entity is allowed only in a context where a data character could occur [✉](https://validator.w3.org/feedback.html?errmsg_id=89#errormsg "Suggest improvements on this error message through our feedback channels")

*   90: a reference to a subdocument entity or external data entity is not allowed in replaceable character data [✉](https://validator.w3.org/feedback.html?errmsg_id=90#errormsg "Suggest improvements on this error message through our feedback channels")

*   91: the number of open entities cannot exceed ENTLVL (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=91#errormsg "Suggest improvements on this error message through our feedback channels")

*   92: a reference to a PI entity is not allowed in replaceable character data [✉](https://validator.w3.org/feedback.html?errmsg_id=92#errormsg "Suggest improvements on this error message through our feedback channels")

*   93: entity X is already open [✉](https://validator.w3.org/feedback.html?errmsg_id=93#errormsg "Suggest improvements on this error message through our feedback channels")

*   94: short reference map X not defined [✉](https://validator.w3.org/feedback.html?errmsg_id=94#errormsg "Suggest improvements on this error message through our feedback channels")

*   95: short reference map in DTD must specify associated element type [✉](https://validator.w3.org/feedback.html?errmsg_id=95#errormsg "Suggest improvements on this error message through our feedback channels")

*   96: short reference map in document instance cannot specify associated element type [✉](https://validator.w3.org/feedback.html?errmsg_id=96#errormsg "Suggest improvements on this error message through our feedback channels")

*   97: short reference map X for element Y not defined in DTD [✉](https://validator.w3.org/feedback.html?errmsg_id=97#errormsg "Suggest improvements on this error message through our feedback channels")

*   98: X is not a short reference delimiter [✉](https://validator.w3.org/feedback.html?errmsg_id=98#errormsg "Suggest improvements on this error message through our feedback channels")

*   99: short reference delimiter X already mapped in this declaration [✉](https://validator.w3.org/feedback.html?errmsg_id=99#errormsg "Suggest improvements on this error message through our feedback channels")

*   100: no document element [✉](https://validator.w3.org/feedback.html?errmsg_id=100#errormsg "Suggest improvements on this error message through our feedback channels")

*   102: entity end not allowed in processing instruction [✉](https://validator.w3.org/feedback.html?errmsg_id=102#errormsg "Suggest improvements on this error message through our feedback channels")

*   103: length of processing instruction must not exceed PILEN (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=103#errormsg "Suggest improvements on this error message through our feedback channels")

*   104: missing PIC delimiter [✉](https://validator.w3.org/feedback.html?errmsg_id=104#errormsg "Suggest improvements on this error message through our feedback channels")

*   106: X is not a member of a group specified for any attribute [✉](https://validator.w3.org/feedback.html?errmsg_id=106#errormsg "Suggest improvements on this error message through our feedback channels")

*   109: an attribute value specification must start with a literal or a name character [✉](https://validator.w3.org/feedback.html?errmsg_id=109#errormsg "Suggest improvements on this error message through our feedback channels")

*   110: length of name token must not exceed NAMELEN (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=110#errormsg "Suggest improvements on this error message through our feedback channels")

*   113: duplicate definition of attribute X [✉](https://validator.w3.org/feedback.html?errmsg_id=113#errormsg "Suggest improvements on this error message through our feedback channels")

*   114: data attribute specification must be omitted if attribute specification list is empty [✉](https://validator.w3.org/feedback.html?errmsg_id=114#errormsg "Suggest improvements on this error message through our feedback channels")

*   115: marked section end not in marked section declaration [✉](https://validator.w3.org/feedback.html?errmsg_id=115#errormsg "Suggest improvements on this error message through our feedback channels")

*   116: number of open marked sections must not exceed TAGLVL (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=116#errormsg "Suggest improvements on this error message through our feedback channels")

*   117: missing marked section end [✉](https://validator.w3.org/feedback.html?errmsg_id=117#errormsg "Suggest improvements on this error message through our feedback channels")

*   118: marked section started here [✉](https://validator.w3.org/feedback.html?errmsg_id=118#errormsg "Suggest improvements on this error message through our feedback channels")

*   119: entity end in character data, replaceable character data or ignored marked section [✉](https://validator.w3.org/feedback.html?errmsg_id=119#errormsg "Suggest improvements on this error message through our feedback channels")

*   126: non-impliable attribute X not specified but OMITTAG NO and SHORTTAG NO [✉](https://validator.w3.org/feedback.html?errmsg_id=126#errormsg "Suggest improvements on this error message through our feedback channels")

*   128: first occurrence of CURRENT attribute X not specified [✉](https://validator.w3.org/feedback.html?errmsg_id=128#errormsg "Suggest improvements on this error message through our feedback channels")

*   129: X is not a notation name [✉](https://validator.w3.org/feedback.html?errmsg_id=129#errormsg "Suggest improvements on this error message through our feedback channels")

*   130: X is not a general entity name [✉](https://validator.w3.org/feedback.html?errmsg_id=130#errormsg "Suggest improvements on this error message through our feedback channels")

*   132: X is not a data or subdocument entity [✉](https://validator.w3.org/feedback.html?errmsg_id=132#errormsg "Suggest improvements on this error message through our feedback channels")

*   133: content model is ambiguous: when no tokens have been matched, both the Y and Z occurrences of X are possible [✉](https://validator.w3.org/feedback.html?errmsg_id=133#errormsg "Suggest improvements on this error message through our feedback channels")

*   134: content model is ambiguous: when the current token is the Y occurrence of X, both the a and b occurrences of Z are possible [✉](https://validator.w3.org/feedback.html?errmsg_id=134#errormsg "Suggest improvements on this error message through our feedback channels")

*   135: content model is ambiguous: when the current token is the Y occurrence of X and the innermost containing AND group has been matched, both the a and b occurrences of Z are possible [✉](https://validator.w3.org/feedback.html?errmsg_id=135#errormsg "Suggest improvements on this error message through our feedback channels")

*   136: content model is ambiguous: when the current token is the Y occurrence of X and the innermost Z containing AND groups have been matched, both the b and c occurrences of a are possible [✉](https://validator.w3.org/feedback.html?errmsg_id=136#errormsg "Suggest improvements on this error message through our feedback channels")

*   138: comment declaration started here [✉](https://validator.w3.org/feedback.html?errmsg_id=138#errormsg "Suggest improvements on this error message through our feedback channels")

*   140: data or replaceable character data in declaration subset [✉](https://validator.w3.org/feedback.html?errmsg_id=140#errormsg "Suggest improvements on this error message through our feedback channels")

*   142: ID X first defined here [✉](https://validator.w3.org/feedback.html?errmsg_id=142#errormsg "Suggest improvements on this error message through our feedback channels")

*   143: value of fixed attribute X not equal to default [✉](https://validator.w3.org/feedback.html?errmsg_id=143#errormsg "Suggest improvements on this error message through our feedback channels")

*   144: character X is not significant in the reference concrete syntax and so cannot occur in a comment in the SGML declaration [✉](https://validator.w3.org/feedback.html?errmsg_id=144#errormsg "Suggest improvements on this error message through our feedback channels")

*   145: minimum data of first minimum literal in SGML declaration must be ""ISO 8879:1986"" or ""ISO 8879:1986 (ENR)"" or ""ISO 8879:1986 (WWW)"" not X [✉](https://validator.w3.org/feedback.html?errmsg_id=145#errormsg "Suggest improvements on this error message through our feedback channels")

*   146: parameter before LCNMSTRT must be NAMING not X [✉](https://validator.w3.org/feedback.html?errmsg_id=146#errormsg "Suggest improvements on this error message through our feedback channels")

*   147: unexpected entity end in SGML declaration: only X, S separators and comments allowed [✉](https://validator.w3.org/feedback.html?errmsg_id=147#errormsg "Suggest improvements on this error message through our feedback channels")

*   148: X invalid: only Y and parameter separators allowed [✉](https://validator.w3.org/feedback.html?errmsg_id=148#errormsg "Suggest improvements on this error message through our feedback channels")

*   149: magnitude of X too big [✉](https://validator.w3.org/feedback.html?errmsg_id=149#errormsg "Suggest improvements on this error message through our feedback channels")

*   150: character X is not significant in the reference concrete syntax and so cannot occur in a literal in the SGML declaration except as the replacement of a character reference [✉](https://validator.w3.org/feedback.html?errmsg_id=150#errormsg "Suggest improvements on this error message through our feedback channels")

*   151: X is not a valid syntax reference character number [✉](https://validator.w3.org/feedback.html?errmsg_id=151#errormsg "Suggest improvements on this error message through our feedback channels")

*   152: a parameter entity reference cannot occur in an SGML declaration [✉](https://validator.w3.org/feedback.html?errmsg_id=152#errormsg "Suggest improvements on this error message through our feedback channels")

*   153: X invalid: only Y and parameter separators are allowed [✉](https://validator.w3.org/feedback.html?errmsg_id=153#errormsg "Suggest improvements on this error message through our feedback channels")

*   154: cannot continue because of previous errors [✉](https://validator.w3.org/feedback.html?errmsg_id=154#errormsg "Suggest improvements on this error message through our feedback channels")

*   155: SGML declaration cannot be parsed because the character set does not contain characters having the following numbers in ISO 646: X [✉](https://validator.w3.org/feedback.html?errmsg_id=155#errormsg "Suggest improvements on this error message through our feedback channels")

*   156: the specified character set is invalid because it does not contain the minimum data characters having the following numbers in ISO 646: X [✉](https://validator.w3.org/feedback.html?errmsg_id=156#errormsg "Suggest improvements on this error message through our feedback channels")

*   157: character numbers declared more than once: X [✉](https://validator.w3.org/feedback.html?errmsg_id=157#errormsg "Suggest improvements on this error message through our feedback channels")

*   158: character numbers should have been declared UNUSED: X [✉](https://validator.w3.org/feedback.html?errmsg_id=158#errormsg "Suggest improvements on this error message through our feedback channels")

*   159: character numbers missing in base set: X [✉](https://validator.w3.org/feedback.html?errmsg_id=159#errormsg "Suggest improvements on this error message through our feedback channels")

*   160: characters in the document character set with numbers exceeding X not supported [✉](https://validator.w3.org/feedback.html?errmsg_id=160#errormsg "Suggest improvements on this error message through our feedback channels")

*   161: invalid formal public identifier X: missing // [✉](https://validator.w3.org/feedback.html?errmsg_id=161#errormsg "Suggest improvements on this error message through our feedback channels")

*   162: invalid formal public identifier X: no SPACE after public text class [✉](https://validator.w3.org/feedback.html?errmsg_id=162#errormsg "Suggest improvements on this error message through our feedback channels")

*   163: invalid formal public identifier X: invalid public text class [✉](https://validator.w3.org/feedback.html?errmsg_id=163#errormsg "Suggest improvements on this error message through our feedback channels")

*   164: invalid formal public identifier X: public text language must be a name containing only upper case letters [✉](https://validator.w3.org/feedback.html?errmsg_id=164#errormsg "Suggest improvements on this error message through our feedback channels")

*   165: invalid formal public identifer X: public text display version not permitted with this text class [✉](https://validator.w3.org/feedback.html?errmsg_id=165#errormsg "Suggest improvements on this error message through our feedback channels")

*   166: invalid formal public identifier X: extra field [✉](https://validator.w3.org/feedback.html?errmsg_id=166#errormsg "Suggest improvements on this error message through our feedback channels")

*   167: public text class of public identifier in notation identifier must be NOTATION [✉](https://validator.w3.org/feedback.html?errmsg_id=167#errormsg "Suggest improvements on this error message through our feedback channels")

*   168: base character set X is unknown [✉](https://validator.w3.org/feedback.html?errmsg_id=168#errormsg "Suggest improvements on this error message through our feedback channels")

*   169: delimiter set is ambiguous: X and Y can be recognized in the same mode [✉](https://validator.w3.org/feedback.html?errmsg_id=169#errormsg "Suggest improvements on this error message through our feedback channels")

*   170: characters with the following numbers in the syntax reference character set are significant in the concrete syntax but are not in the document character set: X [✉](https://validator.w3.org/feedback.html?errmsg_id=170#errormsg "Suggest improvements on this error message through our feedback channels")

*   171: there is no unique character in the document character set corresponding to character number X in the syntax reference character set [✉](https://validator.w3.org/feedback.html?errmsg_id=171#errormsg "Suggest improvements on this error message through our feedback channels")

*   172: there is no unique character in the internal character set corresponding to character number X in the syntax reference character set [✉](https://validator.w3.org/feedback.html?errmsg_id=172#errormsg "Suggest improvements on this error message through our feedback channels")

*   173: the character with number X in ISO 646 is significant but has no representation in the syntax reference character set [✉](https://validator.w3.org/feedback.html?errmsg_id=173#errormsg "Suggest improvements on this error message through our feedback channels")

*   174: capacity set X is unknown [✉](https://validator.w3.org/feedback.html?errmsg_id=174#errormsg "Suggest improvements on this error message through our feedback channels")

*   175: capacity X already specified [✉](https://validator.w3.org/feedback.html?errmsg_id=175#errormsg "Suggest improvements on this error message through our feedback channels")

*   176: value of capacity X exceeds value of TOTALCAP [✉](https://validator.w3.org/feedback.html?errmsg_id=176#errormsg "Suggest improvements on this error message through our feedback channels")

*   177: syntax X is unknown [✉](https://validator.w3.org/feedback.html?errmsg_id=177#errormsg "Suggest improvements on this error message through our feedback channels")

*   178: UCNMSTRT must have the same number of characters as LCNMSTRT [✉](https://validator.w3.org/feedback.html?errmsg_id=178#errormsg "Suggest improvements on this error message through our feedback channels")

*   179: UCNMCHAR must have the same number of characters as LCNMCHAR [✉](https://validator.w3.org/feedback.html?errmsg_id=179#errormsg "Suggest improvements on this error message through our feedback channels")

*   180: number of open subdocuments exceeds quantity specified for SUBDOC parameter in SGML declaration (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=180#errormsg "Suggest improvements on this error message through our feedback channels")

*   181: entity X declared SUBDOC, but SUBDOC NO specified in SGML declaration [✉](https://validator.w3.org/feedback.html?errmsg_id=181#errormsg "Suggest improvements on this error message through our feedback channels")

*   182: a parameter entity referenced in a parameter separator must end in the same declaration [✉](https://validator.w3.org/feedback.html?errmsg_id=182#errormsg "Suggest improvements on this error message through our feedback channels")

*   184: generic identifier X used in DTD but not defined [✉](https://validator.w3.org/feedback.html?errmsg_id=184#errormsg "Suggest improvements on this error message through our feedback channels")

*   185: X not finished but document ended [✉](https://validator.w3.org/feedback.html?errmsg_id=185#errormsg "Suggest improvements on this error message through our feedback channels")

*   186: cannot continue with subdocument because of previous errors [✉](https://validator.w3.org/feedback.html?errmsg_id=186#errormsg "Suggest improvements on this error message through our feedback channels")

*   188: no internal or external document type declaration subset; will parse without validation [✉](https://validator.w3.org/feedback.html?errmsg_id=188#errormsg "Suggest improvements on this error message through our feedback channels")

*   189: this is not an SGML document [✉](https://validator.w3.org/feedback.html?errmsg_id=189#errormsg "Suggest improvements on this error message through our feedback channels")

*   190: length of start-tag before interpretation of literals must not exceed TAGLEN (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=190#errormsg "Suggest improvements on this error message through our feedback channels")

*   191: a parameter entity referenced in a token separator must end in the same group [✉](https://validator.w3.org/feedback.html?errmsg_id=191#errormsg "Suggest improvements on this error message through our feedback channels")

*   192: the following character numbers are shunned characters that are not significant and so should have been declared UNUSED: X [✉](https://validator.w3.org/feedback.html?errmsg_id=192#errormsg "Suggest improvements on this error message through our feedback channels")

*   193: there is no unique character in the specified document character set corresponding to character number X in ISO 646 [✉](https://validator.w3.org/feedback.html?errmsg_id=193#errormsg "Suggest improvements on this error message through our feedback channels")

*   194: length of attribute value must not exceed LITLEN less NORMSEP (-X) [✉](https://validator.w3.org/feedback.html?errmsg_id=194#errormsg "Suggest improvements on this error message through our feedback channels")

*   195: length of tokenized attribute value must not exceed LITLEN less NORMSEP (-X) [✉](https://validator.w3.org/feedback.html?errmsg_id=195#errormsg "Suggest improvements on this error message through our feedback channels")

*   196: concrete syntax scope is INSTANCE but value of X quantity is less than value in reference quantity set [✉](https://validator.w3.org/feedback.html?errmsg_id=196#errormsg "Suggest improvements on this error message through our feedback channels")

*   197: public text class of formal public identifier of base character set must be CHARSET [✉](https://validator.w3.org/feedback.html?errmsg_id=197#errormsg "Suggest improvements on this error message through our feedback channels")

*   198: public text class of formal public identifier of capacity set must be CAPACITY [✉](https://validator.w3.org/feedback.html?errmsg_id=198#errormsg "Suggest improvements on this error message through our feedback channels")

*   199: public text class of formal public identifier of concrete syntax must be SYNTAX [✉](https://validator.w3.org/feedback.html?errmsg_id=199#errormsg "Suggest improvements on this error message through our feedback channels")

*   200: when there is an MSOCHAR there must also be an MSICHAR [✉](https://validator.w3.org/feedback.html?errmsg_id=200#errormsg "Suggest improvements on this error message through our feedback channels")

*   201: character number X in the syntax reference character set was specified as a character to be switched but is not a markup character [✉](https://validator.w3.org/feedback.html?errmsg_id=201#errormsg "Suggest improvements on this error message through our feedback channels")

*   202: character number X was specified as a character to be switched but is not in the syntax reference character set [✉](https://validator.w3.org/feedback.html?errmsg_id=202#errormsg "Suggest improvements on this error message through our feedback channels")

*   203: character numbers X in the document character set have been assigned the same meaning, but this is the meaning of a significant character [✉](https://validator.w3.org/feedback.html?errmsg_id=203#errormsg "Suggest improvements on this error message through our feedback channels")

*   204: character number X assigned to more than one function [✉](https://validator.w3.org/feedback.html?errmsg_id=204#errormsg "Suggest improvements on this error message through our feedback channels")

*   205: X is already a function name [✉](https://validator.w3.org/feedback.html?errmsg_id=205#errormsg "Suggest improvements on this error message through our feedback channels")

*   206: characters with the following numbers in ISO 646 are significant in the concrete syntax but are not in the document character set: X [✉](https://validator.w3.org/feedback.html?errmsg_id=206#errormsg "Suggest improvements on this error message through our feedback channels")

*   207: general delimiter X consists solely of function characters [✉](https://validator.w3.org/feedback.html?errmsg_id=207#errormsg "Suggest improvements on this error message through our feedback channels")

*   208: letters assigned to LCNMCHAR, UCNMCHAR, LCNMSTRT or UCNMSTRT: X [✉](https://validator.w3.org/feedback.html?errmsg_id=208#errormsg "Suggest improvements on this error message through our feedback channels")

*   209: digits assigned to LCNMCHAR, UCNMCHAR, LCNMSTRT or UCNMSTRT: X [✉](https://validator.w3.org/feedback.html?errmsg_id=209#errormsg "Suggest improvements on this error message through our feedback channels")

*   210: character number X cannot be assigned to LCNMCHAR, UCNMCHAR, LCNMSTRT or UCNMSTRT because it is RE [✉](https://validator.w3.org/feedback.html?errmsg_id=210#errormsg "Suggest improvements on this error message through our feedback channels")

*   211: character number X cannot be assigned to LCNMCHAR, UCNMCHAR, LCNMSTRT or UCNMSTRT because it is RS [✉](https://validator.w3.org/feedback.html?errmsg_id=211#errormsg "Suggest improvements on this error message through our feedback channels")

*   212: character number X cannot be assigned to LCNMCHAR, UCNMCHAR, LCNMSTRT or UCNMSTRT because it is SPACE [✉](https://validator.w3.org/feedback.html?errmsg_id=212#errormsg "Suggest improvements on this error message through our feedback channels")

*   213: separator characters assigned to LCNMCHAR, UCNMCHAR, LCNMSTRT or UCNMSTRT: X [✉](https://validator.w3.org/feedback.html?errmsg_id=213#errormsg "Suggest improvements on this error message through our feedback channels")

*   214: character number X cannot be switched because it is a Digit, LC Letter or UC Letter [✉](https://validator.w3.org/feedback.html?errmsg_id=214#errormsg "Suggest improvements on this error message through our feedback channels")

*   215: pointless for number of characters to be 0 [✉](https://validator.w3.org/feedback.html?errmsg_id=215#errormsg "Suggest improvements on this error message through our feedback channels")

*   216: X cannot be the replacement for a reference reserved name because it is another reference reserved name [✉](https://validator.w3.org/feedback.html?errmsg_id=216#errormsg "Suggest improvements on this error message through our feedback channels")

*   217: X cannot be the replacement for a reference reserved name because it is the replacement of another reference reserved name [✉](https://validator.w3.org/feedback.html?errmsg_id=217#errormsg "Suggest improvements on this error message through our feedback channels")

*   218: replacement for reserved name X already specified [✉](https://validator.w3.org/feedback.html?errmsg_id=218#errormsg "Suggest improvements on this error message through our feedback channels")

*   219: X is not a valid name in the declared concrete syntax [✉](https://validator.w3.org/feedback.html?errmsg_id=219#errormsg "Suggest improvements on this error message through our feedback channels")

*   220: X is not a valid short reference delimiter because it has more than one B sequence [✉](https://validator.w3.org/feedback.html?errmsg_id=220#errormsg "Suggest improvements on this error message through our feedback channels")

*   221: X is not a valid short reference delimiter because it is adjacent to a character that can occur in a blank sequence [✉](https://validator.w3.org/feedback.html?errmsg_id=221#errormsg "Suggest improvements on this error message through our feedback channels")

*   222: length of delimiter X exceeds NAMELEN (Y) [✉](https://validator.w3.org/feedback.html?errmsg_id=222#errormsg "Suggest improvements on this error message through our feedback channels")

*   223: length of reserved name X exceeds NAMELEN (Y) [✉](https://validator.w3.org/feedback.html?errmsg_id=223#errormsg "Suggest improvements on this error message through our feedback channels")

*   224: character numbers assigned to both LCNMCHAR or UCNMCHAR and LCNMSTRT or UCNMSTRT: X [✉](https://validator.w3.org/feedback.html?errmsg_id=224#errormsg "Suggest improvements on this error message through our feedback channels")

*   225: when the concrete syntax scope is INSTANCE the syntax reference character set of the declared syntax must be the same as that of the reference concrete syntax [✉](https://validator.w3.org/feedback.html?errmsg_id=225#errormsg "Suggest improvements on this error message through our feedback channels")

*   226: end-tag minimization should be O for element with declared content of EMPTY [✉](https://validator.w3.org/feedback.html?errmsg_id=226#errormsg "Suggest improvements on this error message through our feedback channels")

*   227: end-tag minimization should be O for element X because it has CONREF attribute [✉](https://validator.w3.org/feedback.html?errmsg_id=227#errormsg "Suggest improvements on this error message through our feedback channels")

*   228: element X has a declared content of EMPTY and a CONREF attribute [✉](https://validator.w3.org/feedback.html?errmsg_id=228#errormsg "Suggest improvements on this error message through our feedback channels")

*   229: element X has a declared content of EMPTY and a NOTATION attribute [✉](https://validator.w3.org/feedback.html?errmsg_id=229#errormsg "Suggest improvements on this error message through our feedback channels")

*   230: declared value of data attribute cannot be ENTITY, ENTITIES, ID, IDREF, IDREFS or NOTATION [✉](https://validator.w3.org/feedback.html?errmsg_id=230#errormsg "Suggest improvements on this error message through our feedback channels")

*   231: default value of data attribute cannot be CONREF or CURRENT [✉](https://validator.w3.org/feedback.html?errmsg_id=231#errormsg "Suggest improvements on this error message through our feedback channels")

*   232: number of attribute names and name tokens (X) exceeds ATTCNT (Y) [✉](https://validator.w3.org/feedback.html?errmsg_id=232#errormsg "Suggest improvements on this error message through our feedback channels")

*   233: if the declared value is ID the default value must be IMPLIED or REQUIRED [✉](https://validator.w3.org/feedback.html?errmsg_id=233#errormsg "Suggest improvements on this error message through our feedback channels")

*   234: the attribute definition list already declared attribute X as the ID attribute [✉](https://validator.w3.org/feedback.html?errmsg_id=234#errormsg "Suggest improvements on this error message through our feedback channels")

*   235: the attribute definition list already declared attribute X as the NOTATION attribute [✉](https://validator.w3.org/feedback.html?errmsg_id=235#errormsg "Suggest improvements on this error message through our feedback channels")

*   236: token X occurs more than once in attribute definition list [✉](https://validator.w3.org/feedback.html?errmsg_id=236#errormsg "Suggest improvements on this error message through our feedback channels")

*   237: no attributes defined for notation X [✉](https://validator.w3.org/feedback.html?errmsg_id=237#errormsg "Suggest improvements on this error message through our feedback channels")

*   238: notation X for entity Y undefined [✉](https://validator.w3.org/feedback.html?errmsg_id=238#errormsg "Suggest improvements on this error message through our feedback channels")

*   239: entity X undefined in short reference map Y [✉](https://validator.w3.org/feedback.html?errmsg_id=239#errormsg "Suggest improvements on this error message through our feedback channels")

*   240: notation X is undefined but had attribute definition [✉](https://validator.w3.org/feedback.html?errmsg_id=240#errormsg "Suggest improvements on this error message through our feedback channels")

*   241: length of interpreted parameter literal in bracketed text plus the length of the bracketing delimiters must not exceed LITLEN (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=241#errormsg "Suggest improvements on this error message through our feedback channels")

*   242: length of rank stem plus length of rank suffix must not exceed NAMELEN (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=242#errormsg "Suggest improvements on this error message through our feedback channels")

*   243: document instance must start with document element [✉](https://validator.w3.org/feedback.html?errmsg_id=243#errormsg "Suggest improvements on this error message through our feedback channels")

*   244: content model nesting level exceeds GRPLVL (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=244#errormsg "Suggest improvements on this error message through our feedback channels")

*   245: grand total of content tokens exceeds GRPGTCNT (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=245#errormsg "Suggest improvements on this error message through our feedback channels")

*   249: DTDs other than base allowed only if CONCUR YES or EXPLICIT YES [✉](https://validator.w3.org/feedback.html?errmsg_id=249#errormsg "Suggest improvements on this error message through our feedback channels")

*   250: end of entity other than document entity after document element [✉](https://validator.w3.org/feedback.html?errmsg_id=250#errormsg "Suggest improvements on this error message through our feedback channels")

*   251: X declaration illegal after document element [✉](https://validator.w3.org/feedback.html?errmsg_id=251#errormsg "Suggest improvements on this error message through our feedback channels")

*   252: character reference illegal after document element [✉](https://validator.w3.org/feedback.html?errmsg_id=252#errormsg "Suggest improvements on this error message through our feedback channels")

*   253: entity reference illegal after document element [✉](https://validator.w3.org/feedback.html?errmsg_id=253#errormsg "Suggest improvements on this error message through our feedback channels")

*   254: marked section illegal after document element [✉](https://validator.w3.org/feedback.html?errmsg_id=254#errormsg "Suggest improvements on this error message through our feedback channels")

*   255: the X occurrence of Y in the content model for Z cannot be excluded at this point because it is contextually required [✉](https://validator.w3.org/feedback.html?errmsg_id=255#errormsg "Suggest improvements on this error message through our feedback channels")

*   256: the X occurrence of Y in the content model for Z cannot be excluded because it is neither inherently optional nor a member of an OR group [✉](https://validator.w3.org/feedback.html?errmsg_id=256#errormsg "Suggest improvements on this error message through our feedback channels")

*   257: an attribute value specification must be an attribute value literal unless SHORTTAG YES is specified [✉](https://validator.w3.org/feedback.html?errmsg_id=257#errormsg "Suggest improvements on this error message through our feedback channels")

*   258: value cannot be specified both for notation attribute and content reference attribute [✉](https://validator.w3.org/feedback.html?errmsg_id=258#errormsg "Suggest improvements on this error message through our feedback channels")

*   259: notation X already defined [✉](https://validator.w3.org/feedback.html?errmsg_id=259#errormsg "Suggest improvements on this error message through our feedback channels")

*   260: short reference map X already defined [✉](https://validator.w3.org/feedback.html?errmsg_id=260#errormsg "Suggest improvements on this error message through our feedback channels")

*   261: first defined here [✉](https://validator.w3.org/feedback.html?errmsg_id=261#errormsg "Suggest improvements on this error message through our feedback channels")

*   262: general delimiter role X already defined [✉](https://validator.w3.org/feedback.html?errmsg_id=262#errormsg "Suggest improvements on this error message through our feedback channels")

*   263: number of ID references in start-tag must not exceed GRPCNT (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=263#errormsg "Suggest improvements on this error message through our feedback channels")

*   264: number of entity names in attribute specification list must not exceed GRPCNT (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=264#errormsg "Suggest improvements on this error message through our feedback channels")

*   265: normalized length of attribute specification list must not exceed ATTSPLEN (X); length was Y [✉](https://validator.w3.org/feedback.html?errmsg_id=265#errormsg "Suggest improvements on this error message through our feedback channels")

*   266: short reference delimiter X already specified [✉](https://validator.w3.org/feedback.html?errmsg_id=266#errormsg "Suggest improvements on this error message through our feedback channels")

*   267: single character short references were already specified for character numbers: X [✉](https://validator.w3.org/feedback.html?errmsg_id=267#errormsg "Suggest improvements on this error message through our feedback channels")

*   268: default entity used in entity attribute X [✉](https://validator.w3.org/feedback.html?errmsg_id=268#errormsg "Suggest improvements on this error message through our feedback channels")

*   269: reference to entity X uses default entity [✉](https://validator.w3.org/feedback.html?errmsg_id=269#errormsg "Suggest improvements on this error message through our feedback channels")

*   270: entity X in short reference map Y uses default entity [✉](https://validator.w3.org/feedback.html?errmsg_id=270#errormsg "Suggest improvements on this error message through our feedback channels")

*   271: no DTD X declared [✉](https://validator.w3.org/feedback.html?errmsg_id=271#errormsg "Suggest improvements on this error message through our feedback channels")

*   272: LPD X has neither internal nor external subset [✉](https://validator.w3.org/feedback.html?errmsg_id=272#errormsg "Suggest improvements on this error message through our feedback channels")

*   273: element types have different link attribute definitions [✉](https://validator.w3.org/feedback.html?errmsg_id=273#errormsg "Suggest improvements on this error message through our feedback channels")

*   274: link set X already defined [✉](https://validator.w3.org/feedback.html?errmsg_id=274#errormsg "Suggest improvements on this error message through our feedback channels")

*   275: empty result attribute specification [✉](https://validator.w3.org/feedback.html?errmsg_id=275#errormsg "Suggest improvements on this error message through our feedback channels")

*   276: no source element type X [✉](https://validator.w3.org/feedback.html?errmsg_id=276#errormsg "Suggest improvements on this error message through our feedback channels")

*   277: no result element type X [✉](https://validator.w3.org/feedback.html?errmsg_id=277#errormsg "Suggest improvements on this error message through our feedback channels")

*   278: end of document in LPD subset [✉](https://validator.w3.org/feedback.html?errmsg_id=278#errormsg "Suggest improvements on this error message through our feedback channels")

*   279: X declaration not allowed in LPD subset [✉](https://validator.w3.org/feedback.html?errmsg_id=279#errormsg "Suggest improvements on this error message through our feedback channels")

*   280: ID link set declaration not allowed in simple link declaration subset [✉](https://validator.w3.org/feedback.html?errmsg_id=280#errormsg "Suggest improvements on this error message through our feedback channels")

*   281: link set declaration not allowed in simple link declaration subset [✉](https://validator.w3.org/feedback.html?errmsg_id=281#errormsg "Suggest improvements on this error message through our feedback channels")

*   282: attributes can only be defined for base document element (not X) in simple link declaration subset [✉](https://validator.w3.org/feedback.html?errmsg_id=282#errormsg "Suggest improvements on this error message through our feedback channels")

*   283: a short reference mapping declaration is allowed only in the base DTD [✉](https://validator.w3.org/feedback.html?errmsg_id=283#errormsg "Suggest improvements on this error message through our feedback channels")

*   284: a short reference use declaration is allowed only in the base DTD [✉](https://validator.w3.org/feedback.html?errmsg_id=284#errormsg "Suggest improvements on this error message through our feedback channels")

*   285: default value of link attribute cannot be CURRENT or CONREF [✉](https://validator.w3.org/feedback.html?errmsg_id=285#errormsg "Suggest improvements on this error message through our feedback channels")

*   286: declared value of link attribute cannot be ID, IDREF, IDREFS or NOTATION [✉](https://validator.w3.org/feedback.html?errmsg_id=286#errormsg "Suggest improvements on this error message through our feedback channels")

*   287: only fixed attributes can be defined in simple LPD [✉](https://validator.w3.org/feedback.html?errmsg_id=287#errormsg "Suggest improvements on this error message through our feedback channels")

*   288: only one ID link set declaration allowed in an LPD subset [✉](https://validator.w3.org/feedback.html?errmsg_id=288#errormsg "Suggest improvements on this error message through our feedback channels")

*   289: no initial link set defined for LPD X [✉](https://validator.w3.org/feedback.html?errmsg_id=289#errormsg "Suggest improvements on this error message through our feedback channels")

*   290: notation X not defined in source DTD [✉](https://validator.w3.org/feedback.html?errmsg_id=290#errormsg "Suggest improvements on this error message through our feedback channels")

*   291: result document type in simple link specification must be implied [✉](https://validator.w3.org/feedback.html?errmsg_id=291#errormsg "Suggest improvements on this error message through our feedback channels")

*   292: simple link requires SIMPLE YES [✉](https://validator.w3.org/feedback.html?errmsg_id=292#errormsg "Suggest improvements on this error message through our feedback channels")

*   293: implicit link requires IMPLICIT YES [✉](https://validator.w3.org/feedback.html?errmsg_id=293#errormsg "Suggest improvements on this error message through our feedback channels")

*   294: explicit link requires EXPLICIT YES [✉](https://validator.w3.org/feedback.html?errmsg_id=294#errormsg "Suggest improvements on this error message through our feedback channels")

*   295: LPD not allowed before first DTD [✉](https://validator.w3.org/feedback.html?errmsg_id=295#errormsg "Suggest improvements on this error message through our feedback channels")

*   296: DTD not allowed after an LPD [✉](https://validator.w3.org/feedback.html?errmsg_id=296#errormsg "Suggest improvements on this error message through our feedback channels")

*   297: definition of general entity X is unstable [✉](https://validator.w3.org/feedback.html?errmsg_id=297#errormsg "Suggest improvements on this error message through our feedback channels")

*   298: definition of parameter entity X is unstable [✉](https://validator.w3.org/feedback.html?errmsg_id=298#errormsg "Suggest improvements on this error message through our feedback channels")

*   299: multiple link rules for ID X but not all have link attribute specifications [✉](https://validator.w3.org/feedback.html?errmsg_id=299#errormsg "Suggest improvements on this error message through our feedback channels")

*   300: multiple link rules for element type X but not all have link attribute specifications [✉](https://validator.w3.org/feedback.html?errmsg_id=300#errormsg "Suggest improvements on this error message through our feedback channels")

*   301: link type X does not have a link set Y [✉](https://validator.w3.org/feedback.html?errmsg_id=301#errormsg "Suggest improvements on this error message through our feedback channels")

*   302: link set use declaration for simple link process [✉](https://validator.w3.org/feedback.html?errmsg_id=302#errormsg "Suggest improvements on this error message through our feedback channels")

*   303: no link type X [✉](https://validator.w3.org/feedback.html?errmsg_id=303#errormsg "Suggest improvements on this error message through our feedback channels")

*   304: both document type and link type X [✉](https://validator.w3.org/feedback.html?errmsg_id=304#errormsg "Suggest improvements on this error message through our feedback channels")

*   305: link type X already defined [✉](https://validator.w3.org/feedback.html?errmsg_id=305#errormsg "Suggest improvements on this error message through our feedback channels")

*   306: document type X already defined [✉](https://validator.w3.org/feedback.html?errmsg_id=306#errormsg "Suggest improvements on this error message through our feedback channels")

*   307: link set X used in LPD but not defined [✉](https://validator.w3.org/feedback.html?errmsg_id=307#errormsg "Suggest improvements on this error message through our feedback channels")

*   308: #IMPLIED already linked to result element type X [✉](https://validator.w3.org/feedback.html?errmsg_id=308#errormsg "Suggest improvements on this error message through our feedback channels")

*   309: number of active simple link processes exceeds quantity specified for SIMPLE parameter in SGML declaration (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=309#errormsg "Suggest improvements on this error message through our feedback channels")

*   310: only one chain of explicit link processes can be active [✉](https://validator.w3.org/feedback.html?errmsg_id=310#errormsg "Suggest improvements on this error message through our feedback channels")

*   311: source document type name for link type X must be base document type since EXPLICIT YES 1 [✉](https://validator.w3.org/feedback.html?errmsg_id=311#errormsg "Suggest improvements on this error message through our feedback channels")

*   312: only one implicit link process can be active [✉](https://validator.w3.org/feedback.html?errmsg_id=312#errormsg "Suggest improvements on this error message through our feedback channels")

*   313: sorry, link type X not activated: only one implicit or explicit link process can be active (with base document type as source document type) [✉](https://validator.w3.org/feedback.html?errmsg_id=313#errormsg "Suggest improvements on this error message through our feedback channels")

*   314: name missing after name group in entity reference [✉](https://validator.w3.org/feedback.html?errmsg_id=314#errormsg "Suggest improvements on this error message through our feedback channels")

*   315: source document type name for link type X must be base document type since EXPLICIT NO [✉](https://validator.w3.org/feedback.html?errmsg_id=315#errormsg "Suggest improvements on this error message through our feedback channels")

*   316: link process must be activated before base DTD [✉](https://validator.w3.org/feedback.html?errmsg_id=316#errormsg "Suggest improvements on this error message through our feedback channels")

*   317: unexpected entity end while starting second pass [✉](https://validator.w3.org/feedback.html?errmsg_id=317#errormsg "Suggest improvements on this error message through our feedback channels")

*   318: type X of element with ID Y not associated element type for applicable link rule in ID link set [✉](https://validator.w3.org/feedback.html?errmsg_id=318#errormsg "Suggest improvements on this error message through our feedback channels")

*   319: DATATAG feature not implemented [✉](https://validator.w3.org/feedback.html?errmsg_id=319#errormsg "Suggest improvements on this error message through our feedback channels")

*   320: generic identifier specification missing after document type specification in start-tag [✉](https://validator.w3.org/feedback.html?errmsg_id=320#errormsg "Suggest improvements on this error message through our feedback channels")

*   321: generic identifier specification missing after document type specification in end-tag [✉](https://validator.w3.org/feedback.html?errmsg_id=321#errormsg "Suggest improvements on this error message through our feedback channels")

*   322: a NET-enabling start-tag cannot include a document type specification [✉](https://validator.w3.org/feedback.html?errmsg_id=322#errormsg "Suggest improvements on this error message through our feedback channels")

*   324: invalid default SGML declaration [✉](https://validator.w3.org/feedback.html?errmsg_id=324#errormsg "Suggest improvements on this error message through our feedback channels")

*   326: entity was defined here [✉](https://validator.w3.org/feedback.html?errmsg_id=326#errormsg "Suggest improvements on this error message through our feedback channels")

*   327: content model is mixed but does not allow #PCDATA everywhere [✉](https://validator.w3.org/feedback.html?errmsg_id=327#errormsg "Suggest improvements on this error message through our feedback channels")

*   328: start or end of range must specify a single character [✉](https://validator.w3.org/feedback.html?errmsg_id=328#errormsg "Suggest improvements on this error message through our feedback channels")

*   329: number of first character in range must not exceed number of second character in range [✉](https://validator.w3.org/feedback.html?errmsg_id=329#errormsg "Suggest improvements on this error message through our feedback channels")

*   330: delimiter cannot be an empty string [✉](https://validator.w3.org/feedback.html?errmsg_id=330#errormsg "Suggest improvements on this error message through our feedback channels")

*   331: too many characters assigned same meaning with minimum literal [✉](https://validator.w3.org/feedback.html?errmsg_id=331#errormsg "Suggest improvements on this error message through our feedback channels")

*   332: earlier reference to entity X used default entity [✉](https://validator.w3.org/feedback.html?errmsg_id=332#errormsg "Suggest improvements on this error message through our feedback channels")

*   335: unused short reference map X [✉](https://validator.w3.org/feedback.html?errmsg_id=335#errormsg "Suggest improvements on this error message through our feedback channels")

*   336: unused parameter entity X [✉](https://validator.w3.org/feedback.html?errmsg_id=336#errormsg "Suggest improvements on this error message through our feedback channels")

*   337: cannot generate system identifier for public text X [✉](https://validator.w3.org/feedback.html?errmsg_id=337#errormsg "Suggest improvements on this error message through our feedback channels")

*   339: cannot generate system identifier for parameter entity X [✉](https://validator.w3.org/feedback.html?errmsg_id=339#errormsg "Suggest improvements on this error message through our feedback channels")

*   340: cannot generate system identifier for document type X [✉](https://validator.w3.org/feedback.html?errmsg_id=340#errormsg "Suggest improvements on this error message through our feedback channels")

*   341: cannot generate system identifier for link type X [✉](https://validator.w3.org/feedback.html?errmsg_id=341#errormsg "Suggest improvements on this error message through our feedback channels")

*   342: cannot generate system identifier for notation X [✉](https://validator.w3.org/feedback.html?errmsg_id=342#errormsg "Suggest improvements on this error message through our feedback channels")

*   343: element type X both included and excluded [✉](https://validator.w3.org/feedback.html?errmsg_id=343#errormsg "Suggest improvements on this error message through our feedback channels")

*   345: minimum data of AFDR declaration must be ""ISO/IEC 10744:1997"" not X [✉](https://validator.w3.org/feedback.html?errmsg_id=345#errormsg "Suggest improvements on this error message through our feedback channels")

*   346: AFDR declaration required before use of AFDR extensions [✉](https://validator.w3.org/feedback.html?errmsg_id=346#errormsg "Suggest improvements on this error message through our feedback channels")

*   347: ENR extensions were used but minimum literal was not ""ISO 8879:1986 (ENR)"" or ""ISO 8879:1986 (WWW)"" [✉](https://validator.w3.org/feedback.html?errmsg_id=347#errormsg "Suggest improvements on this error message through our feedback channels")

*   348: illegal numeric character reference to non-SGML character X in literal [✉](https://validator.w3.org/feedback.html?errmsg_id=348#errormsg "Suggest improvements on this error message through our feedback channels")

*   349: cannot convert character reference to number X because description Y unrecognized [✉](https://validator.w3.org/feedback.html?errmsg_id=349#errormsg "Suggest improvements on this error message through our feedback channels")

*   350: cannot convert character reference to number X because character Y from baseset Z unknown [✉](https://validator.w3.org/feedback.html?errmsg_id=350#errormsg "Suggest improvements on this error message through our feedback channels")

*   351: character reference to number X cannot be converted because of problem with internal character set [✉](https://validator.w3.org/feedback.html?errmsg_id=351#errormsg "Suggest improvements on this error message through our feedback channels")

*   352: cannot convert character reference to number X because character not in internal character set [✉](https://validator.w3.org/feedback.html?errmsg_id=352#errormsg "Suggest improvements on this error message through our feedback channels")

*   353: Web SGML adaptations were used but minimum literal was not ""ISO 8879:1986 (WWW)"" [✉](https://validator.w3.org/feedback.html?errmsg_id=353#errormsg "Suggest improvements on this error message through our feedback channels")

*   354: token X can be value for multiple attributes so attribute name required [✉](https://validator.w3.org/feedback.html?errmsg_id=354#errormsg "Suggest improvements on this error message through our feedback channels")

*   355: length of hex number must not exceed NAMELEN (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=355#errormsg "Suggest improvements on this error message through our feedback channels")

*   356: X is not a valid name in the declared concrete syntax [✉](https://validator.w3.org/feedback.html?errmsg_id=356#errormsg "Suggest improvements on this error message through our feedback channels")

*   357: CDATA declared content [✉](https://validator.w3.org/feedback.html?errmsg_id=357#errormsg "Suggest improvements on this error message through our feedback channels")

*   358: RCDATA declared content [✉](https://validator.w3.org/feedback.html?errmsg_id=358#errormsg "Suggest improvements on this error message through our feedback channels")

*   359: inclusion [✉](https://validator.w3.org/feedback.html?errmsg_id=359#errormsg "Suggest improvements on this error message through our feedback channels")

*   360: exclusion [✉](https://validator.w3.org/feedback.html?errmsg_id=360#errormsg "Suggest improvements on this error message through our feedback channels")

*   361: NUMBER or NUMBERS declared value [✉](https://validator.w3.org/feedback.html?errmsg_id=361#errormsg "Suggest improvements on this error message through our feedback channels")

*   362: NAME or NAMES declared value [✉](https://validator.w3.org/feedback.html?errmsg_id=362#errormsg "Suggest improvements on this error message through our feedback channels")

*   363: NUTOKEN or NUTOKENS declared value [✉](https://validator.w3.org/feedback.html?errmsg_id=363#errormsg "Suggest improvements on this error message through our feedback channels")

*   364: CONREF attribute [✉](https://validator.w3.org/feedback.html?errmsg_id=364#errormsg "Suggest improvements on this error message through our feedback channels")

*   365: CURRENT attribute [✉](https://validator.w3.org/feedback.html?errmsg_id=365#errormsg "Suggest improvements on this error message through our feedback channels")

*   366: TEMP marked section [✉](https://validator.w3.org/feedback.html?errmsg_id=366#errormsg "Suggest improvements on this error message through our feedback channels")

*   367: included marked section in the instance [✉](https://validator.w3.org/feedback.html?errmsg_id=367#errormsg "Suggest improvements on this error message through our feedback channels")

*   368: ignored marked section in the instance [✉](https://validator.w3.org/feedback.html?errmsg_id=368#errormsg "Suggest improvements on this error message through our feedback channels")

*   369: RCDATA marked section [✉](https://validator.w3.org/feedback.html?errmsg_id=369#errormsg "Suggest improvements on this error message through our feedback channels")

*   370: processing instruction entity [✉](https://validator.w3.org/feedback.html?errmsg_id=370#errormsg "Suggest improvements on this error message through our feedback channels")

*   371: bracketed text entity [✉](https://validator.w3.org/feedback.html?errmsg_id=371#errormsg "Suggest improvements on this error message through our feedback channels")

*   372: internal CDATA entity [✉](https://validator.w3.org/feedback.html?errmsg_id=372#errormsg "Suggest improvements on this error message through our feedback channels")

*   373: internal SDATA entity [✉](https://validator.w3.org/feedback.html?errmsg_id=373#errormsg "Suggest improvements on this error message through our feedback channels")

*   374: external CDATA entity [✉](https://validator.w3.org/feedback.html?errmsg_id=374#errormsg "Suggest improvements on this error message through our feedback channels")

*   375: external SDATA entity [✉](https://validator.w3.org/feedback.html?errmsg_id=375#errormsg "Suggest improvements on this error message through our feedback channels")

*   376: attribute definition list declaration for notation [✉](https://validator.w3.org/feedback.html?errmsg_id=376#errormsg "Suggest improvements on this error message through our feedback channels")

*   377: rank stem [✉](https://validator.w3.org/feedback.html?errmsg_id=377#errormsg "Suggest improvements on this error message through our feedback channels")

*   379: comment in parameter separator [✉](https://validator.w3.org/feedback.html?errmsg_id=379#errormsg "Suggest improvements on this error message through our feedback channels")

*   380: named character reference [✉](https://validator.w3.org/feedback.html?errmsg_id=380#errormsg "Suggest improvements on this error message through our feedback channels")

*   381: AND group [✉](https://validator.w3.org/feedback.html?errmsg_id=381#errormsg "Suggest improvements on this error message through our feedback channels")

*   382: attribute value not a literal [✉](https://validator.w3.org/feedback.html?errmsg_id=382#errormsg "Suggest improvements on this error message through our feedback channels")

*   383: attribute name missing [✉](https://validator.w3.org/feedback.html?errmsg_id=383#errormsg "Suggest improvements on this error message through our feedback channels")

*   384: element declaration for group of element types [✉](https://validator.w3.org/feedback.html?errmsg_id=384#errormsg "Suggest improvements on this error message through our feedback channels")

*   385: attribute definition list declaration for group of element types [✉](https://validator.w3.org/feedback.html?errmsg_id=385#errormsg "Suggest improvements on this error message through our feedback channels")

*   386: empty comment declaration [✉](https://validator.w3.org/feedback.html?errmsg_id=386#errormsg "Suggest improvements on this error message through our feedback channels")

*   388: multiple comments in comment declaration [✉](https://validator.w3.org/feedback.html?errmsg_id=388#errormsg "Suggest improvements on this error message through our feedback channels")

*   389: no status keyword [✉](https://validator.w3.org/feedback.html?errmsg_id=389#errormsg "Suggest improvements on this error message through our feedback channels")

*   390: multiple status keywords [✉](https://validator.w3.org/feedback.html?errmsg_id=390#errormsg "Suggest improvements on this error message through our feedback channels")

*   391: parameter entity reference in document instance [✉](https://validator.w3.org/feedback.html?errmsg_id=391#errormsg "Suggest improvements on this error message through our feedback channels")

*   392: CURRENT attribute [✉](https://validator.w3.org/feedback.html?errmsg_id=392#errormsg "Suggest improvements on this error message through our feedback channels")

*   393: element type minimization parameter [✉](https://validator.w3.org/feedback.html?errmsg_id=393#errormsg "Suggest improvements on this error message through our feedback channels")

*   395: #PCDATA not first in model group [✉](https://validator.w3.org/feedback.html?errmsg_id=395#errormsg "Suggest improvements on this error message through our feedback channels")

*   396: #PCDATA in SEQ group [✉](https://validator.w3.org/feedback.html?errmsg_id=396#errormsg "Suggest improvements on this error message through our feedback channels")

*   397: #PCDATA in nested model group [✉](https://validator.w3.org/feedback.html?errmsg_id=397#errormsg "Suggest improvements on this error message through our feedback channels")

*   398: #PCDATA in model group that does not have REP occurrence indicator [✉](https://validator.w3.org/feedback.html?errmsg_id=398#errormsg "Suggest improvements on this error message through our feedback channels")

*   399: name group or name token group used connector other than OR [✉](https://validator.w3.org/feedback.html?errmsg_id=399#errormsg "Suggest improvements on this error message through our feedback channels")

*   400: processing instruction does not start with name [✉](https://validator.w3.org/feedback.html?errmsg_id=400#errormsg "Suggest improvements on this error message through our feedback channels")

*   401: S separator in status keyword specification in document instance [✉](https://validator.w3.org/feedback.html?errmsg_id=401#errormsg "Suggest improvements on this error message through our feedback channels")

*   402: reference to external data entity [✉](https://validator.w3.org/feedback.html?errmsg_id=402#errormsg "Suggest improvements on this error message through our feedback channels")

*   405: SGML declaration was not implied [✉](https://validator.w3.org/feedback.html?errmsg_id=405#errormsg "Suggest improvements on this error message through our feedback channels")

*   406: marked section in internal DTD subset [✉](https://validator.w3.org/feedback.html?errmsg_id=406#errormsg "Suggest improvements on this error message through our feedback channels")

*   408: entity end in different element from entity reference [✉](https://validator.w3.org/feedback.html?errmsg_id=408#errormsg "Suggest improvements on this error message through our feedback channels")

*   409: NETENABL IMMEDNET requires EMPTYNRM YES [✉](https://validator.w3.org/feedback.html?errmsg_id=409#errormsg "Suggest improvements on this error message through our feedback channels")

*   411: declaration of default entity [✉](https://validator.w3.org/feedback.html?errmsg_id=411#errormsg "Suggest improvements on this error message through our feedback channels")

*   412: reference to parameter entity in parameter separator in internal subset [✉](https://validator.w3.org/feedback.html?errmsg_id=412#errormsg "Suggest improvements on this error message through our feedback channels")

*   413: reference to parameter entity in token separator in internal subset [✉](https://validator.w3.org/feedback.html?errmsg_id=413#errormsg "Suggest improvements on this error message through our feedback channels")

*   414: reference to parameter entity in parameter literal in internal subset [✉](https://validator.w3.org/feedback.html?errmsg_id=414#errormsg "Suggest improvements on this error message through our feedback channels")

*   415: cannot generate system identifier for SGML declaration reference [✉](https://validator.w3.org/feedback.html?errmsg_id=415#errormsg "Suggest improvements on this error message through our feedback channels")

*   416: public text class of formal public identifier of SGML declaration must be SD [✉](https://validator.w3.org/feedback.html?errmsg_id=416#errormsg "Suggest improvements on this error message through our feedback channels")

*   417: SGML declaration reference was used but minimum literal was not ""ISO 8879:1986 (WWW)"" [✉](https://validator.w3.org/feedback.html?errmsg_id=417#errormsg "Suggest improvements on this error message through our feedback channels")

*   418: member of model group containing #PCDATA has occurrence indicator [✉](https://validator.w3.org/feedback.html?errmsg_id=418#errormsg "Suggest improvements on this error message through our feedback channels")

*   419: member of model group containing #PCDATA is a model group [✉](https://validator.w3.org/feedback.html?errmsg_id=419#errormsg "Suggest improvements on this error message through our feedback channels")

*   420: reference to non-predefined entity [✉](https://validator.w3.org/feedback.html?errmsg_id=420#errormsg "Suggest improvements on this error message through our feedback channels")

*   421: reference to external entity [✉](https://validator.w3.org/feedback.html?errmsg_id=421#errormsg "Suggest improvements on this error message through our feedback channels")

*   422: declaration of default entity conflicts with IMPLYDEF ENTITY YES [✉](https://validator.w3.org/feedback.html?errmsg_id=422#errormsg "Suggest improvements on this error message through our feedback channels")

*   423: parsing with respect to more than one active doctype not supported [✉](https://validator.w3.org/feedback.html?errmsg_id=423#errormsg "Suggest improvements on this error message through our feedback channels")

*   424: cannot have active doctypes and link types at the same time [✉](https://validator.w3.org/feedback.html?errmsg_id=424#errormsg "Suggest improvements on this error message through our feedback channels")

*   425: number of concurrent document instances exceeds quantity specified for CONCUR parameter in SGML declaration (X) [✉](https://validator.w3.org/feedback.html?errmsg_id=425#errormsg "Suggest improvements on this error message through our feedback channels")

*   426: datatag group can only be specified in base document type [✉](https://validator.w3.org/feedback.html?errmsg_id=426#errormsg "Suggest improvements on this error message through our feedback channels")

*   427: element not in the base document type can't have an empty start-tag [✉](https://validator.w3.org/feedback.html?errmsg_id=427#errormsg "Suggest improvements on this error message through our feedback channels")

*   428: element not in base document type can't have an empty end-tag [✉](https://validator.w3.org/feedback.html?errmsg_id=428#errormsg "Suggest improvements on this error message through our feedback channels")

*   429: immediately recursive element [✉](https://validator.w3.org/feedback.html?errmsg_id=429#errormsg "Suggest improvements on this error message through our feedback channels")

*   430: invalid URN X: missing "":"" [✉](https://validator.w3.org/feedback.html?errmsg_id=430#errormsg "Suggest improvements on this error message through our feedback channels")

*   431: invalid URN X: missing ""urn:"" prefix [✉](https://validator.w3.org/feedback.html?errmsg_id=431#errormsg "Suggest improvements on this error message through our feedback channels")

*   432: invalid URN X: invalid namespace identifier [✉](https://validator.w3.org/feedback.html?errmsg_id=432#errormsg "Suggest improvements on this error message through our feedback channels")

*   433: invalid URN X: invalid namespace specific string [✉](https://validator.w3.org/feedback.html?errmsg_id=433#errormsg "Suggest improvements on this error message through our feedback channels")

*   434: invalid URN X: extra field [✉](https://validator.w3.org/feedback.html?errmsg_id=434#errormsg "Suggest improvements on this error message through our feedback channels")

*   435: prolog can't be omitted unless CONCUR NO and LINK EXPLICIT NO and either IMPLYDEF ELEMENT YES or IMPLYDEF DOCTYPE YES [✉](https://validator.w3.org/feedback.html?errmsg_id=435#errormsg "Suggest improvements on this error message through our feedback channels")

*   436: can't determine name of #IMPLIED document element [✉](https://validator.w3.org/feedback.html?errmsg_id=436#errormsg "Suggest improvements on this error message through our feedback channels")

*   437: can't use #IMPLICIT doctype unless CONCUR NO and LINK EXPLICIT NO [✉](https://validator.w3.org/feedback.html?errmsg_id=437#errormsg "Suggest improvements on this error message through our feedback channels")

*   438: Sorry, #IMPLIED doctypes not implemented [✉](https://validator.w3.org/feedback.html?errmsg_id=438#errormsg "Suggest improvements on this error message through our feedback channels")

*   439: reference to DTD data entity ignored [✉](https://validator.w3.org/feedback.html?errmsg_id=439#errormsg "Suggest improvements on this error message through our feedback channels")

*   440: notation X for parameter entity Y undefined [✉](https://validator.w3.org/feedback.html?errmsg_id=440#errormsg "Suggest improvements on this error message through our feedback channels")

*   441: notation X for external subset undefined [✉](https://validator.w3.org/feedback.html?errmsg_id=441#errormsg "Suggest improvements on this error message through our feedback channels")

*   442: attribute X can't be redeclared [✉](https://validator.w3.org/feedback.html?errmsg_id=442#errormsg "Suggest improvements on this error message through our feedback channels")

*   443: #IMPLICIT attributes have already been specified for notation X [✉](https://validator.w3.org/feedback.html?errmsg_id=443#errormsg "Suggest improvements on this error message through our feedback channels")

*   444: a name group is not allowed in a parameter entity reference in a start tag [✉](https://validator.w3.org/feedback.html?errmsg_id=444#errormsg "Suggest improvements on this error message through our feedback channels")

*   445: name group in a parameter entity reference in an end tag (SGML forbids them in start tags) [✉](https://validator.w3.org/feedback.html?errmsg_id=445#errormsg "Suggest improvements on this error message through our feedback channels")

*   446: if the declared value is NOTATION a default value of CONREF is useless [✉](https://validator.w3.org/feedback.html?errmsg_id=446#errormsg "Suggest improvements on this error message through our feedback channels")

*   447: Sorry, #ALL and #IMPLICIT content tokens not implemented [✉](https://validator.w3.org/feedback.html?errmsg_id=447#errormsg "Suggest improvements on this error message through our feedback channels")
