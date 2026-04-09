Search
      
    
  

  
    
    
  

  

    
      
Instruments
      
      **
        v2.11.0
      **
    
    

      
- Pages

        
- Modules

    

  

  
  

  
  
    

# 

  Instruments.CustomFunctions 
  (Instruments v2.11.0)

  

Creates custom prefixed functions

Often, a module will have functions that all have a common prefix.
It's somewhat tedious to have to put this prefix in every call to
every metric function. Using this module can help somewhat.

When you `use` this module, it defines custom, module-specific metrics
functions that include your prefix. For example:

```
defmodule Prefixed do
  use Instruments.CustomFunctions, prefix: "my.module"

  def do_something() do
    increment("do_something_counts")
    do_another_thing()
  end

  def long_running() do
     measure("timed_fn", &compute/0)
  end

  defp compute(), do: Process.sleep(10_000)
  defp do_another_thing, do: 3
end
```

In the above example, we increment `do_something_counts` and `timed_fn`, yet
the metrics emitted are `my.module.do_something_counts` and `my.module.timed_fn`.