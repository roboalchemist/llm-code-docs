# Class: Jekyll::Commands::New
  
    Inherits:
    
      Jekyll::Command
      
        

          
- Object

- Jekyll::Command

- Jekyll::Commands::New

        show all
      

    Defined in:
    lib/jekyll/commands/new.rb
  
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**blank_template**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**create_blank_site**(path)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**init_with_program**(prog)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**initialized_post_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Internal: Gets the filename of the sample post to be created.

-
  
      .**process**(args, options = {})  ⇒ Object 

-
  
      .**scaffold_post_content**  ⇒ Object 

### Methods inherited from Jekyll::Command

add_build_options, configuration_from_options, inherited, process_site, process_with_graceful_fail, subclasses

## Class Method Details

###
  
    .**blank_template**  ⇒ Object 
  

  

  

  
    
      

```

44
45
46
```

```
# File 'lib/jekyll/commands/new.rb', line 44

def blank_template
  File.expand_path("../../blank_template", __dir__)
end
```

###
  
    .**create_blank_site**(path)  ⇒ Object 
  

  

  

  
    
      

```

48
49
50
51
52
53
54
55
```

```
# File 'lib/jekyll/commands/new.rb', line 48

def create_blank_site(path)
  FileUtils.cp_r blank_template + "/.", path
  FileUtils.chmod_R "u+w", path

  Dir.chdir(path) do
    FileUtils.mkdir(%w(_data _drafts _includes _posts))
  end
end
```

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
21
22
```

```
# File 'lib/jekyll/commands/new.rb', line 9

def init_with_program(prog)
  prog.command(:new) do |c|
    c.syntax "new PATH"
    c.description "Creates a new Jekyll site scaffold in PATH"

    c.option "force", "--force", "Force creation even if PATH already exists"
    c.option "blank", "--blank", "Creates scaffolding but with empty files"
    c.option "skip-bundle", "--skip-bundle", "Skip 'bundle install'"

    c.action do |args, options|
      Jekyll::Commands::New.process(args, options)
    end
  end
end
```

###
  
    .**initialized_post_name**  ⇒ Object 
  

  

  

  
    

Internal: Gets the filename of the sample post to be created

Returns the filename of the sample post, as a String

```

64
65
66
```

```
# File 'lib/jekyll/commands/new.rb', line 64

def initialized_post_name
  "_posts/#{Time.now.strftime("%Y-%m-%d")}-welcome-to-jekyll.markdown"
end
```

###
  
    .**process**(args, options = {})  ⇒ Object 
  

  

  

  
    

Raises:

-

        (ArgumentError)

```

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
```

```
# File 'lib/jekyll/commands/new.rb', line 24

def process(args, options = {})
  raise ArgumentError, "You must specify a path." if args.empty?

  new_blog_path = File.expand_path(args.join(" "), Dir.pwd)
  FileUtils.mkdir_p new_blog_path
  if preserve_source_location?(new_blog_path, options)
    Jekyll.logger.error "Conflict:", "#{new_blog_path} exists and is not empty."
    Jekyll.logger.abort_with "", "Ensure #{new_blog_path} is empty or else try again " \
                                 "with `--force` to proceed and overwrite any files."
  end

  if options["blank"]
    create_blank_site new_blog_path
  else
    create_site new_blog_path
  end

  after_install(new_blog_path, options)
end
```

###
  
    .**scaffold_post_content**  ⇒ Object 
  

  

  

  
    
      

```

57
58
59
```

```
# File 'lib/jekyll/commands/new.rb', line 57

def scaffold_post_content
  ERB.new(File.read(File.expand_path(scaffold_path, site_template))).result
end
```
