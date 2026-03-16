# Class: Nokogiri::XML::EntityDecl
  
  
  

  
  
    Inherits:
    
      Node
      
        

          
- Object
          
            
- Node
          
            
- Nokogiri::XML::EntityDecl
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/entity_decl.rb,

  ext/nokogiri/xml_entity_decl.c

  
  

  
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
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**new**(name, doc, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**content**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the content.

  

      
        
- 
  
    
      #**entity_type**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the entity type.

  

      
        
- 
  
    
      #**external_id**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the external identifier for PUBLIC.

  

      
        
- 
  
    
      #**original_content**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the original_content before ref substitution.

  

      
        
- 
  
    
      #**system_id**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the URI for a SYSTEM or PUBLIC Entity.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Node

  

#<<, #<=>, #==, #[], #[]=, #accept, #add_child, #add_class, #add_namespace_definition, #add_next_sibling, #add_previous_sibling, #after, #ancestors, #append_class, #attribute, #attribute_nodes, #attribute_with_ns, #attributes, #before, #blank?, #canonicalize, #cdata?, #child, #children, #children=, #classes, #clone, #comment?, #content=, #create_external_subset, #create_internal_subset, #css_path, #data_ptr?, #deconstruct_keys, #decorate!, #default_namespace=, #description, #do_xinclude, #document, #document?, #dup, #each, #element?, #element_children, #encode_special_chars, #external_subset, #first_element_child, #fragment, #fragment?, #html?, #initialize, #inner_html, #inner_html=, #internal_subset, #key?, #keys, #kwattr_add, #kwattr_append, #kwattr_remove, #kwattr_values, #lang, #lang=, #last_element_child, #line, #line=, #matches?, #namespace, #namespace=, #namespace_definitions, #namespace_scopes, #namespaced_key?, #namespaces, #native_content=, #next_element, #next_sibling, #node_name, #node_name=, #node_type, #parent, #parent=, #parse, #path, #pointer_id, #prepend_child, #previous_element, #previous_sibling, #processing_instruction?, #read_only?, #remove_attribute, #remove_class, #replace, #serialize, #swap, #text?, #to_html, #to_s, #to_xhtml, #to_xml, #traverse, #unlink, #value?, #values, #wrap, #write_html_to, #write_to, #write_xhtml_to, #write_xml_to, #xml?

  
  
  
  
  
  
  
  
  
  
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
  

  
    
## Class Method Details

    
      
  
### 
  
    .**new**(name, doc, *args)  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/nokogiri/xml/entity_decl.rb', line 12

def self.new(name, doc, *args)
  doc.create_entity(name, *args)
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**content**  ⇒ Object 
  

  

  

  
    

Get the content

  

  
  

  
    
      

```

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
```

    
    
      

```
# File 'ext/nokogiri/xml_entity_decl.c', line 28

static VALUE
get_content(VALUE self)
{
  xmlEntityPtr node;
  Noko_Node_Get_Struct(self, xmlEntity, node);

  if (!node->content) { return Qnil; }

  return NOKOGIRI_STR_NEW(node->content, node->length);
}

```

    
  

    
      
  
### 
  
    #**entity_type**  ⇒ Object 
  

  

  

  
    

Get the entity type

  

  
  

  
    
      

```

45
46
47
48
49
50
51
52
```

    
    
      

```
# File 'ext/nokogiri/xml_entity_decl.c', line 45

static VALUE
entity_type(VALUE self)
{
  xmlEntityPtr node;
  Noko_Node_Get_Struct(self, xmlEntity, node);

  return INT2NUM((int)node->etype);
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
  
    #**original_content**  ⇒ Object 
  

  

  

  
    

Get the original_content before ref substitution

  

  
  

  
    
      

```

11
12
13
14
15
16
17
18
19
20
```

    
    
      

```
# File 'ext/nokogiri/xml_entity_decl.c', line 11

static VALUE
original_content(VALUE self)
{
  xmlEntityPtr node;
  Noko_Node_Get_Struct(self, xmlEntity, node);

  if (!node->orig) { return Qnil; }

  return NOKOGIRI_STR_NEW2(node->orig);
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