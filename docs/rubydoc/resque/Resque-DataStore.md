# Class: Resque::DataStore
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Resque::DataStore
          
        

        show all
      
    
  
  

  
  
  
      Extended by:
      Forwardable
  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/data_store.rb
  
  

## Overview

  
    

An interface between Resque’s persistence and the actual implementation.

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** FailedQueueAccess, QueueAccess, StatsAccess, Workers
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        HEARTBEAT_KEY =
          
        
        

```
"workers:heartbeat"
```

      
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**all_resque_keys**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an array of all known Resque keys in Redis.

  

      
        
- 
  
    
      #**decremet_stat**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**identifier**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get a string identifying the underlying server.

  

      
        
- 
  
    
      #**initialize**(redis)  ⇒ DataStore 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of DataStore.

  

      
        
- 
  
    
      #**method_missing**(sym, *args, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Compatibility with any non-Resque classes that were using Resque.redis as a way to access Redis.

  

      
        
- 
  
    
      #**reconnect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Force a reconnect to Redis without closing the connection in the parent process after a fork.

  

      
        
- 
  
    
      #**respond_to?**(method, include_all = false)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

make use respond like redis.

  

      
        
- 
  
    
      #**server_time**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(redis)  ⇒ DataStore 
  

  

  

  
    

Returns a new instance of DataStore.

  

  

  
    
      

```

9
10
11
12
13
14
15
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 9

def initialize(redis)
  @redis                = redis
  @queue_access         = QueueAccess.new(@redis)
  @failed_queue_access  = FailedQueueAccess.new(@redis)
  @workers              = Workers.new(@redis)
  @stats_access         = StatsAccess.new(@redis)
end
```

    
  

  

  
## Dynamic Method Handling

  

    This class handles dynamic methods through the method_missing method
    
  
  
    
  
### 
  
    #**method_missing**(sym, *args, &block)  ⇒ Object 
  

  

  

  
    

Compatibility with any non-Resque classes that were using Resque.redis as a way to access Redis

  

  

  
    
      

```

63
64
65
66
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 63

def method_missing(sym,*args,&block)
  # TODO: deprecation warning?
  @redis.send(sym,*args,&block)
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**all_resque_keys**  ⇒ Object 
  

  

  

  
    

Returns an array of all known Resque keys in Redis. Redis’ KEYS operation is O(N) for the keyspace, so be careful - this can be slow for big databases.

  

  

  
    
      

```

89
90
91
92
93
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 89

def all_resque_keys
  @redis.keys("*").map do |key|
    key.sub("#{@redis.namespace}:", '')
  end
end
```

    
  

    
      
  
### 
  
    #**decremet_stat**(*args)  ⇒ Object 
  

  

  

  
    
      

```

57
58
59
60
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 57

def decremet_stat(*args)
  warn '[Resque] [Deprecation] Resque::DataStore #decremet_stat method is deprecated (please use #decrement_stat)'
  decrement_stat(*args)
end
```

    
  

    
      
  
### 
  
    #**identifier**  ⇒ Object 
  

  

  

  
    

Get a string identifying the underlying server. Probably should be private, but was public so must stay public

  

  

  
    
      

```

75
76
77
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 75

def identifier
  @redis.inspect
end
```

    
  

    
      
  
### 
  
    #**reconnect**  ⇒ Object 
  

  

  

  
    

Force a reconnect to Redis without closing the connection in the parent process after a fork.

  

  

  
    
      

```

81
82
83
84
85
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 81

def reconnect
  @redis.disconnect!
  @redis.ping
  nil
end
```

    
  

    
      
  
### 
  
    #**respond_to?**(method, include_all = false)  ⇒ Boolean 
  

  

  

  
    

make use respond like redis

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

69
70
71
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 69

def respond_to?(method,include_all=false)
  @redis.respond_to?(method,include_all) || super
end
```

    
  

    
      
  
### 
  
    #**server_time**  ⇒ Object 
  

  

  

  
    
      

```

95
96
97
98
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 95

def server_time
  time, _ = @redis.time
  Time.at(time)
end
```