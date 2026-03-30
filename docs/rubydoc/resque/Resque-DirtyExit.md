# Exception: Resque::DirtyExit
  
  
  

  
  
    Inherits:
    
      RuntimeError
      
        

          
- Object
          
            
- RuntimeError
          
            
- Resque::DirtyExit
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/errors.rb
  
  

## Overview

  
    

Raised when a worker was killed while processing a job.

  

  

  
## Direct Known Subclasses

  

PruneDeadWorkerDirtyExit

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**process_status**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute process_status.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(message = nil, process_status = nil)  ⇒ DirtyExit 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of DirtyExit.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(message = nil, process_status = nil)  ⇒ DirtyExit 
  

  

  

  
    
      

```

12
13
14
15
```

    
    
      

```
# File 'lib/resque/errors.rb', line 12

def initialize(message=nil, process_status=nil)
  @process_status = process_status
  super message
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**process_status**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute process_status.

  

  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/resque/errors.rb', line 10

def process_status
  @process_status
end

```