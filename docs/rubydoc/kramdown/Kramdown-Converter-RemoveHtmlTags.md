# Class: Kramdown::Converter::RemoveHtmlTags
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- Kramdown::Converter::RemoveHtmlTags
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/converter/remove_html_tags.rb
  
  

## Overview

  
    

Removes all block (and optionally span) level HTML tags from the element tree.

This converter can be used on parsed HTML documents to get an element tree that will only contain native kramdown elements.

**Note** that the returned element tree may not be fully conformant (i.e. the content models of *some elements may be violated)!

This converter modifies the given tree in-place and returns it.

  

  

  
## Constant Summary

  
  
### Constants inherited
     from Base

  

Base::SMART_QUOTE_INDICES

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#data, #options, #root, #warnings

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**convert**(el)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(root, options)  ⇒ RemoveHtmlTags 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of RemoveHtmlTags.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

apply_template, #apply_template_after?, #apply_template_before?, #basic_generate_id, convert, #extract_code_language, #extract_code_language!, #format_math, #generate_id, get_template, #highlight_code, #in_toc?, #output_header_level, #smart_quote_entity, #warning

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(root, options)  ⇒ RemoveHtmlTags 
  

  

  

  
    

Returns a new instance of RemoveHtmlTags.

  

  

  
    
      

```

27
28
29
30
```

    
    
      

```
# File 'lib/kramdown/converter/remove_html_tags.rb', line 27

def initialize(root, options)
  super
  @options[:template] = ''
end

```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**convert**(el)  ⇒ Object 
  

  

  

  
    
      

```

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
51
52
53
```

    
    
      

```
# File 'lib/kramdown/converter/remove_html_tags.rb', line 32

def convert(el)
  real_el, el = el, el.value if el.type == :footnote

  children = el.children.dup
  index = 0
  while index < children.length
    if children[index].type == :xml_pi ||
        (children[index].type == :html_element && (children[index].value == 'style' ||
                                                   children[index].value == 'script'))
      children[index..index] = []
    elsif children[index].type == :html_element &&
        ((@options[:remove_block_html_tags] && children[index].options[:category] == :block) ||
         (@options[:remove_span_html_tags] && children[index].options[:category] == :span))
      children[index..index] = children[index].children
    else
      convert(children[index])
      index += 1
    end
  end
  el.children = children
  real_el || el
end

```