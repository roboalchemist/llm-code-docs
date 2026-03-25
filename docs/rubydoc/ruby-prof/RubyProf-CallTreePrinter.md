# Class: RubyProf::CallTreePrinter
  
  
  

  
  
    Inherits:
    
      AbstractPrinter
      
        

          
- Object
          
            
- AbstractPrinter
          
            
- RubyProf::CallTreePrinter
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/ruby-prof/printers/call_tree_printer.rb
  
  

## Overview

  
    

Generates profiling information in callgrind format for use by kcachegrind and similar tools.

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**path**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute path.

  

    
  

  
  
  
### Attributes inherited from AbstractPrinter

  

#filter_by, #max_percent, #min_percent, #sort_method

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**needs_dir?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**calltree_name**(method_info)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert**(value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**determine_event_specification_and_value_scale**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**file**(method)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**file_name_for_thread**(thread)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**file_path_for_thread**(thread)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print**(path: ".")  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_headers**(output, thread)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_method**(output, method)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_thread**(thread)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_threads**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**remove_subsidiary_files_from_previous_profile_runs**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from AbstractPrinter

  

#initialize, #method_href, #method_location, #open_asset, #print_column_headers, #print_footer, #print_header, #time_format

  
## Constructor Details

  
    

This class inherits a constructor from RubyProf::AbstractPrinter
  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**path**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute path.

  

  

  
    
      

```

82
83
84
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_tree_printer.rb', line 82

def path
  @path
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**needs_dir?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

84
85
86
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_tree_printer.rb', line 84

def self.needs_dir?
  true
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**calltree_name**(method_info)  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_tree_printer.rb', line 13

def calltree_name(method_info)
  klass_path = method_info.klass_name.gsub("::", '/')
  result = "#{klass_path}::#{method_info.method_name}"

  case method_info.klass_flags
    when 0x2
      "#{result}^"
    when 0x4
      "#{result}^"
    when 0x8
     "#{result}*"
    else
     result
  end
end
```

    
  

    
      
  
### 
  
    #**convert**(value)  ⇒ Object 
  

  

  

  
    
      

```

65
66
67
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_tree_printer.rb', line 65

def convert(value)
  (value * @value_scale).round
end
```

    
  

    
      
  
### 
  
    #**determine_event_specification_and_value_scale**  ⇒ Object 
  

  

  

  
    
      

```

29
30
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
41
42
43
44
45
46
47
48
49
50
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_tree_printer.rb', line 29

def determine_event_specification_and_value_scale
  @event_specification = String.new("events: ")
  case @result.measure_mode
    when RubyProf::PROCESS_TIME
      @value_scale = RubyProf::CLOCKS_PER_SEC
      @event_specification << 'process_time'
    when RubyProf::WALL_TIME
      @value_scale = 1_000_000
      @event_specification << 'wall_time'
    when RubyProf.const_defined?(:ALLOCATIONS) && RubyProf::ALLOCATIONS
      @value_scale = 1
      @event_specification << 'allocations'
    when RubyProf.const_defined?(:GC_RUNS) && RubyProf::GC_RUNS
      @value_scale = 1
      @event_specification << 'gc_runs'
    when RubyProf.const_defined?(:GC_TIME) && RubyProf::GC_TIME
      @value_scale = 1000000
      @event_specification << 'gc_time'
    else
      raise "Unknown measure mode: #{RubyProf.measure_mode}"
  end
end
```

    
  

    
      
  
### 
  
    #**file**(method)  ⇒ Object 
  

  

  

  
    
      

```

69
70
71
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_tree_printer.rb', line 69

def file(method)
  method.source_file ? File.expand_path(method.source_file) : ''
end
```

    
  

    
      
  
### 
  
    #**file_name_for_thread**(thread)  ⇒ Object 
  

  

  

  
    
      

```

94
95
96
97
98
99
100
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_tree_printer.rb', line 94

def file_name_for_thread(thread)
  if thread.fiber_id == Fiber.current.object_id
    ["callgrind.out", $$].join(".")
  else
    ["callgrind.out", $$, thread.fiber_id].join(".")
  end
end
```

    
  

    
      
  
### 
  
    #**file_path_for_thread**(thread)  ⇒ Object 
  

  

  

  
    
      

```

102
103
104
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_tree_printer.rb', line 102

def file_path_for_thread(thread)
  File.join(path, file_name_for_thread(thread))
end
```

    
  

    
      
  
### 
  
    #**print**(path: ".")  ⇒ Object 
  

  

  

  
    
      

```

52
53
54
55
56
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_tree_printer.rb', line 52

def print(path: ".", **)
  @path = path
  determine_event_specification_and_value_scale
  print_threads
end
```

    
  

    
      
  
### 
  
    #**print_headers**(output, thread)  ⇒ Object 
  

  

  

  
    
      

```

106
107
108
109
110
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_tree_printer.rb', line 106

def print_headers(output, thread)
  output << "#{@event_specification}\n\n"
  # this doesn't work. kcachegrind does not fully support the spec.
  # output << "thread: #{thread.id}\n\n"
end
```

    
  

    
      
  
### 
  
    #**print_method**(output, method)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_tree_printer.rb', line 112

def print_method(output, method)
  # Print out the file and method name
  output << "fl=#{file(method)}\n"
  output << "fn=#{self.calltree_name(method)}\n"

  # Now print out the function line number and its self time
  output << "#{method.line} #{convert(method.self_time)}\n"

  # Now print out all the children methods
  method.call_trees.callees.each do |callee|
    output << "cfl=#{file(callee.target)}\n"
    output << "cfn=#{self.calltree_name(callee.target)}\n"
    output << "calls=#{callee.called} #{callee.line}\n"

    # Print out total times here!
    output << "#{callee.line} #{convert(callee.total_time)}\n"
  end
  output << "\n"
end
```

    
  

    
      
  
### 
  
    #**print_thread**(thread)  ⇒ Object 
  

  

  

  
    
      

```

73
74
75
76
77
78
79
80
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_tree_printer.rb', line 73

def print_thread(thread)
  File.open(file_path_for_thread(thread), "w") do |f|
    print_headers(f, thread)
    thread.methods.reverse_each do |method|
      print_method(f, method)
    end
  end
end
```

    
  

    
      
  
### 
  
    #**print_threads**  ⇒ Object 
  

  

  

  
    
      

```

58
59
60
61
62
63
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_tree_printer.rb', line 58

def print_threads
  remove_subsidiary_files_from_previous_profile_runs
  @result.threads.each do |thread|
    print_thread(thread)
  end
end
```

    
  

    
      
  
### 
  
    #**remove_subsidiary_files_from_previous_profile_runs**  ⇒ Object 
  

  

  

  
    
      

```

88
89
90
91
92
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_tree_printer.rb', line 88

def remove_subsidiary_files_from_previous_profile_runs
  pattern = ["callgrind.out", $$, "*"].join(".")
  files = Dir.glob(File.join(path, pattern))
  FileUtils.rm_f(files)
end
```