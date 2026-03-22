# Class: Prawn::Document::BoundingBox
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Prawn::Document::BoundingBox
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/document/bounding_box.rb
  
  

## Overview

  
    

Low level layout helper that simplifies coordinate math.

See #bounding_box for a description of what this class is used for.

  

  

  
## Direct Known Subclasses

  

ColumnBox

## Defined Under Namespace

  
    
  
    
      **Classes:** NoReferenceBounds
    
  

  
## Stable API collapse

  

    
      
- 
  
    
      #**document**  ⇒ Prawn::Document 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Owning document.

  

    
      
- 
  
    
      #**parent**  ⇒ BoundingBox? 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Parent bounding box.

  

    
      
- 
  
    
      #**total_left_padding**  ⇒ Number 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The current indentation of the left side of the bounding box.

  

    
      
- 
  
    
      #**total_right_padding**  ⇒ Number 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The current indentation of the right side of the bounding box.

  

    
      
- 
  
    
      #**width**  ⇒ Number 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Width of the bounding box.

  

    
  

  
    
## 
      Stable API
      collapse
    

    

      
        
- 
  
    
      #**absolute_bottom**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Absolute bottom y-coordinate of the bottom box.

  

      
        
- 
  
    
      #**absolute_bottom_left**  ⇒ Array(Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

Absolute bottom-left point of the bounding box.

  

      
        
- 
  
    
      #**absolute_bottom_right**  ⇒ Array(Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

Absolute bottom-left point of the bounding box.

  

      
        
- 
  
    
      #**absolute_left**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Absolute left x-coordinate of the bounding box.

  

      
        
- 
  
    
      #**absolute_right**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Absolute right x-coordinate of the bounding box.

  

      
        
- 
  
    
      #**absolute_top**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Absolute top y-coordinate of the bounding box.

  

      
        
- 
  
    
      #**absolute_top_left**  ⇒ Array(Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

Absolute top-left point of the bounding box.

  

      
        
- 
  
    
      #**absolute_top_right**  ⇒ Array(Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

Absolute top-right point of the bounding box.

  

      
        
- 
  
    
      #**add_left_padding**(left_padding)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Increase the left padding of the bounding box.

  

      
        
- 
  
    
      #**add_right_padding**(right_padding)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Increase the right padding of the bounding box.

  

      
        
- 
  
    
      #**anchor**  ⇒ Array(Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

The translated origin (x, y - height) which describes the location of the bottom left corner of the bounding box.

  

      
        
- 
  
    
      #**bottom**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Relative bottom y-coordinate of the bounding box.

  

      
        
- 
  
    
      #**bottom_left**  ⇒ Array(Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

Relative bottom-left point of the bounding box.

  

      
        
- 
  
    
      #**bottom_right**  ⇒ Array(Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

Relative bottom-right point of the bounding box.

  

      
        
- 
  
    
      #**height**  ⇒ Number 
    

    
      (also: #update_height)
    
  
  
  
  
  
  
  
  

  
    

Height of the bounding box.

  

      
        
- 
  
    
      #**indent**(left_padding, right_padding = 0)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Temporarily adjust the x coordinate to allow for left padding.

  

      
        
- 
  
    
      #**initialize**(document, parent, point, options = {})  ⇒ BoundingBox 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of BoundingBox.

  

      
        
- 
  
    
      #**left**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Relative left x-coordinate of the bounding box.

  

      
        
- 
  
    
      #**left_side**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

An alias for #absolute_left.

  

      
        
- 
  
    
      #**right**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Relative right x-coordinate of the bounding box.

  

      
        
- 
  
    
      #**right_side**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

An alias for #absolute_right.

  

      
        
- 
  
    
      #**subtract_left_padding**(left_padding)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Decrease the left padding of the bounding box.

  

      
        
- 
  
    
      #**subtract_right_padding**(right_padding)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Decrease the right padding of the bounding box.

  

      
        
- 
  
    
      #**top**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Relative top y-coordinate of the bounding box.

  

      
        
- 
  
    
      #**top_left**  ⇒ Array(Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

Relative top-left point of the bounding_box.

  

      
        
- 
  
    
      #**top_right**  ⇒ Array(Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

Relative top-right point of the bounding box.

  

      
    

  
    
## 
      Extension API
      collapse
    

    

      
        
- 
  
    
      .**restore_deep_copy**(bounds, document)  ⇒ BoundingBox 
    

    
  
  
  
  
  
  
  
  

  
    

Restores a copy of the bounds taken by #deep_copy in the context of the given `document`.

  

      
        
- 
  
    
      #**deep_copy**  ⇒ BoundingBox 
    

    
  
  
  
  
  
  
  
  

  
    

Returns a deep copy of these bounds (including all parent bounds but not copying the reference to the Document).

  

      
        
- 
  
    
      #**move_past_bottom**  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Moves to the top of the next page of the document, starting a new page if necessary.

  

      
        
- 
  
    
      #**reference_bounds**  ⇒ BoundingBox 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the innermost non-stretchy bounding box.

  

      
        
- 
  
    
      #**stretchy?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns `false` when the box has a defined height, `true` when the height is being calculated on the fly based on the current vertical position.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(document, parent, point, options = {})  ⇒ BoundingBox 
  

  

  

  
    

Returns a new instance of BoundingBox.

  

  

Parameters:

  
    
- 
      
        document
      
      
        (Prawn::Document)
      
      
      
        —
        

ownding document

      
    
  
    
- 
      
        parent
      
      
        (BoundingBox?)
      
      
      
        —
        

parent bounding box

      
    
  
    
- 
      
        point
      
      
        (Array(Number, Number))
      
      
      
        —
        

coordinates of the top left corner

      
    
  
    
- 
      
        options
      
      
        (Hash{Symbol => any})
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :width
          (Number)
          
            
          
          
            — 

width

          
        
      
        
- 
          :height
          (Number)
          
            
          
          
            — 

optional height

          
        
      
    

  

  
    
      

```

258
259
260
261
262
263
264
265
266
267
268
269
270
271
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 258

def initialize(document, parent, point, options = {})
  unless options[:width]
    raise ArgumentError, 'BoundingBox needs the :width option to be set'
  end

  @document = document
  @parent = parent
  @x, @y = point
  @width = options[:width]
  @height = options[:height]
  @total_left_padding = 0
  @total_right_padding = 0
  @stretched_height = nil
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**document**  ⇒ Prawn::Document  (readonly)
  

  

  

  
    

Owning document.

  

  

Returns:

  
    
- 
      
      
        (Prawn::Document)
      
      
      
    
  

  
    
      

```

277
278
279
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 277

def document
  @document
end

```

    
  

    
      
      
      
  
### 
  
    #**parent**  ⇒ BoundingBox?  (readonly)
  

  

  

  
    

Parent bounding box.

  

  

Returns:

  
    
- 
      
      
        (BoundingBox?)
      
      
      
    
  

  
    
      

```

283
284
285
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 283

def parent
  @parent
end

```

    
  

    
      
      
      
  
### 
  
    #**total_left_padding**  ⇒ Number  (readonly)
  

  

  

  
    

The current indentation of the left side of the bounding box.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

289
290
291
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 289

def total_left_padding
  @total_left_padding
end

```

    
  

    
      
      
      
  
### 
  
    #**total_right_padding**  ⇒ Number  (readonly)
  

  

  

  
    

The current indentation of the right side of the bounding box.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

295
296
297
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 295

def total_right_padding
  @total_right_padding
end

```

    
  

    
      
      
      
  
### 
  
    #**width**  ⇒ Number  (readonly)
  

  

  

  
    

Width of the bounding box.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

522
523
524
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 522

def width
  @width
end

```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**restore_deep_copy**(bounds, document)  ⇒ BoundingBox 
  

  

  

  
    

Restores a copy of the bounds taken by #deep_copy in the context of the given `document`. Does **not** set the bounds of the document to the resulting Prawn::Document::BoundingBox, only returns it.

  

  

Parameters:

  
    
- 
      
        bounds
      
      
        (BoundingBox)
      
      
      
    
  
    
- 
      
        document
      
      
        (Prawn::Document)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (BoundingBox)
      
      
      
    
  

  
    
      

```

619
620
621
622
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 619

def self.restore_deep_copy(bounds, document)
  bounds.instance_variable_set(:@document, document)
  bounds
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**absolute_bottom**  ⇒ Number 
  

  

  

  
    

Absolute bottom y-coordinate of the bottom box.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

487
488
489
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 487

def absolute_bottom
  @y - height
end

```

    
  

    
      
  
### 
  
    #**absolute_bottom_left**  ⇒ Array(Number, Number) 
  

  

  

  
    

Absolute bottom-left point of the bounding box.

  

  

Returns:

  
    
- 
      
      
        (Array(Number, Number))
      
      
      
    
  

  
    
      

```

508
509
510
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 508

def absolute_bottom_left
  [absolute_left, absolute_bottom]
end

```

    
  

    
      
  
### 
  
    #**absolute_bottom_right**  ⇒ Array(Number, Number) 
  

  

  

  
    

Absolute bottom-left point of the bounding box.

  

  

Returns:

  
    
- 
      
      
        (Array(Number, Number))
      
      
      
    
  

  
    
      

```

515
516
517
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 515

def absolute_bottom_right
  [absolute_right, absolute_bottom]
end

```

    
  

    
      
  
### 
  
    #**absolute_left**  ⇒ Number 
  

  

  

  
    

Absolute left x-coordinate of the bounding box.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

466
467
468
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 466

def absolute_left
  @x
end

```

    
  

    
      
  
### 
  
    #**absolute_right**  ⇒ Number 
  

  

  

  
    

Absolute right x-coordinate of the bounding box.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

473
474
475
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 473

def absolute_right
  @x + width
end

```

    
  

    
      
  
### 
  
    #**absolute_top**  ⇒ Number 
  

  

  

  
    

Absolute top y-coordinate of the bounding box.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

480
481
482
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 480

def absolute_top
  @y
end

```

    
  

    
      
  
### 
  
    #**absolute_top_left**  ⇒ Array(Number, Number) 
  

  

  

  
    

Absolute top-left point of the bounding box.

  

  

Returns:

  
    
- 
      
      
        (Array(Number, Number))
      
      
      
    
  

  
    
      

```

494
495
496
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 494

def absolute_top_left
  [absolute_left, absolute_top]
end

```

    
  

    
      
  
### 
  
    #**absolute_top_right**  ⇒ Array(Number, Number) 
  

  

  

  
    

Absolute top-right point of the bounding box.

  

  

Returns:

  
    
- 
      
      
        (Array(Number, Number))
      
      
      
    
  

  
    
      

```

501
502
503
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 501

def absolute_top_right
  [absolute_right, absolute_top]
end

```

    
  

    
      
  
### 
  
    #**add_left_padding**(left_padding)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Increase the left padding of the bounding box.

  

  

Parameters:

  
    
- 
      
        left_padding
      
      
        (Number)
      
      
      
    
  

  
    
      

```

348
349
350
351
352
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 348

def add_left_padding(left_padding)
  @total_left_padding += left_padding
  @x += left_padding
  @width -= left_padding
end

```

    
  

    
      
  
### 
  
    #**add_right_padding**(right_padding)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Increase the right padding of the bounding box.

  

  

Parameters:

  
    
- 
      
        right_padding
      
      
        (Number)
      
      
      
    
  

  
    
      

```

370
371
372
373
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 370

def add_right_padding(right_padding)
  @total_right_padding += right_padding
  @width -= right_padding
end

```

    
  

    
      
  
### 
  
    #**anchor**  ⇒ Array(Number, Number) 
  

  

  

  
    

The translated origin (x, y - height) which describes the location of the bottom left corner of the bounding box.

  

  

Returns:

  
    
- 
      
      
        (Array(Number, Number))
      
      
      
    
  

  
    
      

```

302
303
304
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 302

def anchor
  [@x, @y - height]
end

```

    
  

    
      
  
### 
  
    #**bottom**  ⇒ Number 
  

  

  

  
    

Relative bottom y-coordinate of the bounding box. Always 0.

  

  
  
    
#### Examples:

    
      
        
##### 

Position some text 3 pts from the bottom of the containing box

      
      

```
draw_text('hello', at: [0, (bounds.bottom + 3)])

```

    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

411
412
413
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 411

def bottom
  0
end

```

    
  

    
      
  
### 
  
    #**bottom_left**  ⇒ Array(Number, Number) 
  

  

  

  
    

Relative bottom-left point of the bounding box.

  

  
  
    
#### Examples:

    
      
        
##### 

Draw a line along the left hand side of the page

      
      

```
stroke do
  line(bounds.bottom_left, bounds.top_left)
end

```

    
  

Returns:

  
    
- 
      
      
        (Array(Number, Number))
      
      
      
    
  

  
    
      

```

459
460
461
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 459

def bottom_left
  [left, bottom]
end

```

    
  

    
      
  
### 
  
    #**bottom_right**  ⇒ Array(Number, Number) 
  

  

  

  
    

Relative bottom-right point of the bounding box.

  

  
  
    
#### Examples:

    
      
        
##### 

Draw a line along the right hand side of the page

      
      

```
stroke do
  line(bounds.bottom_right, bounds.top_right)
end

```

    
  

Returns:

  
    
- 
      
      
        (Array(Number, Number))
      
      
      
    
  

  
    
      

```

447
448
449
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 447

def bottom_right
  [right, bottom]
end

```

    
  

    
      
  
### 
  
    #**deep_copy**  ⇒ BoundingBox 
  

  

  

  
    

Returns a deep copy of these bounds (including all parent bounds but not copying the reference to the Document).

  

  

Returns:

  
    
- 
      
      
        (BoundingBox)
      
      
      
    
  

  
    
      

```

598
599
600
601
602
603
604
605
606
607
608
609
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 598

def deep_copy
  copy = dup
  # Deep-copy the parent bounds
  copy.instance_variable_set(
    :@parent,
    if @parent.is_a?(BoundingBox)
      @parent.deep_copy
    end,
  )
  copy.instance_variable_set(:@document, nil)
  copy
end

```

    
  

    
      
  
### 
  
    #**height**  ⇒ Number 
  

  
    Also known as:
    update_height
    
  

  

  
    

Height of the bounding box. If the box is ‘stretchy’ (unspecified height attribute), height is calculated as the distance from the top of the box to the current drawing position.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

529
530
531
532
533
534
535
536
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 529

def height
  return @height if @height

  @stretched_height = [
    (absolute_top - @document.y),
    Float(@stretched_height || 0.0),
  ].max
end

```

    
  

    
      
  
### 
  
    #**indent**(left_padding, right_padding = 0)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Temporarily adjust the x coordinate to allow for left padding

  

  
  
    
#### Examples:

    
      
      

```
indent 20 do
  text "20 points in"
  indent 30 do
    text "50 points in"
  end
end

indent 20, 20 do
  text "indented on both sides"
end

```

    
  

Parameters:

  
    
- 
      
        left_padding
      
      
        (Number)
      
      
      
    
  
    
- 
      
        right_padding
      
      
        (Number)
      
      
        *(defaults to: 0)*
      
      
    
  

  
    
      

```

334
335
336
337
338
339
340
341
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 334

def indent(left_padding, right_padding = 0)
  add_left_padding(left_padding)
  add_right_padding(right_padding)
  yield
ensure
  @document.bounds.subtract_left_padding(left_padding)
  @document.bounds.subtract_right_padding(right_padding)
end

```

    
  

    
      
  
### 
  
    #**left**  ⇒ Number 
  

  

  

  
    

Relative left x-coordinate of the bounding box. Always 0.

  

  
  
    
#### Examples:

    
      
        
##### 

Position some text 3 pts from the left of the containing box

      
      

```
draw_text('hello', at: [(bounds.left + 3), 0])

```

    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

312
313
314
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 312

def left
  0
end

```

    
  

    
      
  
### 
  
    #**left_side**  ⇒ Number 
  

  

  

  
    

An alias for #absolute_left.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

542
543
544
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 542

def left_side
  absolute_left
end

```

    
  

    
      
  
### 
  
    #**move_past_bottom**  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Moves to the top of the next page of the document, starting a new page if necessary.

  

  

  
    
      

```

560
561
562
563
564
565
566
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 560

def move_past_bottom
  if @document.page_number == @document.page_count
    @document.start_new_page
  else
    @document.go_to_page(@document.page_number + 1)
  end
end

```

    
  

    
      
  
### 
  
    #**reference_bounds**  ⇒ BoundingBox 
  

  

  

  
    

Returns the innermost non-stretchy bounding box.

  

  

Returns:

  
    
- 
      
      
        (BoundingBox)
      
      
      
    
  

Raises:

  
    
- 
      
      
        (NoReferenceBounds)
      
      
      
    
  

  
    
      

```

581
582
583
584
585
586
587
588
589
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 581

def reference_bounds
  if stretchy?
    raise NoReferenceBounds unless @parent

    @parent.reference_bounds
  else
    self
  end
end

```

    
  

    
      
  
### 
  
    #**right**  ⇒ Number 
  

  

  

  
    

Relative right x-coordinate of the bounding box. Equal to the box width.

  

  
  
    
#### Examples:

    
      
        
##### 

Position some text 3 pts from the right of the containing box

      
      

```
draw_text('hello', at: [(bounds.right - 3), 0])

```

    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

391
392
393
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 391

def right
  @width
end

```

    
  

    
      
  
### 
  
    #**right_side**  ⇒ Number 
  

  

  

  
    

An alias for #absolute_right.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

550
551
552
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 550

def right_side
  absolute_right
end

```

    
  

    
      
  
### 
  
    #**stretchy?**  ⇒ Boolean 
  

  

  

  
    

Returns `false` when the box has a defined height, `true` when the height is being calculated on the fly based on the current vertical position.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

573
574
575
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 573

def stretchy?
  !@height
end

```

    
  

    
      
  
### 
  
    #**subtract_left_padding**(left_padding)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Decrease the left padding of the bounding box.

  

  

Parameters:

  
    
- 
      
        left_padding
      
      
        (Number)
      
      
      
    
  

  
    
      

```

359
360
361
362
363
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 359

def subtract_left_padding(left_padding)
  @total_left_padding -= left_padding
  @x -= left_padding
  @width += left_padding
end

```

    
  

    
      
  
### 
  
    #**subtract_right_padding**(right_padding)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Decrease the right padding of the bounding box.

  

  

Parameters:

  
    
- 
      
        right_padding
      
      
        (Number)
      
      
      
    
  

  
    
      

```

380
381
382
383
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 380

def subtract_right_padding(right_padding)
  @total_right_padding -= right_padding
  @width += right_padding
end

```

    
  

    
      
  
### 
  
    #**top**  ⇒ Number 
  

  

  

  
    

Relative top y-coordinate of the bounding box. Equal to the box height.

  

  
  
    
#### Examples:

    
      
        
##### 

Position some text 3 pts from the top of the containing box

      
      

```
draw_text('hello', at: [0, (bounds.top - 3)])

```

    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

401
402
403
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 401

def top
  height
end

```

    
  

    
      
  
### 
  
    #**top_left**  ⇒ Array(Number, Number) 
  

  

  

  
    

Relative top-left point of the bounding_box.

  

  
  
    
#### Examples:

    
      
        
##### 

Draw a line from the top left of the box diagonally to the bottom right

      
      

```
stroke do
  line(bounds.top_left, bounds.bottom_right)
end

```

    
  

Returns:

  
    
- 
      
      
        (Array(Number, Number))
      
      
      
    
  

  
    
      

```

423
424
425
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 423

def top_left
  [left, top]
end

```

    
  

    
      
  
### 
  
    #**top_right**  ⇒ Array(Number, Number) 
  

  

  

  
    

Relative top-right point of the bounding box.

  

  
  
    
#### Examples:

    
      
        
##### 

Draw a line from the top_right of the box diagonally to the bottom left

      
      

```
stroke do
  line(bounds.top_right, bounds.bottom_left)
end

```

    
  

Returns:

  
    
- 
      
      
        (Array(Number, Number))
      
      
      
    
  

  
    
      

```

435
436
437
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 435

def top_right
  [right, top]
end

```