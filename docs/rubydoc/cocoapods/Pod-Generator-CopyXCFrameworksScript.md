# Class: Pod::Generator::CopyXCFrameworksScript
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::Generator::CopyXCFrameworksScript
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/generator/copy_xcframework_script.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**platform**  ⇒ Platform 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The platform of the target for which this script will run.

  

    
      
- 
  
    
      #**sandbox_root**  ⇒ Pathname 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The root directory of the sandbox.

  

    
      
- 
  
    
      #**xcframeworks**  ⇒ Array<Pod::Xcode::XCFramework> 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

List of xcframeworks to copy.

  

    
  

  
    
## 
      Private Helpers
      collapse
    

    

      
        
- 
  
    
      .**dsym_folder**(xcframework_path)  ⇒ Array<Pathname> 
    

    
  
  
  
  
  
  
  
  

  
    

All found .dSYM paths.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**generate**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The contents of the embed frameworks script.

  

      
        
- 
  
    
      #**initialize**(xcframeworks, sandbox_root, platform)  ⇒ CopyXCFrameworksScript 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Creates a script for copying XCFramework slcies into an intermediate build directory.

  

      
        
- 
  
    
      #**save_as**(pathname)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Saves the resource script to the given pathname.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(xcframeworks, sandbox_root, platform)  ⇒ CopyXCFrameworksScript 
  

  

  

  
    

Creates a script for copying XCFramework slcies into an intermediate build directory

  

  

Parameters:

  
    
- 
      
        xcframeworks
      
      
        (Array<Pod::Xcode::XCFramework>)
      
      
      
        —
        

the list of xcframeworks to copy

      
    
  
    
- 
      
        sandbox_root
      
      
        (Pathname)
      
      
      
        —
        

the root of the Sandbox into which this script will be installed

      
    
  
    
- 
      
        platform
      
      
        (Platform)
      
      
      
        —
        

the platform of the target for which this script will be run

      
    
  

  
    
      

```

29
30
31
32
33
```

    
    
      

```
# File 'lib/cocoapods/generator/copy_xcframework_script.rb', line 29

def initialize(xcframeworks, sandbox_root, platform)
  @xcframeworks = xcframeworks
  @sandbox_root = sandbox_root
  @platform = platform
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**platform**  ⇒ Platform  (readonly)
  

  

  

  
    

Returns the platform of the target for which this script will run.

  

  

Returns:

  
    
- 
      
      
        (Platform)
      
      
      
        —
        

the platform of the target for which this script will run

      
    
  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/cocoapods/generator/copy_xcframework_script.rb', line 16

def platform
  @platform
end
```

    
  

    
      
      
      
  
### 
  
    #**sandbox_root**  ⇒ Pathname  (readonly)
  

  

  

  
    

Returns the root directory of the sandbox.

  

  

Returns:

  
    
- 
      
      
        (Pathname)
      
      
      
        —
        

the root directory of the sandbox

      
    
  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/cocoapods/generator/copy_xcframework_script.rb', line 12

def sandbox_root
  @sandbox_root
end
```

    
  

    
      
      
      
  
### 
  
    #**xcframeworks**  ⇒ Array<Pod::Xcode::XCFramework>  (readonly)
  

  

  

  
    

Returns List of xcframeworks to copy.

  

  

Returns:

  
    
- 
      
      
        (Array<Pod::Xcode::XCFramework>)
      
      
      
        —
        

List of xcframeworks to copy

      
    
  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/cocoapods/generator/copy_xcframework_script.rb', line 8

def xcframeworks
  @xcframeworks
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**dsym_folder**(xcframework_path)  ⇒ Array<Pathname> 
  

  

  

  
    

Returns all found .dSYM paths.

  

  

Parameters:

  
    
- 
      
        xcframework_path
      
      
        (Pathname)
      
      
      
        —
        

the base path of the .xcframework bundle

      
    
  

Returns:

  
    
- 
      
      
        (Array<Pathname>)
      
      
      
        —
        

all found .dSYM paths

      
    
  

  
    
      

```

218
219
220
221
222
223
```

    
    
      

```
# File 'lib/cocoapods/generator/copy_xcframework_script.rb', line 218

def dsym_folder(xcframework_path)
  basename = File.basename(xcframework_path, '.xcframework')
  dsym_basename = basename + '.dSYMs'
  path = xcframework_path.dirname + dsym_basename
  Pathname.new(path) if File.directory?(path)
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**generate**  ⇒ String 
  

  

  

  
    

Returns The contents of the embed frameworks script.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

The contents of the embed frameworks script.

      
    
  

  
    
      

```

51
52
53
```

    
    
      

```
# File 'lib/cocoapods/generator/copy_xcframework_script.rb', line 51

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
      
        pathname
      
      
        (Pathname)
      
      
      
        —
        

The path where the embed frameworks script should be saved.

      
    
  

  
    
      

```

42
43
44
45
46
47
```

    
    
      

```
# File 'lib/cocoapods/generator/copy_xcframework_script.rb', line 42

def save_as(pathname)
  pathname.open('w') do |file|
    file.puts(script)
  end
  File.chmod(0o755, pathname.to_s)
end
```