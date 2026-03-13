# Class: Jekyll::Commands::NewTheme
  
    Inherits:
    
      Jekyll::Command
      
        

          
- Object

- Jekyll::Command

- Jekyll::Commands::NewTheme

        show all
      

    Defined in:
    lib/jekyll/commands/new_theme.rb
  
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**init_with_program**(prog)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**process**(args, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods inherited from Jekyll::Command

add_build_options, configuration_from_options, inherited, process_site, process_with_graceful_fail, subclasses

## Class Method Details

###
  
    .**init_with_program**(prog)  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/jekyll/commands/new_theme.rb', line 9

def init_with_program(prog)
  prog.command(:"new-theme") do |c|
    c.syntax "new-theme NAME"
    c.description "Creates a new Jekyll theme scaffold"
    c.option "code_of_conduct", "-c", "--code-of-conduct",
             "Include a Code of Conduct. (defaults to false)"

    c.action do |args, opts|
      Jekyll::Commands::NewTheme.process(args, opts)
    end
  end
end

```

###
  
    .**process**(args, opts)  ⇒ Object 
  

  

  

  
    
      

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
34
35
```

```
# File 'lib/jekyll/commands/new_theme.rb', line 22

def process(args, opts)
  if !args || args.empty?
    raise Jekyll::Errors::InvalidThemeName, "You must specify a theme name."
  end

  new_theme_name = args.join("_")
  theme = Jekyll::ThemeBuilder.new(new_theme_name, opts)
  Jekyll.logger.abort_with "Conflict:", "#{theme.path} already exists." if theme.path.exist?

  theme.create!
  Jekyll.logger.info "Your new Jekyll theme, #{theme.name.cyan}, " \
                     "is ready for you in #{theme.path.to_s.cyan}!"
  Jekyll.logger.info "For help getting started, read #{theme.path}/README.md."
end

```
