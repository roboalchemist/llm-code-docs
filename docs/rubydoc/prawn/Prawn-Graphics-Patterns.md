# Module: Prawn::Graphics::Patterns
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Prawn::Graphics
  
  

  
  
    Defined in:
    lib/prawn/graphics/patterns.rb
  
  

## Overview

  
    

Implements axial & radial gradients.

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** Gradient, GradientStop
    
  

  
    
## 
      Stable API
      collapse
    

    

      
        
- 
  
    
      #**fill_gradient**(*args, **kwargs)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Sets the fill gradient.

  

      
        
- 
  
    
      #**stroke_gradient**(*args, **kwargs)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Sets the stroke gradient.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    
      #**fill_gradient**(from, to, color1, color2, apply_margin_options: false)  ⇒ void 
    
      #**fill_gradient**(from, r1, to, r2, color1, color2, apply_margin_options: false)  ⇒ void 
    
      #**fill_gradient**(from: , to: , r1: nil, r2: nil, stops: , apply_margin_options: true)  ⇒ void 
    
  

  

  

  
    

Sets the fill gradient.

  

  
  

Overloads:
  

    
      
      
- 
        #**fill_gradient**(from, to, color1, color2, apply_margin_options: false)  ⇒ void 
        
  
    

This method returns an undefined value.

Set an axial (linear) fill gradient.

  

  

Parameters:

  
    
  - 
      
      
      
      
        
        

Starting point of the gradient.

      
    
  
    
  - 
      
      
      
      
        
        

ending point of the gradient.

      
    
  
    
  - 
      
      
      
      
        
        

starting color of the gradient.

      
    
  
    
  - 
      
      
      
      
        
        

ending color of the gradient.

      
    
  
    
  - 
      
      
      
      
        
        

(false) If set `true`, will transform the gradient’s co-ordinate space so it matches the current co-ordinate space of the document. This option will be the default from Prawn v3, and is default `true` if you use the all-keyword version of this method. The default for the positional arguments version (this one), `false`, will mean if you (for example) scale your document by 2 and put a gradient inside, you will have to manually multiply your co-ordinates by 2 so the gradient is correctly positioned.

      
    
  

      
    
      
      
- 
        #**fill_gradient**(from, r1, to, r2, color1, color2, apply_margin_options: false)  ⇒ void 
        
  
    

This method returns an undefined value.

Set a radial fill gradient.

  

  

Parameters:

  
    
  - 
      
      
      
      
        
        

Starting point of the gradient.

      
    
  
    
  - 
      
      
      
      
        
        

Radius of the starting circle of a radial gradient.  The circle is centered at `from`.

      
    
  
    
  - 
      
      
      
      
        
        

Ending point of the gradient.

      
    
  
    
  - 
      
      
      
      
        
        

Radius of the ending circle of a radial gradient.  The circle is centered at `to`.

      
    
  
    
  - 
      
      
      
      
        
        

Starting color.

      
    
  
    
  - 
      
      
      
      
        
        

Ending color.

      
    
  
    
  - 
      
      
      
      
        
        

(false) If set `true`, will transform the gradient’s co-ordinate space so it matches the current co-ordinate space of the document. This option will be the default from Prawn v3, and is default `true` if you use the all-keyword version of this method. The default for the positional arguments version (this one), `false`, will mean if you (for example) scale your document by 2 and put a gradient inside, you will have to manually multiply your co-ordinates by 2 so the gradient is correctly positioned.

      
    
  

      
    
      
      
- 
        #**fill_gradient**(from: , to: , r1: nil, r2: nil, stops: , apply_margin_options: true)  ⇒ void 
        
  
    

This method returns an undefined value.

Set the fill gradient.

  

  
  
    
#### Examples:

    
      
        
##### 

Draw a horizontal axial gradient that starts at red on the left and ends at blue on the right

      
      

```
fill_gradient from: [0, 0], to: [100, 0], stops: ['ff0000', '0000ff']

```

    
      
        
##### 

Draw a horizontal radial gradient that starts at red, is green 80% through, and finishes blue

      
      

```
fill_gradient from: [0, 0], r1: 0, to: [100, 0], r2: 180,
  stops: { 0 => 'ff0000', 0.8 => '00ff00', 1 => '0000ff' }

```

    
  

Parameters:

  
    
  - 
      
      
      
        *(defaults to: )*
      
      
        
        

Starting point of the gradient.

      
    
  
    
  - 
      
      
      
        *(defaults to: nil)*
      
      
        
        

Radius of the starting circle of a radial gradient. The circle is centered at `from`. If omitted a linear gradient will be produced.

      
    
  
    
  - 
      
      
      
        *(defaults to: )*
      
      
        
        

Ending point of the gradient.

      
    
  
    
  - 
      
      
      
        *(defaults to: nil)*
      
      
        
        

Radius of the ending circle of a radial gradient.  The circle is centered at `to`.

      
    
  
    
  - 
      
      
      
        *(defaults to: )*
      
      
        
        

Color stops. Each stop is either just a color, in which case the stops will be evenly distributed across the gradient, or a hash where the key is a position between 0 and 1 indicating what distance through the gradient the color should change, and the value is a color.

      
    
  
    
  - 
      
      
      
      
        
        

(true) If set `true`, will transform the gradient’s co-ordinate space so it matches the current co-ordinate space of the document. This option will be the default from Prawn v3, and is default `true` if you use the all-keyword version of this method (this one). The default for the old arguments format, `false`, will mean if you (for example) scale your document by 2 and put a gradient inside, you will have to manually multiply your co-ordinates by 2 so the gradient is correctly positioned.

      
    
  

      
    
  

  
    
      

```

105
106
107
```

    
    
      

```
# File 'lib/prawn/graphics/patterns.rb', line 105

def fill_gradient(*args, **kwargs)
  set_gradient(:fill, *args, **kwargs)
end

```

    
  

    
      
  
### 
  
    
      #**fill_gradient**(from, to, color1, color2, apply_margin_options: false)  ⇒ void 
    
      #**fill_gradient**(from, r1, to, r2, color1, color2, apply_margin_options: false)  ⇒ void 
    
      #**fill_gradient**(from: , to: , r1: nil, r2: nil, stops: , apply_margin_options: true)  ⇒ void 
    
  

  

  

  
    

Sets the stroke gradient.

  

  
  

Overloads:
  

    
      
      
- 
        #**fill_gradient**(from, to, color1, color2, apply_margin_options: false)  ⇒ void 
        
  
    

This method returns an undefined value.

Set an axial (linear) stroke gradient.

  

  

Parameters:

  
    
  - 
      
      
      
      
        
        

Starting point of the gradient.

      
    
  
    
  - 
      
      
      
      
        
        

ending point of the gradient.

      
    
  
    
  - 
      
      
      
      
        
        

starting color of the gradient.

      
    
  
    
  - 
      
      
      
      
        
        

ending color of the gradient.

      
    
  
    
  - 
      
      
      
      
        
        

(false) If set `true`, will transform the gradient’s co-ordinate space so it matches the current co-ordinate space of the document. This option will be the default from Prawn v3, and is default `true` if you use the all-keyword version of this method. The default for the positional arguments version (this one), `false`, will mean if you (for example) scale your document by 2 and put a gradient inside, you will have to manually multiply your co-ordinates by 2 so the gradient is correctly positioned.

      
    
  

      
    
      
      
- 
        #**fill_gradient**(from, r1, to, r2, color1, color2, apply_margin_options: false)  ⇒ void 
        
  
    

This method returns an undefined value.

Set a radial stroke gradient.

  

  

Parameters:

  
    
  - 
      
      
      
      
        
        

Starting point of the gradient.

      
    
  
    
  - 
      
      
      
      
        
        

Radius of the starting circle of a radial gradient.  The circle is centered at `from`.

      
    
  
    
  - 
      
      
      
      
        
        

Ending point of the gradient.

      
    
  
    
  - 
      
      
      
      
        
        

Radius of the ending circle of a radial gradient.  The circle is centered at `to`.

      
    
  
    
  - 
      
      
      
      
        
        

Starting color.

      
    
  
    
  - 
      
      
      
      
        
        

Ending color.

      
    
  
    
  - 
      
      
      
      
        
        

(false) If set `true`, will transform the gradient’s co-ordinate space so it matches the current co-ordinate space of the document. This option will be the default from Prawn v3, and is default `true` if you use the all-keyword version of this method. The default for the positional arguments version (this one), `false`, will mean if you (for example) scale your document by 2 and put a gradient inside, you will have to manually multiply your co-ordinates by 2 so the gradient is correctly positioned.

      
    
  

      
    
      
      
- 
        #**fill_gradient**(from: , to: , r1: nil, r2: nil, stops: , apply_margin_options: true)  ⇒ void 
        
  
    

This method returns an undefined value.

Set the stroke gradient.

  

  
  
    
#### Examples:

    
      
        
##### 

Draw a horizontal axial gradient that starts at red on the left and ends at blue on the right

      
      

```
stroke_gradient from: [0, 0], to: [100, 0], stops: ['ff0000', '0000ff']

```

    
      
        
##### 

Draw a horizontal radial gradient that starts at red, is green 80% through, and finishes blue

      
      

```
stroke_gradient from: [0, 0], r1: 0, to: [100, 0], r2: 180,
  stops: { 0 => 'ff0000', 0.8 => '00ff00', 1 => '0000ff' }

```

    
  

Parameters:

  
    
  - 
      
      
      
        *(defaults to: )*
      
      
        
        

Starting point of the gradient.

      
    
  
    
  - 
      
      
      
        *(defaults to: nil)*
      
      
        
        

Radius of the starting circle of a radial gradient. The circle is centered at `from`. If omitted a linear gradient will be produced.

      
    
  
    
  - 
      
      
      
        *(defaults to: )*
      
      
        
        

Ending point of the gradient.

      
    
  
    
  - 
      
      
      
        *(defaults to: nil)*
      
      
        
        

Radius of the ending circle of a radial gradient.  The circle is centered at `to`.

      
    
  
    
  - 
      
      
      
        *(defaults to: )*
      
      
        
        

Color stops. Each stop is either just a color, in which case the stops will be evenly distributed across the gradient, or a hash where the key is a position between 0 and 1 indicating what distance through the gradient the color should change, and the value is a color.

      
    
  
    
  - 
      
      
      
      
        
        

(true) If set `true`, will transform the gradient’s co-ordinate space so it matches the current co-ordinate space of the document. This option will be the default from Prawn v3, and is default `true` if you use the all-keyword version of this method (this one). The default for the old arguments format, `false`, will mean if you (for example) scale your document by 2 and put a gradient inside, you will have to manually multiply your co-ordinates by 2 so the gradient is correctly positioned.

      
    
  

      
    
  

  
    
      

```

194
195
196
```

    
    
      

```
# File 'lib/prawn/graphics/patterns.rb', line 194

def stroke_gradient(*args, **kwargs)
  set_gradient(:stroke, *args, **kwargs)
end

```