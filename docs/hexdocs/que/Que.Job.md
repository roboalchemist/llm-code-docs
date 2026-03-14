Search
      
    
  

  
    
    
  

  

    
      
Que
      
      **
        v0.10.1
      **
    
    

      
- Pages

        
- Modules

        
- Mix Tasks

    

  

  
  

  
    

# 

    
      **
      View Source
    

  Que.Job 
  (Que v0.10.1)

  

Module to manage a Job's state and execute the worker's callbacks.

Defines a `Que.Job` struct an keeps track of the Job's worker, arguments,
status and more. Meant for internal usage, so you shouldn't use this
unless you absolutely know what you're doing.
  

    
# 
      
        **
        Link to this section
      
      Summary
    

  
    
## 
      Types
    

      
        
          status()

        

          

One of the atoms in `[:queued, :started, :failed, :completed]`

      

      
        
          t()

        

          

A `Que.Job` struct

      

  

  
    
## 
      Functions
    

      
        
          handle_failure(job, error)

        

          

Handles Job Failure, Calls appropriate worker method and updates the job
status to :failed

      

      
        
          handle_success(job)

        

          

Handles Job Success, Calls appropriate worker method and updates the job
status to :completed

      

      
        
          new(worker, args \\ nil)

        

          

Returns a new Job struct with defaults

      

      
        
          perform(job)

        

          

Updates the Job struct with new status and spawns & monitors a new Task
under the TaskSupervisor which executes the perform method with supplied
arguments

      

      
        
          set_status(job, status)

        

          

Update the Job status to one of the predefined values in `@statuses`

      

  

  

    
# 
      
        **
        Link to this section
      
Types
    

    

  
    
      **
      Link to this type
    
    
# status()

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
status() :: atom()
```

      

One of the atoms in `[:queued, :started, :failed, :completed]`
  

  
    
      **
      Link to this type
    
    
# t()

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
t() :: %Que.Job{
  arguments: term(),
  created_at: term(),
  id: term(),
  pid: term(),
  ref: term(),
  status: term(),
  updated_at: term(),
  worker: term()
}
```

      

A `Que.Job` struct
  

    
# 
      
        **
        Link to this section
      
Functions
    

    

  
    
      **
      Link to this function
    
    
# handle_failure(job, error)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
handle_failure(job :: t(), error :: term()) :: t()
```

      

Handles Job Failure, Calls appropriate worker method and updates the job
status to :failed
  

  
    
      **
      Link to this function
    
    
# handle_success(job)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
handle_success(job :: t()) :: t()
```

      

Handles Job Success, Calls appropriate worker method and updates the job
status to :completed
  

    

  
    
      **
      Link to this function
    
    
# new(worker, args \\ nil)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
new(worker :: Que.Worker.t(), args :: list()) :: t()
```

      

Returns a new Job struct with defaults
  

  
    
      **
      Link to this function
    
    
# perform(job)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
perform(job :: t()) :: t()
```

      

Updates the Job struct with new status and spawns & monitors a new Task
under the TaskSupervisor which executes the perform method with supplied
arguments
  

  
    
      **
      Link to this function
    
    
# set_status(job, status)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
set_status(job :: t(), status :: status()) :: t()
```

      

Update the Job status to one of the predefined values in `@statuses`