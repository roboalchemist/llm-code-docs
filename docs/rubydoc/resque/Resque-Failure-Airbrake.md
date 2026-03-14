# Class: Resque::Failure::Airbrake
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- Resque::Failure::Airbrake
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/failure/airbrake.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#exception, #payload, #queue, #worker

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**configure**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**count**(queue = nil, class_name = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**save**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

all, clear, each, #initialize, #log, queues, remove, requeue, url

  
## Constructor Details

  
    

This class inherits a constructor from Resque::Failure::Base
  

  
    
## Class Method Details

    
      
  
### 
  
    .**configure**(&block)  ⇒ Object 
  

  

  

  
    
      

```

10
11
12
13
14
15
```

    
    
      

```
# File 'lib/resque/failure/airbrake.rb', line 10

def self.configure(&block)
  Resque.logger.warn "This actually sets global Airbrake configuration, " \
    "which is probably not what you want."
  Resque::Failure.backend = self
  ::Airbrake.configure(&block)
end
```

    
  

    
      
  
### 
  
    .**count**(queue = nil, class_name = nil)  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
20
21
```

    
    
      

```
# File 'lib/resque/failure/airbrake.rb', line 17

def self.count(queue = nil, class_name = nil)
  # We can't get the total # of errors from Airbrake so we fake it
  # by asking Resque how many errors it has seen.
  Stat[:failed]
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**save**  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/resque/failure/airbrake.rb', line 23

def save
  notify(
    exception,
    parameters: {
      payload_class: payload['class'].to_s,
      payload_args: payload['args'].inspect
    }
  )
end
```