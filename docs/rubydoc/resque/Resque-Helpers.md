# Module: Resque::Helpers
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Resque, Job, Job, Worker, Worker
  
  

  
  
    Defined in:
    lib/resque/helpers.rb
  
  

## Overview

  
    

Methods used by various classes in Resque.

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** DecodeException
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**classify**(dashed_word)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a word with dashes, returns a camel cased version of it.

  

      
        
- 
  
    
      #**constantize**(camel_cased_word)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Tries to find a constant with the name specified in the argument string.

  

      
        
- 
  
    
      #**decode**(object)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a string, returns a Ruby object.

  

      
        
- 
  
    
      #**encode**(object)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given a Ruby object, returns a string suitable for storage in a queue.

  

      
        
- 
  
    
      #**redis**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Direct access to the Redis instance.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**classify**(dashed_word)  ⇒ Object 
  

  

  

  
    

Given a word with dashes, returns a camel cased version of it.

  

  

  
    
      

```

39
40
41
```

    
    
      

```
# File 'lib/resque/helpers.rb', line 39

def classify(dashed_word)
  Resque.classify(dashed_word)
end

```

    
  

    
      
  
### 
  
    #**constantize**(camel_cased_word)  ⇒ Object 
  

  

  

  
    

Tries to find a constant with the name specified in the argument string

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/resque/helpers.rb', line 44

def constantize(camel_cased_word)
  Resque.constantize(camel_cased_word)
end

```

    
  

    
      
  
### 
  
    #**decode**(object)  ⇒ Object 
  

  

  

  
    

Given a string, returns a Ruby object.

  

  

  
    
      

```

34
35
36
```

    
    
      

```
# File 'lib/resque/helpers.rb', line 34

def decode(object)
  Resque.decode(object)
end

```

    
  

    
      
  
### 
  
    #**encode**(object)  ⇒ Object 
  

  

  

  
    

Given a Ruby object, returns a string suitable for storage in a queue.

  

  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/resque/helpers.rb', line 29

def encode(object)
  Resque.encode(object)
end

```

    
  

    
      
  
### 
  
    #**redis**  ⇒ Object 
  

  

  

  
    

Direct access to the Redis instance.

  

  

  
    
      

```

17
18
19
20
21
22
23
24
25
```

    
    
      

```
# File 'lib/resque/helpers.rb', line 17

def redis
  # No infinite recursions, please.
  # Some external libraries depend on Resque::Helpers being mixed into
  # Resque, but this method causes recursions. If we have a super method,
  # assume it is canonical. (see #1150)
  return super if defined?(super)

  Resque.redis
end

```