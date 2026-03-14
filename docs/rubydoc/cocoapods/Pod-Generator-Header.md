# Class: Pod::Generator::Header
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::Generator::Header
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/generator/header.rb
  
  

## Overview

  
    

Generates a header file.

According to the platform the header imports `UIKit/UIKit.h` or `Cocoa/Cocoa.h`.

  

  

  
## Direct Known Subclasses

  

PrefixHeader, UmbrellaHeader

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**imports**  ⇒ Array<String> 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

The list of the headers to import.

  

    
      
- 
  
    
      #**module_imports**  ⇒ Array<String> 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The list of the modules to import.

  

    
      
- 
  
    
      #**platform**  ⇒ Symbol 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The platform for which the prefix header will be generated.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**generate**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Generates the contents of the header according to the platform.

  

      
        
- 
  
    
      #**initialize**(platform)  ⇒ Header 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize a new instance.

  

      
        
- 
  
    
      #**save_as**(path)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Generates and saves the header to the given path.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(platform)  ⇒ Header 
  

  

  

  
    

Initialize a new instance

  

  

Parameters:

  
    
- 
      
        platform
      
      
        (Symbol)
      
      
      
        —
        

@see platform

      
    
  

  
    
      

```

27
28
29
30
31
```

    
    
      

```
# File 'lib/cocoapods/generator/header.rb', line 27

def initialize(platform)
  @platform = platform
  @imports = []
  @module_imports = []
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**imports**  ⇒ Array<String> 
  

  

  

  
    

Returns The list of the headers to import.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
        —
        

The list of the headers to import.

      
    
  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/cocoapods/generator/header.rb', line 16

def imports
  @imports
end

```

    
  

    
      
      
      
  
### 
  
    #**module_imports**  ⇒ Array<String>  (readonly)
  

  

  

  
    

Returns The list of the modules to import.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
        —
        

The list of the modules to import.

      
    
  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/cocoapods/generator/header.rb', line 20

def module_imports
  @module_imports
end

```

    
  

    
      
      
      
  
### 
  
    #**platform**  ⇒ Symbol  (readonly)
  

  

  

  
    

Returns the platform for which the prefix header will be generated.

  

  

Returns:

  
    
- 
      
      
        (Symbol)
      
      
      
        —
        

the platform for which the prefix header will be generated.

      
    
  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/cocoapods/generator/header.rb', line 12

def platform
  @platform
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**generate**  ⇒ String 
  

  

  

  
    
  
    **Note:**
    

If the platform is iOS an import call to `UIKit/UIKit.h` is added to the top of the prefix header. For OS X `Cocoa/Cocoa.h` is imported.

  

Generates the contents of the header according to the platform.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
```

    
    
      

```
# File 'lib/cocoapods/generator/header.rb', line 41

def generate
  result = ''
  result << "#ifdef __OBJC__\n"
  result << generate_platform_import_header
  result << "#else\n"
  result << "#ifndef FOUNDATION_EXPORT\n"
  result << "#if defined(__cplusplus)\n"
  result << "#define FOUNDATION_EXPORT extern \"C\"\n"
  result << "#else\n"
  result << "#define FOUNDATION_EXPORT extern\n"
  result << "#endif\n"
  result << "#endif\n"
  result << "#endif\n"
  result << "\n"

  imports.each do |import|
    result << %(#import "#{import}"\n)
  end

  unless module_imports.empty?
    module_imports.each do |import|
      result << %(\n@import #{import})
    end
    result << "\n"
  end

  result
end

```

    
  

    
      
  
### 
  
    #**save_as**(path)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Generates and saves the header to the given path.

  

  

Parameters:

  
    
- 
      
        path
      
      
        (Pathname)
      
      
      
        —
        

The path where the header should be stored.

      
    
  

  
    
      

```

77
78
79
```

    
    
      

```
# File 'lib/cocoapods/generator/header.rb', line 77

def save_as(path)
  path.open('w') { |header| header.write(generate) }
end

```