# Class: Nokogiri::XML::DTD
  
  
  

  
  
    Inherits:
    
      Node
      
        

          
- Object
          
            
- Node
          
            
- Nokogiri::XML::DTD
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/dtd.rb,

  ext/nokogiri/xml_dtd.c

  
  

  
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

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**attributes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get a hash of the attributes for this DTD.

  

      
        
- 
  
    
      #**each**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**elements**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get a hash of the elements for this DTD.

  

      
        
- 
  
    
      #**entities**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get a hash of the elements for this DTD.

  

      
        
- 
  
    
      #**external_id**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the external identifier for PUBLIC.

  

      
        
- 
  
    
      #**html5_dtd?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**html_dtd?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**keys**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**notations**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    Returns

All the notations for this DTD in a Hash of Notation `name` to Notation.

  

      
        
- 
  
    
      #**system_id**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the URI for a SYSTEM or PUBLIC Entity.

  

      
        
- 
  
    
      #**validate**(document)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Validate `document` returning a list of errors.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Node

  

#<<, #<=>, #==, #[], #[]=, #accept, #add_child, #add_class, #add_namespace_definition, #add_next_sibling, #add_previous_sibling, #after, #ancestors, #append_class, #attribute, #attribute_nodes, #attribute_with_ns, #before, #blank?, #canonicalize, #cdata?, #child, #children, #children=, #classes, #clone, #comment?, #content, #content=, #create_external_subset, #create_internal_subset, #css_path, #data_ptr?, #deconstruct_keys, #decorate!, #default_namespace=, #description, #do_xinclude, #document, #document?, #dup, #element?, #element_children, #encode_special_chars, #external_subset, #first_element_child, #fragment, #fragment?, #html?, #initialize, #inner_html, #inner_html=, #internal_subset, #key?, #kwattr_add, #kwattr_append, #kwattr_remove, #kwattr_values, #lang, #lang=, #last_element_child, #line, #line=, #matches?, #namespace, #namespace=, #namespace_definitions, #namespace_scopes, #namespaced_key?, #namespaces, #native_content=, new, #next_element, #next_sibling, #node_name, #node_name=, #node_type, #parent, #parent=, #parse, #path, #pointer_id, #prepend_child, #previous_element, #previous_sibling, #processing_instruction?, #read_only?, #remove_attribute, #remove_class, #replace, #serialize, #swap, #text?, #to_html, #to_s, #to_xhtml, #to_xml, #traverse, #unlink, #value?, #values, #wrap, #write_html_to, #write_to, #write_xhtml_to, #write_xml_to, #xml?

  
  
  
  
  
  
  
  
  
  
### Methods included from ClassResolver

  

#related_class

  
  
  
  
  
  
  
  
  
### Methods included from Searchable

  

#>, #at, #at_css, #at_xpath, #css, #search, #xpath

  
  
  
  
  
  
  
  
  
### Methods included from PP::Node

  

#inspect, #pretty_print

  
  
  
  
  
  
  
  
  
### Methods included from HTML5::Node

  

#fragment, #inner_html, #write_to

  
## Constructor Details

  
    

This class inherits a constructor from Nokogiri::XML::Node
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**attributes**  ⇒ Object 
  

  

  

  
    

Get a hash of the attributes for this DTD.

  

  
  

  
    
      

```

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
```

    
    
      

```
# File 'ext/nokogiri/xml_dtd.c', line 87

static VALUE
attributes(VALUE self)
{
  xmlDtdPtr dtd;
  VALUE hash;

  Noko_Node_Get_Struct(self, xmlDtd, dtd);

  hash = rb_hash_new();

  if (!dtd->attributes) { return hash; }

  xmlHashScan((xmlHashTablePtr)dtd->attributes, element_copier, (void *)hash);

  return hash;
}

```

    
  

    
      
  
### 
  
    #**each**  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
20
21
```

    
    
      

```
# File 'lib/nokogiri/xml/dtd.rb', line 17

def each
  attributes.each do |key, value|
    yield([key, value])
  end
end

```

    
  

    
      
  
### 
  
    #**elements**  ⇒ Object 
  

  

  

  
    

Get a hash of the elements for this DTD.

  

  
  

  
    
      

```

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
```

    
    
      

```
# File 'ext/nokogiri/xml_dtd.c', line 110

static VALUE
elements(VALUE self)
{
  xmlDtdPtr dtd;
  VALUE hash;

  Noko_Node_Get_Struct(self, xmlDtd, dtd);

  if (!dtd->elements) { return Qnil; }

  hash = rb_hash_new();

  xmlHashScan((xmlHashTablePtr)dtd->elements, element_copier, (void *)hash);

  return hash;
}

```

    
  

    
      
  
### 
  
    #**entities**  ⇒ Object 
  

  

  

  
    

Get a hash of the elements for this DTD.

  

  
  

  
    
      

```

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
```

    
    
      

```
# File 'ext/nokogiri/xml_dtd.c', line 41

static VALUE
entities(VALUE self)
{
  xmlDtdPtr dtd;
  VALUE hash;

  Noko_Node_Get_Struct(self, xmlDtd, dtd);

  if (!dtd->entities) { return Qnil; }

  hash = rb_hash_new();

  xmlHashScan((xmlHashTablePtr)dtd->entities, element_copier, (void *)hash);

  return hash;
}

```

    
  

    
      
  
### 
  
    #**external_id**  ⇒ Object 
  

  

  

  
    

Get the external identifier for PUBLIC

  

  
  

  
    
      

```

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
```

    
    
      

```
# File 'ext/nokogiri/xml_entity_decl.c', line 60

static VALUE
external_id(VALUE self)
{
  xmlEntityPtr node;
  Noko_Node_Get_Struct(self, xmlEntity, node);

  if (!node->ExternalID) { return Qnil; }

  return NOKOGIRI_STR_NEW2(node->ExternalID);
}

```

    
  

    
      
  
### 
  
    #**html5_dtd?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

27
28
29
30
31
```

    
    
      

```
# File 'lib/nokogiri/xml/dtd.rb', line 27

def html5_dtd?
  html_dtd? &&
    external_id.nil? &&
    (system_id.nil? || system_id == "about:legacy-compat")
end

```

    
  

    
      
  
### 
  
    #**html_dtd?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/nokogiri/xml/dtd.rb', line 23

def html_dtd?
  name.casecmp("html").zero?
end

```

    
  

    
      
  
### 
  
    #**keys**  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/nokogiri/xml/dtd.rb', line 13

def keys
  attributes.keys
end

```

    
  

    
      
  
### 
  
    #**notations**  ⇒ Object 
  

  

  

  
    Returns

All the notations for this DTD in a Hash of Notation `name` to Notation.

  

  
  

  
    
      

```

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
```

    
    
      

```
# File 'ext/nokogiri/xml_dtd.c', line 64

static VALUE
notations(VALUE self)
{
  xmlDtdPtr dtd;
  VALUE hash;

  Noko_Node_Get_Struct(self, xmlDtd, dtd);

  if (!dtd->notations) { return Qnil; }

  hash = rb_hash_new();

  xmlHashScan((xmlHashTablePtr)dtd->notations, notation_copier, (void *)hash);

  return hash;
}

```

    
  

    
      
  
### 
  
    #**system_id**  ⇒ Object 
  

  

  

  
    

Get the URI for a SYSTEM or PUBLIC Entity

  

  
  

  
    
      

```

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
```

    
    
      

```
# File 'ext/nokogiri/xml_entity_decl.c', line 77

static VALUE
system_id(VALUE self)
{
  xmlEntityPtr node;
  Noko_Node_Get_Struct(self, xmlEntity, node);

  if (!node->SystemID) { return Qnil; }

  return NOKOGIRI_STR_NEW2(node->SystemID);
}

```

    
  

    
      
  
### 
  
    #**validate**(document)  ⇒ Object 
  

  

  

  
    

Validate `document` returning a list of errors

  

  
  

  
    
      

```

133
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
```

    
    
      

```
# File 'ext/nokogiri/xml_dtd.c', line 133

static VALUE
validate(VALUE self, VALUE document)
{
  xmlDocPtr doc;
  xmlDtdPtr dtd;
  xmlValidCtxtPtr ctxt;
  VALUE error_list;

  Noko_Node_Get_Struct(self, xmlDtd, dtd);
  doc = noko_xml_document_unwrap(document);
  error_list = rb_ary_new();

  ctxt = xmlNewValidCtxt();

  xmlSetStructuredErrorFunc((void *)error_list, noko__error_array_pusher);

  xmlValidateDtd(ctxt, doc, dtd);

  xmlSetStructuredErrorFunc(NULL, NULL);

  xmlFreeValidCtxt(ctxt);

  return error_list;
}

```