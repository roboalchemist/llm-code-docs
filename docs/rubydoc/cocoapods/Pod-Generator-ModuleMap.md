# Class: Pod::Generator::ModuleMap
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::Generator::ModuleMap
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/generator/module_map.rb
  
  

## Overview

  
    

Generates LLVM module map files. A module map file is generated for each Pod and for each Pod target definition that is built as a framework. It specifies a different umbrella header than usual to avoid name conflicts with existing headers of the podspec.

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** Header
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**headers**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute headers.

  

    
      
- 
  
    
      #**target**  ⇒ PodTarget, AggregateTarget 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The target the module map is generated for.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**generate**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Generates the contents of the module.modulemap file.

  

      
        
- 
  
    
      #**initialize**(target)  ⇒ ModuleMap 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize a new instance.

  

      
        
- 
  
    
      #**save_as**(path)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Generates and saves the Info.plist to the given path.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(target)  ⇒ ModuleMap 
  

  

  

  
    

Initialize a new instance

  

  

Parameters:

  
    
- 
      
        target
      
      
        (PodTarget, AggregateTarget)
      
      
      
        —
        

@see target

      
    
  

  
    
      

```

43
44
45
46
47
48
```

    
    
      

```
# File 'lib/cocoapods/generator/module_map.rb', line 43

def initialize(target)
  @target = target
  @headers = [
    Header.new(target.umbrella_header_path.basename, true),
  ]
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**headers**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute headers.

  

  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/cocoapods/generator/module_map.rb', line 13

def headers
  @headers
end

```

    
  

    
      
      
      
  
### 
  
    #**target**  ⇒ PodTarget, AggregateTarget  (readonly)
  

  

  

  
    

Returns the target the module map is generated for.

  

  

Returns:

  
    
- 
      
      
        (PodTarget, AggregateTarget)
      
      
      
        —
        

the target the module map is generated for.

      
    
  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/cocoapods/generator/module_map.rb', line 11

def target
  @target
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**generate**  ⇒ String 
  

  

  

  
    

Generates the contents of the module.modulemap file.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

68
69
70
71
72
73
74
75
76
77
```

    
    
      

```
# File 'lib/cocoapods/generator/module_map.rb', line 68

def generate
  "\#{module_specifier_prefix}module \#{target.product_module_name}\#{module_declaration_attributes} {\n  \#{headers.join(\"\\n  \")}\n\n  export *\n  module * { export * }\n}\n  MODULE_MAP\nend\n".strip_heredoc

```

    
  

    
      
  
### 
  
    #**save_as**(path)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Generates and saves the Info.plist to the given path.

  

  

Parameters:

  
    
- 
      
        path
      
      
        (Pathname)
      
      
      
        —
        

the path where the prefix header should be stored.

      
    
  

  
    
      

```

57
58
59
60
61
62
```

    
    
      

```
# File 'lib/cocoapods/generator/module_map.rb', line 57

def save_as(path)
  contents = generate
  path.open('w') do |f|
    f.write(contents)
  end
end

```