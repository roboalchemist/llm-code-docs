# Class: Prawn::FontMetricCache
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Prawn::FontMetricCache
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/font_metric_cache.rb
  
  

## Overview

  
    

Cache used internally by Document instances to calculate the width of various strings for layout purposes.

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** CacheEntry
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(document)  ⇒ FontMetricCache 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of FontMetricCache.

  

      
        
- 
  
    
      #**width_of**(string, options)  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Get width of string.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(document)  ⇒ FontMetricCache 
  

  

  

  
    

Returns a new instance of FontMetricCache.

  

  

  
    
      

```

11
12
13
14
15
```

    
    
      

```
# File 'lib/prawn/font_metric_cache.rb', line 11

def initialize(document)
  @document = document

  @cache = {}
end

```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**width_of**(string, options)  ⇒ Number 
  

  

  

  
    

Get width of string.

  

  

Parameters:

  
    
- 
      
        string
      
      
        (String)
      
      
      
    
  
    
- 
      
        options
      
      
        (Hash{Symbol => any})
      
      
      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :style
          (Symbol)
          
            
          
          
        
      
        
- 
          :size
          (Number)
          
            
          
          
        
      
        
- 
          :kerning
          (Boolean)
          
            
              — default:
              false
            
          
          
        
      
    

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

25
26
27
28
29
30
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
```

    
    
      

```
# File 'lib/prawn/font_metric_cache.rb', line 25

def width_of(string, options)
  f =
    if options[:style]
      # override style with :style => :bold
      @document.find_font(@document.font.family, style: options[:style])
    else
      @document.font
    end

  encoded_string = f.normalize_encoding(string)

  key = CacheEntry.new(f, @document.font_size, options, encoded_string)

  @cache[key] ||= f.compute_width_of(encoded_string, options)

  length = @cache[key]

  character_count = @document.font.character_count(encoded_string)
  if character_count.positive?
    length += @document.character_spacing * (character_count - 1)
  end

  length
end

```