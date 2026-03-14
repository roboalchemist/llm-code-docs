# Module: Jekyll::Deprecator
  
      Extended by:
      Deprecator
  
  
  
  
  

  
  
    Included in:
    Deprecator
  
  

  
  
    Defined in:
    lib/jekyll/deprecator.rb
  
  

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**arg_is_present?**(args, deprecated_argument, message)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**defaults_deprecate_type**(old, current)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**deprecation_message**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**no_subcommand**(args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**process**(args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

###
  
    #**arg_is_present?**(args, deprecated_argument, message)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

36
37
38
```

```
# File 'lib/jekyll/deprecator.rb', line 36

def arg_is_present?(args, deprecated_argument, message)
  deprecation_message(message) if args.include?(deprecated_argument)
end
```

###
  
    #**defaults_deprecate_type**(old, current)  ⇒ Object 
  

  

  

  
    
      

```

44
45
46
47
48
```

```
# File 'lib/jekyll/deprecator.rb', line 44

def defaults_deprecate_type(old, current)
  Jekyll.logger.warn "Defaults:", "The '#{old}' type has become '#{current}'."
  Jekyll.logger.warn "Defaults:", "Please update your front-matter defaults to use \
                    'type: #{current}'."
end
```

###
  
    #**deprecation_message**(message)  ⇒ Object 
  

  

  

  
    
      

```

40
41
42
```

```
# File 'lib/jekyll/deprecator.rb', line 40

def deprecation_message(message)
  Jekyll.logger.warn "Deprecation:", message
end
```

###
  
    #**no_subcommand**(args)  ⇒ Object 
  

  

  

  
    
      

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
# File 'lib/jekyll/deprecator.rb', line 27

def no_subcommand(args)
  unless args.empty? ||
      args.first !~ %r(!/^--/!) || %w(--help --version).include?(args.first)
    deprecation_message "Jekyll now uses subcommands instead of just switches. \
                      Run `jekyll help` to find out more."
    abort
  end
end
```

###
  
    #**process**(args)  ⇒ Object 
  

  

  

  
    
      

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
25
```

```
# File 'lib/jekyll/deprecator.rb', line 7

def process(args)
  arg_is_present? args, "--server", "The --server command has been replaced by the \
                      'serve' subcommand."
  arg_is_present? args, "--serve", "The --serve command has been replaced by the \
                      'serve' subcommand."
  arg_is_present? args, "--no-server", "To build Jekyll without launching a server, \
                      use the 'build' subcommand."
  arg_is_present? args, "--auto", "The switch '--auto' has been replaced with \
                      '--watch'."
  arg_is_present? args, "--no-auto", "To disable auto-replication, simply leave off \
                      the '--watch' switch."
  arg_is_present? args, "--pygments", "The 'pygments' settings has been removed in \
                      favour of 'highlighter'."
  arg_is_present? args, "--paginate", "The 'paginate' setting can only be set in \
                      your config files."
  arg_is_present? args, "--url", "The 'url' setting can only be set in your \
                      config files."
  no_subcommand(args)
end
```
