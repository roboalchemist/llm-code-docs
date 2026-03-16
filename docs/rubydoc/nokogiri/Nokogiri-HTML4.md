# Module: Nokogiri::HTML4
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/html4.rb,

  lib/nokogiri/html4/builder.rb,
 lib/nokogiri/html4/document.rb,
 lib/nokogiri/html4/sax/parser.rb,
 lib/nokogiri/html4/entity_lookup.rb,
 lib/nokogiri/html4/encoding_reader.rb,
 lib/nokogiri/html4/sax/push_parser.rb,
 lib/nokogiri/html4/document_fragment.rb,
 lib/nokogiri/html4/sax/parser_context.rb,
 lib/nokogiri/html4/element_description.rb,
 lib/nokogiri/html4/element_description_defaults.rb,
 ext/nokogiri/nokogiri.c

  
  

## Overview

  
    

Since v1.12.0

💡 Before v1.12.0, Nokogiri::HTML4 did not exist, and Nokogiri::HTML was the module/namespace for parsing HTML.

  

  

## Defined Under Namespace

  
    
      **Modules:** SAX
    
  
    
      **Classes:** Builder, Document, DocumentFragment, ElementDescription, EncodingReader, EntityDescription, EntityLookup
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        NamedCharacters =
          
  
    

Instance of Nokogiri::HTML4::EntityLookup

  

  

        
        

```
EntityLookup.new

```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**fragment**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convenience method for Nokogiri::HTML4::DocumentFragment.parse.

  

      
        
- 
  
    
      .**parse**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convenience method for Nokogiri::HTML4::Document.parse.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**fragment**  ⇒ Object 
  

  

  

  
    

Convenience method for Nokogiri::HTML4::DocumentFragment.parse

  

  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/nokogiri/html4.rb', line 24

def fragment(...)
  HTML4::DocumentFragment.parse(...)
end

```

    
  

    
      
  
### 
  
    .**parse**  ⇒ Object 
  

  

  

  
    

Convenience method for Nokogiri::HTML4::Document.parse

  

  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/nokogiri/html4.rb', line 19

def parse(...)
  Document.parse(...)
end

```