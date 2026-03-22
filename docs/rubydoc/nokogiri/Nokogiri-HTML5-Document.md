# Class: Nokogiri::HTML5::Document
  
  
  

  
  
    Inherits:
    
      Nokogiri::HTML4::Document
      
        

          
- Object
          
            
- XML::Node
          
            
- XML::Document
          
            
- Nokogiri::HTML4::Document
          
            
- Nokogiri::HTML5::Document
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/html5/document.rb,

  ext/nokogiri/gumbo.c

  
  

## Overview

  
    

Since v1.12.0

💡 HTML5 functionality is not available when running JRuby.

  

  

  
## Constant Summary

  
  
### Constants inherited
     from XML::Document

  

XML::Document::NCNAME_CHAR, XML::Document::NCNAME_RE, XML::Document::NCNAME_START_CHAR

  
  
  
### Constants inherited
     from XML::Node

  

XML::Node::ATTRIBUTE_DECL, XML::Node::ATTRIBUTE_NODE, XML::Node::CDATA_SECTION_NODE, XML::Node::COMMENT_NODE, XML::Node::DECONSTRUCT_KEYS, XML::Node::DECONSTRUCT_METHODS, XML::Node::DOCB_DOCUMENT_NODE, XML::Node::DOCUMENT_FRAG_NODE, XML::Node::DOCUMENT_NODE, XML::Node::DOCUMENT_TYPE_NODE, XML::Node::DTD_NODE, XML::Node::ELEMENT_DECL, XML::Node::ELEMENT_NODE, XML::Node::ENTITY_DECL, XML::Node::ENTITY_NODE, XML::Node::ENTITY_REF_NODE, XML::Node::HTML_DOCUMENT_NODE, XML::Node::NAMESPACE_DECL, XML::Node::NOTATION_NODE, XML::Node::PI_NODE, XML::Node::TEXT_NODE, XML::Node::XINCLUDE_END, XML::Node::XINCLUDE_START

  
  
  
### Constants included
     from ClassResolver

  

ClassResolver::VALID_NAMESPACES

  
  
  
### Constants included
     from XML::Searchable

  

XML::Searchable::LOOKS_LIKE_XPATH

  
  
  
### Constants included
     from XML::PP::Node

  

XML::PP::Node::COLLECTIONS

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**quirks_mode**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Get the parser’s quirks mode value.

  

    
      
- 
  
    
      #**url**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Get the url name for this document, as passed into Document.parse, Document.read_io, or Document.read_memory.

  

    
  

  
  
  
### Attributes inherited from XML::Document

  

#errors, #namespace_inheritance

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**parse**(string_or_io, url_ = nil, encoding_ = nil, url: url_, encoding: encoding_, **options) {|options| ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   parse(input) { |options| … } → HTML5::Document   parse(input, url: encoding:) { |options| … } → HTML5::Document   parse(input, **options) → HTML5::Document.

  

      
        
- 
  
    
      .**read_io**(io, url_ = nil, encoding_ = nil, url: url_, encoding: encoding_, **options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a new document from an IO object.

  

      
        
- 
  
    
      .**read_memory**(string, url_ = nil, encoding_ = nil, url: url_, encoding: encoding_, **options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a new document from a String.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**fragment**(markup = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   fragment() → Nokogiri::HTML5::DocumentFragment   fragment(markup) → Nokogiri::HTML5::DocumentFragment.

  

      
        
- 
  
    
      #**initialize**(*args)  ⇒ Document 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**to_xml**(options = {}, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**xpath_doctype**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   xpath_doctype() → Nokogiri::CSS::XPathVisitor::DoctypeConfig.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Nokogiri::HTML4::Document

  

#meta_encoding, #meta_encoding=, new, #serialize, #title, #title=, #type

  
  
  
  
  
  
  
  
  
### Methods inherited from XML::Document

  

#add_child, #canonicalize, #clone, #collect_namespaces, #create_cdata, #create_comment, #create_element, #create_entity, #create_text_node, #deconstruct_keys, #decorate, #decorators, #document, #dup, #encoding, #encoding=, #name, #namespaces, new, #remove_namespaces!, #root, #root=, #slop!, #validate, #version

  
  
  
  
  
  
  
  
  
### Methods inherited from XML::Node

  

#<<, #<=>, #==, #[], #[]=, #accept, #add_child, #add_class, #add_namespace_definition, #add_next_sibling, #add_previous_sibling, #after, #ancestors, #append_class, #attribute, #attribute_nodes, #attribute_with_ns, #attributes, #before, #blank?, #canonicalize, #cdata?, #child, #children, #children=, #classes, #clone, #comment?, #content, #content=, #create_external_subset, #create_internal_subset, #css_path, #data_ptr?, #deconstruct_keys, #decorate!, #default_namespace=, #description, #do_xinclude, #document, #document?, #dup, #each, #element?, #element_children, #encode_special_chars, #external_subset, #first_element_child, #fragment?, #html?, #inner_html, #inner_html=, #internal_subset, #key?, #keys, #kwattr_add, #kwattr_append, #kwattr_remove, #kwattr_values, #lang, #lang=, #last_element_child, #line, #line=, #matches?, #namespace, #namespace=, #namespace_definitions, #namespace_scopes, #namespaced_key?, #namespaces, #native_content=, new, #next_element, #next_sibling, #node_name, #node_name=, #node_type, #parent, #parent=, #parse, #path, #pointer_id, #prepend_child, #previous_element, #previous_sibling, #processing_instruction?, #read_only?, #remove_attribute, #remove_class, #replace, #serialize, #swap, #text?, #to_html, #to_s, #to_xhtml, #traverse, #unlink, #value?, #values, #wrap, #write_html_to, #write_to, #write_xhtml_to, #write_xml_to, #xml?

  
  
  
  
  
  
  
  
  
  
### Methods included from ClassResolver

  

#related_class

  
  
  
  
  
  
  
  
  
### Methods included from XML::Searchable

  

#>, #at, #at_css, #at_xpath, #css, #search, #xpath

  
  
  
  
  
  
  
  
  
### Methods included from XML::PP::Node

  

#inspect, #pretty_print

  
  
  
  
  
  
  
  
  
### Methods included from Node

  

#inner_html, #write_to

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(*args)  ⇒ Document 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

159
160
161
162
163
```

    
    
      

```
# File 'lib/nokogiri/html5/document.rb', line 159

def initialize(*args) # :nodoc:
  super
  @url = nil
  @quirks_mode = nil
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**quirks_mode**  ⇒ Object  (readonly)
  

  

  

  
    

Get the parser’s quirks mode value. See HTML5::QuirksMode.

This method returns `nil` if the parser was not invoked (e.g., Nokogiri::HTML5::Document.new).

Since v1.14.0

  

  

  
    
      

```

49
50
51
```

    
    
      

```
# File 'lib/nokogiri/html5/document.rb', line 49

def quirks_mode
  @quirks_mode
end
```

    
  

    
      
      
      
  
### 
  
    #**url**  ⇒ Object  (readonly)
  

  

  

  
    

Get the url name for this document, as passed into Document.parse, Document.read_io, or Document.read_memory

  

  

  
    
      

```

42
43
44
```

    
    
      

```
# File 'lib/nokogiri/html5/document.rb', line 42

def url
  @url
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**parse**(string_or_io, url_ = nil, encoding_ = nil, url: url_, encoding: encoding_, **options) {|options| ... } ⇒ Object 
  

  

  

  
    

:call-seq:

```
parse(input) { |options| ... } → HTML5::Document
parse(input, url: encoding:) { |options| ... } → HTML5::Document
parse(input, **options) → HTML5::Document

```

Parse HTML input with a parser compliant with the HTML5 spec. This method uses the encoding of `input` if it can be determined, or else falls back to the `encoding:` parameter.
Required Parameters

- 

`input` (String | IO) the HTML content to be parsed.

Optional Parameters

- 

`url:` (String) the base URI of the document.

Optional Keyword Arguments

- 

`encoding:` (Encoding) The name of the encoding that should be used when processing the document. When not provided, the encoding will be determined based on the document content.

- 

`max_errors:` (Integer) The maximum number of parse errors to record. (default `Nokogiri::Gumbo::DEFAULT_MAX_ERRORS` which is currently 0)

- 

`max_tree_depth:` (Integer) The maximum depth of the parse tree. (default `Nokogiri::Gumbo::DEFAULT_MAX_TREE_DEPTH`)

- 

`max_attributes:` (Integer) The maximum number of attributes allowed on an element. (default `Nokogiri::Gumbo::DEFAULT_MAX_ATTRIBUTES`)

- 

`parse_noscript_content_as_text:` (Boolean) Whether to parse the content of `noscript` elements as text. (default `false`)

See HTML5@Parsing+options for a complete description of these parsing options.
Yields

If present, the block will be passed a Hash object to modify with parse options before the input is parsed. See HTML5@Parsing+options for a list of available options.

⚠ Note that `url:` and `encoding:` cannot be set by the configuration block.
Returns

Nokogiri::HTML5::Document

**Example:** Parse a string with a specific encoding and custom max errors limit.

```
Nokogiri::HTML5::Document.parse(socket, encoding: "ISO-8859-1", max_errors: 10)

```

**Example:** Parse a string setting the `:parse_noscript_content_as_text` option using the configuration block parameter.

```
Nokogiri::HTML5::Document.parse(input) { |c| c[:parse_noscript_content_as_text] = true }

```

  

  

Yields:

  
    
- 
      
      
        (options)
      
      
      
    
  

  
    
      

```

103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
```

    
    
      

```
# File 'lib/nokogiri/html5/document.rb', line 103

def parse(
  string_or_io,
  url_ = nil, encoding_ = nil,
  url: url_, encoding: encoding_,
  **options, &block
)
  yield options if block
  string_or_io = "" unless string_or_io

  if string_or_io.respond_to?(:encoding) && string_or_io.encoding != Encoding::ASCII_8BIT
    encoding ||= string_or_io.encoding.name
  end

  if string_or_io.respond_to?(:read) && string_or_io.respond_to?(:path)
    url ||= string_or_io.path
  end
  unless string_or_io.respond_to?(:read) || string_or_io.respond_to?(:to_str)
    raise ArgumentError, "not a string or IO object"
  end

  do_parse(string_or_io, url, encoding, **options)
end
```

    
  

    
      
  
### 
  
    .**read_io**(io, url_ = nil, encoding_ = nil, url: url_, encoding: encoding_, **options)  ⇒ Object 
  

  

  

  
    

Create a new document from an IO object.

💡 Most users should prefer Document.parse to this method.

  

  

Raises:

  
    
- 
      
      
      
      
    
  

  
    
      

```

129
130
131
132
133
```

    
    
      

```
# File 'lib/nokogiri/html5/document.rb', line 129

def read_io(io, url_ = nil, encoding_ = nil, url: url_, encoding: encoding_, **options)
  raise ArgumentError, "io object doesn't respond to :read" unless io.respond_to?(:read)

  do_parse(io, url, encoding, **options)
end
```

    
  

    
      
  
### 
  
    .**read_memory**(string, url_ = nil, encoding_ = nil, url: url_, encoding: encoding_, **options)  ⇒ Object 
  

  

  

  
    

Create a new document from a String.

💡 Most users should prefer Document.parse to this method.

  

  

Raises:

  
    
- 
      
      
      
      
    
  

  
    
      

```

138
139
140
141
142
```

    
    
      

```
# File 'lib/nokogiri/html5/document.rb', line 138

def read_memory(string, url_ = nil, encoding_ = nil, url: url_, encoding: encoding_, **options)
  raise ArgumentError, "string object doesn't respond to :to_str" unless string.respond_to?(:to_str)

  do_parse(string, url, encoding, **options)
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**fragment**(markup = nil)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
fragment() → Nokogiri::HTML5::DocumentFragment
fragment(markup) → Nokogiri::HTML5::DocumentFragment

```

Parse a HTML5 document fragment from `markup`, returning a Nokogiri::HTML5::DocumentFragment.
Properties

- 

`markup` (String) The HTML5 markup fragment to be parsed

Returns

Nokogiri::HTML5::DocumentFragment. This object’s children will be empty if `markup` is not passed, is empty, or is `nil`.

  

  

  
    
      

```

178
179
180
```

    
    
      

```
# File 'lib/nokogiri/html5/document.rb', line 178

def fragment(markup = nil)
  DocumentFragment.new(self, markup)
end
```

    
  

    
      
  
### 
  
    #**to_xml**(options = {}, &block)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

182
183
184
185
186
```

    
    
      

```
# File 'lib/nokogiri/html5/document.rb', line 182

def to_xml(options = {}, &block) # :nodoc:
  # Bypass XML::Document#to_xml which doesn't add
  # XML::Node::SaveOptions::AS_XML like XML::Node#to_xml does.
  XML::Node.instance_method(:to_xml).bind_call(self, options, &block)
end
```

    
  

    
      
  
### 
  
    #**xpath_doctype**  ⇒ Object 
  

  

  

  
    

:call-seq:

```
xpath_doctype() → Nokogiri::CSS::XPathVisitor::DoctypeConfig

```

Returns

The document type which determines CSS-to-XPath translation.

See CSS::XPathVisitor for more information.

  

  

  
    
      

```

194
195
196
```

    
    
      

```
# File 'lib/nokogiri/html5/document.rb', line 194

def xpath_doctype
  Nokogiri::CSS::XPathVisitor::DoctypeConfig::HTML5
end
```