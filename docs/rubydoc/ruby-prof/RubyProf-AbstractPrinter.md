# Class: RubyProf::AbstractPrinter
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- RubyProf::AbstractPrinter
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/ruby-prof/printers/abstract_printer.rb
  
  

## Overview

  
    

This is the base class for all Printers. It is never used directly.

  

  

  
## Direct Known Subclasses

  

CallInfoPrinter, CallStackPrinter, CallTreePrinter, DotPrinter, FlameGraphPrinter, FlatPrinter, GraphHtmlPrinter, GraphPrinter

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**filter_by**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute filter_by.

  

    
      
- 
  
    
      #**max_percent**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute max_percent.

  

    
      
- 
  
    
      #**min_percent**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute min_percent.

  

    
      
- 
  
    
      #**sort_method**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute sort_method.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**needs_dir?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

:stopdoc:.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(result)  ⇒ AbstractPrinter 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Create a new printer.

  

      
        
- 
  
    
      #**method_href**(thread, method)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**method_location**(method)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**open_asset**(file)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print**(output = STDOUT, min_percent: 0, max_percent: 100, filter_by: :self_time, sort_method: nil, max_depth: nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Prints a report to the provided output.

  

      
        
- 
  
    
      #**print_column_headers**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_footer**(thread)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_header**(thread)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_thread**(thread)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_threads**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**time_format**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the time format used to show when a profile was run.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(result)  ⇒ AbstractPrinter 
  

  

  

  
    

Create a new printer.

result should be the output generated from a profiling run

  

  

  
    
      

```

15
16
17
18
```

    
    
      

```
# File 'lib/ruby-prof/printers/abstract_printer.rb', line 15

def initialize(result)
  @result = result
  @output = nil
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**filter_by**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute filter_by.

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/ruby-prof/printers/abstract_printer.rb', line 20

def filter_by
  @filter_by
end
```

    
  

    
      
      
      
  
### 
  
    #**max_percent**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute max_percent.

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/ruby-prof/printers/abstract_printer.rb', line 20

def max_percent
  @max_percent
end
```

    
  

    
      
      
      
  
### 
  
    #**min_percent**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute min_percent.

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/ruby-prof/printers/abstract_printer.rb', line 20

def min_percent
  @min_percent
end
```

    
  

    
      
      
      
  
### 
  
    #**sort_method**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute sort_method.

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/ruby-prof/printers/abstract_printer.rb', line 20

def sort_method
  @sort_method
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**needs_dir?**  ⇒ Boolean 
  

  

  

  
    

:stopdoc:

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/ruby-prof/printers/abstract_printer.rb', line 7

def self.needs_dir?
  false
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**method_href**(thread, method)  ⇒ Object 
  

  

  

  
    
      

```

67
68
69
```

    
    
      

```
# File 'lib/ruby-prof/printers/abstract_printer.rb', line 67

def method_href(thread, method)
  h(method.full_name.gsub(/[><#\.\?=:]/,"_") + "_" + thread.fiber_id.to_s)
end
```

    
  

    
      
  
### 
  
    #**method_location**(method)  ⇒ Object 
  

  

  

  
    
      

```

61
62
63
64
65
```

    
    
      

```
# File 'lib/ruby-prof/printers/abstract_printer.rb', line 61

def method_location(method)
  if method.source_file
    "#{method.source_file}:#{method.line}"
  end
end
```

    
  

    
      
  
### 
  
    #**open_asset**(file)  ⇒ Object 
  

  

  

  
    
      

```

71
72
73
74
```

    
    
      

```
# File 'lib/ruby-prof/printers/abstract_printer.rb', line 71

def open_asset(file)
  path = File.join(File.expand_path('../../assets', __FILE__), file)
  File.open(path, 'rb').read
end
```

    
  

    
      
  
### 
  
    #**print**(output = STDOUT, min_percent: 0, max_percent: 100, filter_by: :self_time, sort_method: nil, max_depth: nil)  ⇒ Object 
  

  

  

  
    

Prints a report to the provided output.

output - Any IO object, including STDOUT or a file. The default value is STDOUT.

Keyword arguments:

```
min_percent  - Number 0 to 100 that specifies the minimum
               %self (the methods self time divided by the
               overall total time) that a method must take
               for it to be printed out in the report.
               Default value is 0.

max_percent  - Number 0 to 100 that specifies the maximum
               %self for methods to include.
               Default value is 100.

filter_by    - Which time metric to use when applying
               min_percent and max_percent filters.
               Default value is :self_time.

sort_method  - Specifies method used for sorting method infos.
               Available values are :total_time, :self_time,
               :wait_time, :children_time.
               Default value depends on the printer.

```

  

  

  
    
      

```

51
52
53
54
55
56
57
58
59
```

    
    
      

```
# File 'lib/ruby-prof/printers/abstract_printer.rb', line 51

def print(output = STDOUT, min_percent: 0, max_percent: 100, filter_by: :self_time, sort_method: nil, max_depth: nil, **)
  @output = output
  @min_percent = min_percent
  @max_percent = max_percent
  @filter_by = filter_by
  @sort_method = sort_method || :total_time
  @max_depth = max_depth
  print_threads
end
```

    
  

    
      
  
### 
  
    #**print_column_headers**  ⇒ Object 
  

  

  

  
    
      

```

98
99
```

    
    
      

```
# File 'lib/ruby-prof/printers/abstract_printer.rb', line 98

def print_column_headers
end
```

    
  

    
      
  
### 
  
    #**print_footer**(thread)  ⇒ Object 
  

  

  

  
    
      

```

101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
```

    
    
      

```
# File 'lib/ruby-prof/printers/abstract_printer.rb', line 101

def print_footer(thread)
  metric_data = {
    0 => { label: "time", prefix: "", suffix: "spent" },
    1 => { label: "time", prefix: "", suffix: "spent" },
    2 => { label: "allocations", prefix: "number of ", suffix: "made" },
    3 => { label: "memory", prefix: "", suffix: "used" }
  }

  metric = metric_data[@result.measure_mode]

  metric_label = metric[:label]
  metric_suffix = metric[:suffix]
  metric_prefix = metric[:prefix]

  metric1 = "#{metric_label} #{metric_suffix}"
  metric2 = "#{metric_prefix}#{metric1}"
  metric3 = metric_label

  # Output the formatted text
  @output << <<~EOT

    * recursively called methods

    Columns are:

      %self     - The percentage of #{metric1} by this method relative to the total #{metric3} in the entire program.
      total     - The total #{metric2} by this method and its children.
      self      - The #{metric2} by this method.
      wait      - The time this method spent waiting for other threads.
      child     - The #{metric2} by this method's children.
      calls     - The number of times this method was called.
      name      - The name of the method.
      location  - The location of the method.

    The interpretation of method names is:

      * MyObject#test - An instance method "test" of the class "MyObject"
      * <Object:MyObject>#test - The <> characters indicate a method on a singleton class.

  EOT
end
```

    
  

    
      
  
### 
  
    #**print_header**(thread)  ⇒ Object 
  

  

  

  
    
      

```

88
89
90
91
92
93
94
95
96
```

    
    
      

```
# File 'lib/ruby-prof/printers/abstract_printer.rb', line 88

def print_header(thread)
  @output << "Measure Mode: %s\n" % @result.measure_mode_string
  @output << "Thread ID: %d\n" % thread.id
  @output << "Fiber ID: %d\n" % thread.fiber_id unless thread.id == thread.fiber_id
  @output << "Total: %0.6f\n" % thread.total_time
  @output << "Sort by: #{sort_method}\n"
  @output << "\n"
  print_column_headers
end
```

    
  

    
      
  
### 
  
    #**print_thread**(thread)  ⇒ Object 
  

  

  

  
    
      

```

82
83
84
85
86
```

    
    
      

```
# File 'lib/ruby-prof/printers/abstract_printer.rb', line 82

def print_thread(thread)
  print_header(thread)
  print_methods(thread)
  print_footer(thread)
end
```

    
  

    
      
  
### 
  
    #**print_threads**  ⇒ Object 
  

  

  

  
    
      

```

76
77
78
79
80
```

    
    
      

```
# File 'lib/ruby-prof/printers/abstract_printer.rb', line 76

def print_threads
  @result.threads.each do |thread|
    print_thread(thread)
  end
end
```

    
  

    
      
  
### 
  
    #**time_format**  ⇒ Object 
  

  

  

  
    

Returns the time format used to show when a profile was run

  

  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/ruby-prof/printers/abstract_printer.rb', line 23

def time_format
  '%A, %B %-d at %l:%M:%S %p (%Z)'
end
```