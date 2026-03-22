# Class: Nokogiri::XML::Attr
  
  
  

  
  
    Inherits:
    
      NokogiriXmlNode
      
        

          
- Object
          
            
- NokogiriXmlNode
          
            
- Nokogiri::XML::Attr
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/attr.rb,

  ext/nokogiri/xml_attr.c

  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**new**(document, name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a new Attr element on the `document` with `name`.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**deconstruct_keys**(keys)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: deconstruct_keys(array_of_names) → Hash.

  

      
        
- 
  
    
      #**value=**(content)  ⇒ Object 
    

    
      (also: #content=)
    
  
  
  
  
  
  
  
  

  
    

Set the value for this Attr to `content`.

  

      
    

  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**new**(document, name)  ⇒ Object 
  

  

  

  
    

Create a new Attr element on the `document` with `name`

  

  
  

  
    
      

```

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
```

    
    
      

```
# File 'ext/nokogiri/xml_attr.c', line 55

static VALUE
new (int argc, VALUE *argv, VALUE klass)
{
  xmlDocPtr xml_doc;
  VALUE document;
  VALUE name;
  VALUE rest;
  xmlAttrPtr node;
  VALUE rb_node;

  rb_scan_args(argc, argv, "2*", &document, &name, &rest);

  if (! rb_obj_is_kind_of(document, cNokogiriXmlDocument)) {
    rb_raise(rb_eArgError, "parameter must be a Nokogiri::XML::Document");
  }

  xml_doc = noko_xml_document_unwrap(document);

  node = xmlNewDocProp(
           xml_doc,
           (const xmlChar *)StringValueCStr(name),
           NULL
         );

  noko_xml_document_pin_node((xmlNodePtr)node);

  rb_node = noko_xml_node_wrap(klass, (xmlNodePtr)node);
  rb_obj_call_init(rb_node, argc, argv);

  if (rb_block_given_p()) {
    rb_yield(rb_node);
  }

  return rb_node;
}
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**deconstruct_keys**(keys)  ⇒ Object 
  

  

  

  
    

:call-seq: deconstruct_keys(array_of_names) → Hash

```
Returns a hash describing the Attr, to use in pattern matching.

Valid keys and their values:
- +name+ → (String) The name of the attribute.
- +value+ → (String) The value of the attribute.
- +namespace+ → (Namespace, nil) The Namespace of the attribute, or +nil+ if there is no namespace.

*Example*

  doc = Nokogiri::XML.parse(<<~XML)
    <?xml version="1.0"?>
    <root xmlns="http://nokogiri.org/ns/default" xmlns:noko="http://nokogiri.org/ns/noko">
      <child1 foo="abc" noko:bar="def"/>
    </root>
  XML

  attributes = doc.root.elements.first.attribute_nodes
  # => [#(Attr:0x35c { name = "foo", value = "abc" }),
  #     #(Attr:0x370 {
  #       name = "bar",
  #       namespace = #(Namespace:0x384 {
  #         prefix = "noko",
  #         href = "http://nokogiri.org/ns/noko"
  #         }),
  #       value = "def"
  #       })]

  attributes.first.deconstruct_keys([:name, :value, :namespace])
  # => {:name=>"foo", :value=>"abc", :namespace=>nil}

  attributes.last.deconstruct_keys([:name, :value, :namespace])
  # => {:name=>"bar",
  #     :value=>"def",
  #     :namespace=>
  #      #(Namespace:0x384 {
  #        prefix = "noko",
  #        href = "http://nokogiri.org/ns/noko"
  #        })}

Since v1.14.0

```

  

  

  
    
      

```

55
56
57
```

    
    
      

```
# File 'lib/nokogiri/xml/attr.rb', line 55

def deconstruct_keys(keys)
  { name: name, value: value, namespace: namespace }
end
```

    
  

    
      
  
### 
  
    #**value=**(content)  ⇒ Object 
  

  
    Also known as:
    content=
    
  

  

  
    

Set the value for this Attr to `content`. Use `nil` to remove the value (e.g., a HTML boolean attribute).

  

  
  

  
    
      

```

12
13
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
31
32
33
34
35
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
```

    
    
      

```
# File 'ext/nokogiri/xml_attr.c', line 12

static VALUE
set_value(VALUE self, VALUE content)
{
  xmlAttrPtr attr;
  xmlChar *value;
  xmlNode *cur;

  Noko_Node_Get_Struct(self, xmlAttr, attr);

  if (attr->children) {
    xmlFreeNodeList(attr->children);
  }
  attr->children = attr->last = NULL;

  if (content == Qnil) {
    return content;
  }

  value = xmlEncodeEntitiesReentrant(attr->doc, (unsigned char *)StringValueCStr(content));
  if (xmlStrlen(value) == 0) {
    attr->children = xmlNewDocText(attr->doc, value);
  } else {
    attr->children = xmlStringGetNodeList(attr->doc, value);
  }
  xmlFree(value);

  for (cur = attr->children; cur; cur = cur->next) {
    cur->parent = (xmlNode *)attr;
    cur->doc = attr->doc;
    if (cur->next == NULL) {
      attr->last = cur;
    }
  }

  return content;
}
```