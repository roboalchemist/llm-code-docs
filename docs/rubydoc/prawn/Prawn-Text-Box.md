# Class: Prawn::Text::Box
  
  
  

  
  
    Inherits:
    
      Formatted::Box
      
        

          
- Object
          
            
- Formatted::Box
          
            
- Prawn::Text::Box
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/text/box.rb
  
  

## Overview

  
    

Text box.

Generally, one would use the #text_box convenience method. However, using Box.new in conjunction with ‘render(dry_run: true)` enables one to do calculations prior to placing text on the page, or to determine how much vertical space was consumed by the printed text.

  

  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Formatted::Box

  

#ascender, #at, #descender, #leading, #line_height, #text

  
    
## 
      Experimental API
      collapse
    

    

      
        
- 
  
    
      #**initialize**(string, options = {})  ⇒ Box 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Box.

  

      
        
- 
  
    
      #**render**(flags = {})  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Render text to the document based on the settings defined in constructor.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Formatted::Box

  

#available_width, #draw_fragment, #everything_printed?, extensions, #height, inherited, #line_gap, #nothing_printed?, #valid_options

  
  
  
  
  
  
  
  
  
### Methods included from Formatted::Wrap

  

#wrap

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(string, options = {})  ⇒ Box 
  

  

  

  
    

Returns a new instance of Box.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  
    
- 
      
      
      
        *(defaults to: {})*
      
      
    
  
    
- 
      
      
      
      
        
        

a customizable set of options

      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :document
          (Prawn::Document)
          
            
          
          
            — 

Owning document.

          
        
      
        
- 
          :kerning
          (Boolean)
          
            
              — default:
              value of document.default_kerning?
            
          
          
            — 

Whether or not to use kerning (if it is available with the current font).

          
        
      
        
- 
          :size
          (Number)
          
            
              — default:
              current font size
            
          
          
            — 

The font size to use.

          
        
      
        
- 
          :character_spacing
          (Number)
          
            
              — default:
              0
            
          
          
            — 

The amount of space to add to or remove from the default character spacing.

          
        
      
        
- 
          :disable_wrap_by_char
          (Boolean)
          
            
              — default:
              false
            
          
          
            — 

Whether or not to prevent mid-word breaks when text does not fit in box.

          
        
      
        
- 
          :mode
          (Symbol)
          
            
              — default:
              :fill
            
          
          
            — 

The text rendering mode. See documentation for Document#text_rendering_mode for a list of valid options.

          
        
      
        
- 
          :width
          (Number)
          
            
              — default:
              bounds.right - at[0]
            
          
          
            — 

The width of the box.

          
        
      
        
- 
          :height
          (Number)
          
            
              — default:
              default_height()
            
          
          
            — 

The height of the box.

          
        
      
        
- 
          :direction
          (:ltr, :rtl)
          
            
              — default:
              value of document.text_direction
            
          
          
            — 

Direction of the text (left-to-right or right-to-left).

          
        
      
        
- 
          :fallback_fonts
          (Array<String>)
          
            
          
          
            — 

An array of font names. Each name must be the name of an AFM font or the name that was used to register a family of external fonts (see Document#font_families). If present, then each glyph will be rendered using the first font that includes the glyph, starting with the current font and then moving through `:fallback_fonts`.

          
        
      
        
- 
          :align
          (:left, :center, :right, :justify)
          
            
              — default:
              :left if direction is :ltr, :right if direction is :rtl
            
          
          
            — 

Alignment within the bounding box.

          
        
      
        
- 
          :valign
          (:top, :center, :bottom)
          
            
              — default:
              :top
            
          
          
            — 

Vertical alignment within the bounding box.

          
        
      
        
- 
          :rotate
          (Number)
          
            
          
          
            — 

The angle to rotate the text.

          
        
      
        
- 
          :rotate_around
          (Object)
          
            
          
          
            — :center, :upper_left, :upper_right, :lower_right, :lower_left

(:upper_left) The point around which to rotate the text.

          
        
      
        
- 
          :leading
          (Number)
          
            
              — default:
              value of document.default_leading
            
          
          
            — 

Additional space between lines.

          
        
      
        
- 
          :single_line
          (Boolean)
          
            
              — default:
              false
            
          
          
            — 

If true, then only the first line will be drawn.

          
        
      
        
- 
          :overflow
          (:truncate, :shrink_to_fit, :expand)
          
            
              — default:
              :truncate
            
          
          
            — 

This controls the behavior when the amount of text exceeds the available space.

          
        
      
        
- 
          :min_font_size
          (Number)
          
            
              — default:
              5
            
          
          
            — 

The minimum font size to use when `:overflow` is set to `:shrink_to_fit` (that is the font size will not be reduced to less than this value, even if it means that some text will be cut off).

          
        
      
    

  

  
    
      

```

165
166
167
```

    
    
      

```
# File 'lib/prawn/text/box.rb', line 165

def initialize(string, options = {})
  super([{ text: string }], options)
end

```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**render**(flags = {})  ⇒ String 
  

  

  

  
    

Render text to the document based on the settings defined in constructor.

In order to facilitate look-ahead calculations, this method accepts a ‘dry_run: true` option. If provided, then everything is executed as if rendering, with the exception that nothing is drawn on the page.  Useful for look-ahead computations of height, unprinted text, etc.

  

  

Parameters:

  
    
- 
      
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    

Options Hash (flags):
    

      
        
- 
          :dry_run
          (Boolean)
          
            
              — default:
              false
            
          
          
            — 

Do not draw the text. Everything else is done.

          
        
      
    

  

Returns:

  
    
- 
      
      
      
      
        
        

Any text that did not print under the current settings.

      
    
  

Raises:

  
    
- 
      
      
      
      
        
        

If no font family is defined for the current font.

      
    
  
    
- 
      
      
      
      
        
        

If not wide enough to print any text.

      
    
  

  
    
      

```

186
187
188
189
```

    
    
      

```
# File 'lib/prawn/text/box.rb', line 186

def render(flags = {})
  leftover = super(flags)
  leftover.map { |hash| hash[:text] }.join
end

```