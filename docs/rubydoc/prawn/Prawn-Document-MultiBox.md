# Class: Prawn::Document::MultiBox
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Prawn::Document::MultiBox
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/grid.rb
  
  

## Overview

  
    

A MultiBox is specified by 2 Boxes and spans the areas between.

  

  

  
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
  
    
      #**initialize**(pdf, box1, box2)  ⇒ MultiBox 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of MultiBox.

  

      
        
- 
  
    
      #**left**  ⇒ Float 
    

    
  
  
  
  
  
  
  
  

  
    

x-coordinate of left side.

  

      
        
- 
  
    
      #**name**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Mostly diagnostic method that outputs the name of a box.

  

      
        
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
  
    #**initialize**(pdf, box1, box2)  ⇒ MultiBox 
  

  

  

  
    

Returns a new instance of MultiBox.

  

  

  
    
      

```

299
300
301
302
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 299

def initialize(pdf, box1, box2)
  @pdf = pdf
  @boxes = [box1, box2]
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**pdf**  ⇒ Object  (readonly)
  

  

  

  
    
      

```

305
306
307
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 305

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
      
      
      
      
    
  

  
    
      

```

364
365
366
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 364

def bottom
  bottom_box.bottom
end

```

    
  

    
      
  
### 
  
    #**bottom_left**  ⇒ Array(Float, Float) 
  

  

  

  
    

x,y coordinates of bottom left corner.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

385
386
387
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 385

def bottom_left
  [left, bottom]
end

```

    
  

    
      
  
### 
  
    #**bottom_right**  ⇒ Array(Float, Float) 
  

  

  

  
    

x,y coordinates of bottom right corner.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

392
393
394
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 392

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

400
401
402
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 400

def bounding_box(&blk)
  pdf.bounding_box(top_left, width: width, height: height, &blk)
end

```

    
  

    
      
  
### 
  
    #**gutter**  ⇒ Float 
  

  

  

  
    

Width of the gutter.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

336
337
338
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 336

def gutter
  @boxes[0].gutter
end

```

    
  

    
      
  
### 
  
    #**height**  ⇒ Float 
  

  

  

  
    

Height of a box.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

329
330
331
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 329

def height
  top_box.top - bottom_box.bottom
end

```

    
  

    
      
  
### 
  
    #**left**  ⇒ Float 
  

  

  

  
    

x-coordinate of left side.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

343
344
345
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 343

def left
  left_box.left
end

```

    
  

    
      
  
### 
  
    #**name**  ⇒ String 
  

  

  

  
    

Mostly diagnostic method that outputs the name of a box.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

310
311
312
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 310

def name
  @boxes.map(&:name).join(':')
end

```

    
  

    
      
  
### 
  
    #**right**  ⇒ Float 
  

  

  

  
    

x-coordinate of right side.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

350
351
352
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 350

def right
  right_box.right
end

```

    
  

    
      
  
### 
  
    #**show**(grid_color = 'CCCCCC')  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Drawn the box. Diagnostic method.

  

  

Parameters:

  
    
- 
      
      
      
        *(defaults to: 'CCCCCC')*
      
      
    
  

  
    
      

```

408
409
410
411
412
413
414
415
416
417
418
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 408

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
      
      
      
      
    
  

  
    
      

```

357
358
359
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 357

def top
  top_box.top
end

```

    
  

    
      
  
### 
  
    #**top_left**  ⇒ Array(Float, Float) 
  

  

  

  
    

x,y coordinates of top left corner.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

371
372
373
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 371

def top_left
  [left, top]
end

```

    
  

    
      
  
### 
  
    #**top_right**  ⇒ Array(Float, Float) 
  

  

  

  
    

x,y coordinates of top right corner.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

378
379
380
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 378

def top_right
  [right, top]
end

```

    
  

    
      
  
### 
  
    #**total_height**  ⇒ Object 
  

  

  

  
    
      

```

315
316
317
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 315

def total_height
  @boxes[0].total_height
end

```

    
  

    
      
  
### 
  
    #**width**  ⇒ Float 
  

  

  

  
    

Width of a box.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

322
323
324
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 322

def width
  right_box.right - left_box.left
end

```