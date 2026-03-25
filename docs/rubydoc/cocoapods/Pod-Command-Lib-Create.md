# Class: Pod::Command::Lib::Create
  
    Inherits:
    
      Pod::Command::Lib
      
        

          
- Object

- CLAide::Command

- Pod::Command

- Pod::Command::Lib

- Pod::Command::Lib::Create

        show all
      
    
  
  

  
  
  
      Extended by:
      Executable
  
    Defined in:
    lib/cocoapods/command/lib/create.rb
  
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
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

### Methods included from Executable

capture_command, capture_command!, executable, execute_command, which, which!

### Methods inherited from Pod::Command

# ensure_master_spec_repo_exists!, ensure_not_root_or_allowed!, report_error, run

### Methods included from Pod::Config::Mixin

# config

## Constructor Details

###
  
    #**initialize**(argv)  ⇒ Create 
  

  

  

  
    

Returns a new instance of Create.

```

24
25
26
27
28
29
```

```
# File 'lib/cocoapods/command/lib/create.rb', line 24

def initialize(argv)
  @name = argv.shift_argument
  @template_url = argv.option('template-url', TEMPLATE_REPO)
  super
  @additional_args = argv.remainder!
end
```

## Class Method Details

###
  
    .**options**  ⇒ Object 
  

  

  

  
    
      

```

18
19
20
21
22
```

```
# File 'lib/cocoapods/command/lib/create.rb', line 18

def self.options
  [
    ['--template-url=URL', 'The URL of the git repo containing a compatible template'],
  ].concat(super)
end
```

## Instance Method Details

###
  
    #**run**  ⇒ Object 
  

  

  

  
    
      

```

39
40
41
42
43
```

```
# File 'lib/cocoapods/command/lib/create.rb', line 39

def run
  clone_template
  configure_template
  print_info
end
```

###
  
    #**validate!**  ⇒ Object 
  

  

  

  
    
      

```

31
32
33
34
35
36
37
```

```
# File 'lib/cocoapods/command/lib/create.rb', line 31

def validate!
  super
  help! 'A name for the Pod is required.' unless @name
  help! 'The Pod name cannot contain spaces.' if @name =~ /\s/
  help! 'The Pod name cannot contain plusses.' if @name =~ /\+/
  help! "The Pod name cannot begin with a '.'" if @name[0, 1] == '.'
end
```
