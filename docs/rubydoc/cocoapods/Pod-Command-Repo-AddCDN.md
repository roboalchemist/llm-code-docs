# Class: Pod::Command::Repo::AddCDN
  
    Inherits:
    
      Pod::Command::Repo
      
        

          
- Object

- CLAide::Command

- Pod::Command

- Pod::Command::Repo

- Pod::Command::Repo::AddCDN

        show all
      

    Defined in:
    lib/cocoapods/command/repo/add_cdn.rb
  
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(argv)  ⇒ AddCDN 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of AddCDN.

-
  
      #**run**  ⇒ Object 

-
  
      #**validate!**  ⇒ Object 

### Methods inherited from Pod::Command::Repo

# dir

### Methods included from Executable

capture_command, capture_command!, #executable, execute_command, which, which!

### Methods inherited from Pod::Command

# ensure_master_spec_repo_exists!, ensure_not_root_or_allowed!, options, report_error, run

### Methods included from Pod::Config::Mixin

# config

## Constructor Details

###
  
    #**initialize**(argv)  ⇒ AddCDN 
  

  

  

  
    
      

```

17
18
19
20
21
```

```
# File 'lib/cocoapods/command/repo/add_cdn.rb', line 17

def initialize(argv)
  @name = argv.shift_argument
  @url = argv.shift_argument
  super
end

```

## Instance Method Details

###
  
    #**run**  ⇒ Object 
  

  

  

  
    
      

```

34
35
36
37
38
39
40
```

```
# File 'lib/cocoapods/command/repo/add_cdn.rb', line 34

def run
  section = "Adding spec repo `#{@name}` with CDN `#{@url}`"
  UI.section(section) do
    save_url
    config.sources_manager.sources([dir.basename.to_s]).each(&:verify_compatibility!)
  end
end

```

###
  
    #**validate!**  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
26
27
28
29
30
31
32
```

```
# File 'lib/cocoapods/command/repo/add_cdn.rb', line 23

def validate!
  super
  unless @name && @url
    help! 'Adding a repo needs a `NAME` and a `URL`.'
  end
  if @name == 'master'
    raise Informative,
          'To setup the master specs repo, please run `pod setup`.'
  end
end

```
