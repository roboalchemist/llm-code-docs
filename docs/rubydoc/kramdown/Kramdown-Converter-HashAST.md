# Class: Kramdown::Converter::HashAST
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- Kramdown::Converter::HashAST
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/converter/hash_ast.rb
  
  

## Overview

  
    

Converts a Kramdown::Document to a nested hash for further processing or debug output.

  

  

  
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
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

apply_template, #apply_template_after?, #apply_template_before?, #basic_generate_id, convert, #extract_code_language, #extract_code_language!, #format_math, #generate_id, get_template, #highlight_code, #in_toc?, #initialize, #output_header_level, #smart_quote_entity, #warning

  
## Constructor Details

  
    

This class inherits a constructor from Kramdown::Converter::Base
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**convert**(el)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/hash_ast.rb', line 21

def convert(el)
  hash = {type: el.type}
  hash[:attr] = el.attr unless el.attr.empty?
  hash[:value] = el.value unless el.value.nil?
  hash[:options] = el.options unless el.options.empty?
  unless el.children.empty?
    hash[:children] = []
    el.children.each {|child| hash[:children] << convert(child) }
  end
  hash
end

```