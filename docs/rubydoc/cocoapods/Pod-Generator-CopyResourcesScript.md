# Class: Pod::Generator::CopyResourcesScript
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::Generator::CopyResourcesScript
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/generator/copy_resources_script.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**platform**  ⇒ Platform 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The platform of the library for which the copy resources script is needed.

  

    
      
- 
  
    
      #**resources_by_config**  ⇒ Hash{String, Array{String}] A list of files relative to the project pods root, keyed by build configuration. 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

HashArray{String] A list of files relative to the project pods root, keyed by build configuration.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**generate**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The contents of the copy resources script.

  

      
        
- 
  
    
      #**initialize**(resources_by_config, platform)  ⇒ CopyResourcesScript 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize a new instance.

  

      
        
- 
  
    
      #**save_as**(pathname)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Saves the resource script to the given pathname.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(resources_by_config, platform)  ⇒ CopyResourcesScript 
  

  

  

  
    

Initialize a new instance

  

  

Parameters:

  
    
- 
      
      
      
      
        
        

@see resources_by_config

      
    
  
    
- 
      
      
      
      
        
        

@see platform

      
    
  

  
    
      

```

22
23
24
25
```

    
    
      

```
# File 'lib/cocoapods/generator/copy_resources_script.rb', line 22

def initialize(resources_by_config, platform)
  @resources_by_config = resources_by_config
  @platform = platform
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**platform**  ⇒ Platform  (readonly)
  

  

  

  
    

Returns The platform of the library for which the copy resources script is needed.

  

  

Returns:

  
    
- 
      
      
      
      
        
        

The platform of the library for which the copy resources script is needed.

      
    
  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/cocoapods/generator/copy_resources_script.rb', line 12

def platform
  @platform
end

```

    
  

    
      
      
      
  
### 
  
    #**resources_by_config**  ⇒ Hash{String, Array{String}] A list of files relative to the
project pods root, keyed by build configuration.  (readonly)
  

  

  

  
    

Returns HashArray{String] A list of files relative to the project pods root, keyed by build configuration.

  

  

Returns:

  
    
- 
      
      
      
      
        
        

HashArray{String] A list of files relative to the project pods root, keyed by build configuration.

      
    
  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/cocoapods/generator/copy_resources_script.rb', line 7

def resources_by_config
  @resources_by_config
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**generate**  ⇒ String 
  

  

  

  
    

Returns The contents of the copy resources script.

  

  

Returns:

  
    
- 
      
      
      
      
        
        

The contents of the copy resources script.

      
    
  

  
    
      

```

43
44
45
```

    
    
      

```
# File 'lib/cocoapods/generator/copy_resources_script.rb', line 43

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
      
      
      
      
        
        

The path where the copy resources script should be saved.

      
    
  

  
    
      

```

34
35
36
37
38
39
```

    
    
      

```
# File 'lib/cocoapods/generator/copy_resources_script.rb', line 34

def save_as(pathname)
  pathname.open('w') do |file|
    file.puts(script)
  end
  File.chmod(0755, pathname.to_s)
end

```