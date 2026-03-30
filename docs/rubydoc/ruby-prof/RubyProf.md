# Module: RubyProf
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/ruby-prof/exclude_common_methods.rb,

  lib/ruby-prof.rb,
 lib/ruby-prof/task.rb,
 lib/ruby-prof/thread.rb,
 lib/ruby-prof/profile.rb,
 lib/ruby-prof/version.rb,
 lib/ruby-prof/call_tree.rb,
 lib/ruby-prof/measurement.rb,
 lib/ruby-prof/method_info.rb,
 lib/ruby-prof/call_tree_visitor.rb,
 lib/ruby-prof/printers/dot_printer.rb,
 lib/ruby-prof/printers/flat_printer.rb,
 lib/ruby-prof/printers/graph_printer.rb,
 lib/ruby-prof/printers/multi_printer.rb,
 lib/ruby-prof/printers/abstract_printer.rb,
 lib/ruby-prof/printers/call_info_printer.rb,
 lib/ruby-prof/printers/call_tree_printer.rb,
 lib/ruby-prof/printers/call_stack_printer.rb,
 lib/ruby-prof/printers/graph_html_printer.rb,
 lib/ruby-prof/printers/flame_graph_printer.rb,
 ext/ruby_prof/ruby_prof.c

  
  

## Overview

  
    

:enddoc:

  

  

## Defined Under Namespace

  
    
      **Modules:** ExcludeCommonMethods, Measure
    
  
    
      **Classes:** AbstractPrinter, Allocation, CallInfoPrinter, CallStackPrinter, CallTree, CallTreePrinter, CallTreeVisitor, CallTrees, DotPrinter, FlameGraphPrinter, FlatPrinter, GraphHtmlPrinter, GraphPrinter, Measurement, MethodInfo, MultiPrinter, Profile, ProfileTask, Thread
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        VERSION =
          
        
        

```
"2.0.4"

```

      
        WALL_TIME =
          
        
        

```
INT2NUM(MEASURE_WALL_TIME)

```

      
        ALLOCATIONS =
          
        
        

```
INT2NUM(MEASURE_ALLOCATIONS)

```

      
        CLOCKS_PER_SEC =
          
        
        

```
INT2NUM(CLOCKS_PER_SEC)

```

      
        PROCESS_TIME =
          
        
        

```
INT2NUM(MEASURE_PROCESS_TIME)

```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**figure_measure_mode**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc: Checks if the user specified the clock mode via the RUBY_PROF_MEASURE_MODE environment variable.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**figure_measure_mode**  ⇒ Object 
  

  

  

  
    

:nodoc: Checks if the user specified the clock mode via the RUBY_PROF_MEASURE_MODE environment variable

  

  

  
    
      

```

36
37
38
39
40
41
42
43
44
45
46
47
```

    
    
      

```
# File 'lib/ruby-prof.rb', line 36

def self.figure_measure_mode
  case ENV["RUBY_PROF_MEASURE_MODE"]
  when "wall", "wall_time"
    RubyProf.measure_mode = RubyProf::WALL_TIME
  when "allocations"
    RubyProf.measure_mode = RubyProf::ALLOCATIONS
  when "process", "process_time"
    RubyProf.measure_mode = RubyProf::PROCESS_TIME
  else
    # the default is defined in the measure_mode reader
  end
end

```