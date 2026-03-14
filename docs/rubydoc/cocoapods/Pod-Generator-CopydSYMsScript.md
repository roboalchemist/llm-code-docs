# Class: Pod::Generator::CopydSYMsScript
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::Generator::CopydSYMsScript
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/generator/copy_dsyms_script.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**bcsymbolmap_paths**  ⇒ Array<Pathname, String> 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Bcsymbolmap_paths the bcsymbolmap paths to include in the script contents.

  

    
      
- 
  
    
      #**dsym_paths**  ⇒ Array<Pathname, String> 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Dsym_paths the dSYM paths to include in the script contents.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**generate**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The generated of the copy dSYMs script.

  

      
        
- 
  
    
      #**initialize**(dsym_paths, bcsymbolmap_paths)  ⇒ CopydSYMsScript 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize a new instance.

  

      
        
- 
  
    
      #**save_as**(pathname)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Saves the copy dSYMs script to the given pathname.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(dsym_paths, bcsymbolmap_paths)  ⇒ CopydSYMsScript 
  

  

  

  
    

Initialize a new instance

  

  

Parameters:

  
    
- 
      
        dsym_paths
      
      
        (Array<Pathname, String>)
      
      
      
        —
        

@see dsym_paths

      
    
  
    
- 
      
        bcsymbolmap_paths
      
      
        (Array<Pathname, String>)
      
      
      
        —
        

@see bcsymbolmap_paths

      
    
  

  
    
      

```

17
18
19
20
```

    
    
      

```
# File 'lib/cocoapods/generator/copy_dsyms_script.rb', line 17

def initialize(dsym_paths, bcsymbolmap_paths)
  @dsym_paths = Array(dsym_paths)
  @bcsymbolmap_paths = Array(bcsymbolmap_paths)
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**bcsymbolmap_paths**  ⇒ Array<Pathname, String>  (readonly)
  

  

  

  
    

Returns bcsymbolmap_paths the bcsymbolmap paths to include in the script contents.

  

  

Returns:

  
    
- 
      
      
        (Array<Pathname, String>)
      
      
      
        —
        

bcsymbolmap_paths the bcsymbolmap paths to include in the script contents.

      
    
  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/cocoapods/generator/copy_dsyms_script.rb', line 10

def bcsymbolmap_paths
  @bcsymbolmap_paths
end
```

    
  

    
      
      
      
  
### 
  
    #**dsym_paths**  ⇒ Array<Pathname, String>  (readonly)
  

  

  

  
    

Returns dsym_paths the dSYM paths to include in the script contents.

  

  

Returns:

  
    
- 
      
      
        (Array<Pathname, String>)
      
      
      
        —
        

dsym_paths the dSYM paths to include in the script contents.

      
    
  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/cocoapods/generator/copy_dsyms_script.rb', line 6

def dsym_paths
  @dsym_paths
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**generate**  ⇒ String 
  

  

  

  
    

Returns The generated of the copy dSYMs script.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

The generated of the copy dSYMs script.

      
    
  

  
    
      

```

38
39
40
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
```

    
    
      

```
# File 'lib/cocoapods/generator/copy_dsyms_script.rb', line 38

def generate
  script = <<-SH.strip_heredoc
#{Pod::Generator::ScriptPhaseConstants::DEFAULT_SCRIPT_PHASE_HEADER}
#{Pod::Generator::ScriptPhaseConstants::STRIP_INVALID_ARCHITECTURES_METHOD}
#{Pod::Generator::ScriptPhaseConstants::RSYNC_PROTECT_TMP_FILES}
#{Pod::Generator::ScriptPhaseConstants::INSTALL_DSYM_METHOD}
#{Pod::Generator::ScriptPhaseConstants::INSTALL_BCSYMBOLMAP_METHOD}
  SH
  dsym_paths.each do |dsym_path|
    script << %(install_dsym "#{dsym_path}"\n)
  end
  bcsymbolmap_paths.each do |bcsymbolmap_path|
    script << %(install_bcsymbolmap "#{bcsymbolmap_path}"\n)
  end
  script
end
```

    
  

    
      
  
### 
  
    #**save_as**(pathname)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Saves the copy dSYMs script to the given pathname.

  

  

Parameters:

  
    
- 
      
        pathname
      
      
        (Pathname)
      
      
      
        —
        

The path where the copy dSYMs script should be saved.

      
    
  

  
    
      

```

29
30
31
32
33
34
```

    
    
      

```
# File 'lib/cocoapods/generator/copy_dsyms_script.rb', line 29

def save_as(pathname)
  pathname.open('w') do |file|
    file.puts(generate)
  end
  File.chmod(0755, pathname.to_s)
end
```