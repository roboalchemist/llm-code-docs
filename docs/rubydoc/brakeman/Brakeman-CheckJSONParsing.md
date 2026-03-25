# Class: Brakeman::CheckJSONParsing
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckJSONParsing
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_json_parsing.rb
  
  

  
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
  
    
      #**check_cve_2013_0269**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_cve_2013_0333**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_json_version**(name, version)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(*args)  ⇒ CheckJSONParsing 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of CheckJSONParsing.

  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**uses_gem_backend?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Check for ‘ActiveSupport::JSON.backend = “JSONGem”`.

  

      
        
- 
  
    
      #**uses_json_parse?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**uses_yajl?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Check if `yajl` is included in Gemfile.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from BaseCheck

  

#add_result, description, inherited, #process_array, #process_call, #process_cookies, #process_default, #process_dstr, #process_if, #process_params

  
  
  
  
  
  
  
  
  
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
  
    #**initialize**(*args)  ⇒ CheckJSONParsing 
  

  

  

  
    

Returns a new instance of CheckJSONParsing.

  

  

  
    
      

```

8
9
10
11
```

    
    
      

```
# File 'lib/brakeman/checks/check_json_parsing.rb', line 8

def initialize *args
  super
  @uses_json_parse = nil
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**check_cve_2013_0269**  ⇒ Object 
  

  

  

  
    
      

```

63
64
65
66
67
68
```

    
    
      

```
# File 'lib/brakeman/checks/check_json_parsing.rb', line 63

def check_cve_2013_0269
  [:json, :json_pure].each do |name|
    gem_hash = tracker.config.get_gem name
    check_json_version name, gem_hash[:version] if gem_hash and gem_hash[:version]
  end
end
```

    
  

    
      
  
### 
  
    #**check_cve_2013_0333**  ⇒ Object 
  

  

  

  
    
      

```

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
34
35
36
37
38
39
```

    
    
      

```
# File 'lib/brakeman/checks/check_json_parsing.rb', line 18

def check_cve_2013_0333
  return unless version_between? "0.0.0", "2.3.15" or version_between? "3.0.0", "3.0.19"

  unless uses_yajl? or uses_gem_backend?
    new_version = if version_between? "0.0.0", "2.3.14"
                    "2.3.16"
                  elsif version_between? "3.0.0", "3.0.19"
                    "3.0.20"
                  end

    message = msg(msg_version(rails_version), " has a serious JSON parsing vulnerability. Upgrade to ", msg_version(new_version), " or patch")
    gem_info = gemfile_or_environment

    warn :warning_type => "Remote Code Execution",
      :warning_code => :CVE_2013_0333,
      :message => message,
      :confidence => :high,
      :gem_info => gem_info,
      :link_path => "https://groups.google.com/d/topic/rubyonrails-security/1h2DR63ViGo/discussion",
      :cwe_id => [74] # TODO: is this the best CWE for this?
  end
end
```

    
  

    
      
  
### 
  
    #**check_json_version**(name, version)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_json_parsing.rb', line 70

def check_json_version name, version
  return if version >= "1.7.7" or
            (version >= "1.6.8" and version < "1.7.0") or
            (version >= "1.5.5" and version < "1.6.0")

  warning_type = "Denial of Service"
  confidence = :medium
  gem_name = "#{name} gem"
  message = msg(msg_version(version, gem_name), " has a symbol creation vulnerability. Upgrade to ")

  if version >= "1.7.0"
    confidence = :high
    warning_type = "Remote Code Execution"
    message = msg(msg_version(version, "json gem"), " has a remote code execution vulnerability. Upgrade to ", msg_version("1.7.7", "json gem"))
  elsif version >= "1.6.0"
    message << msg_version("1.6.8", gem_name)
  elsif version >= "1.5.0"
    message << msg_version("1.5.5", gem_name)
  else
    confidence = :weak
    message << msg_version("1.5.5", gem_name)
  end

  if confidence == :medium and uses_json_parse?
    confidence = :high
  end

  warn :warning_type => warning_type,
    :warning_code => :CVE_2013_0269,
    :message => message,
    :confidence => confidence,
    :gem_info => gemfile_or_environment(name),
    :link => "https://groups.google.com/d/topic/rubyonrails-security/4_YvCpLzL58/discussion",
    :cwe_id => [74] # TODO: is this the best CWE for this?
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
16
```

    
    
      

```
# File 'lib/brakeman/checks/check_json_parsing.rb', line 13

def run_check
  check_cve_2013_0333
  check_cve_2013_0269
end
```

    
  

    
      
  
### 
  
    #**uses_gem_backend?**  ⇒ Boolean 
  

  

  

  
    

Check for ‘ActiveSupport::JSON.backend = “JSONGem”`

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

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
# File 'lib/brakeman/checks/check_json_parsing.rb', line 47

def uses_gem_backend?
  matches = tracker.find_call(target: :'ActiveSupport::JSON', method: :backend=, chained: true)

  unless matches.empty?
    json_gem = s(:str, "JSONGem")

    matches.each do |result|
      if result[:call].first_arg == json_gem
        return true
      end
    end
  end

  false
end
```

    
  

    
      
  
### 
  
    #**uses_json_parse?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

106
107
108
109
110
```

    
    
      

```
# File 'lib/brakeman/checks/check_json_parsing.rb', line 106

def uses_json_parse?
  return @uses_json_parse unless @uses_json_parse.nil?

  not tracker.find_call(:target => :JSON, :method => :parse).empty?
end
```

    
  

    
      
  
### 
  
    #**uses_yajl?**  ⇒ Boolean 
  

  

  

  
    

Check if `yajl` is included in Gemfile

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

42
43
44
```

    
    
      

```
# File 'lib/brakeman/checks/check_json_parsing.rb', line 42

def uses_yajl?
  tracker.config.has_gem? :yajl
end
```