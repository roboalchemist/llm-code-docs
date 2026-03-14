# Module: Pod::UserInterface::ErrorReport
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/user_interface/error_report.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**markdown_podfile**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**plugins_string**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**report**(exception)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**report_instructions**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**search_for_exceptions**(exception)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**stack**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**markdown_podfile**  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/cocoapods/user_interface/error_report.rb', line 104

def markdown_podfile
  return '' unless Config.instance.podfile_path && Config.instance.podfile_path.exist?
  "\n### Podfile\n\n```ruby\n\#{Config.instance.podfile_path.read.strip}\n```\n"
end

```

    
  

    
      
  
### 
  
    .**plugins_string**  ⇒ Object 
  

  

  

  
    
      

```

96
97
98
99
100
101
102
```

    
    
      

```
# File 'lib/cocoapods/user_interface/error_report.rb', line 96

def plugins_string
  plugins = installed_plugins
  max_name_length = plugins.keys.map(&:length).max
  plugins.map do |name, version|
    "#{name.ljust(max_name_length)} : #{version}"
  end.sort.join("\n")
end

```

    
  

    
      
  
### 
  
    .**report**(exception)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/cocoapods/user_interface/error_report.rb', line 11

def report(exception)
  "\n\#{'\u2015\u2015\u2015 MARKDOWN TEMPLATE \u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015'.reversed}\n\n### Command\n\n```\n\#{original_command}\n```\n\n\#{report_instructions}\n\n\#{stack}\n### Plugins\n\n```\n\#{plugins_string}\n```\n\#{markdown_podfile}\n### Error\n\n```\n\#{exception.class} - \#{exception.message.force_encoding('UTF-8')}\n\#{exception.backtrace.join(\"\\n\") if exception.backtrace}\n```\n\n\#{'\u2015\u2015\u2015 TEMPLATE END \u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015'.reversed}\n\n\#{'[!] Oh no, an error occurred.'.red}\n\#{error_from_podfile(exception)}\n\#{'Search for existing GitHub issues similar to yours:'.yellow}\n\#{issues_url(exception)}\n\n\#{'If none exists, create a ticket, with the template displayed above, on:'.yellow}\nhttps://github.com/CocoaPods/CocoaPods/issues/new\n\n\#{'Be sure to first read the contributing guide for details on how to properly submit a ticket:'.yellow}\nhttps://github.com/CocoaPods/CocoaPods/blob/master/CONTRIBUTING.md\n\nDon't forget to anonymize any private data!\n\n"
end

```

    
  

    
      
  
### 
  
    .**report_instructions**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/cocoapods/user_interface/error_report.rb', line 56

def report_instructions
  "### Report\n\n* What did you do?\n\n* What did you expect to happen?\n\n* What happened instead?\n"
end

```

    
  

    
      
  
### 
  
    .**search_for_exceptions**(exception)  ⇒ Object 
  

  

  

  
    
      

```

116
117
118
119
120
121
122
123
```

    
    
      

```
# File 'lib/cocoapods/user_interface/error_report.rb', line 116

def search_for_exceptions(exception)
  inspector = GhInspector::Inspector.new 'cocoapods', 'cocoapods'
  message_delegate = UserInterface::InspectorReporter.new
  inspector.search_exception exception, message_delegate
rescue => e
  warn "Searching for inspections failed: #{e}"
  nil
end

```

    
  

    
      
  
### 
  
    .**stack**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/cocoapods/user_interface/error_report.rb', line 68

def stack
  parts = {
    'CocoaPods' => Pod::VERSION,
    'Ruby' => RUBY_DESCRIPTION,
    'RubyGems' => Gem::VERSION,
    'Host' => host_information,
    'Xcode' => xcode_information,
    'Git' => git_information,
    'Ruby lib dir' => RbConfig::CONFIG['libdir'],
    'Repositories' => repo_information,
  }
  justification = parts.keys.map(&:size).max

  str = "### Stack\n\n```\n"
  parts.each do |name, value|
    str << name.rjust(justification)
    str << ' : '
    str << Array(value).join("\n" << (' ' * (justification + 3)))
    str << "\n"
  end

  str << "```\n"
end

```