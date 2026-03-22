# Class: Prawn::Document
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Prawn::Document
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      PDF::Core::Annotations, PDF::Core::Destinations, Internals, Security, Graphics, Images, SoftMask, Stamp, Text, TransformationStack
  
  
  

  

  
  
    Defined in:
    lib/prawn/font.rb,

  lib/prawn/grid.rb,
 lib/prawn/outline.rb,
 lib/prawn/document.rb,
 lib/prawn/repeater.rb,
 lib/prawn/security.rb,
 lib/prawn/document/span.rb,
 lib/prawn/document/internals.rb,
 lib/prawn/document/column_box.rb,
 lib/prawn/document/bounding_box.rb

  
  

## Overview

  
    

rubocop: disable Style/Documentation

  

  

## Defined Under Namespace

  
    
      **Modules:** Internals, Security
    
  
    
      **Classes:** BoundingBox, ColumnBox, Grid, GridBox, MultiBox
    
  

  
    
## 
      Stable API
      collapse
    

    
      
        DEFAULT_OPTS =
          
  
    

Default empty options.

  

  

        
        

```
{}.freeze
```

      
    
  
    
## 
      Extension API
      collapse
    

    
      
        VALID_OPTIONS =
          
  
    

List of recognised options.

  

  

        
        

```
%i[
  page_size page_layout margin left_margin
  right_margin top_margin bottom_margin skip_page_creation
  compress background info
  text_formatter print_scaling
].freeze
```

      
    
  

  
  
  
### Constants included
     from Graphics

  

Graphics::KAPPA

  
  
  
### Constants included
     from Graphics::JoinStyle

  

Graphics::JoinStyle::JOIN_STYLES

  
  
  
### Constants included
     from Graphics::CapStyle

  

Graphics::CapStyle::CAP_STYLES

  
  
  
### Constants included
     from Text

  

Text::NBSP, Text::SHY, Text::ZWSP

  
## Extension API collapse

  

    
      
- 
  
    
      #**state**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
  

  
## Stable Attributes collapse

  

    
      
- 
  
    
      #**margin_box**  ⇒ Prawn::Document::BoundingBox 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Current margin box.

  

    
      
- 
  
    
      #**margins**  ⇒ {:left, :top, :right, :bottom => Number} 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Current page margins.

  

    
      
- 
  
    
      #**page_number**  ⇒ Integer 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Current page number.

  

    
      
- 
  
    
      #**y**  ⇒ Number 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Absolute cursor position.

  

    
  

  
## Extension Attributes collapse

  

    
      
- 
  
    
      #**text_formatter**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Current text formatter.

  

    
  

  
    
## 
      Stable API
      collapse
    

    

      
        
- 
  
    
      .**generate**(filename, options = {}, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Creates and renders a PDF document.

  

      
        
- 
  
    
      #**bounding_box**(point, options = {}) {|parent_box| ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

A bounding box serves two important purposes: * Provide bounds for flowing text, starting at a given point * Translate the origin (0, 0) for graphics primitives.

  

      
        
- 
  
    
      #**bounds**  ⇒ Prawn::Document::BoundingBox 
    

    
  
  
  
  
  
  
  
  

  
    

The bounds method returns the current bounding box you are currently in, which is by default the box represented by the margin box on the document itself.

  

      
        
- 
  
    
      #**bounds=**(bounding_box)  ⇒ bounding_box 
    

    
  
  
  
  
  
  
  
  

  
    

Sets #bounds to the BoundingBox provided.

  

      
        
- 
  
    
      #**canvas**(&block)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

A shortcut to produce a bounding box which is mapped to the document’s absolute coordinates, regardless of how things are nested or margin sizes.

  

      
        
- 
  
    
      #**cursor**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

The current y drawing position relative to the innermost bounding box, or to the page margins at the top level.

  

      
        
- 
  
    
      #**delete_page**(index)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Remove page of the document by index.

  

      
        
- 
  
    
      #**float**  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Executes a block and then restores the original y position.

  

      
        
- 
  
    
      #**font**(name = nil, options = DEFAULT_OPTS) { ... } ⇒ Font 
    

    
  
  
  
  
  
  
  
  

  
    

Without arguments, this returns the currently selected font.

  

      
        
- 
  
    
      #**font_families**  ⇒ Hash{String => Hash{Symbol => String, Hash{Symbol => String}}} 
    

    
  
  
  
  
  
  
  
  

  
    

Hash that maps font family names to their styled individual font definitions.

  

      
        
- 
  
    
      #**font_size**(points = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

When called with no argument, returns the current font size.

  

      
        
- 
  
    
      #**font_size=**(size)  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Sets the font size.

  

      
        
- 
  
    
      #**go_to_page**(page_number)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Re-opens the page with the given (1-based) page number so that you can draw on it.

  

      
        
- 
  
    
      #**indent**(left, right = 0) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Indents the specified number of PDF points for the duration of the block.

  

      
        
- 
  
    
      #**initialize**(options = {}, &block)  ⇒ Document 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Creates a new PDF Document.

  

      
        
- 
  
    
      #**move_cursor_to**(new_y)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Moves to the specified y position in relative terms to the bottom margin.

  

      
        
- 
  
    
      #**move_down**(amount)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Moves down the document by n points relative to the current position inside the current bounding box.

  

      
        
- 
  
    
      #**move_up**(amount)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Moves up the document by n points relative to the current position inside the current bounding box.

  

      
        
- 
  
    
      #**number_pages**(string, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Places a text box on specified pages for page numbering.

  

      
        
- 
  
    
      #**outline**  ⇒ Prawn::Outline 
    

    
  
  
  
  
  
  
  
  

  
    

Lazily instantiates a Prawn::Outline object for document.

  

      
        
- 
  
    
      #**pad**(y) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Moves down the document by y, executes a block, then moves down the document by y again.

  

      
        
- 
  
    
      #**pad_bottom**(y) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Executes a block then moves down the document.

  

      
        
- 
  
    
      #**pad_top**(y) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Moves down the document and then executes a block.

  

      
        
- 
  
    
      #**page_count**  ⇒ Integer 
    

    
  
  
  
  
  
  
  
  

  
    

Number of pages in the document.

  

      
        
- 
  
    
      #**reference_bounds**  ⇒ Prawn::Document::BoundingBox 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the innermost non-stretchy bounding box.

  

      
        
- 
  
    
      #**render**(output = nil)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Renders the PDF document to string.

  

      
        
- 
  
    
      #**render_file**(filename)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Renders the PDF document to file.

  

      
        
- 
  
    
      #**span**(width, options = {}) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

A span is a special purpose bounding box that allows a column of elements to be positioned relative to the margin_box.

  

      
        
- 
  
    
      #**start_new_page**(options = {})  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Creates and advances to a new page in the document.

  

      
        
- 
  
    
      #**width_of**(string, options = {})  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the width of the given string using the given font.

  

      
    

  
    
## 
      Experimental API
      collapse
    

    

      
        
- 
  
    
      #**column_box**(point, options = {}) {|parent_box| ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

A column box is a bounding box with the additional property that when text flows past the bottom, it will wrap first to another column on the same page, and only flow to the next page when all the columns are filled.

  

      
        
- 
  
    
      #**define_grid**(options = {})  ⇒ Grid 
    

    
  
  
  
  
  
  
  
  

  
    

Defines the grid system for a particular document.

  

      
        
- 
  
    
      #**find_font**(name, options = {})  ⇒ Font 
    

    
  
  
  
  
  
  
  
  

  
    

Looks up the given font using the given criteria.

  

      
        
- 
  
    
      #**font_registry**  ⇒ Hash{String => Font} 
    

    
  
  
  
  
  
  
  
  

  
    

Hash of Font objects keyed by names.

  

      
        
- 
  
    
      #**grid**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

A method that can either be used to access a particular grid on the page or work with the grid system directly.

  

      
        
- 
  
    
      #**group**(*_arguments)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**mask**(*fields)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**page_match?**(page_filter, page_number)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Provides a way to execute a block of code repeatedly based on a page_filter.

  

      
        
- 
  
    
      #**repeat**(page_filter, options = {}, &block)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Provides a way to execute a block of code repeatedly based on a `page_filter`.

  

      
        
- 
  
    
      #**save_font** { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Saves the current font, and then yields.

  

      
        
- 
  
    
      #**set_font**(font, size = nil)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Sets the font directly, given an actual Font object and size.

  

      
        
- 
  
    
      #**transaction**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Extension API
      collapse
    

    

      
        
- 
  
    
      .**extensions**  ⇒ Array<Module> 
    

    
  
  
  
  
  
  
  
  

  
    

Any module added to this array will be included into instances of Document at the per-object level.

  

      
        
- 
  
    
      .**inherited**(base)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize_first_page**(options)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Initializes the first page in a new document.

  

      
        
- 
  
    
      #**page**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**repeaters**  ⇒ Array 
    

    
  
  
  
  
  
  
  
  

  
    

A list of all repeaters in the document.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from TransformationStack

  

#add_to_transformation_stack, #current_transformation_matrix_with_translation, #restore_transformation_stack, #save_transformation_stack

  
  
  
  
  
  
  
  
  
### Methods included from SoftMask

  

#soft_mask

  
  
  
  
  
  
  
  
  
### Methods included from Stamp

  

#create_stamp, #stamp, #stamp_at

  
  
  
  
  
  
  
  
  
### Methods included from Images

  

#build_image_object, #embed_image, #image

  
  
  
  
  
  
  
  
  
### Methods included from Graphics

  

#circle, #close_and_stroke, #close_path, #curve, #curve_to, #ellipse, #fill, #fill_and_stroke, #fill_and_stroke_circle, #fill_and_stroke_ellipse, #fill_and_stroke_polygon, #fill_and_stroke_rectangle, #fill_and_stroke_rounded_rectangle, #fill_circle, #fill_ellipse, #fill_polygon, #fill_rectangle, #fill_rounded_polygon, #fill_rounded_rectangle, #horizontal_line, #horizontal_rule, #line, #line_to, #line_width, #line_width=, #move_to, #polygon, #rectangle, #rounded_polygon, #rounded_rectangle, #rounded_vertex, #stroke, #stroke_axis, #stroke_bounds, #stroke_curve, #stroke_ellipse, #stroke_horizontal_line, #stroke_horizontal_rule, #stroke_line, #stroke_polygon, #stroke_rectangle, #stroke_rounded_polygon, #stroke_rounded_rectangle, #stroke_vertical_line, #vertical_line

  
  
  
  
  
  
  
  
  
### Methods included from Graphics::Patterns

  

#fill_gradient, #stroke_gradient

  
  
  
  
  
  
  
  
  
### Methods included from Graphics::Transformation

  

#rotate, #scale, #transformation_matrix, #translate

  
  
  
  
  
  
  
  
  
### Methods included from Graphics::Transparency

  

#transparent

  
  
  
  
  
  
  
  
  
### Methods included from Graphics::JoinStyle

  

#join_style

  
  
  
  
  
  
  
  
  
### Methods included from Graphics::CapStyle

  

#cap_style

  
  
  
  
  
  
  
  
  
### Methods included from Graphics::Dash

  

#dash, #dashed?, #undash

  
  
  
  
  
  
  
  
  
### Methods included from Graphics::Color

  

#fill_color, hex2rgb, rgb2hex, #stroke_color

  
  
  
  
  
  
  
  
  
### Methods included from Graphics::BlendMode

  

#blend_mode

  
  
  
  
  
  
  
  
  
### Methods included from Text

  

#draw_text, #draw_text!, #formatted_text, #height_of, #height_of_formatted, #text, #text_box

  
  
  
  
  
  
  
  
  
### Methods included from Text::Formatted

  

#formatted_text_box

  
  
  
  
  
  
  
  
  
  
### Methods included from Security

  

#encrypt_document, encrypt_string

  
  
  
  
  
  
  
  
  
  
  
### Methods included from Internals

  

#renderer, #restore_graphics_state, #save_graphics_state

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(options = {}, &block)  ⇒ Document 
  

  

  

  
    

Creates a new PDF Document.

Setting e.g. the `:margin` to 100 points and the `:left_margin` to 50 will result in margins of 100 points on every side except for the left, where it will be 50.

The `:margin` can also be an array much like CSS shorthand:

“‘ruby # Top and bottom are 20, left and right are 100. margin: [20, 100] # Top is 50, left and right are 100, bottom is 20. margin: [50, 100, 20] # Top is 10, right is 20, bottom is 30, left is 40. margin: [10, 20, 30, 40] “`

Additionally, `:page_size` can be specified as a simple two value array giving the width and height of the document you need in PDF Points.

  

  
  
    
#### Examples:

    
      
        
##### 

New document, US Letter paper, portrait orientation

      
      

```
pdf = Prawn::Document.new
```

    
      
        
##### 

New document, A4 paper, landscaped

      
      

```
pdf = Prawn::Document.new(page_size: "A4", page_layout: :landscape)
```

    
      
        
##### 

New document, Custom size

      
      

```
pdf = Prawn::Document.new(page_size: [200, 300])
```

    
      
        
##### 

New document, with background

      
      

```
pdf = Prawn::Document.new(
  background: "#{Prawn::DATADIR}/images/pigs.jpg"
)
```

    
  

Parameters:

  
    
- 
      
        options
      
      
        (Hash{Symbol => any})
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    

Options Hash (options):
    

      
        
- 
          :page_size
          (String, Array(Number, Number))
          
            
              — default:
              LETTER
            
          
          
            — 

One of the `PDF::Core::PageGeometry` sizes.

          
        
      
        
- 
          :page_layout
          (:portrait, :landscape)
          
            
          
          
            — 

Page orientation.

          
        
      
        
- 
          :margin
          (Number, Array<Number>)
          
            
              — default:
              [32]
            
          
          
            — 

Sets the margin on all sides in points.

          
        
      
        
- 
          :left_margin
          (Number)
          
            
              — default:
              32
            
          
          
            — 

Sets the left margin in points.

          
        
      
        
- 
          :right_margin
          (Number)
          
            
              — default:
              32
            
          
          
            — 

Sets the right margin in points.

          
        
      
        
- 
          :top_margin
          (Number)
          
            
              — default:
              32
            
          
          
            — 

Sets the top margin in points.

          
        
      
        
- 
          :bottom_margin
          (Number)
          
            
              — default:
              32
            
          
          
            — 

Sets the bottom margin in points.

          
        
      
        
- 
          :skip_page_creation
          (Boolean)
          
            
              — default:
              false
            
          
          
            — 

Creates a document without starting the first page.

          
        
      
        
- 
          :compress
          (Boolean)
          
            
              — default:
              false
            
          
          
            — 

Compresses content streams before rendering them.

          
        
      
        
- 
          :background
          (String?)
          
            
              — default:
              nil
            
          
          
            — 

An image path to be used as background on all pages.

          
        
      
        
- 
          :background_scale
          (Number?)
          
            
              — default:
              1
            
          
          
            — 

Background image scale.

          
        
      
        
- 
          :info
          (Hash{Symbol => any}?)
          
            
              — default:
              nil
            
          
          
            — 

Generic hash allowing for custom metadata properties.

          
        
      
        
- 
          :text_formatter
          (Object)
          
            
              — default:
              Prawn::Text::Formatted::Parser
            
          
          
            — 

The text formatter to use for ‘:inline_format`ted text.

          
        
      
    

  
    
    

  
    
      

```

227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
```

    
    
      

```
# File 'lib/prawn/document.rb', line 227

def initialize(options = {}, &block)
  options = options.dup

  Prawn.verify_options(VALID_OPTIONS, options)

  # need to fix, as the refactoring breaks this
  # raise NotImplementedError if options[:skip_page_creation]

  self.class.extensions.reverse_each { |e| extend(e) }
  self.state = PDF::Core::DocumentState.new(options)
  state.populate_pages_from_store(self)
  renderer.min_version(state.store.min_version) if state.store.min_version

  renderer.min_version(1.6) if options[:print_scaling] == :none

  @background = options[:background]
  @background_scale = options[:background_scale] || 1
  @font_size = 12

  @bounding_box = nil
  @margin_box = nil

  @page_number = 0

  @text_formatter = options.delete(:text_formatter) ||
    Text::Formatted::Parser

  options[:size] = options.delete(:page_size)
  options[:layout] = options.delete(:page_layout)

  initialize_first_page(options)

  @bounding_box = @margin_box

  if block
    block.arity < 1 ? instance_eval(&block) : block[self]
  end
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**margin_box**  ⇒ Prawn::Document::BoundingBox 
  

  

  

  
    

Current margin box.

  

  

Returns:

  
    
- 
      
      
        (Prawn::Document::BoundingBox)
      
      
      
    
  

  
    
      

```

109
110
111
```

    
    
      

```
# File 'lib/prawn/document.rb', line 109

def margin_box
  @margin_box
end
```

    
  

    
      
      
      
  
### 
  
    #**margins**  ⇒ {:left, :top, :right, :bottom => Number}  (readonly)
  

  

  

  
    

Current page margins.

  

  

Returns:

  
    
- 
      
      
        ({:left, :top, :right, :bottom => Number})
      
      
      
    
  

  
    
      

```

113
114
115
```

    
    
      

```
# File 'lib/prawn/document.rb', line 113

def margins
  @margins
end
```

    
  

    
      
      
      
  
### 
  
    #**page_number**  ⇒ Integer 
  

  

  

  
    

Current page number.

  

  

Returns:

  
    
- 
      
      
        (Integer)
      
      
      
    
  

  
    
      

```

121
122
123
```

    
    
      

```
# File 'lib/prawn/document.rb', line 121

def page_number
  @page_number
end
```

    
  

    
      
      
      
  
### 
  
    #**state**  ⇒ Object 
  

  

  

  
    
      

```

778
779
780
```

    
    
      

```
# File 'lib/prawn/document.rb', line 778

def state
  @state
end
```

    
  

    
      
      
      
  
### 
  
    #**text_formatter**  ⇒ Object 
  

  

  

  
    

Current text formatter. By default it’s Text::Formatted::Parser

  

  

Returns:

  
    
- 
      
      
        (Object)
      
      
      
    
  

  
    
      

```

127
128
129
```

    
    
      

```
# File 'lib/prawn/document.rb', line 127

def text_formatter
  @text_formatter
end
```

    
  

    
      
      
      
  
### 
  
    #**y**  ⇒ Number 
  

  

  

  
    

Absolute cursor position.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

117
118
119
```

    
    
      

```
# File 'lib/prawn/document.rb', line 117

def y
  @y
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**extensions**  ⇒ Array<Module> 
  

  

  

  
    

Any module added to this array will be included into instances of Prawn::Document at the per-object level.  These will also be inherited by any subclasses.

  

  
  
    
#### Examples:

    
      
      

```
module MyFancyModule
  def party!
    text "It's a big party!"
  end
end

Prawn::Document.extensions << MyFancyModule

Prawn::Document.generate("foo.pdf") do
  party!
end
```

    
  

Returns:

  
    
- 
      
      
        (Array<Module>)
      
      
      
    
  

  
    
      

```

95
96
97
```

    
    
      

```
# File 'lib/prawn/document.rb', line 95

def self.extensions
  @extensions ||= []
end
```

    
  

    
      
  
### 
  
    .**generate**(filename, options = {}, &block)  ⇒ Object 
  

  

  

  
    

Creates and renders a PDF document.

When using the implicit block form, Prawn will evaluate the block within an instance of Prawn::Document, simplifying your syntax. However, please note that you will not be able to reference variables from the enclosing scope within this block.

“‘ruby # Using implicit block form and rendering to a file Prawn::Document.generate “example.pdf” do

```
# self here is set to the newly instantiated Prawn::Document
# and so any variables in the outside scope are unavailable
font "Times-Roman"
draw_text "Hello World", at: [200,720], size: 32

```

end “‘

If you need to access your local and instance variables, use the explicit block form shown below. In this case, Prawn yields an instance of Prawn::Document and the block is an ordinary closure:

“‘ruby # Using explicit block form and rendering to a file content = “Hello World” Prawn::Document.generate “example.pdf” do |pdf|

```
# self here is left alone
pdf.font "Times-Roman"
pdf.draw_text content, at: [200,720], size: 32

```

end “‘

  

  

  
    
      

```

161
162
163
164
```

    
    
      

```
# File 'lib/prawn/document.rb', line 161

def self.generate(filename, options = {}, &block)
  pdf = new(options, &block)
  pdf.render_file(filename)
end
```

    
  

    
      
  
### 
  
    .**inherited**(base)  ⇒ Object 
  

  

  

  
    
      

```

100
101
102
103
```

    
    
      

```
# File 'lib/prawn/document.rb', line 100

def self.inherited(base)
  super
  extensions.each { |e| base.extensions << e }
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**bounding_box**(point, options = {}) {|parent_box| ... } ⇒ void 
  

  

  

  
    

A bounding box serves two important purposes:

- 

Provide bounds for flowing text, starting at a given point

- 

Translate the origin (0, 0) for graphics primitives

#### Positioning

Bounding boxes are positioned relative to their top left corner and the width measurement is towards the right and height measurement is downwards.

Usage:

- 

Bounding box 100pt×100pt in the absolute bottom left of the containing box:

“‘ruby pdf.bounding_box([0, 100], width: 100, height: 100)

```
stroke_bounds

```

end “‘

- 

Bounding box 200pt×400pt high in the center of the page:

“‘ruby x_pos = ((bounds.width / 2) - 150) y_pos = ((bounds.height / 2) + 200) pdf.bounding_box([x_pos, y_pos], width: 300, height: 400) do

```
stroke_bounds

```

end “‘

#### Flowing Text

When flowing text, the usage of a bounding box is simple. Text will begin at the point specified, flowing the width of the bounding box. After the block exits, the cursor position will be moved to the bottom of the bounding box (y - height). If flowing text exceeds the height of the bounding box, the text will be continued on the next page, starting again at the top-left corner of the bounding box.

Usage:

“‘ruby pdf.bounding_box([100, 500], width: 100, height: 300) do

```
pdf.text "This text will flow in a very narrow box starting" +
 "from [100, 500]. The pointer will then be moved to [100, 200]" +
 "and return to the margin_box"

```

end “‘

Note, this is a low level tool and is designed primarily for building other abstractions. If you just need to flow text on the page, you will want to look at #span and Text#text_box instead.

#### Translating Coordinates

When translating coordinates, the idea is to allow the user to draw relative to the origin, and then translate their drawing to a specified area of the document, rather than adjust all their drawing coordinates to match this new region.

Take for example two triangles which share one point, drawn from the origin:

“‘ruby pdf.polygon [0, 250], [0, 0], [150, 100] pdf.polygon [100, 0], [150, 100], [200, 0] “`

It would be easy enough to translate these triangles to another point, e.g ‘[200, 200]`

“‘ruby pdf.polygon [200, 450], [200, 200], [350, 300] pdf.polygon [300, 200], [350, 300], [400, 200] “`

However, each time you want to move the drawing, you’d need to alter every point in the drawing calls, which as you might imagine, can become tedious.

If instead, we think of the drawing as being bounded by a box, we can see that the image is 200 points wide by 250 points tall.

To translate it to a new origin, we simply select a point at (x, y + height).

Using the [200, 200] example:

“‘ruby pdf.bounding_box([200, 450], width: 200, height: 250) do

```
pdf.stroke do
  pdf.polygon [0, 250], [0, 0], [150, 100]
  pdf.polygon [100, 0], [150, 100], [200, 0]
end

```

end “‘

Notice that the drawing is still relative to the origin. If we want to move this drawing around the document, we simply need to recalculate the top-left corner of the rectangular bounding-box, and all of our graphics calls remain unmodified.

#### Nesting Bounding Boxes

At the top level, bounding boxes are specified relative to the document’s margin_box (which is itself a bounding box). You can also nest bounding boxes, allowing you to build components which are relative to each other

Usage:

“‘ruby pdf.bounding_box([200, 450], width: 200, height: 250) do

```
pdf.stroke_bounds   # Show the containing bounding box
pdf.bounding_box([50, 200], width: 50, height: 50) do
  # a 50x50 bounding box that starts 50 pixels left and 50 pixels down
  # the parent bounding box.
  pdf.stroke_bounds
end

```

end “‘

#### Stretchiness

If you do not specify a height to a bounding box, it will become stretchy and its height will be calculated automatically as you stretch the box downwards.

```
pdf.bounding_box([100, 400], width: 400) do
  pdf.text("The height of this box is #{pdf.bounds.height}")
  pdf.text('this is some text')
  pdf.text('this is some more text')
  pdf.text('and finally a bit more')
  pdf.text("Now the height of this box is #{pdf.bounds.height}")
end

```

#### Absolute Positioning

If you wish to position the bounding boxes at absolute coordinates rather than relative to the margins or other bounding boxes, you can use canvas()

“‘ruby pdf.bounding_box([50, 500], width: 200, height: 300) do

```
pdf.stroke_bounds
pdf.canvas do
  Positioned outside the containing box at the 'real' (300, 450)
  pdf.bounding_box([300, 450], width: 200, height: 200) do
    pdf.stroke_bounds
  end
end

```

end “‘

Of course, if you use canvas, you will be responsible for ensuring that you remain within the printable area of your document.

  

  
  
  
    

This method returns an undefined value.

  

  

Parameters:

  
    
- 
      
        point
      
      
        (Array(Number, Number))
      
      
      
        —
        

top left corner of the new bounding box

      
    
  
    
- 
      
        options
      
      
        (Hash{Symbol => any})
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :width
          (Number)
          
            
          
          
            — 

width of the new bounding box, must be specified.

          
        
      
        
- 
          :height
          (Number)
          
            
          
          
            — 

height of the new bounding box, stretchy box if omitted.

          
        
      
    

  

Yield Parameters:

  
    
- 
      
        parent_box
      
      
        (BoundingBox)
      
      
      
        —
        

parent bounding box

      
    
  

Yield Returns:

  
    
- 
      
      
        (void)
      
      
      
    
  

  
    
      

```

174
175
176
177
178
179
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 174

def bounding_box(point, *args, &block)
  init_bounding_box(block) do |parent_box|
    point = map_to_absolute(point)
    @bounding_box = BoundingBox.new(self, parent_box, point, *args)
  end
end
```

    
  

    
      
  
### 
  
    #**bounds**  ⇒ Prawn::Document::BoundingBox 
  

  

  

  
    

The bounds method returns the current bounding box you are currently in, which is by default the box represented by the margin box on the document itself. When called from within a created `bounding_box` block, the box defined by that call will be returned instead of the document margin box.

Another important point about bounding boxes is that all x and y measurements within a bounding box code block are relative to the bottom left corner of the bounding box.

  

  
  
    
#### Examples:

    
      
      

```
Prawn::Document.new do
  # In the default "margin box" of a Prawn document of 0.5in along each
  # edge

  # Draw a border around the page (the manual way)
  stroke do
    line(bounds.bottom_left, bounds.bottom_right)
    line(bounds.bottom_right, bounds.top_right)
    line(bounds.top_right, bounds.top_left)
    line(bounds.top_left, bounds.bottom_left)
  end

  # Draw a border around the page (the easy way)
  stroke_bounds
end
```

    
  

Returns:

  
    
- 
      
      
        (Prawn::Document::BoundingBox)
      
      
      
    
  

  
    
      

```

504
505
506
```

    
    
      

```
# File 'lib/prawn/document.rb', line 504

def bounds
  @bounding_box
end
```

    
  

    
      
  
### 
  
    #**bounds=**(bounding_box)  ⇒ bounding_box 
  

  

  

  
    

Sets #bounds to the BoundingBox provided. See #bounds for a brief description of what a bounding box is. This function is useful if you really need to change the bounding box manually, but usually, just entering and exiting bounding box code blocks is good enough.

  

  

Parameters:

  
    
- 
      
        bounding_box
      
      
        (Prawn::Document::BoundingBox)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (bounding_box)
      
      
      
    
  

  
    
      

```

523
524
525
```

    
    
      

```
# File 'lib/prawn/document.rb', line 523

def bounds=(bounding_box)
  @bounding_box = bounding_box
end
```

    
  

    
      
  
### 
  
    #**canvas**(&block)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

A shortcut to produce a bounding box which is mapped to the document’s absolute coordinates, regardless of how things are nested or margin sizes.

  

  
  
    
#### Examples:

    
      
      

```
pdf.canvas do
  pdf.line pdf.bounds.bottom_left, pdf.bounds.top_right
end
```

    
  

Yield Returns:

  
    
- 
      
      
        (void)
      
      
      
    
  

  
    
      

```

191
192
193
194
195
196
197
198
199
200
201
202
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 191

def canvas(&block)
  init_bounding_box(block, hold_position: true) do |_|
    # Canvas bbox acts like margin_box in that its parent bounds are unset.
    @bounding_box = BoundingBox.new(
      self,
      nil,
      [0, page.dimensions[3]],
      width: page.dimensions[2],
      height: page.dimensions[3],
    )
  end
end
```

    
  

    
      
  
### 
  
    #**column_box**(point, options = {}) {|parent_box| ... } ⇒ void 
  

  

  

  
    

A column box is a bounding box with the additional property that when text flows past the bottom, it will wrap first to another column on the same page, and only flow to the next page when all the columns are filled.

`column_box` accepts the same parameters as #bounding_box, as well as the number of `:columns` and a `:spacer` (in points) between columns. If resetting the top margin is desired on a new page (e.g. to allow for initial page wide column titles) the option ‘reflow_margins: true` can be set.

  

  
  
  
    

This method returns an undefined value.

  

  

Parameters:

  
    
- 
      
        point
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        options
      
      
        (Hash{Symbol => any})
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :width
          (Number)
          
            
          
          
            — 

width of the new column box, must be specified.

          
        
      
        
- 
          :height
          (Number)
          
            
          
          
            — 

height of the new column box, stretchy box if omitted.

          
        
      
        
- 
          :hold_position
          (Boolean)
          
            
          
          
            — 

whether to put cursor at the bottom of the column box.

          
        
      
        
- 
          :columns
          (Integer)
          
            
              — default:
              3
            
          
          
        
      
        
- 
          :spacer
          (Number)
          
            
              — default:
              font_size
            
          
          
        
      
        
- 
          :reflow_margins
          (Boolean)
          
            
              — default:
              false
            
          
          
        
      
    

  

Yield Parameters:

  
    
- 
      
        parent_box
      
      
        (BoundingBox)
      
      
      
        —
        

parent bounding box

      
    
  

  
    
      

```

34
35
36
37
38
39
```

    
    
      

```
# File 'lib/prawn/document/column_box.rb', line 34

def column_box(*args, &block)
  init_column_box(block) do |parent_box|
    map_to_absolute!(args[0])
    @bounding_box = ColumnBox.new(self, parent_box, *args)
  end
end
```

    
  

    
      
  
### 
  
    #**cursor**  ⇒ Number 
  

  

  

  
    

The current y drawing position relative to the innermost bounding box, or to the page margins at the top level.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

415
416
417
```

    
    
      

```
# File 'lib/prawn/document.rb', line 415

def cursor
  y - bounds.absolute_bottom
end
```

    
  

    
      
  
### 
  
    #**define_grid**(options = {})  ⇒ Grid 
  

  

  

  
    
  
    **Note:**
    

A completely new grid object is built each time `define_grid` is called. This means that all subsequent calls to grid() will use the newly defined Grid object – grids are not nestable like bounding boxes are.

  

Defines the grid system for a particular document. Takes the number of rows and columns and the width to use for the gutter as the keys :rows, :columns, :gutter, :row_gutter, :column_gutter

  

  

Parameters:

  
    
- 
      
        options
      
      
        (Hash{Symbol => any})
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    

Options Hash (options):
    

      
        
- 
          :columns
          (Integer)
          
            
          
          
            — 

Number of columns in the grid.

          
        
      
        
- 
          :rows
          (Integer)
          
            
          
          
            — 

Number of rows in the grid.

          
        
      
        
- 
          :gutter
          (Number)
          
            
          
          
            — 

Gutter size. `:row_gutter` and `:column_gutter` are ignored if specified.

          
        
      
        
- 
          :row_gutter
          (Number)
          
            
          
          
            — 

Row gutter size.

          
        
      
        
- 
          :column_gutter
          (Number)
          
            
          
          
            — 

Column gutter size.

          
        
      
    

  

Returns:

  
    
- 
      
      
        (Grid)
      
      
      
    
  

  
    
      

```

24
25
26
27
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 24

def define_grid(options = {})
  @boxes = nil
  @grid = Grid.new(self, options)
end
```

    
  

    
      
  
### 
  
    #**delete_page**(index)  ⇒ Boolean 
  

  

  

  
    

Remove page of the document by index.

  

  
  
    
#### Examples:

    
      
      

```
pdf = Prawn::Document.new
pdf.page_count #=> 1
3.times { pdf.start_new_page }
pdf.page_count #=> 4
pdf.delete_page(-1)
pdf.page_count #=> 3
```

    
  

Parameters:

  
    
- 
      
        index
      
      
        (Integer)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

366
367
368
369
370
371
372
373
374
375
```

    
    
      

```
# File 'lib/prawn/document.rb', line 366

def delete_page(index)
  return false if index.abs > (state.pages.count - 1)

  state.pages.delete_at(index)

  state.store.pages.data[:Kids].delete_at(index)
  state.store.pages.data[:Count] -= 1
  @page_number -= 1
  true
end
```

    
  

    
      
  
### 
  
    #**find_font**(name, options = {})  ⇒ Font 
  

  

  

  
    

Looks up the given font using the given criteria. Once a font has been found by that matches the criteria, it will be cached to subsequent lookups for that font will return the same object.

  

  

Parameters:

  
    
- 
      
        name
      
      
        (String)
      
      
      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :style
          (Symbol)
          
            
          
          
        
      
        
- 
          :file
          (String)
          
            
          
          
        
      
        
- 
          :font
          (Integer, String)
          
            
          
          
            — 

index or name of the font in a font suitcase/collection

          
        
      
    

  

Returns:

  
    
- 
      
      
        (Font)
      
      
      
    
  

  
    
      

```

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
# File 'lib/prawn/font.rb', line 291

def find_font(name, options = {}) # :nodoc:
  if font_families.key?(name)
    family = name
    name = font_families[name][options[:style] || :normal]
    if name.is_a?(::Hash)
      options = options.merge(name)
      name = options[:file]
    end
  end
  key = "#{family}:#{name}:#{options[:font] || 0}"

  if name.is_a?(Prawn::Font)
    font_registry[key] = name
  else
    font_registry[key] ||=
      Font.load(self, name, options.merge(family: family))
  end
end
```

    
  

    
      
  
### 
  
    #**float**  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Executes a block and then restores the original y position. If new pages were created during this block, it will teleport back to the original page when done.

  

  
  
    
#### Examples:

    
      
      

```
pdf.text "A"

pdf.float do
  pdf.move_down 100
  pdf.text "C"
end

pdf.text "B"
```

    
  

  
    
      

```

442
443
444
445
446
447
448
```

    
    
      

```
# File 'lib/prawn/document.rb', line 442

def float
  original_page = page_number
  original_y = y
  yield
  go_to_page(original_page) unless page_number == original_page
  self.y = original_y
end
```

    
  

    
      
  
### 
  
    #**font**(name = nil, options = DEFAULT_OPTS) { ... } ⇒ Font 
  

  

  

  
    

Without arguments, this returns the currently selected font. Otherwise, it sets the current font. When a block is used, the font is applied transactionally and is rolled back when the block exits.

“‘ruby Prawn::Document.generate(“font.pdf”) do

```
text "Default font is Helvetica"

font "Times-Roman"
text "Now using Times-Roman"

font("DejaVuSans.ttf") do
  text "Using TTF font from file DejaVuSans.ttf"
  font "Courier", style: :bold
  text "You see this in bold Courier"
end

text "Times-Roman, again"

```

end “‘

The `name` parameter must be a string. It can be one of the 14 built-in fonts supported by PDF, or the location of a TTF file. The Fonts::AFM::BUILT_INS array specifies the valid built in font names.

If a TTF/OTF font is specified, the glyphs necessary to render your document will be embedded in the rendered PDF. This should be your preferred option in most cases. It will increase the size of the resulting file, but also make it more portable.

The options parameter is an optional hash providing size and style. To use the :style option you need to map those font styles to their respective font files.

  

  

Parameters:

  
    
- 
      
        name
      
      
        (String)
      
      
        *(defaults to: nil)*
      
      
        —
        

font name. It can be:

  - 

One of 14 PDF built-in fonts.

  - 

A font file path.

  - 

A font name defined in #font_families

      
    
  
    
- 
      
        options
      
      
        (Hash{Symbol => any})
      
      
        *(defaults to: DEFAULT_OPTS)*
      
      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :style
          (Symbol)
          
            
          
          
            — 

font style

          
        
      
    

  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Font)
      
      
      
    
  

  

See Also:
  

    
      
- #font_families
    
      
- Fonts::AFM::BUILT_INS
    
  

  
    
      

```

56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
```

    
    
      

```
# File 'lib/prawn/font.rb', line 56

def font(name = nil, options = DEFAULT_OPTS)
  return((defined?(@font) && @font) || font('Helvetica')) if name.nil?

  if state.pages.empty? && !state.page.in_stamp_stream?
    raise Prawn::Errors::NotOnPage
  end

  new_font = find_font(name.to_s, options)

  if block_given?
    save_font do
      set_font(new_font, options[:size])
      yield
    end
  else
    set_font(new_font, options[:size])
  end

  @font
end
```

    
  

    
      
  
### 
  
    #**font_families**  ⇒ Hash{String => Hash{Symbol => String, Hash{Symbol => String}}} 
  

  

  

  
    

Hash that maps font family names to their styled individual font definitions.

To add support for another font family, append to this hash, e.g:

“‘ruby pdf.font_families.update(

```
"MyTrueTypeFamily" => {
  bold: "foo-bold.ttf",
  italic: "foo-italic.ttf",
  bold_italic: "foo-bold-italic.ttf",
  normal: "foo.ttf",
}

```

) “‘

This will then allow you to use the fonts like so:

“‘ruby pdf.font(“MyTrueTypeFamily”, style: :bold) pdf.text “Some bold text” pdf.font(“MyTrueTypeFamily”) pdf.text “Some normal text” “`

This assumes that you have appropriate TTF/OTF fonts for each style you wish to support.

By default the styles `:bold`, `:italic`, `:bold_italic`, and `:normal` are defined for fonts “Courier”, “Times-Roman” and “Helvetica”. When defining your own font families, you can map any or all of these styles to whatever font files you’d like.

Font definition can be either a hash or just a string.

A hash font definition can specify a number of options:

- 

`:file` – path to the font file (required)

- 

`:subset` – whether to subset the font (default false). Only applicable to TrueType and OpenType fonts (includnig DFont and TTC).

A string font definition is equivalent to hash definition with only `:file` being specified.

  

  

Returns:

  
    
- 
      
      
        (Hash{String => Hash{Symbol => String, Hash{Symbol => String}}})
      
      
      
    
  

  
    
      

```

212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
```

    
    
      

```
# File 'lib/prawn/font.rb', line 212

def font_families
  @font_families ||= {}.merge!(
    'Courier' => {
      bold: 'Courier-Bold',
      italic: 'Courier-Oblique',
      bold_italic: 'Courier-BoldOblique',
      normal: 'Courier',
    },

    'Times-Roman' => {
      bold: 'Times-Bold',
      italic: 'Times-Italic',
      bold_italic: 'Times-BoldItalic',
      normal: 'Times-Roman',
    },

    'Helvetica' => {
      bold: 'Helvetica-Bold',
      italic: 'Helvetica-Oblique',
      bold_italic: 'Helvetica-BoldOblique',
      normal: 'Helvetica',
    },
  )
end
```

    
  

    
      
  
### 
  
    #**font_registry**  ⇒ Hash{String => Font} 
  

  

  

  
    

Hash of Font objects keyed by names.

  

  

Returns:

  
    
- 
      
      
        (Hash{String => Font})
      
      
      
    
  

  
    
      

```

314
315
316
```

    
    
      

```
# File 'lib/prawn/font.rb', line 314

def font_registry
  @font_registry ||= {}
end
```

    
  

    
      
  
### 
  
    
      #**font_size**  ⇒ Number 
    
      #**font_size**(points) { ... } ⇒ void 
    
  

  

  

  
    

When called with no argument, returns the current font size.

When called with a single argument but no block, sets the current font size. When a block is used, the font size is applied transactionally and is rolled back when the block exits. You may still change the font size within a transactional block for individual text segments, or nested calls to `font_size`.

  

  
  
    
#### Examples:

    
      
      

```
Prawn::Document.generate("font_size.pdf") do
  font_size 16
  text "At size 16"

  font_size(10) do
    text "At size 10"
    text "At size 6", size: 6
    text "At size 10"
  end

  text "At size 16"
end
```

    
  

  

Overloads:
  

    
      
      
- 
        #**font_size**  ⇒ Number 
        
  
    

Returns vurrent font size.

  

  

Returns:

  
    
  - 
      
      
        (Number)
      
      
      
        —
        

vurrent font size

      
    
  

      
    
      
      
- 
        #**font_size**(points) { ... } ⇒ void 
        
  
    

This method returns an undefined value.

  

  

Parameters:

  
    
  - 
      
        points
      
      
        (Number)
      
      
      
        —
        

new font size

      
    
  

Yields:

  
    
  - 
      
      
        
      
      
      
        
        

if block is provided font size is set only for the duration of the block

      
    
  

      
    
  

  
    
      

```

106
107
108
109
110
111
112
113
```

    
    
      

```
# File 'lib/prawn/font.rb', line 106

def font_size(points = nil)
  return @font_size unless points

  size_before_yield = @font_size
  @font_size = points
  block_given? ? yield : return
  @font_size = size_before_yield
end
```

    
  

    
      
  
### 
  
    #**font_size=**(size)  ⇒ Number 
  

  

  

  
    

Sets the font size.

  

  

Parameters:

  
    
- 
      
        size
      
      
        (Number)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

119
120
121
```

    
    
      

```
# File 'lib/prawn/font.rb', line 119

def font_size=(size)
  font_size(size)
end
```

    
  

    
      
  
### 
  
    #**go_to_page**(page_number)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Re-opens the page with the given (1-based) page number so that you can draw on it.

  

  

Parameters:

  
    
- 
      
        page_number
      
      
        (Integer)
      
      
      
    
  

  
    
      

```

395
396
397
398
399
400
```

    
    
      

```
# File 'lib/prawn/document.rb', line 395

def go_to_page(page_number)
  @page_number = page_number
  state.page = state.pages[page_number - 1]
  generate_margin_box
  @y = @bounding_box.absolute_top
end
```

    
  

    
      
  
### 
  
    
      #**grid**  ⇒ Grid 
    
      #**grid**(row, column)  ⇒ GridBox 
    
      #**grid**(box1, box2)  ⇒ MultiBox 
    
  

  

  

  
    

A method that can either be used to access a particular grid on the page or work with the grid system directly.

  

  
  

Overloads:
  

    
      
      
- 
        #**grid**  ⇒ Grid 
        
  
    

Get current grid.

  

  

Returns:

  
    
  - 
      
      
        (Grid)
      
      
      
    
  

      
    
      
      
- 
        #**grid**(row, column)  ⇒ GridBox 
        
  
    

Get a grid box.

  

  

Parameters:

  
    
  - 
      
        row
      
      
        (Integer)
      
      
      
    
  
    
  - 
      
        column
      
      
        (Integer)
      
      
      
    
  

Returns:

  
    
  - 
      
      
        (GridBox)
      
      
      
    
  

      
    
      
      
- 
        #**grid**(box1, box2)  ⇒ MultiBox 
        
  
    

Get a grid multi-box.

  

  

Parameters:

  
    
  - 
      
        box1
      
      
        (Array(Integer, Integer))
      
      
      
        —
        

Start box coordinates.

      
    
  
    
  - 
      
        box2
      
      
        (Array(Integer, Integer))
      
      
      
        —
        

End box coordinates.

      
    
  

Returns:

  
    
  - 
      
      
        (MultiBox)
      
      
      
    
  

      
    
  

  
    
      

```

50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 50

def grid(*args)
  @boxes ||= {}
  @boxes[args] ||=
    if args.empty?
      @grid
    else
      g1, g2 = args

      if g1.is_a?(Array) && g2.is_a?(Array) &&
          g1.length == 2 && g2.length == 2
        multi_box(single_box(*g1), single_box(*g2))
      else
        single_box(g1, g2)
      end
    end
end
```

    
  

    
      
  
### 
  
    #**group**(*_arguments)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

700
701
702
703
704
705
706
```

    
    
      

```
# File 'lib/prawn/document.rb', line 700

def group(*_arguments)
  raise NotImplementedError,
    'Document#group has been disabled because its implementation ' \
      'lead to corrupted documents whenever a page boundary was ' \
      'crossed. We will try to work on reimplementing it in a ' \
      'future release'
end
```

    
  

    
      
  
### 
  
    #**indent**(left, right = 0) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Indents the specified number of PDF points for the duration of the block

  

  
  
    
#### Examples:

    
      
      

```
pdf.text "some text"
pdf.indent(20) do
  pdf.text "This is indented 20 points"
end
pdf.text "This starts 20 points left of the above line " +
         "and is flush with the first line"
pdf.indent 20, 20 do
  pdf.text "This line is indented on both sides."
end
```

    
  

Parameters:

  
    
- 
      
        left
      
      
        (Number)
      
      
      
    
  
    
- 
      
        right
      
      
        (Number)
      
      
        *(defaults to: 0)*
      
      
    
  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

  
    
      

```

615
616
617
```

    
    
      

```
# File 'lib/prawn/document.rb', line 615

def indent(left, right = 0, &block)
  bounds.indent(left, right, &block)
end
```

    
  

    
      
  
### 
  
    #**initialize_first_page**(options)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Initializes the first page in a new document. This methods allows customisation of this process in extensions such as Prawn::Template.

  

  

Parameters:

  
    
- 
      
        options
      
      
        (Hash)
      
      
      
    
  

  
    
      

```

767
768
769
770
771
772
773
```

    
    
      

```
# File 'lib/prawn/document.rb', line 767

def initialize_first_page(options)
  if options[:skip_page_creation]
    start_new_page(options.merge(orphan: true))
  else
    start_new_page(options)
  end
end
```

    
  

    
      
  
### 
  
    #**mask**(*fields)  ⇒ Object 
  

  

  

  
    
      

```

749
750
751
752
753
754
755
756
757
```

    
    
      

```
# File 'lib/prawn/document.rb', line 749

def mask(*fields)
  # Stores the current state of the named attributes, executes the block,
  # and then restores the original values after the block has executed.
  # -- I will remove the nodoc if/when this feature is a little less hacky
  stored = {}
  fields.each { |f| stored[f] = public_send(f) }
  yield
  fields.each { |f| public_send(:"#{f}=", stored[f]) }
end
```

    
  

    
      
  
### 
  
    #**move_cursor_to**(new_y)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Moves to the specified y position in relative terms to the bottom margin.

  

  

Parameters:

  
    
- 
      
        new_y
      
      
        (Number)
      
      
      
    
  

  
    
      

```

423
424
425
```

    
    
      

```
# File 'lib/prawn/document.rb', line 423

def move_cursor_to(new_y)
  self.y = new_y + bounds.absolute_bottom
end
```

    
  

    
      
  
### 
  
    #**move_down**(amount)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Moves down the document by n points relative to the current position inside the current bounding box.

  

  

Parameters:

  
    
- 
      
        amount
      
      
        (Number)
      
      
      
    
  

  
    
      

```

541
542
543
```

    
    
      

```
# File 'lib/prawn/document.rb', line 541

def move_down(amount)
  self.y -= amount
end
```

    
  

    
      
  
### 
  
    #**move_up**(amount)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Moves up the document by n points relative to the current position inside the current bounding box.

  

  

Parameters:

  
    
- 
      
        amount
      
      
        (Number)
      
      
      
    
  

  
    
      

```

532
533
534
```

    
    
      

```
# File 'lib/prawn/document.rb', line 532

def move_up(amount)
  self.y += amount
end
```

    
  

    
      
  
### 
  
    #**number_pages**(string, options = {})  ⇒ Object 
  

  

  

  
    

Places a text box on specified pages for page numbering.  This should be called towards the end of document creation, after all your content is already in place. In your template string, ‘<page>` refers to the current page, and `<total>` refers to the total amount of pages in the document. Page numbering should occur at the end of your generate block because the method iterates through existing pages after they are created.

Please refer to Text#text_box for additional options concerning text formatting and placement.

  

  
  
    
#### Examples:

    
      
        
##### 

Print page numbers on every page except for the first. Start counting from five.

      
      

```
Prawn::Document.generate("page_with_numbering.pdf") do
  number_pages "<page> in a total of <total>", {
    start_count_at: 5,
    page_filter: lambda { |pg| pg != 1 },
    at: [bounds.right - 50, 0],
    align: :right,
    size: 14
  }
end
```

    
  

Parameters:

  
    
- 
      
        string
      
      
        (String)
      
      
      
        —
        

Template string for page number wording. Should include ‘<page>` and, optionally, `<total>`.

      
    
  
    
- 
      
        options
      
      
        (Hash{Symbol => any})
      
      
        *(defaults to: {})*
      
      
        —
        

A hash for page numbering and text box options.

      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :page_filter
          (Object)
          
            
          
          
            — 

A filter to specify which pages to place page numbers on. Refer to the method #page_match?

          
        
      
        
- 
          :start_count_at
          (Integer)
          
            
          
          
            — 

The starting count to increment pages from.

          
        
      
        
- 
          :total_pages
          (Integer)
          
            
          
          
            — 

If provided, will replace ‘<total>` with the value given. Useful to override the total number of pages when using the start_count_at option.

          
        
      
        
- 
          :color
          (String, Array<Number>)
          
            
          
          
            — 

Text fill color.

          
        
      
    

  

  
    
      

```

652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
```

    
    
      

```
# File 'lib/prawn/document.rb', line 652

def number_pages(string, options = {})
  opts = options.dup
  start_count_at = opts.delete(:start_count_at)

  page_filter =
    if opts.key?(:page_filter)
      opts.delete(:page_filter)
    else
      :all
    end

  total_pages = opts.delete(:total_pages)
  txtcolor = opts.delete(:color)
  # An explicit height so that we can draw page numbers in the margins
  opts[:height] = 50 unless opts.key?(:height)

  start_count = false
  pseudopage = 0
  (1..page_count).each do |p|
    unless start_count
      pseudopage =
        case start_count_at
        when String
          Integer(start_count_at, 10)
        when (1..)
          Integer(start_count_at)
        else
          1
        end
    end
    if page_match?(page_filter, p)
      go_to_page(p)
      # have to use fill_color here otherwise text reverts back to default
      # fill color
      fill_color(txtcolor) unless txtcolor.nil?
      total_pages = page_count if total_pages.nil?
      str = string.gsub('<page>', pseudopage.to_s)
        .gsub('<total>', total_pages.to_s)
      text_box(str, opts)
      start_count = true # increment page count as soon as first match found
    end
    pseudopage += 1 if start_count
  end
end
```

    
  

    
      
  
### 
  
    #**outline**  ⇒ Prawn::Outline 
  

  

  

  
    

Lazily instantiates a Prawn::Outline object for document. This is used as point of entry to methods to build the outline tree for a document’s table of contents.

  

  

Returns:

  
    
- 
      
      
        (Prawn::Outline)
      
      
      
    
  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/prawn/outline.rb', line 12

def outline
  @outline ||= Outline.new(self)
end
```

    
  

    
      
  
### 
  
    #**pad**(y) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Moves down the document by y, executes a block, then moves down the document by y again.

  

  
  
    
#### Examples:

    
      
      

```
pdf.text "some text"
pdf.pad(100) do
  pdf.text "This is 100 points below the previous line of text"
end
pdf.text "This is 100 points below the previous line of text"
```

    
  

Parameters:

  
    
- 
      
        y
      
      
        (Number)
      
      
      
    
  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

  
    
      

```

592
593
594
595
596
```

    
    
      

```
# File 'lib/prawn/document.rb', line 592

def pad(y)
  move_down(y)
  yield
  move_down(y)
end
```

    
  

    
      
  
### 
  
    #**pad_bottom**(y) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Executes a block then moves down the document

  

  
  
    
#### Examples:

    
      
      

```
pdf.text "some text"
pdf.pad_bottom(100) do
  pdf.text "This text appears right below the previous line of text"
end
pdf.text "This is 100 points below the previous line of text"
```

    
  

Parameters:

  
    
- 
      
        y
      
      
        (Number)
      
      
      
    
  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

  
    
      

```

574
575
576
577
```

    
    
      

```
# File 'lib/prawn/document.rb', line 574

def pad_bottom(y)
  yield
  move_down(y)
end
```

    
  

    
      
  
### 
  
    #**pad_top**(y) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Moves down the document and then executes a block.

  

  
  
    
#### Examples:

    
      
      

```
pdf.text "some text"
pdf.pad_top(100) do
  pdf.text "This is 100 points below the previous line of text"
end
pdf.text "This text appears right below the previous line of text"
```

    
  

Parameters:

  
    
- 
      
        y
      
      
        (Number)
      
      
      
    
  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

  
    
      

```

557
558
559
560
```

    
    
      

```
# File 'lib/prawn/document.rb', line 557

def pad_top(y)
  move_down(y)
  yield
end
```

    
  

    
      
  
### 
  
    #**page**  ⇒ Object 
  

  

  

  
    
      

```

781
782
783
```

    
    
      

```
# File 'lib/prawn/document.rb', line 781

def page
  state.page
end
```

    
  

    
      
  
### 
  
    #**page_count**  ⇒ Integer 
  

  

  

  
    

Number of pages in the document.

  

  
  
    
#### Examples:

    
      
      

```
pdf = Prawn::Document.new
pdf.page_count #=> 1
3.times { pdf.start_new_page }
pdf.page_count #=> 4
```

    
  

Returns:

  
    
- 
      
      
        (Integer)
      
      
      
    
  

  
    
      

```

386
387
388
```

    
    
      

```
# File 'lib/prawn/document.rb', line 386

def page_count
  state.page_count
end
```

    
  

    
      
  
### 
  
    #**page_match?**(page_filter, page_number)  ⇒ Boolean 
  

  

  

  
    

Provides a way to execute a block of code repeatedly based on a page_filter.

Available page filters are:

```
:all         repeats on every page
:odd         repeats on odd pages

```

  

  

Parameters:

  
    
- 
      
        page_filter
      
      
        (:all, :odd, :even, Array<Number>, Range, Proc)
      
      
      
        —
        

  - 

`:all`: repeats on every page

  - 

`:odd`: repeats on odd pages

  - 

`:even`: repeats on even pages

  - 

array: repeats on every page listed in the array

  - 

range: repeats on every page included in the range

  - 

lambda: yields page number and repeats for true return values

      
    
  
    
- 
      
        page_number
      
      
        (Integer)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

733
734
735
736
737
738
739
740
741
742
743
744
745
746
```

    
    
      

```
# File 'lib/prawn/document.rb', line 733

def page_match?(page_filter, page_number)
  case page_filter
  when :all
    true
  when :odd
    page_number.odd?
  when :even
    page_number.even?
  when Range, Array
    page_filter.include?(page_number)
  when Proc
    page_filter.call(page_number)
  end
end
```

    
  

    
      
  
### 
  
    #**reference_bounds**  ⇒ Prawn::Document::BoundingBox 
  

  

  

  
    

Returns the innermost non-stretchy bounding box.

  

  

Returns:

  
    
- 
      
      
        (Prawn::Document::BoundingBox)
      
      
      
    
  

  
    
      

```

512
513
514
```

    
    
      

```
# File 'lib/prawn/document.rb', line 512

def reference_bounds
  @bounding_box.reference_bounds
end
```

    
  

    
      
  
### 
  
    #**render**(output = nil)  ⇒ String 
  

  

  

  
    

Renders the PDF document to string. Pass an open file descriptor to render to file.

  

  
  
  
    

  

  

Parameters:

  
    
- 
      
        output
      
      
        (#<<)
      
      
        *(defaults to: nil)*
      
      
    
  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

456
457
458
459
460
461
462
463
```

    
    
      

```
# File 'lib/prawn/document.rb', line 456

def render(*arguments)
  (1..page_count).each do |i|
    go_to_page(i)
    repeaters.each { |r| r.run(i) }
  end

  renderer.render(*arguments)
end
```

    
  

    
      
  
### 
  
    #**render_file**(filename)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Renders the PDF document to file.

  

  
  
    
#### Examples:

    
      
      

```
pdf.render_file "foo.pdf"
```

    
  

Parameters:

  
    
- 
      
        filename
      
      
        (String)
      
      
      
    
  

  
    
      

```

472
473
474
```

    
    
      

```
# File 'lib/prawn/document.rb', line 472

def render_file(filename)
  File.open(filename, 'wb') { |f| render(f) }
end
```

    
  

    
      
  
### 
  
    #**repeat**(page_filter, options = {}, &block)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Provides a way to execute a block of code repeatedly based on a `page_filter`. Since Stamp is used under the hood, this method is very space efficient.

Also accepts an optional second argument for dynamic content which executes the code in the context of the filtered pages without using a Stamp.

  

  
  
    
#### Examples:

    
      
      

```
Prawn::Document.generate("repeat.pdf", skip_page_creation: true) do
  repeat :all do
    draw_text "ALLLLLL", at: bounds.top_left
  end

  repeat :odd do
    draw_text "ODD", at: [0, 0]
  end

  repeat :even do
    draw_text "EVEN", at: [0, 0]
  end

  repeat [1, 2] do
    draw_text "[1, 2]", at: [100, 0]
  end

  repeat 2..4 do
    draw_text "2..4", at: [200, 0]
  end

  repeat(lambda { |pg| pg % 3 == 0 }) do
    draw_text "Every third", at: [250, 20]
  end

  10.times do
    start_new_page
    draw_text "A wonderful page", at: [400, 400]
  end

  repeat(:all, dynamic: true) do
    text page_number, at: [500, 0]
  end
end
```

    
  

Parameters:

  
    
- 
      
        page_filter
      
      
        (:all, :odd, :even, Array<Integer>, Range, Proc)
      
      
      
        —
        

Pages to draw the repeater content on.

Available page filters are:

  - 

`:all` – repeats on every page.

  - 

`:odd` – repeats on odd pages.

  - 

`:even` – repeats on even pages.

  - 

Array of Integers – repeats on every page listed in the array.

  - 

Range – repeats on every page included in the range.

  - 

Proc – yields page number and repeats for true return values.

      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :dynamic
          (Boolean)
          
            
              — default:
              false
            
          
          
            — 

A dynamic repeater executes block on every matched page. A static repeater uses Stamp#stamp to prepare the content (runs the block once) and puts it on every matched page.

          
        
      
    

  
    
    

  
    
      

```

77
78
79
80
81
82
```

    
    
      

```
# File 'lib/prawn/repeater.rb', line 77

def repeat(page_filter, options = {}, &block)
  dynamic = options.fetch(:dynamic, false)
  repeaters << Prawn::Repeater.new(
    self, page_filter, dynamic, &block
  )
end
```

    
  

    
      
  
### 
  
    #**repeaters**  ⇒ Array 
  

  

  

  
    

A list of all repeaters in the document. See #repeat for details.

  

  

Returns:

  
    
- 
      
      
        (Array)
      
      
      
    
  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/prawn/repeater.rb', line 10

def repeaters
  @repeaters ||= []
end
```

    
  

    
      
  
### 
  
    #**save_font** { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Saves the current font, and then yields. When the block finishes, the original font is restored.

  

  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

  
    
      

```

255
256
257
258
259
260
261
262
263
```

    
    
      

```
# File 'lib/prawn/font.rb', line 255

def save_font
  @font ||= find_font('Helvetica')
  original_font = @font
  original_size = @font_size

  yield
ensure
  set_font(original_font, original_size) if original_font
end
```

    
  

    
      
  
### 
  
    #**set_font**(font, size = nil)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Sets the font directly, given an actual Font object and size.

  

  

Parameters:

  
    
- 
      
        font
      
      
        (Font)
      
      
      
    
  
    
- 
      
        size
      
      
        (Number)
      
      
        *(defaults to: nil)*
      
      
    
  

  
    
      

```

245
246
247
248
```

    
    
      

```
# File 'lib/prawn/font.rb', line 245

def set_font(font, size = nil)
  @font = font
  @font_size = size if size
end
```

    
  

    
      
  
### 
  
    #**span**(width, options = {}) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

A span is a special purpose bounding box that allows a column of elements to be positioned relative to the margin_box.

This method is typically used for flowing a column of text from one page to the next.

  

  
  
    
#### Examples:

    
      
      

```
span(350, position: :center) do
  text "Here's some centered text in a 350 point column. " * 100
end
```

    
  

Parameters:

  
    
- 
      
        width
      
      
        (Number)
      
      
      
        —
        

The width of the column in PDF points

      
    
  
    
- 
      
        options
      
      
        (Hash{Symbol => any })
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :position
          (:left, :center, :right, Number)
          
            
          
          
            — 

position of the span relative to the page margins.

          
        
      
    

  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

Raises:

  
    
- 
      
      
        (ArgumentError)
      
      
      
        —
        

For unsupported `:position` value.

      
    
  

  
    
      

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
55
56
57
58
59
60
61
62
63
```

    
    
      

```
# File 'lib/prawn/document/span.rb', line 31

def span(width, options = {})
  Prawn.verify_options([:position], options)
  original_position = y

  # FIXME: Any way to move this upstream?
  left_boundary =
    case options.fetch(:position, :left)
    when :left
      margin_box.absolute_left
    when :center
      margin_box.absolute_left + (margin_box.width / 2.0) - (width / 2.0)
    when :right
      margin_box.absolute_right - width
    when Numeric
      margin_box.absolute_left + options[:position]
    else
      raise ArgumentError, 'Invalid option for :position'
    end

  # we need to bust out of whatever nested bounding boxes we're in.
  canvas do
    bounding_box(
      [
        left_boundary,
        margin_box.absolute_top,
      ],
      width: width,
    ) do
      self.y = original_position
      yield
    end
  end
end
```

    
  

    
      
  
### 
  
    #**start_new_page**(options = {})  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Creates and advances to a new page in the document.

Page size, margins, and layout can also be set when generating a new page. These values will become the new defaults for page creation.

  

  
  
    
#### Examples:

    
      
      

```
pdf.start_new_page #=> Starts new page keeping current values
pdf.start_new_page(size: "LEGAL", :layout => :landscape)
pdf.start_new_page(left_margin: 50, right_margin: 50)
pdf.start_new_page(margin: 100)
```

    
  

Parameters:

  
    
- 
      
        options
      
      
        (Hash)
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    

Options Hash (options):
    

      
        
- 
          :margins
          (Hash{:left, :right, :top, :bottom => Number}, nil)
          
            
              — default:
              { left: 0, right: 0, top: 0, bottom: 0 }
            
          
          
            — 

Page margins

          
        
      
        
- 
          :crop
          (Hash{:left, :right, :top, :bottom => Number}, nil)
          
            
              — default:
              PDF::Core::Page::ZERO_INDENTS
            
          
          
            — 

Page crop box

          
        
      
        
- 
          :bleed
          (Hash{:left, :right, :top, :bottom => Number}, nil)
          
            
              — default:
              PDF::Core::Page::ZERO_INDENTS
            
          
          
            — 

Page bleed box

          
        
      
        
- 
          :trims
          (Hash{:left, :right, :top, :bottom => Number}, nil)
          
            
              — default:
              PDF::Core::Page::ZERO_INDENTS
            
          
          
            — 

Page trim box

          
        
      
        
- 
          :art_indents
          (Hash{:left, :right, :top, :bottom => Number}, nil)
          
            
              — default:
              PDF::Core::Page::ZERO_INDENTS
            
          
          
            — 

Page art box indents.

          
        
      
        
- 
          :graphic_state
          (PDF::Core::GraphicState, nil)
          
            
              — default:
              nil
            
          
          
            — 

Initial graphic state

          
        
      
        
- 
          :size
          (String, Array<Number>, nil)
          
            
              — default:
              'LETTER'
            
          
          
            — 

Page size. A string identifies a named page size defined in `PDF::Core::PageGeometry`. An array must be a two element array specifying width and height in points.

          
        
      
        
- 
          :layout
          (:portrait, :landscape, nil)
          
            
              — default:
              :portrait
            
          
          
            — 

Page orientation.

          
        
      
    

  

  
    
      

```

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
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
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
348
349
350
351
352
```

    
    
      

```
# File 'lib/prawn/document.rb', line 299

def start_new_page(options = {})
  last_page = state.page
  if last_page
    last_page_size = last_page.size
    last_page_layout = last_page.layout
    last_page_margins = last_page.margins.dup
  end

  page_options = {
    size: options[:size] || last_page_size,
    layout: options[:layout] || last_page_layout,
    margins: last_page_margins,
  }
  if last_page
    if last_page.graphic_state
      new_graphic_state = last_page.graphic_state.dup
    end

    # erase the color space so that it gets reset on new page for fussy
    # pdf-readers
    new_graphic_state&.color_space = {}

    page_options[:graphic_state] = new_graphic_state
  end

  state.page = PDF::Core::Page.new(self, page_options)

  apply_margin_options(options)
  generate_margin_box

  # Reset the bounding box if the new page has different size or layout
  if last_page && (last_page.size != state.page.size ||
                   last_page.layout != state.page.layout)
    @bounding_box = @margin_box
  end

  use_graphic_settings

  unless options[:orphan]
    state.insert_page(state.page, @page_number)
    @page_number += 1

    if @background
      canvas do
        image(@background, scale: @background_scale, at: bounds.top_left)
      end
    end
    @y = @bounding_box.absolute_top

    float do
      state.on_page_create_action(self)
    end
  end
end
```

    
  

    
      
  
### 
  
    #**transaction**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

709
710
711
712
713
714
715
```

    
    
      

```
# File 'lib/prawn/document.rb', line 709

def transaction
  raise NotImplementedError,
    'Document#transaction has been disabled because its implementation ' \
      'lead to corrupted documents whenever a page boundary was ' \
      'crossed. We will try to work on reimplementing it in a ' \
      'future release'
end
```

    
  

    
      
  
### 
  
    #**width_of**(string, options = {})  ⇒ Number 
  

  

  

  
    

Returns the width of the given string using the given font. If `:size` is not specified as one of the options, the string is measured using the current font size. You can also pass `:kerning` as an option to indicate whether kerning should be used when measuring the width (defaults to `false`).

Note that the string *must* be encoded properly for the font being used. For AFM fonts, this is WinAnsi. For TTF/OTF, make sure the font is encoded as UTF-8. You can use the Font#normalize_encoding method to make sure strings are in an encoding appropriate for the current font.

  

  

Parameters:

  
    
- 
      
        string
      
      
        (String)
      
      
      
    
  
    
- 
      
        options
      
      
        (Hash{Symbol => any})
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :inline_format
          (Boolean)
          
            
              — default:
              false
            
          
          
        
      
        
- 
          :kerning
          (Boolean)
          
            
              — default:
              false
            
          
          
        
      
        
- 
          :style
          (Symbol)
          
            
          
          
        
      
    

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

150
151
152
153
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
```

    
    
      

```
# File 'lib/prawn/font.rb', line 150

def width_of(string, options = {})
  if options.key?(:inline_format)
    p = options[:inline_format]
    p = [] unless p.is_a?(Array)

    # Build up an Arranger with the entire string on one line, finalize it,
    # and find its width.
    arranger = Prawn::Text::Formatted::Arranger.new(self, options)
    arranger.consumed = text_formatter.format(string, *p)
    arranger.finalize_line

    arranger.line_width
  else
    width_of_string(string, options)
  end
end
```