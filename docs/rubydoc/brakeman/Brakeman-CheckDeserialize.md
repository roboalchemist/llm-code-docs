# Class: Brakeman::CheckDeserialize
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckDeserialize
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_deserialize.rb
  
  

  
## Constant Summary

  
  
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
  
    
      #**check_csv**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_deserialize**(result, target, arg = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_marshal**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_methods**(target, *methods)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_oj**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_yaml**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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
  
    #**check_csv**  ⇒ Object 
  

  

  

  
    
      

```

35
36
37
```

    
    
      

```
# File 'lib/brakeman/checks/check_deserialize.rb', line 35

def check_csv
  check_methods :CSV, :load
end
```

    
  

    
      
  
### 
  
    #**check_deserialize**(result, target, arg = nil)  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_deserialize.rb', line 69

def check_deserialize result, target, arg = nil
  return unless original? result

  arg ||= result[:call].first_arg
  method = result[:call].method

  if input = has_immediate_user_input?(arg)
    confidence = :high
  elsif input = include_user_input?(arg)
    confidence = :medium
  elsif target == :Marshal
    confidence = :low
    message = msg("Use of ", msg_code("#{target}.#{method}"), " may be dangerous")
  end

  if confidence
    message ||= msg(msg_code("#{target}.#{method}"), " called with ", msg_input(input))

    warn :result => result,
      :warning_type => "Remote Code Execution",
      :warning_code => :unsafe_deserialize,
      :message => message,
      :user_input => input,
      :confidence => confidence,
      :link_path => "unsafe_deserialization",
      :cwe_id => [502]
  end
end
```

    
  

    
      
  
### 
  
    #**check_marshal**  ⇒ Object 
  

  

  

  
    
      

```

39
40
41
```

    
    
      

```
# File 'lib/brakeman/checks/check_deserialize.rb', line 39

def check_marshal
  check_methods :Marshal, :load, :restore
end
```

    
  

    
      
  
### 
  
    #**check_methods**(target, *methods)  ⇒ Object 
  

  

  

  
    
      

```

63
64
65
66
67
```

    
    
      

```
# File 'lib/brakeman/checks/check_deserialize.rb', line 63

def check_methods target, *methods
  tracker.find_call(:target => target, :methods => methods ).each do |result|
    check_deserialize result, target
  end
end
```

    
  

    
      
  
### 
  
    #**check_oj**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_deserialize.rb', line 43

def check_oj
  check_methods :Oj, :object_load # Always unsafe, regardless of mode

  unsafe_mode = :object
  safe_default = oj_safe_default?

  tracker.find_call(:target => :Oj, :method => :load).each do |result|
    call = result[:call]
    options = call.second_arg

    if options and hash? options and mode = hash_access(options, :mode)
      if symbol? mode and mode.value == unsafe_mode
        check_deserialize result, :Oj
      end
    elsif not safe_default
      check_deserialize result, :Oj
    end
  end
end
```

    
  

    
      
  
### 
  
    #**check_yaml**  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/brakeman/checks/check_deserialize.rb', line 15

def check_yaml
  check_methods :YAML, :load_documents, :load_stream, :parse_documents, :parse_stream

  # Check for safe_yaml gem use with YAML.load(..., safe: true)
  if uses_safe_yaml?
    tracker.find_call(target: :YAML, method: :load).each do |result|
      call = result[:call]
      options = call.second_arg

      if hash? options and true? hash_access(options, :safe)
        next
      else
        check_deserialize result, :YAML
      end
    end
  else
    check_methods :YAML, :load
  end
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
11
12
13
```

    
    
      

```
# File 'lib/brakeman/checks/check_deserialize.rb', line 8

def run_check
  check_yaml
  check_csv
  check_marshal
  check_oj
end
```