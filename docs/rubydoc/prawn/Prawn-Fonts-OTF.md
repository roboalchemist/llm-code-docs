# Class: Prawn::Fonts::OTF
  
  
  

  
  
    Inherits:
    
      TTF
      
        

          
- Object
          
            
- Prawn::Font
          
            
- TTF
          
            
- Prawn::Fonts::OTF
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/fonts/otf.rb
  
  

## Overview

  
    
  
    **Note:**
    

You shouldn’t use this class directly.

  

OpenType font. This class is used mostly to distinguish OTF from TTF. All functionality is in the TTF class.

  

  

  
## Constant Summary

  
  
### Constants inherited
     from Prawn::Font

  

Prawn::Font::AFM, Prawn::Font::DFont, Prawn::Font::TTC, Prawn::Font::TTF

  
## Instance Attribute Summary

  
  
### Attributes inherited from TTF

  

#subsets, #ttf

  
  
  
### Attributes inherited from Prawn::Font

  

#family, #name, #options

  
  
  
  
  
  
  
## Method Summary

  
  
### Methods inherited from TTF

  

#basename, #bbox, #cap_height, #character_count, #compute_width_of, #encode_text, #family_class, #glyph_present?, #has_kerning_data?, #initialize, #italic_angle, #normalize_encoding, #pdf_flags, #script?, #serif?, #stem_v, #to_utf8, #unicode?, #x_height

  
  
  
  
  
  
  
  
  
### Methods inherited from Prawn::Font

  

#add_to_current_page, #ascender, #descender, #eql?, font_format, #hash, #height, #height_at, #identifier_for, #initialize, #inspect, #line_gap, load, #normalize_encoding, #normalize_encoding!

  
## Constructor Details

  
    

This class inherits a constructor from Prawn::Fonts::TTF