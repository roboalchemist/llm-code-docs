# Module: Prawn::Graphics
  
  
  

  

  
  
  
  
  
      Includes:
      BlendMode, CapStyle, Color, Dash, JoinStyle, Patterns, Transformation, Transparency
  
  
  

  
  
    Included in:
    Document
  
  

  
  
    Defined in:
    lib/prawn/graphics.rb,

  lib/prawn/graphics/dash.rb,
 lib/prawn/graphics/color.rb,
 lib/prawn/graphics/patterns.rb,
 lib/prawn/graphics/cap_style.rb,
 lib/prawn/graphics/blend_mode.rb,
 lib/prawn/graphics/join_style.rb,
 lib/prawn/graphics/transparency.rb,
 lib/prawn/graphics/transformation.rb

  
  

## Overview

  
    

Implements the drawing facilities for Document. Use this to draw the most beautiful imaginable things.

  

  

## Defined Under Namespace

  
    
      **Modules:** BlendMode, CapStyle, Color, Dash, JoinStyle, Patterns, Transformation, Transparency
    
  
    
  

  
    
## 
      Stable API
      collapse
    

    
      
        KAPPA =
          
  
    

This constant is used to approximate a symmetrical arc using a cubic Bezier curve.

  

  

        
        

```
4.0 * ((Math.sqrt(2) - 1.0) / 3.0)

```

      
    
  

  
  
  
### Constants included
     from JoinStyle

  

JoinStyle::JOIN_STYLES

  
  
  
### Constants included
     from CapStyle

  

CapStyle::CAP_STYLES

  
    
## 
      Stable API
      collapse
    

    

      
        
- 
  
    
      #**circle**(center, radius)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws a circle of radius `radius` with the centre-point at `point` as a complete subpath.

  

      
        
- 
  
    
      #**close_and_stroke** { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Closes and strokes the current path.

  

      
        
- 
  
    
      #**close_path**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Closes the current path.

  

      
        
- 
  
    
      #**curve**(origin, dest, options = {})  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws a Bezier curve between two points, bounded by two additional points.

  

      
        
- 
  
    
      #**curve_to**(dest, options = {})  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws a Bezier curve from the current drawing position to the specified point, bounded by two additional points.

  

      
        
- 
  
    
      #**ellipse**(point, radius1, radius2 = radius1)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws an ellipse of `x` radius `radius1` and `y` radius `radius2` with the centre-point at `point` as a complete subpath.

  

      
        
- 
  
    
      #**fill**(options = {}) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Closes and fills the current path.

  

      
        
- 
  
    
      #**fill_and_stroke**(options = {}) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Closes, fills, and strokes the current path.

  

      
        
- 
  
    
      #**fill_and_stroke_circle**(center, radius)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws, strokes, and fills a circle of radius `radius` with the centre-point at `point`.

  

      
        
- 
  
    
      #**fill_and_stroke_ellipse**(point, radius1, radius2 = radius1)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws, strokes, and fills an ellipse of x radius `r1` and y radius `r2` with the centre-point at `point`.

  

      
        
- 
  
    
      #**fill_and_stroke_polygon**(*points)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws, strokes, and fills a polygon from the specified points.

  

      
        
- 
  
    
      #**fill_and_stroke_rectangle**(point, width, height)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws, fills, and strokes a rectangle given `point`, `width`, and `height`.

  

      
        
- 
  
    
      #**fill_and_stroke_rounded_rectangle**(point, width, height, radius)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws, fills, and strokes a rounded rectangle given `point`, `width`, and `height` and `radius` for the rounded corner.

  

      
        
- 
  
    
      #**fill_circle**(center, radius)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws and fills a circle of radius `radius` with the centre-point at `point`.

  

      
        
- 
  
    
      #**fill_ellipse**(point, radius1, radius2 = radius1)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws and fills an ellipse of x radius `r1` and y radius `r2` with the centre-point at `point`.

  

      
        
- 
  
    
      #**fill_polygon**(*points)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws and fills a polygon from the specified points.

  

      
        
- 
  
    
      #**fill_rectangle**(point, width, height)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws and fills a rectangle given `point`, `width`, and `height`.

  

      
        
- 
  
    
      #**fill_rounded_polygon**(radius, *points)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws and fills a rounded polygon from specified points, using `radius` to define Bezier curves.

  

      
        
- 
  
    
      #**fill_rounded_rectangle**(point, width, height, radius)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws and fills a rounded rectangle given `point`, `width` and `height`, and `radius` for the rounded corner.

  

      
        
- 
  
    
      #**horizontal_line**(x1, x2, options = {})  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws a horizontal line from `x1` to `x2` at the current Document#y position, or the position specified by the `:at` option.

  

      
        
- 
  
    
      #**horizontal_rule**  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws a horizontal line from the left border to the right border of the bounding box at the current Document#y position.

  

      
        
- 
  
    
      #**line**(*points)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Draws a line from one point to another.

  

      
        
- 
  
    
      #**line_to**(*point)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Draws a line from the current drawing position to the specified point.

  

      
        
- 
  
    
      #**line_width**(width = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

When called without an argument, returns the current line thickness.

  

      
        
- 
  
    
      #**line_width=**(width)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Sets line thickness to the `width` specified.

  

      
        
- 
  
    
      #**move_to**(*point)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Moves the drawing position to a given point.

  

      
        
- 
  
    
      #**polygon**(*points)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws a polygon from the specified points.

  

      
        
- 
  
    
      #**rectangle**(point, width, height)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws a rectangle given `point`, ‘width and `height`.

  

      
        
- 
  
    
      #**rounded_polygon**(radius, *points)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws a rounded polygon from specified points using the radius to define bezier curves.

  

      
        
- 
  
    
      #**rounded_rectangle**(point, width, height, radius)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws a rounded rectangle given `point`, `width`, `height`, and `radius` for the rounded corner.

  

      
        
- 
  
    
      #**rounded_vertex**(radius, *points)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Creates a rounded vertex for a line segment used for building a rounded polygon requires a radius to define bezier curve and three points.

  

      
        
- 
  
    
      #**stroke** { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Strokes the current path.

  

      
        
- 
  
    
      #**stroke_axis**(options = {})  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws and strokes X and Y axes rulers beginning at the current bounding box origin (or at a custom location).

  

      
        
- 
  
    
      #**stroke_bounds**  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws and strokes a rectangle represented by the current bounding box.

  

      
        
- 
  
    
      #**stroke_curve**(origin, dest, options = {})  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Strokes a Bezier curve between two points, bounded by two additional points.

  

      
        
- 
  
    
      #**stroke_ellipse**(point, radius1, radius2 = radius1)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws and strokes an ellipse of x radius `r1` and y radius `r2` with the centre-point at `point`.

  

      
        
- 
  
    
      #**stroke_horizontal_line**(x1, x2, options = {})  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Strokes a horizontal line from `x1` to `x2` at the current y position, or the position specified by the :at option.

  

      
        
- 
  
    
      #**stroke_horizontal_rule**  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Strokes a horizontal line from the left border to the right border of the bounding box at the current y position.

  

      
        
- 
  
    
      #**stroke_line**(*points)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Strokes a line from one point to another.

  

      
        
- 
  
    
      #**stroke_polygon**(*points)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Draws and strokes a polygon from the specified points.

  

      
        
- 
  
    
      #**stroke_rectangle**(point, width, height)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws and strokes a rectangle given `point`, `width`, and `height`.

  

      
        
- 
  
    
      #**stroke_rounded_polygon**(radius, *points)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws and strokes a rounded polygon from specified points, using `radius` to define Bezier curves.

  

      
        
- 
  
    
      #**stroke_rounded_rectangle**(point, width, height, radius)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws and strokes a rounded rectangle given `point`, `width` and `height`, and `radius` for the rounded corner.

  

      
        
- 
  
    
      #**stroke_vertical_line**(y1, y2, params)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Strokes a vertical line at the x coordinate given by `:at` from `y1` to `y2`.

  

      
        
- 
  
    
      #**vertical_line**(y1, y2, params)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws a vertical line at the x coordinate given by `:at` from `y1` to `y2`.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Patterns

  

#fill_gradient, #stroke_gradient

  
  
  
  
  
  
  
  
  
### Methods included from Transformation

  

#rotate, #scale, #transformation_matrix, #translate

  
  
  
  
  
  
  
  
  
### Methods included from Transparency

  

#transparent

  
  
  
  
  
  
  
  
  
### Methods included from JoinStyle

  

#join_style

  
  
  
  
  
  
  
  
  
### Methods included from CapStyle

  

#cap_style

  
  
  
  
  
  
  
  
  
### Methods included from Dash

  

#dash, #dashed?, #undash

  
  
  
  
  
  
  
  
  
### Methods included from Color

  

#fill_color, hex2rgb, rgb2hex, #stroke_color

  
  
  
  
  
  
  
  
  
### Methods included from BlendMode

  

#blend_mode

  
    
## Instance Method Details

    
      
  
### 
  
    #**circle**(center, radius)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws a circle of radius `radius` with the centre-point at `point` as a complete subpath. The drawing point will be moved to the centre-point upon completion of the drawing the circle.

  

  
  
    
#### Examples:

    
      
      

```
pdf.circle [100, 100], 25

```

    
  

Parameters:

  
    
- 
      
        center
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        radius
      
      
        (Number)
      
      
      
    
  

  
    
      

```

261
262
263
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 261

def circle(center, radius)
  ellipse(center, radius, radius)
end

```

    
  

    
      
  
### 
  
    #**close_and_stroke** { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Closes and strokes the current path. If a block is provided, yields to the block before closing the path. See Color for color details.

  

  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

  
    
      

```

389
390
391
392
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 389

def close_and_stroke
  yield if block_given?
  renderer.add_content('s')
end

```

    
  

    
      
  
### 
  
    #**close_path**  ⇒ Object 
  

  

  

  
    

Closes the current path.

  

  

  
    
      

```

510
511
512
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 510

def close_path
  renderer.add_content('h')
end

```

    
  

    
      
  
### 
  
    #**curve**(origin, dest, options = {})  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws a Bezier curve between two points, bounded by two additional points

  

  
  
    
#### Examples:

    
      
      

```
pdf.curve [50, 100], [100, 100], bounds: [[90, 90], [75, 75]]

```

    
  

Parameters:

  
    
- 
      
        origin
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        dest
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :bounds
          (Array(Array(Number, Number), Array(Number, Number)))
          
            
          
          
        
      
    

  

  
    
      

```

242
243
244
245
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 242

def curve(origin, dest, options = {})
  move_to(*origin)
  curve_to(dest, options)
end

```

    
  

    
      
  
### 
  
    #**curve_to**(dest, options = {})  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws a Bezier curve from the current drawing position to the specified point, bounded by two additional points.

  

  
  
    
#### Examples:

    
      
      

```
pdf.curve_to [100, 100], bounds: [[90, 90], [75, 75]]

```

    
  

Parameters:

  
    
- 
      
        dest
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :bounds
          (Array(Array(Number, Number), Array(Number, Number)))
          
            
          
          
        
      
    

  

  
    
      

```

85
86
87
88
89
90
91
92
93
94
95
96
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 85

def curve_to(dest, options = {})
  options[:bounds] || raise(
    Prawn::Errors::InvalidGraphicsPath,
    'Bounding points for bezier curve must be specified as :bounds => [[x1,y1],[x2,y2]]',
  )

  curve_points = PDF::Core.real_params(
    (options[:bounds] << dest).flat_map { |e| map_to_absolute(e) },
  )

  renderer.add_content("#{curve_points} c")
end

```

    
  

    
      
  
### 
  
    #**ellipse**(point, radius1, radius2 = radius1)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws an ellipse of `x` radius `radius1` and `y` radius `radius2` with the centre-point at `point` as a complete subpath. The drawing point will be moved to the centre-point upon completion of the drawing the ellipse.

  

  
  
    
#### Examples:

    
      
        
##### 

Draws an ellipse with x-radius 25 and y-radius 50

      
      

```
pdf.ellipse [100, 100], 25, 50

```

    
  

Parameters:

  
    
- 
      
        point
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        radius1
      
      
        (Number)
      
      
      
    
  
    
- 
      
        radius2
      
      
        (Number)
      
      
        *(defaults to: radius1)*
      
      
    
  

  
    
      

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
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 276

def ellipse(point, radius1, radius2 = radius1)
  x, y = point
  l1 = radius1 * KAPPA
  l2 = radius2 * KAPPA

  move_to(x + radius1, y)

  # Upper right hand corner
  curve_to(
    [x, y + radius2],
    bounds: [[x + radius1, y + l2], [x + l1, y + radius2]],
  )

  # Upper left hand corner
  curve_to(
    [x - radius1, y],
    bounds: [[x - l1, y + radius2], [x - radius1, y + l2]],
  )

  # Lower left hand corner
  curve_to(
    [x, y - radius2],
    bounds: [[x - radius1, y - l2], [x - l1, y - radius2]],
  )

  # Lower right hand corner
  curve_to(
    [x + radius1, y],
    bounds: [[x + l1, y - radius2], [x + radius1, y - l2]],
  )

  move_to(x, y)
end

```

    
  

    
      
  
### 
  
    #**fill**(options = {}) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Closes and fills the current path. See Color for color details.

If the option ‘fill_rule: :even_odd` is specified, Prawn will use the even-odd rule to fill the path. Otherwise, the nonzero winding number rule will be used. See the PDF reference, “Graphics -> Path Construction and Painting -> Clipping Path Operators” for details on the difference.

  

  

Parameters:

  
    
- 
      
        options
      
      
        (Hash)
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    

Options Hash (options):
    

      
        
- 
          :fill_rule
          (Symbol)
          
            
          
          
        
      
    

  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

  
    
      

```

485
486
487
488
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 485

def fill(options = {})
  yield if block_given?
  renderer.add_content(options[:fill_rule] == :even_odd ? 'f*' : 'f')
end

```

    
  

    
      
  
### 
  
    #**fill_and_stroke**(options = {}) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Closes, fills, and strokes the current path. If a block is provided, yields to the block before closing the path. See Color for color details.

If the option ‘fill_rule: :even_odd` is specified, Prawn will use the even-odd rule to fill the path. Otherwise, the nonzero winding number rule will be used. See the PDF reference, “Graphics -> Path Construction and Painting -> Clipping Path Operators” for details on the difference.

  

  

Parameters:

  
    
- 
      
        options
      
      
        (Hash)
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    

Options Hash (options):
    

      
        
- 
          :fill_rule
          (Symbol)
          
            
          
          
        
      
    

  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

  
    
      

```

503
504
505
506
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 503

def fill_and_stroke(options = {})
  yield if block_given?
  renderer.add_content(options[:fill_rule] == :even_odd ? 'b*' : 'b')
end

```

    
  

    
      
  
### 
  
    #**fill_and_stroke_circle**(center, radius)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws, strokes, and fills a circle of radius `radius` with the centre-point at `point`.

  

  

Parameters:

  
    
- 
      
        center
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        radius
      
      
        (Number)
      
      
      
    
  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 650

```

    
  

    
      
  
### 
  
    #**fill_and_stroke_ellipse**(point, radius1, radius2 = radius1)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws, strokes, and fills an ellipse of x radius `r1` and y radius `r2` with the centre-point at `point`.

  

  

Parameters:

  
    
- 
      
        point
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        radius1
      
      
        (Number)
      
      
      
    
  
    
- 
      
        radius2
      
      
        (Number)
      
      
        *(defaults to: radius1)*
      
      
    
  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 679

```

    
  

    
      
  
### 
  
    #**fill_and_stroke_polygon**(*points)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws, strokes, and fills a polygon from the specified points.

  

  

Parameters:

  
    
- 
      
        points
      
      
        (Array<Array(Number, Number)>)
      
      
      
    
  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 703

```

    
  

    
      
  
### 
  
    #**fill_and_stroke_rectangle**(point, width, height)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws, fills, and strokes a rectangle given `point`, `width`, and `height`. The rectangle is bounded by its upper-left corner.

  

  

Parameters:

  
    
- 
      
        point
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        width
      
      
        (Number)
      
      
      
    
  
    
- 
      
        height
      
      
        (Number)
      
      
      
    
  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 532

```

    
  

    
      
  
### 
  
    #**fill_and_stroke_rounded_rectangle**(point, width, height, radius)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws, fills, and strokes a rounded rectangle given `point`, `width`, and `height` and `radius` for the rounded corner. The rectangle is bounded by its upper-left corner.

  

  

Parameters:

  
    
- 
      
        point
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        width
      
      
        (Number)
      
      
      
    
  
    
- 
      
        height
      
      
        (Number)
      
      
      
    
  
    
- 
      
        radius
      
      
        (Number)
      
      
      
    
  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 564

```

    
  

    
      
  
### 
  
    #**fill_circle**(center, radius)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws and fills a circle of radius `radius` with the centre-point at `point`.

  

  

Parameters:

  
    
- 
      
        center
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        radius
      
      
        (Number)
      
      
      
    
  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 641

```

    
  

    
      
  
### 
  
    #**fill_ellipse**(point, radius1, radius2 = radius1)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws and fills an ellipse of x radius `r1` and y radius `r2` with the centre-point at `point`.

  

  

Parameters:

  
    
- 
      
        point
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        radius1
      
      
        (Number)
      
      
      
    
  
    
- 
      
        radius2
      
      
        (Number)
      
      
        *(defaults to: radius1)*
      
      
    
  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 669

```

    
  

    
      
  
### 
  
    #**fill_polygon**(*points)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws and fills a polygon from the specified points.

  

  

Parameters:

  
    
- 
      
        points
      
      
        (Array<Array(Number, Number)>)
      
      
      
    
  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 696

```

    
  

    
      
  
### 
  
    #**fill_rectangle**(point, width, height)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws and fills a rectangle given `point`, `width`, and `height`. The rectangle is bounded by its upper-left corner.

  

  

Parameters:

  
    
- 
      
        point
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        width
      
      
        (Number)
      
      
      
    
  
    
- 
      
        height
      
      
        (Number)
      
      
      
    
  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 514

```

    
  

    
      
  
### 
  
    #**fill_rounded_polygon**(radius, *points)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws and fills a rounded polygon from specified points, using `radius` to define Bezier curves.

  

  

Parameters:

  
    
- 
      
        radius
      
      
        (Number)
      
      
      
    
  
    
- 
      
        points
      
      
        (Array<Array(Number, Number)>)
      
      
      
    
  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 719

```

    
  

    
      
  
### 
  
    #**fill_rounded_rectangle**(point, width, height, radius)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws and fills a rounded rectangle given `point`, `width` and `height`, and `radius` for the rounded corner. The rectangle is bounded by its upper-left corner.

  

  

Parameters:

  
    
- 
      
        point
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        width
      
      
        (Number)
      
      
      
    
  
    
- 
      
        height
      
      
        (Number)
      
      
      
    
  
    
- 
      
        radius
      
      
        (Number)
      
      
      
    
  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 541

```

    
  

    
      
  
### 
  
    #**horizontal_line**(x1, x2, options = {})  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws a horizontal line from `x1` to `x2` at the current Document#y position, or the position specified by the `:at` option.

  

  
  
    
#### Examples:

    
      
        
##### 

Draw a line from ‘[25, 75]` to `[100, 75]`

      
      

```
horizontal_line 25, 100, at: 75

```

    
  

Parameters:

  
    
- 
      
        x1
      
      
        (Number)
      
      
      
    
  
    
- 
      
        x2
      
      
        (Number)
      
      
      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :at
          (Number)
          
            
          
          
        
      
    

  

  
    
      

```

202
203
204
205
206
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 202

def horizontal_line(x1, x2, options = {})
  y1 = options[:at] || (y - bounds.absolute_bottom)

  line(x1, y1, x2, y1)
end

```

    
  

    
      
  
### 
  
    #**horizontal_rule**  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws a horizontal line from the left border to the right border of the bounding box at the current Document#y position.

  

  

  
    
      

```

212
213
214
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 212

def horizontal_rule
  horizontal_line(bounds.left, bounds.right)
end

```

    
  

    
      
  
### 
  
    
      #**line**(point1, point2)  ⇒ void 
    
      #**line**(x1, y1, x2, y2)  ⇒ void 
    
  

  

  

  
    

Draws a line from one point to another. Points may be specified as tuples or flattened argument list.

  

  
  
    
#### Examples:

    
      
      

```
pdf.line [100, 100], [200, 250]
pdf.line(100, 100, 200, 250)

```

    
  

  

Overloads:
  

    
      
      
- 
        #**line**(point1, point2)  ⇒ void 
        
  
    

This method returns an undefined value.

  

  

Parameters:

  
    
  - 
      
        point1
      
      
        (Array(Number, Number))
      
      
      
    
  
    
  - 
      
        point2
      
      
        (Array(Number, Number))
      
      
      
    
  

      
    
      
      
- 
        #**line**(x1, y1, x2, y2)  ⇒ void 
        
  
    

This method returns an undefined value.

  

  

Parameters:

  
    
  - 
      
        x1
      
      
        (Number)
      
      
      
    
  
    
  - 
      
        y1
      
      
        (Number)
      
      
      
    
  
    
  - 
      
        x2
      
      
        (Number)
      
      
      
    
  
    
  - 
      
        y2
      
      
        (Number)
      
      
      
    
  

      
    
  

  
    
      

```

185
186
187
188
189
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 185

def line(*points)
  x0, y0, x1, y1 = points.flatten
  move_to(x0, y0)
  line_to(x1, y1)
end

```

    
  

    
      
  
### 
  
    
      #**line_to**(point)  ⇒ void 
    
      #**line_to**(x, y)  ⇒ void 
    
  

  

  

  
    

Draws a line from the current drawing position to the specified point. The destination may be described as a tuple or a flattened list:

  

  
  
    
#### Examples:

    
      
      

```
pdf.line_to [50, 50]
pdf.line_to(50, 50)

```

    
  

  

Overloads:
  

    
      
      
- 
        #**line_to**(point)  ⇒ void 
        
  
    

This method returns an undefined value.

  

  

Parameters:

  
    
  - 
      
        point
      
      
        (Array(Number, Number))
      
      
      
    
  

      
    
      
      
- 
        #**line_to**(x, y)  ⇒ void 
        
  
    

This method returns an undefined value.

  

  

Parameters:

  
    
  - 
      
        x
      
      
        (Number)
      
      
      
    
  
    
  - 
      
        y
      
      
        (Number)
      
      
      
    
  

      
    
  

  
    
      

```

70
71
72
73
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 70

def line_to(*point)
  xy = PDF::Core.real_params(map_to_absolute(point))
  renderer.add_content("#{xy} l")
end

```

    
  

    
      
  
### 
  
    
      #**line_width**  ⇒ Number 
    
      #**line_width**(width)  ⇒ void 
    
  

  

  

  
    

When called without an argument, returns the current line thickness. When called with an argument, sets the line thickness to the specified value (in PDF points).

  

  
  
    
#### Examples:

    
      
      

```
pdf.line_width #=> 1
pdf.line_width(5)
pdf.line_width #=> 5

```

    
  

  

Overloads:
  

    
      
      
- 
        #**line_width**  ⇒ Number 
        
  
    

  

  

Returns:

  
    
  - 
      
      
        (Number)
      
      
      
    
  

      
    
      
      
- 
        #**line_width**(width)  ⇒ void 
        
  
    

This method returns an undefined value.

  

  

Parameters:

  
    
  - 
      
        width
      
      
        (Number)
      
      
      
    
  

      
    
  

  
    
      

```

160
161
162
163
164
165
166
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 160

def line_width(width = nil)
  if width
    self.line_width = width
  else
    current_line_width
  end
end

```

    
  

    
      
  
### 
  
    #**line_width=**(width)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Sets line thickness to the `width` specified.

  

  

Parameters:

  
    
- 
      
        width
      
      
        (Number)
      
      
      
    
  

  
    
      

```

141
142
143
144
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 141

def line_width=(width)
  self.current_line_width = width
  write_line_width
end

```

    
  

    
      
  
### 
  
    
      #**move_to**(point)  ⇒ void 
    
      #**move_to**(x, y)  ⇒ void 
    
  

  

  

  
    

Moves the drawing position to a given point. The point can be specified as a tuple or a flattened argument list.

  

  
  
    
#### Examples:

    
      
      

```
pdf.move_to [100, 50]
pdf.move_to(100, 50)

```

    
  

  

Overloads:
  

    
      
      
- 
        #**move_to**(point)  ⇒ void 
        
  
    

This method returns an undefined value.

  

  

Parameters:

  
    
  - 
      
        point
      
      
        (Array(Number, Number))
      
      
      
    
  

      
    
      
      
- 
        #**move_to**(x, y)  ⇒ void 
        
  
    

This method returns an undefined value.

  

  

Parameters:

  
    
  - 
      
        x
      
      
        (Number)
      
      
      
    
  
    
  - 
      
        y
      
      
        (Number)
      
      
      
    
  

      
    
  

  
    
      

```

51
52
53
54
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 51

def move_to(*point)
  xy = PDF::Core.real_params(map_to_absolute(point))
  renderer.add_content("#{xy} m")
end

```

    
  

    
      
  
### 
  
    #**polygon**(*points)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws a polygon from the specified points.

  

  
  
    
#### Examples:

    
      
        
##### 

Draws a snazzy triangle

      
      

```
pdf.polygon [100,100], [100,200], [200,200]

```

    
  

Parameters:

  
    
- 
      
        points
      
      
        (Array<Array(Number, Number)>)
      
      
      
    
  

  
    
      

```

317
318
319
320
321
322
323
324
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 317

def polygon(*points)
  move_to(points[0])
  (points[1..] << points[0]).each do |point|
    line_to(*point)
  end
  # close the path
  renderer.add_content('h')
end

```

    
  

    
      
  
### 
  
    #**rectangle**(point, width, height)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws a rectangle given `point`, ‘width and `height`. The rectangle is bounded by its upper-left corner.

  

  
  
    
#### Examples:

    
      
      

```
pdf.rectangle [300, 300], 100, 200

```

    
  

Parameters:

  
    
- 
      
        point
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        width
      
      
        (Number)
      
      
      
    
  
    
- 
      
        height
      
      
        (Number)
      
      
      
    
  

  
    
      

```

108
109
110
111
112
113
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 108

def rectangle(point, width, height)
  x, y = map_to_absolute(point)
  box = PDF::Core.real_params([x, y - height, width, height])

  renderer.add_content("#{box} re")
end

```

    
  

    
      
  
### 
  
    #**rounded_polygon**(radius, *points)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws a rounded polygon from specified points using the radius to define bezier curves.

  

  
  
    
#### Examples:

    
      
        
##### 

Draws a rounded filled in polygon

      
      

```
pdf.fill_and_stroke_rounded_polygon(
  10, [100, 250], [200, 300], [300, 250], [300, 150], [200, 100],
  [100, 150]
)

```

    
  

Parameters:

  
    
- 
      
        radius
      
      
        (Number)
      
      
      
    
  
    
- 
      
        points
      
      
        (Array<Array(Number, Number)>)
      
      
      
    
  

  
    
      

```

338
339
340
341
342
343
344
345
346
347
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 338

def rounded_polygon(radius, *points)
  move_to(point_on_line(radius, points[1], points[0]))
  sides = points.size
  points << points[0] << points[1]
  sides.times do |i|
    rounded_vertex(radius, points[i], points[i + 1], points[i + 2])
  end
  # close the path
  renderer.add_content('h')
end

```

    
  

    
      
  
### 
  
    #**rounded_rectangle**(point, width, height, radius)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws a rounded rectangle given `point`, `width`, `height`, and `radius` for the rounded corner. The rectangle is bounded by its upper-left corner.

  

  
  
    
#### Examples:

    
      
      

```
pdf.rounded_rectangle [300, 300], 100, 200, 10

```

    
  

Parameters:

  
    
- 
      
        point
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        width
      
      
        (Number)
      
      
      
    
  
    
- 
      
        height
      
      
        (Number)
      
      
      
    
  
    
- 
      
        radius
      
      
        (Number)
      
      
      
    
  

  
    
      

```

126
127
128
129
130
131
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 126

def rounded_rectangle(point, width, height, radius)
  x, y = point
  rounded_polygon(
    radius, point, [x + width, y], [x + width, y - height], [x, y - height],
  )
end

```

    
  

    
      
  
### 
  
    #**rounded_vertex**(radius, *points)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Creates a rounded vertex for a line segment used for building a rounded polygon requires a radius to define bezier curve and three points. The first two points define the line segment and the third point helps define the curve for the vertex.

  

  

Parameters:

  
    
- 
      
        radius
      
      
        (Number)
      
      
      
    
  
    
- 
      
        points
      
      
        (Array(Array(Number, Number), Array(Number, Number), Array(Number, Number)))
      
      
      
    
  

  
    
      

```

357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 357

def rounded_vertex(radius, *points)
  radial_point1 = point_on_line(radius, points[0], points[1])
  bezier_point1 = point_on_line(
    (radius - (radius * KAPPA)),
    points[0],
    points[1],
  )
  radial_point2 = point_on_line(radius, points[2], points[1])
  bezier_point2 = point_on_line(
    (radius - (radius * KAPPA)),
    points[2],
    points[1],
  )
  line_to(radial_point1)
  curve_to(radial_point2, bounds: [bezier_point1, bezier_point2])
end

```

    
  

    
      
  
### 
  
    #**stroke** { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Strokes the current path. If a block is provided, yields to the block before closing the path. See Color for color details.

  

  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

  
    
      

```

379
380
381
382
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 379

def stroke
  yield if block_given?
  renderer.add_content('S')
end

```

    
  

    
      
  
### 
  
    #**stroke_axis**(options = {})  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws and strokes X and Y axes rulers beginning at the current bounding box origin (or at a custom location).

  

  

Parameters:

  
    
- 
      
        options
      
      
        (Hash)
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    

Options Hash (options):
    

      
        
- 
          :at
          (Array(Number, Number))
          
            
              — default:
              [0, 0], origin of the bounding box
            
          
          
            — 

Origin of the X and Y axes.

          
        
      
        
- 
          :width
          (Number)
          
            
              — default:
              width of the bounding box
            
          
          
            — 

Length of the X axis.

          
        
      
        
- 
          :height
          (Number)
          
            
              — default:
              height of the bounding box
            
          
          
            — 

Length of the Y axis.

          
        
      
        
- 
          :step_length
          (Number)
          
            
              — default:
              100
            
          
          
            — 

Length of the step between markers.

          
        
      
        
- 
          :negative_axes_length
          (Number)
          
            
              — default:
              20
            
          
          
            — 

Length of the negative parts of the axes.

          
        
      
        
- 
          :color
          (String, Array<Number>)
          
            
          
          
            — 

The color of the axes and the text.

          
        
      
    

  

  
    
      

```

418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 418

def stroke_axis(options = {})
  options = {
    at: [0, 0],
    height: bounds.height - (options[:at] || [0, 0])[1],
    width: bounds.width - (options[:at] || [0, 0])[0],
    step_length: 100,
    negative_axes_length: 20,
    color: '000000',
  }.merge(options)

  Prawn.verify_options(
    i[at width height step_length negative_axes_length color],
    options,
  )

  save_graphics_state do
    fill_color(options[:color])
    stroke_color(options[:color])

    dash(1, space: 4)
    stroke_horizontal_line(
      options[:at][0] - options[:negative_axes_length],
      options[:at][0] + options[:width],
      at: options[:at][1],
    )
    stroke_vertical_line(
      options[:at][1] - options[:negative_axes_length],
      options[:at][1] + options[:height],
      at: options[:at][0],
    )
    undash

    fill_circle(options[:at], 1)

    (options[:step_length]..options[:width])
      .step(options[:step_length]) do |point|
      fill_circle([options[:at][0] + point, options[:at][1]], 1)
      draw_text(
        point,
        at: [options[:at][0] + point - 5, options[:at][1] - 10],
        size: 7,
      )
    end

    (options[:step_length]..options[:height])
      .step(options[:step_length]) do |point|
      fill_circle([options[:at][0], options[:at][1] + point], 1)
      draw_text(
        point,
        at: [options[:at][0] - 17, options[:at][1] + point - 2],
        size: 7,
      )
    end
  end
end

```

    
  

    
      
  
### 
  
    #**stroke_bounds**  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws and strokes a rectangle represented by the current bounding box.

  

  

  
    
      

```

397
398
399
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 397

def stroke_bounds
  stroke_rectangle(bounds.top_left, bounds.width, bounds.height)
end

```

    
  

    
      
  
### 
  
    #**stroke_curve**(origin, dest, options = {})  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Strokes a Bezier curve between two points, bounded by two additional points.

  

  

Parameters:

  
    
- 
      
        origin
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        dest
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :bounds
          (Array(Array(Number, Number), Array(Number, Number)))
          
            
          
          
        
      
    

  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 621

```

    
  

    
      
  
### 
  
    #**stroke_ellipse**(point, radius1, radius2 = radius1)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws and strokes an ellipse of x radius `r1` and y radius `r2` with the centre-point at `point`.

  

  

Parameters:

  
    
- 
      
        point
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        radius1
      
      
        (Number)
      
      
      
    
  
    
- 
      
        radius2
      
      
        (Number)
      
      
        *(defaults to: radius1)*
      
      
    
  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 659

```

    
  

    
      
  
### 
  
    #**stroke_horizontal_line**(x1, x2, options = {})  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Strokes a horizontal line from `x1` to `x2` at the current y position, or the position specified by the :at option.

  

  

Parameters:

  
    
- 
      
        x1
      
      
        (Number)
      
      
      
    
  
    
- 
      
        x2
      
      
        (Number)
      
      
      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :at
          (Number)
          
            
          
          
        
      
    

  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 592

```

    
  

    
      
  
### 
  
    #**stroke_horizontal_rule**  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Strokes a horizontal line from the left border to the right border of the bounding box at the current y position.

  

  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 603

```

    
  

    
      
  
### 
  
    
      #**line**(point1, point2)  ⇒ void 
    
      #**line**(x1, y1, x2, y2)  ⇒ void 
    
  

  

  

  
    

Strokes a line from one point to another. Points may be specified as tuples or flattened argument list.

  

  
  

Overloads:
  

    
      
      
- 
        #**line**(point1, point2)  ⇒ void 
        
  
    

This method returns an undefined value.

  

  

Parameters:

  
    
  - 
      
        point1
      
      
        (Array(Number, Number))
      
      
      
    
  
    
  - 
      
        point2
      
      
        (Array(Number, Number))
      
      
      
    
  

      
    
      
      
- 
        #**line**(x1, y1, x2, y2)  ⇒ void 
        
  
    

This method returns an undefined value.

  

  

Parameters:

  
    
  - 
      
        x1
      
      
        (Number)
      
      
      
    
  
    
  - 
      
        y1
      
      
        (Number)
      
      
      
    
  
    
  - 
      
        x2
      
      
        (Number)
      
      
      
    
  
    
  - 
      
        y2
      
      
        (Number)
      
      
      
    
  

      
    
  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 576

```

    
  

    
      
  
### 
  
    #**stroke_polygon**(*points)  ⇒ Object 
  

  

  

  
    

Draws and strokes a polygon from the specified points.

```
@param points [Array<Array(Number, Number)>]
@return [void]

```

  

  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 689

```

    
  

    
      
  
### 
  
    #**stroke_rectangle**(point, width, height)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws and strokes a rectangle given `point`, `width`, and `height`. The rectangle is bounded by its upper-left corner.

  

  

Parameters:

  
    
- 
      
        point
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        width
      
      
        (Number)
      
      
      
    
  
    
- 
      
        height
      
      
        (Number)
      
      
      
    
  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 523

```

    
  

    
      
  
### 
  
    #**stroke_rounded_polygon**(radius, *points)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws and strokes a rounded polygon from specified points, using `radius` to define Bezier curves.

  

  

Parameters:

  
    
- 
      
        radius
      
      
        (Number)
      
      
      
    
  
    
- 
      
        points
      
      
        (Array<Array(Number, Number)>)
      
      
      
    
  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 710

```

    
  

    
      
  
### 
  
    #**stroke_rounded_rectangle**(point, width, height, radius)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws and strokes a rounded rectangle given `point`, `width` and `height`, and `radius` for the rounded corner. The rectangle is bounded by its upper-left corner.

  

  

Parameters:

  
    
- 
      
        point
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        width
      
      
        (Number)
      
      
      
    
  
    
- 
      
        height
      
      
        (Number)
      
      
      
    
  
    
- 
      
        radius
      
      
        (Number)
      
      
      
    
  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 553

```

    
  

    
      
  
### 
  
    #**stroke_vertical_line**(y1, y2, params)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Strokes a vertical line at the x coordinate given by `:at` from `y1` to `y2`.

  

  

Parameters:

  
    
- 
      
        y1
      
      
        (Number)
      
      
      
    
  
    
- 
      
        y2
      
      
        (Number)
      
      
      
    
  
    
- 
      
        params
      
      
        (Hash)
      
      
      
    
  

  
    
    
    
    
    
    
    

Options Hash (params):
    

      
        
- 
          :at
          (Number)
          
            
          
          
        
      
    

  

  
    
      

```

```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 610

```

    
  

    
      
  
### 
  
    #**vertical_line**(y1, y2, params)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws a vertical line at the x coordinate given by `:at` from `y1` to `y2`.

  

  
  
    
#### Examples:

    
      
        
##### 

Draw a line from ‘[25, 100]` to `[25, 300]`

      
      

```
vertical_line 100, 300, at: 25

```

    
  

Parameters:

  
    
- 
      
        y1
      
      
        (Number)
      
      
      
    
  
    
- 
      
        y2
      
      
        (Number)
      
      
      
    
  
    
- 
      
        params
      
      
        (Hash)
      
      
      
    
  

  
    
    
    
    
    
    
    

Options Hash (params):
    

      
        
- 
          :at
          (Number)
          
            
          
          
        
      
    

  

  
    
      

```

227
228
229
```

    
    
      

```
# File 'lib/prawn/graphics.rb', line 227

def vertical_line(y1, y2, params)
  line(params[:at], y1, params[:at], y2)
end

```