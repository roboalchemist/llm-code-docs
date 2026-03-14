# Class: Brakeman::CheckSanitizeMethods
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckSanitizeMethods
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_sanitize_methods.rb
  
  

## Overview

  
    

sanitize and sanitize_css are vulnerable: CVE-2013-1855 and CVE-2013-1857

  

  

  
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
  
    
      #**check_cve_2013_1855**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_cve_2013_1857**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_cve_2018_8048**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_for_cve**(method, code, link)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_rails_html_sanitizer**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**loofah_vulnerable_cve_2018_8048?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**warn_sanitizer_cve**(cve, link, upgrade_version)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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
  
    #**check_cve_2013_1855**  ⇒ Object 
  

  

  

  
    
      

```

34
35
36
```

    
    
      

```
# File 'lib/brakeman/checks/check_sanitize_methods.rb', line 34

def check_cve_2013_1855
  check_for_cve :sanitize_css, :CVE_2013_1855, "https://groups.google.com/d/msg/rubyonrails-security/4_QHo4BqnN8/_RrdfKk12I4J"
end
```

    
  

    
      
  
### 
  
    #**check_cve_2013_1857**  ⇒ Object 
  

  

  

  
    
      

```

38
39
40
```

    
    
      

```
# File 'lib/brakeman/checks/check_sanitize_methods.rb', line 38

def check_cve_2013_1857
  check_for_cve :sanitize, :CVE_2013_1857, "https://groups.google.com/d/msg/rubyonrails-security/zAAU7vGTPvI/1vZDWXqBuXgJ"
end
```

    
  

    
      
  
### 
  
    #**check_cve_2018_8048**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_sanitize_methods.rb', line 72

def check_cve_2018_8048
  if loofah_vulnerable_cve_2018_8048?
    message = msg(msg_version(tracker.config.gem_version(:loofah), "loofah gem"), " is vulnerable (CVE-2018-8048). Upgrade to 2.2.1")

    if tracker.find_call(:target => false, :method => :sanitize).any?
      confidence = :high
    else
      confidence = :medium
    end

    warn :warning_type => "Cross-Site Scripting",
      :warning_code => :CVE_2018_8048,
      :message => message,
      :gem_info => gemfile_or_environment(:loofah),
      :confidence => confidence,
      :link_path => "https://github.com/flavorjones/loofah/issues/144",
      :cwe_id => [79]
  end
end
```

    
  

    
      
  
### 
  
    #**check_for_cve**(method, code, link)  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_sanitize_methods.rb', line 42

def check_for_cve method, code, link
  tracker.find_call(:target => false, :method => method).each do |result|
    next if duplicate? result
    add_result result

    message = msg(msg_version(rails_version), " has a vulnerability in ", msg_code(method), ". Upgrade to ", msg_version(@fix_version), " or patch")

    warn :result => result,
      :warning_type => "Cross-Site Scripting",
      :warning_code => code,
      :message => message,
      :confidence => :high,
      :link_path => link,
      :cwe_id => [79]
  end
end
```

    
  

    
      
  
### 
  
    #**check_rails_html_sanitizer**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_sanitize_methods.rb', line 59

def check_rails_html_sanitizer
  rhs_version = tracker.config.gem_version(:'rails-html-sanitizer')

  if version_between? "1.0.0", "1.0.2", rhs_version
    warn_sanitizer_cve "CVE-2015-7578", "https://groups.google.com/d/msg/rubyonrails-security/uh--W4TDwmI/JbvSRpdbFQAJ", "1.0.3"
    warn_sanitizer_cve "CVE-2015-7580", "https://groups.google.com/d/msg/rubyonrails-security/uh--W4TDwmI/m_CVZtdbFQAJ", "1.0.3"
  end

  if version_between? "1.0.0", "1.0.3", rhs_version
    warn_sanitizer_cve "CVE-2018-3741", "https://groups.google.com/d/msg/rubyonrails-security/tP7W3kLc5u4/uDy2Br7xBgAJ", "1.0.4"
  end
end
```

    
  

    
      
  
### 
  
    #**loofah_vulnerable_cve_2018_8048?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

92
93
94
95
96
97
```

    
    
      

```
# File 'lib/brakeman/checks/check_sanitize_methods.rb', line 92

def loofah_vulnerable_cve_2018_8048?
  loofah_version = tracker.config.gem_version(:loofah)

  # 2.2.1 is fix version
  loofah_version and version_between?("0.0.0", "2.2.0", loofah_version)
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

10
11
12
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
```

    
    
      

```
# File 'lib/brakeman/checks/check_sanitize_methods.rb', line 10

def run_check
  @fix_version = case
    when version_between?('2.0.0', '2.3.17')
      '2.3.18'
    when version_between?('3.0.0', '3.0.99')
      '3.2.13'
    when version_between?('3.1.0', '3.1.11')
      '3.1.12'
    when version_between?('3.2.0', '3.2.12')
      '3.2.13'
    end

  if @fix_version
    check_cve_2013_1855
    check_cve_2013_1857
  end

  if tracker.config.has_gem? :'rails-html-sanitizer'
    check_rails_html_sanitizer
  end

  check_cve_2018_8048
end
```

    
  

    
      
  
### 
  
    #**warn_sanitizer_cve**(cve, link, upgrade_version)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_sanitize_methods.rb', line 99

def warn_sanitizer_cve cve, link, upgrade_version
  message = msg(msg_version(tracker.config.gem_version(:'rails-html-sanitizer'), "rails-html-sanitizer"), " is vulnerable ", msg_cve(cve), ". Upgrade to ", msg_version(upgrade_version, "rails-html-sanitizer"))

  if tracker.find_call(:target => false, :method => :sanitize).any?
    confidence = :high
  else
    confidence = :medium
  end

  warn :warning_type => "Cross-Site Scripting",
    :warning_code => cve.tr('-', '_').to_sym,
    :message => message,
    :gem_info => gemfile_or_environment(:'rails-html-sanitizer'),
    :confidence => confidence,
    :link_path => link,
    :cwe_id => [79]
end
```