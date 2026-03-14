# Class: Pod::Command::Install
  
    Inherits:
    
      Pod::Command
      
        

          
- Object

- CLAide::Command

- Pod::Command

- Pod::Command::Install

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      ProjectDirectory, RepoUpdate
  
    Defined in:
    lib/cocoapods/command/install.rb
  
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(argv)  ⇒ Install 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Install.

-
  
      #**run**  ⇒ Object 

### Methods inherited from Pod::Command

# ensure_master_spec_repo_exists!, ensure_not_root_or_allowed!, report_error, run

### Methods included from Pod::Config::Mixin

# config

## Constructor Details

###
  
    #**initialize**(argv)  ⇒ Install 
  

  

  

  
    

Returns a new instance of Install.

```

39
40
41
42
43
```

```
# File 'lib/cocoapods/command/install.rb', line 39

def initialize(argv)
  super
  @deployment = argv.flag?('deployment', false)
  @clean_install = argv.flag?('clean-install', false)
end
```

## Class Method Details

###
  
    .**options**  ⇒ Object 
  

  

  

  
    
      

```

30
31
32
33
34
35
36
37
```

```
# File 'lib/cocoapods/command/install.rb', line 30

def self.options
  [
    ['--repo-update', 'Force running `pod repo update` before install'],
    ['--deployment', 'Disallow any changes to the Podfile or the Podfile.lock during installation'],
    ['--clean-install', 'Ignore the contents of the project cache and force a full pod installation. This only ' \
      'applies to projects that have enabled incremental installation'],
  ].concat(super).reject { |(name, _)| name == '--no-repo-update' }
end
```

## Instance Method Details

###
  
    #**run**  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/cocoapods/command/install.rb', line 45

def run
  verify_podfile_exists!
  installer = installer_for_config
  installer.repo_update = repo_update?(:default => false)
  installer.update = false
  installer.deployment = @deployment
  installer.clean_install = @clean_install
  installer.install!
end
```
