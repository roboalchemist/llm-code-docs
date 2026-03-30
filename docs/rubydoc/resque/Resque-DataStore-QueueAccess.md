# Class: Resque::DataStore::QueueAccess
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Resque::DataStore::QueueAccess
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/data_store.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**everything_in_queue**(queue)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(redis)  ⇒ QueueAccess 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of QueueAccess.

  

      
        
- 
  
    
      #**list_range**(key, start = 0, count = 1)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Private: do not call.

  

      
        
- 
  
    
      #**peek_in_queue**(queue, start = 0, count = 1)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Examine items in the queue.

  

      
        
- 
  
    
      #**pop_from_queue**(queue)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Pop whatever is on queue.

  

      
        
- 
  
    
      #**push_to_queue**(queue, encoded_item)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**queue_names**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**queue_size**(queue)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the number of items in the queue.

  

      
        
- 
  
    
      #**remove_from_queue**(queue, data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Remove data from the queue, if it’s there, returning the number of removed elements.

  

      
        
- 
  
    
      #**remove_queue**(queue)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**watch_queue**(queue, redis: @redis)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Private: do not call.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(redis)  ⇒ QueueAccess 
  

  

  

  
    

Returns a new instance of QueueAccess.

  

  

  
    
      

```

101
102
103
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 101

def initialize(redis)
  @redis = redis
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**everything_in_queue**(queue)  ⇒ Object 
  

  

  

  
    
      

```

140
141
142
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 140

def everything_in_queue(queue)
  @redis.lrange(redis_key_for_queue(queue), 0, -1)
end
```

    
  

    
      
  
### 
  
    #**list_range**(key, start = 0, count = 1)  ⇒ Object 
  

  

  

  
    

Private: do not call

  

  

  
    
      

```

155
156
157
158
159
160
161
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 155

def list_range(key, start = 0, count = 1)
  if count == 1
    @redis.lindex(key, start)
  else
    Array(@redis.lrange(key, start, start+count-1))
  end
end
```

    
  

    
      
  
### 
  
    #**peek_in_queue**(queue, start = 0, count = 1)  ⇒ Object 
  

  

  

  
    

Examine items in the queue.

NOTE: if count is 1, you will get back an object, otherwise you will

```
get an Array.  I'm not making this up.

```

  

  

  
    
      

```

125
126
127
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 125

def peek_in_queue(queue, start = 0, count = 1)
  list_range(redis_key_for_queue(queue), start, count)
end
```

    
  

    
      
  
### 
  
    #**pop_from_queue**(queue)  ⇒ Object 
  

  

  

  
    

Pop whatever is on queue

  

  

  
    
      

```

112
113
114
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 112

def pop_from_queue(queue)
  @redis.lpop(redis_key_for_queue(queue))
end
```

    
  

    
      
  
### 
  
    #**push_to_queue**(queue, encoded_item)  ⇒ Object 
  

  

  

  
    
      

```

104
105
106
107
108
109
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 104

def push_to_queue(queue,encoded_item)
  @redis.pipelined do |piped|
    watch_queue(queue, redis: piped)
    piped.rpush redis_key_for_queue(queue), encoded_item
  end
end
```

    
  

    
      
  
### 
  
    #**queue_names**  ⇒ Object 
  

  

  

  
    
      

```

129
130
131
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 129

def queue_names
  Array(@redis.smembers(:queues))
end
```

    
  

    
      
  
### 
  
    #**queue_size**(queue)  ⇒ Object 
  

  

  

  
    

Get the number of items in the queue

  

  

  
    
      

```

117
118
119
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 117

def queue_size(queue)
  @redis.llen(redis_key_for_queue(queue)).to_i
end
```

    
  

    
      
  
### 
  
    #**remove_from_queue**(queue, data)  ⇒ Object 
  

  

  

  
    

Remove data from the queue, if it’s there, returning the number of removed elements

  

  

  
    
      

```

145
146
147
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 145

def remove_from_queue(queue,data)
  @redis.lrem(redis_key_for_queue(queue), 0, data)
end
```

    
  

    
      
  
### 
  
    #**remove_queue**(queue)  ⇒ Object 
  

  

  

  
    
      

```

133
134
135
136
137
138
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 133

def remove_queue(queue)
  @redis.pipelined do |piped|
    piped.srem(:queues, [queue.to_s])
    piped.del(redis_key_for_queue(queue))
  end
end
```

    
  

    
      
  
### 
  
    #**watch_queue**(queue, redis: @redis)  ⇒ Object 
  

  

  

  
    

Private: do not call

  

  

  
    
      

```

150
151
152
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 150

def watch_queue(queue, redis: @redis)
  redis.sadd(:queues, [queue.to_s])
end
```