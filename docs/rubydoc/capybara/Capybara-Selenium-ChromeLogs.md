# Module: Capybara::Selenium::ChromeLogs
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/selenium/patches/logs.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        LOG_MSG =
          
        
        

```
"Chromedriver 75+ defaults to W3C mode. Please upgrade to chromedriver >= \\\n75.0.3770.90 if you need to access logs while in W3C compliant mode.\n"

```

      
        COMMANDS =
          
        
        

```
{
  get_available_log_types: [:get, 'session/:session_id/se/log/types'],
  get_log: [:post, 'session/:session_id/se/log'],
  get_log_legacy: [:post, 'session/:session_id/log']
}.freeze

```

      
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**available_log_types**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**commands**(command)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**log**(type)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**available_log_types**  ⇒ Object 
  

  

  

  
    
      

```

21
22
23
24
25
26
```

    
    
      

```
# File 'lib/capybara/selenium/patches/logs.rb', line 21

def available_log_types
  types = execute :get_available_log_types
  Array(types).map(&:to_sym)
rescue ::Selenium::WebDriver::Error::UnknownCommandError
  raise NotImplementedError, LOG_MSG
end

```

    
  

    
      
  
### 
  
    #**commands**(command)  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/capybara/selenium/patches/logs.rb', line 17

def commands(command)
  COMMANDS[command] || super
end

```

    
  

    
      
  
### 
  
    #**log**(type)  ⇒ Object 
  

  

  

  
    
      

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
# File 'lib/capybara/selenium/patches/logs.rb', line 28

def log(type)
  data = begin
    execute :get_log, {}, type: type.to_s
  rescue ::Selenium::WebDriver::Error::UnknownCommandError
    execute :get_log_legacy, {}, type: type.to_s
  end

  Array(data).map do |l|
    ::Selenium::WebDriver::LogEntry.new l.fetch('level', 'UNKNOWN'), l.fetch('timestamp'), l.fetch('message')
  rescue KeyError
    next
  end
rescue ::Selenium::WebDriver::Error::UnknownCommandError
  raise NotImplementedError, LOG_MSG
end

```