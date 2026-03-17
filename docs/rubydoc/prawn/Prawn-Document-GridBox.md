# Class: Prawn::Document::GridBox
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Prawn::Document::GridBox
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/grid.rb
  
  

## Overview

  
    

A Box is a class that represents a bounded area of a page. A Grid object has methods that allow easy access to the coordinates of its corners, which can be plugged into most existing Prawn methods.

  

  

  
## Experimental API collapse

  

    
      
- 
  
    
      #**pdf**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    
  

    
  

  
    
## 
      Experimental API
      collapse
    

    

      
        
- 
  
    
      #**bottom**  ⇒ Float 
    

    
  
  
  
  
  
  
  
  

  
    

y-coordinate of the bottom.

  

      
        
- 
  
    
      #**bottom_left**  ⇒ Array(Float, Float) 
    

    
  
  
  
  
  
  
  
  

  
    

x,y coordinates of bottom left corner.

  

      
        
- 
  
    
      #**bottom_right**  ⇒ Array(Float, Float) 
    

    
  
  
  
  
  
  
  
  

  
    

x,y coordinates of bottom right corner.

  

      
        
- 
  
    
      #**bounding_box** { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Creates a standard bounding box based on the grid box.

  

      
        
- 
  
    
      #**gutter**  ⇒ Float 
    

    
  
  
  
  
  
  
  
  

  
    

Width of the gutter.

  

      
        
- 
  
    
      #**height**  ⇒ Float 
    

    
  
  
  
  
  
  
  
  

  
    

Height of a box.

  

      
        
- 
  
    
      #**initialize**(pdf, rows, columns)  ⇒ GridBox 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of GridBox.

  

      
        
- 
  
    
      #**left**  ⇒ Float 
    

    
  
  
  
  
  
  
  
  

  
    

x-coordinate of left side.

  

      
        
- 
  
    
      #**name**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Mostly diagnostic method that outputs the name of a box as col_num, row_num.

  

      
        
- 
  
    
      #**right**  ⇒ Float 
    

    
  
  
  
  
  
  
  
  

  
    

x-coordinate of right side.

  

      
        
- 
  
    
      #**show**(grid_color = 'CCCCCC')  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Drawn the box.

  

      
        
- 
  
    
      #**top**  ⇒ Float 
    

    
  
  
  
  
  
  
  
  

  
    

y-coordinate of the top.

  

      
        
- 
  
    
      #**top_left**  ⇒ Array(Float, Float) 
    

    
  
  
  
  
  
  
  
  

  
    

x,y coordinates of top left corner.

  

      
        
- 
  
    
      #**top_right**  ⇒ Array(Float, Float) 
    

    
  
  
  
  
  
  
  
  

  
    

x,y coordinates of top right corner.

  

      
        
- 
  
    
      #**total_height**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**width**  ⇒ Float 
    

    
  
  
  
  
  
  
  
  

  
    

Width of a box.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(pdf, rows, columns)  ⇒ GridBox 
  

  

  

  
    

Returns a new instance of GridBox.

  

  

  
    
      

```

168
169
170
171
172
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 168

def initialize(pdf, rows, columns)
  @pdf = pdf
  @rows = rows
  @columns = columns
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**pdf**  ⇒ Object  (readonly)
  

  

  

  
    
      

```

166
167
168
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 166

def pdf
  @pdf
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**bottom**  ⇒ Float 
  

  

  

  
    

y-coordinate of the bottom.

  

  

Returns:

  
    
- 
      
      
        (Float)
      
      
      
    
  

  
    
      

```

232
233
234
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 232

def bottom
  @bottom ||= top - height
end

```

    
  

    
      
  
### 
  
    #**bottom_left**  ⇒ Array(Float, Float) 
  

  

  

  
    

x,y coordinates of bottom left corner.

  

  

Returns:

  
    
- 
      
      
        (Array(Float, Float))
      
      
      
    
  

  
    
      

```

253
254
255
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 253

def bottom_left
  [left, bottom]
end

```

    
  

    
      
  
### 
  
    #**bottom_right**  ⇒ Array(Float, Float) 
  

  

  

  
    

x,y coordinates of bottom right corner.

  

  

Returns:

  
    
- 
      
      
        (Array(Float, Float))
      
      
      
    
  

  
    
      

```

260
261
262
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 260

def bottom_right
  [right, bottom]
end

```

    
  

    
      
  
### 
  
    #**bounding_box** { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Creates a standard bounding box based on the grid box.

  

  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

  
    
      

```

268
269
270
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 268

def bounding_box(&blk)
  pdf.bounding_box(top_left, width: width, height: height, &blk)
end

```

    
  

    
      
  
### 
  
    #**gutter**  ⇒ Float 
  

  

  

  
    

Width of the gutter.

  

  

Returns:

  
    
- 
      
      
        (Float)
      
      
      
    
  

  
    
      

```

204
205
206
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 204

def gutter
  Float(grid.gutter)
end

```

    
  

    
      
  
### 
  
    #**height**  ⇒ Float 
  

  

  

  
    

Height of a box.

  

  

Returns:

  
    
- 
      
      
        (Float)
      
      
      
    
  

  
    
      

```

197
198
199
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 197

def height
  Float(grid.row_height)
end

```

    
  

    
      
  
### 
  
    #**left**  ⇒ Float 
  

  

  

  
    

x-coordinate of left side.

  

  

Returns:

  
    
- 
      
      
        (Float)
      
      
      
    
  

  
    
      

```

211
212
213
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 211

def left
  @left ||= (width + grid.column_gutter) * Float(@columns)
end

```

    
  

    
      
  
### 
  
    #**name**  ⇒ String 
  

  

  

  
    

Mostly diagnostic method that outputs the name of a box as col_num, row_num

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

178
179
180
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 178

def name
  "#{@rows},#{@columns}"
end

```

    
  

    
      
  
### 
  
    #**right**  ⇒ Float 
  

  

  

  
    

x-coordinate of right side.

  

  

Returns:

  
    
- 
      
      
        (Float)
      
      
      
    
  

  
    
      

```

218
219
220
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 218

def right
  @right ||= left + width
end

```

    
  

    
      
  
### 
  
    #**show**(grid_color = 'CCCCCC')  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Drawn the box. Diagnostic method.

  

  

Parameters:

  
    
- 
      
        grid_color
      
      
        (Color)
      
      
        *(defaults to: 'CCCCCC')*
      
      
    
  

  
    
      

```

276
277
278
279
280
281
282
283
284
285
286
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 276

def show(grid_color = 'CCCCCC')
  bounding_box do
    original_stroke_color = pdf.stroke_color

    pdf.stroke_color = grid_color
    pdf.text(name)
    pdf.stroke_bounds

    pdf.stroke_color = original_stroke_color
  end
end

```

    
  

    
      
  
### 
  
    #**top**  ⇒ Float 
  

  

  

  
    

y-coordinate of the top.

  

  

Returns:

  
    
- 
      
      
        (Float)
      
      
      
    
  

  
    
      

```

225
226
227
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 225

def top
  @top ||= total_height - ((height + grid.row_gutter) * Float(@rows))
end

```

    
  

    
      
  
### 
  
    #**top_left**  ⇒ Array(Float, Float) 
  

  

  

  
    

x,y coordinates of top left corner.

  

  

Returns:

  
    
- 
      
      
        (Array(Float, Float))
      
      
      
    
  

  
    
      

```

239
240
241
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 239

def top_left
  [left, top]
end

```

    
  

    
      
  
### 
  
    #**top_right**  ⇒ Array(Float, Float) 
  

  

  

  
    

x,y coordinates of top right corner.

  

  

Returns:

  
    
- 
      
      
        (Array(Float, Float))
      
      
      
    
  

  
    
      

```

246
247
248
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 246

def top_right
  [right, top]
end

```

    
  

    
      
  
### 
  
    #**total_height**  ⇒ Object 
  

  

  

  
    
      

```

183
184
185
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 183

def total_height
  Float(pdf.bounds.height)
end

```

    
  

    
      
  
### 
  
    #**width**  ⇒ Float 
  

  

  

  
    

Width of a box.

  

  

Returns:

  
    
- 
      
      
        (Float)
      
      
      
    
  

  
    
      

```

190
191
192
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 190

def width
  Float(grid.column_width)
end

```