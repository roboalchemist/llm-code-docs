# Class: Pod::Command::Spec::Edit
  
  
  

  
  
    Inherits:
    
      Pod::Command::Spec
      
        

          
- Object
          
            
- CLAide::Command
          
            
- Pod::Command
          
            
- Pod::Command::Spec
          
            
- Pod::Command::Spec::Edit
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/command/spec/edit.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**exec_editor**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(argv)  ⇒ Edit 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Edit.

  

      
        
- 
  
    
      #**run**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**safe_exec**(cmd, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validate!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**which_editor**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods inherited from Pod::Command

  

#ensure_master_spec_repo_exists!, ensure_not_root_or_allowed!, report_error, run

  
  
  
  
  
  
  
  
  
### Methods included from Pod::Config::Mixin

  

#config

  
  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(argv)  ⇒ Edit 
  

  

  

  
    

Returns a new instance of Edit.

  

  

  
    
      

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
# File 'lib/cocoapods/command/spec/edit.rb', line 22

def initialize(argv)
  @use_regex = argv.flag?('regex')
  @show_all = argv.flag?('show-all')
  @query = argv.shift_argument
  @query = @query.gsub('.podspec', '') unless @query.nil?
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
```

    
    
      

```
# File 'lib/cocoapods/command/spec/edit.rb', line 15

def self.options
  [
    ['--regex', 'Interpret the `QUERY` as a regular expression'],
    ['--show-all', 'Pick from all versions of the given podspec'],
  ].concat(super)
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**exec_editor**(*args)  ⇒ Object 
  

  

  

  
    
      

```

74
75
76
77
```

    
    
      

```
# File 'lib/cocoapods/command/spec/edit.rb', line 74

def exec_editor(*args)
  return if args.to_s.empty?
  safe_exec(which_editor, *args)
end

```

    
  

    
      
  
### 
  
    #**run**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
      
      
    
  

  
    
      

```

36
37
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
# File 'lib/cocoapods/command/spec/edit.rb', line 36

def run
  query = @use_regex ? @query : Regexp.escape(@query)
  if @show_all
    specs = get_path_of_spec(query, @show_all).split(/\n/)
    message = "Which spec would you like to edit [1-#{specs.count}]? "
    index = UI.choose_from_array(specs, message)
    filepath = specs[index]
  else
    filepath = get_path_of_spec(query)
  end

  exec_editor(filepath.to_s) if File.exist? filepath
  raise Informative, "#{filepath} doesn't exist."
end

```

    
  

    
      
  
### 
  
    #**safe_exec**(cmd, *args)  ⇒ Object 
  

  

  

  
    
      

```

79
80
81
82
83
```

    
    
      

```
# File 'lib/cocoapods/command/spec/edit.rb', line 79

def safe_exec(cmd, *args)
  # This buys us proper argument quoting and evaluation
  # of environment variables in the cmd parameter.
  exec('/bin/sh', '-i', '-c', cmd + ' "$@"', '--', *args)
end

```

    
  

    
      
  
### 
  
    #**validate!**  ⇒ Object 
  

  

  

  
    
      

```

30
31
32
33
34
```

    
    
      

```
# File 'lib/cocoapods/command/spec/edit.rb', line 30

def validate!
  super
  help! 'A podspec name is required.' unless @query
  validate_regex!(@query) if @use_regex
end

```

    
  

    
      
  
### 
  
    #**which_editor**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
      
      
    
  

  
    
      

```

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
69
70
71
72
```

    
    
      

```
# File 'lib/cocoapods/command/spec/edit.rb', line 51

def which_editor
  editor = ENV['EDITOR']
  # If an editor wasn't set, try to pick a sane default
  return editor unless editor.nil?

  editors = [
    # Find Sublime Text 2
    'subl',
    # Find Textmate
    'mate',
    # Find BBEdit / TextWrangler
    'edit',
    # Find Atom
    'atom',
    # Default to vim
    'vim',
  ]
  editor = editors.find { |e| Pod::Executable.which(e) }
  return editor if editor

  raise Informative, "Failed to open editor. Set your 'EDITOR' environment variable."
end

```