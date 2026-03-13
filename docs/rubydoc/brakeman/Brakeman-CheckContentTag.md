# Class: Brakeman::CheckContentTag
  
  
  

  
  
    Inherits:
    
      CheckCrossSiteScripting
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- CheckCrossSiteScripting
          
            
- Brakeman::CheckContentTag
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_content_tag.rb
  
  

## Overview

  
    

Checks for unescaped values in `content_tag`

```
content_tag :tag, body
                   ^-- Unescaped in Rails 2.x

content_tag, :tag, body, attribute => value
                            ^-- Unescaped in all versions

content_tag, :tag, body, attribute => value
                                        ^
                                        |
        Escaped by default, can be explicitly escaped
        or not by passing in (true|false) as fourth argument

```

  

  

  
## Constant Summary

  
  
### Constants inherited
     from CheckCrossSiteScripting

  

Brakeman::CheckCrossSiteScripting::CGI, Brakeman::CheckCrossSiteScripting::FORM_BUILDER, Brakeman::CheckCrossSiteScripting::HAML_HELPERS, Brakeman::CheckCrossSiteScripting::IGNORE_LIKE, Brakeman::CheckCrossSiteScripting::IGNORE_MODEL_METHODS, Brakeman::CheckCrossSiteScripting::MODEL_METHODS, Brakeman::CheckCrossSiteScripting::URI, Brakeman::CheckCrossSiteScripting::XML_HELPER

  
  
  
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
  
    
      #**check_argument**(result, exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_cve_2016_6316**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**cve_2016_6316?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_call**(exp)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_result**(result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**raw?**(exp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from CheckCrossSiteScripting

  

#actually_process_call, #cgi_escaped?, #check_for_immediate_xss, #form_builder_method?, #haml_escaped?, #html_safe_call?, #ignore_call?, #ignored_method?, #ignored_model_method?, #initialize, #likely_model_attribute?, #process_case, #process_cookies, #process_dstr, #process_escaped_output, #process_format, #process_format_escaped, #process_if, #process_output, #process_params, #process_render, #raw_call?, #safe_input_attribute?, #setup, #xml_escaped?

  
  
  
  
  
  
  
  
  
### Methods inherited from BaseCheck

  

#add_result, description, inherited, #initialize, #process_array, #process_cookies, #process_default, #process_dstr, #process_if, #process_params

  
  
  
  
  
  
  
  
  
### Methods included from Messages

  

#msg, #msg_code, #msg_cve, #msg_file, #msg_input, #msg_lit, #msg_plain, #msg_version

  
  
  
  
  
  
  
  
  
### Methods included from Util

  

#all_literals?, #array?, #block?, #call?, #camelize, #class_name, #constant?, #contains_class?, #cookies?, #dir_glob?, #false?, #hash?, #hash_access, #hash_insert, #hash_iterate, #hash_values, #integer?, #kwsplat?, #literal?, #make_call, #node_type?, #number?, #params?, #pluralize, #rails_version, #recurse_check?, #regexp?, #remove_kwsplat, #request_headers?, #request_value?, #result?, #safe_literal, #safe_literal?, #safe_literal_target?, #set_env_defaults, #sexp?, #simple_literal?, #string?, #string_interp?, #symbol?, #template_path_to_name, #true?, #underscore

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from ProcessorHelper

  

#current_file, #process_all, #process_all!, #process_call_args, #process_call_defn?, #process_class, #process_module

  
  
  
  
  
  
  
  
  
### Methods inherited from SexpProcessor

  

#in_context, #initialize, #process, processors, #scope

  
## Constructor Details

  
    

This class inherits a constructor from Brakeman::CheckCrossSiteScripting
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**check_argument**(result, exp)  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_content_tag.rb', line 104

def check_argument result, exp
  #Check contents of raw() calls directly
  if raw? exp
    arg = process exp.first_arg
  else
    arg = process exp
  end

  if input = has_immediate_user_input?(arg)
    message = msg("Unescaped ", msg_input(input), " in ", msg_code("content_tag"))

    add_result result

    warn :result => result,
      :warning_type => "Cross-Site Scripting",
      :warning_code => :xss_content_tag,
      :message => message,
      :user_input => input,
      :confidence => :high,
      :link_path => "content_tag",
      :cwe_id => [79]

  elsif not tracker.options[:ignore_model_output] and match = has_immediate_model?(arg)
    unless IGNORE_MODEL_METHODS.include? match.method
      add_result result

      if likely_model_attribute? match
        confidence = :high
      else
        confidence = :medium
      end

      warn :result => result,
        :warning_type => "Cross-Site Scripting",
        :warning_code => :xss_content_tag,
        :message => msg("Unescaped model attribute in ", msg_code("content_tag")),
        :user_input => match,
        :confidence => confidence,
        :link_path => "content_tag",
        :cwe_id => [79]
    end

  elsif @matched
    return if @matched.type == :model and tracker.options[:ignore_model_output]

    message = msg("Unescaped ", msg_input(@matched), " in ", msg_code("content_tag"))

    add_result result

    warn :result => result,
      :warning_type => "Cross-Site Scripting",
      :warning_code => :xss_content_tag,
      :message => message,
      :user_input => @matched,
      :confidence => :medium,
      :link_path => "content_tag",
      :cwe_id => [79]
  end
end
```

    
  

    
      
  
### 
  
    #**check_cve_2016_6316**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_content_tag.rb', line 176

def check_cve_2016_6316
  if cve_2016_6316?
    confidence = if @content_tags.any?
                   :high
                 else
                   :medium
                 end

    fix_version = case
                  when version_between?("3.0.0", "3.2.22.3")
                    "3.2.22.4"
                  when version_between?("4.0.0", "4.2.7.0")
                    "4.2.7.1"
                  when version_between?("5.0.0", "5.0.0")
                    "5.0.0.1"
                  when (version.nil? and tracker.options[:rails3])
                    "3.2.22.4"
                  when (version.nil? and tracker.options[:rails4])
                    "4.2.7.2"
                  else
                    return
                  end

    warn :warning_type => "Cross-Site Scripting",
      :warning_code => :CVE_2016_6316,
      :message => msg(msg_version(rails_version), " ", msg_code("content_tag"), " does not escape double quotes in attribute values ", msg_cve("CVE-2016-6316"), ". Upgrade to ", msg_version(fix_version)),
      :confidence => confidence,
      :gem_info => gemfile_or_environment,
      :link_path => "https://groups.google.com/d/msg/ruby-security-ann/8B2iV2tPRSE/JkjCJkSoCgAJ",
      :cwe_id => [79]
  end
end
```

    
  

    
      
  
### 
  
    #**cve_2016_6316?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

213
214
215
216
217
```

    
    
      

```
# File 'lib/brakeman/checks/check_content_tag.rb', line 213

def cve_2016_6316?
  version_between? "3.0.0", "3.2.22.3" or
  version_between? "4.0.0", "4.2.7.0" or
  version_between? "5.0.0", "5.0.0.0"
end
```

    
  

    
      
  
### 
  
    #**process_call**(exp)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_content_tag.rb', line 164

def process_call exp
  if @mark
    actually_process_call exp
  else
    @mark = true
    actually_process_call exp
    @mark = false
  end

  exp
end
```

    
  

    
      
  
### 
  
    #**process_result**(result)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_content_tag.rb', line 45

def process_result result
  return if duplicate? result

  case result[:location][:type]
  when :template
    @current_template = result[:location][:template]
  when :class
    @current_class = result[:location][:class]
    @current_method = result[:location][:method]
  end

  @current_file = result[:location][:file]

  call = result[:call]
  args = call.arglist

  tag_name = args[1]
  content = args[2]
  attributes = args[3]
  escape_attr = args[4]

  @matched = false

  #Silly, but still dangerous if someone uses user input in the tag type
  check_argument result, tag_name

  #Versions before 3.x do not escape body of tag, nor does the rails_xss gem
  unless @matched or (tracker.options[:rails3] and not raw? content)
    check_argument result, content
  end

  # This changed in Rails 6.1.6
  if version_between? '0.0.0', '6.1.5' 
    #Attribute keys are never escaped, so check them for user input
    if not @matched and hash? attributes and not request_value? attributes
      hash_iterate(attributes) do |k, _v|
        check_argument result, k
        return if @matched
      end
    end
  end

  #By default, content_tag escapes attribute values passed in as a hash.
  #But this behavior can be disabled. So only check attributes hash
  #if they are explicitly not escaped.
  if not @matched and attributes and (false? escape_attr or cve_2016_6316?)
    if request_value? attributes or not hash? attributes
      check_argument result, attributes
    else #check hash values
      hash_iterate(attributes) do |_k, v|
        check_argument result, v
        return if @matched
      end
    end
  end
ensure
  @current_template = @current_class = @current_method = @current_file = nil
end
```

    
  

    
      
  
### 
  
    #**raw?**(exp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

209
210
211
```

    
    
      

```
# File 'lib/brakeman/checks/check_content_tag.rb', line 209

def raw? exp
  call? exp and exp.method == :raw
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_content_tag.rb', line 21

def run_check
  @ignore_methods = Set[:button_to, :check_box, :escapeHTML, :escape_once,
                         :field_field, :fields_for, :h, :hidden_field,
                         :hidden_field, :hidden_field_tag, :image_tag, :label,
                         :mail_to, :radio_button, :select,
                         :submit_tag, :text_area, :text_field,
                         :text_field_tag, :url_encode, :u, :url_for,
                         :will_paginate].merge tracker.options[:safe_methods]

  @known_dangerous = []
  @content_tags = tracker.find_call :target => false, :method => :content_tag

  @models = tracker.models.keys
  @inspect_arguments = tracker.options[:check_arguments]
  @mark = nil

  Brakeman.debug "Checking for XSS in content_tag"
  @content_tags.each do |call|
    process_result call
  end

  check_cve_2016_6316
end
```