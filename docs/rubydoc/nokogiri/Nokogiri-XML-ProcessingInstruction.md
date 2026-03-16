# Class: Nokogiri::XML::ProcessingInstruction
  
  
  

  
  
    Inherits:
    
      Node
      
        

          
- Object
          
            
- Node
          
            
- Nokogiri::XML::ProcessingInstruction
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/processing_instruction.rb,

  ext/nokogiri/xml_processing_instruction.c

  
  

  
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
     from Nokogiri::XML::PP::Node

  

Nokogiri::XML::PP::Node::COLLECTIONS

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**new**(document, name, content)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a new ProcessingInstruction element on the `document` with `name` and `content`.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(document, name, content)  ⇒ ProcessingInstruction 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ProcessingInstruction.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Node

  

#<<, #<=>, #==, #[], #[]=, #accept, #add_child, #add_class, #add_namespace_definition, #add_next_sibling, #add_previous_sibling, #after, #ancestors, #append_class, #attribute, #attribute_nodes, #attribute_with_ns, #attributes, #before, #blank?, #canonicalize, #cdata?, #child, #children, #children=, #classes, #clone, #comment?, #content, #content=, #create_external_subset, #create_internal_subset, #css_path, #data_ptr?, #deconstruct_keys, #decorate!, #default_namespace=, #description, #do_xinclude, #document, #document?, #dup, #each, #element?, #element_children, #encode_special_chars, #external_subset, #first_element_child, #fragment, #fragment?, #html?, #inner_html, #inner_html=, #internal_subset, #key?, #keys, #kwattr_add, #kwattr_append, #kwattr_remove, #kwattr_values, #lang, #lang=, #last_element_child, #line, #line=, #matches?, #namespace, #namespace=, #namespace_definitions, #namespace_scopes, #namespaced_key?, #namespaces, #native_content=, #next_element, #next_sibling, #node_name, #node_name=, #node_type, #parent, #parent=, #parse, #path, #pointer_id, #prepend_child, #previous_element, #previous_sibling, #processing_instruction?, #read_only?, #remove_attribute, #remove_class, #replace, #serialize, #swap, #text?, #to_html, #to_s, #to_xhtml, #to_xml, #traverse, #unlink, #value?, #values, #wrap, #write_html_to, #write_to, #write_xhtml_to, #write_xml_to, #xml?

  
  
  
  
  
  
  
  
  
  
### Methods included from ClassResolver

  

#related_class

  
  
  
  
  
  
  
  
  
### Methods included from Searchable

  

#>, #at, #at_css, #at_xpath, #css, #search, #xpath

  
  
  
  
  
  
  
  
  
### Methods included from Nokogiri::XML::PP::Node

  

#inspect, #pretty_print

  
  
  
  
  
  
  
  
  
### Methods included from HTML5::Node

  

#fragment, #inner_html, #write_to

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(document, name, content)  ⇒ ProcessingInstruction 
  

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/nokogiri/xml/processing_instruction.rb', line 6

def initialize(document, name, content)
  super(document, name)
end

```

    
  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**new**(document, name, content)  ⇒ Object 
  

  

  

  
    

Create a new ProcessingInstruction element on the `document` with `name` and `content`

  

  
  

  
    
      

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
```

    
    
      

```
# File 'ext/nokogiri/xml_processing_instruction.c', line 12

static VALUE
new (int argc, VALUE *argv, VALUE klass)
{
  xmlDocPtr xml_doc;
  xmlNodePtr node;
  VALUE document;
  VALUE name;
  VALUE content;
  VALUE rest;
  VALUE rb_node;

  rb_scan_args(argc, argv, "3*", &document, &name, &content, &rest);

  xml_doc = noko_xml_document_unwrap(document);

  node = xmlNewDocPI(
           xml_doc,
           (const xmlChar *)StringValueCStr(name),
           (const xmlChar *)StringValueCStr(content)
         );

  noko_xml_document_pin_node(node);

  rb_node = noko_xml_node_wrap(klass, node);
  rb_obj_call_init(rb_node, argc, argv);

  if (rb_block_given_p()) { rb_yield(rb_node); }

  return rb_node;
}

```