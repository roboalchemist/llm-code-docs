# Class: Pod::Generator::EmbedFrameworksScript
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::Generator::EmbedFrameworksScript
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/generator/embed_frameworks_script.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**frameworks_by_config**  ⇒ Hash{String => Array<FrameworkPaths>} 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Multiple lists of frameworks per configuration.

  

    
      
- 
  
    
      #**xcframeworks_by_config**  ⇒ Hash{String => Array<XCFrameworkPaths>} 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Multiple lists of frameworks per configuration.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**generate**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The contents of the embed frameworks script.

  

      
        
- 
  
    
      #**initialize**(frameworks_by_config, xcframeworks_by_config)  ⇒ EmbedFrameworksScript 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of EmbedFrameworksScript.

  

      
        
- 
  
    
      #**save_as**(pathname)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Saves the resource script to the given pathname.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(frameworks_by_config, xcframeworks_by_config)  ⇒ EmbedFrameworksScript 
  

  

  

  
    

Returns a new instance of EmbedFrameworksScript.

  

  

Parameters:

  
    
- 
      
      
      
      
        
        

# > Array<FrameworkPaths>] frameworks_by_config

@see #frameworks_by_config

      
    
  
    
- 
      
      
      
      
        
        

# > Array<XCFramework>] xcframeworks_by_config

@see #xcframeworks_by_config

      
    
  

  
    
      

```

22
23
24
25
```

    
    
      

```
# File 'lib/cocoapods/generator/embed_frameworks_script.rb', line 22

def initialize(frameworks_by_config, xcframeworks_by_config)
  @frameworks_by_config = frameworks_by_config
  @xcframeworks_by_config = xcframeworks_by_config
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**frameworks_by_config**  ⇒ Hash{String => Array<FrameworkPaths>}  (readonly)
  

  

  

  
    

Returns Multiple lists of frameworks per configuration.

  

  

Returns:

  
    
- 
      
      
      
      
        
        

Multiple lists of frameworks per configuration.

      
    
  

  
    
      

```

9
10
11
```

    
    
      

```
# File 'lib/cocoapods/generator/embed_frameworks_script.rb', line 9

def frameworks_by_config
  @frameworks_by_config
end

```

    
  

    
      
      
      
  
### 
  
    #**xcframeworks_by_config**  ⇒ Hash{String => Array<XCFrameworkPaths>}  (readonly)
  

  

  

  
    

Returns Multiple lists of frameworks per configuration.

  

  

Returns:

  
    
- 
      
      
      
      
        
        

Multiple lists of frameworks per configuration.

      
    
  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/cocoapods/generator/embed_frameworks_script.rb', line 14

def xcframeworks_by_config
  @xcframeworks_by_config
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**generate**  ⇒ String 
  

  

  

  
    

Returns The contents of the embed frameworks script.

  

  

Returns:

  
    
- 
      
      
      
      
        
        

The contents of the embed frameworks script.

      
    
  

  
    
      

```

43
44
45
```

    
    
      

```
# File 'lib/cocoapods/generator/embed_frameworks_script.rb', line 43

def generate
  script
end

```

    
  

    
      
  
### 
  
    #**save_as**(pathname)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Saves the resource script to the given pathname.

  

  

Parameters:

  
    
- 
      
      
      
      
        
        

The path where the embed frameworks script should be saved.

      
    
  

  
    
      

```

34
35
36
37
38
39
```

    
    
      

```
# File 'lib/cocoapods/generator/embed_frameworks_script.rb', line 34

def save_as(pathname)
  pathname.open('w') do |file|
    file.puts(script)
  end
  File.chmod(0755, pathname.to_s)
end

```