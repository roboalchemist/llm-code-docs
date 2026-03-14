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
    

  Que.Queue 
  (Que v0.10.1)

  

Module to manage a Queue comprising of multiple jobs.

Responsible for queueing (duh), executing and handling callbacks,
for `Que.Job`s of a specific `Que.Worker`. Also keeps track of
running jobs and processes them concurrently (if the worker is
configured so).

Meant for internal usage, so you shouldn't use this unless you
absolutely know what you're doing.
  

    
# 
      
        **
        Link to this section
      
      Summary
    

  
    
## 
      Types
    

      
        
          t()

        

          

A `Que.Queue` struct

      

  

  
    
## 
      Functions
    

      
        
          fetch(q)

        

          

Fetches the next Job in queue and returns a queue and Job tuple

      

      
        
          find(queue, key \\ :id, value)

        

          

Finds the Job in Queue by the specified key name and value.

      

      
        
          new(worker, jobs \\ [])

        

          

Returns a new processable Queue with defaults

      

      
        
          process(q)

        

          

Processes the Queue and runs pending jobs

      

      
        
          put(q, jobs)

        

          

Adds one or more Jobs to the `queued` list

      

      
        
          queued(queue)

        

          

Returns queued jobs in the Queue

      

      
        
          remove(q, job)

        

          

Removes the specified Job from `running`

      

      
        
          running(queue)

        

          

Returns running jobs in the Queue

      

      
        
          update(q, job)

        

          

Finds a Job in the Queue by the given Job's id, replaces it and
returns an updated Queue

      

  

  

    
# 
      
        **
        Link to this section
      
Types
    

    

  
    
      **
      Link to this type
    
    
# t()

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
t() :: %Que.Queue{queued: term(), running: term(), worker: term()}
```

      

A `Que.Queue` struct
  

    
# 
      
        **
        Link to this section
      
Functions
    

    

  
    
      **
      Link to this function
    
    
# fetch(q)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
fetch(queue :: t()) :: {t(), Que.Job.t() | nil}
```

      

Fetches the next Job in queue and returns a queue and Job tuple
  

    

  
    
      **
      Link to this function
    
    
# find(queue, key \\ :id, value)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
find(queue :: t(), key :: atom(), value :: term()) :: Que.Job.t() | nil
```

      

Finds the Job in Queue by the specified key name and value.

If no key is specified, it's assumed to be an `:id`. If the
specified key is a :ref, it only searches in the `:running`
list.
  

    

  
    
      **
      Link to this function
    
    
# new(worker, jobs \\ [])

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
new(worker :: Que.Worker.t(), jobs :: [Que.Job.t()]) :: t()
```

      

Returns a new processable Queue with defaults
  

  
    
      **
      Link to this function
    
    
# process(q)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
process(queue :: t()) :: t()
```

      

Processes the Queue and runs pending jobs
  

  
    
      **
      Link to this function
    
    
# put(q, jobs)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
put(queue :: t(), jobs :: Que.Job.t() | [Que.Job.t()]) :: t()
```

      

Adds one or more Jobs to the `queued` list
  

  
    
      **
      Link to this function
    
    
# queued(queue)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
queued(queue :: t()) :: [Que.Job.t()]
```

      

Returns queued jobs in the Queue
  

  
    
      **
      Link to this function
    
    
# remove(q, job)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
remove(queue :: t(), job :: Que.Job.t()) :: t()
```

      

Removes the specified Job from `running`
  

  
    
      **
      Link to this function
    
    
# running(queue)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
running(queue :: t()) :: [Que.Job.t()]
```

      

Returns running jobs in the Queue
  

  
    
      **
      Link to this function
    
    
# update(q, job)

      
       **
       View Source
     

  

  

      
## Specs

      

          

```
update(queue :: t(), job :: Que.Job.t()) :: t()
```

      

Finds a Job in the Queue by the given Job's id, replaces it and
returns an updated Queue