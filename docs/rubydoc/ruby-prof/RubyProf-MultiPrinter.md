# Class: RubyProf::MultiPrinter
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- RubyProf::MultiPrinter
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/ruby-prof/printers/multi_printer.rb
  
  

## Overview

  
    

Helper class to simplify printing profiles of several types from one profiling run. Currently prints a flat profile, a callgrind profile, a call stack profile and a graph profile.

  

  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**needs_dir?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**call_info_report**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

the name of the callinfo profile file.

  

      
        
- 
  
    
      #**dot_report**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

the name of the call stack profile file.

  

      
        
- 
  
    
      #**flame_graph_report**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

the name of the flame graph profile file.

  

      
        
- 
  
    
      #**flat_report**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

the name of the flat profile file.

  

      
        
- 
  
    
      #**graph_html_report**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**graph_report**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

the name of the graph profile file.

  

      
        
- 
  
    
      #**initialize**(result, printers = [:flat, :graph, :graph_html, :flame_graph, :stack])  ⇒ MultiPrinter 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of MultiPrinter.

  

      
        
- 
  
    
      #**print**(profile: "profile", path: File.expand_path("."), **options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create profile files under the specified directory.

  

      
        
- 
  
    
      #**print_to_call_info**(**options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_to_dot**(**options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_to_flame_graph**(**options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_to_flat**(**options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_to_graph**(**options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_to_graph_html**(**options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_to_stack**(**options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_to_tree**(**options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**stack_report**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

the name of the call stack profile file.

  

      
        
- 
  
    
      #**tree_report**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

the name of the callgrind profile file.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(result, printers = [:flat, :graph, :graph_html, :flame_graph, :stack])  ⇒ MultiPrinter 
  

  

  

  
    

Returns a new instance of MultiPrinter.

  

  

  
    
      

```

8
9
10
11
12
13
14
15
16
17
18
19
20
```

    
    
      

```
# File 'lib/ruby-prof/printers/multi_printer.rb', line 8

def initialize(result, printers = [:flat, :graph, :graph_html, :flame_graph, :stack])
  @flat_printer = printers.include?(:flat) ? FlatPrinter.new(result) : nil

  @graph_printer = printers.include?(:graph) ? GraphPrinter.new(result) : nil
  @graph_html_printer = printers.include?(:graph_html) ? GraphHtmlPrinter.new(result) : nil

  @tree_printer = printers.include?(:tree) ? CallTreePrinter.new(result) : nil
  @call_info_printer = printers.include?(:call_tree) ? CallInfoPrinter.new(result) : nil

  @stack_printer = printers.include?(:stack) ? CallStackPrinter.new(result) : nil
  @flame_graph_printer = printers.include?(:flame_graph) ? FlameGraphPrinter.new(result) : nil
  @dot_printer = printers.include?(:dot) ? DotPrinter.new(result) : nil
end
```

    
  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**needs_dir?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

22
23
24
```

    
    
      

```
# File 'lib/ruby-prof/printers/multi_printer.rb', line 22

def self.needs_dir?
  true
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**call_info_report**  ⇒ Object 
  

  

  

  
    

the name of the callinfo profile file

  

  

  
    
      

```

64
65
66
```

    
    
      

```
# File 'lib/ruby-prof/printers/multi_printer.rb', line 64

def call_info_report
  "#{@directory}/#{@file_name}.call_tree.txt"
end
```

    
  

    
      
  
### 
  
    #**dot_report**  ⇒ Object 
  

  

  

  
    

the name of the call stack profile file

  

  

  
    
      

```

84
85
86
```

    
    
      

```
# File 'lib/ruby-prof/printers/multi_printer.rb', line 84

def dot_report
  "#{@directory}/#{@file_name}.dot"
end
```

    
  

    
      
  
### 
  
    #**flame_graph_report**  ⇒ Object 
  

  

  

  
    

the name of the flame graph profile file

  

  

  
    
      

```

79
80
81
```

    
    
      

```
# File 'lib/ruby-prof/printers/multi_printer.rb', line 79

def flame_graph_report
  "#{@directory}/#{@file_name}.flame_graph.html"
end
```

    
  

    
      
  
### 
  
    #**flat_report**  ⇒ Object 
  

  

  

  
    

the name of the flat profile file

  

  

  
    
      

```

50
51
52
```

    
    
      

```
# File 'lib/ruby-prof/printers/multi_printer.rb', line 50

def flat_report
  "#{@directory}/#{@file_name}.flat.txt"
end
```

    
  

    
      
  
### 
  
    #**graph_html_report**  ⇒ Object 
  

  

  

  
    
      

```

59
60
61
```

    
    
      

```
# File 'lib/ruby-prof/printers/multi_printer.rb', line 59

def graph_html_report
  "#{@directory}/#{@file_name}.graph.html"
end
```

    
  

    
      
  
### 
  
    #**graph_report**  ⇒ Object 
  

  

  

  
    

the name of the graph profile file

  

  

  
    
      

```

55
56
57
```

    
    
      

```
# File 'lib/ruby-prof/printers/multi_printer.rb', line 55

def graph_report
  "#{@directory}/#{@file_name}.graph.txt"
end
```

    
  

    
      
  
### 
  
    #**print**(profile: "profile", path: File.expand_path("."), **options)  ⇒ Object 
  

  

  

  
    

Create profile files under the specified directory.

Keyword arguments:

```
profile: - Base name for profile files. Default is "profile".
path:    - Directory to write files to. Default is current directory.

```

Also accepts min_percent:, sort_method:, and other printer-specific kwargs.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/ruby-prof/printers/multi_printer.rb', line 33

def print(profile: "profile", path: File.expand_path("."), **options)
  @file_name = profile
  @directory = path

  print_to_flat(**options) if @flat_printer

  print_to_graph(**options) if @graph_printer
  print_to_graph_html(**options) if @graph_html_printer

  print_to_stack(**options) if @stack_printer
  print_to_flame_graph(**options) if @flame_graph_printer
  print_to_call_info(**options) if @call_info_printer
  print_to_tree(**options) if @tree_printer
  print_to_dot(**options) if @dot_printer
end
```

    
  

    
      
  
### 
  
    #**print_to_call_info**(**options)  ⇒ Object 
  

  

  

  
    
      

```

106
107
108
109
110
```

    
    
      

```
# File 'lib/ruby-prof/printers/multi_printer.rb', line 106

def print_to_call_info(**options)
  File.open(call_info_report, "wb") do |file|
    @call_info_printer.print(file, **options)
  end
end
```

    
  

    
      
  
### 
  
    #**print_to_dot**(**options)  ⇒ Object 
  

  

  

  
    
      

```

128
129
130
131
132
```

    
    
      

```
# File 'lib/ruby-prof/printers/multi_printer.rb', line 128

def print_to_dot(**options)
  File.open(dot_report, "wb") do |file|
    @dot_printer.print(file, **options)
  end
end
```

    
  

    
      
  
### 
  
    #**print_to_flame_graph**(**options)  ⇒ Object 
  

  

  

  
    
      

```

122
123
124
125
126
```

    
    
      

```
# File 'lib/ruby-prof/printers/multi_printer.rb', line 122

def print_to_flame_graph(**options)
  File.open(flame_graph_report, "wb") do |file|
    @flame_graph_printer.print(file, **options)
  end
end
```

    
  

    
      
  
### 
  
    #**print_to_flat**(**options)  ⇒ Object 
  

  

  

  
    
      

```

88
89
90
91
92
```

    
    
      

```
# File 'lib/ruby-prof/printers/multi_printer.rb', line 88

def print_to_flat(**options)
  File.open(flat_report, "wb") do |file|
    @flat_printer.print(file, **options)
  end
end
```

    
  

    
      
  
### 
  
    #**print_to_graph**(**options)  ⇒ Object 
  

  

  

  
    
      

```

94
95
96
97
98
```

    
    
      

```
# File 'lib/ruby-prof/printers/multi_printer.rb', line 94

def print_to_graph(**options)
  File.open(graph_report, "wb") do |file|
    @graph_printer.print(file, **options)
  end
end
```

    
  

    
      
  
### 
  
    #**print_to_graph_html**(**options)  ⇒ Object 
  

  

  

  
    
      

```

100
101
102
103
104
```

    
    
      

```
# File 'lib/ruby-prof/printers/multi_printer.rb', line 100

def print_to_graph_html(**options)
  File.open(graph_html_report, "wb") do |file|
    @graph_html_printer.print(file, **options)
  end
end
```

    
  

    
      
  
### 
  
    #**print_to_stack**(**options)  ⇒ Object 
  

  

  

  
    
      

```

116
117
118
119
120
```

    
    
      

```
# File 'lib/ruby-prof/printers/multi_printer.rb', line 116

def print_to_stack(**options)
  File.open(stack_report, "wb") do |file|
    @stack_printer.print(file, **options)
  end
end
```

    
  

    
      
  
### 
  
    #**print_to_tree**(**options)  ⇒ Object 
  

  

  

  
    
      

```

112
113
114
```

    
    
      

```
# File 'lib/ruby-prof/printers/multi_printer.rb', line 112

def print_to_tree(**options)
  @tree_printer.print(path: @directory, **options)
end
```

    
  

    
      
  
### 
  
    #**stack_report**  ⇒ Object 
  

  

  

  
    

the name of the call stack profile file

  

  

  
    
      

```

74
75
76
```

    
    
      

```
# File 'lib/ruby-prof/printers/multi_printer.rb', line 74

def stack_report
  "#{@directory}/#{@file_name}.stack.html"
end
```

    
  

    
      
  
### 
  
    #**tree_report**  ⇒ Object 
  

  

  

  
    

the name of the callgrind profile file

  

  

  
    
      

```

69
70
71
```

    
    
      

```
# File 'lib/ruby-prof/printers/multi_printer.rb', line 69

def tree_report
  "#{@directory}/#{@file_name}.callgrind.out.#{$$}"
end
```