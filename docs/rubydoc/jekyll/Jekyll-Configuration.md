# Class: Jekyll::Configuration
  
    Inherits:
    
      Hash
      
        

          
- Object

- Hash

- Jekyll::Configuration

        show all
      

    Defined in:
    lib/jekyll/configuration.rb
  
##

      Constant Summary
      collapse
    

    
      
        DEFAULTS =
          
  
    

Default options. Overridden by values in _config.yml. Strings rather than symbols are used for compatibility with YAML.

```
{
  # Where things are
  "source"              => Dir.pwd,
  "destination"         => File.join(Dir.pwd, "_site"),
  "collections_dir"     => "",
  "cache_dir"           => ".jekyll-cache",
  "plugins_dir"         => "_plugins",
  "layouts_dir"         => "_layouts",
  "data_dir"            => "_data",
  "includes_dir"        => "_includes",
  "collections"         => {},

  # Handling Reading
  "safe"                => false,
  "include"             => [".htaccess"],
  "exclude"             => [],
  "keep_files"          => [".git", ".svn"],
  "encoding"            => "utf-8",
  "markdown_ext"        => "markdown,mkdown,mkdn,mkd,md",
  "strict_front_matter" => false,

  # Filtering Content
  "show_drafts"         => nil,
  "limit_posts"         => 0,
  "future"              => false,
  "unpublished"         => false,

  # Plugins
  "whitelist"           => [],
  "plugins"             => [],

  # Conversion
  "markdown"            => "kramdown",
  "highlighter"         => "rouge",
  "lsi"                 => false,
  "excerpt_separator"   => "\n\n",
  "incremental"         => false,

  # Serving
  "detach"              => false, # default to not detaching the server
  "port"                => "4000",
  "host"                => "127.0.0.1",
  "baseurl"             => nil, # this mounts at /, i.e. no subdirectory
  "show_dir_listing"    => false,

  # Output Configuration
  "permalink"           => "date",
  "paginate_path"       => "/page:num",
  "timezone"            => nil, # use the local timezone

  "quiet"               => false,
  "verbose"             => false,
  "defaults"            => [],

  "liquid"              => {
    "error_mode"       => "warn",
    "strict_filters"   => false,
    "strict_variables" => false,
  },

  "kramdown"            => {
    "auto_ids"      => true,
    "toc_levels"    => (1..6).to_a,
    "entity_output" => "as_char",
    "smart_quotes"  => "lsquo,rsquo,ldquo,rdquo",
    "input"         => "GFM",
    "hard_wrap"     => false,
    "guess_lang"    => true,
    "footnote_nr"   => 1,
    "show_warnings" => false,
  },
}.each_with_object(Configuration.new) { |(k, v), hsh| hsh[k] = v.freeze }.freeze
```

        DEFAULT_EXCLUDES =
          
        
        

```
%w(
  .sass-cache .jekyll-cache
  gemfiles Gemfile Gemfile.lock
  node_modules
  vendor/bundle/ vendor/cache/ vendor/gems/ vendor/ruby/
).freeze
```

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**from**(user_config)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Static: Produce a Configuration ready for use in a Site.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**add_default_collections**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**add_default_excludes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**config_files**(override)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Public: Generate list of configuration files from the override.

-
  
      #**csv_to_array**(csv)  ⇒ Object 

Public: Split a CSV string into an array containing its values.

-
  
      #**get_config_value_with_override**(config_key, override)  ⇒ Object 

-
  
      #**quiet**(override = {})  ⇒ Object 

      (also: #quiet?)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**read_config_file**(file)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Public: Read configuration and return merged Hash.

-
  
      #**read_config_files**(files)  ⇒ Object 

Public: Read in a list of configuration files and merge with this hash.

-
  
      #**safe_load_file**(filename)  ⇒ Object 

-
  
      #**source**(override)  ⇒ Object 

Public: Directory of the Jekyll source folder.

-
  
      #**stringify_keys**  ⇒ Object 

Public: Turn all keys into string.

-
  
      #**validate**  ⇒ Object 

Public: Ensure the proper options are set in the configuration.

-
  
      #**verbose**(override = {})  ⇒ Object 

      (also: #verbose?)
    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Class Method Details

###
  
    .**from**(user_config)  ⇒ Object 
  

  

  

  
    

Static: Produce a Configuration ready for use in a Site. It takes the input, fills in the defaults where values do not exist.

user_config - a Hash or Configuration of overrides.

Returns a Configuration filled with defaults.

```

87
88
89
90
```

```
# File 'lib/jekyll/configuration.rb', line 87

def from(user_config)
  Utils.deep_merge_hashes(DEFAULTS, Configuration[user_config].stringify_keys)
    .add_default_collections.add_default_excludes
end
```

## Instance Method Details

###
  
    #**add_default_collections**  ⇒ Object 
  

  

  

  
    
      

```

230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
```

```
# File 'lib/jekyll/configuration.rb', line 230

def add_default_collections
  config = clone

  # It defaults to `{}`, so this is only if someone sets it to null manually.
  return config if config["collections"].nil?

  # Ensure we have a hash.
  if config["collections"].is_a?(Array)
    config["collections"] = config["collections"].each_with_object({}) do |collection, hash|
      hash[collection] = {}
    end
  end

  config["collections"] = Utils.deep_merge_hashes(
    { "posts" => {} }, config["collections"]
  ).tap do |collections|
    collections["posts"]["output"] = true
    if config["permalink"]
      collections["posts"]["permalink"] ||= style_to_permalink(config["permalink"])
    end
  end

  config
end
```

###
  
    #**add_default_excludes**  ⇒ Object 
  

  

  

  
    
      

```

262
263
264
265
266
267
268
```

```
# File 'lib/jekyll/configuration.rb', line 262

def add_default_excludes
  config = clone
  return config if config["exclude"].nil?

  config["exclude"].concat(DEFAULT_EXCLUDES).uniq!
  config
end
```

###
  
    #**config_files**(override)  ⇒ Object 
  

  

  

  
    

Public: Generate list of configuration files from the override

override - the command-line options hash

Returns an Array of config files

```

141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
```

```
# File 'lib/jekyll/configuration.rb', line 141

def config_files(override)
  # Adjust verbosity quickly
  Jekyll.logger.adjust_verbosity(
    :quiet   => quiet?(override),
    :verbose => verbose?(override)
  )

  # Get configuration from <source>/_config.yml or <source>/<config_file>
  config_files = override["config"]
  if config_files.to_s.empty?
    default = %w(yml yaml toml).find(-> { "yml" }) do |ext|
      File.exist?(Jekyll.sanitized_path(source(override), "_config.#{ext}"))
    end
    config_files = Jekyll.sanitized_path(source(override), "_config.#{default}")
    @default_config_file = true
  end
  Array(config_files)
end
```

###
  
    #**csv_to_array**(csv)  ⇒ Object 
  

  

  

  
    

Public: Split a CSV string into an array containing its values

csv - the string of comma-separated values

Returns an array of the values contained in the CSV

```

214
215
216
```

```
# File 'lib/jekyll/configuration.rb', line 214

def csv_to_array(csv)
  csv.split(",").map(&:strip)
end
```

###
  
    #**get_config_value_with_override**(config_key, override)  ⇒ Object 
  

  

  

  
    
      

```

100
101
102
```

```
# File 'lib/jekyll/configuration.rb', line 100

def get_config_value_with_override(config_key, override)
  override[config_key] || self[config_key] || DEFAULTS[config_key]
end
```

###
  
    #**quiet**(override = {})  ⇒ Object 
  

  
    Also known as:
    quiet?
    
  

  

  
    
      

```

113
114
115
```

```
# File 'lib/jekyll/configuration.rb', line 113

def quiet(override = {})
  get_config_value_with_override("quiet", override)
end
```

###
  
    #**read_config_file**(file)  ⇒ Object 
  

  

  

  
    

Public: Read configuration and return merged Hash

file - the path to the YAML file to be read in

Returns this configuration, overridden by the values in the file

```

165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
```

```
# File 'lib/jekyll/configuration.rb', line 165

def read_config_file(file)
  file = File.expand_path(file)
  next_config = safe_load_file(file)

  unless next_config.is_a?(Hash)
    raise ArgumentError, "Configuration file: (INVALID) #{file}".yellow
  end

  Jekyll.logger.info "Configuration file:", file
  next_config
rescue SystemCallError
  if @default_config_file ||= nil
    Jekyll.logger.warn "Configuration file:", "none"
    {}
  else
    Jekyll.logger.error "Fatal:", "The configuration file '#{file}' could not be found."
    raise LoadError, "The Configuration file '#{file}' could not be found."
  end
end
```

###
  
    #**read_config_files**(files)  ⇒ Object 
  

  

  

  
    

Public: Read in a list of configuration files and merge with this hash

files - the list of configuration file paths

Returns the full configuration, with the defaults overridden by the values in the configuration files

```

191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
```

```
# File 'lib/jekyll/configuration.rb', line 191

def read_config_files(files)
  configuration = clone

  begin
    files.each do |config_file|
      next if config_file.nil? || config_file.empty?

      new_config = read_config_file(config_file)
      configuration = Utils.deep_merge_hashes(configuration, new_config)
    end
  rescue ArgumentError => e
    Jekyll.logger.warn "WARNING:", "Error reading configuration. Using defaults (and options)."
    warn e
  end

  configuration.validate.add_default_collections
end
```

###
  
    #**safe_load_file**(filename)  ⇒ Object 
  

  

  

  
    
      

```

123
124
125
126
127
128
129
130
131
132
133
134
```

```
# File 'lib/jekyll/configuration.rb', line 123

def safe_load_file(filename)
  case File.extname(filename)
  when %r!\.toml!i
    Jekyll::External.require_with_graceful_fail("tomlrb") unless defined?(Tomlrb)
    Tomlrb.load_file(filename)
  when %r!\.ya?ml!i
    SafeYAML.load_file(filename) || {}
  else
    raise ArgumentError,
          "No parser for '#{filename}' is available. Use a .y(a)ml or .toml file instead."
  end
end
```

###
  
    #**source**(override)  ⇒ Object 
  

  

  

  
    

Public: Directory of the Jekyll source folder

override - the command-line options hash

Returns the path to the Jekyll source directory

```

109
110
111
```

```
# File 'lib/jekyll/configuration.rb', line 109

def source(override)
  get_config_value_with_override("source", override)
end
```

###
  
    #**stringify_keys**  ⇒ Object 
  

  

  

  
    

Public: Turn all keys into string

Return a copy of the hash where all its keys are strings

```

96
97
98
```

```
# File 'lib/jekyll/configuration.rb', line 96

def stringify_keys
  each_with_object({}) { |(k, v), hsh| hsh[k.to_s] = v }
end
```

###
  
    #**validate**  ⇒ Object 
  

  

  

  
    

Public: Ensure the proper options are set in the configuration

Returns the configuration Hash

```

221
222
223
224
225
226
227
228
```

```
# File 'lib/jekyll/configuration.rb', line 221

def validate
  config = clone

  check_plugins(config)
  check_include_exclude(config)

  config
end
```

###
  
    #**verbose**(override = {})  ⇒ Object 
  

  
    Also known as:
    verbose?
    
  

  

  
    
      

```

118
119
120
```

```
# File 'lib/jekyll/configuration.rb', line 118

def verbose(override = {})
  get_config_value_with_override("verbose", override)
end
```
