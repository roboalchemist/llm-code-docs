# Module: Jekyll::Utils::Platforms
  
      Extended by:
      Platforms
  
  
  
  
  

  
  
    Included in:
    Platforms
  
  

  
  
    Defined in:
    lib/jekyll/utils/platforms.rb
  
  

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**bash_on_windows?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Determine if Windows Subsystem for Linux (WSL).

-
  
      #**jruby?**  ⇒ Boolean 

-
  
      #**linux?**  ⇒ Boolean 

-
  
      #**mri?**  ⇒ Boolean 

-
  
      #**osx?**  ⇒ Boolean 

-
  
      #**unix?**  ⇒ Boolean 

-
  
      #**vanilla_windows?**  ⇒ Boolean 

      (also: #really_windows?)
    
  
  
  
  
  
  
  
  

  
    

Not a Windows Subsystem for Linux (WSL).

-
  
      #**windows?**  ⇒ Boolean 

## Instance Method Details

###
  
    #**bash_on_windows?**  ⇒ Boolean 
  

  

  

  
    

Determine if Windows Subsystem for Linux (WSL)

Returns:

-

```

27
28
29
```

```
# File 'lib/jekyll/utils/platforms.rb', line 27

def bash_on_windows?
  linux_os? && microsoft_proc_version?
end

```

###
  
    #**jruby?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

```

8
9
10
```

```
# File 'lib/jekyll/utils/platforms.rb', line 8

def jruby?
  RUBY_ENGINE == "jruby"
end

```

###
  
    #**linux?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

```

31
32
33
```

```
# File 'lib/jekyll/utils/platforms.rb', line 31

def linux?
  linux_os? && !microsoft_proc_version?
end

```

###
  
    #**mri?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

```

12
13
14
```

```
# File 'lib/jekyll/utils/platforms.rb', line 12

def mri?
  RUBY_ENGINE == "ruby"
end

```

###
  
    #**osx?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

```

35
36
37
```

```
# File 'lib/jekyll/utils/platforms.rb', line 35

def osx?
  rbconfig_host.match?(%r!darwin|mac os!)
end

```

###
  
    #**unix?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

```

39
40
41
```

```
# File 'lib/jekyll/utils/platforms.rb', line 39

def unix?
  rbconfig_host.match?(%r!solaris|bsd!)
end

```

###
  
    #**vanilla_windows?**  ⇒ Boolean 
  

  
    Also known as:
    really_windows?
    
  

  

  
    

Not a Windows Subsystem for Linux (WSL)

Returns:

-

```

21
22
23
```

```
# File 'lib/jekyll/utils/platforms.rb', line 21

def vanilla_windows?
  rbconfig_host.match?(%r!mswin|mingw|cygwin!) && proc_version.empty?
end

```

###
  
    #**windows?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

```

16
17
18
```

```
# File 'lib/jekyll/utils/platforms.rb', line 16

def windows?
  vanilla_windows? || bash_on_windows?
end

```
