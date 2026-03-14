# Class: ActiveJob::QueueAdapters::ResqueAdapter
  
  
  

  
  
    Inherits:
    
      AbstractAdapter
      
        

          
- Object
          
            
- AbstractAdapter
          
            
- ActiveJob::QueueAdapters::ResqueAdapter
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/active_job/queue_adapters/resque_adapter.rb
  
  

## Overview

  
    

# Resque adapter for Active Job

Resque (pronounced like “rescue”) is a Redis-backed library for creating background jobs, placing those jobs on multiple queues, and processing them later.

Read more about Resque here.

To use Resque set the queue_adapter config to `:resque`.

```
Rails.application.config.active_job.queue_adapter = :resque

```

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** JobWrapper
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**enqueue**(job)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**enqueue_at**(job, timestamp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**enqueue**(job)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

32
33
34
35
```

    
    
      

```
# File 'lib/active_job/queue_adapters/resque_adapter.rb', line 32

def enqueue(job) # :nodoc:
  JobWrapper.instance_variable_set(:@queue, job.queue_name)
  Resque.enqueue_to job.queue_name, JobWrapper, job.serialize
end
```

    
  

    
      
  
### 
  
    #**enqueue_at**(job, timestamp)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

37
38
39
40
41
42
43
```

    
    
      

```
# File 'lib/active_job/queue_adapters/resque_adapter.rb', line 37

def enqueue_at(job, timestamp) # :nodoc:
  unless Resque.respond_to?(:enqueue_at_with_queue)
    raise NotImplementedError, "To be able to schedule jobs with Resque you need the " \
      "resque-scheduler gem. Please add it to your Gemfile and run bundle install"
  end
  Resque.enqueue_at_with_queue job.queue_name, timestamp, JobWrapper, job.serialize
end
```