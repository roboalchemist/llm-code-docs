# Class: RubyProf::CallStackPrinter
  
  
  

  
  
    Inherits:
    
      AbstractPrinter
      
        

          
- Object
          
            
- AbstractPrinter
          
            
- RubyProf::CallStackPrinter
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      ERB::Util
  
  
  

  

  
  
    Defined in:
    lib/ruby-prof/printers/call_stack_printer.rb
  
  

## Overview

  
    

Prints a HTML visualization of the call tree.

To use the printer:

```
result = RubyProf.profile do
  [code to profile]
end

printer = RubyProf::CallStackPrinter.new(result)
printer.print(STDOUT)

```

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**application**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute application.

  

    
      
- 
  
    
      #**expansion**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute expansion.

  

    
      
- 
  
    
      #**threshold**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute threshold.

  

    
      
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
  
    
      #**arguments**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**base64_image**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**color**(p)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**dump**(ci)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**graph_link**(call_tree)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**link**(method, recursive)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**method_href**(method)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**name**(call_tree)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print**(output = STDOUT, title: "ruby-prof call stack", threshold: 1.0, expansion: 10.0, application: $PROGRAM_NAME, min_percent: 0, max_percent: 100, filter_by: :self_time, sort_method: nil, max_depth: nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Specify print options.

  

      
        
- 
  
    
      #**print_stack**(output, visited, call_tree, parent_time, depth = 0)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**sum**(a)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**template**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**total_time**(call_trees)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
  
### Methods inherited from AbstractPrinter

  

#initialize, #method_location, needs_dir?, #open_asset, #print_column_headers, #print_footer, #print_header, #print_thread, #print_threads, #time_format

  
## Constructor Details

  
    

This class inherits a constructor from RubyProf::AbstractPrinter
  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**application**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute application.

  

  

  
    
      

```

152
153
154
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_stack_printer.rb', line 152

def application
  @application
end
```

    
  

    
      
      
      
  
### 
  
    #**expansion**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute expansion.

  

  

  
    
      

```

152
153
154
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_stack_printer.rb', line 152

def expansion
  @expansion
end
```

    
  

    
      
      
      
  
### 
  
    #**threshold**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute threshold.

  

  

  
    
      

```

152
153
154
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_stack_printer.rb', line 152

def threshold
  @threshold
end
```

    
  

    
      
      
      
  
### 
  
    #**title**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute title.

  

  

  
    
      

```

152
153
154
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_stack_printer.rb', line 152

def title
  @title
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**arguments**  ⇒ Object 
  

  

  

  
    
      

```

154
155
156
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_stack_printer.rb', line 154

def arguments
  ARGV.join(' ')
end
```

    
  

    
      
  
### 
  
    #**base64_image**  ⇒ Object 
  

  

  

  
    
      

```

158
159
160
161
162
163
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_stack_printer.rb', line 158

def base64_image
  @data ||= begin
    file = open_asset('call_stack_printer.png')
    Base64.encode64(file).gsub(/\n/, '')
  end
end
```

    
  

    
      
  
### 
  
    #**color**(p)  ⇒ Object 
  

  

  

  
    
      

```

139
140
141
142
143
144
145
146
147
148
149
150
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_stack_printer.rb', line 139

def color(p)
  case i = p.to_i
  when 0..5
    "01"
  when 5..10
    "05"
  when 100
    "9"
  else
    "#{i/10}"
  end
end
```

    
  

    
      
  
### 
  
    #**dump**(ci)  ⇒ Object 
  

  

  

  
    
      

```

135
136
137
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_stack_printer.rb', line 135

def dump(ci)
  $stderr.printf "%s/%d t:%f s:%f w:%f  \n", ci, ci.object_id, ci.total_time, ci.self_time, ci.wait_time
end
```

    
  

    
      
  
### 
  
    #**graph_link**(call_tree)  ⇒ Object 
  

  

  

  
    
      

```

117
118
119
120
121
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_stack_printer.rb', line 117

def graph_link(call_tree)
  total_calls = call_tree.target.called
  totals = total_calls.to_s
  "[#{call_tree.called} calls, #{totals} total]"
end
```

    
  

    
      
  
### 
  
    #**link**(method, recursive)  ⇒ Object 
  

  

  

  
    
      

```

107
108
109
110
111
112
113
114
115
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_stack_printer.rb', line 107

def link(method, recursive)
  method_name = "#{recursive ? '*' : ''}#{method.full_name}"
  if method.source_file.nil?
    h method_name
  else
    file = File.expand_path(method.source_file)
   "<a href=\"file://#{file}##{method.line}\">#{h method_name}</a>"
  end
end
```

    
  

    
      
  
### 
  
    #**method_href**(method)  ⇒ Object 
  

  

  

  
    
      

```

123
124
125
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_stack_printer.rb', line 123

def method_href(method)
  h(method.full_name.gsub(/[><#\.\?=:]/,"_"))
end
```

    
  

    
      
  
### 
  
    #**name**(call_tree)  ⇒ Object 
  

  

  

  
    
      

```

102
103
104
105
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_stack_printer.rb', line 102

def name(call_tree)
  method = call_tree.target
  method.full_name
end
```

    
  

    
      
  
### 
  
    #**print**(output = STDOUT, title: "ruby-prof call stack", threshold: 1.0, expansion: 10.0, application: $PROGRAM_NAME, min_percent: 0, max_percent: 100, filter_by: :self_time, sort_method: nil, max_depth: nil)  ⇒ Object 
  

  

  

  
    

Specify print options.

output     - Any IO object, including STDOUT or a file.

Keyword arguments:

```
title:       - a String to override the default "ruby-prof call stack"
               title of the report.

threshold:   - a float from 0 to 100 that sets the threshold of
               results displayed.
               Default value is 1.0

expansion:   - a float from 0 to 100 that sets the threshold of
               results that are expanded, if the percent_total
               exceeds it.
               Default value is 10.0

application: - a String to override the name of the application,
               as it appears on the report.

```

Also accepts min_percent:, max_percent:, filter_by:, and sort_method: from AbstractPrinter.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_stack_printer.rb', line 46

def print(output = STDOUT, title: "ruby-prof call stack", threshold: 1.0,
          expansion: 10.0, application: $PROGRAM_NAME,
          min_percent: 0, max_percent: 100, filter_by: :self_time, sort_method: nil, max_depth: nil, **)
  @min_percent = min_percent
  @max_percent = max_percent
  @filter_by = filter_by
  @sort_method = sort_method
  @max_depth = max_depth
  @title = title
  @threshold = threshold
  @expansion = expansion
  @application = application
  output << ERB.new(self.template).result(binding)
end
```

    
  

    
      
  
### 
  
    #**print_stack**(output, visited, call_tree, parent_time, depth = 0)  ⇒ Object 
  

  

  

  
    
      

```

61
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
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_stack_printer.rb', line 61

def print_stack(output, visited, call_tree, parent_time, depth = 0)
  total_time = call_tree.total_time
  percent_parent = (total_time/parent_time)*100
  percent_total = (total_time/@overall_time)*100
  return unless percent_total > min_percent
  color = self.color(percent_total)
  visible = percent_total >= threshold
  expanded = percent_total >= expansion
  display = visible ? "block" : "none"

  output << "<li class=\"color#{color}\" style=\"display:#{display}\">" << "\n"

  if visited.include?(call_tree)
    output << "<a href=\"#\" class=\"toggle empty\" ></a>" << "\n"
    output << "<span>%s %s</span>" % [link(call_tree.target, true), graph_link(call_tree)] << "\n"
  else
    visited << call_tree

    if call_tree.children.empty? || (@max_depth && depth >= @max_depth)
      output << "<a href=\"#\" class=\"toggle empty\" ></a>" << "\n"
    else
      visible_children = call_tree.children.any?{|ci| (ci.total_time/@overall_time)*100 >= threshold}
      image = visible_children ? (expanded ? "minus" : "plus") : "empty"
      output << "<a href=\"#\" class=\"toggle #{image}\" ></a>" << "\n"
    end
    output << "<span>%4.2f%% (%4.2f%%) %s %s</span>" % [percent_total, percent_parent,
                                                        link(call_tree.target, false), graph_link(call_tree)] << "\n"

    unless call_tree.children.empty? || (@max_depth && depth >= @max_depth)
      output <<  (expanded ? '<ul>' : '<ul style="display:none">')  << "\n"
      call_tree.children.sort_by{|c| -c.total_time}.each do |child_call_tree|
        print_stack(output, visited, child_call_tree, total_time, depth + 1)
      end
      output << '</ul>' << "\n"
    end

    visited.delete(call_tree)
  end
  output << '</li>' << "\n"
end
```

    
  

    
      
  
### 
  
    #**sum**(a)  ⇒ Object 
  

  

  

  
    
      

```

131
132
133
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_stack_printer.rb', line 131

def sum(a)
  a.inject(0.0){|s,t| s+=t}
end
```

    
  

    
      
  
### 
  
    #**template**  ⇒ Object 
  

  

  

  
    
      

```

165
166
167
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_stack_printer.rb', line 165

def template
  open_asset('call_stack_printer.html.erb')
end
```

    
  

    
      
  
### 
  
    #**total_time**(call_trees)  ⇒ Object 
  

  

  

  
    
      

```

127
128
129
```

    
    
      

```
# File 'lib/ruby-prof/printers/call_stack_printer.rb', line 127

def total_time(call_trees)
  sum(call_trees.map{|ci| ci.total_time})
end
```