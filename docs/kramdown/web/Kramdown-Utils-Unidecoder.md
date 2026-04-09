# Module: Kramdown::Utils::Unidecoder
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/utils/unidecoder.rb
  
  

## Overview

  
    

Provides the ability to tranliterate Unicode strings into plain ASCII ones.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        CODEPOINTS =
          
        
        

```
Hash.new do |h, k|
  h[k] = YAML.load_file(File.join(path, "stringex", "unidecoder_data", "#{k}.yml"))
end

```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**decode**(string)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Transliterate string from Unicode into ASCII.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**decode**(string)  ⇒ Object 
  

  

  

  
    

Transliterate string from Unicode into ASCII.

  

  

  
    
      

```

29
30
31
32
33
34
35
36
```

    
    
      

```
# File 'lib/kramdown/utils/unidecoder.rb', line 29

def self.decode(string)
  string.gsub(/[^\x00-\x7f]/u) do |codepoint|
    unpacked = codepoint.unpack1("U")
    CODEPOINTS[sprintf("x%02x", unpacked >> 8)][unpacked & 255]
  rescue StandardError
    "?"
  end
end

```