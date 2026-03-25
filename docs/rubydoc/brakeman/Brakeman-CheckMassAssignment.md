# Class: Brakeman::CheckMassAssignment
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckMassAssignment
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_mass_assignment.rb
  
  

## Overview

  
    

Checks for mass assignments to models.

See guides.rubyonrails.org/security.html#mass-assignment for details

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        LITERALS =
          
        
        

```

```

      
    
  

  
  
  
### Constants inherited
     from BaseCheck

  

BaseCheck::CONFIDENCE

  
  
  
### Constants included
     from Util

  

Util::ALL_COOKIES, Util::ALL_PARAMETERS, Util::COOKIES, Util::COOKIES_SEXP, Util::DIR_CONST, Util::PARAMETERS, Util::PARAMS_SEXP, Util::PATH_PARAMETERS, Util::QUERY_PARAMETERS, Util::REQUEST_COOKIES, Util::REQUEST_ENV, Util::REQUEST_PARAMETERS, Util::REQUEST_PARAMS, Util::REQUEST_REQUEST_PARAMETERS, Util::SAFE_LITERAL, Util::SESSION, Util::SESSION_SEXP, Util::SIMPLE_LITERALS

  
  
  
### Constants inherited
     from SexpProcessor

  

SexpProcessor::VERSION

  
## Instance Attribute Summary

  
  
### Attributes inherited from BaseCheck

  

#tracker, #warnings

  
  
  
### Attributes inherited from SexpProcessor

  

#context, #env, #expected

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**all_literal_args?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**calls_slice?**(result)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_call**(call)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Want to ignore calls to Model.new that have no arguments.

  

      
        
- 
  
    
      #**check_mass_assignment**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_permit!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Look for and warn about uses of Parameters#permit! for mass assignment.

  

      
        
- 
  
    
      #**check_permit_all_parameters**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**find_mass_assign_calls**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ CheckMassAssignment 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of CheckMassAssignment.

  

      
        
- 
  
    
      #**inside_safe_method?**(result)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Ignore blah_some_path(params.permit!).

  

      
        
- 
  
    
      #**literal?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_result**(res)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

All results should be Model.new(…) or Model.attributes=() calls.

  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**subsequent_mass_assignment?**(result)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Look for actual use of params in mass assignment to avoid warning about uses of Parameters#permit! without any mass assignment or when mass assignment is restricted by model instead.

  

      
        
- 
  
    
      #**warn_on_permit!**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from BaseCheck

  

#add_result, description, inherited, #process_array, #process_call, #process_cookies, #process_default, #process_dstr, #process_if, #process_params

  
  
  
  
  
  
  
  
  
### Methods included from Messages

  

#msg, #msg_code, #msg_cve, #msg_file, #msg_input, #msg_lit, #msg_plain, #msg_version

  
  
  
  
  
  
  
  
  
### Methods included from Util

  

#all_literals?, #array?, #block?, #call?, #camelize, #class_name, #constant?, #contains_class?, #cookies?, #dir_glob?, #false?, #hash?, #hash_access, #hash_insert, #hash_iterate, #hash_values, #integer?, #kwsplat?, #make_call, #node_type?, #number?, #params?, #pluralize, #rails_version, #recurse_check?, #regexp?, #remove_kwsplat, #request_headers?, #request_value?, #result?, #safe_literal, #safe_literal?, #safe_literal_target?, #set_env_defaults, #sexp?, #simple_literal?, #string?, #string_interp?, #symbol?, #template_path_to_name, #true?, #underscore

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from ProcessorHelper

  

#current_file, #process_all, #process_all!, #process_call_args, #process_call_defn?, #process_class, #process_module

  
  
  
  
  
  
  
  
  
### Methods inherited from SexpProcessor

  

#in_context, #process, processors, #scope

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ CheckMassAssignment 
  

  

  

  
    

Returns a new instance of CheckMassAssignment.

  

  

  
    
      

```

12
13
14
15
```

    
    
      

```
# File 'lib/brakeman/checks/check_mass_assignment.rb', line 12

def initialize(*)
  super
  @mass_assign_calls = nil
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**all_literal_args?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

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
142
143
144
145
```

    
    
      

```
# File 'lib/brakeman/checks/check_mass_assignment.rb', line 132

def all_literal_args? exp
  if call? exp
    exp.each_arg do |arg|
      return false unless literal? arg
    end

    true
  else
    exp.all? do |arg|
      literal? arg
    end
  end

end
```

    
  

    
      
  
### 
  
    #**calls_slice?**(result)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

178
179
180
181
```

    
    
      

```
# File 'lib/brakeman/checks/check_mass_assignment.rb', line 178

def calls_slice? result
  result[:chain].include? :slice or
    (result[:full_call] and result[:full_call][:chain].include? :slice)
end
```

    
  

    
      
  
### 
  
    #**check_call**(call)  ⇒ Object 
  

  

  

  
    

Want to ignore calls to Model.new that have no arguments

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_mass_assignment.rb', line 110

def check_call call
  process_call_args call

  if call.method == :update
    arg = call.second_arg
  else
    arg = call.first_arg
  end

  if arg.nil? #empty new()
    false
  elsif hash? arg and not include_user_input? arg
    false
  elsif all_literal_args? call
    false
  else
    true
  end
end
```

    
  

    
      
  
### 
  
    #**check_mass_assignment**  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/brakeman/checks/check_mass_assignment.rb', line 54

def check_mass_assignment
  return if mass_assign_disabled?

  Brakeman.debug "Processing possible mass assignment calls"
  find_mass_assign_calls.each do |result|
    process_result result
  end
end
```

    
  

    
      
  
### 
  
    #**check_permit!**  ⇒ Object 
  

  

  

  
    

Look for and warn about uses of Parameters#permit! for mass assignment

  

  

  
    
      

```

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
# File 'lib/brakeman/checks/check_mass_assignment.rb', line 160

def check_permit!
  tracker.find_call(:method => :permit!, :nested => true).each do |result|
    if params? result[:call].target
      unless inside_safe_method? result or calls_slice? result
        warn_on_permit! result
      end
    end
  end
end
```

    
  

    
      
  
### 
  
    #**check_permit_all_parameters**  ⇒ Object 
  

  

  

  
    
      

```

213
214
215
216
217
218
219
220
221
222
223
224
225
226
```

    
    
      

```
# File 'lib/brakeman/checks/check_mass_assignment.rb', line 213

def check_permit_all_parameters
  tracker.find_call(target: :"ActionController::Parameters", method: :permit_all_parameters=).each do |result|
    call = result[:call]

    if true? call.first_arg
      warn :result => result,
        :warning_type => "Mass Assignment",
        :warning_code => :mass_assign_permit_all,
        :message => msg('Mass assignment is globally enabled. Disable and specify exact keys using ', msg_code('params.permit'), ' instead'),
        :confidence => :high,
        :cwe_id => [915]
    end
  end
end
```

    
  

    
      
  
### 
  
    #**find_mass_assign_calls**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_mass_assignment.rb', line 23

def find_mass_assign_calls
  return @mass_assign_calls if @mass_assign_calls

  models = []
  tracker.models.each do |name, m|
    if m.is_a? Hash
      p m
    end
    if m.unprotected_model?
      models << name
    end
  end

  return [] if models.empty?

  Brakeman.debug "Finding possible mass assignment calls on #{models.length} models"
  @mass_assign_calls = tracker.find_call :chained => true, :targets => models, :methods => [:new,
    :attributes=,
    :update_attributes,
    :update_attributes!,
    :create,
    :create!,
    :build,
    :first_or_create,
    :first_or_create!,
    :first_or_initialize!,
    :assign_attributes,
    :update
  ]
end
```

    
  

    
      
  
### 
  
    #**inside_safe_method?**(result)  ⇒ Boolean 
  

  

  

  
    

Ignore blah_some_path(params.permit!)

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

171
172
173
174
175
176
```

    
    
      

```
# File 'lib/brakeman/checks/check_mass_assignment.rb', line 171

def inside_safe_method? result
  parent_call = result.dig(:parent, :call)

  call? parent_call and
    parent_call.method.match(/_path$/)
end
```

    
  

    
      
  
### 
  
    #**literal?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_mass_assignment.rb', line 147

def literal? exp
  if sexp? exp
    if exp.node_type == :hash
      all_literal_args? exp
    else
      LITERALS.include? exp.node_type
    end
  else
    true
  end
end
```

    
  

    
      
  
### 
  
    #**process_result**(res)  ⇒ Object 
  

  

  

  
    

All results should be Model.new(…) or Model.attributes=() calls

  

  

  
    
      

```

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
101
102
103
104
105
106
107
```

    
    
      

```
# File 'lib/brakeman/checks/check_mass_assignment.rb', line 64

def process_result res
  call = res[:call]

  check = check_call call

  if check and original? res

    model = tracker.models[res[:chain].first]
    attr_protected = (model and model.attr_protected)
    first_arg = call.first_arg

    if attr_protected and tracker.options[:ignore_attr_protected]
      return
    elsif call? first_arg and (first_arg.method == :slice or first_arg.method == :only)
      return
    elsif input = include_user_input?(call.arglist)
      if not node_type? first_arg, :hash
        if attr_protected
          confidence = :medium
        else
          confidence = :high
        end
      else
        return
      end
    elsif node_type? call.first_arg, :lit, :str
      return
    else
      confidence = :weak
      input = nil
    end

    warn :result => res,
      :warning_type => "Mass Assignment",
      :warning_code => :mass_assign_call,
      :message => "Unprotected mass assignment",
      :code => call,
      :user_input => input,
      :confidence => confidence,
      :cwe_id => [915]
  end

  res
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
20
21
```

    
    
      

```
# File 'lib/brakeman/checks/check_mass_assignment.rb', line 17

def run_check
  check_mass_assignment
  check_permit!
  check_permit_all_parameters
end
```

    
  

    
      
  
### 
  
    #**subsequent_mass_assignment?**(result)  ⇒ Boolean 
  

  

  

  
    

Look for actual use of params in mass assignment to avoid warning about uses of Parameters#permit! without any mass assignment or when mass assignment is restricted by model instead.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

186
187
188
189
190
191
192
193
194
```

    
    
      

```
# File 'lib/brakeman/checks/check_mass_assignment.rb', line 186

def subsequent_mass_assignment? result
  location = result[:location]
  line = result[:call].line
  find_mass_assign_calls.any? do |call|
    call[:location] == location and
    params? call[:call].first_arg and
    call[:call].line >= line
  end
end
```

    
  

    
      
  
### 
  
    #**warn_on_permit!**(result)  ⇒ Object 
  

  

  

  
    
      

```

196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
```

    
    
      

```
# File 'lib/brakeman/checks/check_mass_assignment.rb', line 196

def warn_on_permit! result
  return unless original? result

  confidence = if subsequent_mass_assignment? result
                 :high
               else
                 :medium
               end

  warn :result => result,
    :warning_type => "Mass Assignment",
    :warning_code => :mass_assign_permit!,
    :message => msg('Specify exact keys allowed for mass assignment instead of using ', msg_code('permit!'), ' which allows any keys'),
    :confidence => confidence,
    :cwe_id => [915]
end
```