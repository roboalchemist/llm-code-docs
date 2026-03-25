# Class: Prawn::Fonts::TTC
  
  
  

  
  
    Inherits:
    
      TTF
      
        

          
- Object
          
            
- Prawn::Font
          
            
- TTF
          
            
- Prawn::Fonts::TTC
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/fonts/ttc.rb
  
  

## Overview

  
    
  
    **Note:**
    

You shouldn’t use this class directly.

  

TrueType Collection font. It’s an SFNT-based format that contains a bunch of TrueType fonts in a single file.

  

  

  
## Constant Summary

  
  
### Constants inherited
     from Prawn::Font

  

Prawn::Font::AFM, Prawn::Font::DFont, Prawn::Font::TTC, Prawn::Font::TTF

  
## Instance Attribute Summary

  
  
### Attributes inherited from TTF

  

#subsets, #ttf

  
  
  
### Attributes inherited from Prawn::Font

  

#family, #name, #options

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**font_names**(file)  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

Returns a list of the names of all named fonts in the given ttc file.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from TTF

  

#basename, #bbox, #cap_height, #character_count, #compute_width_of, #encode_text, #family_class, #glyph_present?, #has_kerning_data?, #initialize, #italic_angle, #normalize_encoding, #pdf_flags, #script?, #serif?, #stem_v, #to_utf8, #unicode?, #x_height

  
  
  
  
  
  
  
  
  
### Methods inherited from Prawn::Font

  

#add_to_current_page, #ascender, #descender, #eql?, font_format, #hash, #height, #height_at, #identifier_for, #initialize, #inspect, #line_gap, load, #normalize_encoding, #normalize_encoding!

  
## Constructor Details

  
    

This class inherits a constructor from Prawn::Fonts::TTF
  

  
    
## Class Method Details

    
      
  
### 
  
    .**font_names**(file)  ⇒ Array<String> 
  

  

  

  
    

Returns a list of the names of all named fonts in the given ttc file. They are returned in order of their appearance in the file.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

17
18
19
20
21
```

    
    
      

```
# File 'lib/prawn/fonts/ttc.rb', line 17

def self.font_names(file)
  TTFunk::Collection.open(file) do |ttc|
    ttc.map { |font| font.name.font_name.first }
  end
end

```