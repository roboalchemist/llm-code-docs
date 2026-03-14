# Class: Pod::Command::Spec::Cat
  
  
  

  
  
    Inherits:
    
      Pod::Command::Spec
      
        

          
- Object
          
            
- CLAide::Command
          
            
- Pod::Command
          
            
- Pod::Command::Spec
          
            
- Pod::Command::Spec::Cat
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/command/spec/cat.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(argv)  ⇒ Cat 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Cat.

  

      
        
- 
  
    
      #**run**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validate!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods inherited from Pod::Command

  

#ensure_master_spec_repo_exists!, ensure_not_root_or_allowed!, report_error, run

  
  
  
  
  
  
  
  
  
### Methods included from Pod::Config::Mixin

  

#config

  
  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(argv)  ⇒ Cat 
  

  

  

  
    

Returns a new instance of Cat.

  

  

  
    
      

```

23
24
25
26
27
28
29
30
```

    
    
      

```
# File 'lib/cocoapods/command/spec/cat.rb', line 23

def initialize(argv)
  @use_regex = argv.flag?('regex')
  @show_all = argv.flag?('show-all')
  @query = argv.shift_argument
  @query = @query.gsub('.podspec', '') unless @query.nil?
  @version = argv.option('version')
  super
end

```

    
  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**options**  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
18
19
20
21
```

    
    
      

```
# File 'lib/cocoapods/command/spec/cat.rb', line 15

def self.options
  [
    ['--regex', 'Interpret the `QUERY` as a regular expression'],
    ['--show-all', 'Pick from all versions of the given podspec'],
    ['--version', 'Print a specific version of the given podspec'],
  ].concat(super)
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**run**  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/cocoapods/command/spec/cat.rb', line 38

def run
  query = @use_regex ? @query : Regexp.escape(@query)
  filepath = if @show_all
               specs = get_path_of_spec(query, @show_all).split(/\n/)
               index = UI.choose_from_array(specs, "Which spec would you like to print [1-#{specs.count}]? ")
               specs[index]
             else
               get_path_of_spec(query, @version)
             end

  UI.puts File.read(filepath)
end

```

    
  

    
      
  
### 
  
    #**validate!**  ⇒ Object 
  

  

  

  
    
      

```

32
33
34
35
36
```

    
    
      

```
# File 'lib/cocoapods/command/spec/cat.rb', line 32

def validate!
  super
  help! 'A podspec name is required.' unless @query
  validate_regex!(@query) if @use_regex
end

```