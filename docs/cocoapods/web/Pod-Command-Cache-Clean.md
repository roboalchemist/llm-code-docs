# Class: Pod::Command::Cache::Clean
  
    Inherits:
    
      Pod::Command::Cache
      
        

          
- Object

- CLAide::Command

- Pod::Command

- Pod::Command::Cache

- Pod::Command::Cache::Clean

        show all
      

    Defined in:
    lib/cocoapods/command/cache/clean.rb
  
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(argv)  ⇒ Clean 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Clean.

-
  
      #**run**  ⇒ Object 

-
  
      #**validate!**  ⇒ Object 

### Methods inherited from Pod::Command

# ensure_master_spec_repo_exists!, ensure_not_root_or_allowed!, report_error, run

### Methods included from Pod::Config::Mixin

# config

## Constructor Details

###
  
    #**initialize**(argv)  ⇒ Clean 
  

  

  

  
    

Returns a new instance of Clean.

```

27
28
29
30
31
```

```
# File 'lib/cocoapods/command/cache/clean.rb', line 27

def initialize(argv)
  @pod_name = argv.shift_argument
  @wipe_all = argv.flag?('all')
  super
end

```

## Class Method Details

###
  
    .**options**  ⇒ Object 
  

  

  

  
    
      

```

21
22
23
24
25
```

```
# File 'lib/cocoapods/command/cache/clean.rb', line 21

def self.options
  [[
    '--all', 'Remove all the cached pods without asking'
  ]].concat(super)
end

```

## Instance Method Details

###
  
    #**run**  ⇒ Object 
  

  

  

  
    
      

```

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
53
```

```
# File 'lib/cocoapods/command/cache/clean.rb', line 33

def run
  if @pod_name.nil?
    # Note: at that point, @wipe_all is always true (thanks to `validate!`)
    # Remove all
    clear_cache
  else
    # Remove only cache for this pod
    cache_descriptors = @cache.cache_descriptors_per_pod[@pod_name]
    if cache_descriptors.nil?
      UI.notice("No cache for pod named #{@pod_name} found")
    elsif cache_descriptors.count > 1 && !@wipe_all
      # Ask which to remove
      choices = cache_descriptors.map { |c| "#{@pod_name} v#{c[:version]} (#{pod_type(c)})" }
      index = UI.choose_from_array(choices, 'Which pod cache do you want to remove?')
      remove_caches([cache_descriptors[index]])
    else
      # Remove all found cache of this pod
      remove_caches(cache_descriptors)
    end
  end
end

```

###
  
    #**validate!**  ⇒ Object 
  

  

  

  
    
      

```

55
56
57
58
59
60
61
```

```
# File 'lib/cocoapods/command/cache/clean.rb', line 55

def validate!
  super
  if @pod_name.nil? && !@wipe_all
    # Security measure, to avoid removing the pod cache too agressively by mistake
    help! 'You should either specify a pod name or use the --all flag'
  end
end

```
