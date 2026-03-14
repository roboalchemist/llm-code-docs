# Class: Jekyll::Drops::CollectionDrop
  
    Inherits:
    
      Drop
      
        

          
- Object

- Liquid::Drop

- Drop

- Jekyll::Drops::CollectionDrop

        show all
      
    
  
  

  
  
  
      Extended by:
      Forwardable
  
    Defined in:
    lib/jekyll/drops/collection_drop.rb
  
## Constant Summary

### Constants inherited

     from Drop

Drop::NON_CONTENT_METHODS

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**to_s**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods inherited from Drop

# [], #[]=, #content_methods, data_delegator, data_delegators, delegate_method, delegate_method_as, delegate_methods, #each, #each_key, #fetch, getter_method_names, #hash_for_json, #initialize, #inspect, #key?, #keys, #merge, #merge!, mutable, mutable?, private_delegate_methods, #to_h, #to_json

## Constructor Details

This class inherits a constructor from Jekyll::Drops::Drop
  
## Instance Method Details

###
  
    #**to_s**  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
```

```
# File 'lib/jekyll/drops/collection_drop.rb', line 15

def to_s
  docs.to_s
end

```
