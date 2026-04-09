# Class: Jekyll::Commands::Help
  
    Inherits:
    
      Jekyll::Command
      
        

          
- Object

- Jekyll::Command

- Jekyll::Commands::Help

        show all
      

    Defined in:
    lib/jekyll/commands/help.rb
  
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**init_with_program**(prog)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**invalid_command**(prog, cmd)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

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
19
20
21
22
23
24
```

```
# File 'lib/jekyll/commands/help.rb', line 7

def init_with_program(prog)
  prog.command(:help) do |c|
    c.syntax "help [subcommand]"
    c.description "Show the help message, optionally for a given subcommand."

    c.action do |args, _|
      cmd = (args.first || "").to_sym
      if args.empty?
        Jekyll.logger.info prog.to_s
      elsif prog.has_command? cmd
        Jekyll.logger.info prog.commands[cmd].to_s
      else
        invalid_command(prog, cmd)
        abort
      end
    end
  end
end
```

###
  
    .**invalid_command**(prog, cmd)  ⇒ Object 
  

  

  

  
    
      

```

26
27
28
29
30
```

```
# File 'lib/jekyll/commands/help.rb', line 26

def invalid_command(prog, cmd)
  Jekyll.logger.error "Error:",
                      "Hmm... we don't know what the '#{cmd}' command is."
  Jekyll.logger.info  "Valid commands:", prog.commands.keys.join(", ")
end
```
