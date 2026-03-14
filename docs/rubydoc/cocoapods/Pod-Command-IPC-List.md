# Class: Pod::Command::IPC::List
  
    Inherits:
    
      Pod::Command::IPC
      
        

          
- Object

- CLAide::Command

- Pod::Command

- Pod::Command::IPC

- Pod::Command::IPC::List

        show all
      

    Defined in:
    lib/cocoapods/command/ipc/list.rb
  
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**run**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods inherited from Pod::Command::IPC

# output_pipe

### Methods inherited from Pod::Command

# ensure_master_spec_repo_exists!, ensure_not_root_or_allowed!, #initialize, options, report_error, run

### Methods included from Pod::Config::Mixin

# config

## Constructor Details

This class inherits a constructor from Pod::Command
  
## Instance Method Details

###
  
    #**run**  ⇒ Object 
  

  

  

  
    
      

```

18
19
20
21
22
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
33
34
35
36
```

```
# File 'lib/cocoapods/command/ipc/list.rb', line 18

def run
  require 'yaml'
  sets = config.sources_manager.aggregate.all_sets
  result = {}
  sets.each do |set|
    begin
      spec = set.specification
      result[spec.name] = {
        'authors' => spec.authors.keys,
        'summary' => spec.summary,
        'description' => spec.description,
        'platforms' => spec.available_platforms.map { |p| p.name.to_s },
      }
    rescue DSLError
      next
    end
  end
  output_pipe.puts result.to_yaml
end
```
