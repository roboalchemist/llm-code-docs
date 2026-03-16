# Class: Nokogiri::HTML4::DocumentFragment
  
  
  

  
  
    Inherits:
    
      XML::DocumentFragment
      
        

          
- Object
          
            
- XML::Node
          
            
- XML::DocumentFragment
          
            
- Nokogiri::HTML4::DocumentFragment
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/html4/document_fragment.rb
  
  

  
## Direct Known Subclasses

  

Nokogiri::HTML5::DocumentFragment

  
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

  
## Instance Attribute Summary

  
  
### Attributes inherited from XML::DocumentFragment

  

#parse_options

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**parse**(input, encoding_ = nil, options_ = XML::ParseOptions::DEFAULT_HTML, encoding: encoding_, options: options_, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   parse(input) { |options| … } → HTML4::DocumentFragment   parse(input, encoding:, options:) { |options| … } → HTML4::DocumentFragment.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(document, input = nil, context_ = nil, options_ = XML::ParseOptions::DEFAULT_HTML, context: context_, options: options_) {|options| ... } ⇒ DocumentFragment 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

:call-seq:   new(document) { |options| … } → HTML4::DocumentFragment   new(document, input) { |options| … } → HTML4::DocumentFragment   new(document, input, context:, options:) { |options| … } → HTML4::DocumentFragment.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from XML::DocumentFragment

  

#css, #deconstruct, #dup, #errors, #errors=, #fragment, #name, native_new, new, #search, #to_html, #to_s, #to_xhtml, #to_xml

  
  
  
  
  
  
  
  
  
### Methods inherited from XML::Node

  

#<<, #<=>, #==, #[], #[]=, #accept, #add_child, #add_class, #add_namespace_definition, #add_next_sibling, #add_previous_sibling, #after, #ancestors, #append_class, #attribute, #attribute_nodes, #attribute_with_ns, #attributes, #before, #blank?, #canonicalize, #cdata?, #child, #children, #children=, #classes, #clone, #comment?, #content, #content=, #create_external_subset, #create_internal_subset, #css_path, #data_ptr?, #deconstruct_keys, #decorate!, #default_namespace=, #description, #do_xinclude, #document, #document?, #dup, #each, #element?, #element_children, #encode_special_chars, #external_subset, #first_element_child, #fragment, #fragment?, #html?, #inner_html, #inner_html=, #internal_subset, #key?, #keys, #kwattr_add, #kwattr_append, #kwattr_remove, #kwattr_values, #lang, #lang=, #last_element_child, #line, #line=, #matches?, #namespace, #namespace=, #namespace_definitions, #namespace_scopes, #namespaced_key?, #namespaces, #native_content=, new, #next_element, #next_sibling, #node_name, #node_name=, #node_type, #parent, #parent=, #parse, #path, #pointer_id, #prepend_child, #previous_element, #previous_sibling, #processing_instruction?, #read_only?, #remove_attribute, #remove_class, #replace, #serialize, #swap, #text?, #to_html, #to_s, #to_xhtml, #to_xml, #traverse, #unlink, #value?, #values, #wrap, #write_html_to, #write_to, #write_xhtml_to, #write_xml_to, #xml?

  
  
  
  
  
  
  
  
  
  
### Methods included from ClassResolver

  

#related_class

  
  
  
  
  
  
  
  
  
### Methods included from XML::Searchable

  

#>, #at, #at_css, #at_xpath, #css, #search, #xpath

  
  
  
  
  
  
  
  
  
### Methods included from XML::PP::Node

  

#inspect, #pretty_print

  
  
  
  
  
  
  
  
  
### Methods included from Nokogiri::HTML5::Node

  

#fragment, #inner_html, #write_to

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(document, input = nil, context_ = nil, options_ = XML::ParseOptions::DEFAULT_HTML, context: context_, options: options_) {|options| ... } ⇒ DocumentFragment 
  

  

  

  
    

:call-seq:

```
new(document) { |options| ... } 
```

Parse HTML4 fragment input from a String, and return a new HTML4::DocumentFragment.

💡 It’s recommended to use either HTML4::DocumentFragment.parse or XML::Node#parse rather than call this method directly.
Required Parameters

- 

`document` (HTML4::Document) The parent document to associate the returned fragment with.

Optional Parameters

- 

`input` (String) The content to be parsed.

Optional Keyword Arguments

- 

`context:` (Nokogiri::XML::Node) The **context node** for the subtree created. See below for more information.

- 

`options:` (Nokogiri::XML::ParseOptions) Configuration object that determines some behaviors during parsing. See ParseOptions for more information. The default value is `ParseOptions::DEFAULT_HTML`.

Yields

If a block is given, a Nokogiri::XML::ParseOptions object is yielded to the block which can be configured before parsing. See ParseOptions for more information.
Returns

HTML4::DocumentFragment

### Context Node

If a context node is specified using `context:`, then the fragment will be created by calling XML::Node#parse on that node, so the parser will behave as if that Node is the parent of the fragment subtree.

  

  

Yields:

  
    
- 
      
      
        (options)
      
      
      
    
  

  
    
      

```

134
135
136
137
138
139
140
141
142
143
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
```

    
    
      

```
# File 'lib/nokogiri/html4/document_fragment.rb', line 134

def initialize(
  document, input = nil,
  context_ = nil, options_ = XML::ParseOptions::DEFAULT_HTML,
  context: context_, options: options_
) # rubocop:disable Lint/MissingSuper
  return self unless input

  options = Nokogiri::XML::ParseOptions.new(options) if Integer === options
  @parse_options = options
  yield options if block_given?

  if context
    preexisting_errors = document.errors.dup
    node_set = context.parse("<div>#{input}</div>", options)
    node_set.first.children.each { |child| child.parent = self } unless node_set.empty?
    self.errors = document.errors - preexisting_errors
  else
    # This is a horrible hack, but I don't care
    path = if /^\s*?<body/i.match?(input)
      "/html/body"
    else
      "/html/body/node()"
    end

    temp_doc = HTML4::Document.parse("<html><body>#{input}", nil, document.encoding, options)
    temp_doc.xpath(path).each { |child| child.parent = self }
    self.errors = temp_doc.errors
  end
  children
end

```

    
  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**parse**(input, encoding_ = nil, options_ = XML::ParseOptions::DEFAULT_HTML, encoding: encoding_, options: options_, &block)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
parse(input) { |options| ... } 
```

Parse HTML4 fragment input from a String, and return a new HTML4::DocumentFragment. This method creates a new, empty HTML4::Document to contain the fragment.
Required Parameters

- 

`input` (String | IO) The content to be parsed.

Optional Keyword Arguments

- 

`encoding:` (String) The name of the encoding that should be used when processing the document. When not provided, the encoding will be determined based on the document content.

- 

`options:` (Nokogiri::XML::ParseOptions) Configuration object that determines some behaviors during parsing. See ParseOptions for more information. The default value is `ParseOptions::DEFAULT_HTML`.

Yields

If a block is given, a Nokogiri::XML::ParseOptions object is yielded to the block which can be configured before parsing. See ParseOptions for more information.
Returns

HTML4::DocumentFragment

**Example:** Parsing a string

```
fragment = HTML4::DocumentFragment.parse("<div>Hello World</div>")

```

**Example:** Parsing an IO

```
fragment = File.open("fragment.html") do |file|
  HTML4::DocumentFragment.parse(file)
end

```

**Example:** Specifying encoding

```
fragment = HTML4::DocumentFragment.parse(input, encoding: "EUC-JP")

```

**Example:** Setting parse options dynamically

```
HTML4::DocumentFragment.parse("<div>Hello World") do |options|
  options.huge.pedantic
end

```

  

  

  
    
      

```

52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
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
86
87
88
89
90
91
92
93
94
95
```

    
    
      

```
# File 'lib/nokogiri/html4/document_fragment.rb', line 52

def self.parse(
  input,
  encoding_ = nil, options_ = XML::ParseOptions::DEFAULT_HTML,
  encoding: encoding_, options: options_,
  &block
)
  # TODO: this method should take a context node.
  doc = HTML4::Document.new

  if input.respond_to?(:read)
    # Handle IO-like objects (IO, File, StringIO, etc.)
    # The _read_ method of these objects doesn't accept an +encoding+ parameter.
    # Encoding is usually set when the IO object is created or opened,
    # or by using the _set_encoding_ method.
    #
    # 1. If +encoding+ is provided and the object supports _set_encoding_,
    #    set the encoding before reading.
    # 2. Read the content from the IO-like object.
    #
    # Note: After reading, the content's encoding will be:
    # - The encoding set by _set_encoding_ if it was called
    # - The default encoding of the IO object otherwise
    #
    # For StringIO specifically, _set_encoding_ affects only the internal string,
    # not how the data is read out.
    input.set_encoding(encoding) if encoding && input.respond_to?(:set_encoding)
    input = input.read
  end

  encoding ||= if input.respond_to?(:encoding)
    encoding = input.encoding
    if encoding == ::Encoding::ASCII_8BIT
      "UTF-8"
    else
      encoding.name
    end
  else
    "UTF-8"
  end

  doc.encoding = encoding

  new(doc, input, options: options, &block)
end

```