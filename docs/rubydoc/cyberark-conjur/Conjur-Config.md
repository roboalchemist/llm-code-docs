# Class: Conjur::Config
  
    Inherits:
    
      Object
      
        

          
- Object

- Conjur::Config

        show all
      

    Defined in:
    lib/conjur/config.rb
  
##

      Constant Summary
      collapse
    

    
      
        @@attributes =
          
        
        

```
{}

```

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**[]**(key)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**alternate_key**(key)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**apply**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**clear**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**default_config_files**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**inspect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**keys**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**load**(config_files = default_config_files)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**member?**(key)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**merge**(a)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**plugin_config_files**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**plugins**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**user_config_files**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

###
  
    .**[]**(key)  ⇒ Object 
  

  

  

  
    
      

```

124
125
126
```

```
# File 'lib/conjur/config.rb', line 124

def [](key)
  @@attributes[key.to_s]
end

```

###
  
    .**alternate_key**(key)  ⇒ Object 
  

  

  

  
    
      

```

132
133
134
135
136
137
138
```

```
# File 'lib/conjur/config.rb', line 132

def alternate_key key
  case key
    when String then key.to_sym
    when Symbol then key.to_s
    else key
  end
end

```

###
  
    .**apply**  ⇒ Object 
  

  

  

  
    
      

```

78
79
80
81
82
83
84
85
86
87
88
89
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
```

```
# File 'lib/conjur/config.rb', line 78

def apply
  require 'conjur/configuration'

  keys = Config.keys.dup
  keys.delete(:plugins)

  cfg = Conjur.configuration
  keys.each do |k|
    if Conjur.configuration.respond_to?("#{k}_env_var") && (env_var = Conjur.configuration.send("#{k}_env_var")) && (v = ENV[env_var])
      if Conjur.log
        Conjur.log << "Not overriding environment setting #{k}=#{v}\n"
      end
      next
    end
    value = Config[k]
    cfg.set k, value if value
  end

  Conjur.log << "Using authn url #{Conjur.configuration.authn_url}\n" if Conjur.log

  Conjur.config.apply_cert_config!
end

```

###
  
    .**clear**  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
```

```
# File 'lib/conjur/config.rb', line 29

def clear
  @@attributes = {}
end

```

###
  
    .**default_config_files**  ⇒ Object 
  

  

  

  
    
      

```

55
56
57
```

```
# File 'lib/conjur/config.rb', line 55

def default_config_files
  ['/etc/conjur.conf', user_config_files, plugin_config_files].flatten.uniq
end

```

###
  
    .**inspect**  ⇒ Object 
  

  

  

  
    
      

```

102
103
104
```

```
# File 'lib/conjur/config.rb', line 102

def inspect
  @@attributes.inspect
end

```

###
  
    .**keys**  ⇒ Object 
  

  

  

  
    
      

```

120
121
122
```

```
# File 'lib/conjur/config.rb', line 120

def keys
  @@attributes.keys.map(&:to_sym)
end

```

###
  
    .**load**(config_files = default_config_files)  ⇒ Object 
  

  

  

  
    
      

```

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
```

```
# File 'lib/conjur/config.rb', line 59

def load(config_files = default_config_files)
  require 'yaml'
  require 'conjur/log'

  config_files.each do |f|
    if File.file?(f)
      if Conjur.log
        Conjur.log << "Loading #{f}\n"
      end
      config = YAML.load(IO.read(f)).stringify_keys rescue {}
      if config['cert_file']
        config['cert_file'] = File.expand_path(config['cert_file'], File.dirname(f))
      end
      Conjur::Config.merge config
    end
  end
end

```

###
  
    .**member?**(key)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

128
129
130
```

```
# File 'lib/conjur/config.rb', line 128

def member? key
  @@attributes.member?(key) || @@attributes.member?(alternate_key(key))
end

```

###
  
    .**merge**(a)  ⇒ Object 
  

  

  

  
    
      

```

115
116
117
118
```

```
# File 'lib/conjur/config.rb', line 115

def merge(a)
  a = {} unless a
  @@attributes.deep_merge!(a.stringify_keys)
end

```

###
  
    .**plugin_config_files**  ⇒ Object 
  

  

  

  
    
      

```

33
34
35
```

```
# File 'lib/conjur/config.rb', line 33

def plugin_config_files
  [ '/opt/conjur/etc/plugins.yml' ]
end

```

###
  
    .**plugins**  ⇒ Object 
  

  

  

  
    
      

```

106
107
108
109
110
111
112
113
```

```
# File 'lib/conjur/config.rb', line 106

def plugins
  plugins = @@attributes['plugins']
  if plugins
    plugins.is_a?(Array) ? plugins : plugins.split(',')
  else
    []
  end
end

```

###
  
    .**user_config_files**  ⇒ Object 
  

  

  

  
    
      

```

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
48
49
50
51
52
53
```

```
# File 'lib/conjur/config.rb', line 37

def user_config_files
  $stderr.puts "variable return %s\n", ENV['CONJURRC']
  #raise ENV.inspect
  if ENV['CONJURRC']
    $stderr.puts "variable return %s\n", ENV['CONJURRC']
    return ENV['CONJURRC']
  else
    homefile = File.expand_path "~/.conjurrc"
    pwdfile = File.expand_path ".conjurrc"
    if homefile != pwdfile && File.file?(pwdfile)
      $stderr.puts """NOTE:\t.conjurrc file detected in the current directory.\n"\
          "\tIt's no longer consulted in this version. Please explicitly\n"\
          "\tset CONJURRC=./.conjurrc if you're sure you want to use it."
    end
    [ homefile ]
  end
end

```
