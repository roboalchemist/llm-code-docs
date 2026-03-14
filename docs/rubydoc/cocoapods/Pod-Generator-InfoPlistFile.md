# Class: Pod::Generator::InfoPlistFile
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::Generator::InfoPlistFile
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/generator/info_plist_file.rb
  
  

## Overview

  
    

Generates Info.plist files. A Info.plist file is generated for each Pod and for each Pod target definition, that requires to be built as framework. It states public attributes.

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**additional_entries**  ⇒ Hash 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Any additional entries to include in this Info.plist.

  

    
      
- 
  
    
      #**bundle_package_type**  ⇒ Symbol 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The CFBundlePackageType of the target this Info.plist file is for.

  

    
      
- 
  
    
      #**platform**  ⇒ Platform 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The platform to use for when generating this Info.plist file.

  

    
      
- 
  
    
      #**version**  ⇒ String 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Version The version to use for when generating this Info.plist file.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**generate**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Generates the contents of the Info.plist.

  

      
        
- 
  
    
      #**initialize**(version, platform, bundle_package_type = :fmwk, additional_entries = {})  ⇒ InfoPlistFile 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize a new instance.

  

      
        
- 
  
    
      #**save_as**(path)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Generates and saves the Info.plist to the given path.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(version, platform, bundle_package_type = :fmwk, additional_entries = {})  ⇒ InfoPlistFile 
  

  

  

  
    

Initialize a new instance

  

  

Parameters:

  
    
- 
      
        version
      
      
        (String)
      
      
      
        —
        

@see #version

      
    
  
    
- 
      
        platform
      
      
        (Platform)
      
      
      
        —
        

@see #platform

      
    
  
    
- 
      
        bundle_package_type
      
      
        (Symbol)
      
      
        *(defaults to: :fmwk)*
      
      
        —
        

@see #bundle_package_type

      
    
  
    
- 
      
        additional_entries
      
      
        (Hash)
      
      
        *(defaults to: {})*
      
      
        —
        

@see #additional_entries

      
    
  

  
    
      

```

32
33
34
35
36
37
```

    
    
      

```
# File 'lib/cocoapods/generator/info_plist_file.rb', line 32

def initialize(version, platform, bundle_package_type = :fmwk, additional_entries = {})
  @version = version
  @platform = platform
  @bundle_package_type = bundle_package_type
  @additional_entries = additional_entries
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**additional_entries**  ⇒ Hash  (readonly)
  

  

  

  
    

Returns any additional entries to include in this Info.plist.

  

  

Returns:

  
    
- 
      
      
        (Hash)
      
      
      
        —
        

any additional entries to include in this Info.plist

      
    
  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/cocoapods/generator/info_plist_file.rb', line 23

def additional_entries
  @additional_entries
end
```

    
  

    
      
      
      
  
### 
  
    #**bundle_package_type**  ⇒ Symbol  (readonly)
  

  

  

  
    

Returns the CFBundlePackageType of the target this Info.plist file is for.

  

  

Returns:

  
    
- 
      
      
        (Symbol)
      
      
      
        —
        

the CFBundlePackageType of the target this Info.plist file is for.

      
    
  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/cocoapods/generator/info_plist_file.rb', line 19

def bundle_package_type
  @bundle_package_type
end
```

    
  

    
      
      
      
  
### 
  
    #**platform**  ⇒ Platform  (readonly)
  

  

  

  
    

Returns The platform to use for when generating this Info.plist file.

  

  

Returns:

  
    
- 
      
      
        (Platform)
      
      
      
        —
        

The platform to use for when generating this Info.plist file.

      
    
  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/cocoapods/generator/info_plist_file.rb', line 14

def platform
  @platform
end
```

    
  

    
      
      
      
  
### 
  
    #**version**  ⇒ String  (readonly)
  

  

  

  
    

Returns version The version to use for when generating this Info.plist file.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

version The version to use for when generating this Info.plist file.

      
    
  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/cocoapods/generator/info_plist_file.rb', line 10

def version
  @version
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**generate**  ⇒ String 
  

  

  

  
    

Generates the contents of the Info.plist

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

57
58
59
```

    
    
      

```
# File 'lib/cocoapods/generator/info_plist_file.rb', line 57

def generate
  to_plist(info)
end
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

46
47
48
49
50
51
```

    
    
      

```
# File 'lib/cocoapods/generator/info_plist_file.rb', line 46

def save_as(path)
  contents = generate
  path.open('w') do |f|
    f.write(contents)
  end
end
```