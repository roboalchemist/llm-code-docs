# Class: RubyProf::FlameGraphPrinter
  
  
  

  
  
    Inherits:
    
      AbstractPrinter
      
        

          
- Object
          
            
- AbstractPrinter
          
            
- RubyProf::FlameGraphPrinter
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      ERB::Util
  
  
  

  

  
  
    Defined in:
    lib/ruby-prof/printers/flame_graph_printer.rb
  
  

## Overview

  
    

Prints a HTML flame graph visualization of the call tree.

To use the printer:

```
result = RubyProf.profile do
  [code to profile]
end

printer = RubyProf::FlameGraphPrinter.new(result)
printer.print(STDOUT)

```

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**title**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute title.

  

    
  

  
  
  
### Attributes inherited from AbstractPrinter

  

#filter_by, #max_percent, #min_percent, #sort_method

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**build_flame_data**(call_tree, depth = 0)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**flame_data_json**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print**(output = STDOUT, title: "ruby-prof flame graph", min_percent: 0, max_percent: 100, filter_by: :self_time, sort_method: nil, max_depth: nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Specify print options.

  

      
        
- 
  
    
      #**template**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
  
### Methods inherited from AbstractPrinter

  

#initialize, #method_href, #method_location, needs_dir?, #open_asset, #print_column_headers, #print_footer, #print_header, #print_thread, #print_threads, #time_format

  
## Constructor Details

  
    

This class inherits a constructor from RubyProf::AbstractPrinter
  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**title**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute title.

  

  

  
    
      

```

42
43
44
```

    
    
      

```
# File 'lib/ruby-prof/printers/flame_graph_printer.rb', line 42

def title
  @title
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**build_flame_data**(call_tree, depth = 0)  ⇒ Object 
  

  

  

  
    
      

```

44
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
```

    
    
      

```
# File 'lib/ruby-prof/printers/flame_graph_printer.rb', line 44

def build_flame_data(call_tree, depth = 0)
  node = {
    name: call_tree.target.full_name,
    value: call_tree.total_time,
    self_value: call_tree.self_time,
    called: call_tree.called,
    children: []
  }

  if @max_depth.nil? || depth < @max_depth
    call_tree.children.each do |child|
      node[:children] << build_flame_data(child, depth + 1)
    end
  end

  node
end
```

    
  

    
      
  
### 
  
    #**flame_data_json**  ⇒ Object 
  

  

  

  
    
      

```

62
63
64
65
66
67
68
69
70
71
72
```

    
    
      

```
# File 'lib/ruby-prof/printers/flame_graph_printer.rb', line 62

def flame_data_json
  threads = @result.threads.map do |thread|
    {
      id: thread.id,
      fiber_id: thread.fiber_id,
      total_time: thread.total_time,
      data: build_flame_data(thread.call_tree)
    }
  end
  JSON.generate(threads)
end
```

    
  

    
      
  
### 
  
    #**print**(output = STDOUT, title: "ruby-prof flame graph", min_percent: 0, max_percent: 100, filter_by: :self_time, sort_method: nil, max_depth: nil)  ⇒ Object 
  

  

  

  
    

Specify print options.

output - Any IO object, including STDOUT or a file.

Keyword arguments:

```
title:       - a String to override the default "ruby-prof flame graph"
               title of the report.

```

Also accepts min_percent:, max_percent:, filter_by:, and sort_method: from AbstractPrinter.

  

  

  
    
      

```

31
32
33
34
35
36
37
38
39
40
```

    
    
      

```
# File 'lib/ruby-prof/printers/flame_graph_printer.rb', line 31

def print(output = STDOUT, title: "ruby-prof flame graph",
          min_percent: 0, max_percent: 100, filter_by: :self_time, sort_method: nil, max_depth: nil, **)
  @min_percent = min_percent
  @max_percent = max_percent
  @filter_by = filter_by
  @sort_method = sort_method
  @max_depth = max_depth
  @title = title
  output << ERB.new(self.template).result(binding)
end
```

    
  

    
      
  
### 
  
    #**template**  ⇒ Object 
  

  

  

  
    
      

```

74
75
76
```

    
    
      

```
# File 'lib/ruby-prof/printers/flame_graph_printer.rb', line 74

def template
  open_asset('flame_graph_printer.html.erb')
end
```