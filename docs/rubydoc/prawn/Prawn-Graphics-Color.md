# Module: Prawn::Graphics::Color
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Prawn::Graphics
  
  

  
  
    Defined in:
    lib/prawn/graphics/color.rb
  
  

## Overview

  
    

Implements color handling.

  

  

  
    
## 
      Stable API
      collapse
    

    

      
        
- 
  
    
      .**hex2rgb**(hex)  ⇒ Array(Integer, Integer, Integer) 
    

    
  
  
  
  
  
  
  
  

  
    

Converts hex string into RGB value array.

  

      
        
- 
  
    
      .**rgb2hex**(rgb)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Converts RGB value array to hex string suitable for use with #fill_color and #stroke_color.

  

      
        
- 
  
    
      #**fill_color**(*color)  ⇒ Object 
    

    
      (also: #fill_color=)
    
  
  
  
  
  
  
  
  

  
    

Sets or returns the fill color.

  

      
        
- 
  
    
      #**stroke_color**(*color)  ⇒ Object 
    

    
      (also: #stroke_color=)
    
  
  
  
  
  
  
  
  

  
    

Sets or returns the line stroking color.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**hex2rgb**(hex)  ⇒ Array(Integer, Integer, Integer) 
  

  

  

  
    

Converts hex string into RGB value array.

  

  
  
    
#### Examples:

    
      
      

```
Prawn::Graphics::Color.hex2rgb("ff7808")
#=> [255, 120, 8]
```

    
  

Parameters:

  
    
- 
      
        hex
      
      
        (String)
      
      
      
        —
        

must be 6-digits long.

      
    
  

Returns:

  
    
- 
      
      
        (Array(Integer, Integer, Integer))
      
      
      
    
  

  
    
      

```

101
102
103
104
105
106
```

    
    
      

```
# File 'lib/prawn/graphics/color.rb', line 101

def hex2rgb(hex)
  r = hex[0..1]
  g = hex[2..3]
  b = hex[4..5]
  [r, g, b].map { |e| e.to_i(16) }
end
```

    
  

    
      
  
### 
  
    .**rgb2hex**(rgb)  ⇒ String 
  

  

  

  
    

Converts RGB value array to hex string suitable for use with #fill_color and #stroke_color.

  

  
  
    
#### Examples:

    
      
      

```
Prawn::Graphics::Color.rgb2hex([255, 120, 8])
#=> "ff7808"
```

    
  

Parameters:

  
    
- 
      
        rgb
      
      
        (Array(Number, Number, Number))
      
      
      
        —
        

Each component has to be in the range from 0 to 255.

      
    
  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

89
90
91
```

    
    
      

```
# File 'lib/prawn/graphics/color.rb', line 89

def rgb2hex(rgb)
  rgb.map { |e| format('%<value>02x', value: e) }.join
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    
      #**fill_color**  ⇒ String, Array<Number> 
    
      #**fill_color**(color)  ⇒ void 
    
  

  
    Also known as:
    fill_color=
    
  

  

  
    

Sets or returns the fill color.

  

  
  

Overloads:
  

    
      
      
- 
        #**fill_color**  ⇒ String, Array<Number> 
        
  
    

Returns the current fill color.

  

  

Returns:

  
    
  - 
      
      
        (String, Array<Number>)
      
      
      
    
  

      
    
      
      
- 
        #**fill_color**(color)  ⇒ void 
        
  
    

This method returns an undefined value.

Sets the fill color.

If a single argument is provided, it should be a 6 digit HTML color code.

“‘ruby pdf.fill_color “f0ffc1” “`

If 4 arguments are provided, the color is assumed to be a CMYK value. Values range is 0–100.

“‘ruby pdf.fill_color 0, 99, 95, 0 “`

  

  

Parameters:

  
    
  - 
      
        color
      
      
        (String, Array<Number>)
      
      
      
    
  

      
    
  

  
    
      

```

35
36
37
38
39
40
```

    
    
      

```
# File 'lib/prawn/graphics/color.rb', line 35

def fill_color(*color)
  return current_fill_color if color.empty?

  self.current_fill_color = process_color(*color)
  set_fill_color
end
```

    
  

    
      
  
### 
  
    
      #**stroke_color**  ⇒ String, Array<Number> 
    
      #**stroke_color**(color)  ⇒ void 
    
  

  
    Also known as:
    stroke_color=
    
  

  

  
    

Sets or returns the line stroking color.

  

  
  

Overloads:
  

    
      
      
- 
        #**stroke_color**  ⇒ String, Array<Number> 
        
  
    

When called with no argument, it returns the current stroking color.

  

  

Returns:

  
    
  - 
      
      
        (String, Array<Number>)
      
      
      
    
  

      
    
      
      
- 
        #**stroke_color**(color)  ⇒ void 
        
  
    

This method returns an undefined value.

Sets the stroking color.

  

  

Parameters:

  
    
  - 
      
        color
      
      
        (String, Array<Number>)
      
      
      
        —
        

new stroking color:

    - 

In String form it should be a 6 digit HTML color code.

“‘ruby pdf.stroke_color “f0ffc1” “`

    - 

If 4 arguments are provided, the color is assumed to be a CMYK value. Values range from 0 to 100.

“‘ruby pdf.stroke_color 0, 99, 95, 0 “`

      
    
  

      
    
  

  
    
      

```

67
68
69
70
71
72
73
```

    
    
      

```
# File 'lib/prawn/graphics/color.rb', line 67

def stroke_color(*color)
  return current_stroke_color if color.empty?

  color = process_color(*color)
  self.current_stroke_color = color
  set_stroke_color(color)
end
```