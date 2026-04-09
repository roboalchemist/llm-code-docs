# Class: Nokogiri::HTML5::DocumentFragment
  
  
  

  
  
    Inherits:
    
      Nokogiri::HTML4::DocumentFragment
      
        

          
- Object
          
            
- XML::Node
          
            
- XML::DocumentFragment
          
            
- Nokogiri::HTML4::DocumentFragment
          
            
- Nokogiri::HTML5::DocumentFragment
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/html5/document_fragment.rb
  
  

## Overview

  
    

Since v1.12.0

💡 HTML5 functionality is not available when running JRuby.

  

  

  
## Constant Summary

  
  
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
  
    
      #**document**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute document.

  

    
      
- 
  
    
      #**errors**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute errors.

  

    
      
- 
  
    
      #**quirks_mode**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Get the parser’s quirks mode value.

  

    
  

  
  
  
### Attributes inherited from XML::DocumentFragment

  

#parse_options

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**parse**(input, encoding_ = nil, positional_options_hash = nil, encoding: encoding_, **options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   parse(input, **options) → HTML5::DocumentFragment.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**extract_params**(params)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**initialize**(doc, input = nil, context_ = nil, positional_options_hash = nil, context: context_, **options)  ⇒ DocumentFragment 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

:call-seq:   new(document, input, **options) → HTML5::DocumentFragment.

  

      
        
- 
  
    
      #**serialize**(options = {}, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
    

  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods inherited from XML::DocumentFragment

  

#css, #deconstruct, #dup, #fragment, #name, native_new, new, #search, #to_html, #to_s, #to_xhtml, #to_xml

  
  
  
  
  
  
  
  
  
### Methods inherited from XML::Node

  

#<<, #<=>, #==, #[], #[]=, #accept, #add_child, #add_class, #add_namespace_definition, #add_next_sibling, #add_previous_sibling, #after, #ancestors, #append_class, #attribute, #attribute_nodes, #attribute_with_ns, #attributes, #before, #blank?, #canonicalize, #cdata?, #child, #children, #children=, #classes, #clone, #comment?, #content, #content=, #create_external_subset, #create_internal_subset, #css_path, #data_ptr?, #deconstruct_keys, #decorate!, #default_namespace=, #description, #do_xinclude, #document?, #dup, #each, #element?, #element_children, #encode_special_chars, #external_subset, #first_element_child, #fragment, #fragment?, #html?, #inner_html, #inner_html=, #internal_subset, #key?, #keys, #kwattr_add, #kwattr_append, #kwattr_remove, #kwattr_values, #lang, #lang=, #last_element_child, #line, #line=, #matches?, #namespace, #namespace=, #namespace_definitions, #namespace_scopes, #namespaced_key?, #namespaces, #native_content=, new, #next_element, #next_sibling, #node_name, #node_name=, #node_type, #parent, #parent=, #parse, #path, #pointer_id, #prepend_child, #previous_element, #previous_sibling, #processing_instruction?, #read_only?, #remove_attribute, #remove_class, #replace, #swap, #text?, #to_html, #to_s, #to_xhtml, #to_xml, #traverse, #unlink, #value?, #values, #wrap, #write_html_to, #write_to, #write_xhtml_to, #write_xml_to, #xml?

  
  
  
  
  
  
  
  
  
  
### Methods included from ClassResolver

  

#related_class

  
  
  
  
  
  
  
  
  
### Methods included from XML::Searchable

  

#>, #at, #at_css, #at_xpath, #css, #search, #xpath

  
  
  
  
  
  
  
  
  
### Methods included from XML::PP::Node

  

#inspect, #pretty_print

  
  
  
  
  
  
  
  
  
### Methods included from Node

  

#fragment, #inner_html, #write_to

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(doc, input = nil, context_ = nil, positional_options_hash = nil, context: context_, **options)  ⇒ DocumentFragment 
  

  

  

  
    

:call-seq:

```
new(document, input, **options) → HTML5::DocumentFragment

```

Parse HTML5 fragment input from a String, and return a new HTML5::DocumentFragment.

💡 It’s recommended to use either HTML5::DocumentFragment.parse or HTML5::Node#fragment rather than call this method directly.
Required Parameters

- 

`document` (HTML5::Document) The parent document to associate the returned fragment with.

Optional Parameters

- 

`input` (String) The content to be parsed.

Optional Keyword Arguments

- 

`encoding:` (String | Encoding) The encoding, or name of the encoding, that should be used when processing the document. When not provided, the encoding will be determined based on the document content. Also see Nokogiri::HTML5 for a longer explanation of how encoding is handled by the parser.

- 

`context:` (String | Nokogiri::XML::Node) The node, or the name of an HTML5 element, in which to parse the document fragment. (default “body”)

- 

`max_errors:` (Integer) The maximum number of parse errors to record. (default `Nokogiri::Gumbo::DEFAULT_MAX_ERRORS` which is currently 0)

- 

`max_tree_depth:` (Integer) The maximum depth of the parse tree. (default `Nokogiri::Gumbo::DEFAULT_MAX_TREE_DEPTH`)

- 

`max_attributes:` (Integer) The maximum number of attributes allowed on an element. (default `Nokogiri::Gumbo::DEFAULT_MAX_ATTRIBUTES`)

- 

`parse_noscript_content_as_text:` (Boolean) Whether to parse the content of `noscript` elements as text. (default `false`)

See HTML5@Parsing+options for a complete description of these parsing options.
Returns

HTML5::DocumentFragment

### Context Node

If a context node is specified using `context:`, then the parser will behave as if that Node, or a hypothetical tag named as specified, is the parent of the fragment subtree.

  

  

  
    
      

```

144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
```

    
    
      

```
# File 'lib/nokogiri/html5/document_fragment.rb', line 144

def initialize(
  doc, input = nil,
  context_ = nil, positional_options_hash = nil,
  context: context_,
  **options
) # rubocop:disable Lint/MissingSuper
  unless positional_options_hash.nil? || positional_options_hash.empty?
    options.merge!(positional_options_hash)
  end

  @document = doc
  @errors = []
  return self unless input

  input = Nokogiri::HTML5.read_and_encode(input, nil)

  context = options.delete(:context) if options.key?(:context)

  options[:max_attributes] ||= Nokogiri::Gumbo::DEFAULT_MAX_ATTRIBUTES
  options[:max_errors] ||= options.delete(:max_parse_errors) || Nokogiri::Gumbo::DEFAULT_MAX_ERRORS
  options[:max_tree_depth] ||= Nokogiri::Gumbo::DEFAULT_MAX_TREE_DEPTH

  Nokogiri::Gumbo.fragment(self, input, context, **options)
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**document**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute document.

  

  

  
    
      

```

88
89
90
```

    
    
      

```
# File 'lib/nokogiri/html5/document_fragment.rb', line 88

def document
  @document
end
```

    
  

    
      
      
      
  
### 
  
    #**errors**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute errors.

  

  

  
    
      

```

89
90
91
```

    
    
      

```
# File 'lib/nokogiri/html5/document_fragment.rb', line 89

def errors
  @errors
end
```

    
  

    
      
      
      
  
### 
  
    #**quirks_mode**  ⇒ Object  (readonly)
  

  

  

  
    

Get the parser’s quirks mode value. See HTML5::QuirksMode.

This method returns `nil` if the parser was not invoked (e.g., ‘Nokogiri::HTML5::DocumentFragment.new(doc)`).

Since v1.14.0

  

  

  
    
      

```

97
98
99
```

    
    
      

```
# File 'lib/nokogiri/html5/document_fragment.rb', line 97

def quirks_mode
  @quirks_mode
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**parse**(input, encoding_ = nil, positional_options_hash = nil, encoding: encoding_, **options)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
parse(input, **options) → HTML5::DocumentFragment

```

Parse HTML5 fragment input from a String, and return a new HTML5::DocumentFragment. This method creates a new, empty HTML5::Document to contain the fragment.
Parameters

- 

`input` (String | IO) The HTML5 document fragment to parse.

Optional Keyword Arguments

- 

`encoding:` (String | Encoding) The encoding, or name of the encoding, that should be used when processing the document. When not provided, the encoding will be determined based on the document content. Also see Nokogiri::HTML5 for a longer explanation of how encoding is handled by the parser.

- 

`context:` (String | Nokogiri::XML::Node) The node, or the name of an HTML5 element, “in context” of which to parse the document fragment. See below for more information. (default “body”)

- 

`max_errors:` (Integer) The maximum number of parse errors to record. (default `Nokogiri::Gumbo::DEFAULT_MAX_ERRORS` which is currently 0)

- 

`max_tree_depth:` (Integer) The maximum depth of the parse tree. (default `Nokogiri::Gumbo::DEFAULT_MAX_TREE_DEPTH`)

- 

`max_attributes:` (Integer) The maximum number of attributes allowed on an element. (default `Nokogiri::Gumbo::DEFAULT_MAX_ATTRIBUTES`)

- 

`parse_noscript_content_as_text:` (Boolean) Whether to parse the content of `noscript` elements as text. (default `false`)

See HTML5@Parsing+options for a complete description of these parsing options.
Returns

Nokogiri::HTML5::DocumentFragment

### Context Node

If a context node is specified using `context:`, then the parser will behave as if that Node, or a hypothetical tag named as specified, is the parent of the fragment subtree.

  

  

  
    
      

```

69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
```

    
    
      

```
# File 'lib/nokogiri/html5/document_fragment.rb', line 69

def parse(
  input,
  encoding_ = nil, positional_options_hash = nil,
  encoding: encoding_, **options
)
  unless positional_options_hash.nil? || positional_options_hash.empty?
    options.merge!(positional_options_hash)
  end

  context = options.delete(:context)

  document = HTML5::Document.new
  document.encoding = "UTF-8"
  input = HTML5.read_and_encode(input, encoding)

  new(document, input, context, options)
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**extract_params**(params)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
```

    
    
      

```
# File 'lib/nokogiri/html5/document_fragment.rb', line 175

def extract_params(params) # :nodoc:
  handler = params.find do |param|
    ![Hash, String, Symbol].include?(param.class)
  end
  params -= [handler] if handler

  hashes = []
  while Hash === params.last || params.last.nil?
    hashes << params.pop
    break if params.empty?
  end
  ns, binds = hashes.reverse

  ns ||=
    begin
      ns = {}
      children.each { |child| ns.merge!(child.namespaces) }
      ns
    end

  [params, handler, ns, binds]
end
```

    
  

    
      
  
### 
  
    #**serialize**(options = {}, &block)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

169
170
171
172
173
```

    
    
      

```
# File 'lib/nokogiri/html5/document_fragment.rb', line 169

def serialize(options = {}, &block) # :nodoc:
  # Bypass XML::Document.serialize which doesn't support options even
  # though XML::Node.serialize does!
  XML::Node.instance_method(:serialize).bind_call(self, options, &block)
end
```