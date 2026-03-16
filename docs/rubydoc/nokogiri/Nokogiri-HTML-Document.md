# Class: Nokogiri::HTML::Document
  
  
  

  
  
    Inherits:
    
      XML::Document
      
        

          
- Object
          
            
- XML::Node
          
            
- XML::Document
          
            
- Nokogiri::HTML::Document
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/html.rb
  
  

## Overview

  
    

💡 This class is an alias for Nokogiri::HTML4::Document as of v1.12.0.

  

  

  
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

  
  
  
  
  
  
  
## Method Summary

  
  
### Methods inherited from XML::Document

  

#add_child, #canonicalize, #clone, #collect_namespaces, #create_cdata, #create_comment, #create_element, #create_entity, #create_text_node, #deconstruct_keys, #decorate, #decorators, #document, #dup, #encoding, #encoding=, #fragment, #initialize, #name, #namespaces, new, parse, read_io, read_memory, #remove_namespaces!, #root, #root=, #slop!, #url, #validate, #version, #xpath_doctype

  
  
  
  
  
  
  
  
  
### Methods inherited from XML::Node

  

#<<, #<=>, #==, #[], #[]=, #accept, #add_child, #add_class, #add_namespace_definition, #add_next_sibling, #add_previous_sibling, #after, #ancestors, #append_class, #attribute, #attribute_nodes, #attribute_with_ns, #attributes, #before, #blank?, #canonicalize, #cdata?, #child, #children, #children=, #classes, #clone, #comment?, #content, #content=, #create_external_subset, #create_internal_subset, #css_path, #data_ptr?, #deconstruct_keys, #decorate!, #default_namespace=, #description, #do_xinclude, #document, #document?, #dup, #each, #element?, #element_children, #encode_special_chars, #external_subset, #first_element_child, #fragment, #fragment?, #html?, #initialize, #inner_html, #inner_html=, #internal_subset, #key?, #keys, #kwattr_add, #kwattr_append, #kwattr_remove, #kwattr_values, #lang, #lang=, #last_element_child, #line, #line=, #matches?, #namespace, #namespace=, #namespace_definitions, #namespace_scopes, #namespaced_key?, #namespaces, #native_content=, new, #next_element, #next_sibling, #node_name, #node_name=, #node_type, #parent, #parent=, #parse, #path, #pointer_id, #prepend_child, #previous_element, #previous_sibling, #processing_instruction?, #read_only?, #remove_attribute, #remove_class, #replace, #serialize, #swap, #text?, #to_html, #to_s, #to_xhtml, #to_xml, #traverse, #unlink, #value?, #values, #wrap, #write_html_to, #write_to, #write_xhtml_to, #write_xml_to, #xml?

  
  
  
  
  
  
  
  
  
  
### Methods included from ClassResolver

  

#related_class

  
  
  
  
  
  
  
  
  
### Methods included from XML::Searchable

  

#>, #at, #at_css, #at_xpath, #css, #search, #xpath

  
  
  
  
  
  
  
  
  
### Methods included from XML::PP::Node

  

#inspect, #pretty_print

  
  
  
  
  
  
  
  
  
### Methods included from Nokogiri::HTML5::Node

  

#fragment, #inner_html, #write_to

  
## Constructor Details

  
    

This class inherits a constructor from Nokogiri::XML::Document