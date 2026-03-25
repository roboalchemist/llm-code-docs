# Class: RubyProf::DotPrinter
  
  
  

  
  
    Inherits:
    
      AbstractPrinter
      
        

          
- Object
          
            
- AbstractPrinter
          
            
- RubyProf::DotPrinter
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/ruby-prof/printers/dot_printer.rb
  
  

## Overview

  
    

Generates a graphviz graph in dot format.

To use the dot printer:

```
result = RubyProf.profile do
  [code to profile]
end

printer = RubyProf::DotPrinter.new(result)
printer.print(STDOUT)

```

You can use either dot viewer such as GraphViz, or the dot command line tool to reformat the output into a wide variety of outputs:

```
dot -Tpng graph.dot > graph.png

```

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        CLUSTER_COLORS =
          
        
        

```
%w[#1A35A6 #2E86C1 #1ABC9C #5B2C8E #2471A3 #148F77 #1F618D #7D3C98]
```

      
    
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from AbstractPrinter

  

#filter_by, #max_percent, #min_percent, #sort_method

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(result)  ⇒ DotPrinter 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Creates the DotPrinter using a RubyProf::Proile.

  

      
        
- 
  
    
      #**print**(output = STDOUT, min_percent: 0, max_percent: 100, filter_by: :self_time, sort_method: nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Print a graph report to the provided output.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from AbstractPrinter

  

#method_href, #method_location, needs_dir?, #open_asset, #print_column_headers, #print_footer, #print_header, #time_format

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(result)  ⇒ DotPrinter 
  

  

  

  
    

Creates the DotPrinter using a RubyProf::Proile.

  

  

  
    
      

```

26
27
28
29
30
31
```

    
    
      

```
# File 'lib/ruby-prof/printers/dot_printer.rb', line 26

def initialize(result)
  super(result)
  @seen_methods = Set.new
  @class_color_map = {}
  @color_index = 0
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**print**(output = STDOUT, min_percent: 0, max_percent: 100, filter_by: :self_time, sort_method: nil)  ⇒ Object 
  

  

  

  
    

Print a graph report to the provided output.

output - Any IO object, including STDOUT or a file. The default value is STDOUT.

Keyword arguments - See AbstractPrinter#print for available options.

When profiling results that cover a large number of method calls it helps to use the min_percent: option, for example:

```
DotPrinter.new(result).print(STDOUT, min_percent: 5)

```

  

  

  
    
      

```

45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
```

    
    
      

```
# File 'lib/ruby-prof/printers/dot_printer.rb', line 45

def print(output = STDOUT, min_percent: 0, max_percent: 100, filter_by: :self_time, sort_method: nil, **)
  @output = output
  @min_percent = min_percent
  @max_percent = max_percent
  @filter_by = filter_by
  @sort_method = sort_method

  puts 'digraph "Profile" {'
  puts 'rankdir=TB;'
  puts 'bgcolor="#FAFAFA";'
  puts 'node [fontname="Helvetica" fontsize=11 style="filled,rounded" shape=box fillcolor="#FFFFFF" color="#CCCCCC" penwidth=1.2];'
  puts 'edge [fontname="Helvetica" fontsize=9 color="#5B7DB1" arrowsize=0.7];'
  puts 'labelloc=t;'
  puts 'labeljust=l;'
  print_threads
  puts '}'
end
```