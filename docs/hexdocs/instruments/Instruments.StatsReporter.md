Search
      
    
  

  
    
    
  

  

    
      
Instruments
      
      **
        v2.11.0
      **
    
    

      
- Pages

        
- Modules

    

  

  
  

  
  
    

# 

  Instruments.StatsReporter behaviour
  (Instruments v2.11.0)

  

A behavoiur for reporters.

Reporters emit values back to the underlying reporting system.
Out of the box, Instruments provides `Instruments.Statix`, `Instruments.StatsReporter.Logger`,
and `Instruments.StatsReporter.Null`reporters.
  

    
# 
      
        **
        Link to this section
      
      Summary
    

  
    
## 
      Types
    

      
        
          key()

        

      

      
        
          stats_return()

        

      

  

  
    
## 
      Callbacks
    

      
        
          connect()

        

          

Connect to the reporter.
This function is called by the system prior to using the reporter,
any connections should be established in this function.

      

      
        
          decrement(key, integer, keyword)

        

          

Decrement a key by the specified value

      

      
        
          gauge(key, integer, keyword)

        

          

Set the value of the key to the specified value

      

      
        
          histogram(key, integer, keyword)

        

          

Include the value in the histogram defined by `key`

      

      
        
          increment(key, integer, keyword)

        

          

Increment a key by the specified value

      

      
        
          measure(
  key,
  keyword,
  function
)

        

          

Measure the execution time of the provided function and
include it in the metric defined by `key`

      

      
        
          send_event(title, text, keyword)

        

          

Send a DataDog event with the given title and text

      

      
        
          set(key, integer, keyword)

        

          

Write the value into the set defined by `key`

      

      
        
          timing(key, integer, keyword)

        

          

Include the timing in the `key`

      

  

  

    
# 
      
        **
        Link to this section
      
Types
    

    

  
    
      **
      Link to this type
    
    
# key()

  

  

      

          

```
@type key() :: String.t()
```

      

  

  
    
      **
      Link to this type
    
    
# stats_return()

  

  

      

          

```
@type stats_return() :: :ok | {:error, term()}
```

      

  

    
# 
      
        **
        Link to this section
      
Callbacks
    

    

  
    
      **
      Link to this callback
    
    
# connect()

  

  

      

          

```
@callback connect() :: :ok
```

      

Connect to the reporter.
This function is called by the system prior to using the reporter,
any connections should be established in this function.
  

  
    
      **
      Link to this callback
    
    
# decrement(key, integer, keyword)

  

  

      

          

```
@callback decrement(key(), integer(), keyword()) :: stats_return()
```

      

Decrement a key by the specified value
  

  
    
      **
      Link to this callback
    
    
# gauge(key, integer, keyword)

  

  

      

          

```
@callback gauge(key(), integer(), keyword()) :: stats_return()
```

      

Set the value of the key to the specified value
  

  
    
      **
      Link to this callback
    
    
# histogram(key, integer, keyword)

  

  

      

          

```
@callback histogram(key(), integer(), keyword()) :: stats_return()
```

      

Include the value in the histogram defined by `key`
  

  
    
      **
      Link to this callback
    
    
# increment(key, integer, keyword)

  

  

      

          

```
@callback increment(key(), integer(), keyword()) :: stats_return()
```

      

Increment a key by the specified value
  

  
    
      **
      Link to this callback
    
    
# measure(
  key,
  keyword,
  function
)

  

  

      

          

```
@callback measure(key(), keyword(), (-> any())) :: any()
```

      

Measure the execution time of the provided function and
include it in the metric defined by `key`
  

  
    
      **
      Link to this callback
    
    
# send_event(title, text, keyword)

      (optional)

  

  

      

          

```
@callback send_event(title :: iodata(), text :: iodata(), keyword()) :: stats_return()
```

      

Send a DataDog event with the given title and text
  

  
    
      **
      Link to this callback
    
    
# set(key, integer, keyword)

  

  

      

          

```
@callback set(key(), integer(), keyword()) :: stats_return()
```

      

Write the value into the set defined by `key`
  

  
    
      **
      Link to this callback
    
    
# timing(key, integer, keyword)

  

  

      

          

```
@callback timing(key(), integer(), keyword()) :: stats_return()
```

      

Include the timing in the `key`