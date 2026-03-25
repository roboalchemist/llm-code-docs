# Class: SimpleForm::Wrappers::Single
  
  
  

  
  
    Inherits:
    
      Many
      
        

          
- Object
          
            
- Many
          
            
- SimpleForm::Wrappers::Single
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/simple_form/wrappers/single.rb
  
  

## Overview

  
    

`Single` is an optimization for a wrapper that has only one component.

  

  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Many

  

#components, #defaults, #namespace

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(name, wrapper_options = {}, options = {})  ⇒ Single 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Single.

  

      
        
- 
  
    
      #**render**(input)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Many

  

#find

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name, wrapper_options = {}, options = {})  ⇒ Single 
  

  

  

  
    

Returns a new instance of Single.

  

  

  
    
      

```

6
7
8
9
10
```

    
    
      

```
# File 'lib/simple_form/wrappers/single.rb', line 6

def initialize(name, wrapper_options = {}, options = {})
  @component = Leaf.new(name, options)

  super(name, [@component], wrapper_options)
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**render**(input)  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
15
16
17
18
```

    
    
      

```
# File 'lib/simple_form/wrappers/single.rb', line 12

def render(input)
  options = input.options
  if options[namespace] != false
    content = @component.render(input)
    wrap(input, options, content) if content
  end
end
```