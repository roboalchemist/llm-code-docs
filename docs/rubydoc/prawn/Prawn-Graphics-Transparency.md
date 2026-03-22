# Module: Prawn::Graphics::Transparency
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Prawn::Graphics
  
  

  
  
    Defined in:
    lib/prawn/graphics/transparency.rb
  
  

## Overview

  
    

This module is used to place transparent content on the page. It has the capacity for separate transparency values for stroked content and all other content.

  

  

  
    
## 
      Stable API
      collapse
    

    

      
        
- 
  
    
      #**transparent**(opacity, stroke_opacity = opacity) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Set opacity.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**transparent**(opacity, stroke_opacity = opacity) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Set opacity.

  

  
  
    
#### Examples:

    
      
        
##### 

Both the fill and stroke will be at 50% opacity.

      
      

```
pdf.transparent(0.5) do
  pdf.text("hello world")
  pdf.fill_and_stroke_circle([x, y], 25)
end

```

    
      
        
##### 

The fill will be at 50% opacity, but the stroke will be at 75% opacity.

      
      

```
pdf.transparent(0.5, 0.75) do
  pdf.text("hello world")
  pdf.fill_and_stroke_circle([x, y], 25)
end

```

    
  

Parameters:

  
    
- 
      
        opacity
      
      
        (Number)
      
      
      
        —
        

Fill opacity. Clipped to the 0.0 to 1.0 range.

      
    
  
    
- 
      
        stroke_opacity
      
      
        (Number)
      
      
        *(defaults to: opacity)*
      
      
        —
        

Stroke opacity. Clipped to the 0.0 to 1.0 range.

      
    
  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

  
    
      

```

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
42
```

    
    
      

```
# File 'lib/prawn/graphics/transparency.rb', line 30

def transparent(opacity, stroke_opacity = opacity)
  renderer.min_version(1.4)

  opacity = opacity.clamp(0.0, 1.0)
  stroke_opacity = stroke_opacity.clamp(0.0, 1.0)

  save_graphics_state
  renderer.add_content(
    "/#{opacity_dictionary_name(opacity, stroke_opacity)} gs",
  )
  yield
  restore_graphics_state
end

```