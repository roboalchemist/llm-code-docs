# Class: ActiveJob::QueueAdapters::ResqueAdapter::JobWrapper
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- ActiveJob::QueueAdapters::ResqueAdapter::JobWrapper
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/active_job/queue_adapters/resque_adapter.rb
  
  

## Overview

  
    

:nodoc:

  

  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**perform**(job_data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**perform**(job_data)  ⇒ Object 
  

  

  

  
    
      

```

47
48
49
```

    
    
      

```
# File 'lib/active_job/queue_adapters/resque_adapter.rb', line 47

def perform(job_data)
  ::ActiveJob::Base.execute job_data
end
```