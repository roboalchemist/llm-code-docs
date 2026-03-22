# Class: Prawn::Fonts::DFont
  
  
  

  
  
    Inherits:
    
      TTF
      
        

          
- Object
          
            
- Prawn::Font
          
            
- TTF
          
            
- Prawn::Fonts::DFont
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/fonts/dfont.rb
  
  

## Overview

  
    
  
    **Note:**
    

You shouldn’t use this class directly.

  

DFONT font. DFONT is a bunch of TrueType fonts in a single file.

  

  

  
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
  
    
      .**font_count**(file)  ⇒ Integer 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the number of fonts contained in the dfont file.

  

      
        
- 
  
    
      .**named_fonts**(file)  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

Returns a list of the names of all named fonts in the given dfont file.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from TTF

  

#basename, #bbox, #cap_height, #character_count, #compute_width_of, #encode_text, #family_class, #glyph_present?, #has_kerning_data?, #initialize, #italic_angle, #normalize_encoding, #pdf_flags, #script?, #serif?, #stem_v, #to_utf8, #unicode?, #x_height

  
  
  
  
  
  
  
  
  
### Methods inherited from Prawn::Font

  

#add_to_current_page, #ascender, #descender, #eql?, font_format, #hash, #height, #height_at, #identifier_for, #initialize, #inspect, #line_gap, load, #normalize_encoding, #normalize_encoding!

  
## Constructor Details

  
    

This class inherits a constructor from Prawn::Fonts::TTF
  

  
    
## Class Method Details

    
      
  
### 
  
    .**font_count**(file)  ⇒ Integer 
  

  

  

  
    

Returns the number of fonts contained in the dfont file.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

29
30
31
32
33
```

    
    
      

```
# File 'lib/prawn/fonts/dfont.rb', line 29

def self.font_count(file)
  TTFunk::ResourceFile.open(file) do |f|
    return f.map['sfnt'][:list].length
  end
end
```

    
  

    
      
  
### 
  
    .**named_fonts**(file)  ⇒ Array<String> 
  

  

  

  
    

Returns a list of the names of all named fonts in the given dfont file. Note that fonts are not required to be named in a dfont file, so the list may be empty even if the file does contain fonts. Also, note that the list is returned in no particular order, so the first font in the list is not necessarily the font at index 0 in the file.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

19
20
21
22
23
```

    
    
      

```
# File 'lib/prawn/fonts/dfont.rb', line 19

def self.named_fonts(file)
  TTFunk::ResourceFile.open(file) do |f|
    return f.resources_for('sfnt')
  end
end
```