# Class: Nokogiri::XML::Document
  
  
  

  
  
    Inherits:
    
      Node
      
        

          
- Object
          
            
- Node
          
            
- Nokogiri::XML::Document
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/document.rb,

  ext/nokogiri/xml_document.c

  
  

## Overview

  
    

Nokogiri::XML::Document is the main entry point for dealing with XML documents. The Document is created by parsing XML content from a String or an IO object. See Nokogiri::XML::Document.parse for more information on parsing.

Document inherits a great deal of functionality from its superclass Nokogiri::XML::Node, so please read that class’s documentation as well.

  

  

  
## Direct Known Subclasses

  

HTML4::Document, HTML::Document

  
    
## 
      Constant Summary
      collapse
    

    
      
        NCNAME_START_CHAR =
          
  
    

See www.w3.org/TR/REC-xml-names/#ns-decl for more details. Note that we’re not attempting to handle unicode characters partly because libxml2 doesn’t handle unicode characters in NCNAMEs.

  

  

        
        

```
"A-Za-z_"

```

      
        NCNAME_CHAR =
          
        
        

```
NCNAME_START_CHAR + "\\-\\.0-9"

```

      
        NCNAME_RE =
          
        
        

```
/^xmlns(?::([#{NCNAME_START_CHAR}][#{NCNAME_CHAR}]*))?$/

```

      
    
  

  
  
  
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
  
    
      #**errors**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

The errors found while parsing a document.

  

    
      
- 
  
    
      #**namespace_inheritance**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

When `true`, reparented elements without a namespace will inherit their new parent’s namespace (if one exists).

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**new**(version = "1.0")  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a new empty document declaring XML version `version`.

  

      
        
- 
  
    
      .**parse**(string_or_io, url_ = nil, encoding_ = nil, options_ = XML::ParseOptions::DEFAULT_XML, url: url_, encoding: encoding_, options: options_) {|options| ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

call-seq:   parse(input) { |options| … } => Nokogiri::XML::Document   parse(input, url:, encoding:, options:) => Nokogiri::XML::Document.

  

      
        
- 
  
    
      .**read_io**(io, url, encoding, options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a new document from an IO object.

  

      
        
- 
  
    
      .**read_memory**(string, url, encoding, options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a new document from a String.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**add_child**(node_or_tags)  ⇒ Object 
    

    
      (also: #<<)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**canonicalize**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Canonicalize a document and return the results.

  

      
        
- 
  
    
      #**clone**(level = 1)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   clone → Nokogiri::XML::Document   clone(level) → Nokogiri::XML::Document.

  

      
        
- 
  
    
      #**collect_namespaces**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   collect_namespaces() → Hash<String(Namespace#prefix) ⇒ String(Namespace#href)>.

  

      
        
- 
  
    
      #**create_cdata**(string, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a CDATA Node containing `string`.

  

      
        
- 
  
    
      #**create_comment**(string, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a Comment Node containing `string`.

  

      
        
- 
  
    
      #**create_element**(name, *contents_or_attrs, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   create_element(name, *contents_or_attrs, &block) → Nokogiri::XML::Element.

  

      
        
- 
  
    
      #**create_entity**(name, type, external_id, system_id, content)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a new entity named `name`.

  

      
        
- 
  
    
      #**create_text_node**(string, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a Text Node with `string`.

  

      
        
- 
  
    
      #**deconstruct_keys**(keys)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: deconstruct_keys(array_of_names) → Hash.

  

      
        
- 
  
    
      #**decorate**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Apply any decorators to `node`.

  

      
        
- 
  
    
      #**decorators**(key)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the list of decorators given `key`.

  

      
        
- 
  
    
      #**document**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

A reference to `self`.

  

      
        
- 
  
    
      #**dup**(level = 1)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   dup → Nokogiri::XML::Document   dup(level) → Nokogiri::XML::Document.

  

      
        
- 
  
    
      #**encoding**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the encoding for this Document.

  

      
        
- 
  
    
      #**encoding=**(encoding)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Set the encoding string for this Document.

  

      
        
- 
  
    
      #**fragment**(tags = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a Nokogiri::XML::DocumentFragment from `tags` Returns an empty fragment if `tags` is nil.

  

      
        
- 
  
    
      #**initialize**(*args)  ⇒ Document 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

:nodoc: # rubocop:disable Lint/MissingSuper.

  

      
        
- 
  
    
      #**name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The name of this document.

  

      
        
- 
  
    
      #**namespaces**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the hash of namespaces on the root Nokogiri::XML::Node.

  

      
        
- 
  
    
      #**remove_namespaces!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Remove all namespaces from all nodes in the document.

  

      
        
- 
  
    
      #**root**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the root node for this document.

  

      
        
- 
  
    
      #**root=**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Set the root element on this document.

  

      
        
- 
  
    
      #**slop!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Explore a document with shortcut methods.

  

      
        
- 
  
    
      #**url**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the url name for this document.

  

      
        
- 
  
    
      #**validate**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Validate this Document against its DTD.

  

      
        
- 
  
    
      #**version**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the XML version for this Document.

  

      
        
- 
  
    
      #**xpath_doctype**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   xpath_doctype() → Nokogiri::CSS::XPathVisitor::DoctypeConfig.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Node

  

#<=>, #==, #[], #[]=, #accept, #add_class, #add_namespace_definition, #add_next_sibling, #add_previous_sibling, #after, #ancestors, #append_class, #attribute, #attribute_nodes, #attribute_with_ns, #attributes, #before, #blank?, #cdata?, #child, #children, #children=, #classes, #comment?, #content, #content=, #create_external_subset, #create_internal_subset, #css_path, #data_ptr?, #decorate!, #default_namespace=, #description, #do_xinclude, #document?, #each, #element?, #element_children, #encode_special_chars, #external_subset, #first_element_child, #fragment?, #html?, #inner_html, #inner_html=, #internal_subset, #key?, #keys, #kwattr_add, #kwattr_append, #kwattr_remove, #kwattr_values, #lang, #lang=, #last_element_child, #line, #line=, #matches?, #namespace, #namespace=, #namespace_definitions, #namespace_scopes, #namespaced_key?, #native_content=, #next_element, #next_sibling, #node_name, #node_name=, #node_type, #parent, #parent=, #parse, #path, #pointer_id, #prepend_child, #previous_element, #previous_sibling, #processing_instruction?, #read_only?, #remove_attribute, #remove_class, #replace, #serialize, #swap, #text?, #to_html, #to_s, #to_xhtml, #traverse, #unlink, #value?, #values, #wrap, #write_html_to, #write_to, #write_xhtml_to, #write_xml_to, #xml?

  
  
  
  
  
  
  
  
  
  
### Methods included from ClassResolver

  

#related_class

  
  
  
  
  
  
  
  
  
### Methods included from Searchable

  

#>, #at, #at_css, #at_xpath, #css, #search, #xpath

  
  
  
  
  
  
  
  
  
### Methods included from PP::Node

  

#inspect, #pretty_print

  
  
  
  
  
  
  
  
  
### Methods included from HTML5::Node

  

#inner_html, #write_to

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(*args)  ⇒ Document 
  

  

  

  
    

:nodoc: # rubocop:disable Lint/MissingSuper

  

  

  
    
      

```

190
191
192
193
194
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 190

def initialize(*args) # :nodoc: # rubocop:disable Lint/MissingSuper
  @errors     = []
  @decorators = nil
  @namespace_inheritance = false
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**errors**  ⇒ Object 
  

  

  

  
    

The errors found while parsing a document.
Returns

Array<Nokogiri::XML::SyntaxError>

  

  

  
    
      

```

141
142
143
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 141

def errors
  @errors
end

```

    
  

    
      
      
      
  
### 
  
    #**namespace_inheritance**  ⇒ Object 
  

  

  

  
    

When `true`, reparented elements without a namespace will inherit their new parent’s namespace (if one exists). Defaults to `false`.
Returns

Boolean

**Example:** Default behavior of namespace inheritance

```
xml = "        <root xmlns:foo=\"http://nokogiri.org/default_ns/test/foo\">\n          <foo:parent>\n          </foo:parent>\n        </root>\n      EOF\ndoc = Nokogiri::XML(xml)\nparent = doc.at_xpath(\"//foo:parent\", \"foo\" => \"http://nokogiri.org/default_ns/test/foo\")\nparent.add_child(\"<child></child>\")\ndoc.to_xml\n# => <?xml version=\"1.0\"?>\n#    <root xmlns:foo=\"http://nokogiri.org/default_ns/test/foo\">\n#      <foo:parent>\n#        <child/>\n#      </foo:parent>\n#    </root>\n"

```

**Example:** Setting namespace inheritance to `true`

```
xml = "        <root xmlns:foo=\"http://nokogiri.org/default_ns/test/foo\">\n          <foo:parent>\n          </foo:parent>\n        </root>\n      EOF\ndoc = Nokogiri::XML(xml)\ndoc.namespace_inheritance = true\nparent = doc.at_xpath(\"//foo:parent\", \"foo\" => \"http://nokogiri.org/default_ns/test/foo\")\nparent.add_child(\"<child></child>\")\ndoc.to_xml\n# => <?xml version=\"1.0\"?>\n#    <root xmlns:foo=\"http://nokogiri.org/default_ns/test/foo\">\n#      <foo:parent>\n#        <foo:child/>\n#      </foo:parent>\n#    </root>\n"

```

Since v1.12.4

  

  

  
    
      

```

188
189
190
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 188

def namespace_inheritance
  @namespace_inheritance
end

```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**new**(version = "1.0")  ⇒ Object 
  

  

  

  
    

Create a new empty document declaring XML version `version`.

  

  
  

  
    
      

```

455
456
457
458
459
460
461
462
463
464
465
466
467
468
```

    
    
      

```
# File 'ext/nokogiri/xml_document.c', line 455

static VALUE
new (int argc, VALUE *argv, VALUE klass)
{
  xmlDocPtr doc;
  VALUE version, rest, rb_doc ;

  rb_scan_args(argc, argv, "0*", &rest);
  version = rb_ary_entry(rest, (long)0);
  if (NIL_P(version)) { version = rb_str_new2("1.0"); }

  doc = xmlNewDoc((xmlChar *)StringValueCStr(version));
  rb_doc = noko_xml_document_wrap_with_init_args(klass, doc, argc, argv);
  return rb_doc ;
}

```

    
  

    
      
  
### 
  
    .**parse**(string_or_io, url_ = nil, encoding_ = nil, options_ = XML::ParseOptions::DEFAULT_XML, url: url_, encoding: encoding_, options: options_) {|options| ... } ⇒ Object 
  

  

  

  
    

call-seq:

```
parse(input) { |options| ... } => Nokogiri::XML::Document
parse(input, url:, encoding:, options:) => Nokogiri::XML::Document

```

Parse XML input from a String or IO object, and return a new XML::Document.

🛡 By default, Nokogiri treats documents as untrusted, and so does not attempt to load DTDs or access the network. See Nokogiri::XML::ParseOptions for a complete list of options; and that module’s DEFAULT_XML constant for what’s set (and not set) by default.
Required Parameters

- 

`input` (String | IO) The content to be parsed.

Optional Keyword Arguments

- 

`url:` (String) The base URI for this document.

- 

`encoding:` (String) The name of the encoding that should be used when processing the document. When not provided, the encoding will be determined based on the document content.

- 

`options:` (Nokogiri::XML::ParseOptions) Configuration object that determines some behaviors during parsing. See ParseOptions for more information. The default value is `ParseOptions::DEFAULT_XML`.

Yields

If a block is given, a Nokogiri::XML::ParseOptions object is yielded to the block which can be configured before parsing. See Nokogiri::XML::ParseOptions for more information.
Returns

Nokogiri::XML::Document

  

  

Yields:

  
    
- 
      
      
        (options)
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 56

def parse(
  string_or_io,
  url_ = nil, encoding_ = nil, options_ = XML::ParseOptions::DEFAULT_XML,
  url: url_, encoding: encoding_, options: options_
)
  options = Nokogiri::XML::ParseOptions.new(options) if Integer === options
  yield options if block_given?

  url ||= string_or_io.respond_to?(:path) ? string_or_io.path : nil

  if empty_doc?(string_or_io)
    if options.strict?
      raise Nokogiri::XML::SyntaxError, "Empty document"
    else
      return encoding ? new.tap { |i| i.encoding = encoding } : new
    end
  end

  doc = if string_or_io.respond_to?(:read)
    # TODO: should we instead check for respond_to?(:to_path) ?
    if string_or_io.is_a?(Pathname)
      # resolve the Pathname to the file and open it as an IO object, see #2110
      string_or_io = string_or_io.expand_path.open
      url ||= string_or_io.path
    end

    read_io(string_or_io, url, encoding, options.to_i)
  else
    # read_memory pukes on empty docs
    read_memory(string_or_io, url, encoding, options.to_i)
  end

  # do xinclude processing
  doc.do_xinclude(options) if options.xinclude?

  doc
end

```

    
  

    
      
  
### 
  
    .**read_io**(io, url, encoding, options)  ⇒ Object 
  

  

  

  
    

Create a new document from an IO object

  

  
  

  
    
      

```

366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
```

    
    
      

```
# File 'ext/nokogiri/xml_document.c', line 366

static VALUE
noko_xml_document_s_read_io(VALUE rb_class,
                            VALUE rb_io,
                            VALUE rb_url,
                            VALUE rb_encoding,
                            VALUE rb_options)
{
  /* TODO: deprecate this method, parse should be the preferred entry point. then we can make this
     private. */
  libxmlStructuredErrorHandlerState handler_state;
  VALUE rb_errors = rb_ary_new();

  noko__structured_error_func_save_and_set(&handler_state, (void *)rb_errors, noko__error_array_pusher);

  const char *c_url    = NIL_P(rb_url)      ? NULL : StringValueCStr(rb_url);
  const char *c_enc    = NIL_P(rb_encoding) ? NULL : StringValueCStr(rb_encoding);
  xmlDocPtr c_document = xmlReadIO(
                           (xmlInputReadCallback)noko_io_read,
                           (xmlInputCloseCallback)noko_io_close,
                           (void *)rb_io,
                           c_url,
                           c_enc,
                           (int)NUM2INT(rb_options)
                         );

  noko__structured_error_func_restore(&handler_state);

  if (c_document == NULL) {
    xmlFreeDoc(c_document);

    VALUE exception = rb_funcall(cNokogiriXmlSyntaxError, rb_intern("aggregate"), 1, rb_errors);
    if (RB_TEST(exception)) {
      rb_exc_raise(exception);
    } else {
      rb_raise(rb_eRuntimeError, "Could not parse document");
    }
  }

  VALUE rb_document = noko_xml_document_wrap(rb_class, c_document);
  rb_iv_set(rb_document, "@errors", rb_errors);
  return rb_document;
}

```

    
  

    
      
  
### 
  
    .**read_memory**(string, url, encoding, options)  ⇒ Object 
  

  

  

  
    

Create a new document from a String

  

  
  

  
    
      

```

415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
```

    
    
      

```
# File 'ext/nokogiri/xml_document.c', line 415

static VALUE
noko_xml_document_s_read_memory(VALUE rb_class,
                                VALUE rb_input,
                                VALUE rb_url,
                                VALUE rb_encoding,
                                VALUE rb_options)
{
  /* TODO: deprecate this method, parse should be the preferred entry point. then we can make this
     private. */
  VALUE rb_errors = rb_ary_new();
  xmlSetStructuredErrorFunc((void *)rb_errors, noko__error_array_pusher);

  const char *c_buffer = StringValuePtr(rb_input);
  const char *c_url    = NIL_P(rb_url)      ? NULL : StringValueCStr(rb_url);
  const char *c_enc    = NIL_P(rb_encoding) ? NULL : StringValueCStr(rb_encoding);
  int c_buffer_len     = (int)RSTRING_LEN(rb_input);
  xmlDocPtr c_document = xmlReadMemory(c_buffer, c_buffer_len, c_url, c_enc, (int)NUM2INT(rb_options));

  xmlSetStructuredErrorFunc(NULL, NULL);

  if (c_document == NULL) {
    VALUE exception = rb_funcall(cNokogiriXmlSyntaxError, rb_intern("aggregate"), 1, rb_errors);
    if (RB_TEST(exception)) {
      rb_exc_raise(exception);
    } else {
      rb_raise(rb_eRuntimeError, "Could not parse document");
    }
  }

  VALUE document = noko_xml_document_wrap(rb_class, c_document);
  rb_iv_set(document, "@errors", rb_errors);
  return document;
}

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_child**(node_or_tags)  ⇒ Object 
  

  
    Also known as:
    <<
    
  

  

  
    
      

```

437
438
439
440
441
442
443
444
445
446
447
448
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 437

def add_child(node_or_tags)
  raise "A document may not have multiple root nodes." if (root && root.name != "nokogiri_text_wrapper") && !(node_or_tags.comment? || node_or_tags.processing_instruction?)

  node_or_tags = coerce(node_or_tags)
  if node_or_tags.is_a?(XML::NodeSet)
    raise "A document may not have multiple root nodes." if node_or_tags.size > 1

    super(node_or_tags.first)
  else
    super
  end
end

```

    
  

    
      
  
### 
  
    
      #**canonicalize**(mode = XML_C14N_1_0, inclusive_namespaces = nil, with_comments = false)  ⇒ Object 
    
      #**canonicalize** {|obj, parent| ... } ⇒ Object 
    
  

  

  

  
    

Canonicalize a document and return the results.  Takes an optional block that takes two parameters: the `obj` and that node’s `parent`. The  `obj` will be either a Nokogiri::XML::Node, or a Nokogiri::XML::Namespace The block must return a non-nil, non-false value if the `obj` passed in should be included in the canonicalized document.

  

  
  

Overloads:
  

    
      
      
      
- 
        #**canonicalize** {|obj, parent| ... } ⇒ Object 
        
  
    

  

  

Yields:

  
    
  - 
      
      
        (obj, parent)
      
      
      
    
  

      
    
  

  
    
      

```

600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
```

    
    
      

```
# File 'ext/nokogiri/xml_document.c', line 600

static VALUE
rb_xml_document_canonicalize(int argc, VALUE *argv, VALUE self)
{
  VALUE rb_mode;
  VALUE rb_namespaces;
  VALUE rb_comments_p;
  int c_mode = 0;
  xmlChar **c_namespaces;

  xmlDocPtr c_doc;
  xmlOutputBufferPtr c_obuf;
  xmlC14NIsVisibleCallback c_callback_wrapper = NULL;
  void *rb_callback = NULL;

  VALUE rb_cStringIO;
  VALUE rb_io;

  rb_scan_args(argc, argv, "03", &rb_mode, &rb_namespaces, &rb_comments_p);
  if (!NIL_P(rb_mode)) {
    Check_Type(rb_mode, T_FIXNUM);
    c_mode = NUM2INT(rb_mode);
  }
  if (!NIL_P(rb_namespaces)) {
    Check_Type(rb_namespaces, T_ARRAY);
    if (c_mode == XML_C14N_1_0 || c_mode == XML_C14N_1_1) {
      rb_raise(rb_eRuntimeError, "This canonicalizer does not support this operation");
    }
  }

  c_doc = noko_xml_document_unwrap(self);

  rb_cStringIO = rb_const_get_at(rb_cObject, rb_intern("StringIO"));
  rb_io = rb_class_new_instance(0, 0, rb_cStringIO);
  c_obuf = xmlAllocOutputBuffer(NULL);

  c_obuf->writecallback = (xmlOutputWriteCallback)noko_io_write;
  c_obuf->closecallback = (xmlOutputCloseCallback)noko_io_close;
  c_obuf->context = (void *)rb_io;

  if (rb_block_given_p()) {
    c_callback_wrapper = block_caller;
    rb_callback = (void *)rb_block_proc();
  }

  if (NIL_P(rb_namespaces)) {
    c_namespaces = NULL;
  } else {
    long ns_len = RARRAY_LEN(rb_namespaces);
    c_namespaces = ruby_xcalloc((size_t)ns_len + 1, sizeof(xmlChar *));
    for (int j = 0 ; j < ns_len ; j++) {
      VALUE entry = rb_ary_entry(rb_namespaces, j);
      c_namespaces[j] = (xmlChar *)StringValueCStr(entry);
    }
  }

  int ret = xmlC14NExecute(c_doc, c_callback_wrapper, rb_callback,
                           c_mode,
                           c_namespaces,
                           (int)RTEST(rb_comments_p),
                           c_obuf);

  ruby_xfree(c_namespaces);
  xmlOutputBufferClose(c_obuf);

  if (ret < 0) {
    rb_raise(rb_eRuntimeError, "canonicalization failed");
  }

  return rb_funcall(rb_io, rb_intern("string"), 0);
}

```

    
  

    
      
  
### 
  
    #**clone**(level = 1)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
clone 
```

Clone this node.
Parameters

- 

`level` (optional Integer). 0 is a shallow copy, 1 (the default) is a deep copy.

Returns

The new Nokogiri::XML::Document

  

  

  
    
      

```

223
224
225
226
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 223

def clone(level = 1)
  copy = OBJECT_CLONE_METHOD.bind_call(self)
  copy.initialize_copy_with_args(self, level)
end

```

    
  

    
      
  
### 
  
    #**collect_namespaces**  ⇒ Object 
  

  

  

  
    

:call-seq:

```
collect_namespaces() 
```

Recursively get all namespaces from this node and its subtree and return them as a hash.

⚠ This method will not handle duplicate namespace prefixes, since the return value is a hash.

Note that this method does an xpath lookup for nodes with namespaces, and as a result the order (and which duplicate prefix “wins”) may be dependent on the implementation of the underlying XML library.

**Example:** Basic usage

Given this document:

```
<root xmlns="default" xmlns:foo="bar">
  <bar xmlns:hello="world" />
</root>

```

This method will return:

```
{"xmlns:foo"=>"bar", "xmlns"=>"default", "xmlns:hello"=>"world"}

```

**Example:** Duplicate prefixes

Given this document:

```
<root xmlns:foo="bar">
  <bar xmlns:foo="baz" />
</root>

```

The hash returned will be something like:

```
{"xmlns:foo" => "baz"}

```

  

  

  
    
      

```

361
362
363
364
365
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 361

def collect_namespaces
  xpath("//namespace::*").each_with_object({}) do |ns, hash|
    hash[["xmlns", ns.prefix].compact.join(":")] = ns.href if ns.prefix != "xml"
  end
end

```

    
  

    
      
  
### 
  
    #**create_cdata**(string, &block)  ⇒ Object 
  

  

  

  
    

Create a CDATA Node containing `string`

  

  

  
    
      

```

306
307
308
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 306

def create_cdata(string, &block)
  Nokogiri::XML::CDATA.new(self, string.to_s, &block)
end

```

    
  

    
      
  
### 
  
    #**create_comment**(string, &block)  ⇒ Object 
  

  

  

  
    

Create a Comment Node containing `string`

  

  

  
    
      

```

311
312
313
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 311

def create_comment(string, &block)
  Nokogiri::XML::Comment.new(self, string.to_s, &block)
end

```

    
  

    
      
  
### 
  
    #**create_element**(name, *contents_or_attrs, &block)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
create_element(name, *contents_or_attrs, &block) 
```

Create a new Element with `name` belonging to this document, optionally setting contents or attributes.

This method is *not* the most user-friendly option if your intention is to add a node to the document tree. Prefer one of the Nokogiri::XML::Node methods like Node#add_child, Node#add_next_sibling, Node#replace, etc. which will both create an element (or subtree) and place it in the document tree.

Arguments may be passed to initialize the element:

- 

a Hash argument will be used to set attributes

- 

a non-Hash object that responds to #to_s will be used to set the new node’s contents

A block may be passed to mutate the node.
Parameters

- 

`name` (String)

- 

`contents_or_attrs` (#to_s, Hash)

Yields

`node` (Nokogiri::XML::Element)
Returns

Nokogiri::XML::Element

**Example:** An empty element without attributes

```
doc.create_element("div")
# => <div></div>

```

**Example:** An element with contents

```
doc.create_element("div", "contents")
# => <div>contents</div>

```

**Example:** An element with attributes

```
doc.create_element("div", {"class" => "container"})
# => <div class='container'></div>

```

**Example:** An element with contents and attributes

```
doc.create_element("div", "contents", {"class" => "container"})
# => <div class='container'>contents</div>

```

**Example:** Passing a block to mutate the element

```
doc.create_element("div") { |node| node["class"] = "blue" if before_noon? }

```

  

  

  
    
      

```

276
277
278
279
280
281
282
283
284
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
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 276

def create_element(name, *contents_or_attrs, &block)
  elm = Nokogiri::XML::Element.new(name, self, &block)
  contents_or_attrs.each do |arg|
    case arg
    when Hash
      arg.each do |k, v|
        key = k.to_s
        if key =~ NCNAME_RE
          ns_name = Regexp.last_match(1)
          elm.add_namespace_definition(ns_name, v)
        else
          elm[k.to_s] = v.to_s
        end
      end
    else
      elm.content = arg
    end
  end
  if (ns = elm.namespace_definitions.find { |n| n.prefix.nil? || (n.prefix == "") })
    elm.namespace = ns
  end
  elm
end

```

    
  

    
      
  
### 
  
    #**create_entity**(name, type, external_id, system_id, content)  ⇒ Object 
  

  

  

  
    

Create a new entity named `name`.

`type` is an integer representing the type of entity to be created, and it defaults to `Nokogiri::XML::EntityDecl::INTERNAL_GENERAL`. See the constants on Nokogiri::XML::EntityDecl for more information.

`external_id`, `system_id`, and `content` set the External ID, System ID, and content respectively.  All of these parameters are optional.

  

  
  

  
    
      

```

528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
```

    
    
      

```
# File 'ext/nokogiri/xml_document.c', line 528

static VALUE
noko_xml_document__create_entity(int argc, VALUE *argv, VALUE rb_document)
{
  VALUE rb_name;
  VALUE rb_type;
  VALUE rb_ext_id;
  VALUE rb_sys_id;
  VALUE rb_content;

  rb_scan_args(argc, argv, "14",
               &rb_name,
               &rb_type, &rb_ext_id, &rb_sys_id, &rb_content);

  xmlDocPtr c_document = noko_xml_document_unwrap(rb_document);

  libxmlStructuredErrorHandlerState handler_state;
  VALUE rb_errors = rb_ary_new();
  noko__structured_error_func_save_and_set(&handler_state, (void *)rb_errors, noko__error_array_pusher);

  xmlEntityPtr c_entity = xmlAddDocEntity(
                            c_document,
                            (xmlChar *)(NIL_P(rb_name) ? NULL : StringValueCStr(rb_name)),
                            (int)(NIL_P(rb_type) ? XML_INTERNAL_GENERAL_ENTITY : NUM2INT(rb_type)),
                            (xmlChar *)(NIL_P(rb_ext_id) ? NULL : StringValueCStr(rb_ext_id)),
                            (xmlChar *)(NIL_P(rb_sys_id) ? NULL : StringValueCStr(rb_sys_id)),
                            (xmlChar *)(NIL_P(rb_content) ? NULL : StringValueCStr(rb_content))
                          );

  noko__structured_error_func_restore(&handler_state);

  if (NULL == c_entity) {
    VALUE exception = rb_funcall(cNokogiriXmlSyntaxError, rb_intern("aggregate"), 1, rb_errors);
    if (RB_TEST(exception)) {
      rb_exc_raise(exception);
    } else {
      rb_raise(rb_eRuntimeError, "Could not create entity");
    }
  }

  return noko_xml_node_wrap(cNokogiriXmlEntityDecl, (xmlNodePtr)c_entity);
}

```

    
  

    
      
  
### 
  
    #**create_text_node**(string, &block)  ⇒ Object 
  

  

  

  
    

Create a Text Node with `string`

  

  

  
    
      

```

301
302
303
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 301

def create_text_node(string, &block)
  Nokogiri::XML::Text.new(string.to_s, self, &block)
end

```

    
  

    
      
  
### 
  
    #**deconstruct_keys**(keys)  ⇒ Object 
  

  

  

  
    

:call-seq: deconstruct_keys(array_of_names) → Hash

```
Returns a hash describing the Document, to use in pattern matching.

Valid keys and their values:
- +root+ 
```

  

  

  
    
      

```

501
502
503
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 501

def deconstruct_keys(keys)
  { root: root }
end

```

    
  

    
      
  
### 
  
    #**decorate**(node)  ⇒ Object 
  

  

  

  
    

Apply any decorators to `node`

  

  

  
    
      

```

409
410
411
412
413
414
415
416
417
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 409

def decorate(node)
  return unless @decorators

  @decorators.each do |klass, list|
    next unless node.is_a?(klass)

    list.each { |mod| node.extend(mod) }
  end
end

```

    
  

    
      
  
### 
  
    #**decorators**(key)  ⇒ Object 
  

  

  

  
    

Get the list of decorators given `key`

  

  

  
    
      

```

368
369
370
371
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 368

def decorators(key)
  @decorators ||= {}
  @decorators[key] ||= []
end

```

    
  

    
      
  
### 
  
    #**document**  ⇒ Object 
  

  

  

  
    

A reference to `self`

  

  

  
    
      

```

321
322
323
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 321

def document
  self
end

```

    
  

    
      
  
### 
  
    #**dup**(level = 1)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
dup 
```

Duplicate this node.
Parameters

- 

`level` (optional Integer). 0 is a shallow copy, 1 (the default) is a deep copy.

Returns

The new Nokogiri::XML::Document

  

  

  
    
      

```

207
208
209
210
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 207

def dup(level = 1)
  copy = OBJECT_DUP_METHOD.bind_call(self)
  copy.initialize_copy_with_args(self, level)
end

```

    
  

    
      
  
### 
  
    #**encoding**  ⇒ Object 
  

  

  

  
    

Get the encoding for this Document

  

  
  

  
    
      

```

336
337
338
339
340
341
342
343
```

    
    
      

```
# File 'ext/nokogiri/xml_document.c', line 336

static VALUE
encoding(VALUE self)
{
  xmlDocPtr doc = noko_xml_document_unwrap(self);

  if (!doc->encoding) { return Qnil; }
  return NOKOGIRI_STR_NEW2(doc->encoding);
}

```

    
  

    
      
  
### 
  
    #**encoding=**(encoding)  ⇒ Object 
  

  

  

  
    

Set the encoding string for this Document

  

  
  

  
    
      

```

316
317
318
319
320
321
322
323
324
325
326
327
328
```

    
    
      

```
# File 'ext/nokogiri/xml_document.c', line 316

static VALUE
set_encoding(VALUE self, VALUE encoding)
{
  xmlDocPtr doc = noko_xml_document_unwrap(self);

  if (doc->encoding) {
    xmlFree(DISCARD_CONST_QUAL_XMLCHAR(doc->encoding));
  }

  doc->encoding = xmlStrdup((xmlChar *)StringValueCStr(encoding));

  return encoding;
}

```

    
  

    
      
  
### 
  
    #**fragment**(tags = nil)  ⇒ Object 
  

  

  

  
    

Create a Nokogiri::XML::DocumentFragment from `tags` Returns an empty fragment if `tags` is nil.

  

  

  
    
      

```

429
430
431
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 429

def fragment(tags = nil)
  DocumentFragment.new(self, tags, root)
end

```

    
  

    
      
  
### 
  
    #**name**  ⇒ Object 
  

  

  

  
    

The name of this document.  Always returns “document”

  

  

  
    
      

```

316
317
318
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 316

def name
  "document"
end

```

    
  

    
      
  
### 
  
    #**namespaces**  ⇒ Object 
  

  

  

  
    

Get the hash of namespaces on the root Nokogiri::XML::Node

  

  

  
    
      

```

422
423
424
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 422

def namespaces
  root ? root.namespaces : {}
end

```

    
  

    
      
  
### 
  
    #**remove_namespaces!**  ⇒ Object 
  

  

  

  
    

Remove all namespaces from all nodes in the document.

This could be useful for developers who either don’t understand namespaces or don’t care about them.

The following example shows a use case, and you can decide for yourself whether this is a good thing or not:

```
doc = Nokogiri::XML "   <root>\n     <car xmlns:part=\"http://general-motors.com/\">\n       <part:tire>Michelin Model XGV</part:tire>\n     </car>\n     <bicycle xmlns:part=\"http://schwinn.com/\">\n       <part:tire>I'm a bicycle tire!</part:tire>\n     </bicycle>\n   </root>\n   EOXML\n\ndoc.xpath(\"//tire\").to_s # => \"\"\ndoc.xpath(\"//part:tire\", \"part\" => \"http://general-motors.com/\").to_s # => \"<part:tire>Michelin Model XGV</part:tire>\"\ndoc.xpath(\"//part:tire\", \"part\" => \"http://schwinn.com/\").to_s # => \"<part:tire>I'm a bicycle tire!</part:tire>\"\n\ndoc.remove_namespaces!\n\ndoc.xpath(\"//tire\").to_s # => \"<tire>Michelin Model XGV</tire><tire>I'm a bicycle tire!</tire>\"\ndoc.xpath(\"//part:tire\", \"part\" => \"http://general-motors.com/\").to_s # => \"\"\ndoc.xpath(\"//part:tire\", \"part\" => \"http://schwinn.com/\").to_s # => \"\"\n"

```

For more information on why this probably is **not** a good thing in general, please direct your browser to tenderlovemaking.com/2009/04/23/namespaces-in-xml.html

  

  
  

  
    
      

```

507
508
509
510
511
512
513
514
```

    
    
      

```
# File 'ext/nokogiri/xml_document.c', line 507

static VALUE
remove_namespaces_bang(VALUE self)
{
  xmlDocPtr doc = noko_xml_document_unwrap(self);

  recursively_remove_namespaces_from_node((xmlNodePtr)doc);
  return self;
}

```

    
  

    
      
  
### 
  
    #**root**  ⇒ Object 
  

  

  

  
    

Get the root node for this document.

  

  
  

  
    
      

```

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
308
```

    
    
      

```
# File 'ext/nokogiri/xml_document.c', line 294

static VALUE
rb_xml_document_root(VALUE self)
{
  xmlDocPtr c_document;
  xmlNodePtr c_root;

  c_document = noko_xml_document_unwrap(self);

  c_root = xmlDocGetRootElement(c_document);
  if (!c_root) {
    return Qnil;
  }

  return noko_xml_node_wrap(Qnil, c_root) ;
}

```

    
  

    
      
  
### 
  
    #**root=**  ⇒ Object 
  

  

  

  
    

Set the root element on this document

  

  
  

  
    
      

```

250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
```

    
    
      

```
# File 'ext/nokogiri/xml_document.c', line 250

static VALUE
rb_xml_document_root_set(VALUE self, VALUE rb_new_root)
{
  xmlDocPtr c_document;
  xmlNodePtr c_new_root = NULL, c_current_root;

  c_document = noko_xml_document_unwrap(self);

  c_current_root = xmlDocGetRootElement(c_document);
  if (c_current_root) {
    xmlUnlinkNode(c_current_root);
    noko_xml_document_pin_node(c_current_root);
  }

  if (!NIL_P(rb_new_root)) {
    if (!rb_obj_is_kind_of(rb_new_root, cNokogiriXmlNode)) {
      rb_raise(rb_eArgError,
               "expected Nokogiri::XML::Node but received %"PRIsVALUE,
               rb_obj_class(rb_new_root));
    }

    Noko_Node_Get_Struct(rb_new_root, xmlNode, c_new_root);

    /* If the new root's document is not the same as the current document,
     * then we need to dup the node in to this document. */
    if (c_new_root->doc != c_document) {
      c_new_root = xmlDocCopyNode(c_new_root, c_document, 1);
      if (!c_new_root) {
        rb_raise(rb_eRuntimeError, "Could not reparent node (xmlDocCopyNode)");
      }
    }
  }

  xmlDocSetRootElement(c_document, c_new_root);

  return rb_new_root;
}

```

    
  

    
      
  
### 
  
    #**slop!**  ⇒ Object 
  

  

  

  
    

Explore a document with shortcut methods. See Nokogiri::Slop for details.

Note that any nodes that have been instantiated before #slop! is called will not be decorated with sloppy behavior. So, if you’re in irb, the preferred idiom is:

```
irb> doc = Nokogiri::Slop my_markup

```

and not

```
irb> doc = Nokogiri::HTML my_markup
... followed by irb's implicit inspect (and therefore instantiation of every node) ...
irb> doc.slop!
... which does absolutely nothing.

```

  

  

  
    
      

```

398
399
400
401
402
403
404
405
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 398

def slop!
  unless decorators(XML::Node).include?(Nokogiri::Decorators::Slop)
    decorators(XML::Node) << Nokogiri::Decorators::Slop
    decorate!
  end

  self
end

```

    
  

    
      
  
### 
  
    #**url**  ⇒ Object 
  

  

  

  
    

Get the url name for this document.

  

  
  

  
    
      

```

234
235
236
237
238
239
240
241
242
```

    
    
      

```
# File 'ext/nokogiri/xml_document.c', line 234

static VALUE
url(VALUE self)
{
  xmlDocPtr doc = noko_xml_document_unwrap(self);

  if (doc->URL) { return NOKOGIRI_STR_NEW2(doc->URL); }

  return Qnil;
}

```

    
  

    
      
  
### 
  
    #**validate**  ⇒ Object 
  

  

  

  
    

Validate this Document against its DTD.  Returns a list of errors on the document or `nil` when there is no DTD.

  

  

  
    
      

```

376
377
378
379
380
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 376

def validate
  return unless internal_subset

  internal_subset.validate(self)
end

```

    
  

    
      
  
### 
  
    #**version**  ⇒ Object 
  

  

  

  
    

Get the XML version for this Document

  

  
  

  
    
      

```

351
352
353
354
355
356
357
358
```

    
    
      

```
# File 'ext/nokogiri/xml_document.c', line 351

static VALUE
version(VALUE self)
{
  xmlDocPtr doc = noko_xml_document_unwrap(self);

  if (!doc->version) { return Qnil; }
  return NOKOGIRI_STR_NEW2(doc->version);
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

457
458
459
```

    
    
      

```
# File 'lib/nokogiri/xml/document.rb', line 457

def xpath_doctype
  Nokogiri::CSS::XPathVisitor::DoctypeConfig::XML
end

```