# Class: Brakeman::CheckRedirect
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckRedirect
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_redirect.rb
  
  

## Overview

  
    

Reports any calls to `redirect_to` which include parameters in the arguments.

For example:

redirect_to params.merge(:action => :elsewhere)

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        DANGEROUS_KEYS =
          
        
        

```
[:host, :subdomain, :domain, :port]
```

      
    
  

  
  
  
### Constants inherited
     from BaseCheck

  

BaseCheck::CONFIDENCE

  
  
  
### Constants included
     from Util

  

Util::ALL_COOKIES, Util::ALL_PARAMETERS, Util::COOKIES, Util::COOKIES_SEXP, Util::DIR_CONST, Util::LITERALS, Util::PARAMETERS, Util::PARAMS_SEXP, Util::PATH_PARAMETERS, Util::QUERY_PARAMETERS, Util::REQUEST_COOKIES, Util::REQUEST_ENV, Util::REQUEST_PARAMETERS, Util::REQUEST_PARAMS, Util::REQUEST_REQUEST_PARAMETERS, Util::SAFE_LITERAL, Util::SESSION, Util::SESSION_SEXP, Util::SIMPLE_LITERALS

  
  
  
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
  
    
      #**allow_other_host?**(call)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**association?**(model_name, meth)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Check if method is actually an association in a Model.

  

      
        
- 
  
    
      #**call_has_param**(arg, key)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_url_for**(call)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

`url_for` is only_path => true by default.

  

      
        
- 
  
    
      #**decorated_model?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns true if exp is (probably) a decorated model instance using the Draper gem.

  

      
        
- 
  
    
      #**disallow_other_host?**(call)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**explicit_host?**(arg)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**friendly_model?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns true if exp is (probably) a friendly model instance using the FriendlyId gem.

  

      
        
- 
  
    
      #**has_only_path?**(arg)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**include_user_input?**(opt, immediate = :immediate)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Custom check for user input.

  

      
        
- 
  
    
      #**model_instance?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns true if exp is (probably) a model instance.

  

      
        
- 
  
    
      #**model_target?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**only_path?**(call)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Checks `redirect_to` arguments for only_path => true which essentially nullifies the danger posed by redirecting with user input.

  

      
        
- 
  
    
      #**process_result**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**protected_by_raise?**(call)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**raise_on_redirects?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**safe_permit?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**slice_call?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**use_unsafe_hash_method?**(arg)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from BaseCheck

  

#add_result, description, inherited, #initialize, #process_array, #process_call, #process_cookies, #process_default, #process_dstr, #process_if, #process_params

  
  
  
  
  
  
  
  
  
### Methods included from Messages

  

#msg, #msg_code, #msg_cve, #msg_file, #msg_input, #msg_lit, #msg_plain, #msg_version

  
  
  
  
  
  
  
  
  
### Methods included from Util

  

#all_literals?, #array?, #block?, #call?, #camelize, #class_name, #constant?, #contains_class?, #cookies?, #dir_glob?, #false?, #hash?, #hash_access, #hash_insert, #hash_iterate, #hash_values, #integer?, #kwsplat?, #literal?, #make_call, #node_type?, #number?, #params?, #pluralize, #rails_version, #recurse_check?, #regexp?, #remove_kwsplat, #request_headers?, #request_value?, #result?, #safe_literal, #safe_literal?, #safe_literal_target?, #set_env_defaults, #sexp?, #simple_literal?, #string?, #string_interp?, #symbol?, #template_path_to_name, #true?, #underscore

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from ProcessorHelper

  

#current_file, #process_all, #process_all!, #process_call_args, #process_call_defn?, #process_class, #process_module

  
  
  
  
  
  
  
  
  
### Methods inherited from SexpProcessor

  

#in_context, #initialize, #process, processors, #scope

  
## Constructor Details

  
    

This class inherits a constructor from Brakeman::BaseCheck
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**allow_other_host?**(call)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

281
282
283
284
285
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 281

def allow_other_host? call
  opt = call.last_arg

  hash? opt and true? hash_access(opt, :allow_other_host)
end
```

    
  

    
      
  
### 
  
    #**association?**(model_name, meth)  ⇒ Boolean 
  

  

  

  
    

Check if method is actually an association in a Model

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

237
238
239
240
241
242
243
244
245
246
247
248
249
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 237

def association? model_name, meth
  if call? model_name
    return association? model_name.target, meth
  elsif model_name? model_name
    model = tracker.models[class_name(model_name)]
  else
    return false
  end

  return false unless model

  model.association? meth
end
```

    
  

    
      
  
### 
  
    #**call_has_param**(arg, key)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 142

def call_has_param arg, key
  if call? arg and call? arg.target
    target = arg.target
    method = target.method

    node_type? target.target, :params and method == key
  else
    false
  end
end
```

    
  

    
      
  
### 
  
    #**check_url_for**(call)  ⇒ Object 
  

  

  

  
    

`url_for` is only_path => true by default. This checks to see if it is set to false for some reason.

  

  

  
    
      

```

183
184
185
186
187
188
189
190
191
192
193
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 183

def check_url_for call
  arg = call.first_arg

  if hash? arg
    if value = hash_access(arg, :only_path)
      return false if false?(value)
    end
  end

  true
end
```

    
  

    
      
  
### 
  
    #**decorated_model?**(exp)  ⇒ Boolean 
  

  

  

  
    

Returns true if exp is (probably) a decorated model instance using the Draper gem

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

224
225
226
227
228
229
230
231
232
233
234
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 224

def decorated_model? exp
  if node_type? exp, :or
    decorated_model? exp.lhs or decorated_model? exp.rhs
  else
    tracker.config.has_gem? :draper and
    call? exp and
    node_type?(exp.target, :const) and
    exp.target.value.to_s.match(/Decorator$/) and
    exp.method == :decorate
  end
end
```

    
  

    
      
  
### 
  
    #**disallow_other_host?**(call)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

287
288
289
290
291
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 287

def disallow_other_host? call
  opt = call.last_arg

  hash? opt and false? hash_access(opt, :allow_other_host)
end
```

    
  

    
      
  
### 
  
    #**explicit_host?**(arg)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

161
162
163
164
165
166
167
168
169
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
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 161

def explicit_host? arg
  return unless sexp? arg

  if hash? arg
    if value = hash_access(arg, :host)
      return !has_immediate_user_input?(value)
    end
  elsif call? arg
    target = arg.target

    if hash? target and value = hash_access(target, :host)
      return !has_immediate_user_input?(value)
    elsif call? arg
      return explicit_host? target
    end
  end

  false
end
```

    
  

    
      
  
### 
  
    #**friendly_model?**(exp)  ⇒ Boolean 
  

  

  

  
    

Returns true if exp is (probably) a friendly model instance using the FriendlyId gem

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

218
219
220
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 218

def friendly_model? exp
  call? exp and model_name? exp.target and exp.method == :friendly
end
```

    
  

    
      
  
### 
  
    #**has_only_path?**(arg)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

153
154
155
156
157
158
159
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 153

def has_only_path? arg
  if value = hash_access(arg, :only_path)
    return true if true?(value)
  end

  false
end
```

    
  

    
      
  
### 
  
    #**include_user_input?**(opt, immediate = :immediate)  ⇒ Boolean 
  

  

  

  
    

Custom check for user input. First looks to see if the user input is being output directly. This is necessary because of tracker.options which can be used to enable/disable reporting output of method calls which use user input as arguments.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 81

def include_user_input? opt, immediate = :immediate
  Brakeman.debug "Checking if call includes user input"

  # if the first argument is an array, rails assumes you are building a
  # polymorphic route, which will never jump off-host
  return false if array? opt

  if tracker.options[:ignore_redirect_to_model]
    if model_instance?(opt) or decorated_model?(opt)
      return false
    end
  end

  if res = has_immediate_model?(opt)
    unless call? opt and opt.method.to_s =~ /_path/
      return Match.new(immediate, res)
    end
  elsif call? opt
    if request_value? opt
      return Match.new(immediate, opt)
    elsif opt.method == :url_for and include_user_input? opt.first_arg
      return Match.new(immediate, opt)
      #Ignore helpers like some_model_url?
    elsif opt.method.to_s =~ /_(url|path)\z/
      return false
    elsif opt.method == :url_from
      return false
    end
  elsif request_value? opt
    return Match.new(immediate, opt)
  elsif node_type? opt, :or
    return (include_user_input?(opt.lhs) or include_user_input?(opt.rhs))
  end

  if tracker.options[:check_arguments] and call? opt
    include_user_input? opt.first_arg, false  #I'm doubting if this is really necessary...
  else
    false
  end
end
```

    
  

    
      
  
### 
  
    #**model_instance?**(exp)  ⇒ Boolean 
  

  

  

  
    

Returns true if exp is (probably) a model instance

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 196

def model_instance? exp
  if node_type? exp, :or
    model_instance? exp.lhs or model_instance? exp.rhs
  elsif call? exp
    if model_target? exp and
      (@model_find_calls.include? exp.method or exp.method.to_s.match(/^find_by_/))
      true
    else
      association?(exp.target, exp.method)
    end
  end
end
```

    
  

    
      
  
### 
  
    #**model_target?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

209
210
211
212
213
214
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 209

def model_target? exp
  return false unless call? exp
  model_name? exp.target or
  friendly_model? exp.target or
  model_target? exp.target
end
```

    
  

    
      
  
### 
  
    #**only_path?**(call)  ⇒ Boolean 
  

  

  

  
    

Checks `redirect_to` arguments for only_path => true which essentially nullifies the danger posed by redirecting with user input

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 124

def only_path? call
  arg = call.first_arg

  if hash? arg
    return has_only_path? arg
  elsif call? arg and arg.method == :url_for
    return check_url_for(arg)
  elsif call? arg and hash? arg.first_arg and use_unsafe_hash_method? arg
    return has_only_path? arg.first_arg
  end

  false
end
```

    
  

    
      
  
### 
  
    #**process_result**(result)  ⇒ Object 
  

  

  

  
    
      

```

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
73
74
75
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 35

def process_result result
  return unless original? result

  call = result[:call]
  opt = call.first_arg

  # Location is specified with `fallback_location:`
  # otherwise the arguments do not contain a location and
  # the call can be ignored
  if call.method == :redirect_back
    if hash? opt and location = hash_access(opt, :fallback_location)
      opt = location
    else
      return
    end
  end

  if not protected_by_raise?(call) and
      not only_path?(call) and
      not explicit_host?(opt) and
      not slice_call?(opt) and
      not safe_permit?(opt) and
      not disallow_other_host?(call) and
      res = include_user_input?(opt)

    if res.type == :immediate and not allow_other_host?(call)
      confidence = :high
    else
      confidence = :weak
    end

    warn :result => result,
      :warning_type => "Redirect",
      :warning_code => :open_redirect,
      :message => "Possible unprotected redirect",
      :code => call,
      :user_input => res,
      :confidence => confidence,
      :cwe_id => [601]
  end
end
```

    
  

    
      
  
### 
  
    #**protected_by_raise?**(call)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

272
273
274
275
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 272

def protected_by_raise? call
  raise_on_redirects? and
    not allow_other_host? call
end
```

    
  

    
      
  
### 
  
    #**raise_on_redirects?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

277
278
279
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 277

def raise_on_redirects?
  @raise_on_redirects ||= true?(tracker.config.rails.dig(:action_controller, :raise_on_open_redirects))
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

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
28
29
30
31
32
33
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 13

def run_check
  @model_find_calls = Set[:all, :create, :create!, :find, :find_by_sql, :first, :first!, :last, :last!, :new, :sole]

  if tracker.options[:rails3]
    @model_find_calls.merge [:from, :group, :having, :joins, :lock, :order, :reorder, :select, :where]
  end

  if version_between? "4.0.0", "9.9.9"
    @model_find_calls.merge [:find_by, :find_by!, :take]
  end

  if version_between? "7.0.0", "9.9.9"
    @model_find_calls << :find_sole_by
  end

  methods = [:redirect_to, :redirect_back, :redirect_back_or_to]

  @tracker.find_call(:target => false, :methods => methods).each do |res|
    process_result res
  end
end
```

    
  

    
      
  
### 
  
    #**safe_permit?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

258
259
260
261
262
263
264
265
266
267
268
269
270
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 258

def safe_permit? exp
  if call? exp and params? exp.target and exp.method == :permit
    exp.each_arg do |opt|
      if symbol? opt and DANGEROUS_KEYS.include? opt.value
        return false
      end
    end

    return true
  end

  false
end
```

    
  

    
      
  
### 
  
    #**slice_call?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

251
252
253
254
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 251

def slice_call? exp
  return unless call? exp
  exp.method == :slice
end
```

    
  

    
      
  
### 
  
    #**use_unsafe_hash_method?**(arg)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

138
139
140
```

    
    
      

```
# File 'lib/brakeman/checks/check_redirect.rb', line 138

def use_unsafe_hash_method? arg
  return call_has_param(arg, :to_unsafe_hash) || call_has_param(arg, :to_unsafe_h)
end
```