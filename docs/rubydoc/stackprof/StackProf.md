# Module: StackProf
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/stackprof.rb,

  lib/stackprof/report.rb,
 lib/stackprof/middleware.rb,
 lib/stackprof/truffleruby.rb,
 ext/stackprof/stackprof.c

  
  

## Defined Under Namespace

  
    
  
    
      **Classes:** Middleware, Report
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        VERSION =
          
        
        

```
'0.2.28'
```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**results**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**run**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**running?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**sample**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**start**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**stop**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**use_postponed_job!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**results**(*args)  ⇒ Object 
  

  

  

  
    
      

```

389
390
391
```

    
    
      

```
# File 'ext/stackprof/stackprof.c', line 389

def results(*args)
  unimplemented
end
```

    
  

    
      
  
### 
  
    .**run**(*args)  ⇒ Object 
  

  

  

  
    
      

```

486
487
488
```

    
    
      

```
# File 'ext/stackprof/stackprof.c', line 486

def run(*args)
  unimplemented
end
```

    
  

    
      
  
### 
  
    .**running?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

495
496
497
```

    
    
      

```
# File 'ext/stackprof/stackprof.c', line 495

def running?
  false
end
```

    
  

    
      
  
### 
  
    .**sample**  ⇒ Object 
  

  

  

  
    
      

```

850
851
852
```

    
    
      

```
# File 'ext/stackprof/stackprof.c', line 850

def sample
  unimplemented
end
```

    
  

    
      
  
### 
  
    .**start**(*args)  ⇒ Object 
  

  

  

  
    
      

```

175
176
177
```

    
    
      

```
# File 'ext/stackprof/stackprof.c', line 175

def start(*args)
  unimplemented
end
```

    
  

    
      
  
### 
  
    .**stop**  ⇒ Object 
  

  

  

  
    
      

```

271
272
273
```

    
    
      

```
# File 'ext/stackprof/stackprof.c', line 271

def stop
  unimplemented
end
```

    
  

    
      
  
### 
  
    .**use_postponed_job!**  ⇒ Object 
  

  

  

  
    
      

```

925
926
927
```

    
    
      

```
# File 'ext/stackprof/stackprof.c', line 925

def use_postponed_job!
  # noop
end
```