# Class: Kramdown::Converter::Toc
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- Kramdown::Converter::Toc
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/converter/toc.rb
  
  

## Overview

  
    

Converts a Kramdown::Document to an element tree that represents the table of contents.

The returned tree consists of Element objects of type :toc where the root element is just used as container object. Each :toc element contains as value the wrapped :header element and under the attribute key :id the header ID that should be used (note that this ID may not exist in the wrapped element).

Since the TOC tree consists of special :toc elements, one cannot directly feed this tree to other converters!

  

  

  
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
  
    
      #**initialize**(root, options)  ⇒ Toc 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Toc.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

apply_template, #apply_template_after?, #apply_template_before?, #basic_generate_id, convert, #extract_code_language, #extract_code_language!, #format_math, #generate_id, get_template, #highlight_code, #in_toc?, #output_header_level, #smart_quote_entity, #warning

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(root, options)  ⇒ Toc 
  

  

  

  
    

Returns a new instance of Toc.

  

  

  
    
      

```

27
28
29
30
31
32
```

    
    
      

```
# File 'lib/kramdown/converter/toc.rb', line 27

def initialize(root, options)
  super
  @toc = Element.new(:toc)
  @stack = []
  @options[:template] = ''
end

```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**convert**(el)  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/kramdown/converter/toc.rb', line 34

def convert(el)
  if el.type == :header && in_toc?(el)
    attr = el.attr.dup
    attr['id'] = generate_id(el.options[:raw_text]) if @options[:auto_ids] && !attr['id']
    add_to_toc(el, attr['id']) if attr['id']
  else
    el.children.each {|child| convert(child) }
  end
  @toc
end

```