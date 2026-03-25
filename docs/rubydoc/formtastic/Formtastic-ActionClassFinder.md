# Class: Formtastic::ActionClassFinder
  
  
  

  
  
    Inherits:
    
      NamespacedClassFinder
      
        

          
- Object
          
            
- NamespacedClassFinder
          
            
- Formtastic::ActionClassFinder
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/formtastic/action_class_finder.rb
  
  

## Overview

  
    

Uses the NamespacedClassFinder to look up action class names.

See Helpers::ActionHelper#namespaced_action_class for details.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**class_name**(as)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(builder)  ⇒ ActionClassFinder 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ActionClassFinder.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from NamespacedClassFinder

  

#find, finder_method, #resolve, use_const_defined?

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(builder)  ⇒ ActionClassFinder 
  

  

  

  
    

Returns a new instance of ActionClassFinder.

  

  

Parameters:

  
    
- 
      
        builder
      
      
        (FormBuilder)
      
      
      
    
  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/formtastic/action_class_finder.rb', line 11

def initialize(builder)
  super builder.action_namespaces
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**class_name**(as)  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/formtastic/action_class_finder.rb', line 15

def class_name(as)
  "#{super}Action"
end
```