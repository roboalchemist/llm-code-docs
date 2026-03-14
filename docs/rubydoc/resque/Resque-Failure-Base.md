# Class: Resque::Failure::Base
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Resque::Failure::Base
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/failure/base.rb
  
  

## Overview

  
    

All Failure classes are expected to subclass Base.

When a job fails, a new instance of your Failure backend is created and #save is called.

  

  

  
## Direct Known Subclasses

  

Airbrake, Multiple, Redis, RedisMultiQueue

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**exception**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

The exception object raised by the failed job.

  

    
      
- 
  
    
      #**payload**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

The payload object associated with the failed job.

  

    
      
- 
  
    
      #**queue**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

The string name of the queue from which the failed job was pulled.

  

    
      
- 
  
    
      #**worker**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

The worker object who detected the failure.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**all**(offset = 0, limit = 1, queue = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns a paginated array of failure objects.

  

      
        
- 
  
    
      .**clear**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Clear all failure objects.

  

      
        
- 
  
    
      .**count**(queue = nil, class_name = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The number of failures.

  

      
        
- 
  
    
      .**each**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Iterate across failed objects.

  

      
        
- 
  
    
      .**queues**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an array of all available failure queues.

  

      
        
- 
  
    
      .**remove**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**requeue**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**url**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

A URL where someone can go to view failures.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(exception, worker, queue, payload)  ⇒ Base 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Base.

  

      
        
- 
  
    
      #**log**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Logging!.

  

      
        
- 
  
    
      #**save**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

When a job fails, a new instance of your Failure backend is created and #save is called.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(exception, worker, queue, payload)  ⇒ Base 
  

  

  

  
    

Returns a new instance of Base.

  

  

  
    
      

```

20
21
22
23
24
25
```

    
    
      

```
# File 'lib/resque/failure/base.rb', line 20

def initialize(exception, worker, queue, payload)
  @exception = exception
  @worker    = worker
  @queue     = queue
  @payload   = payload
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**exception**  ⇒ Object 
  

  

  

  
    

The exception object raised by the failed job

  

  

  
    
      

```

9
10
11
```

    
    
      

```
# File 'lib/resque/failure/base.rb', line 9

def exception
  @exception
end
```

    
  

    
      
      
      
  
### 
  
    #**payload**  ⇒ Object 
  

  

  

  
    

The payload object associated with the failed job

  

  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/resque/failure/base.rb', line 18

def payload
  @payload
end
```

    
  

    
      
      
      
  
### 
  
    #**queue**  ⇒ Object 
  

  

  

  
    

The string name of the queue from which the failed job was pulled

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/resque/failure/base.rb', line 15

def queue
  @queue
end
```

    
  

    
      
      
      
  
### 
  
    #**worker**  ⇒ Object 
  

  

  

  
    

The worker object who detected the failure

  

  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/resque/failure/base.rb', line 12

def worker
  @worker
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**all**(offset = 0, limit = 1, queue = nil)  ⇒ Object 
  

  

  

  
    

Returns a paginated array of failure objects.

  

  

  
    
      

```

45
46
47
```

    
    
      

```
# File 'lib/resque/failure/base.rb', line 45

def self.all(offset = 0, limit = 1, queue = nil)
  []
end
```

    
  

    
      
  
### 
  
    .**clear**(*args)  ⇒ Object 
  

  

  

  
    

Clear all failure objects

  

  

  
    
      

```

58
59
```

    
    
      

```
# File 'lib/resque/failure/base.rb', line 58

def self.clear(*args)
end
```

    
  

    
      
  
### 
  
    .**count**(queue = nil, class_name = nil)  ⇒ Object 
  

  

  

  
    

The number of failures.

  

  

  
    
      

```

35
36
37
```

    
    
      

```
# File 'lib/resque/failure/base.rb', line 35

def self.count(queue = nil, class_name = nil)
  0
end
```

    
  

    
      
  
### 
  
    .**each**(*args)  ⇒ Object 
  

  

  

  
    

Iterate across failed objects

  

  

  
    
      

```

50
51
```

    
    
      

```
# File 'lib/resque/failure/base.rb', line 50

def self.each(*args)
end
```

    
  

    
      
  
### 
  
    .**queues**  ⇒ Object 
  

  

  

  
    

Returns an array of all available failure queues

  

  

  
    
      

```

40
41
42
```

    
    
      

```
# File 'lib/resque/failure/base.rb', line 40

def self.queues
  []
end
```

    
  

    
      
  
### 
  
    .**remove**(*args)  ⇒ Object 
  

  

  

  
    
      

```

64
65
```

    
    
      

```
# File 'lib/resque/failure/base.rb', line 64

def self.remove(*args)
end
```

    
  

    
      
  
### 
  
    .**requeue**(*args)  ⇒ Object 
  

  

  

  
    
      

```

61
62
```

    
    
      

```
# File 'lib/resque/failure/base.rb', line 61

def self.requeue(*args)
end
```

    
  

    
      
  
### 
  
    .**url**  ⇒ Object 
  

  

  

  
    

A URL where someone can go to view failures.

  

  

  
    
      

```

54
55
```

    
    
      

```
# File 'lib/resque/failure/base.rb', line 54

def self.url
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**log**(message)  ⇒ Object 
  

  

  

  
    

Logging!

  

  

  
    
      

```

68
69
70
```

    
    
      

```
# File 'lib/resque/failure/base.rb', line 68

def log(message)
  @worker.log(message)
end
```

    
  

    
      
  
### 
  
    #**save**  ⇒ Object 
  

  

  

  
    

When a job fails, a new instance of your Failure backend is created and #save is called.

This is where you POST or PUT or whatever to your Failure service.

  

  

  
    
      

```

31
32
```

    
    
      

```
# File 'lib/resque/failure/base.rb', line 31

def save
end
```