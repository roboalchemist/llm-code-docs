# Module: Prawn::Graphics::Transformation
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Prawn::Graphics
  
  

  
  
    Defined in:
    lib/prawn/graphics/transformation.rb
  
  

## Overview

  
    

Implements user-space coordinate transformation.

  

  

  
    
## 
      Stable API
      collapse
    

    

      
        
- 
  
    
      #**rotate**(angle, options = {}) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Rotate the user space.

  

      
        
- 
  
    
      #**scale**(factor, options = {}) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Scale the user space.

  

      
        
- 
  
    
      #**transformation_matrix**(*matrix) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Transform the user space (see notes for rotate regarding graphics state) Generally, one would use the #rotate, #scale, and #translate convenience methods instead of calling transformation_matrix directly.

  

      
        
- 
  
    
      #**translate**(x, y) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Translate the user space.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**rotate**(angle, options = {}) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Rotate the user space. If a block is not provided, then you must save and restore the graphics state yourself.

  

  
  
    
#### Examples:

    
      
      

```
save_graphics_state
rotate 30
text "rotated text"
restore_graphics_state

```

    
      
        
##### 

Rotating a rectangle around its upper-left corner

      
      

```
x = 300
y = 300
width = 150
height = 200
angle = 30
pdf.rotate(angle, :origin => [x, y]) do
  pdf.stroke_rectangle([x, y], width, height)
end

```

    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :origin
          (Array(Number, Number))
          
            
          
          
            — 

Rotation origin point. A block must be provided if specified.

          
        
      
    

  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

Raises:

  
    
- 
      
      
      
      
        
        

if an `:origin` option is provided, but no block is given.

      
    
  

Parameters:

  
    
- 
      
      
      
      
        
        

Angle in degrees.

      
    
  
    
- 
      
      
      
        *(defaults to: {})*
      
      
    
  

  
    
      

```

36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
```

    
    
      

```
# File 'lib/prawn/graphics/transformation.rb', line 36

def rotate(angle, options = {}, &block)
  Prawn.verify_options(:origin, options)
  rad = degree_to_rad(angle)
  cos = Math.cos(rad)
  sin = Math.sin(rad)
  if options[:origin].nil?
    transformation_matrix(cos, sin, -sin, cos, 0, 0, &block)
  else
    raise Prawn::Errors::BlockRequired unless block

    x = options[:origin][0] + bounds.absolute_left
    y = options[:origin][1] + bounds.absolute_bottom
    x_prime = (x * cos) - (y * sin)
    y_prime = (x * sin) + (y * cos)
    translate(x - x_prime, y - y_prime) do
      transformation_matrix(cos, sin, -sin, cos, 0, 0, &block)
    end
  end
end

```

    
  

    
      
  
### 
  
    #**scale**(factor, options = {}) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Scale the user space. If a block is not provided, then you must save and restore the graphics state yourself.

  

  
  
    
#### Examples:

    
      
      

```
save_graphics_state
scale 1.5
text "scaled text"
restore_graphics_state

```

    
      
        
##### 

Scale a rectangle from its upper-left corner

      
      

```
x = 300
y = 300
width = 150
height = 200
factor = 1.5
pdf.scale(angle, :origin => [x, y]) do
  pdf.stroke_rectangle([x, y], width, height)
end

```

    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :origin
          (Array(Number, Number))
          
            
          
          
            — 

The point from which to scale. A block must be provided if specified.

          
        
      
    

  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

Raises:

  
    
- 
      
      
      
      
        
        

If an `:origin` option is provided, but no block is given.

      
    
  

Parameters:

  
    
- 
      
      
      
      
        
        

Scale factor.

      
    
  
    
- 
      
      
      
        *(defaults to: {})*
      
      
    
  

  
    
      

```

109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
```

    
    
      

```
# File 'lib/prawn/graphics/transformation.rb', line 109

def scale(factor, options = {}, &block)
  Prawn.verify_options(:origin, options)
  if options[:origin].nil?
    transformation_matrix(factor, 0, 0, factor, 0, 0, &block)
  else
    raise Prawn::Errors::BlockRequired unless block

    x = options[:origin][0] + bounds.absolute_left
    y = options[:origin][1] + bounds.absolute_bottom
    x_prime = factor * x
    y_prime = factor * y
    translate(x - x_prime, y - y_prime) do
      transformation_matrix(factor, 0, 0, factor, 0, 0, &block)
    end
  end
end

```

    
  

    
      
  
### 
  
    #**transformation_matrix**(*matrix) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Transform the user space (see notes for rotate regarding graphics state) Generally, one would use the #rotate, #scale, and #translate convenience methods instead of calling transformation_matrix directly

  

  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

Parameters:

  
    
- 
      
      
      
      
        
        

Transformation matrix.

The six elements correspond to the following elements of the transformation matrix:

“‘plain a b 0 c d 0 e f 0 “`

      
    
  

  
    
      

```

154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
```

    
    
      

```
# File 'lib/prawn/graphics/transformation.rb', line 154

def transformation_matrix(*matrix)
  if matrix.length != 6
    raise ArgumentError,
      'Transformation matrix must have exacty 6 elements'
  end
  save_graphics_state if block_given?

  add_to_transformation_stack(*matrix)

  values = PDF::Core.real_params(matrix)
  renderer.add_content("#{values} cm")
  if block_given?
    yield
    restore_graphics_state
  end
end

```

    
  

    
      
  
### 
  
    #**translate**(x, y) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Translate the user space. If a block is not provided, then you must save and restore the graphics state yourself.

  

  
  
    
#### Examples:

    
      
        
##### 

Move the text up and over 10

      
      

```
save_graphics_state
translate(10, 10)
text "scaled text"
restore_graphics_state

```

    
      
        
##### 

draw a rectangle with its upper-left corner at x + 10, y + 10

      
      

```
x = 300
y = 300
width = 150
height = 200
pdf.translate(10, 10) do
  pdf.stroke_rectangle([x, y], width, height)
end

```

    
  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

Parameters:

  
    
- 
      
      
      
      
    
  
    
- 
      
      
      
      
    
  

  
    
      

```

78
79
80
```

    
    
      

```
# File 'lib/prawn/graphics/transformation.rb', line 78

def translate(x, y, &block)
  transformation_matrix(1, 0, 0, 1, x, y, &block)
end

```