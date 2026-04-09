# Class: Pod::Command::Env
  
    Inherits:
    
      Pod::Command
      
        

          
- Object

- CLAide::Command

- Pod::Command

- Pod::Command::Env

        show all
      

    Defined in:
    lib/cocoapods/command/env.rb
  
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(argv)  ⇒ Env 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Env.

-
  
      #**markdown_podfile**  ⇒ Object 

-
  
      #**plugins_string**  ⇒ Object 

-
  
      #**report**  ⇒ Object 

-
  
      #**run**  ⇒ Object 

-
  
      #**stack**  ⇒ Object 

### Methods inherited from Pod::Command

# ensure_master_spec_repo_exists!, ensure_not_root_or_allowed!, report_error, run

### Methods included from Pod::Config::Mixin

# config

## Constructor Details

###
  
    #**initialize**(argv)  ⇒ Env 
  

  

  

  
    

Returns a new instance of Env.

```

14
15
16
17
```

```
# File 'lib/cocoapods/command/env.rb', line 14

def initialize(argv)
  super
  config.silent = false
end
```

## Class Method Details

###
  
    .**options**  ⇒ Object 
  

  

  

  
    
      

```

9
10
11
12
```

```
# File 'lib/cocoapods/command/env.rb', line 9

def self.options
  options = []
  options.concat(super.reject { |option, _| option == '--silent' })
end
```

## Instance Method Details

###
  
    #**markdown_podfile**  ⇒ Object 
  

  

  

  
    
      

```

41
42
43
```

```
# File 'lib/cocoapods/command/env.rb', line 41

def markdown_podfile
  UI::ErrorReport.markdown_podfile
end
```

###
  
    #**plugins_string**  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
```

```
# File 'lib/cocoapods/command/env.rb', line 45

def plugins_string
  UI::ErrorReport.plugins_string
end
```

###
  
    #**report**  ⇒ Object 
  

  

  

  
    
      

```

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
```

```
# File 'lib/cocoapods/command/env.rb', line 23

def report
  <<-EOS

#{stack}
#{executable_path}
### Plugins

```

# {plugins_string}

```
#{markdown_podfile}
EOS
end
```

###
  
    #**run**  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
```

```
# File 'lib/cocoapods/command/env.rb', line 19

def run
  UI.puts report
end
```

###
  
    #**stack**  ⇒ Object 
  

  

  

  
    
      

```

37
38
39
```

```
# File 'lib/cocoapods/command/env.rb', line 37

def stack
  UI::ErrorReport.stack
end
```
