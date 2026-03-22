# Module: Prawn::Graphics::JoinStyle
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Prawn::Graphics
  
  

  
  
    Defined in:
    lib/prawn/graphics/join_style.rb
  
  

## Overview

  
    

Implements stroke join styling.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        JOIN_STYLES =
          
        
        

```
{ miter: 0, round: 1, bevel: 2 }.freeze
```

      
    
  

  
    
## 
      Stable API
      collapse
    

    

      
        
- 
  
    
      #**join_style**(style = nil)  ⇒ Object 
    

    
      (also: #join_style=)
    
  
  
  
  
  
  
  
  

  
    

Get or set the join style for stroked lines and curves.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    
      #**join_style**  ⇒ :miter, ... 
    
      #**join_style**(style)  ⇒ void 
    
  

  
    Also known as:
    join_style=
    
  

  

  
    

Get or set the join style for stroked lines and curves.

  

  
  

Overloads:
  

    
      
      
- 
        #**join_style**  ⇒ :miter, ... 
        
  
    

Get current join style.

  

  

Returns:

  
    
  - 
      
      
        (:miter, :round, :bevel)
      
      
      
    
  

      
    
      
      
- 
        #**join_style**(style)  ⇒ void 
        
  
    
  
    **Note:**
    

If this method is never called, `:miter` will be used for join style throughout the document.

  

This method returns an undefined value.

Set join style.

  

  

Parameters:

  
    
  - 
      
        style
      
      
        (:miter, :round, :bevel)
      
      
      
    
  

      
    
  

  
    
      

```

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
# File 'lib/prawn/graphics/join_style.rb', line 29

def join_style(style = nil)
  return current_join_style || :miter if style.nil?

  self.current_join_style = style

  unless JOIN_STYLES.key?(current_join_style)
    raise Prawn::Errors::InvalidJoinStyle,
      "#{style} is not a recognized join style. Valid styles are " +
        JOIN_STYLES.keys.join(', ')
  end

  write_stroke_join_style
end
```