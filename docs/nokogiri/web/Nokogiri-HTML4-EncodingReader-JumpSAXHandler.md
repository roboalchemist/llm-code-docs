# Class: Nokogiri::HTML4::EncodingReader::JumpSAXHandler
  
  
  

  
  
    Inherits:
    
      SAXHandler
      
        

          
- Object
          
            
- XML::SAX::Document
          
            
- SAXHandler
          
            
- Nokogiri::HTML4::EncodingReader::JumpSAXHandler
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/html4/encoding_reader.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from SAXHandler

  

#encoding

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(jumptag)  ⇒ JumpSAXHandler 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of JumpSAXHandler.

  

      
        
- 
  
    
      #**start_element**(name, attrs = [])  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods inherited from XML::SAX::Document

  

#cdata_block, #characters, #comment, #end_document, #end_element, #end_element_namespace, #error, #processing_instruction, #reference, #start_document, #start_element_namespace, #warning, #xmldecl

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(jumptag)  ⇒ JumpSAXHandler 
  

  

  

  
    

Returns a new instance of JumpSAXHandler.

  

  

  
    
      

```

47
48
49
50
```

    
    
      

```
# File 'lib/nokogiri/html4/encoding_reader.rb', line 47

def initialize(jumptag)
  @jumptag = jumptag
  super()
end

```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**start_element**(name, attrs = [])  ⇒ Object 
  

  

  

  
    
      

```

52
53
54
55
56
```

    
    
      

```
# File 'lib/nokogiri/html4/encoding_reader.rb', line 52

def start_element(name, attrs = [])
  super
  throw(@jumptag, @encoding) if @encoding
  throw(@jumptag, nil) if /\A(?:div|h1|img|p|br)\z/.match?(name)
end

```