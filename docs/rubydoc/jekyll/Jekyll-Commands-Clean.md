# Class: Jekyll::Commands::Clean
  
    Inherits:
    
      Jekyll::Command
      
        

          
- Object

- Jekyll::Command

- Jekyll::Commands::Clean

        show all
      

    Defined in:
    lib/jekyll/commands/clean.rb
  
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**init_with_program**(prog)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**process**(options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**remove**(filename, checker_func: :file?)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods inherited from Jekyll::Command

add_build_options, configuration_from_options, inherited, process_site, process_with_graceful_fail, subclasses

## Class Method Details

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
```

```
# File 'lib/jekyll/commands/clean.rb', line 7

def init_with_program(prog)
  prog.command(:clean) do |c|
    c.syntax "clean [subcommand]"
    c.description "Clean the site (removes site output and metadata file) without building."

    add_build_options(c)

    c.action do |_, options|
      Jekyll::Commands::Clean.process(options)
    end
  end
end

```

###
  
    .**process**(options)  ⇒ Object 
  

  

  

  
    
      

```

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
```

```
# File 'lib/jekyll/commands/clean.rb', line 20

def process(options)
  options = configuration_from_options(options)
  destination = options["destination"]
  metadata_file = File.join(options["source"], ".jekyll-metadata")
  cache_dir = File.join(options["source"], options["cache_dir"])
  sass_cache = ".sass-cache"

  remove(destination, :checker_func => :directory?)
  remove(metadata_file, :checker_func => :file?)
  remove(cache_dir, :checker_func => :directory?)
  remove(sass_cache, :checker_func => :directory?)
end

```

###
  
    .**remove**(filename, checker_func: :file?)  ⇒ Object 
  

  

  

  
    
      

```

33
34
35
36
37
38
39
40
```

```
# File 'lib/jekyll/commands/clean.rb', line 33

def remove(filename, checker_func: :file?)
  if File.public_send(checker_func, filename)
    Jekyll.logger.info "Cleaner:", "Removing #{filename}..."
    FileUtils.rm_rf(filename)
  else
    Jekyll.logger.info "Cleaner:", "Nothing to do for #{filename}."
  end
end

```
