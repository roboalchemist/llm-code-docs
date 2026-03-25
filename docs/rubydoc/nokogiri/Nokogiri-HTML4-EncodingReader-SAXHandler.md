# Class: Nokogiri::HTML4::EncodingReader::SAXHandler
  
  
  

  
  
    Inherits:
    
      XML::SAX::Document
      
        

          
- Object
          
            
- XML::SAX::Document
          
            
- Nokogiri::HTML4::EncodingReader::SAXHandler
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/html4/encoding_reader.rb
  
  

  
## Direct Known Subclasses

  

JumpSAXHandler

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**encoding**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute encoding.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**  ⇒ SAXHandler 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of SAXHandler.

  

      
        
- 
  
    
      #**start_element**(name, attrs = [])  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from XML::SAX::Document

  

#cdata_block, #characters, #comment, #end_document, #end_element, #end_element_namespace, #error, #processing_instruction, #reference, #start_document, #start_element_namespace, #warning, #xmldecl

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ SAXHandler 
  

  

  

  
    

Returns a new instance of SAXHandler.

  

  

  
    
      

```

27
28
29
30
```

    
    
      

```
# File 'lib/nokogiri/html4/encoding_reader.rb', line 27

def initialize
  @encoding = nil
  super
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**encoding**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute encoding.

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/nokogiri/html4/encoding_reader.rb', line 25

def encoding
  @encoding
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**start_element**(name, attrs = [])  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/nokogiri/html4/encoding_reader.rb', line 32

def start_element(name, attrs = [])
  return unless name == "meta"

  attr = Hash[attrs]
  (charset = attr["charset"]) &&
    (@encoding = charset)
  (http_equiv = attr["http-equiv"]) &&
    http_equiv.match(/\AContent-Type\z/i) &&
    (content = attr["content"]) &&
    (m = content.match(/;\s*charset\s*=\s*([\w-]+)/)) &&
    (@encoding = m[1])
end

```