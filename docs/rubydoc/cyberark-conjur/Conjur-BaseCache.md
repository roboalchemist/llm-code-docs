# Class: Conjur::BaseCache
  
    Inherits:
    
      Object
      
        

          
- Object

- Conjur::BaseCache

        show all
      

    Defined in:
    lib/conjur/cache.rb
  
## Overview

A cache which performs no caching.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**fetch_attributes**(cache_key, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

###
  
    #**fetch_attributes**(cache_key, &block)  ⇒ Object 
  

  

  

  
    
      

```

4
5
6
```

```
# File 'lib/conjur/cache.rb', line 4

def fetch_attributes cache_key, &block
  yield
end
```
