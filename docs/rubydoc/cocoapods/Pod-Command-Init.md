# Class: Pod::Command::Init
  
  
  

  
  
    Inherits:
    
      Pod::Command
      
        

          
- Object
          
            
- CLAide::Command
          
            
- Pod::Command
          
            
- Pod::Command::Init
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/command/init.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(argv)  ⇒ Init 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Init.

  

      
        
- 
  
    
      #**run**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validate!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Pod::Command

  

#ensure_master_spec_repo_exists!, ensure_not_root_or_allowed!, options, report_error, run

  
  
  
  
  
  
  
  
  
### Methods included from Pod::Config::Mixin

  

#config

  
  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(argv)  ⇒ Init 
  

  

  

  
    

Returns a new instance of Init.

  

  

  
    
      

```

23
24
25
26
27
28
```

    
    
      

```
# File 'lib/cocoapods/command/init.rb', line 23

def initialize(argv)
  @podfile_path = Pathname.pwd + 'Podfile'
  @project_path = argv.shift_argument
  @project_paths = Pathname.pwd.children.select { |pn| pn.extname == '.xcodeproj' }
  super
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**run**  ⇒ Object 
  

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/cocoapods/command/init.rb', line 44

def run
  @podfile_path.open('w') { |f| f << podfile_template(@xcode_project) }
end
```

    
  

    
      
  
### 
  
    #**validate!**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (Informative)
      
      
      
    
  

  
    
      

```

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
# File 'lib/cocoapods/command/init.rb', line 30

def validate!
  super
  raise Informative, 'Existing Podfile found in directory' unless config.podfile_path_in_dir(Pathname.pwd).nil?
  if @project_path
    help! "Xcode project at #{@project_path} does not exist" unless File.exist? @project_path
    project_path = @project_path
  else
    raise Informative, 'No Xcode project found, please specify one' unless @project_paths.length > 0
    raise Informative, 'Multiple Xcode projects found, please specify one' unless @project_paths.length == 1
    project_path = @project_paths.first
  end
  @xcode_project = Xcodeproj::Project.open(project_path)
end
```