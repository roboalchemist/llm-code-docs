# Class: Nokogiri::XML::Comment
  
  
  

  
  
    Inherits:
    
      CharacterData
      
        

          
- Object
          
            
- NokogiriXmlNode
          
            
- CharacterData
          
            
- Nokogiri::XML::Comment
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    ext/nokogiri/xml_comment.c
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**new**(document_or_node, content)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a new Comment element on the `document` with `content`.

  

      
    

  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from PP::CharacterData

  

#inspect, #pretty_print

  

  
    
## Class Method Details

    
      
  
### 
  
    .**new**(document_or_node, content)  ⇒ Object 
  

  

  

  
    

Create a new Comment element on the `document` with `content`. Alternatively, if a `node` is passed, the `node`‘s document is used.

  

  
  

  
    
      

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
```

    
    
      

```
# File 'ext/nokogiri/xml_comment.c', line 14

static VALUE
new (int argc, VALUE *argv, VALUE klass)
{
  xmlDocPtr xml_doc;
  xmlNodePtr node;
  VALUE document;
  VALUE content;
  VALUE rest;
  VALUE rb_node;

  rb_scan_args(argc, argv, "2*", &document, &content, &rest);

  Check_Type(content, T_STRING);
  if (rb_obj_is_kind_of(document, cNokogiriXmlNode)) {
    document = rb_funcall(document, document_id, 0);
  } else if (!rb_obj_is_kind_of(document, cNokogiriXmlDocument)
             && !rb_obj_is_kind_of(document, cNokogiriXmlDocumentFragment)) {
    rb_raise(rb_eArgError, "first argument must be a XML::Document or XML::Node");
  }
  xml_doc = noko_xml_document_unwrap(document);

  node = xmlNewDocComment(xml_doc, (const xmlChar *)StringValueCStr(content));
  noko_xml_document_pin_node(node);
  rb_node = noko_xml_node_wrap(klass, node);
  rb_obj_call_init(rb_node, argc, argv);

  if (rb_block_given_p()) { rb_yield(rb_node); }

  return rb_node;
}
```