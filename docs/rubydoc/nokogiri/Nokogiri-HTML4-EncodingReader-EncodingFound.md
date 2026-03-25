# Exception: Nokogiri::HTML4::EncodingReader::EncodingFound
  
  
  

  
  
    Inherits:
    
      StandardError
      
        

          
- Object
          
            
- StandardError
          
            
- Nokogiri::HTML4::EncodingReader::EncodingFound
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/html4/encoding_reader.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**found_encoding**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute found_encoding.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(encoding)  ⇒ EncodingFound 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of EncodingFound.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(encoding)  ⇒ EncodingFound 
  

  

  

  
    

Returns a new instance of EncodingFound.

  

  

  
    
      

```

18
19
20
21
```

    
    
      

```
# File 'lib/nokogiri/html4/encoding_reader.rb', line 18

def initialize(encoding)
  @found_encoding = encoding
  super(format("encoding found: %s", encoding))
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**found_encoding**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute found_encoding.

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/nokogiri/html4/encoding_reader.rb', line 16

def found_encoding
  @found_encoding
end

```