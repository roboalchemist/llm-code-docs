# Class: Jekyll::PluginManager
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::PluginManager

        show all
      

    Defined in:
    lib/jekyll/plugin_manager.rb
  
## Instance Attribute Summary collapse

-
  
      #**site**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute site.

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**gemfile_exists?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Check for the existence of a Gemfile.

-
  
      .**require_from_bundler**  ⇒ Object 

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**conscientious_require**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Require all the plugins which are allowed.

-
  
      #**deprecation_checks**  ⇒ Object 

-
  
      #**initialize**(site)  ⇒ PluginManager 

    constructor
  
  
  
  
  
  

  
    

Create an instance of this class.

-
  
      #**plugin_allowed?**(plugin_name)  ⇒ Boolean 

Check whether a gem plugin is allowed to be used during this build.

-
  
      #**plugins_path**  ⇒ Object 

Public: Setup the plugin search path.

-
  
      #**require_gems**  ⇒ Object 

Require each of the gem plugins specified.

-
  
      #**require_plugin_files**  ⇒ Object 

Require all .rb files if safe mode is off.

-
  
      #**require_theme_deps**  ⇒ Object 

Require each of the runtime_dependencies specified by the theme’s gemspec.

-
  
      #**whitelist**  ⇒ Object 

Build an array of allowed plugin gem names.

## Constructor Details

###
  
    #**initialize**(site)  ⇒ PluginManager 
  

  

  

  
    

Create an instance of this class.

site - the instance of Jekyll::Site we’re concerned with

Returns nothing

```

12
13
14
```

```
# File 'lib/jekyll/plugin_manager.rb', line 12

def initialize(site)
  @site = site
end
```

## Instance Attribute Details

###
  
    #**site**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute site.

```

5
6
7
```

```
# File 'lib/jekyll/plugin_manager.rb', line 5

def site
  @site
end
```

## Class Method Details

###
  
    .**gemfile_exists?**  ⇒ Boolean 
  

  

  

  
    

Check for the existence of a Gemfile.

Returns true if a Gemfile exists in the places bundler will look

Returns:

-

        (Boolean)

```

67
68
69
```

```
# File 'lib/jekyll/plugin_manager.rb', line 67

def self.gemfile_exists?
  File.file?("Gemfile") || (ENV["BUNDLE_GEMFILE"] && File.file?(ENV["BUNDLE_GEMFILE"]))
end
```

###
  
    .**require_from_bundler**  ⇒ Object 
  

  

  

  
    
      

```

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
59
60
61
62
```

```
# File 'lib/jekyll/plugin_manager.rb', line 48

def self.require_from_bundler
  if !ENV["JEKYLL_NO_BUNDLER_REQUIRE"] && gemfile_exists?
    require "bundler"

    Bundler.setup
    required_gems = Bundler.require(:jekyll_plugins)
    message = "Required #{required_gems.map(&:name).join(", ")}"
    Jekyll.logger.debug("PluginManager:", message)
    ENV["JEKYLL_NO_BUNDLER_REQUIRE"] = "true"

    true
  else
    false
  end
end
```

## Instance Method Details

###
  
    #**conscientious_require**  ⇒ Object 
  

  

  

  
    

Require all the plugins which are allowed.

Returns nothing

```

19
20
21
22
23
24
```

```
# File 'lib/jekyll/plugin_manager.rb', line 19

def conscientious_require
  require_theme_deps if site.theme
  require_plugin_files
  require_gems
  deprecation_checks
end
```

###
  
    #**deprecation_checks**  ⇒ Object 
  

  

  

  
    
      

```

112
113
114
115
116
117
118
119
120
121
```

```
# File 'lib/jekyll/plugin_manager.rb', line 112

def deprecation_checks
  pagination_included = (site.config["plugins"] || []).include?("jekyll-paginate") ||
    defined?(Jekyll::Paginate)
  if site.config["paginate"] && !pagination_included
    Jekyll::Deprecator.deprecation_message <<~MSG
      You appear to have pagination turned on, but you haven't included the `jekyll-paginate`
      gem. Ensure you have `plugins: [jekyll-paginate]` in your configuration file.
    MSG
  end
end
```

###
  
    #**plugin_allowed?**(plugin_name)  ⇒ Boolean 
  

  

  

  
    

Check whether a gem plugin is allowed to be used during this build.

plugin_name - the name of the plugin

Returns true if the plugin name is in the whitelist or if the site is not

```
in safe mode.

```

Returns:

-

        (Boolean)

```

77
78
79
```

```
# File 'lib/jekyll/plugin_manager.rb', line 77

def plugin_allowed?(plugin_name)
  !site.safe || whitelist.include?(plugin_name)
end
```

###
  
    #**plugins_path**  ⇒ Object 
  

  

  

  
    

Public: Setup the plugin search path

Returns an Array of plugin search paths

```

104
105
106
107
108
109
110
```

```
# File 'lib/jekyll/plugin_manager.rb', line 104

def plugins_path
  if site.config["plugins_dir"].eql? Jekyll::Configuration::DEFAULTS["plugins_dir"]
    [site.in_source_dir(site.config["plugins_dir"])]
  else
    Array(site.config["plugins_dir"]).map { |d| File.expand_path(d) }
  end
end
```

###
  
    #**require_gems**  ⇒ Object 
  

  

  

  
    

Require each of the gem plugins specified.

Returns nothing.

```

29
30
31
32
33
```

```
# File 'lib/jekyll/plugin_manager.rb', line 29

def require_gems
  Jekyll::External.require_with_graceful_fail(
    site.gems.select { |plugin| plugin_allowed?(plugin) }
  )
end
```

###
  
    #**require_plugin_files**  ⇒ Object 
  

  

  

  
    

Require all .rb files if safe mode is off

Returns nothing.

```

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
# File 'lib/jekyll/plugin_manager.rb', line 92

def require_plugin_files
  unless site.safe
    plugins_path.each do |plugin_search_path|
      plugin_files = Utils.safe_glob(plugin_search_path, File.join("**", "*.rb"))
      Jekyll::External.require_with_graceful_fail(plugin_files)
    end
  end
end
```

###
  
    #**require_theme_deps**  ⇒ Object 
  

  

  

  
    

Require each of the runtime_dependencies specified by the theme’s gemspec.

Returns false only if no dependencies have been specified, otherwise nothing.

```

38
39
40
41
42
43
44
45
46
```

```
# File 'lib/jekyll/plugin_manager.rb', line 38

def require_theme_deps
  return false unless site.theme.runtime_dependencies

  site.theme.runtime_dependencies.each do |dep|
    next if dep.name == "jekyll"

    External.require_with_graceful_fail(dep.name) if plugin_allowed?(dep.name)
  end
end
```

###
  
    #**whitelist**  ⇒ Object 
  

  

  

  
    

Build an array of allowed plugin gem names.

Returns an array of strings, each string being the name of a gem name

```
that is allowed to be used.

```

```

85
86
87
```

```
# File 'lib/jekyll/plugin_manager.rb', line 85

def whitelist
  @whitelist ||= [site.config["whitelist"]].flatten
end
```
