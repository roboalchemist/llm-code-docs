# Class: Brakeman::CallIndex
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Brakeman::CallIndex
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/call_index.rb
  
  

## Overview

  
    

Stores call sites to look up later.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**find_calls**(options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Find calls matching specified option hash.

  

      
        
- 
  
    
      #**index_calls**(calls)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(calls)  ⇒ CallIndex 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize index with calls from FindAllCalls.

  

      
        
- 
  
    
      #**remove_indexes_by_class**(classes)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**remove_indexes_by_file**(file)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**remove_template_indexes**(template_name = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(calls)  ⇒ CallIndex 
  

  

  

  
    

Initialize index with calls from FindAllCalls

  

  

  
    
      

```

7
8
9
10
11
12
```

    
    
      

```
# File 'lib/brakeman/call_index.rb', line 7

def initialize calls
  @calls_by_method = {}
  @calls_by_target = {}

  index_calls calls
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**find_calls**(options)  ⇒ Object 
  

  

  

  
    

Find calls matching specified option hash.

Options:

```
* :target - symbol, array of symbols, or regular expression to match target(s)
* :method - symbol, array of symbols, or regular expression to match method(s)
* :chained - boolean, whether or not to match against a whole method chain (false by default)
* :nested - boolean, whether or not to match against a method call that is a target itself (false by default)

```

  

  

  
    
      

```

22
23
24
25
26
27
28
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
# File 'lib/brakeman/call_index.rb', line 22

def find_calls options
  target = options[:target] || options[:targets]
  method = options[:method] || options[:methods]
  nested = options[:nested]

  if options[:chained]
    return find_chain options
  #Find by narrowest category
  elsif target.is_a? Array and method.is_a? Array
    if target.length > method.length
      calls = filter_by_target calls_by_methods(method), target
    else
      calls = calls_by_targets(target)
      calls = filter_by_method calls, method
    end

  elsif target.is_a? Regexp and method
    calls = filter_by_target(calls_by_method(method), target)

  elsif method.is_a? Regexp and target
    calls = filter_by_method(calls_by_target(target), method)

  #Find by target, then by methods, if provided
  elsif target
    calls = calls_by_target target

    if calls and method
      calls = filter_by_method calls, method
    end

  #Find calls with no explicit target
  #with either :target => nil or :target => false
  elsif (options.key? :target or options.key? :targets) and not target and method
    calls = calls_by_method method
    calls = filter_by_target calls, nil

  #Find calls by method
  elsif method
    calls = calls_by_method method
  else
    raise "Invalid arguments to CallCache#find_calls: #{options.inspect}"
  end

  return [] if calls.nil?

  #Remove calls that are actually targets of other calls
  #Unless those are explicitly desired
  calls = filter_nested calls unless nested

  calls
end
```

    
  

    
      
  
### 
  
    #**index_calls**(calls)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/call_index.rb', line 104

def index_calls calls
  calls.each do |call|
    @calls_by_method[call[:method]] ||= []
    @calls_by_method[call[:method]] << call

    target = call[:target]

    if not target.is_a? Sexp
      @calls_by_target[target] ||= []
      @calls_by_target[target] << call
    elsif target.node_type == :params or target.node_type == :session
      @calls_by_target[target.node_type] ||= []
      @calls_by_target[target.node_type] << call
    end
  end
end
```

    
  

    
      
  
### 
  
    #**remove_indexes_by_class**(classes)  ⇒ Object 
  

  

  

  
    
      

```

84
85
86
87
88
89
90
91
92
```

    
    
      

```
# File 'lib/brakeman/call_index.rb', line 84

def remove_indexes_by_class classes
  [@calls_by_method, @calls_by_target].each do |calls_by|
    calls_by.each do |_name, calls|
      calls.delete_if do |call|
        call[:location][:type] == :class and classes.include? call[:location][:class]
      end
    end
  end
end
```

    
  

    
      
  
### 
  
    #**remove_indexes_by_file**(file)  ⇒ Object 
  

  

  

  
    
      

```

94
95
96
97
98
99
100
101
102
```

    
    
      

```
# File 'lib/brakeman/call_index.rb', line 94

def remove_indexes_by_file file
  [@calls_by_method, @calls_by_target].each do |calls_by|
    calls_by.each do |_name, calls|
      calls.delete_if do |call|
        call[:location][:file] == file
      end
    end
  end
end
```

    
  

    
      
  
### 
  
    #**remove_template_indexes**(template_name = nil)  ⇒ Object 
  

  

  

  
    
      

```

74
75
76
77
78
79
80
81
82
```

    
    
      

```
# File 'lib/brakeman/call_index.rb', line 74

def remove_template_indexes template_name = nil
  [@calls_by_method, @calls_by_target].each do |calls_by|
    calls_by.each do |_name, calls|
      calls.delete_if do |call|
        from_template call, template_name
      end
    end
  end
end
```