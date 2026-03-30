# Module: Kramdown::Converter::MathEngine::Mathjax
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/converter/math_engine/mathjax.rb
  
  

## Overview

  
    

Uses the MathJax javascript library for displaying math.

Note that the javascript library itself is not include or linked, this has to be done separately. Only the math content is marked up correctly.

  

  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**call**(converter, el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**call**(converter, el, opts)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/math_engine/mathjax.rb', line 18

def self.call(converter, el, opts)
  value = converter.escape_html(el.value)
  result = el.options[:category] == :block ? "\\[#{value}\\]\n" : "\\(#{value}\\)"
  if el.attr.empty?
    result
  elsif el.options[:category] == :block
    converter.format_as_block_html('div', el.attr, result, opts[:indent])
  else
    converter.format_as_span_html('span', el.attr, "$#{el.value}$")
  end
end

```