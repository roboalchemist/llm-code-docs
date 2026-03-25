# Class: Brakeman::Report::Base
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Brakeman::Report::Base
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Util
  
  
  

  

  
  
    Defined in:
    lib/brakeman/report/report_base.rb
  
  

## Overview

  
    

Base class for report formats

  

  

  
## Direct Known Subclasses

  

CSV, CodeClimate, Github, Hash, JSON, JUnit, SARIF, Sonar, Table, Text

  
## Constant Summary

  
  
### Constants included
     from Util

  

Util::ALL_COOKIES, Util::ALL_PARAMETERS, Util::COOKIES, Util::COOKIES_SEXP, Util::DIR_CONST, Util::LITERALS, Util::PARAMETERS, Util::PARAMS_SEXP, Util::PATH_PARAMETERS, Util::QUERY_PARAMETERS, Util::REQUEST_COOKIES, Util::REQUEST_ENV, Util::REQUEST_PARAMETERS, Util::REQUEST_PARAMS, Util::REQUEST_REQUEST_PARAMETERS, Util::SAFE_LITERAL, Util::SESSION, Util::SESSION_SEXP, Util::SIMPLE_LITERALS

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**checks**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute checks.

  

    
      
- 
  
    
      #**tracker**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute tracker.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**absolute_paths?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**all_warnings**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**context_for**(warning)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return array of lines surrounding the warning location from the original file.

  

      
        
- 
  
    
      #**controller_information**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**controller_warnings**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**filter_warnings**(warnings)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**generic_warnings**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**github_url**(file, line = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**ignored_warnings**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(tracker)  ⇒ Base 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Base.

  

      
        
- 
  
    
      #**model_warnings**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**number_of_templates**(tracker)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**rails_version**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**template_warnings**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**warning_file**(warning)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**warnings_summary**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return summary of warnings in hash and store in @warnings_summary.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Util

  

#all_literals?, #array?, #block?, #call?, #camelize, #class_name, #constant?, #contains_class?, #cookies?, #dir_glob?, #false?, #hash?, #hash_access, #hash_insert, #hash_iterate, #hash_values, #integer?, #kwsplat?, #literal?, #make_call, #node_type?, #number?, #params?, #pluralize, #recurse_check?, #regexp?, #remove_kwsplat, #request_headers?, #request_value?, #result?, #safe_literal, #safe_literal?, #safe_literal_target?, #set_env_defaults, #sexp?, #simple_literal?, #string?, #string_interp?, #symbol?, #template_path_to_name, #true?, #underscore

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(tracker)  ⇒ Base 
  

  

  

  
    

Returns a new instance of Base.

  

  

  
    
      

```

14
15
16
17
18
19
20
21
```

    
    
      

```
# File 'lib/brakeman/report/report_base.rb', line 14

def initialize tracker
  @app_tree = tracker.app_tree
  @tracker = tracker
  @checks = tracker.checks
  @ignore_filter = tracker.ignored_filter
  @highlight_user_input = tracker.options[:highlight_user_input]
  @warnings_summary = nil
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**checks**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute checks.

  

  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/brakeman/report/report_base.rb', line 12

def checks
  @checks
end
```

    
  

    
      
      
      
  
### 
  
    #**tracker**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute tracker.

  

  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/brakeman/report/report_base.rb', line 12

def tracker
  @tracker
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**absolute_paths?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

124
125
126
```

    
    
      

```
# File 'lib/brakeman/report/report_base.rb', line 124

def absolute_paths?
  @tracker.options[:absolute_paths]
end
```

    
  

    
      
  
### 
  
    #**all_warnings**  ⇒ Object 
  

  

  

  
    
      

```

78
79
80
81
82
83
84
```

    
    
      

```
# File 'lib/brakeman/report/report_base.rb', line 78

def all_warnings
  if @ignore_filter
    @all_warnings ||= @ignore_filter.shown_warnings
  else
    @all_warnings ||= tracker.checks.all_warnings
  end
end
```

    
  

    
      
  
### 
  
    #**context_for**(warning)  ⇒ Object 
  

  

  

  
    

Return array of lines surrounding the warning location from the original file.

  

  

  
    
      

```

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
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
```

    
    
      

```
# File 'lib/brakeman/report/report_base.rb', line 140

def context_for warning
  file = warning.file
  context = []
  return context unless warning.line and file and file.exists?

  current_line = 0
  start_line = warning.line - 5
  end_line = warning.line + 5

  start_line = 1 if start_line < 0

  File.open file do |f|
    f.each_line do |line|
      current_line += 1

      next if line.strip == ""

      if current_line > end_line
        break
      end

      if current_line >= start_line
        context << [current_line, line]
      end
    end
  end

  context
end
```

    
  

    
      
  
### 
  
    #**controller_information**  ⇒ Object 
  

  

  

  
    
      

```

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
73
74
75
76
```

    
    
      

```
# File 'lib/brakeman/report/report_base.rb', line 41

def controller_information
  controller_rows = []

  tracker.controllers.keys.map{|k| k.to_s}.sort.each do |name|
    name = name.to_sym
    c = tracker.controllers[name]

    if tracker.routes.include? :allow_all_actions or (tracker.routes[name] and tracker.routes[name].include? :allow_all_actions)
      routes = c.methods_public.keys.map{|e| e.to_s}.sort.join(", ")
    elsif tracker.routes[name].nil?
      #No routes defined for this controller.
      #This can happen when it is only a parent class
      #for other controllers, for example.
      routes = "[None]"

    else
      routes = (Set.new(c.methods_public.keys) & tracker.routes[name.to_sym]).
        to_a.
        map {|e| e.to_s}.
        sort.
        join(", ")
    end

    if routes == ""
      routes = "[None]"
    end

    controller_rows << { "Name" => name.to_s,
      "Parent" => c.parent.to_s,
      "Includes" => c.includes.join(", "),
      "Routes" => routes
    }
  end

  controller_rows
end
```

    
  

    
      
  
### 
  
    #**controller_warnings**  ⇒ Object 
  

  

  

  
    
      

```

108
109
110
```

    
    
      

```
# File 'lib/brakeman/report/report_base.rb', line 108

def controller_warnings
  filter_warnings tracker.checks.controller_warnings
end
```

    
  

    
      
  
### 
  
    #**filter_warnings**(warnings)  ⇒ Object 
  

  

  

  
    
      

```

86
87
88
89
90
91
92
93
94
```

    
    
      

```
# File 'lib/brakeman/report/report_base.rb', line 86

def filter_warnings warnings
  if @ignore_filter
    warnings.reject do |w|
      @ignore_filter.ignored? w
    end
  else
    warnings
  end
end
```

    
  

    
      
  
### 
  
    #**generic_warnings**  ⇒ Object 
  

  

  

  
    
      

```

96
97
98
```

    
    
      

```
# File 'lib/brakeman/report/report_base.rb', line 96

def generic_warnings
  filter_warnings tracker.checks.warnings
end
```

    
  

    
      
  
### 
  
    #**github_url**(file, line = nil)  ⇒ Object 
  

  

  

  
    
      

```

183
184
185
186
187
188
189
190
```

    
    
      

```
# File 'lib/brakeman/report/report_base.rb', line 183

def github_url file, line=nil
  if repo_url = @tracker.options[:github_url] and file
    url = "#{repo_url}/#{file.relative}"
    url << "#L#{line}" if line
  else
    nil
  end
end
```

    
  

    
      
  
### 
  
    #**ignored_warnings**  ⇒ Object 
  

  

  

  
    
      

```

112
113
114
115
116
117
118
```

    
    
      

```
# File 'lib/brakeman/report/report_base.rb', line 112

def ignored_warnings
  if @ignore_filter
    @ignore_filter.ignored_warnings
  else
    []
  end
end
```

    
  

    
      
  
### 
  
    #**model_warnings**  ⇒ Object 
  

  

  

  
    
      

```

104
105
106
```

    
    
      

```
# File 'lib/brakeman/report/report_base.rb', line 104

def model_warnings
  filter_warnings tracker.checks.model_warnings
end
```

    
  

    
      
  
### 
  
    #**number_of_templates**(tracker)  ⇒ Object 
  

  

  

  
    
      

```

120
121
122
```

    
    
      

```
# File 'lib/brakeman/report/report_base.rb', line 120

def number_of_templates tracker
  Set.new(tracker.templates.map {|k,v| v.name.to_s[/[^.]+/]}).length
end
```

    
  

    
      
  
### 
  
    #**rails_version**  ⇒ Object 
  

  

  

  
    
      

```

170
171
172
173
174
175
176
177
178
179
180
181
```

    
    
      

```
# File 'lib/brakeman/report/report_base.rb', line 170

def rails_version
  case
  when tracker.config.rails_version
    tracker.config.rails_version
  when tracker.options[:rails4]
    "4.x"
  when tracker.options[:rails3]
    "3.x"
  else
    "Unknown"
  end
end
```

    
  

    
      
  
### 
  
    #**template_warnings**  ⇒ Object 
  

  

  

  
    
      

```

100
101
102
```

    
    
      

```
# File 'lib/brakeman/report/report_base.rb', line 100

def template_warnings
  filter_warnings tracker.checks.template_warnings
end
```

    
  

    
      
  
### 
  
    #**warning_file**(warning)  ⇒ Object 
  

  

  

  
    
      

```

128
129
130
131
132
133
134
135
136
```

    
    
      

```
# File 'lib/brakeman/report/report_base.rb', line 128

def warning_file warning
  return nil if warning.file.nil?

  if absolute_paths?
    warning.file.absolute
  else
    warning.file.relative
  end
end
```

    
  

    
      
  
### 
  
    #**warnings_summary**  ⇒ Object 
  

  

  

  
    

Return summary of warnings in hash and store in @warnings_summary

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/report/report_base.rb', line 24

def warnings_summary
  return @warnings_summary if @warnings_summary

  summary = Hash.new(0)
  high_confidence_warnings = 0

  [all_warnings].each do |warnings|
    warnings.each do |warning|
      summary[warning.warning_type.to_s] += 1
      high_confidence_warnings += 1 if warning.confidence == 0
    end
  end

  summary[:high_confidence] = high_confidence_warnings
  @warnings_summary = summary
end
```