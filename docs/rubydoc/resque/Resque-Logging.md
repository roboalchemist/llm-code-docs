# Module: Resque::Logging
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Worker
  
  

  
  
    Defined in:
    lib/resque/logging.rb
  
  

## Overview

  
    

Include this module in classes you wish to have logging facilities

  

  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**debug**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Log level aliases.

  

      
        
- 
  
    
      .**error**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**fatal**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**info**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**log**(severity, message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Thunk to the logger’s own log method (if configured).

  

      
        
- 
  
    
      .**warn**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**debug**(message)  ⇒ Object 
  

  

  

  
    

Log level aliases

  

  

  
    
      

```

12
```

    
    
      

```
# File 'lib/resque/logging.rb', line 12

def debug(message); Logging.log :debug, message; end

```

    
  

    
      
  
### 
  
    .**error**(message)  ⇒ Object 
  

  

  

  
    
      

```

15
```

    
    
      

```
# File 'lib/resque/logging.rb', line 15

def error(message); Logging.log :error, message; end

```

    
  

    
      
  
### 
  
    .**fatal**(message)  ⇒ Object 
  

  

  

  
    
      

```

16
```

    
    
      

```
# File 'lib/resque/logging.rb', line 16

def fatal(message); Logging.log :fatal, message; end

```

    
  

    
      
  
### 
  
    .**info**(message)  ⇒ Object 
  

  

  

  
    
      

```

13
```

    
    
      

```
# File 'lib/resque/logging.rb', line 13

def info(message);  Logging.log :info,  message; end

```

    
  

    
      
  
### 
  
    .**log**(severity, message)  ⇒ Object 
  

  

  

  
    

Thunk to the logger’s own log method (if configured)

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/resque/logging.rb', line 7

def self.log(severity, message)
  Resque.logger.__send__(severity, message) if Resque.logger
end

```

    
  

    
      
  
### 
  
    .**warn**(message)  ⇒ Object 
  

  

  

  
    
      

```

14
```

    
    
      

```
# File 'lib/resque/logging.rb', line 14

def warn(message);  Logging.log :warn,  message; end

```