# Module: Resque::Stat
  
  
  

  

  
  
  
      Extended by:
      Stat
  
  
  
  
  

  
  
    Included in:
    Stat
  
  

  
  
    Defined in:
    lib/resque/stat.rb
  
  

## Overview

  
    

The stat subsystem. Used to keep track of integer counts.

```
Get a stat:  Stat[name]
Incr a stat: Stat.incr(name)
Decr a stat: Stat.decr(name)
Kill a stat: Stat.clear(name)

```

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**<<**(stat)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Increments a stat by one.

  

      
        
- 
  
    
      #**>>**(stat)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Decrements a stat by one.

  

      
        
- 
  
    
      #**[]**(stat)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Alias of `get`.

  

      
        
- 
  
    
      #**clear**(stat, **opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Removes a stat from Redis, effectively setting it to 0.

  

      
        
- 
  
    
      #**data_store**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**data_store=**(data_store)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**decr**(stat, by = 1)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

For a string stat name, decrements the stat by one.

  

      
        
- 
  
    
      #**get**(stat)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the int value of a stat, given a string stat name.

  

      
        
- 
  
    
      #**incr**(stat, by = 1, **opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

For a string stat name, increments the stat by one.

  

      
        
- 
  
    
      #**redis**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**<<**(stat)  ⇒ Object 
  

  

  

  
    

Increments a stat by one.

  

  

  
    
      

```

43
44
45
```

    
    
      

```
# File 'lib/resque/stat.rb', line 43

def <<(stat)
  incr stat
end

```

    
  

    
      
  
### 
  
    #**>>**(stat)  ⇒ Object 
  

  

  

  
    

Decrements a stat by one.

  

  

  
    
      

```

56
57
58
```

    
    
      

```
# File 'lib/resque/stat.rb', line 56

def >>(stat)
  decr stat
end

```

    
  

    
      
  
### 
  
    #**[]**(stat)  ⇒ Object 
  

  

  

  
    

Alias of `get`

  

  

  
    
      

```

30
31
32
```

    
    
      

```
# File 'lib/resque/stat.rb', line 30

def [](stat)
  get(stat)
end

```

    
  

    
      
  
### 
  
    #**clear**(stat, **opts)  ⇒ Object 
  

  

  

  
    

Removes a stat from Redis, effectively setting it to 0.

  

  

  
    
      

```

61
62
63
```

    
    
      

```
# File 'lib/resque/stat.rb', line 61

def clear(stat, **opts)
  data_store.clear_stat(stat, **opts)
end

```

    
  

    
      
  
### 
  
    #**data_store**  ⇒ Object 
  

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/resque/stat.rb', line 16

def data_store
  @data_store ||= Resque.redis
end

```

    
  

    
      
  
### 
  
    #**data_store=**(data_store)  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/resque/stat.rb', line 20

def data_store=(data_store)
  @data_store = data_store
end

```

    
  

    
      
  
### 
  
    #**decr**(stat, by = 1)  ⇒ Object 
  

  

  

  
    

For a string stat name, decrements the stat by one.

Can optionally accept a second int parameter. The stat is then decremented by that amount.

  

  

  
    
      

```

51
52
53
```

    
    
      

```
# File 'lib/resque/stat.rb', line 51

def decr(stat, by = 1)
  data_store.decrement_stat(stat,by)
end

```

    
  

    
      
  
### 
  
    #**get**(stat)  ⇒ Object 
  

  

  

  
    

Returns the int value of a stat, given a string stat name.

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/resque/stat.rb', line 25

def get(stat)
  data_store.stat(stat)
end

```

    
  

    
      
  
### 
  
    #**incr**(stat, by = 1, **opts)  ⇒ Object 
  

  

  

  
    

For a string stat name, increments the stat by one.

Can optionally accept a second int parameter. The stat is then incremented by that amount.

  

  

  
    
      

```

38
39
40
```

    
    
      

```
# File 'lib/resque/stat.rb', line 38

def incr(stat, by = 1, **opts)
  data_store.increment_stat(stat, by, **opts)
end

```

    
  

    
      
  
### 
  
    #**redis**  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
14
```

    
    
      

```
# File 'lib/resque/stat.rb', line 11

def redis
  warn '[Resque] [Deprecation] Resque::Stat #redis method is deprecated (please use #data_store)'
  data_store
end

```