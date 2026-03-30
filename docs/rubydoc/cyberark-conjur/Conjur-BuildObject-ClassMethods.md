# Module: Conjur::BuildObject::ClassMethods
  
    Included in:
    RoleGrant
  
  

  
  
    Defined in:
    lib/conjur/build_object.rb
  
  

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**build_object**(id, credentials, default_class:)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**find_class**(class_name, default_class)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

###
  
    #**build_object**(id, credentials, default_class:)  ⇒ Object 
  

  

  

  
    
      

```

26
27
28
29
30
31
```

```
# File 'lib/conjur/build_object.rb', line 26

def build_object id, credentials, default_class:
  id = Id.new id
  class_name = id.kind.classify.to_sym
  find_class(class_name, default_class)
    .new(id, credentials)
end

```

###
  
    #**find_class**(class_name, default_class)  ⇒ Object 
  

  

  

  
    
      

```

33
34
35
36
37
38
39
40
```

```
# File 'lib/conjur/build_object.rb', line 33

def find_class class_name, default_class
  cls = if Conjur.constants.member?(class_name)
    Conjur.const_get(class_name)
  else
    default_class
  end
  cls < BaseObject ? cls : default_class
end

```
