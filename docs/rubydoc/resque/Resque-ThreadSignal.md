# Class: Resque::ThreadSignal
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Resque::ThreadSignal
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/thread_signal.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**  ⇒ ThreadSignal 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ThreadSignal.

  

      
        
- 
  
    
      #**signal**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**wait_for_signal**(timeout)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ ThreadSignal 
  

  

  

  
    

Returns a new instance of ThreadSignal.

  

  

  
    
      

```

2
3
4
5
6
```

    
    
      

```
# File 'lib/resque/thread_signal.rb', line 2

def initialize
  @mutex = Mutex.new
  @signaled = false
  @received = ConditionVariable.new
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**signal**  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
11
12
13
```

    
    
      

```
# File 'lib/resque/thread_signal.rb', line 8

def signal
  @mutex.synchronize do
    @signaled = true
    @received.signal
  end
end
```

    
  

    
      
  
### 
  
    #**wait_for_signal**(timeout)  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
18
19
20
21
22
23
```

    
    
      

```
# File 'lib/resque/thread_signal.rb', line 15

def wait_for_signal(timeout)
  @mutex.synchronize do
    unless @signaled
      @received.wait(@mutex, timeout)
    end

    @signaled
  end
end
```