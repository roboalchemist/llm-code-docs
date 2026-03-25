# Module: Jekyll::External
  
    Defined in:
    lib/jekyll/external.rb
  
  

  
    
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**blessed_gems**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Gems that, if installed, should be loaded.

-
  
      .**require_if_present**(names)  ⇒ Object 

Require a gem or file if it’s present, otherwise silently fail.

-
  
      .**require_with_graceful_fail**(names)  ⇒ Object 

Require a gem or gems.

-
  
      .**version_constraint**(gem_name)  ⇒ Object 

The version constraint required to activate a given gem.

## Class Method Details

###
  
    .**blessed_gems**  ⇒ Object 
  

  

  

  
    

Gems that, if installed, should be loaded. Usually contain subcommands.

```

10
11
12
13
14
15
16
```

```
# File 'lib/jekyll/external.rb', line 10

def blessed_gems
  %w(
    jekyll-compose
    jekyll-docs
    jekyll-import
  )
end
```

###
  
    .**require_if_present**(names)  ⇒ Object 
  

  

  

  
    

Require a gem or file if it’s present, otherwise silently fail.

names - a string gem name or array of gem names

```

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
# File 'lib/jekyll/external.rb', line 23

def require_if_present(names)
  Array(names).each do |name|
    require name
  rescue LoadError
    Jekyll.logger.debug "Couldn't load #{name}. Skipping."
    yield(name, version_constraint(name)) if block_given?
    false
  end
end
```

###
  
    .**require_with_graceful_fail**(names)  ⇒ Object 
  

  

  

  
    

Require a gem or gems. If it’s not present, show a very nice error message that explains everything and is much more helpful than the normal LoadError.

names - a string gem name or array of gem names

```

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
```

```
# File 'lib/jekyll/external.rb', line 54

def require_with_graceful_fail(names)
  Array(names).each do |name|
    Jekyll.logger.debug "Requiring:", name.to_s
    require name
  rescue LoadError => e
    Jekyll.logger.error "Dependency Error:", <<~MSG
      Yikes! It looks like you don't have #{name} or one of its dependencies installed.
      In order to use Jekyll as currently configured, you'll need to install this gem.

      If you've run Jekyll with `bundle exec`, ensure that you have included the #{name}
      gem in your Gemfile as well.

      The full error message from Ruby is: '#{e.message}'

      If you run into trouble, you can find helpful resources at https://jekyllrb.com/help/!
    MSG
    raise Jekyll::Errors::MissingDependencyException, name
  end
end
```

###
  
    .**version_constraint**(gem_name)  ⇒ Object 
  

  

  

  
    

The version constraint required to activate a given gem. Usually the gem version requirement is “> 0,” because any version will do. In the case of jekyll-docs, however, we require the exact same version as Jekyll.

Returns a String version constraint in a parseable form for RubyGems.

```

41
42
43
44
45
```

```
# File 'lib/jekyll/external.rb', line 41

def version_constraint(gem_name)
  return "= #{Jekyll::VERSION}" if gem_name.to_s.eql?("jekyll-docs")

  "> 0"
end
```
