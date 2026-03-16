# Class: Nokogiri::XML::DocumentFragment
  
  
  

  
  
    Inherits:
    
      Node
      
        

          
- Object
          
            
- Node
          
            
- Nokogiri::XML::DocumentFragment
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/document_fragment.rb,

  ext/nokogiri/xml_document_fragment.c

  
  

## Overview

  
    

DocumentFragment represents a fragment of an XML document. It provides the same functionality exposed by XML::Node and can be used to contain one or more XML subtrees.

  

  

  
## Direct Known Subclasses

  

HTML4::DocumentFragment, HTML::DocumentFragment

  
## Constant Summary

  
  
### Constants inherited
     from Node

  

Node::ATTRIBUTE_DECL, Node::ATTRIBUTE_NODE, Node::CDATA_SECTION_NODE, Node::COMMENT_NODE, Node::DECONSTRUCT_KEYS, Node::DECONSTRUCT_METHODS, Node::DOCB_DOCUMENT_NODE, Node::DOCUMENT_FRAG_NODE, Node::DOCUMENT_NODE, Node::DOCUMENT_TYPE_NODE, Node::DTD_NODE, Node::ELEMENT_DECL, Node::ELEMENT_NODE, Node::ENTITY_DECL, Node::ENTITY_NODE, Node::ENTITY_REF_NODE, Node::HTML_DOCUMENT_NODE, Node::NAMESPACE_DECL, Node::NOTATION_NODE, Node::PI_NODE, Node::TEXT_NODE, Node::XINCLUDE_END, Node::XINCLUDE_START

  
  
  
### Constants included
     from ClassResolver

  

ClassResolver::VALID_NAMESPACES

  
  
  
### Constants included
     from Searchable

  

Searchable::LOOKS_LIKE_XPATH

  
  
  
### Constants included
     from PP::Node

  

PP::Node::COLLECTIONS

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**parse_options**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The options used to parse the document fragment.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**native_new**(rb_doc)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      .**new**(document)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Wrapper method to separate the concerns of: - the native object allocator’s parameter (it only requires `document`) - the initializer’s parameters.

  

      
        
- 
  
    
      .**parse**(tags, options_ = ParseOptions::DEFAULT_XML, options: options_, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   parse(input) { |options| … } → XML::DocumentFragment   parse(input, options:) → XML::DocumentFragment.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**css**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

call-seq: css *rules, [namespace-bindings, custom-pseudo-class].

  

      
        
- 
  
    
      #**deconstruct**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: deconstruct() → Array.

  

      
        
- 
  
    
      #**dup**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**errors**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

A list of Nokogiri::XML::SyntaxError found when parsing a document.

  

      
        
- 
  
    
      #**errors=**(things)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**fragment**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(document, tags = nil, context_ = nil, options_ = ParseOptions::DEFAULT_XML, context: context_, options: options_) {|options| ... } ⇒ DocumentFragment 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

:call-seq:   new(document, input=nil) { |options| … } → DocumentFragment   new(document, input=nil, context:, options:) → DocumentFragment.

  

      
        
- 
  
    
      #**name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

return the name for DocumentFragment.

  

      
        
- 
  
    
      #**search**(*rules)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

call-seq: search *paths, [namespace-bindings, xpath-variable-bindings, custom-handler-class].

  

      
        
- 
  
    
      #**to_html**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convert this DocumentFragment to html See Nokogiri::XML::NodeSet#to_html.

  

      
        
- 
  
    
      #**to_s**  ⇒ Object 
    

    
      (also: #serialize)
    
  
  
  
  
  
  
  
  

  
    

Convert this DocumentFragment to a string.

  

      
        
- 
  
    
      #**to_xhtml**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convert this DocumentFragment to xhtml See Nokogiri::XML::NodeSet#to_xhtml.

  

      
        
- 
  
    
      #**to_xml**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convert this DocumentFragment to xml See Nokogiri::XML::NodeSet#to_xml.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Node

  

#<<, #<=>, #==, #[], #[]=, #accept, #add_child, #add_class, #add_namespace_definition, #add_next_sibling, #add_previous_sibling, #after, #ancestors, #append_class, #attribute, #attribute_nodes, #attribute_with_ns, #attributes, #before, #blank?, #canonicalize, #cdata?, #child, #children, #children=, #classes, #clone, #comment?, #content, #content=, #create_external_subset, #create_internal_subset, #css_path, #data_ptr?, #deconstruct_keys, #decorate!, #default_namespace=, #description, #do_xinclude, #document, #document?, #each, #element?, #element_children, #encode_special_chars, #external_subset, #first_element_child, #fragment?, #html?, #inner_html, #inner_html=, #internal_subset, #key?, #keys, #kwattr_add, #kwattr_append, #kwattr_remove, #kwattr_values, #lang, #lang=, #last_element_child, #line, #line=, #matches?, #namespace, #namespace=, #namespace_definitions, #namespace_scopes, #namespaced_key?, #namespaces, #native_content=, #next_element, #next_sibling, #node_name, #node_name=, #node_type, #parent, #parent=, #parse, #path, #pointer_id, #prepend_child, #previous_element, #previous_sibling, #processing_instruction?, #read_only?, #remove_attribute, #remove_class, #replace, #swap, #text?, #traverse, #unlink, #value?, #values, #wrap, #write_html_to, #write_to, #write_xhtml_to, #write_xml_to, #xml?

  
  
  
  
  
  
  
  
  
  
### Methods included from ClassResolver

  

#related_class

  
  
  
  
  
  
  
  
  
### Methods included from Searchable

  

#>, #at, #at_css, #at_xpath, #xpath

  
  
  
  
  
  
  
  
  
### Methods included from PP::Node

  

#inspect, #pretty_print

  
  
  
  
  
  
  
  
  
### Methods included from HTML5::Node

  

#inner_html, #write_to

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(document, tags = nil, context_ = nil, options_ = ParseOptions::DEFAULT_XML, context: context_, options: options_) {|options| ... } ⇒ DocumentFragment 
  

  

  

  
    

:call-seq:

```
new(document, input=nil) { |options| ... } → DocumentFragment
new(document, input=nil, context:, options:) → DocumentFragment

```

Parse XML fragment input from a String, and return a new DocumentFragment that is associated with the given `document`.

💡 It’s recommended to use either XML::DocumentFragment.parse or Node#parse rather than call this method directly.
Required Parameters

- 

`document` (XML::Document) The parent document to associate the returned fragment with.

Optional Parameters

- 

`input` (String) The content to be parsed.

Optional Keyword Arguments

- 

`context:` (Nokogiri::XML::Node) The **context node** for the subtree created. See below for more information.

- 

`options:` (Nokogiri::XML::ParseOptions) Configuration object that determines some behaviors during parsing. See ParseOptions for more information. The default value is `ParseOptions::DEFAULT_XML`.

Yields

If a block is given, a Nokogiri::XML::ParseOptions object is yielded to the block which can be configured before parsing. See ParseOptions for more information.
Returns

XML::DocumentFragment

### Context Node

If a context node is specified using `context:`, then the fragment will be created by calling Node#parse on that node, so the parser will behave as if that Node is the parent of the fragment subtree, and will resolve namespaces relative to that node.

  

  

Yields:

  
    
- 
      
      
        (options)
      
      
      
    
  

  
    
      

```

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
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
```

    
    
      

```
# File 'lib/nokogiri/xml/document_fragment.rb', line 85

def initialize(
  document, tags = nil,
  context_ = nil, options_ = ParseOptions::DEFAULT_XML,
  context: context_, options: options_
) # rubocop:disable Lint/MissingSuper
  return self unless tags

  options = Nokogiri::XML::ParseOptions.new(options) if Integer === options
  @parse_options = options
  yield options if block_given?

  children = if context
    # Fix for issue#490
    if Nokogiri.jruby?
      # fix for issue #770
      context.parse("<root #{namespace_declarations(context)}>#{tags}</root>", options).children
    else
      context.parse(tags, options)
    end
  else
    wrapper_doc = XML::Document.parse("<root>#{tags}</root>", nil, nil, options)
    self.errors = wrapper_doc.errors
    wrapper_doc.xpath("/root/node()")
  end
  children.each { |child| child.parent = self }
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**parse_options**  ⇒ Object  (readonly)
  

  

  

  
    

The options used to parse the document fragment. Returns the value of any options that were passed into the constructor as a parameter or set in a config block, else the default options for the specific subclass.

  

  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/nokogiri/xml/document_fragment.rb', line 12

def parse_options
  @parse_options
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**native_new**(rb_doc)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

6
7
8
9
10
11
12
13
14
15
16
17
18
19
```

    
    
      

```
# File 'ext/nokogiri/xml_document_fragment.c', line 6

static VALUE
noko_xml_document_fragment_s_native_new(VALUE klass, VALUE rb_doc)
{
  xmlDocPtr c_doc;
  xmlNodePtr c_node;
  VALUE rb_node;

  c_doc = noko_xml_document_unwrap(rb_doc);
  c_node = xmlNewDocFragment(c_doc->doc);
  noko_xml_document_pin_node(c_node);
  rb_node = noko_xml_node_wrap(klass, c_node);

  return rb_node;
}
```

    
  

    
      
  
### 
  
    .**new**(document)  ⇒ Object 
  

  

  

  
    

Wrapper method to separate the concerns of:

- 

the native object allocator’s parameter (it only requires `document`)

- 

the initializer’s parameters

  

  

  
    
      

```

42
43
44
45
46
```

    
    
      

```
# File 'lib/nokogiri/xml/document_fragment.rb', line 42

def new(document, ...) # :nodoc:
  instance = native_new(document)
  instance.send(:initialize, document, ...)
  instance
end
```

    
  

    
      
  
### 
  
    .**parse**(tags, options_ = ParseOptions::DEFAULT_XML, options: options_, &block)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
parse(input) { |options| ... } → XML::DocumentFragment
parse(input, options:) → XML::DocumentFragment

```

Parse XML fragment input from a String, and return a new XML::DocumentFragment. This method creates a new, empty XML::Document to contain the fragment.
Required Parameters

- 

`input` (String) The content to be parsed.

Optional Keyword Arguments

- 

`options` (Nokogiri::XML::ParseOptions) Configuration object that determines some behaviors during parsing. See ParseOptions for more information. The default value is `ParseOptions::DEFAULT_XML`.

Yields

If a block is given, a Nokogiri::XML::ParseOptions object is yielded to the block which can be configured before parsing. See Nokogiri::XML::ParseOptions for more information.
Returns

Nokogiri::XML::DocumentFragment

  

  

  
    
      

```

35
36
37
```

    
    
      

```
# File 'lib/nokogiri/xml/document_fragment.rb', line 35

def parse(tags, options_ = ParseOptions::DEFAULT_XML, options: options_, &block)
  new(XML::Document.new, tags, options: options, &block)
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**css**(*args)  ⇒ Object 
  

  

  

  
    

call-seq: css *rules, [namespace-bindings, custom-pseudo-class]

Search this fragment for CSS `rules`. `rules` must be one or more CSS selectors. For example:

For more information see Nokogiri::XML::Searchable#css

  

  

  
    
      

```

173
174
175
176
177
178
179
```

    
    
      

```
# File 'lib/nokogiri/xml/document_fragment.rb', line 173

def css(*args)
  if children.any?
    children.css(*args) # 'children' is a smell here
  else
    NodeSet.new(document)
  end
end
```

    
  

    
      
  
### 
  
    #**deconstruct**  ⇒ Object 
  

  

  

  
    

:call-seq: deconstruct() → Array

```
Returns the root nodes of this document fragment as an array, to use in pattern matching.

💡 Note that text nodes are returned as well as elements. If you wish to operate only on
root elements, you should deconstruct the array returned by
<tt>DocumentFragment#elements</tt>.

*Example*

  frag = Nokogiri::HTML5.fragment(<<~HTML)
    <div>Start</div>
    This is a <a href="#jump">shortcut</a> for you.
    <div>End</div>
  HTML

  frag.deconstruct
  # => [#(Element:0x35c { name = "div", children = [ #(Text "Start")] }),
  #     #(Text "\n" + "This is a "),
  #     #(Element:0x370 {
  #       name = "a",
  #       attributes = [ #(Attr:0x384 { name = "href", value = "#jump" })],
  #       children = [ #(Text "shortcut")]
  #       }),
  #     #(Text " for you.\n"),
  #     #(Element:0x398 { name = "div", children = [ #(Text "End")] }),
  #     #(Text "\n")]

*Example* only the elements, not the text nodes.

  frag.elements.deconstruct
  # => [#(Element:0x35c { name = "div", children = [ #(Text "Start")] }),
  #     #(Element:0x370 {
  #       name = "a",
  #       attributes = [ #(Attr:0x384 { name = "href", value = "#jump" })],
  #       children = [ #(Text "shortcut")]
  #       }),
  #     #(Element:0x398 { name = "div", children = [ #(Text "End")] })]

Since v1.14.0

```

  

  

  
    
      

```

261
262
263
```

    
    
      

```
# File 'lib/nokogiri/xml/document_fragment.rb', line 261

def deconstruct
  children.to_a
end
```

    
  

    
      
  
### 
  
    #**dup**  ⇒ Object 
  

  

  

  
    
      

```

113
114
115
116
117
118
119
120
```

    
    
      

```
# File 'lib/nokogiri/xml/document_fragment.rb', line 113

def dup
  new_document = document.dup
  new_fragment = self.class.new(new_document)
  children.each do |child|
    child.dup(1, new_document).parent = new_fragment
  end
  new_fragment
end
```

    
  

    
      
  
### 
  
    #**errors**  ⇒ Object 
  

  

  

  
    

A list of Nokogiri::XML::SyntaxError found when parsing a document

  

  

  
    
      

```

207
208
209
```

    
    
      

```
# File 'lib/nokogiri/xml/document_fragment.rb', line 207

def errors
  document.errors
end
```

    
  

    
      
  
### 
  
    #**errors=**(things)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

211
212
213
```

    
    
      

```
# File 'lib/nokogiri/xml/document_fragment.rb', line 211

def errors=(things) # :nodoc:
  document.errors = things
end
```

    
  

    
      
  
### 
  
    #**fragment**(data)  ⇒ Object 
  

  

  

  
    
      

```

215
216
217
```

    
    
      

```
# File 'lib/nokogiri/xml/document_fragment.rb', line 215

def fragment(data)
  document.fragment(data)
end
```

    
  

    
      
  
### 
  
    #**name**  ⇒ Object 
  

  

  

  
    

return the name for DocumentFragment

  

  

  
    
      

```

125
126
127
```

    
    
      

```
# File 'lib/nokogiri/xml/document_fragment.rb', line 125

def name
  "#document-fragment"
end
```

    
  

    
      
  
### 
  
    #**search**(*rules)  ⇒ Object 
  

  

  

  
    

call-seq: search *paths, [namespace-bindings, xpath-variable-bindings, custom-handler-class]

Search this fragment for `paths`. `paths` must be one or more XPath or CSS queries.

For more information see Nokogiri::XML::Searchable#search

  

  

  
    
      

```

192
193
194
195
196
197
198
199
200
201
202
```

    
    
      

```
# File 'lib/nokogiri/xml/document_fragment.rb', line 192

def search(*rules)
  rules, handler, ns, binds = extract_params(rules)

  rules.inject(NodeSet.new(document)) do |set, rule|
    set + if Searchable::LOOKS_LIKE_XPATH.match?(rule)
      xpath(*[rule, ns, handler, binds].compact)
    else
      children.css(*[rule, ns, handler].compact) # 'children' is a smell here
    end
  end
end
```

    
  

    
      
  
### 
  
    #**to_html**(*args)  ⇒ Object 
  

  

  

  
    

Convert this DocumentFragment to html See Nokogiri::XML::NodeSet#to_html

  

  

  
    
      

```

138
139
140
141
142
143
144
145
```

    
    
      

```
# File 'lib/nokogiri/xml/document_fragment.rb', line 138

def to_html(*args)
  if Nokogiri.jruby?
    options = args.first.is_a?(Hash) ? args.shift : {}
    options[:save_with] ||= Node::SaveOptions::DEFAULT_HTML
    args.insert(0, options)
  end
  children.to_html(*args)
end
```

    
  

    
      
  
### 
  
    #**to_s**  ⇒ Object 
  

  
    Also known as:
    serialize
    
  

  

  
    

Convert this DocumentFragment to a string

  

  

  
    
      

```

131
132
133
```

    
    
      

```
# File 'lib/nokogiri/xml/document_fragment.rb', line 131

def to_s
  children.to_s
end
```

    
  

    
      
  
### 
  
    #**to_xhtml**(*args)  ⇒ Object 
  

  

  

  
    

Convert this DocumentFragment to xhtml See Nokogiri::XML::NodeSet#to_xhtml

  

  

  
    
      

```

150
151
152
153
154
155
156
157
```

    
    
      

```
# File 'lib/nokogiri/xml/document_fragment.rb', line 150

def to_xhtml(*args)
  if Nokogiri.jruby?
    options = args.first.is_a?(Hash) ? args.shift : {}
    options[:save_with] ||= Node::SaveOptions::DEFAULT_XHTML
    args.insert(0, options)
  end
  children.to_xhtml(*args)
end
```

    
  

    
      
  
### 
  
    #**to_xml**(*args)  ⇒ Object 
  

  

  

  
    

Convert this DocumentFragment to xml See Nokogiri::XML::NodeSet#to_xml

  

  

  
    
      

```

162
163
164
```

    
    
      

```
# File 'lib/nokogiri/xml/document_fragment.rb', line 162

def to_xml(*args)
  children.to_xml(*args)
end
```