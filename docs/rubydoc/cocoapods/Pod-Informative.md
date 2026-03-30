# Class: Pod::Informative
  
    Inherits:
    
      PlainInformative
      
        

          
- Object

- PlainInformative

- Pod::Informative

        show all
      

    Defined in:
    lib/cocoapods.rb
  
## Overview

Indicates an user error. This is defined in cocoapods-core.

## Direct Known Subclasses

NoSpecFoundError

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  

  
    
## Instance Method Details

###
  
    #**message**  ⇒ Object 
  

  

  

  
    
      

```

37
38
39
```

```
# File 'lib/cocoapods.rb', line 37

def message
  "[!] #{super}".red
end
```
