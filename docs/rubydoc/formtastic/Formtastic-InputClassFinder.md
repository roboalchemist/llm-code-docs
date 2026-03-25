# Class: Formtastic::InputClassFinder
  
  
  

  
  
    Inherits:
    
      NamespacedClassFinder
      
        

          
- Object
          
            
- NamespacedClassFinder
          
            
- Formtastic::InputClassFinder
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/formtastic/input_class_finder.rb
  
  

## Overview

  
    

Uses the NamespacedClassFinder to look up input class names.

See FormBuilder#namespaced_input_class for details.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**class_name**(as)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(builder)  ⇒ InputClassFinder 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of InputClassFinder.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from NamespacedClassFinder

  

#find, finder_method, #resolve, use_const_defined?

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(builder)  ⇒ InputClassFinder 
  

  

  

  
    

Returns a new instance of InputClassFinder.

  

  

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
# File 'lib/formtastic/input_class_finder.rb', line 11

def initialize(builder)
  super builder.input_namespaces
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
# File 'lib/formtastic/input_class_finder.rb', line 15

def class_name(as)
  "#{super}Input"
end
```