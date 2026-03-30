# Module: Resque::Failure
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/failure.rb,

  lib/resque/failure/base.rb,
 lib/resque/failure/redis.rb,
 lib/resque/failure/airbrake.rb,
 lib/resque/failure/multiple.rb,
 lib/resque/failure/redis_multi_queue.rb

  
  

## Overview

  
    

The Failure module provides an interface for working with different failure backends.

You can use it to query the failure backend without knowing which specific backend is being used. For instance, the Resque web app uses it to display stats and other information.

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** Airbrake, Base, Multiple, Redis, RedisMultiQueue
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**all**(offset = 0, limit = 1, queue = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an array of all the failures, paginated.

  

      
        
- 
  
    
      .**backend**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the current backend class.

  

      
        
- 
  
    
      .**backend=**(backend)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Sets the current backend.

  

      
        
- 
  
    
      .**clear**(queue = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Clear all failure jobs.

  

      
        
- 
  
    
      .**clear_retried**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**count**(queue = nil, class_name = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the int count of how many failures we have seen.

  

      
        
- 
  
    
      .**create**(options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Creates a new failure, which is delegated to the appropriate backend.

  

      
        
- 
  
    
      .**each**(offset = 0, limit = self.count, queue = nil, class_name = nil, order = 'desc', &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Iterate across all failures with the given options.

  

      
        
- 
  
    
      .**failure_queue_name**(job_queue_name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Obtain the failure queue name for a given job queue.

  

      
        
- 
  
    
      .**job_queue_name**(failure_queue_name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Obtain the job queue name for a given failure queue.

  

      
        
- 
  
    
      .**queues**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an array of all the failed queues in the system.

  

      
        
- 
  
    
      .**remove**(id, queue = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**remove_queue**(queue)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Removes all failed jobs in a specific queue.

  

      
        
- 
  
    
      .**requeue**(id, queue = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**requeue_all**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Requeues all failed jobs.

  

      
        
- 
  
    
      .**requeue_queue**(queue)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Requeues all failed jobs in a specific queue.

  

      
        
- 
  
    
      .**url**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The string url of the backend’s web interface, if any.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**all**(offset = 0, limit = 1, queue = nil)  ⇒ Object 
  

  

  

  
    

Returns an array of all the failures, paginated.

`offset` is the int of the first item in the page, `limit` is the number of items to return.

  

  

  
    
      

```

75
76
77
```

    
    
      

```
# File 'lib/resque/failure.rb', line 75

def self.all(offset = 0, limit = 1, queue = nil)
  backend.all(offset, limit, queue)
end
```

    
  

    
      
  
### 
  
    .**backend**  ⇒ Object 
  

  

  

  
    

Returns the current backend class. If none has been set, falls back to `Resque::Failure::Redis`

  

  

  
    
      

```

34
35
36
37
38
39
40
41
42
43
44
45
46
47
```

    
    
      

```
# File 'lib/resque/failure.rb', line 34

def self.backend
  return @backend if @backend

  case ENV['FAILURE_BACKEND']
  when 'redis_multi_queue'
    require 'resque/failure/redis_multi_queue'
    @backend = Failure::RedisMultiQueue
  when 'redis', nil
    require 'resque/failure/redis'
    @backend = Failure::Redis
  else
    raise ArgumentError, "invalid failure backend: #{FAILURE_BACKEND}"
  end
end
```

    
  

    
      
  
### 
  
    .**backend=**(backend)  ⇒ Object 
  

  

  

  
    

Sets the current backend. Expects a class descendent of `Resque::Failure::Base`.

Example use:

```
require 'resque/failure/airbrake'
Resque::Failure.backend = Resque::Failure::Airbrake

```

  

  

  
    
      

```

27
28
29
```

    
    
      

```
# File 'lib/resque/failure.rb', line 27

def self.backend=(backend)
  @backend = backend
end
```

    
  

    
      
  
### 
  
    .**clear**(queue = nil)  ⇒ Object 
  

  

  

  
    

Clear all failure jobs

  

  

  
    
      

```

90
91
92
```

    
    
      

```
# File 'lib/resque/failure.rb', line 90

def self.clear(queue = nil)
  backend.clear(queue)
end
```

    
  

    
      
  
### 
  
    .**clear_retried**  ⇒ Object 
  

  

  

  
    
      

```

94
95
96
97
98
```

    
    
      

```
# File 'lib/resque/failure.rb', line 94

def self.clear_retried
  each do |index, job|
    remove(index) unless job['retried_at'].nil?
  end
end
```

    
  

    
      
  
### 
  
    .**count**(queue = nil, class_name = nil)  ⇒ Object 
  

  

  

  
    

Returns the int count of how many failures we have seen.

  

  

  
    
      

```

67
68
69
```

    
    
      

```
# File 'lib/resque/failure.rb', line 67

def self.count(queue = nil, class_name = nil)
  backend.count(queue, class_name)
end
```

    
  

    
      
  
### 
  
    .**create**(options = {})  ⇒ Object 
  

  

  

  
    

Creates a new failure, which is delegated to the appropriate backend.

Expects a hash with the following keys:

```
:exception - The Exception object
:worker    - The Worker object who is reporting the failure
:queue     - The string name of the queue from which the job was pulled
:payload   - The job's payload

```

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/resque/failure.rb', line 16

def self.create(options = {})
  backend.new(*options.values_at(:exception, :worker, :queue, :payload)).save
end
```

    
  

    
      
  
### 
  
    .**each**(offset = 0, limit = self.count, queue = nil, class_name = nil, order = 'desc', &block)  ⇒ Object 
  

  

  

  
    

Iterate across all failures with the given options

  

  

  
    
      

```

80
81
82
```

    
    
      

```
# File 'lib/resque/failure.rb', line 80

def self.each(offset = 0, limit = self.count, queue = nil, class_name = nil, order = 'desc', &block)
  backend.each(offset, limit, queue, class_name, order, &block)
end
```

    
  

    
      
  
### 
  
    .**failure_queue_name**(job_queue_name)  ⇒ Object 
  

  

  

  
    

Obtain the failure queue name for a given job queue

  

  

  
    
      

```

50
51
52
53
54
```

    
    
      

```
# File 'lib/resque/failure.rb', line 50

def self.failure_queue_name(job_queue_name)
  name = "#{job_queue_name}_failed"
  Resque.data_store.add_failed_queue(name)
  name
end
```

    
  

    
      
  
### 
  
    .**job_queue_name**(failure_queue_name)  ⇒ Object 
  

  

  

  
    

Obtain the job queue name for a given failure queue

  

  

  
    
      

```

57
58
59
```

    
    
      

```
# File 'lib/resque/failure.rb', line 57

def self.job_queue_name(failure_queue_name)
  failure_queue_name.sub(/_failed$/, '')
end
```

    
  

    
      
  
### 
  
    .**queues**  ⇒ Object 
  

  

  

  
    

Returns an array of all the failed queues in the system

  

  

  
    
      

```

62
63
64
```

    
    
      

```
# File 'lib/resque/failure.rb', line 62

def self.queues
  backend.queues
end
```

    
  

    
      
  
### 
  
    .**remove**(id, queue = nil)  ⇒ Object 
  

  

  

  
    
      

```

104
105
106
```

    
    
      

```
# File 'lib/resque/failure.rb', line 104

def self.remove(id, queue = nil)
  backend.remove(id, queue)
end
```

    
  

    
      
  
### 
  
    .**remove_queue**(queue)  ⇒ Object 
  

  

  

  
    

Removes all failed jobs in a specific queue. Queue name should be a string.

  

  

  
    
      

```

121
122
123
```

    
    
      

```
# File 'lib/resque/failure.rb', line 121

def self.remove_queue(queue)
  backend.remove_queue(queue)
end
```

    
  

    
      
  
### 
  
    .**requeue**(id, queue = nil)  ⇒ Object 
  

  

  

  
    
      

```

100
101
102
```

    
    
      

```
# File 'lib/resque/failure.rb', line 100

def self.requeue(id, queue = nil)
  backend.requeue(id, queue)
end
```

    
  

    
      
  
### 
  
    .**requeue_all**  ⇒ Object 
  

  

  

  
    

Requeues all failed jobs

  

  

  
    
      

```

115
116
117
```

    
    
      

```
# File 'lib/resque/failure.rb', line 115

def self.requeue_all
  backend.requeue_all
end
```

    
  

    
      
  
### 
  
    .**requeue_queue**(queue)  ⇒ Object 
  

  

  

  
    

Requeues all failed jobs in a specific queue. Queue name should be a string.

  

  

  
    
      

```

110
111
112
```

    
    
      

```
# File 'lib/resque/failure.rb', line 110

def self.requeue_queue(queue)
  backend.requeue_queue(queue)
end
```

    
  

    
      
  
### 
  
    .**url**  ⇒ Object 
  

  

  

  
    

The string url of the backend’s web interface, if any.

  

  

  
    
      

```

85
86
87
```

    
    
      

```
# File 'lib/resque/failure.rb', line 85

def self.url
  backend.url
end
```