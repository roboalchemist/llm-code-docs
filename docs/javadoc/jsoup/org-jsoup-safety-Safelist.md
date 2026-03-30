Package org.jsoup.safety

# Class Safelist

java.lang.Object
org.jsoup.safety.Safelist

---

public class Safelist
extends Object
Safe-lists define what HTML (elements and attributes) to allow through the cleaner. Everything else is removed.
 

 Start with one of the defaults:
 
 

 
- `none()`
 
- `simpleText()`
 
- `basic()`
 
- `basicWithImages()`
 
- `relaxed()`
 

 

 If you need to allow more through (please be careful!), tweak a base safelist with:
 
 

 
- `addTags(String...tagNames)`
 
- `addAttributes(String tagName, String...attributes)`
 
- `addEnforcedAttribute(String tagName, String attribute, String value)`
 
- `addProtocols(String tagName, String attribute, String...protocols)`
 

 

 You can remove any setting from an existing safelist with:
 
 

 
- `removeTags(String...tagNames)`
 
- `removeAttributes(String tagName, String...attributes)`
 
- `removeEnforcedAttribute(String tagName, String attribute)`
 
- `removeProtocols(String tagName, String attribute, String...removeProtocols)`
 

 

 The cleaner and these safelists assume that you want to clean a `body` fragment of HTML (to add user
 supplied HTML into a templated page), and not to clean a full HTML document. If the latter is the case, you could wrap
 the templated document HTML around the cleaned body HTML.
 
 

 If you are going to extend a safelist, please be very careful. Make sure you understand what attributes may lead to
 XSS attack vectors. URL attributes are particularly vulnerable and require careful validation. See 
 the XSS Filter Evasion Cheat Sheet for some
 XSS attack examples (that jsoup will safegaurd against the default Cleaner and Safelist configuration).
 

- 

## Constructor Summary

Constructors

Constructor
Description
`Safelist()`

Create a new, empty safelist.

`Safelist(Safelist copy)`

Deep copy an existing Safelist to a new Safelist.

- 

## Method Summary

Modifier and Type
Method
Description
`Safelist`
`addAttributes(String tag,
 String... attributes)`

Add a list of allowed attributes to a tag.

`Safelist`
`addEnforcedAttribute(String tag,
 String attribute,
 String value)`

Add an enforced attribute to a tag.

`Safelist`
`addProtocols(String tag,
 String attribute,
 String... protocols)`

Add allowed URL protocols for an element's URL attribute.

`Safelist`
`addTags(String... tags)`

Add a list of allowed elements to a safelist.

`static Safelist`
`basic()`

     This safelist allows a fuller range of text nodes: `a, b, blockquote, br, cite, code, dd, dl, dt, em, i, li,
     ol, p, pre, q, small, span, strike, strong, sub, sup, u, ul`, and appropriate attributes.

`static Safelist`
`basicWithImages()`

This safelist allows the same text tags as `basic()`, and also allows `img` tags, with appropriate
     attributes, with `src` pointing to `http` or `https`.

`Attributes`
`getEnforcedAttributes(String tagName)`

Gets the Attributes that should be enforced for a given tag

`boolean`
`isSafeAttribute(String tagName,
 Element el,
 Attribute attr)`

Test if the supplied attribute is allowed by this safelist for this tag.

`boolean`
`isSafeTag(String tag)`

Test if the supplied tag is allowed by this safelist.

`static Safelist`
`none()`

This safelist allows only text nodes: any HTML Element or any Node other than a TextNode will be removed.

`boolean`
`preserveRelativeLinks()`

Get the current setting for preserving relative links.

`Safelist`
`preserveRelativeLinks(boolean preserve)`

Configure this Safelist to preserve relative links in an element's URL attribute, or convert them to absolute
 links.

`static Safelist`
`relaxed()`

This safelist allows a full range of text and structural body HTML: `a, b, blockquote, br, caption, cite,
     code, col, colgroup, dd, div, dl, dt, em, h1, h2, h3, h4, h5, h6, i, img, li, ol, p, pre, q, small, span, strike, strong, sub,
     sup, table, tbody, td, tfoot, th, thead, tr, u, ul`

`Safelist`
`removeAttributes(String tag,
 String... attributes)`

Remove a list of allowed attributes from a tag.

`Safelist`
`removeEnforcedAttribute(String tag,
 String attribute)`

Remove a previously configured enforced attribute from a tag.

`Safelist`
`removeProtocols(String tag,
 String attribute,
 String... removeProtocols)`

Remove allowed URL protocols for an element's URL attribute.

`Safelist`
`removeTags(String... tags)`

Remove a list of allowed elements from a safelist.

`static Safelist`
`simpleText()`

This safelist allows only simple text formatting: `b, em, i, strong, u`.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### Safelist

public Safelist()
Create a new, empty safelist. Generally it will be better to start with a default prepared safelist instead.

See Also:

    - `basic()`

    - `basicWithImages()`

    - `simpleText()`

    - `relaxed()`

  - 

### Safelist

public Safelist(Safelist copy)
Deep copy an existing Safelist to a new Safelist.

Parameters:
`copy` - the Safelist to copy

- 

## Method Details

  - 

### none

public static Safelist none()
This safelist allows only text nodes: any HTML Element or any Node other than a TextNode will be removed.
     

     Note that the output of `Jsoup.clean(String, Safelist)` is still **HTML** even when using
     this Safelist, and so any HTML entities in the output will be appropriately escaped. If you want plain text, not
     HTML, you should use a text method such as `Element.text()` instead, after cleaning the document.
     
     

Example:
     

```

     String sourceBodyHtml = "<p>5 is < 6.</p>";
     String html = Jsoup.clean(sourceBodyHtml, Safelist.none());

     Cleaner cleaner = new Cleaner(Safelist.none());
     String text = cleaner.clean(Jsoup.parse(sourceBodyHtml)).text();

     // html is: 5 is < 6.
     // text is: 5 is < 6.
     
```

Returns:
safelist

  - 

### simpleText

public static Safelist simpleText()
This safelist allows only simple text formatting: `b, em, i, strong, u`. All other HTML (tags and
     attributes) will be removed.

Returns:
safelist

  - 

### basic

public static Safelist basic()

     This safelist allows a fuller range of text nodes: `a, b, blockquote, br, cite, code, dd, dl, dt, em, i, li,
     ol, p, pre, q, small, span, strike, strong, sub, sup, u, ul`, and appropriate attributes.
     
     

     Links (`a` elements) can point to `http, https, ftp, mailto`, and have an enforced
     `rel=nofollow` attribute if they link offsite (as indicated by the specified base URI).
     
     

     Does not allow images.
     

Returns:
safelist

  - 

### basicWithImages

public static Safelist basicWithImages()
This safelist allows the same text tags as `basic()`, and also allows `img` tags, with appropriate
     attributes, with `src` pointing to `http` or `https`.

Returns:
safelist

  - 

### relaxed

public static Safelist relaxed()
This safelist allows a full range of text and structural body HTML: `a, b, blockquote, br, caption, cite,
     code, col, colgroup, dd, div, dl, dt, em, h1, h2, h3, h4, h5, h6, i, img, li, ol, p, pre, q, small, span, strike, strong, sub,
     sup, table, tbody, td, tfoot, th, thead, tr, u, ul`
     

     Links do not have an enforced `rel=nofollow` attribute, but you can add that if desired.
     

Returns:
safelist

  - 

### addTags

public Safelist addTags(String... tags)
Add a list of allowed elements to a safelist. (If a tag is not allowed, it will be removed from the HTML.)

Parameters:
`tags` - tag names to allow
Returns:
this (for chaining)

  - 

### removeTags

public Safelist removeTags(String... tags)
Remove a list of allowed elements from a safelist. (If a tag is not allowed, it will be removed from the HTML.)

Parameters:
`tags` - tag names to disallow
Returns:
this (for chaining)

  - 

### addAttributes

public Safelist addAttributes(String tag,
 String... attributes)
Add a list of allowed attributes to a tag. (If an attribute is not allowed on an element, it will be removed.)
     

     E.g.: `addAttributes("a", "href", "class")` allows `href` and `class` attributes
     on `a` tags.
     
     

     To make an attribute valid for **all tags**, use the pseudo tag `:all`, e.g.
     `addAttributes(":all", "class")`.
     

Parameters:
`tag` - The tag the attributes are for. The tag will be added to the allowed tag list if necessary.
`attributes` - List of valid attributes for the tag
Returns:
this (for chaining)

  - 

### removeAttributes

public Safelist removeAttributes(String tag,
 String... attributes)
Remove a list of allowed attributes from a tag. (If an attribute is not allowed on an element, it will be removed.)
     

     E.g.: `removeAttributes("a", "href", "class")` disallows `href` and `class`
     attributes on `a` tags.
     
     

     To make an attribute invalid for **all tags**, use the pseudo tag `:all`, e.g.
     `removeAttributes(":all", "class")`.
     

Parameters:
`tag` - The tag the attributes are for.
`attributes` - List of invalid attributes for the tag
Returns:
this (for chaining)

  - 

### addEnforcedAttribute

public Safelist addEnforcedAttribute(String tag,
 String attribute,
 String value)
Add an enforced attribute to a tag. An enforced attribute will always be added to the element. If the element
     already has the attribute set, it will be overridden with this value.
     

     E.g.: `addEnforcedAttribute("a", "rel", "nofollow")` will make all `a` tags output as
     `<a href="..." rel="nofollow">`
     

Parameters:
`tag` - The tag the enforced attribute is for. The tag will be added to the allowed tag list if necessary.
`attribute` - The attribute name
`value` - The enforced attribute value
Returns:
this (for chaining)

  - 

### removeEnforcedAttribute

public Safelist removeEnforcedAttribute(String tag,
 String attribute)
Remove a previously configured enforced attribute from a tag.

Parameters:
`tag` - The tag the enforced attribute is for.
`attribute` - The attribute name
Returns:
this (for chaining)

  - 

### preserveRelativeLinks

public Safelist preserveRelativeLinks(boolean preserve)
Configure this Safelist to preserve relative links in an element's URL attribute, or convert them to absolute
 links. By default, this is **false**: URLs will be  made absolute (e.g. start with an allowed protocol, like
 e.g. `http://`.

Parameters:
`preserve` - `true` to allow relative links, `false` (default) to deny
Returns:
this Safelist, for chaining.
See Also:

    - `addProtocols(java.lang.String, java.lang.String, java.lang.String...)`

  - 

### preserveRelativeLinks

public boolean preserveRelativeLinks()
Get the current setting for preserving relative links.

Returns:
`true` if relative links are preserved, `false` if they are converted to absolute.

  - 

### addProtocols

public Safelist addProtocols(String tag,
 String attribute,
 String... protocols)
Add allowed URL protocols for an element's URL attribute. This restricts the possible values of the attribute to
     URLs with the defined protocol.
     

     E.g.: `addProtocols("a", "href", "ftp", "http", "https")`
     
     

     To allow a link to an in-page URL anchor (i.e. `<a href="#anchor">`, add a `#`:

     E.g.: `addProtocols("a", "href", "#")`
     

Parameters:
`tag` - Tag the URL protocol is for
`attribute` - Attribute name
`protocols` - List of valid protocols
Returns:
this, for chaining

  - 

### removeProtocols

public Safelist removeProtocols(String tag,
 String attribute,
 String... removeProtocols)
Remove allowed URL protocols for an element's URL attribute. If you remove all protocols for an attribute, that
     attribute will allow any protocol.
     

     E.g.: `removeProtocols("a", "href", "ftp")`
     

Parameters:
`tag` - Tag the URL protocol is for
`attribute` - Attribute name
`removeProtocols` - List of invalid protocols
Returns:
this, for chaining

  - 

### isSafeTag

public boolean isSafeTag(String tag)
Test if the supplied tag is allowed by this safelist.

Parameters:
`tag` - test tag
Returns:
true if allowed

  - 

### isSafeAttribute

public boolean isSafeAttribute(String tagName,
 Element el,
 Attribute attr)
Test if the supplied attribute is allowed by this safelist for this tag.

Parameters:
`tagName` - tag to consider allowing the attribute in
`el` - element under test, to confirm protocol
`attr` - attribute under test
Returns:
true if allowed

  - 

### getEnforcedAttributes

public Attributes getEnforcedAttributes(String tagName)
Gets the Attributes that should be enforced for a given tag

Parameters:
`tagName` - the tag
Returns:
the attributes that will be enforced; empty if none are set for the given tag