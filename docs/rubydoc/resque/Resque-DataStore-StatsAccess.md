# Class: Resque::DataStore::StatsAccess
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Resque::DataStore::StatsAccess
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/data_store.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**clear_stat**(stat, redis: @redis)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**decremet_stat**(stat, by = 1)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**increment_stat**(stat, by = 1, redis: @redis)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(redis)  ⇒ StatsAccess 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of StatsAccess.

  

      
        
- 
  
    
      #**stat**(stat)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(redis)  ⇒ StatsAccess 
  

  

  

  
    

Returns a new instance of StatsAccess.

  

  

  
    
      

```

315
316
317
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 315

def initialize(redis)
  @redis = redis
end

```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**clear_stat**(stat, redis: @redis)  ⇒ Object 
  

  

  

  
    
      

```

330
331
332
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 330

def clear_stat(stat, redis: @redis)
  redis.del("stat:#{stat}")
end

```

    
  

    
      
  
### 
  
    #**decremet_stat**(stat, by = 1)  ⇒ Object 
  

  

  

  
    
      

```

326
327
328
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 326

def decremet_stat(stat, by = 1)
  @redis.decrby("stat:#{stat}", by)
end

```

    
  

    
      
  
### 
  
    #**increment_stat**(stat, by = 1, redis: @redis)  ⇒ Object 
  

  

  

  
    
      

```

322
323
324
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 322

def increment_stat(stat, by = 1, redis: @redis)
  redis.incrby("stat:#{stat}", by)
end

```

    
  

    
      
  
### 
  
    #**stat**(stat)  ⇒ Object 
  

  

  

  
    
      

```

318
319
320
```

    
    
      

```
# File 'lib/resque/data_store.rb', line 318

def stat(stat)
  @redis.get("stat:#{stat}").to_i
end

```