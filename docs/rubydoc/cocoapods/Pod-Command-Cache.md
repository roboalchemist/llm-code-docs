# Class: Pod::Command::Cache
  
    Inherits:
    
      Pod::Command
      
        

          
- Object

- CLAide::Command

- Pod::Command

- Pod::Command::Cache

        show all
      

    Defined in:
    lib/cocoapods/command/cache.rb,

  lib/cocoapods/command/cache/list.rb,
 lib/cocoapods/command/cache/clean.rb

## Direct Known Subclasses

Clean, List

## Defined Under Namespace

      **Classes:** Clean, List
    
  

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(argv)  ⇒ Cache 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Cache.

### Methods inherited from Pod::Command

# ensure_master_spec_repo_exists!, ensure_not_root_or_allowed!, options, report_error, run

### Methods included from Pod::Config::Mixin

# config

## Constructor Details

###
  
    #**initialize**(argv)  ⇒ Cache 
  

  

  

  
    

Returns a new instance of Cache.

```

16
17
18
19
```

```
# File 'lib/cocoapods/command/cache.rb', line 16

def initialize(argv)
  @cache = Downloader::Cache.new(Config.instance.cache_root + 'Pods')
  super
end
```
