# 

      
        **
        View Source
      

    ExMachina.Sequence 
    (ex_machina v2.8.0)

  

    

Module for generating sequential values.

Use `ExMachina.sequence/1` or `ExMachina.sequence/2` to generate
sequential values instead of calling this module directly.
    

Module for generating sequential values.

Use `ExMachina.sequence/1` or `ExMachina.sequence/2` to generate
sequential values instead of calling this module directly.
    

    
# 
      
        **
      
      Summary
    

  
## 
    Functions
  

    
      
        child_spec(arg)

      

        

Returns a specification to start this module under a supervisor.

    

    
      
        reset()

      

        

Reset all sequences so that the next sequence starts from 0

    

    
      
        reset(sequence_names)

      

        

Reset specific sequences so long as they already exist. The sequences
specified will be reset to 0, while others will remain at their current index.

    

  

    
# 
      
        **
      
      Functions
    

    

  
    
      **
      Link to this function
    
    
# child_spec(arg)

      
       **
       View Source
     

  

  

Returns a specification to start this module under a supervisor.

See `Supervisor`.
  

  
    
      **
      Link to this function
    
    
# reset()

      
       **
       View Source
     

  

  

      

          

```
@spec reset() :: :ok
```

      

Reset all sequences so that the next sequence starts from 0
## 
  
    **
  
  Example

```
ExMachina.Sequence.next("joe") # "joe0"
ExMachina.Sequence.next("joe") # "joe1"

ExMachina.Sequence.reset()

ExMachina.Sequence.next("joe") # resets so the return value is "joe0"
```

You can use list as well

```
ExMachina.Sequence.next("alphabet_sequence", ["A", "B"]) # "A"
ExMachina.Sequence.next("alphabet_sequence", ["A", "B"]) # "B"

ExMachina.Sequence.reset()

ExMachina.Sequence.next("alphabet_sequence", ["A", "B"]) # resets so the return value is "A"
```

If you want to reset sequences at the beginning of every test, put it in a
`setup` block in your test.

```
setup do
  ExMachina.Sequence.reset()
end
```

  

  
    
      **
      Link to this function
    
    
# reset(sequence_names)

      
       **
       View Source
     

  

  

      

          

```
@spec reset(any()) :: :ok
```

      

Reset specific sequences so long as they already exist. The sequences
specified will be reset to 0, while others will remain at their current index.

You can reset a single sequence,
## 
  
    **
  
  Example

```
ExMachina.Sequence.next(:alphabet, ["A", "B", "C"]) # "A"
ExMachina.Sequence.next(:alphabet, ["A", "B", "C"]) # "B"

ExMachina.Sequence.reset(:alphabet)

ExMachina.Sequence.next(:alphabet, ["A", "B", "C"]) # "A"
```

And you can also reset multiple sequences at once,
## 
  
    **
  
  Example

```
ExMachina.Sequence.next(:numeric, [1, 2, 3]) # 1
ExMachina.Sequence.next(:numeric, [1, 2, 3]) # 2
ExMachina.Sequence.next("joe") # "joe0"
ExMachina.Sequence.next("joe") # "joe1"

ExMachina.Sequence.reset(["joe", :numeric])

ExMachina.Sequence.next(:numeric, [1, 2, 3]) # 1
ExMachina.Sequence.next("joe") # "joe0"
```