# Module: Pod::Config::Mixin
  
    Included in:
    Pod::Command, Installer, Installer::Analyzer, UserInterface, Validator
  
  

  
  
    Defined in:
    lib/cocoapods/config.rb
  
## Overview

Provides support for accessing the configuration instance in other scopes.

##

      Singleton
      collapse
    

    

      
        
-
  
      #**config**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

###
  
    #**config**  ⇒ Object 
  

  

  

  
    
      

```

362
363
364
```

```
# File 'lib/cocoapods/config.rb', line 362

def config
  Config.instance
end
```
