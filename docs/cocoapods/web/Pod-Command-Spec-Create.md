# Class: Pod::Command::Spec::Create
  
    Inherits:
    
      Pod::Command::Spec
      
        

          
- Object

- CLAide::Command

- Pod::Command

- Pod::Command::Spec

- Pod::Command::Spec::Create

        show all
      

    Defined in:
    lib/cocoapods/command/spec/create.rb
  
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(argv)  ⇒ Create 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Create.

-
  
      #**run**  ⇒ Object 

-
  
      #**validate!**  ⇒ Object 

### Methods inherited from Pod::Command

# ensure_master_spec_repo_exists!, ensure_not_root_or_allowed!, options, report_error, run

### Methods included from Pod::Config::Mixin

# config

## Constructor Details

###
  
    #**initialize**(argv)  ⇒ Create 
  

  

  

  
    

Returns a new instance of Create.

```

17
18
19
20
21
```

```
# File 'lib/cocoapods/command/spec/create.rb', line 17

def initialize(argv)
  @name_or_url = argv.shift_argument
  @url = argv.shift_argument
  super
end

```

## Instance Method Details

###
  
    #**run**  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
31
32
33
34
35
36
37
38
39
40
41
```

```
# File 'lib/cocoapods/command/spec/create.rb', line 28

def run
  if repo_id_match = (@url || @name_or_url).match(%r{github.com/([^/\.]*\/[^/\.]*)\.*})
    repo_id = repo_id_match[1]
    data = github_data_for_template(repo_id)
    data[:name] = @name_or_url if @url
    UI.puts semantic_versioning_notice(repo_id, data[:name]) if data[:version] == '0.0.1'
  else
    data = default_data_for_template(@name_or_url)
  end

  spec = spec_template(data)
  (Pathname.pwd + "#{data[:name]}.podspec").open('w') { |f| f << spec }
  UI.puts "\nSpecification created at #{data[:name]}.podspec".green
end

```

###
  
    #**validate!**  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
26
```

```
# File 'lib/cocoapods/command/spec/create.rb', line 23

def validate!
  super
  help! 'A pod name or repo URL is required.' unless @name_or_url
end

```
