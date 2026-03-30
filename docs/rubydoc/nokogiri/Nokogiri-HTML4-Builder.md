# Class: Nokogiri::HTML4::Builder
  
  
  

  
  
    Inherits:
    
      XML::Builder
      
        

          
- Object
          
            
- XML::Builder
          
            
- Nokogiri::HTML4::Builder
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/html4/builder.rb
  
  

## Overview

  
    

Nokogiri HTML builder is used for building HTML documents.  It is very similar to the Nokogiri::XML::Builder.  In fact, you should go read the documentation for Nokogiri::XML::Builder before reading this documentation.

## Synopsis:

Create an HTML document with a body that has an onload attribute, and a span tag with a class of “bold” that has content of “Hello world”.

```
builder = Nokogiri::HTML4::Builder.new do |doc|
  doc.html {
    doc.body(:onload => 'some_func();') {
      doc.span.bold {
        doc.text "Hello world"
      }
    }
  }
end
puts builder.to_html

```

The HTML builder inherits from the XML builder, so make sure to read the Nokogiri::XML::Builder documentation.

  

  

  
## Constant Summary

  
  
### Constants inherited
     from XML::Builder

  

XML::Builder::DEFAULT_DOCUMENT_OPTIONS

  
  
  
### Constants included
     from ClassResolver

  

ClassResolver::VALID_NAMESPACES

  
## Instance Attribute Summary

  
  
### Attributes inherited from XML::Builder

  

#arity, #context, #doc, #parent

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**to_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convert the builder to HTML.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from XML::Builder

  

#<<, #[], #cdata, #comment, #initialize, #method_missing, #text, #to_xml, with

  
  
  
  
  
  
  
  
  
### Methods included from ClassResolver

  

#related_class

  
## Constructor Details

  
    

This class inherits a constructor from Nokogiri::XML::Builder
  

  
## Dynamic Method Handling

  

    This class handles dynamic methods through the method_missing method
    
      in the class Nokogiri::XML::Builder
    
  
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**to_html**  ⇒ Object 
  

  

  

  
    

Convert the builder to HTML

  

  

  
    
      

```

32
33
34
```

    
    
      

```
# File 'lib/nokogiri/html4/builder.rb', line 32

def to_html
  @doc.to_html
end
```