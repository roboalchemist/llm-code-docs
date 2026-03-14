# Class: Jekyll::Command
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::Command

        show all
      

    Defined in:
    lib/jekyll/command.rb
  
## Direct Known Subclasses

Jekyll::Commands::Build, Jekyll::Commands::Clean, Jekyll::Commands::Doctor, Jekyll::Commands::Help, Jekyll::Commands::New, Jekyll::Commands::NewTheme, Jekyll::Commands::Serve

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**add_build_options**(cmd)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Add common options to a command for building configuration.

-
  
      .**configuration_from_options**(options)  ⇒ Object 

Create a full Jekyll configuration with the options passed in as overrides.

-
  
      .**inherited**(base)  ⇒ Object 

Keep a list of subclasses of Jekyll::Command every time it’s inherited Called automatically.

-
  
      .**process_site**(site)  ⇒ Object 

Run Site#process and catch errors.

-
  
      .**process_with_graceful_fail**(cmd, options, *klass)  ⇒ Object 

Run ::process method in a given set of Jekyll::Command subclasses and suggest re-running the associated command with –trace switch to obtain any additional information or backtrace regarding the encountered Exception.

-
  
      .**subclasses**  ⇒ Object 

A list of subclasses of Jekyll::Command.

## Class Method Details

###
  
    .**add_build_options**(cmd)  ⇒ Object 
  

  

  

  
    

Add common options to a command for building configuration

cmd - the Jekyll::Command to add these options to

Returns nothing rubocop:disable Metrics/MethodLength

```

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
```

```
# File 'lib/jekyll/command.rb', line 53

def add_build_options(cmd)
  cmd.option "config", "--config CONFIG_FILE[,CONFIG_FILE2,...]",
             Array, "Custom configuration file"
  cmd.option "destination", "-d", "--destination DESTINATION",
             "The current folder will be generated into DESTINATION"
  cmd.option "source", "-s", "--source SOURCE", "Custom source directory"
  cmd.option "future", "--future", "Publishes posts with a future date"
  cmd.option "limit_posts", "--limit_posts MAX_POSTS", Integer,
             "Limits the number of posts to parse and publish"
  cmd.option "watch", "-w", "--[no-]watch", "Watch for changes and rebuild"
  cmd.option "baseurl", "-b", "--baseurl URL",
             "Serve the website from the given base URL"
  cmd.option "force_polling", "--force_polling", "Force watch to use polling"
  cmd.option "lsi", "--lsi", "Use LSI for improved related posts"
  cmd.option "show_drafts", "-D", "--drafts", "Render posts in the _drafts folder"
  cmd.option "unpublished", "--unpublished",
             "Render posts that were marked as unpublished"
  cmd.option "disable_disk_cache", "--disable-disk-cache",
             "Disable caching to disk in non-safe mode"
  cmd.option "quiet", "-q", "--quiet", "Silence output."
  cmd.option "verbose", "-V", "--verbose", "Print verbose output."
  cmd.option "incremental", "-I", "--incremental", "Enable incremental rebuild."
  cmd.option "strict_front_matter", "--strict_front_matter",
             "Fail if errors are present in front matter"
end
```

###
  
    .**configuration_from_options**(options)  ⇒ Object 
  

  

  

  
    

Create a full Jekyll configuration with the options passed in as overrides

options - the configuration overrides

Returns a full Jekyll configuration

```

41
42
43
44
45
```

```
# File 'lib/jekyll/command.rb', line 41

def configuration_from_options(options)
  return options if options.is_a?(Jekyll::Configuration)

  Jekyll.configuration(options)
end
```

###
  
    .**inherited**(base)  ⇒ Object 
  

  

  

  
    

Keep a list of subclasses of Jekyll::Command every time it’s inherited Called automatically.

base - the subclass

Returns nothing

```

17
18
19
20
```

```
# File 'lib/jekyll/command.rb', line 17

def inherited(base)
  subclasses << base
  super(base)
end
```

###
  
    .**process_site**(site)  ⇒ Object 
  

  

  

  
    

Run Site#process and catch errors

site - the Jekyll::Site object

Returns nothing

```

27
28
29
30
31
32
33
34
```

```
# File 'lib/jekyll/command.rb', line 27

def process_site(site)
  site.process
rescue Jekyll::Errors::FatalException => e
  Jekyll.logger.error "ERROR:", "YOUR SITE COULD NOT BE BUILT:"
  Jekyll.logger.error "", "------------------------------------"
  Jekyll.logger.error "", e.message
  exit(1)
end
```

###
  
    .**process_with_graceful_fail**(cmd, options, *klass)  ⇒ Object 
  

  

  

  
    

Run ::process method in a given set of Jekyll::Command subclasses and suggest re-running the associated command with –trace switch to obtain any additional information or backtrace regarding the encountered Exception.

cmd     - the Jekyll::Command to be handled options - configuration overrides klass   - an array of Jekyll::Command subclasses associated with the command

Note that all exceptions are rescued.. rubocop: disable Lint/RescueException

```

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
```

```
# File 'lib/jekyll/command.rb', line 90

def process_with_graceful_fail(cmd, options, *klass)
  klass.each { |k| k.process(options) if k.respond_to?(:process) }
rescue Exception => e
  raise e if cmd.trace

  msg = " Please append `--trace` to the `#{cmd.name}` command "
  dashes = "-" * msg.length
  Jekyll.logger.error "", dashes
  Jekyll.logger.error "Jekyll #{Jekyll::VERSION} ", msg
  Jekyll.logger.error "", " for any additional information or backtrace. "
  Jekyll.logger.abort_with "", dashes
end
```

###
  
    .**subclasses**  ⇒ Object 
  

  

  

  
    

A list of subclasses of Jekyll::Command

```

7
8
9
```

```
# File 'lib/jekyll/command.rb', line 7

def subclasses
  @subclasses ||= []
end
```
