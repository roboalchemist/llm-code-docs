# Class: SimpleForm::Wrappers::Root
  
  
  

  
  
    Inherits:
    
      Many
      
        

          
- Object
          
            
- Many
          
            
- SimpleForm::Wrappers::Root
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/simple_form/wrappers/root.rb
  
  

## Overview

  
    

`Root` is the root wrapper for all components. It is special cased to always have a namespace and to add special html classes.

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**options**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute options.

  

    
  

  
  
  
### Attributes inherited from Many

  

#components, #defaults, #namespace

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**find**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Provide a fallback if name cannot be found.

  

      
        
- 
  
    
      #**initialize**(*args)  ⇒ Root 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Root.

  

      
        
- 
  
    
      #**render**(input)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(*args)  ⇒ Root 
  

  

  

  
    

Returns a new instance of Root.

  

  

  
    
      

```

9
10
11
12
```

    
    
      

```
# File 'lib/simple_form/wrappers/root.rb', line 9

def initialize(*args)
  super(:wrapper, *args)
  @options = @defaults.except(:tag, :class, :error_class, :hint_class)
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**options**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute options.

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/simple_form/wrappers/root.rb', line 7

def options
  @options
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**find**(name)  ⇒ Object 
  

  

  

  
    

Provide a fallback if name cannot be found.

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/simple_form/wrappers/root.rb', line 20

def find(name)
  super || SimpleForm::Wrappers::Many.new(name, [Leaf.new(name)])
end
```

    
  

    
      
  
### 
  
    #**render**(input)  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
17
```

    
    
      

```
# File 'lib/simple_form/wrappers/root.rb', line 14

def render(input)
  input.options.reverse_merge!(@options)
  super
end
```