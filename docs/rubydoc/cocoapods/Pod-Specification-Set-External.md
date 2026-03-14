# Class: Pod::Specification::Set::External
  
    Inherits:
    
      Object
      
        

          
- Object

- Pod::Specification::Set::External

        show all
      

    Defined in:
    lib/cocoapods/resolver/lazy_specification.rb
  
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**all_specifications**(_warn_for_multiple_pod_sources, requirement)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

###
  
    #**all_specifications**(_warn_for_multiple_pod_sources, requirement)  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
48
49
50
51
```

```
# File 'lib/cocoapods/resolver/lazy_specification.rb', line 45

def all_specifications(_warn_for_multiple_pod_sources, requirement)
  if requirement.satisfied_by? specification.version
    [specification]
  else
    []
  end
end
```
