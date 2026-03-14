# Module: Conjur::BuildObject
  
    Included in:
    API, BaseObject
  
  

  
  
    Defined in:
    lib/conjur/build_object.rb
  
## Defined Under Namespace

      **Modules:** ClassMethods
    
  
    
  

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**build_object**(id, default_class: Resource)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

###
  
    #**build_object**(id, default_class: Resource)  ⇒ Object 
  

  

  

  
    
      

```

43
44
45
```

```
# File 'lib/conjur/build_object.rb', line 43

def build_object id, default_class: Resource
  self.class.build_object id, credentials, default_class: default_class
end
```
