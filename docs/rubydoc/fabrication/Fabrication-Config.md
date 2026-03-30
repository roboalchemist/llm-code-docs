# Module: Fabrication::Config
  
  
  

  

  
  
  
      Extended by:
      Config
  
  
  
  
  

  
  
    Included in:
    Config
  
  

  
  
    Defined in:
    lib/fabrication/config.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**logger**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      #**sequence_start**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**configure** {|_self| ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fabricator_dir**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fabricator_dir=**(folders)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fabricator_path**  ⇒ Object 
    

    
      (also: #fabricator_paths)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fabricator_path=**(folders)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**generator_for**(default_generators, klass)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**generators**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**notifiers**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**path_prefix**  ⇒ Object 
    

    
      (also: #path_prefixes)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**path_prefix=**(folders)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**recursion_limit**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**recursion_limit=**(limit)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**register_notifier**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**register_with_steps=**(value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**reset_defaults**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**logger**  ⇒ Object 
  

  

  

  
    
      

```

21
22
23
24
25
```

    
    
      

```
# File 'lib/fabrication/config.rb', line 21

def logger
  @logger ||= Logger.new($stdout).tap do |logger|
    logger.level = Logger::WARN
  end
end
```

    
  

    
      
      
      
  
### 
  
    #**sequence_start**  ⇒ Object 
  

  

  

  
    
      

```

48
49
50
```

    
    
      

```
# File 'lib/fabrication/config.rb', line 48

def sequence_start
  @sequence_start ||= 0
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**configure** {|_self| ... } ⇒ Object 
  

  

  

  
    

  

  

Yields:

  
    
- 
      
      
        (_self)
      
      
      
    
  

Yield Parameters:

  
    
- 
      
        _self
      
      
        (Fabrication::Config)
      
      
      
        —
        

the object that the method was called on

      
    
  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/fabrication/config.rb', line 7

def configure
  yield self
end
```

    
  

    
      
  
### 
  
    #**fabricator_dir**  ⇒ Object 
  

  

  

  
    
      

```

32
33
34
35
36
```

    
    
      

```
# File 'lib/fabrication/config.rb', line 32

def fabricator_dir
  Support.log_deprecation('Fabrication::Config.fabricator_dir has been ' \
                          'replaced by Fabrication::Config.fabricator_path')
  fabricator_path
end
```

    
  

    
      
  
### 
  
    #**fabricator_dir=**(folders)  ⇒ Object 
  

  

  

  
    
      

```

42
43
44
45
46
```

    
    
      

```
# File 'lib/fabrication/config.rb', line 42

def fabricator_dir=(folders)
  Support.log_deprecation('Fabrication::Config.fabricator_dir has been ' \
                          'replaced by Fabrication::Config.fabricator_path')
  self.fabricator_path = folders
end
```

    
  

    
      
  
### 
  
    #**fabricator_path**  ⇒ Object 
  

  
    Also known as:
    fabricator_paths
    
  

  

  
    
      

```

27
28
29
```

    
    
      

```
# File 'lib/fabrication/config.rb', line 27

def fabricator_path
  @fabricator_path ||= ['test/fabricators', 'spec/fabricators']
end
```

    
  

    
      
  
### 
  
    #**fabricator_path=**(folders)  ⇒ Object 
  

  

  

  
    
      

```

38
39
40
```

    
    
      

```
# File 'lib/fabrication/config.rb', line 38

def fabricator_path=(folders)
  @fabricator_path = ([] << folders).flatten
end
```

    
  

    
      
  
### 
  
    #**generator_for**(default_generators, klass)  ⇒ Object 
  

  

  

  
    
      

```

65
66
67
```

    
    
      

```
# File 'lib/fabrication/config.rb', line 65

def generator_for(default_generators, klass)
  (generators + default_generators).detect { |gen| gen.supports?(klass) }
end
```

    
  

    
      
  
### 
  
    #**generators**  ⇒ Object 
  

  

  

  
    
      

```

61
62
63
```

    
    
      

```
# File 'lib/fabrication/config.rb', line 61

def generators
  @generators ||= []
end
```

    
  

    
      
  
### 
  
    #**notifiers**  ⇒ Object 
  

  

  

  
    
      

```

90
91
92
```

    
    
      

```
# File 'lib/fabrication/config.rb', line 90

def notifiers
  @notifiers ||= []
end
```

    
  

    
      
  
### 
  
    #**path_prefix**  ⇒ Object 
  

  
    Also known as:
    path_prefixes
    
  

  

  
    
      

```

56
57
58
```

    
    
      

```
# File 'lib/fabrication/config.rb', line 56

def path_prefix
  @path_prefix ||= [defined?(Rails) ? Rails.root : '.']
end
```

    
  

    
      
  
### 
  
    #**path_prefix=**(folders)  ⇒ Object 
  

  

  

  
    
      

```

52
53
54
```

    
    
      

```
# File 'lib/fabrication/config.rb', line 52

def path_prefix=(folders)
  @path_prefix = ([] << folders).flatten
end
```

    
  

    
      
  
### 
  
    #**recursion_limit**  ⇒ Object 
  

  

  

  
    
      

```

69
70
71
```

    
    
      

```
# File 'lib/fabrication/config.rb', line 69

def recursion_limit
  @recursion_limit ||= 20
end
```

    
  

    
      
  
### 
  
    #**recursion_limit=**(limit)  ⇒ Object 
  

  

  

  
    
      

```

73
74
75
```

    
    
      

```
# File 'lib/fabrication/config.rb', line 73

def recursion_limit=(limit)
  @recursion_limit = limit
end
```

    
  

    
      
  
### 
  
    #**register_notifier**(&block)  ⇒ Object 
  

  

  

  
    
      

```

94
95
96
```

    
    
      

```
# File 'lib/fabrication/config.rb', line 94

def register_notifier(&block)
  notifiers.push(block)
end
```

    
  

    
      
  
### 
  
    #**register_with_steps=**(value)  ⇒ Object 
  

  

  

  
    
      

```

77
78
79
80
81
82
83
84
85
86
87
88
```

    
    
      

```
# File 'lib/fabrication/config.rb', line 77

def register_with_steps=(value)
  Support.log_deprecation(
    'Fabrication::Config.register_with_steps has been deprecated. ' \
    'Please regenerate your cucumber steps with `rails g fabrication:cucumber_steps'
  )

  return unless value

  register_notifier do |name, object|
    Fabrication::Cucumber::Fabrications[name] = object
  end
end
```

    
  

    
      
  
### 
  
    #**reset_defaults**  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
14
15
16
17
```

    
    
      

```
# File 'lib/fabrication/config.rb', line 11

def reset_defaults
  @fabricator_path =
    @path_prefix =
      @sequence_start =
        @generators =
          nil
end
```