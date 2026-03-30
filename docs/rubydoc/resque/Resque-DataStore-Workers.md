# Class: Resque::DataStore::Workers
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Resque::DataStore::Workers
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/data_store.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**acquire_pruning_dead_worker_lock**(worker, expiry)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**all_heartbeats**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**get_worker_payload**(worker_id)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

return the worker’s payload i.e.

  

      
        
- 
  
    
      #**heartbeat**(worker)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**heartbeat!**(worker, time)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(redis)  ⇒ Workers 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Workers.

  

      
        
- 
  
    
      #**register_worker**(worker)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**remove_heartbeat**(worker)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**set_worker_payload**(worker, data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**unregister_worker**(worker, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**worker_done_working**(worker, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**worker_exists?**(worker_id)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**worker_ids**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**worker_start_time**(worker)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**worker_started**(worker, redis: @redis)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**workers_map**(worker_ids)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a list of worker ids, returns a map of those ids to the worker’s value in redis, even if that value maps to nil.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(redis)  ⇒ Workers 
  

  

  

  
    

Returns a new instance of Workers.

  

  

  
    
      

```

217
218
219
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 217

def initialize(redis)
  @redis = redis
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**acquire_pruning_dead_worker_lock**(worker, expiry)  ⇒ Object 
  

  

  

  
    
      

```

280
281
282
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 280

def acquire_pruning_dead_worker_lock(worker, expiry)
  @redis.set(redis_key_for_worker_pruning, worker.to_s, :ex => expiry, :nx => true)
end
```

    
  

    
      
  
### 
  
    #**all_heartbeats**  ⇒ Object 
  

  

  

  
    
      

```

276
277
278
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 276

def all_heartbeats
  @redis.hgetall(HEARTBEAT_KEY)
end
```

    
  

    
      
  
### 
  
    #**get_worker_payload**(worker_id)  ⇒ Object 
  

  

  

  
    

return the worker’s payload i.e. job

  

  

  
    
      

```

233
234
235
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 233

def get_worker_payload(worker_id)
  @redis.get("worker:#{worker_id}")
end
```

    
  

    
      
  
### 
  
    #**heartbeat**(worker)  ⇒ Object 
  

  

  

  
    
      

```

267
268
269
270
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 267

def heartbeat(worker)
  heartbeat = @redis.hget(HEARTBEAT_KEY, worker.to_s)
  heartbeat && Time.parse(heartbeat)
end
```

    
  

    
      
  
### 
  
    #**heartbeat!**(worker, time)  ⇒ Object 
  

  

  

  
    
      

```

272
273
274
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 272

def heartbeat!(worker, time)
  @redis.hset(HEARTBEAT_KEY, worker.to_s, time.iso8601)
end
```

    
  

    
      
  
### 
  
    #**register_worker**(worker)  ⇒ Object 
  

  

  

  
    
      

```

241
242
243
244
245
246
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 241

def register_worker(worker)
  @redis.pipelined do |piped|
    piped.sadd(:workers, [worker.id])
    worker_started(worker, redis: piped)
  end
end
```

    
  

    
      
  
### 
  
    #**remove_heartbeat**(worker)  ⇒ Object 
  

  

  

  
    
      

```

263
264
265
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 263

def remove_heartbeat(worker)
  @redis.hdel(HEARTBEAT_KEY, worker.to_s)
end
```

    
  

    
      
  
### 
  
    #**set_worker_payload**(worker, data)  ⇒ Object 
  

  

  

  
    
      

```

284
285
286
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 284

def set_worker_payload(worker, data)
  @redis.set(redis_key_for_worker(worker), data)
end
```

    
  

    
      
  
### 
  
    #**unregister_worker**(worker, &block)  ⇒ Object 
  

  

  

  
    
      

```

252
253
254
255
256
257
258
259
260
261
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 252

def unregister_worker(worker, &block)
  @redis.pipelined do |piped|
    piped.srem(:workers, [worker.id])
    piped.del(redis_key_for_worker(worker))
    piped.del(redis_key_for_worker_start_time(worker))
    piped.hdel(HEARTBEAT_KEY, worker.to_s)

    block.call redis: piped
  end
end
```

    
  

    
      
  
### 
  
    #**worker_done_working**(worker, &block)  ⇒ Object 
  

  

  

  
    
      

```

292
293
294
295
296
297
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 292

def worker_done_working(worker, &block)
  @redis.pipelined do |piped|
    piped.del(redis_key_for_worker(worker))
    block.call redis: piped
  end
end
```

    
  

    
      
  
### 
  
    #**worker_exists?**(worker_id)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

237
238
239
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 237

def worker_exists?(worker_id)
  @redis.sismember(:workers, worker_id)
end
```

    
  

    
      
  
### 
  
    #**worker_ids**  ⇒ Object 
  

  

  

  
    
      

```

221
222
223
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 221

def worker_ids
  Array(@redis.smembers(:workers))
end
```

    
  

    
      
  
### 
  
    #**worker_start_time**(worker)  ⇒ Object 
  

  

  

  
    
      

```

288
289
290
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 288

def worker_start_time(worker)
  @redis.get(redis_key_for_worker_start_time(worker))
end
```

    
  

    
      
  
### 
  
    #**worker_started**(worker, redis: @redis)  ⇒ Object 
  

  

  

  
    
      

```

248
249
250
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 248

def worker_started(worker, redis: @redis)
  redis.set(redis_key_for_worker_start_time(worker), Time.now.to_s)
end
```

    
  

    
      
  
### 
  
    #**workers_map**(worker_ids)  ⇒ Object 
  

  

  

  
    

Given a list of worker ids, returns a map of those ids to the worker’s value in redis, even if that value maps to nil

  

  

  
    
      

```

227
228
229
230
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 227

def workers_map(worker_ids)
  redis_keys = worker_ids.map { |id| "worker:#{id}" }
  @redis.mapped_mget(*redis_keys)
end
```