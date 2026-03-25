# Module: Prawn::Graphics::BlendMode
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Prawn::Graphics
  
  

  
  
    Defined in:
    lib/prawn/graphics/blend_mode.rb
  
  

## Overview

  
    

The BlendMode module is used to change the way two graphic objects are blended together.

  

  

  
    
## 
      Stable API
      collapse
    

    

      
        
- 
  
    
      #**blend_mode**(blend_mode = :Normal) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Set blend mode.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**blend_mode**(blend_mode = :Normal) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Set blend mode. If a block is passed blend mode is restored afterwards.

Passing an array of blend modes is allowed. PDF viewers should blend layers based on the first recognized blend mode.

Valid blend modes since PDF 1.4 include `:Normal`, `:Multiply`, `:Screen`, `:Overlay`, `:Darken`, `:Lighten`, `:ColorDodge`, `:ColorBurn`, `:HardLight`, `:SoftLight`, `:Difference`, `:Exclusion`, `:Hue`, `:Saturation`, `:Color`, and `:Luminosity`.

  

  
  
    
#### Examples:

    
      
      

```
pdf.fill_color('0000ff')
pdf.fill_rectangle([x, y + 25], 50, 50)
pdf.blend_mode(:Multiply) do
  pdf.fill_color('ff0000')
  pdf.fill_circle([x, y], 25)
end

```

    
  

Parameters:

  
    
- 
      
        blend_mode
      
      
        (Symbol, Array<Symbol>)
      
      
        *(defaults to: :Normal)*
      
      
    
  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/prawn/graphics/blend_mode.rb', line 31

def blend_mode(blend_mode = :Normal)
  renderer.min_version(1.4)

  save_graphics_state if block_given?
  renderer.add_content("/#{blend_mode_dictionary_name(blend_mode)} gs")
  if block_given?
    yield
    restore_graphics_state
  end
end

```