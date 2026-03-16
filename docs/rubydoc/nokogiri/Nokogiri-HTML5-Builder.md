# Class: Nokogiri::HTML5::Builder
  
  
  

  
  
    Inherits:
    
      XML::Builder
      
        

          
- Object
          
            
- XML::Builder
          
            
- Nokogiri::HTML5::Builder
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/html5/builder.rb
  
  

## Overview

  
    

Nokogiri HTML5 builder is used for building HTML documents. It is very similar to the Nokogiri::XML::Builder.  In fact, you should go read the documentation for Nokogiri::XML::Builder before reading this documentation.

The construction behavior is identical to HTML4::Builder, but HTML5 documents implement the [HTML5 standard’s serialization algorithm](www.w3.org/TR/2008/WD-html5-20080610/serializing.html).

## Synopsis:

Create an HTML5 document with a body that has an onload attribute, and a span tag with a class of “bold” that has content of “Hello world”.

```
builder = Nokogiri::HTML5::Builder.new do |doc|
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

The HTML5 builder inherits from the XML builder, so make sure to read the Nokogiri::XML::Builder documentation.

  

  

  
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

35
36
37
```

    
    
      

```
# File 'lib/nokogiri/html5/builder.rb', line 35

def to_html
  @doc.to_html
end
```