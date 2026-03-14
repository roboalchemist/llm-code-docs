# Class: Pod::Command::List
  
  
  

  
  
    Inherits:
    
      Pod::Command
      
        

          
- Object
          
            
- CLAide::Command
          
            
- Pod::Command
          
            
- Pod::Command::List
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/command/list.rb
  
  

  
    
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
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**update_if_necessary!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Pod::Command

  

#ensure_master_spec_repo_exists!, ensure_not_root_or_allowed!, report_error, run

  
  
  
  
  
  
  
  
  
### Methods included from Pod::Config::Mixin

  

#config

  
  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(argv)  ⇒ List 
  

  

  

  
    
      

```

14
15
16
17
18
```

    
    
      

```
# File 'lib/cocoapods/command/list.rb', line 14

def initialize(argv)
  @update = argv.flag?('update')
  @stats  = argv.flag?('stats')
  super
end

```

    
  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**options**  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
10
11
12
```

    
    
      

```
# File 'lib/cocoapods/command/list.rb', line 7

def self.options
  [
    ['--update', 'Run `pod repo update` before listing'],
    ['--stats',  'Show additional stats (like GitHub watchers and forks)'],
  ].concat(super)
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**run**  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
23
24
25
26
```

    
    
      

```
# File 'lib/cocoapods/command/list.rb', line 20

def run
  update_if_necessary!

  sets = config.sources_manager.aggregate.all_sets
  sets.each { |set| UI.pod(set, :name_and_version) }
  UI.puts "\n#{sets.count} pods were found"
end

```

    
  

    
      
  
### 
  
    #**update_if_necessary!**  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
31
32
```

    
    
      

```
# File 'lib/cocoapods/command/list.rb', line 28

def update_if_necessary!
  UI.section("\nUpdating Spec Repositories\n".yellow) do
    Repo::Update.new(CLAide::ARGV.new([])).run
  end if @update
end

```