# Class: Pod::Command::Repo::List
  
    Inherits:
    
      Pod::Command::Repo
      
        

          
- Object

- CLAide::Command

- Pod::Command

- Pod::Command::Repo

- Pod::Command::Repo::List

        show all
      

    Defined in:
    lib/cocoapods/command/repo/list.rb
  
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(argv)  ⇒ List 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of List.

-
  
      #**run**  ⇒ Object 

### Methods inherited from Pod::Command::Repo

# dir

### Methods included from Executable

capture_command, capture_command!, #executable, execute_command, which, which!

### Methods inherited from Pod::Command

# ensure_master_spec_repo_exists!, ensure_not_root_or_allowed!, report_error, run

### Methods included from Pod::Config::Mixin

# config

## Constructor Details

###
  
    #**initialize**(argv)  ⇒ List 
  

  

  

  
    

Returns a new instance of List.

```

15
16
17
18
```

```
# File 'lib/cocoapods/command/repo/list.rb', line 15

def initialize(argv)
  @count_only = argv.flag?('count-only')
  super
end

```

## Class Method Details

###
  
    .**options**  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
```

```
# File 'lib/cocoapods/command/repo/list.rb', line 11

def self.options
  [['--count-only', 'Show the total number of repos']].concat(super)
end

```

## Instance Method Details

###
  
    #**run**  ⇒ Object 
  

  

  

  
    
      

```

32
33
34
35
36
```

```
# File 'lib/cocoapods/command/repo/list.rb', line 32

def run
  sources = config.sources_manager.all
  print_sources(sources) unless @count_only
  print_count_of_sources(sources)
end

```
