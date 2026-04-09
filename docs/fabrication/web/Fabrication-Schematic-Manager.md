# Class: Fabrication::Schematic::Manager
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Fabrication::Schematic::Manager
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Singleton
  
  
  

  

  
  
    Defined in:
    lib/fabrication/schematic/manager.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**[]**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**build_stack**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**clear**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**create_stack**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**empty?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**freeze**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initializing?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**load_definitions**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**preinitialize**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**prevent_recursion!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**register**(name, options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**schematics**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_params_stack**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**[]**(name)  ⇒ Object 
  

  

  

  
    
      

```

39
40
41
```

    
    
      

```
# File 'lib/fabrication/schematic/manager.rb', line 39

def [](name)
  schematics[name.to_sym]
end
```

    
  

    
      
  
### 
  
    #**build_stack**  ⇒ Object 
  

  

  

  
    
      

```

47
48
49
```

    
    
      

```
# File 'lib/fabrication/schematic/manager.rb', line 47

def build_stack
  @build_stack ||= []
end
```

    
  

    
      
  
### 
  
    #**clear**  ⇒ Object 
  

  

  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/fabrication/schematic/manager.rb', line 21

def clear
  schematics.clear
end
```

    
  

    
      
  
### 
  
    #**create_stack**  ⇒ Object 
  

  

  

  
    
      

```

43
44
45
```

    
    
      

```
# File 'lib/fabrication/schematic/manager.rb', line 43

def create_stack
  @create_stack ||= []
end
```

    
  

    
      
  
### 
  
    #**empty?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/fabrication/schematic/manager.rb', line 25

def empty?
  schematics.empty?
end
```

    
  

    
      
  
### 
  
    #**freeze**  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/fabrication/schematic/manager.rb', line 29

def freeze
  @initializing = false
end
```

    
  

    
      
  
### 
  
    #**initializing?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/fabrication/schematic/manager.rb', line 13

def initializing?
  @initializing ||= nil
end
```

    
  

    
      
  
### 
  
    #**load_definitions**  ⇒ Object 
  

  

  

  
    
      

```

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
69
70
```

    
    
      

```
# File 'lib/fabrication/schematic/manager.rb', line 55

def load_definitions
  preinitialize
  Fabrication::Config.path_prefixes.each do |prefix|
    Fabrication::Config.fabricator_paths.each do |path|
      if File.file?(path)
        load path
      else
        Dir.glob(File.join(prefix.to_s, path, '**', '*.rb')).each do |file|
          load file
        end
      end
    end
  end
ensure
  freeze
end
```

    
  

    
      
  
### 
  
    #**preinitialize**  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
11
```

    
    
      

```
# File 'lib/fabrication/schematic/manager.rb', line 8

def preinitialize
  @initializing = true
  clear
end
```

    
  

    
      
  
### 
  
    #**prevent_recursion!**  ⇒ Object 
  

  

  

  
    
      

```

72
73
74
75
76
```

    
    
      

```
# File 'lib/fabrication/schematic/manager.rb', line 72

def prevent_recursion!
  (create_stack + build_stack + to_params_stack).group_by(&:to_sym).each do |name, values|
    raise Fabrication::InfiniteRecursionError, name if values.length > Fabrication::Config.recursion_limit
  end
end
```

    
  

    
      
  
### 
  
    #**register**(name, options)  ⇒ Object 
  

  

  

  
    
      

```

33
34
35
36
37
```

    
    
      

```
# File 'lib/fabrication/schematic/manager.rb', line 33

def register(name, options, &)
  name = name.to_sym
  raise_if_registered(name)
  store(name, Array(options.delete(:aliases)), options, &)
end
```

    
  

    
      
  
### 
  
    #**schematics**  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/fabrication/schematic/manager.rb', line 17

def schematics
  @schematics ||= {}
end
```

    
  

    
      
  
### 
  
    #**to_params_stack**  ⇒ Object 
  

  

  

  
    
      

```

51
52
53
```

    
    
      

```
# File 'lib/fabrication/schematic/manager.rb', line 51

def to_params_stack
  @to_params_stack ||= []
end
```