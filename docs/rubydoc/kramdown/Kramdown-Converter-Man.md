# Class: Kramdown::Converter::Man
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- Kramdown::Converter::Man
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/converter/man.rb
  
  

## Overview

  
    

Converts a Kramdown::Document to a manpage in groff format. See man(7), groff_man(7) and man-pages(7) for information regarding the output.

  

  

  
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
  
    
      #**convert**(el, opts = {indent: 0, result: +''})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

apply_template, #apply_template_after?, #apply_template_before?, #basic_generate_id, convert, #extract_code_language, #extract_code_language!, #format_math, #generate_id, get_template, #highlight_code, #in_toc?, #initialize, #output_header_level, #smart_quote_entity, #warning

  
## Constructor Details

  
    

This class inherits a constructor from Kramdown::Converter::Base
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**convert**(el, opts = {indent: 0, result: +''})  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/kramdown/converter/man.rb', line 20

def convert(el, opts = {indent: 0, result: +''}) # :nodoc:
  send("convert_#{el.type}", el, opts)
end

```