# Class: Nokogiri::XML::AttributeDecl
  
  
  

  
  
    Inherits:
    
      Node
      
        

          
- Object
          
            
- Node
          
            
- Nokogiri::XML::AttributeDecl
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/attribute_decl.rb,

  ext/nokogiri/xml_attribute_decl.c

  
  

## Overview

  
    

Represents an attribute declaration in a DTD

  

  

  
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
  
    
      #**attribute_type**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The attribute_type for this AttributeDecl.

  

      
        
- 
  
    
      #**default**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The default value.

  

      
        
- 
  
    
      #**enumeration**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

An enumeration of possible values.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Node

  

#<<, #<=>, #==, #[], #[]=, #accept, #add_child, #add_class, #add_namespace_definition, #add_next_sibling, #add_previous_sibling, #after, #ancestors, #append_class, #attribute, #attribute_nodes, #attribute_with_ns, #attributes, #before, #blank?, #canonicalize, #cdata?, #child, #children, #children=, #classes, #clone, #comment?, #content, #content=, #create_external_subset, #create_internal_subset, #css_path, #data_ptr?, #deconstruct_keys, #decorate!, #default_namespace=, #description, #do_xinclude, #document, #document?, #dup, #each, #element?, #element_children, #encode_special_chars, #external_subset, #first_element_child, #fragment, #fragment?, #html?, #initialize, #inner_html, #inner_html=, #internal_subset, #key?, #keys, #kwattr_add, #kwattr_append, #kwattr_remove, #kwattr_values, #lang, #lang=, #last_element_child, #line, #line=, #matches?, #namespace, #namespace=, #namespace_definitions, #namespace_scopes, #namespaced_key?, #namespaces, #native_content=, new, #next_element, #next_sibling, #node_name, #node_name=, #node_type, #parent, #parent=, #parse, #path, #pointer_id, #prepend_child, #previous_element, #previous_sibling, #processing_instruction?, #read_only?, #remove_attribute, #remove_class, #replace, #serialize, #swap, #text?, #to_html, #to_s, #to_xhtml, #to_xml, #traverse, #unlink, #value?, #values, #wrap, #write_html_to, #write_to, #write_xhtml_to, #write_xml_to, #xml?

  
  
  
  
  
  
  
  
  
  
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
  
    #**attribute_type**  ⇒ Object 
  

  

  

  
    

The attribute_type for this AttributeDecl

  

  
  

  
    
      

```

11
12
13
14
15
16
17
```

    
    
      

```
# File 'ext/nokogiri/xml_attribute_decl.c', line 11

static VALUE
attribute_type(VALUE self)
{
  xmlAttributePtr node;
  Noko_Node_Get_Struct(self, xmlAttribute, node);
  return INT2NUM(node->atype);
}

```

    
  

    
      
  
### 
  
    #**default**  ⇒ Object 
  

  

  

  
    

The default value

  

  
  

  
    
      

```

25
26
27
28
29
30
31
32
33
```

    
    
      

```
# File 'ext/nokogiri/xml_attribute_decl.c', line 25

static VALUE
default_value(VALUE self)
{
  xmlAttributePtr node;
  Noko_Node_Get_Struct(self, xmlAttribute, node);

  if (node->defaultValue) { return NOKOGIRI_STR_NEW2(node->defaultValue); }
  return Qnil;
}

```

    
  

    
      
  
### 
  
    #**enumeration**  ⇒ Object 
  

  

  

  
    

An enumeration of possible values

  

  
  

  
    
      

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
57
58
59
```

    
    
      

```
# File 'ext/nokogiri/xml_attribute_decl.c', line 41

static VALUE
enumeration(VALUE self)
{
  xmlAttributePtr node;
  xmlEnumerationPtr enm;
  VALUE list;

  Noko_Node_Get_Struct(self, xmlAttribute, node);

  list = rb_ary_new();
  enm = node->tree;

  while (enm) {
    rb_ary_push(list, NOKOGIRI_STR_NEW2(enm->name));
    enm = enm->next;
  }

  return list;
}

```