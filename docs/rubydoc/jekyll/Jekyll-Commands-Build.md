# Class: Jekyll::Commands::Build
  
    Inherits:
    
      Jekyll::Command
      
        

          
- Object

- Jekyll::Command

- Jekyll::Commands::Build

        show all
      

    Defined in:
    lib/jekyll/commands/build.rb
  
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**build**(site, options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Build your Jekyll site.

-
  
      .**init_with_program**(prog)  ⇒ Object 

Create the Mercenary command for the Jekyll CLI for this Command.

-
  
      .**process**(options)  ⇒ Object 

Build your jekyll site Continuously watch if `watch` is set to true in the config.

-
  
      .**watch**(site, options)  ⇒ Object 

Private: Watch for file changes and rebuild the site.

### Methods inherited from Jekyll::Command

add_build_options, configuration_from_options, inherited, process_site, process_with_graceful_fail, subclasses

## Class Method Details

###
  
    .**build**(site, options)  ⇒ Object 
  

  

  

  
    

Build your Jekyll site.

site - the Jekyll::Site instance to build options - A Hash of options passed to the command

Returns nothing.

```

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
```

```
# File 'lib/jekyll/commands/build.rb', line 55

def build(site, options)
  t = Time.now
  source      = File.expand_path(options["source"])
  destination = File.expand_path(options["destination"])
  incremental = options["incremental"]
  Jekyll.logger.info "Source:", source
  Jekyll.logger.info "Destination:", destination
  Jekyll.logger.info "Incremental build:",
                     (incremental ? "enabled" : "disabled. Enable with --incremental")
  Jekyll.logger.info "Generating..."
  process_site(site)
  Jekyll.logger.info "", "done in #{(Time.now - t).round(3)} seconds."
end
```

###
  
    .**init_with_program**(prog)  ⇒ Object 
  

  

  

  
    

Create the Mercenary command for the Jekyll CLI for this Command

```

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
21
```

```
# File 'lib/jekyll/commands/build.rb', line 8

def init_with_program(prog)
  prog.command(:build) do |c|
    c.syntax      "build [options]"
    c.description "Build your site"
    c.alias :b

    add_build_options(c)

    c.action do |_, options|
      options["serving"] = false
      process_with_graceful_fail(c, options, self)
    end
  end
end
```

###
  
    .**process**(options)  ⇒ Object 
  

  

  

  
    

Build your jekyll site Continuously watch if `watch` is set to true in the config.

```

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
```

```
# File 'lib/jekyll/commands/build.rb', line 25

def process(options)
  # Adjust verbosity quickly
  Jekyll.logger.adjust_verbosity(options)

  options = configuration_from_options(options)
  site = Jekyll::Site.new(options)

  if options.fetch("skip_initial_build", false)
    Jekyll.logger.warn "Build Warning:",
                       "Skipping the initial build. This may result in an out-of-date site."
  else
    build(site, options)
  end

  if options.fetch("detach", false)
    Jekyll.logger.info "Auto-regeneration:",
                       "disabled when running server detached."
  elsif options.fetch("watch", false)
    watch(site, options)
  else
    Jekyll.logger.info "Auto-regeneration:", "disabled. Use --watch to enable."
  end
end
```

###
  
    .**watch**(site, options)  ⇒ Object 
  

  

  

  
    

Private: Watch for file changes and rebuild the site.

site - A Jekyll::Site instance options - A Hash of options passed to the command

Returns nothing.

```

75
76
77
78
```

```
# File 'lib/jekyll/commands/build.rb', line 75

def watch(site, options)
  External.require_with_graceful_fail "jekyll-watch"
  Jekyll::Watcher.watch(options, site)
end
```
