# Class: Jekyll::Commands::Doctor
  
    Inherits:
    
      Jekyll::Command
      
        

          
- Object

- Jekyll::Command

- Jekyll::Commands::Doctor

        show all
      

    Defined in:
    lib/jekyll/commands/doctor.rb
  
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**conflicting_urls**(site)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**deprecated_relative_permalinks**(site)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**fsnotify_buggy?**(_site)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**healthy?**(site)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**init_with_program**(prog)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**process**(options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**proper_site_url?**(site)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**properly_gathered_posts?**(site)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**urls_only_differ_by_case**(site)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods inherited from Jekyll::Command

add_build_options, configuration_from_options, inherited, process_site, process_with_graceful_fail, subclasses

## Class Method Details

###
  
    .**conflicting_urls**(site)  ⇒ Object 
  

  

  

  
    
      

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
```

```
# File 'lib/jekyll/commands/doctor.rb', line 68

def conflicting_urls(site)
  conflicting_urls = false
  destination_map(site).each do |dest, paths|
    next unless paths.size > 1

    conflicting_urls = true
    Jekyll.logger.warn "Conflict:",
                       "The following destination is shared by multiple files."
    Jekyll.logger.warn "", "The written file may end up with unexpected contents."
    Jekyll.logger.warn "", dest.to_s.cyan
    paths.each { |path| Jekyll.logger.warn "", " - #{path}" }
    Jekyll.logger.warn ""
  end
  conflicting_urls
end

```

###
  
    .**deprecated_relative_permalinks**(site)  ⇒ Object 
  

  

  

  
    
      

```

60
61
62
63
64
65
66
```

```
# File 'lib/jekyll/commands/doctor.rb', line 60

def deprecated_relative_permalinks(site)
  if site.config["relative_permalinks"]
    Jekyll::Deprecator.deprecation_message "Your site still uses relative permalinks, " \
                                           "which was removed in Jekyll v3.0.0."
    true
  end
end

```

###
  
    .**fsnotify_buggy?**(_site)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

```

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
```

```
# File 'lib/jekyll/commands/doctor.rb', line 84

def fsnotify_buggy?(_site)
  return true unless Utils::Platforms.osx?

  if Dir.pwd != `pwd`.strip
    Jekyll.logger.error "      We have detected that there might be trouble using fsevent on your\n      operating system, you can read https://github.com/thibaudgg/rb-fsevent/wiki/no-fsevents-fired-(OSX-bug)\n      for possible workarounds or you can work around it immediately\n      with `--force-polling`.\n    STR\n\n    false\n  end\n\n  true\nend\n"

```

###
  
    .**healthy?**(site)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

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
```

```
# File 'lib/jekyll/commands/doctor.rb', line 35

def healthy?(site)
  [
    fsnotify_buggy?(site),
    !deprecated_relative_permalinks(site),
    !conflicting_urls(site),
    !urls_only_differ_by_case(site),
    proper_site_url?(site),
    properly_gathered_posts?(site),
  ].all?
end

```

###
  
    .**init_with_program**(prog)  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
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
```

```
# File 'lib/jekyll/commands/doctor.rb', line 7

def init_with_program(prog)
  prog.command(:doctor) do |c|
    c.syntax "doctor"
    c.description "Search site and print specific deprecation warnings"
    c.alias(:hyde)

    c.option "config", "--config CONFIG_FILE[,CONFIG_FILE2,...]", Array,
             "Custom configuration file"

    c.action do |_, options|
      Jekyll::Commands::Doctor.process(options)
    end
  end
end

```

###
  
    .**process**(options)  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/jekyll/commands/doctor.rb', line 22

def process(options)
  site = Jekyll::Site.new(configuration_from_options(options))
  site.reset
  site.read
  site.generate

  if healthy?(site)
    Jekyll.logger.info "Your test results", "are in. Everything looks fine."
  else
    abort
  end
end

```

###
  
    .**proper_site_url?**(site)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

```

115
116
117
118
119
120
121
122
```

```
# File 'lib/jekyll/commands/doctor.rb', line 115

def proper_site_url?(site)
  url = site.config["url"]
  [
    url_exists?(url),
    url_valid?(url),
    url_absolute(url),
  ].all?
end

```

###
  
    .**properly_gathered_posts?**(site)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

```

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
# File 'lib/jekyll/commands/doctor.rb', line 46

def properly_gathered_posts?(site)
  return true if site.config["collections_dir"].empty?

  posts_at_root = site.in_source_dir("_posts")
  return true unless File.directory?(posts_at_root)

  Jekyll.logger.warn "Warning:",
                     "Detected '_posts' directory outside custom `collections_dir`!"
  Jekyll.logger.warn "",
                     "Please move '#{posts_at_root}' into the custom directory at " \
                     "'#{site.in_source_dir(site.config["collections_dir"])}'"
  false
end

```

###
  
    .**urls_only_differ_by_case**(site)  ⇒ Object 
  

  

  

  
    
      

```

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
```

```
# File 'lib/jekyll/commands/doctor.rb', line 101

def urls_only_differ_by_case(site)
  urls_only_differ_by_case = false
  urls = case_insensitive_urls(site.pages + site.docs_to_write, site.dest)
  urls.each_value do |real_urls|
    next unless real_urls.uniq.size > 1

    urls_only_differ_by_case = true
    Jekyll.logger.warn "Warning:", "The following URLs only differ by case. On a " \
                                   "case-insensitive file system one of the URLs will be " \
                                   "overwritten by the other: #{real_urls.join(", ")}"
  end
  urls_only_differ_by_case
end

```
