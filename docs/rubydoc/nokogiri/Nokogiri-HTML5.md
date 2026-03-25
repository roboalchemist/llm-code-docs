# Module: Nokogiri::HTML5
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/html5.rb,

  lib/nokogiri/html5/node.rb,
 lib/nokogiri/html5/builder.rb,
 lib/nokogiri/html5/document.rb,
 lib/nokogiri/html5/document_fragment.rb,
 ext/nokogiri/nokogiri.c

  
  

## Overview

  
    

## Usage

Parse an HTML5 document:

```
doc = Nokogiri.HTML5(input)

```

Parse an HTML5 fragment:

```
fragment = Nokogiri::HTML5.fragment(input)

```

⚠ HTML5 functionality is not available when running JRuby.

## Parsing options

The document and fragment parsing methods support options that are different from Nokogiri::HTML4::Document or Nokogiri::XML::Document.

- 

`Nokogiri.HTML5(input, url:, encoding:, **parse_options)`

- 

`Nokogiri::HTML5.parse(input, url:, encoding:, **parse_options)`

- 

`Nokogiri::HTML5::Document.parse(input, url:, encoding:, **parse_options)`

- 

`Nokogiri::HTML5.fragment(input, encoding:, **parse_options)`

- 

`Nokogiri::HTML5::DocumentFragment.parse(input, encoding:, **parse_options)`

The four currently supported parse options are

- 

`max_errors:` (Integer, default 0) Maximum number of parse errors to report in HTML5::Document#errors.

- 

`max_tree_depth:` (Integer, default `Nokogiri::Gumbo::DEFAULT_MAX_TREE_DEPTH`) Maximum tree depth to parse.

- 

`max_attributes:` (Integer, default `Nokogiri::Gumbo::DEFAULT_MAX_ATTRIBUTES`) Maximum number of attributes to parse per element.

- 

`parse_noscript_content_as_text:` (Boolean, default false) When enabled, parse `noscript` tag content as text, mimicking the behavior of web browsers.

These options are explained in the following sections.

### Error reporting: `max_errors:`

Nokogiri contains an experimental HTML5 parse error reporting facility. By default, no parse errors are reported but this can be configured by passing the `:max_errors` option to HTML5.parse or HTML5.fragment.

For example, this script:

```
doc = Nokogiri::HTML5.parse('<span/>Hi there!</span foo=bar />', max_errors: 10)
doc.errors.each do |err|
  puts(err)
end

```

Emits:

```
1:1: ERROR: Expected a doctype token
<span/>Hi there!</span foo=bar />
^
1:1: ERROR: Start tag of nonvoid HTML element ends with '/>', use '>'.
<span/>Hi there!</span foo=bar />
^
1:17: ERROR: End tag ends with '/>', use '>'.
<span/>Hi there!</span foo=bar />
                ^
1:17: ERROR: End tag contains attributes.
<span/>Hi there!</span foo=bar />
                ^

```

Using `max_errors: -1` results in an unlimited number of errors being returned.

The errors returned by HTML5::Document#errors are instances of Nokogiri::XML::SyntaxError.

The HTML standard defines a number of standard parse error codes. These error codes only cover the “tokenization” stage of parsing HTML. The parse errors in the “tree construction” stage do not have standardized error codes (yet).

As a convenience to Nokogiri users, the defined error codes are available via Nokogiri::XML::SyntaxError#str1 method.

```
doc = Nokogiri::HTML5.parse('<span/>Hi there!</span foo=bar />', max_errors: 10)
doc.errors.each do |err|
  puts("#{err.line}:#{err.column}: #{err.str1}")
end
doc = Nokogiri::HTML5.parse('<span/>Hi there!</span foo=bar />',
# => 1:1: generic-parser
#    1:1: non-void-html-element-start-tag-with-trailing-solidus
#    1:17: end-tag-with-trailing-solidus
#    1:17: end-tag-with-attributes

```

Note that the first error is `generic-parser` because it’s an error from the tree construction stage and doesn’t have a standardized error code.

For the purposes of semantic versioning, the error messages, error locations, and error codes are not part of Nokogiri’s public API. That is, these are subject to change without Nokogiri’s major version number changing. These may be stabilized in the future.

### Maximum tree depth: `max_tree_depth:`

The maximum depth of the DOM tree parsed by the various parsing methods is configurable by the `:max_tree_depth` option. If the depth of the tree would exceed this limit, then an `ArgumentError` is thrown.

This limit (which defaults to `Nokogiri::Gumbo::DEFAULT_MAX_TREE_DEPTH`) can be removed by giving the option `max_tree_depth: -1`.

```
html = '<!DOCTYPE html>' + '<div>' * 1000
doc = Nokogiri.HTML5(html)
# raises ArgumentError: Document tree depth limit exceeded
doc = Nokogiri.HTML5(html, max_tree_depth: -1)

```

### Attribute limit per element: `max_attributes:`

The maximum number of attributes per DOM element is configurable by the `:max_attributes` option. If a given element would exceed this limit, then an `ArgumentError` is thrown.

This limit (which defaults to `Nokogiri::Gumbo::DEFAULT_MAX_ATTRIBUTES`) can be removed by giving the option `max_attributes: -1`.

```
html = '<!DOCTYPE html><div ' + (1..1000).map { |x| "attr-#{x}" }.join(' # ') + '>'
# "<!DOCTYPE html><div attr-1 attr-2 attr-3 ... attr-1000>"
doc = Nokogiri.HTML5(html)
# raises ArgumentError: Attributes per element limit exceeded

doc = Nokogiri.HTML5(html, max_attributes: -1)
# parses successfully

```

### Parse `noscript` elements’ content as text: `parse_noscript_content_as_text:`

By default, the content of `noscript` elements is parsed as HTML elements. Browsers that support scripting parse the content of `noscript` elements as raw text.

The `:parse_noscript_content_as_text` option causes Nokogiri to parse the content of `noscript` elements as a single text node.

```
html = "<!DOCTYPE html><noscript><meta charset='UTF-8'><link rel=stylesheet href=!></noscript>"
doc = Nokogiri::HTML5.parse(html, parse_noscript_content_as_text: true)
pp doc.at_xpath("/html/head/noscript")
# => #(Element:0x878c {
#        name = "noscript",
#        children = [ #(Text "<meta charset='UTF-8'><link rel=stylesheet href=!>")]
#      })

```

In contrast, `parse_noscript_content_as_text: false` (the default) causes the `noscript` element in the previous example to have two children, a `meta` element and a `link` element.

```
doc = Nokogiri::HTML5.parse(html)
puts doc.at_xpath("/html/head/noscript")
# => #(Element:0x96b4 {
#      name = "noscript",
#      children = [
#        #(Element:0x97e0 { name = "meta", attribute_nodes = [ #(Attr:0x990c { name = "charset", value = "UTF-8" })] }),
#        #(Element:0x9b00 {
#          name = "link",
#          attribute_nodes = [
#            #(Attr:0x9c2c { name = "rel", value = "stylesheet" }),
#            #(Attr:0x9dd0 { name = "href", value = "!" })]
#          })]
#      })

```

## HTML Serialization

After parsing HTML, it may be serialized using any of the Nokogiri::XML::Node serialization methods. In particular, XML::Node#serialize, XML::Node#to_html, and XML::Node#to_s will serialize a given node and its children. (This is the equivalent of JavaScript’s `Element.outerHTML`.) Similarly, XML::Node#inner_html will serialize the children of a given node. (This is the equivalent of JavaScript’s `Element.innerHTML`.)

```
doc = Nokogiri::HTML5("<!DOCTYPE html><span>Hello world!</span>")
puts doc.serialize
# => <!DOCTYPE html><html><head></head><body><span>Hello world!</span></body></html>

```

Due to quirks in how HTML is parsed and serialized, it’s possible for a DOM tree to be serialized and then re-parsed, resulting in a different DOM. Mostly, this happens with DOMs produced from invalid HTML. Unfortunately, even valid HTML may not survive serialization and re-parsing.

In particular, a newline at the start of `pre`, `listing`, and `textarea` elements is ignored by the parser.

```
doc = Nokogiri::HTML5("<!DOCTYPE html>\n<pre>\nContent</pre>\n")
puts doc.at('/html/body/pre').serialize
# => <pre>Content</pre>

```

In this case, the original HTML is semantically equivalent to the serialized version. If the `pre`, `listing`, or `textarea` content starts with two newlines, the first newline will be stripped on the first parse and the second newline will be stripped on the second, leading to semantically different DOMs. Passing the parameter `preserve_newline: true` will cause two or more newlines to be preserved. (A single leading newline will still be removed.)

```
doc = Nokogiri::HTML5("<!DOCTYPE html>\n<listing>\n\nContent</listing>\n")
puts doc.at('/html/body/listing').serialize(preserve_newline: true)
# => <listing>
#
#    Content</listing>

```

## Encodings

Nokogiri always parses HTML5 using UTF-8; however, the encoding of the input can be explicitly selected via the optional `encoding` parameter. This is most useful when the input comes not from a string but from an IO object.

When serializing a document or node, the encoding of the output string can be specified via the `:encoding` options. Characters that cannot be encoded in the selected encoding will be encoded as HTML numeric entities.

```
frag = Nokogiri::HTML5.fragment('<span>아는 길도 물어가라</span>')
html = frag.serialize(encoding: 'US-ASCII')
puts html
# => <span>아는 길도 물어가라</span>

frag = Nokogiri::HTML5.fragment(html)
puts frag.serialize
# => <span>아는 길도 물어가라</span>

```

(There’s a bug in all current versions of Ruby that can cause the entity encoding to fail. Of the mandated supported encodings for HTML, the only encoding I’m aware of that has this bug is `'ISO-2022-JP'`. We recommend avoiding this encoding.)

## Notes

- 

The Nokogiri::HTML5.fragment function takes a String or IO and parses it as a HTML5 document in a `body` context. As a result, the `html`, `head`, and `body` elements are removed from this document, and any children of these elements that remain are returned as a Nokogiri::HTML5::DocumentFragment; but you can pass in a different context (e.g., “html” to get `head` and `body` tags in the result).

- 

The Nokogiri::HTML5.parse function takes a String or IO and passes it to the `gumbo_parse_with_options` method, using the default options.  The resulting Gumbo parse tree is then walked.

- 

Instead of uppercase element names, lowercase element names are produced.

- 

Instead of returning `unknown` as the element name for unknown tags, the original tag name is returned verbatim.

Since v1.12.0

  

  

## Defined Under Namespace

  
    
      **Modules:** Node, QuirksMode
    
  
    
      **Classes:** Builder, Document, DocumentFragment
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**fragment**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convenience method for Nokogiri::HTML5::DocumentFragment.parse.

  

      
        
- 
  
    
      .**parse**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convenience method for Nokogiri::HTML5::Document.parse.

  

      
        
- 
  
    
      .**read_and_encode**(string, encoding)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**fragment**  ⇒ Object 
  

  

  

  
    

Convenience method for Nokogiri::HTML5::DocumentFragment.parse

  

  

  
    
      

```

280
281
282
```

    
    
      

```
# File 'lib/nokogiri/html5.rb', line 280

def fragment(...)
  DocumentFragment.parse(...)
end

```

    
  

    
      
  
### 
  
    .**parse**  ⇒ Object 
  

  

  

  
    

Convenience method for Nokogiri::HTML5::Document.parse

  

  

  
    
      

```

275
276
277
```

    
    
      

```
# File 'lib/nokogiri/html5.rb', line 275

def parse(...)
  Document.parse(...)
end

```

    
  

    
      
  
### 
  
    .**read_and_encode**(string, encoding)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
```

    
    
      

```
# File 'lib/nokogiri/html5.rb', line 285

def read_and_encode(string, encoding)
  # Read the string with the given encoding.
  if string.respond_to?(:read)
    string = if encoding.nil?
      string.read
    else
      string.read(encoding: encoding)
    end
  else
    # Otherwise the string has the given encoding.
    string = string.to_s
    if encoding
      string = string.dup
      string.force_encoding(encoding)
    end
  end

  # convert to UTF-8
  if string.encoding != Encoding::UTF_8
    string = reencode(string)
  end
  string
end

```