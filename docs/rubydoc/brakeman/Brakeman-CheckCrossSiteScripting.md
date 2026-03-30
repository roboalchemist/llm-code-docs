# Class: Brakeman::CheckCrossSiteScripting
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckCrossSiteScripting
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_cross_site_scripting.rb
  
  

## Overview

  
    

This check looks for unescaped output in templates which contains parameters or model attributes.

For example:

<%= User.find(:id).name %> <%= params %>

  

  

  
## Direct Known Subclasses

  

CheckContentTag, CheckLinkTo, CheckRenderInline, CheckSimpleFormat

  
    
## 
      Constant Summary
      collapse
    

    
      
        IGNORE_MODEL_METHODS =
          
  
    

Model methods which are known to be harmless

  

  

        
        

```
Set[:average, :count, :maximum, :minimum, :sum, :id]
```

      
        MODEL_METHODS =
          
        
        

```
Set[:all, :find, :first, :last, :new]
```

      
        IGNORE_LIKE =
          
        
        

```
/^link_to_|(_path|_tag|_url)$/
```

      
        HAML_HELPERS =
          
        
        

```
Sexp.new(:colon2, Sexp.new(:const, :Haml), :Helpers)
```

      
        XML_HELPER =
          
        
        

```
Sexp.new(:colon2, Sexp.new(:const, :Erubis), :XmlHelper)
```

      
        URI =
          
        
        

```
Sexp.new(:const, :URI)
```

      
        CGI =
          
        
        

```
Sexp.new(:const, :CGI)
```

      
        FORM_BUILDER =
          
        
        

```
Sexp.new(:call, Sexp.new(:const, :FormBuilder), :new)
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
  
    
      #**actually_process_call**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**cgi_escaped?**(target, method)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_for_immediate_xss**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**form_builder_method?**(target, method)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**haml_escaped?**(target, method)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**html_safe_call?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**ignore_call?**(target, method)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**ignored_method?**(target, method)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**ignored_model_method?**(target, method)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(*args)  ⇒ CheckCrossSiteScripting 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of CheckCrossSiteScripting.

  

      
        
- 
  
    
      #**likely_model_attribute?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Call already involves a model, but might not be acting on a record.

  

      
        
- 
  
    
      #**process_call**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Check a call for user input.

  

      
        
- 
  
    
      #**process_case**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_cookies**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Note that cookies have been found.

  

      
        
- 
  
    
      #**process_dstr**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Process as default.

  

      
        
- 
  
    
      #**process_escaped_output**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Look for calls to raw() Otherwise, ignore.

  

      
        
- 
  
    
      #**process_format**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Process as default.

  

      
        
- 
  
    
      #**process_format_escaped**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Ignore output HTML escaped via HAML.

  

      
        
- 
  
    
      #**process_if**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Ignore condition in if Sexp.

  

      
        
- 
  
    
      #**process_output**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Process an output Sexp.

  

      
        
- 
  
    
      #**process_params**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Note that params have been found.

  

      
        
- 
  
    
      #**process_render**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Ignore calls to render.

  

      
        
- 
  
    
      #**raw_call?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Run check.

  

      
        
- 
  
    
      #**safe_input_attribute?**(target, method)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**setup**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**xml_escaped?**(target, method)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from BaseCheck

  

#add_result, description, inherited, #process_array, #process_default

  
  
  
  
  
  
  
  
  
### Methods included from Messages

  

#msg, #msg_code, #msg_cve, #msg_file, #msg_input, #msg_lit, #msg_plain, #msg_version

  
  
  
  
  
  
  
  
  
### Methods included from Util

  

#all_literals?, #array?, #block?, #call?, #camelize, #class_name, #constant?, #contains_class?, #cookies?, #dir_glob?, #false?, #hash?, #hash_access, #hash_insert, #hash_iterate, #hash_values, #integer?, #kwsplat?, #literal?, #make_call, #node_type?, #number?, #params?, #pluralize, #rails_version, #recurse_check?, #regexp?, #remove_kwsplat, #request_headers?, #request_value?, #result?, #safe_literal, #safe_literal?, #safe_literal_target?, #set_env_defaults, #sexp?, #simple_literal?, #string?, #string_interp?, #symbol?, #template_path_to_name, #true?, #underscore

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from ProcessorHelper

  

#current_file, #process_all, #process_all!, #process_call_args, #process_call_defn?, #process_class, #process_module

  
  
  
  
  
  
  
  
  
### Methods inherited from SexpProcessor

  

#in_context, #process, processors, #scope

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(*args)  ⇒ CheckCrossSiteScripting 
  

  

  

  
    

Returns a new instance of CheckCrossSiteScripting.

  

  

  
    
      

```

36
37
38
39
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 36

def initialize *args
  super
  @matched = @mark = false
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**actually_process_call**(exp)  ⇒ Object 
  

  

  

  
    
      

```

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
227
228
229
230
231
232
233
234
235
236
237
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 216

def actually_process_call exp
  return if @matched
  target = exp.target
  if sexp? target
    target = process target
  end

  method = exp.method

  #Ignore safe items
  if ignore_call? target, method
    @matched = false
  elsif sexp? target and model_name? target[1] #TODO: use method call?
    @matched = Match.new(:model, exp)
  elsif cookies? exp
    @matched = Match.new(:cookies, exp)
  elsif @inspect_arguments and params? exp
    @matched = Match.new(:params, exp)
  elsif @inspect_arguments
    process_call_args exp
  end
end
```

    
  

    
      
  
### 
  
    #**cgi_escaped?**(target, method)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

369
370
371
372
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 369

def cgi_escaped? target, method
  method == :escape and
  (target == URI or target == CGI)
end
```

    
  

    
      
  
### 
  
    #**check_for_immediate_xss**(exp)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 60

def check_for_immediate_xss exp
  return :duplicate if duplicate? exp

  if exp.node_type == :output
    out = exp.value
  end

  if raw_call? exp
    out = exp.value.first_arg
  elsif html_safe_call? exp
    out = exp.value.target
  end

  return if call? out and ignore_call? out.target, out.method

  if input = has_immediate_user_input?(out)
    add_result exp

    message = msg("Unescaped ", msg_input(input))

    warn :template => @current_template,
      :warning_type => "Cross-Site Scripting",
      :warning_code => :cross_site_scripting,
      :message => message,
      :code => input.match,
      :confidence => :high,
      :cwe_id => [79]

  elsif not tracker.options[:ignore_model_output] and match = has_immediate_model?(out)
    method = if call? match
               match.method
             else
               nil
             end

    unless IGNORE_MODEL_METHODS.include? method
      add_result exp

      if likely_model_attribute? match
        confidence = :high
      else
        confidence = :medium
      end

      message = "Unescaped model attribute"
      link_path = "cross_site_scripting"
      warning_code = :cross_site_scripting

      if node_type?(out, :call, :safe_call, :attrasgn, :safe_attrasgn) && out.method == :to_json
        message += " in JSON hash"
        link_path += "_to_json"
        warning_code = :xss_to_json
      end

      warn :template => @current_template,
        :warning_type => "Cross-Site Scripting",
        :warning_code => warning_code,
        :message => message,
        :code => match,
        :confidence => confidence,
        :link_path => link_path,
        :cwe_id => [79]
    end

  else
    false
  end
end
```

    
  

    
      
  
### 
  
    #**form_builder_method?**(target, method)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

382
383
384
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 382

def form_builder_method? target, method
  target == FORM_BUILDER and @ignore_methods.include? method
end
```

    
  

    
      
  
### 
  
    #**haml_escaped?**(target, method)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

374
375
376
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 374

def haml_escaped? target, method
  method == :html_escape and target == HAML_HELPERS
end
```

    
  

    
      
  
### 
  
    #**html_safe_call?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

344
345
346
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 344

def html_safe_call? exp
  call? exp.value and exp.value.method == :html_safe
end
```

    
  

    
      
  
### 
  
    #**ignore_call?**(target, method)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

348
349
350
351
352
353
354
355
356
357
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 348

def ignore_call? target, method
  ignored_method?(target, method) or
  safe_input_attribute?(target, method) or
  ignored_model_method?(target, method) or
  form_builder_method?(target, method) or
  haml_escaped?(target, method) or
  boolean_method?(method) or
  cgi_escaped?(target, method) or
  xml_escaped?(target, method)
end
```

    
  

    
      
  
### 
  
    #**ignored_method?**(target, method)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

365
366
367
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 365

def ignored_method? target, method
  @ignore_methods.include? method or method.to_s =~ IGNORE_LIKE
end
```

    
  

    
      
  
### 
  
    #**ignored_model_method?**(target, method)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

359
360
361
362
363
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 359

def ignored_model_method? target, method
  ((@matched and @matched.type == :model) or
     model_name? target) and
     IGNORE_MODEL_METHODS.include? method
end
```

    
  

    
      
  
### 
  
    #**likely_model_attribute?**(exp)  ⇒ Boolean 
  

  

  

  
    

Call already involves a model, but might not be acting on a record

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 130

def likely_model_attribute? exp
  return false unless call? exp

  method = exp.method

  if MODEL_METHODS.include? method or method.to_s.start_with? "find_by_"
    true
  else
    likely_model_attribute? exp.target
  end
end
```

    
  

    
      
  
### 
  
    #**process_call**(exp)  ⇒ Object 
  

  

  

  
    

Check a call for user input

Since we want to report an entire call and not just part of one, use @mark to mark when a call is started. Any dangerous values inside will then report the entire call chain.

  

  

  
    
      

```

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
180
181
182
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
194
195
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
212
213
214
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 168

def process_call exp
  if @mark
    actually_process_call exp
  else
    @mark = true
    actually_process_call exp
    message = nil

    if @matched
      unless @matched.type and tracker.options[:ignore_model_output]
        message = msg("Unescaped ", msg_input(@matched))
      end

      if message and not duplicate? exp
        add_result exp

        link_path = "cross_site_scripting"
        warning_code = :cross_site_scripting

        if @known_dangerous.include? exp.method
          confidence = :high
          if exp.method == :to_json
            message << msg_plain(" in JSON hash")
            link_path += "_to_json"
            warning_code = :xss_to_json
          end
        else
          confidence = :weak
        end

        warn :template => @current_template,
          :warning_type => "Cross-Site Scripting",
          :warning_code => warning_code,
          :message => message,
          :code => exp,
          :user_input => @matched,
          :confidence => confidence,
          :link_path => link_path,
          :cwe_id => [79]
      end
    end

    @mark = @matched = false
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**process_case**(exp)  ⇒ Object 
  

  

  

  
    
      

```

278
279
280
281
282
283
284
285
286
287
288
289
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 278

def process_case exp
  #Ignore user input in case value
  #TODO: also ignore when values

  current = 2
  while current < exp.length
    process exp[current] if exp[current]
    current += 1
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**process_cookies**(exp)  ⇒ Object 
  

  

  

  
    

Note that cookies have been found

  

  

  
    
      

```

246
247
248
249
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 246

def process_cookies exp
  @matched = Match.new(:cookies, exp)
  exp
end
```

    
  

    
      
  
### 
  
    #**process_dstr**(exp)  ⇒ Object 
  

  

  

  
    

Process as default

  

  

  
    
      

```

257
258
259
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 257

def process_dstr exp
  process_default exp
end
```

    
  

    
      
  
### 
  
    #**process_escaped_output**(exp)  ⇒ Object 
  

  

  

  
    

Look for calls to raw() Otherwise, ignore

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 149

def process_escaped_output exp
  unless check_for_immediate_xss exp
    if not duplicate? exp
      if raw_call? exp
        process exp.value.first_arg
      elsif html_safe_call? exp
        process exp.value.target
      end
    end
  end
  exp
end
```

    
  

    
      
  
### 
  
    #**process_format**(exp)  ⇒ Object 
  

  

  

  
    

Process as default

  

  

  
    
      

```

262
263
264
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 262

def process_format exp
  process_default exp
end
```

    
  

    
      
  
### 
  
    #**process_format_escaped**(exp)  ⇒ Object 
  

  

  

  
    

Ignore output HTML escaped via HAML

  

  

  
    
      

```

267
268
269
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 267

def process_format_escaped exp
  exp
end
```

    
  

    
      
  
### 
  
    #**process_if**(exp)  ⇒ Object 
  

  

  

  
    

Ignore condition in if Sexp

  

  

  
    
      

```

272
273
274
275
276
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 272

def process_if exp
  process exp.then_clause if sexp? exp.then_clause
  process exp.else_clause if sexp? exp.else_clause
  exp
end
```

    
  

    
      
  
### 
  
    #**process_output**(exp)  ⇒ Object 
  

  

  

  
    

Process an output Sexp

  

  

  
    
      

```

143
144
145
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 143

def process_output exp
  process exp.value.dup
end
```

    
  

    
      
  
### 
  
    #**process_params**(exp)  ⇒ Object 
  

  

  

  
    

Note that params have been found

  

  

  
    
      

```

240
241
242
243
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 240

def process_params exp
  @matched = Match.new(:params, exp)
  exp
end
```

    
  

    
      
  
### 
  
    #**process_render**(exp)  ⇒ Object 
  

  

  

  
    

Ignore calls to render

  

  

  
    
      

```

252
253
254
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 252

def process_render exp
  exp
end
```

    
  

    
      
  
### 
  
    #**raw_call?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

340
341
342
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 340

def raw_call? exp
  exp.value.node_type == :call and exp.value.method == :raw
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    

Run check

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 42

def run_check
  setup

  tracker.each_template do |name, template|
    Brakeman.debug "Checking #{name} for XSS"

    @current_template = template

    template.each_output do |out|
      unless check_for_immediate_xss out
        @matched = false
        @mark = false
        process out
      end
    end
  end
end
```

    
  

    
      
  
### 
  
    #**safe_input_attribute?**(target, method)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

386
387
388
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 386

def safe_input_attribute? target, method
  target and always_safe_method? method
end
```

    
  

    
      
  
### 
  
    #**setup**  ⇒ Object 
  

  

  

  
    
      

```

291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 291

def setup
  @ignore_methods = Set[:==, :!=, :button_to, :check_box, :content_tag, :escapeHTML, :escape_once,
                         :field_field, :fields_for, :form_for, :h, :hidden_field,
                         :hidden_field, :hidden_field_tag, :image_tag, :label,
                         :link_to, :mail_to, :radio_button, :select,
                         :submit_tag, :text_area, :text_field,
                         :text_field_tag, :url_encode, :u, :url_for,
                         :will_paginate].merge tracker.options[:safe_methods]

  @models = tracker.models.keys
  @inspect_arguments = tracker.options[:check_arguments]

  @known_dangerous = Set[:truncate, :concat]

  if version_between? "2.0.0", "3.0.5"
    @known_dangerous << :auto_link
  elsif version_between? "3.0.6", "3.0.99"
    @ignore_methods << :auto_link
  end

  if version_between? "2.0.0", "2.3.14" or tracker.config.gem_version(:'rails-html-sanitizer') == '1.0.2'
    @known_dangerous << :strip_tags
  end

  if tracker.config.has_gem? :'rails-html-sanitizer' and
     version_between? "1.0.0", "1.0.2", tracker.config.gem_version(:'rails-html-sanitizer')

    @known_dangerous << :sanitize
  end

  json_escape_on = false
  initializers = tracker.find_call(target: :ActiveSupport, method: :escape_html_entities_in_json=)
  initializers.each {|result| json_escape_on = true?(result[:call].first_arg) }

  if tracker.config.escape_html_entities_in_json?
    json_escape_on = true
  elsif version_between? "4.0.0", "9.9.9"
    json_escape_on = true
  end

  if !json_escape_on or version_between? "0.0.0", "2.0.99"
    @known_dangerous << :to_json
    Brakeman.debug("Automatic to_json escaping not enabled, consider to_json dangerous")
  else
    @safe_input_attributes << :to_json
    Brakeman.debug("Automatic to_json escaping is enabled.")
  end
end
```

    
  

    
      
  
### 
  
    #**xml_escaped?**(target, method)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

378
379
380
```

    
    
      

```
# File 'lib/brakeman/checks/check_cross_site_scripting.rb', line 378

def xml_escaped? target, method
  method == :escape_xml and target == XML_HELPER
end
```