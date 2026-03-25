# Class: Nokogiri::XML::CDATA
  
  
  

  
  
    Inherits:
    
      Text
      
        

          
- Object
          
            
- NokogiriXmlNode
          
            
- CharacterData
          
            
- Text
          
            
- Nokogiri::XML::CDATA
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/cdata.rb,

  ext/nokogiri/xml_cdata.c

  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**new**(document, content)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a new CDATA element on the `document` with `content`.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the name of this CDATA node.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Text

  

#content=

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from PP::CharacterData

  

#inspect, #pretty_print

  

  
    
## Class Method Details

    
      
  
### 
  
    .**new**(document, content)  ⇒ Object 
  

  

  

  
    

Create a new CDATA element on the `document` with `content`

If `content` cannot be implicitly converted to a string, this method will raise a TypeError exception.

  

  
  

  
    
      

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
48
49
50
```

    
    
      

```
# File 'ext/nokogiri/xml_cdata.c', line 14

static VALUE
rb_xml_cdata_s_new(int argc, VALUE *argv, VALUE klass)
{
  xmlDocPtr c_document;
  xmlNodePtr c_node;
  VALUE rb_document;
  VALUE rb_content;
  VALUE rb_rest;
  VALUE rb_node;

  rb_scan_args(argc, argv, "2*", &rb_document, &rb_content, &rb_rest);

  Check_Type(rb_content, T_STRING);
  if (!rb_obj_is_kind_of(rb_document, cNokogiriXmlNode)) {
    rb_raise(rb_eTypeError,
             "expected first parameter to be a Nokogiri::XML::Document, received %"PRIsVALUE,
             rb_obj_class(rb_document));
  }

  if (!rb_obj_is_kind_of(rb_document, cNokogiriXmlDocument)) {
    xmlNodePtr deprecated_node_type_arg;
    NOKO_WARN_DEPRECATION("Passing a Node as the first parameter to CDATA.new is deprecated. Please pass a Document instead. This will become an error in Nokogiri v1.17.0."); // TODO: deprecated in v1.15.3, remove in v1.17.0
    Noko_Node_Get_Struct(rb_document, xmlNode, deprecated_node_type_arg);
    c_document = deprecated_node_type_arg->doc;
  } else {
    c_document = noko_xml_document_unwrap(rb_document);
  }

  c_node = xmlNewCDataBlock(c_document, (xmlChar *)StringValueCStr(rb_content), RSTRING_LENINT(rb_content));
  noko_xml_document_pin_node(c_node);
  rb_node = noko_xml_node_wrap(klass, c_node);
  rb_obj_call_init(rb_node, argc, argv);

  if (rb_block_given_p()) { rb_yield(rb_node); }

  return rb_node;
}
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**name**  ⇒ Object 
  

  

  

  
    

Get the name of this CDATA node

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/nokogiri/xml/cdata.rb', line 8

def name
  "#cdata-section"
end
```