# Class: Brakeman::CheckSQLCVEs
  
  
  

  
  
    Inherits:
    
      BaseCheck
      
        

          
- Object
          
            
- SexpProcessor
          
            
- BaseCheck
          
            
- Brakeman::CheckSQLCVEs
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/checks/check_sql_cves.rb
  
  

  
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
  
    
      #**check_cve_2014_0080**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_rails_versions_against_cve_issues**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**cve_warning_for**(versions, cve, link)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run_check**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**upgrade_version?**(versions)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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
  
    #**check_cve_2014_0080**  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/brakeman/checks/check_sql_cves.rb', line 96

def check_cve_2014_0080
  return unless version_between? "4.0.0", "4.0.2" and
                @tracker.config.has_gem? :pg

  warn :warning_type => 'SQL Injection',
    :warning_code => :CVE_2014_0080,
    :message => msg(msg_version(rails_version), " contains a SQL injection vulnerability ", msg_cve("CVE-2014-0080"), " with PostgreSQL. Upgrade to ", msg_version("4.0.3")),
    :confidence => :high,
    :gem_info => gemfile_or_environment(:pg),
    :link_path => "https://groups.google.com/d/msg/rubyonrails-security/Wu96YkTUR6s/pPLBMZrlwvYJ",
    :cwe_id => [89]
end
```

    
  

    
      
  
### 
  
    #**check_rails_versions_against_cve_issues**  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql_cves.rb', line 13

def check_rails_versions_against_cve_issues
  issues = [
    {
      :cve => "CVE-2012-2660",
      :versions => [%w[2.0.0 2.3.14 2.3.17], %w[3.0.0 3.0.12 3.0.13], %w[3.1.0 3.1.4 3.1.5], %w[3.2.0 3.2.3 3.2.4]],
      :url => "https://groups.google.com/d/topic/rubyonrails-security/8SA-M3as7A8/discussion"
    },
    {
      :cve => "CVE-2012-2661",
      :versions => [%w[3.0.0 3.0.12 3.0.13], %w[3.1.0 3.1.4 3.1.5], %w[3.2.0 3.2.3 3.2.5]],
      :url => "https://groups.google.com/d/topic/rubyonrails-security/dUaiOOGWL1k/discussion"
    },
    {
      :cve => "CVE-2012-2695",
      :versions => [%w[2.0.0 2.3.14 2.3.15], %w[3.0.0 3.0.13 3.0.14], %w[3.1.0 3.1.5 3.1.6], %w[3.2.0 3.2.5 3.2.6]],
      :url => "https://groups.google.com/d/topic/rubyonrails-security/l4L0TEVAz1k/discussion"
    },
    {
      :cve => "CVE-2012-5664",
      :versions => [%w[2.0.0 2.3.14 2.3.15], %w[3.0.0 3.0.17 3.0.18], %w[3.1.0 3.1.8 3.1.9], %w[3.2.0 3.2.9 3.2.18]],
      :url => "https://groups.google.com/d/topic/rubyonrails-security/DCNTNp_qjFM/discussion"
    },
    {
      :cve => "CVE-2013-0155",
      :versions => [%w[2.0.0 2.3.15 2.3.16], %w[3.0.0 3.0.18 3.0.19], %w[3.1.0 3.1.9 3.1.10], %w[3.2.0 3.2.10 3.2.11]],
      :url => "https://groups.google.com/d/topic/rubyonrails-security/c7jT-EeN9eI/discussion"
    },
    {
      :cve => "CVE-2016-6317",
      :versions => [%w[4.2.0 4.2.7.0 4.2.7.1]],
      :url => "https://groups.google.com/d/msg/ruby-security-ann/WccgKSKiPZA/9DrsDVSoCgAJ"
    },

  ]

  unless lts_version? '2.3.18.6'
   issues << {
      :cve => "CVE-2013-6417",
      :versions => [%w[2.0.0 3.2.15 3.2.16], %w[4.0.0 4.0.1 4.0.2]],
      :url => "https://groups.google.com/d/msg/ruby-security-ann/niK4drpSHT4/g8JW8ZsayRkJ"
    }
  end

  if tracker.config.has_gem? :pg
    issues << {
      :cve => "CVE-2014-3482",
      :versions => [%w[2.0.0 2.9.9 3.2.19], %w[3.0.0 3.2.18 3.2.19], %w[4.0.0 4.0.6 4.0.7], %w[4.1.0 4.1.2 4.1.3]],
      :url => "https://groups.google.com/d/msg/rubyonrails-security/wDxePLJGZdI/WP7EasCJTA4J"
    } <<
    {
      :cve => "CVE-2014-3483",
      :versions => [%w[2.0.0 2.9.9 3.2.19], %w[3.0.0 3.2.18 3.2.19], %w[4.0.0 4.0.6 4.0.7], %w[4.1.0 4.1.2 4.1.3]],
      :url => "https://groups.google.com/d/msg/rubyonrails-security/wDxePLJGZdI/WP7EasCJTA4J" }
  end

  issues.each do |cve_issue|
    cve_warning_for cve_issue[:versions], cve_issue[:cve], cve_issue[:url]
  end
end
```

    
  

    
      
  
### 
  
    #**cve_warning_for**(versions, cve, link)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql_cves.rb', line 73

def cve_warning_for versions, cve, link
  upgrade_version = upgrade_version? versions
  return unless upgrade_version

  code = cve.tr('-', '_').to_sym

  warn :warning_type => 'SQL Injection',
    :warning_code => code,
    :message => msg(msg_version(rails_version), " contains a SQL injection vulnerability ", msg_cve(cve), ". Upgrade to ", msg_version(upgrade_version)),
    :confidence => :high,
    :gem_info => gemfile_or_environment,
    :link_path => link,
    :cwe_id => [89]
end
```

    
  

    
      
  
### 
  
    #**run_check**  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
11
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql_cves.rb', line 8

def run_check
  check_rails_versions_against_cve_issues
  check_cve_2014_0080
end
```

    
  

    
      
  
### 
  
    #**upgrade_version?**(versions)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

88
89
90
91
92
93
94
```

    
    
      

```
# File 'lib/brakeman/checks/check_sql_cves.rb', line 88

def upgrade_version? versions
  versions.each do |low, high, upgrade|
    return upgrade if version_between? low, high
  end

  false
end
```