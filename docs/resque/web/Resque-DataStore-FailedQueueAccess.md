# Class: Resque::DataStore::FailedQueueAccess
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Resque::DataStore::FailedQueueAccess
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/data_store.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**add_failed_queue**(failed_queue_name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**clear_failed_queue**(failed_queue_name = :failed)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**failed_queue_names**(find_queue_names_in_key = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(redis)  ⇒ FailedQueueAccess 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of FailedQueueAccess.

  

      
        
- 
  
    
      #**num_failed**(failed_queue_name = :failed)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**push_to_failed_queue**(data, failed_queue_name = :failed)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**remove_failed_queue**(failed_queue_name = :failed)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**remove_from_failed_queue**(index_in_failed_queue, failed_queue_name = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**update_item_in_failed_queue**(index_in_failed_queue, new_item_data, failed_queue_name = :failed)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(redis)  ⇒ FailedQueueAccess 
  

  

  

  
    

Returns a new instance of FailedQueueAccess.

  

  

  
    
      

```

172
173
174
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 172

def initialize(redis)
  @redis = redis
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_failed_queue**(failed_queue_name)  ⇒ Object 
  

  

  

  
    
      

```

176
177
178
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 176

def add_failed_queue(failed_queue_name)
  @redis.sadd(:failed_queues, [failed_queue_name])
end
```

    
  

    
      
  
### 
  
    #**clear_failed_queue**(failed_queue_name = :failed)  ⇒ Object 
  

  

  

  
    
      

```

200
201
202
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 200

def clear_failed_queue(failed_queue_name=:failed)
  @redis.del(failed_queue_name)
end
```

    
  

    
      
  
### 
  
    #**failed_queue_names**(find_queue_names_in_key = nil)  ⇒ Object 
  

  

  

  
    
      

```

188
189
190
191
192
193
194
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 188

def failed_queue_names(find_queue_names_in_key=nil)
  if find_queue_names_in_key.nil?
    [:failed]
  else
    Array(@redis.smembers(find_queue_names_in_key))
  end
end
```

    
  

    
      
  
### 
  
    #**num_failed**(failed_queue_name = :failed)  ⇒ Object 
  

  

  

  
    
      

```

184
185
186
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 184

def num_failed(failed_queue_name=:failed)
  @redis.llen(failed_queue_name).to_i
end
```

    
  

    
      
  
### 
  
    #**push_to_failed_queue**(data, failed_queue_name = :failed)  ⇒ Object 
  

  

  

  
    
      

```

196
197
198
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 196

def push_to_failed_queue(data,failed_queue_name=:failed)
  @redis.rpush(failed_queue_name,data)
end
```

    
  

    
      
  
### 
  
    #**remove_failed_queue**(failed_queue_name = :failed)  ⇒ Object 
  

  

  

  
    
      

```

180
181
182
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 180

def remove_failed_queue(failed_queue_name=:failed)
  @redis.del(failed_queue_name)
end
```

    
  

    
      
  
### 
  
    #**remove_from_failed_queue**(index_in_failed_queue, failed_queue_name = nil)  ⇒ Object 
  

  

  

  
    
      

```

208
209
210
211
212
213
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 208

def remove_from_failed_queue(index_in_failed_queue,failed_queue_name=nil)
  failed_queue_name ||= :failed
  hopefully_unique_value_we_can_use_to_delete_job = ""
  @redis.lset(failed_queue_name, index_in_failed_queue, hopefully_unique_value_we_can_use_to_delete_job)
  @redis.lrem(failed_queue_name, 1,                     hopefully_unique_value_we_can_use_to_delete_job)
end
```

    
  

    
      
  
### 
  
    #**update_item_in_failed_queue**(index_in_failed_queue, new_item_data, failed_queue_name = :failed)  ⇒ Object 
  

  

  

  
    
      

```

204
205
206
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 204

def update_item_in_failed_queue(index_in_failed_queue,new_item_data,failed_queue_name=:failed)
  @redis.lset(failed_queue_name, index_in_failed_queue, new_item_data)
end
```