# Class: Pod::Command::IPC
  
  
  

  
  
    Inherits:
    
      Pod::Command
      
        

          
- Object
          
            
- CLAide::Command
          
            
- Pod::Command
          
            
- Pod::Command::IPC
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/command/ipc.rb,

  lib/cocoapods/command/ipc/list.rb,
 lib/cocoapods/command/ipc/repl.rb,
 lib/cocoapods/command/ipc/spec.rb,
 lib/cocoapods/command/ipc/podfile.rb,
 lib/cocoapods/command/ipc/podfile_json.rb,
 lib/cocoapods/command/ipc/update_search_index.rb

  
  

  
## Direct Known Subclasses

  

List, Podfile, PodfileJSON, Repl, Spec, UpdateSearchIndex

## Defined Under Namespace

  
    
  
    
      **Classes:** List, Podfile, PodfileJSON, Repl, Spec, UpdateSearchIndex
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**output_pipe**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Pod::Command

  

#ensure_master_spec_repo_exists!, ensure_not_root_or_allowed!, #initialize, options, report_error, run

  
  
  
  
  
  
  
  
  
### Methods included from Pod::Config::Mixin

  

#config

  
  
  
  
  
  
  
  
## Constructor Details

  
    

This class inherits a constructor from Pod::Command
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**output_pipe**  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/cocoapods/command/ipc.rb', line 14

def output_pipe
  STDOUT
end
```