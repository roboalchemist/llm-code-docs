# Class: Pod::Command::Cache::List
  
  
  

  
  
    Inherits:
    
      Pod::Command::Cache
      
        

          
- Object
          
            
- CLAide::Command
          
            
- Pod::Command
          
            
- Pod::Command::Cache
          
            
- Pod::Command::Cache::List
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/command/cache/list.rb
  
  

  
    
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
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods inherited from Pod::Command

  

#ensure_master_spec_repo_exists!, ensure_not_root_or_allowed!, report_error, run

  
  
  
  
  
  
  
  
  
### Methods included from Pod::Config::Mixin

  

#config

  
  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(argv)  ⇒ List 
  

  

  

  
    

Returns a new instance of List.

  

  

  
    
      

```

22
23
24
25
26
```

    
    
      

```
# File 'lib/cocoapods/command/cache/list.rb', line 22

def initialize(argv)
  @pod_name = argv.shift_argument
  @short_output = argv.flag?('short')
  super
end
```

    
  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**options**  ⇒ Object 
  

  

  

  
    
      

```

16
17
18
19
20
```

    
    
      

```
# File 'lib/cocoapods/command/cache/list.rb', line 16

def self.options
  [[
    '--short', 'Only print the path relative to the cache root'
  ]].concat(super)
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
42
```

    
    
      

```
# File 'lib/cocoapods/command/cache/list.rb', line 28

def run
  UI.puts("$CACHE_ROOT: #{@cache.root}") if @short_output
  if @pod_name.nil? # Print all
    @cache.cache_descriptors_per_pod.each do |pod_name, cache_descriptors|
      print_pod_cache_infos(pod_name, cache_descriptors)
    end
  else # Print only for the requested pod
    cache_descriptors = @cache.cache_descriptors_per_pod[@pod_name]
    if cache_descriptors.nil?
      UI.notice("No cache for pod named #{@pod_name} found")
    else
      print_pod_cache_infos(@pod_name, cache_descriptors)
    end
  end
end
```