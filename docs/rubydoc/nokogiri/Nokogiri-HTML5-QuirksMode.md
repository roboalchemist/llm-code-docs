# Module: Nokogiri::HTML5::QuirksMode
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/html5/document.rb
  
  

## Overview

  
    

Enum for the HTML5 parser quirks mode values. Values returned by HTML5::Document#quirks_mode

See dom.spec.whatwg.org/#concept-document-quirks for more information on HTML5 quirks mode.

Since v1.14.0

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        NO_QUIRKS =
          
  
    

The document was parsed in “no-quirks” mode

  

  

        
        

```
0

```

      
        QUIRKS =
          
  
    

The document was parsed in “quirks” mode

  

  

        
        

```
1

```

      
        LIMITED_QUIRKS =
          
  
    

The document was parsed in “limited-quirks” mode

  

  

        
        

```
2

```