# Module: Nokogiri::CSS::XPathVisitor::DoctypeConfig
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/css/xpath_visitor.rb
  
  

## Overview

  
    

Enum to direct XPathVisitor when to tweak the XPath query to suit the nature of the document being searched. Note that searches for CSS selectors from a Nokogiri document, fragment, or node will choose the correct option automatically.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        XML =
          
  
    

The document being searched is an XML document. This is the default.

  

  

        
        

```
:xml
```

      
        HTML4 =
          
  
    

The document being searched is an HTML4 document.

  

  

        
        

```
:html4
```

      
        HTML5 =
          
  
    

The document being searched is an HTML5 document.

  

  

        
        

```
:html5
```

      
        VALUES =
          
  
    

:nodoc: array of values for validation

  

  

        
        

```
[XML, HTML4, HTML5]
```