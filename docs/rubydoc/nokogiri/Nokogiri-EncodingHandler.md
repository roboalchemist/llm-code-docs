# Class: Nokogiri::EncodingHandler
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Nokogiri::EncodingHandler
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/encoding_handler.rb,

  ext/nokogiri/xml_encoding_handler.c

  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        USEFUL_ALIASES =
          
  
    

Popular encoding aliases not known by all iconv implementations that Nokogiri should support.

  

  

        
        

```
{
  # alias_name => true_name
  "ISO-2022-JP" => "ISO-2022-JP", # only for JRuby tests, this is a no-op in CRuby
  "NOKOGIRI-SENTINEL" => "ISO-2022-JP", # indicating the Nokogiri has installed aliases
  "Windows-31J" => "CP932", # Windows-31J is the IANA registered name of CP932.
}

```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**name**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Get the name of this EncodingHandler.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**Nokogiri::EncodingHandler.[]**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the encoding handler for `name`.

  

      
        
- 
  
    
      .**Nokogiri::EncodingHandler.alias**(real_name, alias_name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Alias encoding handler with name `real_name` to name `alias_name`.

  

      
        
- 
  
    
      .**Nokogiri::EncodingHandler.clear_aliases!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Remove all encoding aliases.

  

      
        
- 
  
    
      .**Nokogiri::EncodingHandler.delete**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Delete the encoding alias named `name`.

  

      
        
- 
  
    
      .**install_default_aliases**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(name)  ⇒ EncodingHandler 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of EncodingHandler.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name)  ⇒ EncodingHandler 
  

  

  

  
    

Returns a new instance of EncodingHandler.

  

  

  
    
      

```

48
49
50
```

    
    
      

```
# File 'lib/nokogiri/encoding_handler.rb', line 48

def initialize(name)
  @name = name
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**name**  ⇒ Object  (readonly)
  

  

  

  
    

Get the name of this EncodingHandler

  

  
  

  
    
      

```

88
89
90
```

    
    
      

```
# File 'ext/nokogiri/xml_encoding_handler.c', line 88

def name
  @name
end

```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**Nokogiri::EncodingHandler.[]**(name)  ⇒ Object 
  

  

  

  
    

Get the encoding handler for `name`

  

  
  

  
    
      

```

27
28
29
```

    
    
      

```
# File 'ext/nokogiri/xml_encoding_handler.c', line 27

def [](name)
  storage.key?(name) ? new(storage[name]) : nil
end

```

    
  

    
      
  
### 
  
    .**Nokogiri::EncodingHandler.alias**(real_name, alias_name)  ⇒ Object 
  

  

  

  
    

Alias encoding handler with name `real_name` to name `alias_name`

  

  
  

  
    
      

```

60
61
62
```

    
    
      

```
# File 'ext/nokogiri/xml_encoding_handler.c', line 60

def alias(name, alias_name)
  storage[alias_name] = name
end

```

    
  

    
      
  
### 
  
    .**Nokogiri::EncodingHandler.clear_aliases!**  ⇒ Object 
  

  

  

  
    

Remove all encoding aliases.

  

  
  

  
    
      

```

74
75
76
```

    
    
      

```
# File 'ext/nokogiri/xml_encoding_handler.c', line 74

def clear_aliases!
  storage.clear
end

```

    
  

    
      
  
### 
  
    .**Nokogiri::EncodingHandler.delete**(name)  ⇒ Object 
  

  

  

  
    

Delete the encoding alias named `name`

  

  
  

  
    
      

```

46
47
48
```

    
    
      

```
# File 'ext/nokogiri/xml_encoding_handler.c', line 46

def delete(name)
  storage.delete(name)
end

```

    
  

    
      
  
### 
  
    .**install_default_aliases**  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
18
19
```

    
    
      

```
# File 'lib/nokogiri/encoding_handler.rb', line 15

def install_default_aliases
  USEFUL_ALIASES.each do |alias_name, name|
    EncodingHandler.alias(name, alias_name) if EncodingHandler[alias_name].nil?
  end
end

```