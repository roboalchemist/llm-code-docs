# Class: Nokogiri::HTML4::Document
  
  
  

  
  
    Inherits:
    
      XML::Document
      
        

          
- Object
          
            
- XML::Node
          
            
- XML::Document
          
            
- Nokogiri::HTML4::Document
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/html4/document.rb,

  ext/nokogiri/html4_document.c

  
  

  
## Direct Known Subclasses

  

Nokogiri::HTML5::Document

  
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

  
## Instance Attribute Summary

  
  
### Attributes inherited from XML::Document

  

#errors, #namespace_inheritance

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**new**(uri = nil, external_id = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a new empty document with base URI `uri` and external ID `external_id`.

  

      
        
- 
  
    
      .**parse**(input, url_ = nil, encoding_ = nil, options_ = XML::ParseOptions::DEFAULT_HTML, url: url_, encoding: encoding_, options: options_) {|options| ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   parse(input) { |options| … } => Nokogiri::HTML4::Document   parse(input, url:, encoding:, options:) => Nokogiri::HTML4::Document.

  

      
        
- 
  
    
      .**read_io**(io, url, encoding, options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Read the HTML document from `io` with given `url`, `encoding`, and `options`.

  

      
        
- 
  
    
      .**read_memory**(string, url, encoding, options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Read the HTML document contained in `string` with given `url`, `encoding`, and `options`.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**fragment**(tags = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a Nokogiri::XML::DocumentFragment from `tags`.

  

      
        
- 
  
    
      #**meta_encoding**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the meta tag encoding for this document.

  

      
        
- 
  
    
      #**meta_encoding=**(encoding)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Set the meta tag encoding for this document.

  

      
        
- 
  
    
      #**serialize**(options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Serialize Node using `options`.

  

      
        
- 
  
    
      #**title**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the title string of this document.

  

      
        
- 
  
    
      #**title=**(text)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Set the title string of this document.

  

      
        
- 
  
    
      #**type**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The type for this document.

  

      
        
- 
  
    
      #**xpath_doctype**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   xpath_doctype() → Nokogiri::CSS::XPathVisitor::DoctypeConfig.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from XML::Document

  

#add_child, #canonicalize, #clone, #collect_namespaces, #create_cdata, #create_comment, #create_element, #create_entity, #create_text_node, #deconstruct_keys, #decorate, #decorators, #document, #dup, #encoding, #encoding=, #initialize, #name, #namespaces, #remove_namespaces!, #root, #root=, #slop!, #url, #validate, #version

  
  
  
  
  
  
  
  
  
### Methods inherited from XML::Node

  

#<<, #<=>, #==, #[], #[]=, #accept, #add_child, #add_class, #add_namespace_definition, #add_next_sibling, #add_previous_sibling, #after, #ancestors, #append_class, #attribute, #attribute_nodes, #attribute_with_ns, #attributes, #before, #blank?, #canonicalize, #cdata?, #child, #children, #children=, #classes, #clone, #comment?, #content, #content=, #create_external_subset, #create_internal_subset, #css_path, #data_ptr?, #deconstruct_keys, #decorate!, #default_namespace=, #description, #do_xinclude, #document, #document?, #dup, #each, #element?, #element_children, #encode_special_chars, #external_subset, #first_element_child, #fragment?, #html?, #initialize, #inner_html, #inner_html=, #internal_subset, #key?, #keys, #kwattr_add, #kwattr_append, #kwattr_remove, #kwattr_values, #lang, #lang=, #last_element_child, #line, #line=, #matches?, #namespace, #namespace=, #namespace_definitions, #namespace_scopes, #namespaced_key?, #namespaces, #native_content=, #next_element, #next_sibling, #node_name, #node_name=, #node_type, #parent, #parent=, #parse, #path, #pointer_id, #prepend_child, #previous_element, #previous_sibling, #processing_instruction?, #read_only?, #remove_attribute, #remove_class, #replace, #swap, #text?, #to_html, #to_s, #to_xhtml, #to_xml, #traverse, #unlink, #value?, #values, #wrap, #write_html_to, #write_to, #write_xhtml_to, #write_xml_to, #xml?

  
  
  
  
  
  
  
  
  
  
### Methods included from ClassResolver

  

#related_class

  
  
  
  
  
  
  
  
  
### Methods included from XML::Searchable

  

#>, #at, #at_css, #at_xpath, #css, #search, #xpath

  
  
  
  
  
  
  
  
  
### Methods included from XML::PP::Node

  

#inspect, #pretty_print

  
  
  
  
  
  
  
  
  
### Methods included from Nokogiri::HTML5::Node

  

#inner_html, #write_to

  
## Constructor Details

  
    

This class inherits a constructor from Nokogiri::XML::Document
  

  
    
## Class Method Details

    
      
  
### 
  
    .**new**(uri = nil, external_id = nil)  ⇒ Object 
  

  

  

  
    

Create a new empty document with base URI `uri` and external ID `external_id`.

  

  
  

  
    
      

```

14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
```

    
    
      

```
# File 'ext/nokogiri/html4_document.c', line 14

static VALUE
rb_html_document_s_new(int argc, VALUE *argv, VALUE klass)
{
  VALUE uri, external_id, rest, rb_doc;
  htmlDocPtr doc;

  rb_scan_args(argc, argv, "0*", &rest);
  uri = rb_ary_entry(rest, (long)0);
  external_id = rb_ary_entry(rest, (long)1);

  doc = htmlNewDoc(
          RTEST(uri) ? (const xmlChar *)StringValueCStr(uri) : NULL,
          RTEST(external_id) ? (const xmlChar *)StringValueCStr(external_id) : NULL
        );
  rb_doc = noko_xml_document_wrap_with_init_args(klass, doc, argc, argv);
  return rb_doc ;
}

```

    
  

    
      
  
### 
  
    .**parse**(input, url_ = nil, encoding_ = nil, options_ = XML::ParseOptions::DEFAULT_HTML, url: url_, encoding: encoding_, options: options_) {|options| ... } ⇒ Object 
  

  

  

  
    

:call-seq:

```
parse(input) { |options| ... } => Nokogiri::HTML4::Document
parse(input, url:, encoding:, options:) => Nokogiri::HTML4::Document

```

Parse HTML4 input from a String or IO object, and return a new HTML4::Document.
Required Parameters

- 

`input` (String | IO) The content to be parsed.

Optional Keyword Arguments

- 

`url:` (String) The base URI for this document.

- 

`encoding:` (String) The name of the encoding that should be used when processing the document. When not provided, the encoding will be determined based on the document content.

- 

`options:` (Nokogiri::XML::ParseOptions) Configuration object that determines some behaviors during parsing. See ParseOptions for more information. The default value is `ParseOptions::DEFAULT_HTML`.

Yields

If a block is given, a Nokogiri::XML::ParseOptions object is yielded to the block which can be configured before parsing. See Nokogiri::XML::ParseOptions for more information.
Returns

Nokogiri::HTML4::Document

  

  

Yields:

  
    
- 
      
      
        (options)
      
      
      
    
  

  
    
      

```

189
190
191
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
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
```

    
    
      

```
# File 'lib/nokogiri/html4/document.rb', line 189

def parse(
  input,
  url_ = nil, encoding_ = nil, options_ = XML::ParseOptions::DEFAULT_HTML,
  url: url_, encoding: encoding_, options: options_
)
  options = Nokogiri::XML::ParseOptions.new(options) if Integer === options
  yield options if block_given?

  url ||= input.respond_to?(:path) ? input.path : nil

  if input.respond_to?(:encoding)
    unless input.encoding == Encoding::ASCII_8BIT
      encoding ||= input.encoding.name
    end
  end

  if input.respond_to?(:read)
    if input.is_a?(Pathname)
      # resolve the Pathname to the file and open it as an IO object, see #2110
      input = input.expand_path.open
      url ||= input.path
    end

    unless encoding
      input = EncodingReader.new(input)
      begin
        return read_io(input, url, encoding, options.to_i)
      rescue EncodingReader::EncodingFound => e
        encoding = e.found_encoding
      end
    end
    return read_io(input, url, encoding, options.to_i)
  end

  # read_memory pukes on empty docs
  if input.nil? || input.empty?
    return encoding ? new.tap { |i| i.encoding = encoding } : new
  end

  encoding ||= EncodingReader.detect_encoding(input)

  read_memory(input, url, encoding, options.to_i)
end

```

    
  

    
      
  
### 
  
    .**read_io**(io, url, encoding, options)  ⇒ Object 
  

  

  

  
    

Read the HTML document from `io` with given `url`, `encoding`, and `options`.  See Nokogiri::HTML4.parse

  

  
  

  
    
      

```

39
40
41
42
43
44
45
46
47
48
49
50
51
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
```

    
    
      

```
# File 'ext/nokogiri/html4_document.c', line 39

static VALUE
rb_html_document_s_read_io(VALUE klass, VALUE rb_io, VALUE rb_url, VALUE rb_encoding, VALUE rb_options)
{
  VALUE rb_doc;
  VALUE rb_error_list = rb_ary_new();
  htmlDocPtr c_doc;
  const char *c_url = NIL_P(rb_url) ? NULL : StringValueCStr(rb_url);
  const char *c_encoding = NIL_P(rb_encoding) ? NULL : StringValueCStr(rb_encoding);
  int options = NUM2INT(rb_options);

  xmlSetStructuredErrorFunc((void *)rb_error_list, noko__error_array_pusher);

  c_doc = htmlReadIO(noko_io_read, noko_io_close, (void *)rb_io, c_url, c_encoding, options);

  xmlSetStructuredErrorFunc(NULL, NULL);

  /*
   * If EncodingFound has occurred in EncodingReader, make sure to do
   * a cleanup and propagate the error.
   */
  if (rb_respond_to(rb_io, id_encoding_found)) {
    VALUE encoding_found = rb_funcall(rb_io, id_encoding_found, 0);
    if (!NIL_P(encoding_found)) {
      xmlFreeDoc(c_doc);
      rb_exc_raise(encoding_found);
    }
  }

  if ((c_doc == NULL) || (!(options & XML_PARSE_RECOVER) && (RARRAY_LEN(rb_error_list) > 0))) {
    VALUE rb_error ;

    xmlFreeDoc(c_doc);

    rb_error = rb_ary_entry(rb_error_list, 0);
    if (rb_error == Qnil) {
      rb_raise(rb_eRuntimeError, "Could not parse document");
    } else {
      VALUE exception_message = rb_funcall(rb_error, id_to_s, 0);
      exception_message = rb_str_concat(rb_str_new2("Parser without recover option encountered error or warning: "),
                                        exception_message);
      rb_exc_raise(rb_class_new_instance(1, &exception_message, cNokogiriXmlSyntaxError));
    }

    return Qnil;
  }

  rb_doc = noko_xml_document_wrap(klass, c_doc);
  rb_iv_set(rb_doc, "@errors", rb_error_list);
  return rb_doc;
}

```

    
  

    
      
  
### 
  
    .**read_memory**(string, url, encoding, options)  ⇒ Object 
  

  

  

  
    

Read the HTML document contained in `string` with given `url`, `encoding`, and `options`.  See Nokogiri::HTML4.parse

  

  
  

  
    
      

```

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
125
126
127
128
129
130
131
132
133
134
135
136
```

    
    
      

```
# File 'ext/nokogiri/html4_document.c', line 97

static VALUE
rb_html_document_s_read_memory(VALUE klass, VALUE rb_html, VALUE rb_url, VALUE rb_encoding, VALUE rb_options)
{
  VALUE rb_doc;
  VALUE rb_error_list = rb_ary_new();
  htmlDocPtr c_doc;
  const char *c_buffer = StringValuePtr(rb_html);
  const char *c_url = NIL_P(rb_url) ? NULL : StringValueCStr(rb_url);
  const char *c_encoding = NIL_P(rb_encoding) ? NULL : StringValueCStr(rb_encoding);
  int html_len = (int)RSTRING_LEN(rb_html);
  int options = NUM2INT(rb_options);

  xmlSetStructuredErrorFunc((void *)rb_error_list, noko__error_array_pusher);

  c_doc = htmlReadMemory(c_buffer, html_len, c_url, c_encoding, options);

  xmlSetStructuredErrorFunc(NULL, NULL);

  if ((c_doc == NULL) || (!(options & XML_PARSE_RECOVER) && (RARRAY_LEN(rb_error_list) > 0))) {
    VALUE rb_error ;

    xmlFreeDoc(c_doc);

    rb_error = rb_ary_entry(rb_error_list, 0);
    if (rb_error == Qnil) {
      rb_raise(rb_eRuntimeError, "Could not parse document");
    } else {
      VALUE exception_message = rb_funcall(rb_error, id_to_s, 0);
      exception_message = rb_str_concat(rb_str_new2("Parser without recover option encountered error or warning: "),
                                        exception_message);
      rb_exc_raise(rb_class_new_instance(1, &exception_message, cNokogiriXmlSyntaxError));
    }

    return Qnil;
  }

  rb_doc = noko_xml_document_wrap(klass, c_doc);
  rb_iv_set(rb_doc, "@errors", rb_error_list);
  return rb_doc;
}

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**fragment**(tags = nil)  ⇒ Object 
  

  

  

  
    

Create a Nokogiri::XML::DocumentFragment from `tags`

  

  

  
    
      

```

149
150
151
```

    
    
      

```
# File 'lib/nokogiri/html4/document.rb', line 149

def fragment(tags = nil)
  DocumentFragment.new(self, tags, root)
end

```

    
  

    
      
  
### 
  
    #**meta_encoding**  ⇒ Object 
  

  

  

  
    

Get the meta tag encoding for this document.  If there is no meta tag, then nil is returned.

  

  

  
    
      

```

12
13
14
15
16
17
18
```

    
    
      

```
# File 'lib/nokogiri/html4/document.rb', line 12

def meta_encoding
  if (meta = at_xpath("//meta[@charset]"))
    meta[:charset]
  elsif (meta = meta_content_type)
    meta["content"][/charset\s*=\s*([\w-]+)/i, 1]
  end
end

```

    
  

    
      
  
### 
  
    #**meta_encoding=**(encoding)  ⇒ Object 
  

  

  

  
    

Set the meta tag encoding for this document.

If an meta encoding tag is already present, its content is replaced with the given text.

Otherwise, this method tries to create one at an appropriate place supplying head and/or html elements as necessary, which is inside a head element if any, and before any text node or content element (typically <body>) if any.

The result when trying to set an encoding that is different from the document encoding is undefined.

Beware in CRuby, that libxml2 automatically inserts a meta tag into a head element.

  

  

  
    
      

```

36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
```

    
    
      

```
# File 'lib/nokogiri/html4/document.rb', line 36

def meta_encoding=(encoding)
  if (meta = meta_content_type)
    meta["content"] = format("text/html; charset=%s", encoding)
    encoding
  elsif (meta = at_xpath("//meta[@charset]"))
    meta["charset"] = encoding
  else
    meta = XML::Node.new("meta", self)
    if (dtd = internal_subset) && dtd.html5_dtd?
      meta["charset"] = encoding
    else
      meta["http-equiv"] = "Content-Type"
      meta["content"] = format("text/html; charset=%s", encoding)
    end

    if (head = at_xpath("//head"))
      head.prepend_child(meta)
    else
      set_metadata_element(meta)
    end
    encoding
  end
end

```

    
  

    
      
  
### 
  
    #**serialize**(options = {})  ⇒ Object 
  

  

  

  
    

Serialize Node using `options`. Save options can also be set using a block.

See also Nokogiri::XML::Node::SaveOptions and Node@Serialization+and+Generating+Output.

These two statements are equivalent:

```
node.serialize(:encoding => 'UTF-8', :save_with => FORMAT | AS_XML)

```

or

```
node.serialize(:encoding => 'UTF-8') do |config|
  config.format.as_xml
end

```

  

  

  
    
      

```

142
143
144
145
```

    
    
      

```
# File 'lib/nokogiri/html4/document.rb', line 142

def serialize(options = {})
  options[:save_with] ||= XML::Node::SaveOptions::DEFAULT_HTML
  super
end

```

    
  

    
      
  
### 
  
    #**title**  ⇒ Object 
  

  

  

  
    

Get the title string of this document.  Return nil if there is no title tag.

  

  

  
    
      

```

70
71
72
```

    
    
      

```
# File 'lib/nokogiri/html4/document.rb', line 70

def title
  (title = at_xpath("//title")) && title.inner_text
end

```

    
  

    
      
  
### 
  
    #**title=**(text)  ⇒ Object 
  

  

  

  
    

Set the title string of this document.

If a title element is already present, its content is replaced with the given text.

Otherwise, this method tries to create one at an appropriate place supplying head and/or html elements as necessary, which is inside a head element if any, right after a meta encoding/charset tag if any, and before any text node or content element (typically <body>) if any.

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/nokogiri/html4/document.rb', line 85

def title=(text)
  tnode = XML::Text.new(text, self)
  if (title = at_xpath("//title"))
    title.children = tnode
    return text
  end

  title = XML::Node.new("title", self) << tnode
  if (head = at_xpath("//head"))
    head << title
  elsif (meta = at_xpath("//meta[@charset]") || meta_content_type)
    # better put after charset declaration
    meta.add_next_sibling(title)
  else
    set_metadata_element(title)
  end
end

```

    
  

    
      
  
### 
  
    #**type**  ⇒ Object 
  

  

  

  
    

The type for this document

  

  
  

  
    
      

```

144
145
146
147
148
149
```

    
    
      

```
# File 'ext/nokogiri/html4_document.c', line 144

static VALUE
rb_html_document_type(VALUE self)
{
  htmlDocPtr doc = noko_xml_document_unwrap(self);
  return INT2NUM(doc->type);
}

```

    
  

    
      
  
### 
  
    #**xpath_doctype**  ⇒ Object 
  

  

  

  
    

:call-seq:

```
xpath_doctype() 
```

Returns

The document type which determines CSS-to-XPath translation.

See XPathVisitor for more information.

  

  

  
    
      

```

159
160
161
```

    
    
      

```
# File 'lib/nokogiri/html4/document.rb', line 159

def xpath_doctype
  Nokogiri::CSS::XPathVisitor::DoctypeConfig::HTML4
end

```