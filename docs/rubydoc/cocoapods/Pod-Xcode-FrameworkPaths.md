# Class: Pod::Xcode::FrameworkPaths
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::Xcode::FrameworkPaths
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/xcode/framework_paths.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**bcsymbolmap_paths**  ⇒ Array<String>, Nil 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The bcsymbolmap files path array, if one exists.

  

    
      
- 
  
    
      #**dsym_path**  ⇒ String, Nil 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The dSYM path, if one exists.

  

    
      
- 
  
    
      #**source_path**  ⇒ String 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The path to the .framework.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**from_path**(path)  ⇒ FrameworkPaths 
    

    
  
  
  
  
  
  
  
  

  
    

The path of the framework with dsym & bcsymbolmap paths, if found.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**==**(other)  ⇒ Object 
    

    
      (also: #eql?)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**all_paths**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**hash**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(source_path, dsym_path = nil, bcsymbolmap_paths = nil)  ⇒ FrameworkPaths 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of FrameworkPaths.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(source_path, dsym_path = nil, bcsymbolmap_paths = nil)  ⇒ FrameworkPaths 
  

  

  

  
    

Returns a new instance of FrameworkPaths.

  

  

  
    
      

```

16
17
18
19
20
```

    
    
      

```
# File 'lib/cocoapods/xcode/framework_paths.rb', line 16

def initialize(source_path, dsym_path = nil, bcsymbolmap_paths = nil)
  @source_path = source_path
  @dsym_path = dsym_path
  @bcsymbolmap_paths = bcsymbolmap_paths
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**bcsymbolmap_paths**  ⇒ Array<String>, Nil  (readonly)
  

  

  

  
    

Returns the bcsymbolmap files path array, if one exists.

  

  

Returns:

  
    
- 
      
      
        (Array<String>, Nil)
      
      
      
        —
        

the bcsymbolmap files path array, if one exists

      
    
  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/cocoapods/xcode/framework_paths.rb', line 14

def bcsymbolmap_paths
  @bcsymbolmap_paths
end
```

    
  

    
      
      
      
  
### 
  
    #**dsym_path**  ⇒ String, Nil  (readonly)
  

  

  

  
    

Returns the dSYM path, if one exists.

  

  

Returns:

  
    
- 
      
      
        (String, Nil)
      
      
      
        —
        

the dSYM path, if one exists

      
    
  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/cocoapods/xcode/framework_paths.rb', line 10

def dsym_path
  @dsym_path
end
```

    
  

    
      
      
      
  
### 
  
    #**source_path**  ⇒ String  (readonly)
  

  

  

  
    

Returns the path to the .framework.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

the path to the .framework

      
    
  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/cocoapods/xcode/framework_paths.rb', line 6

def source_path
  @source_path
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**from_path**(path)  ⇒ FrameworkPaths 
  

  

  

  
    

Returns the path of the framework with dsym & bcsymbolmap paths, if found.

  

  

Parameters:

  
    
- 
      
        path
      
      
        (Pathname)
      
      
      
        —
        

the path to the `.framework` bundle

      
    
  

Returns:

  
    
- 
      
      
        (FrameworkPaths)
      
      
      
        —
        

the path of the framework with dsym & bcsymbolmap paths, if found

      
    
  

  
    
      

```

44
45
46
47
48
49
50
51
```

    
    
      

```
# File 'lib/cocoapods/xcode/framework_paths.rb', line 44

def self.from_path(path)
  dsym_name = "#{path.basename}.dSYM"
  dsym_path = Pathname.new("#{path.dirname}/#{dsym_name}")
  dsym_path = nil unless dsym_path.exist?
  bcsymbolmap_paths = Pathname.glob(path.dirname, '*.bcsymbolmap')

  FrameworkPaths.new(path, dsym_path, bcsymbolmap_paths)
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**==**(other)  ⇒ Object 
  

  
    Also known as:
    eql?
    
  

  

  
    
      

```

22
23
24
25
26
27
28
```

    
    
      

```
# File 'lib/cocoapods/xcode/framework_paths.rb', line 22

def ==(other)
  if other.class == self.class
    other.source_path == @source_path && other.dsym_path == @dsym_path && other.bcsymbolmap_paths == @bcsymbolmap_paths
  else
    false
  end
end
```

    
  

    
      
  
### 
  
    #**all_paths**  ⇒ Object 
  

  

  

  
    
      

```

36
37
38
```

    
    
      

```
# File 'lib/cocoapods/xcode/framework_paths.rb', line 36

def all_paths
  [source_path, dsym_path, bcsymbolmap_paths].flatten.compact
end
```

    
  

    
      
  
### 
  
    #**hash**  ⇒ Object 
  

  

  

  
    
      

```

32
33
34
```

    
    
      

```
# File 'lib/cocoapods/xcode/framework_paths.rb', line 32

def hash
  [source_path, dsym_path, bcsymbolmap_paths].hash
end
```