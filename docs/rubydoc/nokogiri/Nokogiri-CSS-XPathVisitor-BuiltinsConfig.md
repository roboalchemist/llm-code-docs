# Module: Nokogiri::CSS::XPathVisitor::BuiltinsConfig
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/css/xpath_visitor.rb
  
  

## Overview

  
    

Enum to direct XPathVisitor when to use Nokogiri builtin XPath functions.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        NEVER =
          
  
    

Never use Nokogiri builtin functions, always generate vanilla XPath 1.0 queries. This is the default when calling Nokogiri::CSS.xpath_for directly.

  

  

        
        

```
:never
```

      
        ALWAYS =
          
  
    

Always use Nokogiri builtin functions whenever possible. This is probably only useful for testing.

  

  

        
        

```
:always
```

      
        OPTIMAL =
          
  
    

Only use Nokogiri builtin functions when they will be faster than vanilla XPath. This is the behavior chosen when searching for CSS selectors on a Nokogiri document, fragment, or node.

  

  

        
        

```
:optimal
```

      
        VALUES =
          
  
    

:nodoc: array of values for validation

  

  

        
        

```
[NEVER, ALWAYS, OPTIMAL]
```