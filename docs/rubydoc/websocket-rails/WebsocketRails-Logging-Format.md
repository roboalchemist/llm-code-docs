# Module: WebsocketRails::Logging::Format
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/logging.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**format**(severity, time, progname, msg)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**format_time**(time)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**format**(severity, time, progname, msg)  ⇒ Object 
  

  

  

  
    
      

```

122
123
124
```

    
    
      

```
# File 'lib/websocket_rails/logging.rb', line 122

def format(severity, time, progname, msg)
  "#{severity[0, 1]} [#{format_time(time)}] #{msg}\n"
end
```

    
  

    
      
  
### 
  
    .**format_time**(time)  ⇒ Object 
  

  

  

  
    
      

```

126
127
128
```

    
    
      

```
# File 'lib/websocket_rails/logging.rb', line 126

def format_time(time)
  time.strftime("%Y-%m-%d %H:%M:%S.") << time.usec.to_s[0, 3]
end
```