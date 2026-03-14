# Class: Pod::Generator::FileList
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::Generator::FileList
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/generator/file_list.rb
  
  

## Overview

  
    

Generates an xcfilelist file.

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**paths**  ⇒ Array<String> 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The paths of the files in the file list.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**generate**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Generates the contents of the file list.

  

      
        
- 
  
    
      #**initialize**(paths)  ⇒ FileList 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize a new instance.

  

      
        
- 
  
    
      #**save_as**(path)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Generates and saves the file list to the given path.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(paths)  ⇒ FileList 
  

  

  

  
    

Initialize a new instance

  

  

Parameters:

  
    
- 
      
      
      
      
        
        

@see paths

      
    
  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/cocoapods/generator/file_list.rb', line 15

def initialize(paths)
  @paths = paths
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**paths**  ⇒ Array<String>  (readonly)
  

  

  

  
    

Returns The paths of the files in the file list.

  

  

Returns:

  
    
- 
      
      
      
      
        
        

The paths of the files in the file list.

      
    
  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/cocoapods/generator/file_list.rb', line 8

def paths
  @paths
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**generate**  ⇒ String 
  

  

  

  
    

Generates the contents of the file list.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/cocoapods/generator/file_list.rb', line 23

def generate
  paths.join("\n")
end
```

    
  

    
      
  
### 
  
    #**save_as**(path)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Generates and saves the file list to the given path.

  

  

Parameters:

  
    
- 
      
      
      
      
        
        

The path where the file list should be stored.

      
    
  

  
    
      

```

34
35
36
```

    
    
      

```
# File 'lib/cocoapods/generator/file_list.rb', line 34

def save_as(path)
  path.open('w') { |file_list| file_list.write(generate) }
end
```