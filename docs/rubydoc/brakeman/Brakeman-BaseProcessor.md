# Class: Brakeman::BaseProcessor
  
  
  

  
  
    Inherits:
    
      SexpProcessor
      
        

          
- Object
          
            
- SexpProcessor
          
            
- Brakeman::BaseProcessor
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      ProcessorHelper, SafeCallHelper, Util
  
  
  

  

  
  
    Defined in:
    lib/brakeman/processors/base_processor.rb
  
  

## Overview

  
    

Base processor for most processors.

  

  

  
## Direct Known Subclasses

  

ControllerProcessor, FileTypeDetector, LibraryProcessor, ModelProcessor, TemplateProcessor

  
    
## 
      Constant Summary
      collapse
    

    
      
        IGNORE =
          
        
        

```
Sexp.new(:ignore).line(0)
```

      
    
  

  
  
  
### Constants included
     from Util

  

Util::ALL_COOKIES, Util::ALL_PARAMETERS, Util::COOKIES, Util::COOKIES_SEXP, Util::DIR_CONST, Util::LITERALS, Util::PARAMETERS, Util::PARAMS_SEXP, Util::PATH_PARAMETERS, Util::QUERY_PARAMETERS, Util::REQUEST_COOKIES, Util::REQUEST_ENV, Util::REQUEST_PARAMETERS, Util::REQUEST_PARAMS, Util::REQUEST_REQUEST_PARAMETERS, Util::SAFE_LITERAL, Util::SESSION, Util::SESSION_SEXP, Util::SIMPLE_LITERALS

  
  
  
### Constants inherited
     from SexpProcessor

  

SexpProcessor::VERSION

  
## Instance Attribute Summary

  
  
### Attributes inherited from SexpProcessor

  

#context, #env, #expected

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**find_render_type**(call, in_view = false)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Determines the type of a call to render.

  

      
        
- 
  
    
      #**ignore**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(tracker)  ⇒ BaseProcessor 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Return a new Processor.

  

      
        
- 
  
    
      #**make_inline_render**(value, options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**make_render**(exp, in_view = false)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Generates :render node from call to render.

  

      
        
- 
  
    
      #**make_render_in_view**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convenience method for ‘make_render exp, true`.

  

      
        
- 
  
    
      #**process_arglist**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Processes the values in an argument list.

  

      
        
- 
  
    
      #**process_attrasgn**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Processes an attribute assignment, which can be either x.y = 1 or x = 1.

  

      
        
- 
  
    
      #**process_block**(exp)  ⇒ Object 
    

    
      (also: #process_rlist)
    
  
  
  
  
  
  
  
  

  
    

Processes a block.

  

      
        
- 
  
    
      #**process_cdecl**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_default**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Default processing.

  

      
        
- 
  
    
      #**process_dstr**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

String with interpolation.

  

      
        
- 
  
    
      #**process_evstr**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Processes the inside of an interpolated String.

  

      
        
- 
  
    
      #**process_file**(exp, current_file)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_hash**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Processes a hash.

  

      
        
- 
  
    
      #**process_if**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Process an if statement.

  

      
        
- 
  
    
      #**process_ignore**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Ignore ignore Sexps.

  

      
        
- 
  
    
      #**process_iter**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Processes calls with blocks.

  

      
        
- 
  
    
      #**process_lasgn**(exp)  ⇒ Object 
    

    
      (also: #process_iasgn)
    
  
  
  
  
  
  
  
  

  
    

Processes a local assignment.

  

      
        
- 
  
    
      #**process_scope**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Process a new scope.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Util

  

#all_literals?, #array?, #block?, #call?, #camelize, #class_name, #constant?, #contains_class?, #cookies?, #dir_glob?, #false?, #hash?, #hash_access, #hash_insert, #hash_iterate, #hash_values, #integer?, #kwsplat?, #literal?, #make_call, #node_type?, #number?, #params?, #pluralize, #rails_version, #recurse_check?, #regexp?, #remove_kwsplat, #request_headers?, #request_value?, #result?, #safe_literal, #safe_literal?, #safe_literal_target?, #set_env_defaults, #sexp?, #simple_literal?, #string?, #string_interp?, #symbol?, #template_path_to_name, #true?, #underscore

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from ProcessorHelper

  

#current_file, #process_all, #process_all!, #process_call_args, #process_call_defn?, #process_class, #process_module

  
  
  
  
  
  
  
  
  
### Methods inherited from SexpProcessor

  

#in_context, #process, processors, #scope

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(tracker)  ⇒ BaseProcessor 
  

  

  

  
    

Return a new Processor.

  

  

  
    
      

```

14
15
16
17
18
19
20
```

    
    
      

```
# File 'lib/brakeman/processors/base_processor.rb', line 14

def initialize tracker
  super()
  @last = nil
  @tracker = tracker
  @app_tree = tracker.app_tree if tracker
  @current_template = @current_module = @current_class = @current_method = @current_file = nil
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**find_render_type**(call, in_view = false)  ⇒ Object 
  

  

  

  
    

Determines the type of a call to render.

Possible types are: :action, :default, :file, :inline, :js, :json, :nothing, :partial, :template, :text, :update, :xml

And also :layout for inside templates

  

  

  
    
      

```

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
250
251
252
253
254
255
256
257
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
271
272
273
274
275
276
277
278
279
```

    
    
      

```
# File 'lib/brakeman/processors/base_processor.rb', line 219

def find_render_type call, in_view = false
  rest = Sexp.new(:hash).line(call.line)
  type = nil
  value = nil
  first_arg = call.first_arg

  if call.second_arg.nil? and first_arg == Sexp.new(:lit, :update)
    return :update, nil, Sexp.new(:arglist, *call.args[0..-2]) #TODO HUH?
  end

  #Look for render :action, ... or render "action", ...
  if string? first_arg or symbol? first_arg
    if @current_template and @tracker.options[:rails3]
      type = :partial
      value = first_arg
    else
      type = :action
      value = first_arg
    end
  elsif first_arg.is_a? Symbol or first_arg.is_a? String
    type = :action
    value = Sexp.new(:lit, first_arg.to_sym).line(call.line)
  elsif first_arg.nil?
    type = :default
  elsif not hash? first_arg
    # Maybe do partial if in view?
    type = :action
    value = first_arg
  end

  types_in_hash = Set[:action, :file, :inline, :js, :json, :nothing, :partial, :template, :text, :update, :xml]

  #render :layout => "blah" means something else when in a template
  if in_view
    types_in_hash << :layout
  end

  last_arg = call.last_arg

  #Look for "type" of render in options hash
  #For example, render :file => "blah"
  if hash? last_arg
    hash_iterate(last_arg) do |key, val|
      if symbol? key and types_in_hash.include? key.value
        type = key.value
        value = val
      else  
        rest << key << val
      end
    end
  end

  type ||= :default
  value ||= :default

  if type == :inline and string? value and not hash_access(rest, :type)
    value, rest = make_inline_render(value, rest)
  end

  return type, value, rest
end
```

    
  

    
      
  
### 
  
    #**ignore**  ⇒ Object 
  

  

  

  
    
      

```

27
28
29
```

    
    
      

```
# File 'lib/brakeman/processors/base_processor.rb', line 27

def ignore
  IGNORE
end
```

    
  

    
      
  
### 
  
    #**make_inline_render**(value, options)  ⇒ Object 
  

  

  

  
    
      

```

281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
```

    
    
      

```
# File 'lib/brakeman/processors/base_processor.rb', line 281

def make_inline_render value, options
  require 'brakeman/parsers/template_parser'

  class_or_module = (@current_class || @current_module)

  class_or_module = if class_or_module.nil?
                      "Unknown"
                    else
                      class_or_module.name
                    end

  template_name = "#@current_method/inline@#{value.line}:#{class_or_module}".to_sym
  type, ast = Brakeman::TemplateParser.parse_inline_erb(@tracker, value.value)
  ast = ast.deep_clone(value.line)
  @tracker.processor.process_template(template_name, ast, type, nil, @current_file)
  @tracker.processor.process_template_alias(@tracker.templates[template_name])

  return s(:lit, template_name).line(value.line), options
end
```

    
  

    
      
  
### 
  
    #**make_render**(exp, in_view = false)  ⇒ Object 
  

  

  

  
    

Generates :render node from call to render.

  

  

  
    
      

```

203
204
205
206
207
208
209
210
```

    
    
      

```
# File 'lib/brakeman/processors/base_processor.rb', line 203

def make_render exp, in_view = false 
  render_type, value, rest = find_render_type exp, in_view
  rest = process rest
  result = Sexp.new(:render, render_type, value, rest)
  result.line(exp.line)

  result
end
```

    
  

    
      
  
### 
  
    #**make_render_in_view**(exp)  ⇒ Object 
  

  

  

  
    

Convenience method for ‘make_render exp, true`

  

  

  
    
      

```

198
199
200
```

    
    
      

```
# File 'lib/brakeman/processors/base_processor.rb', line 198

def make_render_in_view exp
  make_render exp, true
end
```

    
  

    
      
  
### 
  
    #**process_arglist**(exp)  ⇒ Object 
  

  

  

  
    

Processes the values in an argument list

  

  

  
    
      

```

145
146
147
148
149
150
151
152
153
```

    
    
      

```
# File 'lib/brakeman/processors/base_processor.rb', line 145

def process_arglist exp
  exp = exp.dup
  exp.shift
  exp.map! do |e|
    process e
  end

  exp.unshift :arglist
end
```

    
  

    
      
  
### 
  
    #**process_attrasgn**(exp)  ⇒ Object 
  

  

  

  
    

Processes an attribute assignment, which can be either x.y = 1 or x = 1

  

  

  
    
      

```

172
173
174
175
176
177
```

    
    
      

```
# File 'lib/brakeman/processors/base_processor.rb', line 172

def process_attrasgn exp
  exp = exp.dup
  exp.target = process exp.target
  exp.arglist = process exp.arglist
  exp
end
```

    
  

    
      
  
### 
  
    #**process_block**(exp)  ⇒ Object 
  

  
    Also known as:
    process_rlist
    
  

  

  
    

Processes a block. Changes Sexp node type to :rlist

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/processors/base_processor.rb', line 106

def process_block exp
  exp = exp.dup
  exp.shift

  exp.map! do |e|
    process e
  end

  exp.unshift :rlist
end
```

    
  

    
      
  
### 
  
    #**process_cdecl**(exp)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/processors/base_processor.rb', line 184

def process_cdecl exp
  if @tracker
    @tracker.add_constant exp.lhs,
      exp.rhs,
      :file => current_file,
      :module => @current_module,
      :class => @current_class,
      :method => @current_method
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**process_default**(exp)  ⇒ Object 
  

  

  

  
    

Default processing.

  

  

  
    
      

```

37
38
39
40
41
42
43
44
45
```

    
    
      

```
# File 'lib/brakeman/processors/base_processor.rb', line 37

def process_default exp
  exp = exp.dup

  exp.each_with_index do |e, i|
    exp[i] = process e if sexp? e and not e.empty?
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**process_dstr**(exp)  ⇒ Object 
  

  

  

  
    

String with interpolation.

  

  

  
    
      

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
95
96
97
98
99
100
101
102
103
```

    
    
      

```
# File 'lib/brakeman/processors/base_processor.rb', line 86

def process_dstr exp
  exp = exp.dup
  exp.shift
  exp.map! do |e|
    if e.is_a? String
      e
    else
      res = process e
      if res.empty?
        nil
      else
        res
      end
    end
  end.compact!

  exp.unshift :dstr
end
```

    
  

    
      
  
### 
  
    #**process_evstr**(exp)  ⇒ Object 
  

  

  

  
    

Processes the inside of an interpolated String.

  

  

  
    
      

```

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
# File 'lib/brakeman/processors/base_processor.rb', line 120

def process_evstr exp
  exp = exp.dup
  if exp[1]
    exp[1] = process exp[1]
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**process_file**(exp, current_file)  ⇒ Object 
  

  

  

  
    
      

```

22
23
24
25
```

    
    
      

```
# File 'lib/brakeman/processors/base_processor.rb', line 22

def process_file exp, current_file
  @current_file = current_file
  process exp
end
```

    
  

    
      
  
### 
  
    #**process_hash**(exp)  ⇒ Object 
  

  

  

  
    

Processes a hash

  

  

  
    
      

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
141
142
```

    
    
      

```
# File 'lib/brakeman/processors/base_processor.rb', line 130

def process_hash exp
  exp = exp.dup
  exp.shift
  exp.map! do |e|
    if sexp? e
      process e
    else
      e
    end
  end

  exp.unshift :hash
end
```

    
  

    
      
  
### 
  
    #**process_if**(exp)  ⇒ Object 
  

  

  

  
    

Process an if statement.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/processors/base_processor.rb', line 48

def process_if exp
  exp = exp.dup
  condition = exp[1] = process exp.condition

  if true? condition
    exp[2] = process exp.then_clause if exp.then_clause
    exp[3] = nil
  elsif false? condition
    exp[2] = nil
    exp[3] = process exp.else_clause if exp.else_clause
  else
    exp[2] = process exp.then_clause if exp.then_clause
    exp[3] = process exp.else_clause if exp.else_clause
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**process_ignore**(exp)  ⇒ Object 
  

  

  

  
    

Ignore ignore Sexps

  

  

  
    
      

```

180
181
182
```

    
    
      

```
# File 'lib/brakeman/processors/base_processor.rb', line 180

def process_ignore exp
  exp
end
```

    
  

    
      
  
### 
  
    #**process_iter**(exp)  ⇒ Object 
  

  

  

  
    

Processes calls with blocks.

s(:iter, CALL, :lasgn|:masgn, BLOCK)

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/processors/base_processor.rb', line 69

def process_iter exp
  exp = exp.dup
  call = process exp.block_call
  #deal with assignments somehow
  if exp.block
    block = process exp.block
    block = nil if block.empty?
  else
    block = nil
  end

  call = Sexp.new(:iter, call, exp.block_args, block).compact
  call.line(exp.line)
  call
end
```

    
  

    
      
  
### 
  
    #**process_lasgn**(exp)  ⇒ Object 
  

  
    Also known as:
    process_iasgn
    
  

  

  
    

Processes a local assignment

  

  

  
    
      

```

156
157
158
159
160
```

    
    
      

```
# File 'lib/brakeman/processors/base_processor.rb', line 156

def process_lasgn exp
  exp = exp.dup
  exp.rhs = process exp.rhs
  exp
end
```

    
  

    
      
  
### 
  
    #**process_scope**(exp)  ⇒ Object 
  

  

  

  
    

Process a new scope. Removes expressions that are set to nil.

  

  

  
    
      

```

32
33
34
```

    
    
      

```
# File 'lib/brakeman/processors/base_processor.rb', line 32

def process_scope exp
  #NOPE?
end
```