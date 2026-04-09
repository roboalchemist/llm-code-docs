# Class: Pod::Command::Repo::Add
  
    Inherits:
    
      Pod::Command::Repo
      
        

          
- Object

- CLAide::Command

- Pod::Command

- Pod::Command::Repo

- Pod::Command::Repo::Add

        show all
      

    Defined in:
    lib/cocoapods/command/repo/add.rb
  
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(argv)  ⇒ Add 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Add.

-
  
      #**run**  ⇒ Object 

-
  
      #**validate!**  ⇒ Object 

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
  
    #**initialize**(argv)  ⇒ Add 
  

  

  

  
    

Returns a new instance of Add.

```

24
25
26
27
28
29
30
```

```
# File 'lib/cocoapods/command/repo/add.rb', line 24

def initialize(argv)
  @name = argv.shift_argument
  @url = argv.shift_argument
  @branch = argv.shift_argument
  @progress = argv.flag?('progress')
  super
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
# File 'lib/cocoapods/command/repo/add.rb', line 18

def self.options
  [
    ['--progress', 'Show the progress of cloning the spec repository'],
  ].concat(super)
end

```

## Instance Method Details

###
  
    #**run**  ⇒ Object 
  

  

  

  
    
      

```

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
```

```
# File 'lib/cocoapods/command/repo/add.rb', line 43

def run
  section = "Cloning spec repo `#{@name}` from `#{@url}`"
  section << " (branch `#{@branch}`)" if @branch
  UI.section(section) do
    create_repos_dir
    clone_repo
    checkout_branch
    config.sources_manager.sources([dir.basename.to_s]).each(&:verify_compatibility!)
  end
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
37
38
39
40
41
```

```
# File 'lib/cocoapods/command/repo/add.rb', line 32

def validate!
  super
  unless @name && @url
    help! 'Adding a repo needs a `NAME` and a `URL`.'
  end
  if @name == 'trunk'
    raise Informative,
          "Repo name `trunk` is reserved for CocoaPods' main spec repo accessed via CDN."
  end
end

```
