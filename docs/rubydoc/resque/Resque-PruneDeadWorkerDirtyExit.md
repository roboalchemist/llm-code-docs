# Exception: Resque::PruneDeadWorkerDirtyExit
  
  
  

  
  
    Inherits:
    
      DirtyExit
      
        

          
- Object
          
            
- RuntimeError
          
            
- DirtyExit
          
            
- Resque::PruneDeadWorkerDirtyExit
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/errors.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from DirtyExit

  

#process_status

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(hostname, job)  ⇒ PruneDeadWorkerDirtyExit 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of PruneDeadWorkerDirtyExit.

  

      
    

  

  
  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(hostname, job)  ⇒ PruneDeadWorkerDirtyExit 
  

  

  

  
    

Returns a new instance of PruneDeadWorkerDirtyExit.

  

  

  
    
      

```

19
20
21
22
```

    
    
      

```
# File 'lib/resque/errors.rb', line 19

def initialize(hostname, job)
  job ||= "<Unknown Job>"
  super("Worker #{hostname} did not gracefully exit while processing #{job}")
end

```