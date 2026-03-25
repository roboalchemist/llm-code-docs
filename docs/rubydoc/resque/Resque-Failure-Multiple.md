# Class: Resque::Failure::Multiple
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- Resque::Failure::Multiple
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/failure/multiple.rb
  
  

## Overview

  
    

A Failure backend that uses multiple backends delegates all queries to the first backend

  

  

  
## Class Attribute Summary collapse

  

    
      
- 
  
    
      .**classes**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute classes.

  

    
  

  
  
  
### Attributes inherited from Base

  

#exception, #payload, #queue, #worker

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**all**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns a paginated array of failure objects.

  

      
        
- 
  
    
      .**clear**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Clear all failure objects.

  

      
        
- 
  
    
      .**configure** {|_self| ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**count**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The number of failures.

  

      
        
- 
  
    
      .**each**(*args, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Iterate across failed objects.

  

      
        
- 
  
    
      .**queues**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an array of all available failure queues.

  

      
        
- 
  
    
      .**remove**(index, queue = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**requeue**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**requeue_all**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**requeue_queue**(queue)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**url**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

A URL where someone can go to view failures.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(*args)  ⇒ Multiple 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Multiple.

  

      
        
- 
  
    
      #**save**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#log

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(*args)  ⇒ Multiple 
  

  

  

  
    

Returns a new instance of Multiple.

  

  

  
    
      

```

16
17
18
19
```

    
    
      

```
# File 'lib/resque/failure/multiple.rb', line 16

def initialize(*args)
  super
  @backends = self.class.classes.map {|klass| klass.new(*args)}
end

```

    
  

  

  
    
## Class Attribute Details

    
      
      
      
  
### 
  
    .**classes**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute classes.

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/resque/failure/multiple.rb', line 8

def classes
  @classes
end

```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**all**(*args)  ⇒ Object 
  

  

  

  
    

Returns a paginated array of failure objects.

  

  

  
    
      

```

36
37
38
```

    
    
      

```
# File 'lib/resque/failure/multiple.rb', line 36

def self.all(*args)
  classes.first.all(*args)
end

```

    
  

    
      
  
### 
  
    .**clear**(*args)  ⇒ Object 
  

  

  

  
    

Clear all failure objects

  

  

  
    
      

```

51
52
53
```

    
    
      

```
# File 'lib/resque/failure/multiple.rb', line 51

def self.clear(*args)
  classes.first.clear(*args)
end

```

    
  

    
      
  
### 
  
    .**configure** {|_self| ... } ⇒ Object 
  

  

  

  
    

  

  

Yields:

  
    
- 
      
      
        (_self)
      
      
      
    
  

Yield Parameters:

  
    
- 
      
        _self
      
      
        (Resque::Failure::Multiple)
      
      
      
        —
        

the object that the method was called on

      
    
  

  
    
      

```

11
12
13
14
```

    
    
      

```
# File 'lib/resque/failure/multiple.rb', line 11

def self.configure
  yield self
  Resque::Failure.backend = self
end

```

    
  

    
      
  
### 
  
    .**count**(*args)  ⇒ Object 
  

  

  

  
    

The number of failures.

  

  

  
    
      

```

26
27
28
```

    
    
      

```
# File 'lib/resque/failure/multiple.rb', line 26

def self.count(*args)
  classes.first.count(*args)
end

```

    
  

    
      
  
### 
  
    .**each**(*args, &block)  ⇒ Object 
  

  

  

  
    

Iterate across failed objects

  

  

  
    
      

```

41
42
43
```

    
    
      

```
# File 'lib/resque/failure/multiple.rb', line 41

def self.each(*args, &block)
  classes.first.each(*args, &block)
end

```

    
  

    
      
  
### 
  
    .**queues**  ⇒ Object 
  

  

  

  
    

Returns an array of all available failure queues

  

  

  
    
      

```

31
32
33
```

    
    
      

```
# File 'lib/resque/failure/multiple.rb', line 31

def self.queues
  classes.first.queues
end

```

    
  

    
      
  
### 
  
    .**remove**(index, queue = nil)  ⇒ Object 
  

  

  

  
    
      

```

67
68
69
```

    
    
      

```
# File 'lib/resque/failure/multiple.rb', line 67

def self.remove(index, queue = nil)
  classes.each { |klass| klass.remove(index, queue) }
end

```

    
  

    
      
  
### 
  
    .**requeue**(*args)  ⇒ Object 
  

  

  

  
    
      

```

55
56
57
```

    
    
      

```
# File 'lib/resque/failure/multiple.rb', line 55

def self.requeue(*args)
  classes.first.requeue(*args)
end

```

    
  

    
      
  
### 
  
    .**requeue_all**  ⇒ Object 
  

  

  

  
    
      

```

59
60
61
```

    
    
      

```
# File 'lib/resque/failure/multiple.rb', line 59

def self.requeue_all
  classes.first.requeue_all
end

```

    
  

    
      
  
### 
  
    .**requeue_queue**(queue)  ⇒ Object 
  

  

  

  
    
      

```

63
64
65
```

    
    
      

```
# File 'lib/resque/failure/multiple.rb', line 63

def self.requeue_queue(queue)
  classes.first.requeue_queue(queue)
end

```

    
  

    
      
  
### 
  
    .**url**  ⇒ Object 
  

  

  

  
    

A URL where someone can go to view failures.

  

  

  
    
      

```

46
47
48
```

    
    
      

```
# File 'lib/resque/failure/multiple.rb', line 46

def self.url
  classes.first.url
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**save**  ⇒ Object 
  

  

  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/resque/failure/multiple.rb', line 21

def save
  @backends.each(&:save)
end

```