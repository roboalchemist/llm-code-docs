# Class: Pod::Generator::BridgeSupport
  
    Inherits:
    
      Object
      
        

          
- Object

- Pod::Generator::BridgeSupport

        show all
      
    
  
  

  
  
  
      Extended by:
      Executable
  
    Defined in:
    lib/cocoapods/generator/bridge_support.rb
  
## Instance Attribute Summary collapse

-
  
      #**headers**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute headers.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(headers)  ⇒ BridgeSupport 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of BridgeSupport.

-
  
      #**save_as**(pathname)  ⇒ Object 

-
  
      #**search_paths**  ⇒ Object 

### Methods included from Executable

capture_command, capture_command!, executable, execute_command, which, which!

## Constructor Details

###
  
    #**initialize**(headers)  ⇒ BridgeSupport 
  

  

  

  
    

Returns a new instance of BridgeSupport.

```

9
10
11
```

```
# File 'lib/cocoapods/generator/bridge_support.rb', line 9

def initialize(headers)
  @headers = headers
end
```

## Instance Attribute Details

###
  
    #**headers**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute headers.

```

7
8
9
```

```
# File 'lib/cocoapods/generator/bridge_support.rb', line 7

def headers
  @headers
end
```

## Instance Method Details

###
  
    #**save_as**(pathname)  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
```

```
# File 'lib/cocoapods/generator/bridge_support.rb', line 17

def save_as(pathname)
  gen_bridge_metadata('-c', search_paths.join(' '), '-o', pathname, *headers)
end
```

###
  
    #**search_paths**  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
```

```
# File 'lib/cocoapods/generator/bridge_support.rb', line 13

def search_paths
  @headers.map { |header| "-I '#{header.dirname}'" }.uniq
end
```
