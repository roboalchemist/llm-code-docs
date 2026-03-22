# Module: Prawn::Graphics::CapStyle
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Prawn::Graphics
  
  

  
  
    Defined in:
    lib/prawn/graphics/cap_style.rb
  
  

## Overview

  
    

Implements stroke cap styling

  

  

  
    
## 
      Stable API
      collapse
    

    
      
        CAP_STYLES =
          
        
        

```
{ butt: 0, round: 1, projecting_square: 2 }.freeze
```

      
    
  

  
    
## 
      Stable API
      collapse
    

    

      
        
- 
  
    
      #**cap_style**(style = nil)  ⇒ Object 
    

    
      (also: #cap_style=)
    
  
  
  
  
  
  
  
  

  
    

Sets the cap style for stroked lines and curves.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    
      #**cap_style**(style)  ⇒ void 
    
      #**cap_style**  ⇒ Symbol 
    
  

  
    Also known as:
    cap_style=
    
  

  

  
    

Sets the cap style for stroked lines and curves.

  

  
  

Overloads:
  

    
      
      
- 
        #**cap_style**(style)  ⇒ void 
        
  
    

This method returns an undefined value.

  

  

Parameters:

  
    
  - 
      
        style
      
      
        (:butt, :round, :projecting_square)
      
      
      
        —
        

(:butt)

      
    
  

      
    
      
      
- 
        #**cap_style**  ⇒ Symbol 
        
  
    

  

  

Returns:

  
    
  - 
      
      
        (Symbol)
      
      
      
    
  

      
    
  

  
    
      

```

19
20
21
22
23
24
25
```

    
    
      

```
# File 'lib/prawn/graphics/cap_style.rb', line 19

def cap_style(style = nil)
  return current_cap_style || :butt if style.nil?

  self.current_cap_style = style

  write_stroke_cap_style
end
```