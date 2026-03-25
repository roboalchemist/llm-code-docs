# Module: Prawn
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn.rb,

  lib/prawn/font.rb,
 lib/prawn/grid.rb,
 lib/prawn/text.rb,
 lib/prawn/view.rb,
 lib/prawn/fonts.rb,
 lib/prawn/stamp.rb,
 lib/prawn/errors.rb,
 lib/prawn/images.rb,
 lib/prawn/outline.rb,
 lib/prawn/version.rb,
 lib/prawn/document.rb,
 lib/prawn/encoding.rb,
 lib/prawn/graphics.rb,
 lib/prawn/repeater.rb,
 lib/prawn/security.rb,
 lib/prawn/text/box.rb,
 lib/prawn/fonts/afm.rb,
 lib/prawn/fonts/otf.rb,
 lib/prawn/fonts/ttc.rb,
 lib/prawn/fonts/ttf.rb,
 lib/prawn/soft_mask.rb,
 lib/prawn/utilities.rb,
 lib/prawn/images/jpg.rb,
 lib/prawn/images/png.rb,
 lib/prawn/fonts/dfont.rb,
 lib/prawn/images/image.rb,
 lib/prawn/measurements.rb,
 lib/prawn/document/span.rb,
 lib/prawn/graphics/dash.rb,
 lib/prawn/image_handler.rb,
 lib/prawn/graphics/color.rb,
 lib/prawn/text/formatted.rb,
 lib/prawn/font_metric_cache.rb,
 lib/prawn/graphics/patterns.rb,
 lib/prawn/document/internals.rb,
 lib/prawn/graphics/cap_style.rb,
 lib/prawn/text/formatted/box.rb,
 lib/prawn/document/column_box.rb,
 lib/prawn/graphics/blend_mode.rb,
 lib/prawn/graphics/join_style.rb,
 lib/prawn/text/formatted/wrap.rb,
 lib/prawn/transformation_stack.rb,
 lib/prawn/document/bounding_box.rb,
 lib/prawn/fonts/to_unicode_cmap.rb,
 lib/prawn/graphics/transparency.rb,
 lib/prawn/text/formatted/parser.rb,
 lib/prawn/graphics/transformation.rb,
 lib/prawn/text/formatted/arranger.rb,
 lib/prawn/text/formatted/fragment.rb,
 lib/prawn/text/formatted/line_wrap.rb

  
  

## Overview

  
    

text/formatted/rectangle.rb : Implements text boxes with formatted text

Copyright February 2010, Daniel Nelson. All Rights Reserved.

This is free software. Please see the LICENSE and COPYING files for details.

  

  

## Defined Under Namespace

  
    
      **Modules:** Encoding, Errors, Fonts, Graphics, Images, Measurements, SoftMask, Stamp, Text, TransformationStack, View
    
  
    
      **Classes:** Document, Font, FontMetricCache, ImageHandler, Outline, Repeater, SynchronizedCache
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        BASEDIR =
          
  
    

The base source directory for Prawn as installed on the system.

  

  

        
        

```
File.expand_path(File.join(dir, '..'))

```

      
        DATADIR =
          
  
    

Directory where Prawn keeps its data files.

  

  

        
        

```
File.expand_path(File.join(dir, '..', 'data'))

```

      
        FLOAT_PRECISION =
          
  
    **Deprecated.** 

This is not used any more.

  

  

        
        

```
1.0e-9

```

      
        VERSION =
          
  
    

Prawn versions

  

  

        
        

```
'2.5.0'

```

      
    
  

  
    
## 
      Extension API
      collapse
    

    

      
        
- 
  
    
      .**image_handler**  ⇒ ImageHandler 
    

    
  
  
  
  
  
  
  
  

  
    

Image handler.

  

      
    

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**debug**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

When set to `true`, Prawn will verify hash options to ensure only valid keys are used.

  

      
        
- 
  
    
      .**debug=**(value)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

When set to `true`, Prawn will verify hash options to ensure only valid keys are used.

  

      
        
- 
  
    
      .**verify_options**(accepted, actual) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**debug**  ⇒ Boolean 
  

  

  

  
    

When set to `true`, Prawn will verify hash options to ensure only valid keys are used. Off by default.

Example:

“‘shell >> Prawn::Document.new(:tomato => “Juicy”) Prawn::Errors::UnknownOption: Detected unknown option(s): [:tomato] Accepted options are: [:page_size, :page_layout, :left_margin, …] “`

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

38
39
40
```

    
    
      

```
# File 'lib/prawn.rb', line 38

def debug
  @debug
end

```

    
  

    
      
  
### 
  
    .**debug=**(value)  ⇒ Boolean 
  

  

  

  
    

When set to `true`, Prawn will verify hash options to ensure only valid keys are used. Off by default.

Example:

“‘shell >> Prawn::Document.new(:tomato => “Juicy”) Prawn::Errors::UnknownOption: Detected unknown option(s): [:tomato] Accepted options are: [:page_size, :page_layout, :left_margin, …] “`

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

38
39
40
```

    
    
      

```
# File 'lib/prawn.rb', line 38

def debug=(value)
  @debug = value
end

```

    
  

    
      
  
### 
  
    .**image_handler**  ⇒ ImageHandler 
  

  

  

  
    

Image handler.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

9
10
11
```

    
    
      

```
# File 'lib/prawn/image_handler.rb', line 9

def self.image_handler
  @image_handler ||= ImageHandler.new
end

```

    
  

    
      
  
### 
  
    .**verify_options**(accepted, actual) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

  

  

Parameters:

  
    
- 
      
      
      
      
        
        

list of valid options

      
    
  
    
- 
      
      
      
      
        
        

opetions hash to validate

      
    
  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

Raises:

  
    
- 
      
      
      
      
    
  

  
    
      

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
```

    
    
      

```
# File 'lib/prawn.rb', line 50

def verify_options(accepted, actual)
  return unless debug || $DEBUG

  unless (act = Set[*actual.keys]).subset?(acc = Set[*accepted])
    raise Prawn::Errors::UnknownOption,
      "\nDetected unknown option(s): #{(act - acc).to_a.inspect}\nAccepted options are: #{accepted.inspect}"
  end
  yield if block_given?
end

```