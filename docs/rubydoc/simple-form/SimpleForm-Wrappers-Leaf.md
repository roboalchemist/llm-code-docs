# Class: SimpleForm::Wrappers::Leaf
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- SimpleForm::Wrappers::Leaf
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/simple_form/wrappers/leaf.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**namespace**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute namespace.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**find**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(namespace, options = {})  ⇒ Leaf 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Leaf.

  

      
        
- 
  
    
      #**render**(input)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(namespace, options = {})  ⇒ Leaf 
  

  

  

  
    

Returns a new instance of Leaf.

  

  

  
    
      

```

7
8
9
10
```

    
    
      

```
# File 'lib/simple_form/wrappers/leaf.rb', line 7

def initialize(namespace, options = {})
  @namespace = namespace
  @options = options
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**namespace**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute namespace.

  

  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/simple_form/wrappers/leaf.rb', line 5

def namespace
  @namespace
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**find**(name)  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/simple_form/wrappers/leaf.rb', line 24

def find(name)
  self if @namespace == name
end
```

    
  

    
      
  
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
19
20
21
22
```

    
    
      

```
# File 'lib/simple_form/wrappers/leaf.rb', line 12

def render(input)
  method = input.method(@namespace)

  if method.arity.zero?
    SimpleForm.deprecator.warn(SimpleForm::CUSTOM_INPUT_DEPRECATION_WARN % { name: @namespace })

    method.call
  else
    method.call(@options)
  end
end
```