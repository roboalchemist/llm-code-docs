# Class: Pod::Generator::Constant
  
    Inherits:
    
      Object
      
        

          
- Object

- Pod::Generator::Constant

        show all
      

    Defined in:
    lib/cocoapods/generator/constant.rb
  
## Overview

Generates a constant file.

## Instance Attribute Summary collapse

-
  
      #**generate**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute generate.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(contents)  ⇒ Constant 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Constant.

-
  
      #**save_as**(path)  ⇒ Object 

## Constructor Details

###
  
    #**initialize**(contents)  ⇒ Constant 
  

  

  

  
    

Returns a new instance of Constant.

```

6
7
8
```

```
# File 'lib/cocoapods/generator/constant.rb', line 6

def initialize(contents)
  @generate = contents
end

```

## Instance Attribute Details

###
  
    #**generate**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute generate.

```

10
11
12
```

```
# File 'lib/cocoapods/generator/constant.rb', line 10

def generate
  @generate
end

```

## Instance Method Details

###
  
    #**save_as**(path)  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
15
16
```

```
# File 'lib/cocoapods/generator/constant.rb', line 12

def save_as(path)
  path.open('w') do |f|
    f.write(generate)
  end
end

```
