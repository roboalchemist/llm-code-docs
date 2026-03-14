# Module: Jekyll
  
    Defined in:
    lib/jekyll/url.rb,

  lib/jekyll.rb,
 lib/jekyll/page.rb,
 lib/jekyll/site.rb,
 lib/jekyll/cache.rb,
 lib/jekyll/hooks.rb,
 lib/jekyll/theme.rb,
 lib/jekyll/utils.rb,
 lib/jekyll/errors.rb,
 lib/jekyll/layout.rb,
 lib/jekyll/plugin.rb,
 lib/jekyll/reader.rb,
 lib/jekyll/cleaner.rb,
 lib/jekyll/command.rb,
 lib/jekyll/excerpt.rb,
 lib/jekyll/filters.rb,
 lib/jekyll/version.rb,
 lib/jekyll/document.rb,
 lib/jekyll/external.rb,
 lib/jekyll/profiler.rb,
 lib/jekyll/renderer.rb,
 lib/jekyll/converter.rb,
 lib/jekyll/generator.rb,
 lib/jekyll/inclusion.rb,
 lib/jekyll/publisher.rb,
 lib/jekyll/stevenson.rb,
 lib/jekyll/tags/link.rb,
 lib/jekyll/collection.rb,
 lib/jekyll/deprecator.rb,
 lib/jekyll/drops/drop.rb,
 lib/jekyll/utils/ansi.rb,
 lib/jekyll/utils/exec.rb,
 lib/jekyll/convertible.rb,
 lib/jekyll/log_adapter.rb,
 lib/jekyll/regenerator.rb,
 lib/jekyll/static_file.rb,
 lib/jekyll/commands/new.rb,
 lib/jekyll/entry_filter.rb,
 lib/jekyll/page_excerpt.rb,
 lib/jekyll/path_manager.rb,
 lib/jekyll/tags/include.rb,
 lib/jekyll/utils/win_tz.rb,
 lib/jekyll/commands/help.rb,
 lib/jekyll/configuration.rb,
 lib/jekyll/related_posts.rb,
 lib/jekyll/tags/post_url.rb,
 lib/jekyll/theme_builder.rb,
 lib/jekyll/commands/build.rb,
 lib/jekyll/commands/clean.rb,
 lib/jekyll/commands/serve.rb,
 lib/jekyll/drops/url_drop.rb,
 lib/jekyll/plugin_manager.rb,
 lib/jekyll/tags/highlight.rb,
 lib/jekyll/utils/internet.rb,
 lib/jekyll/commands/doctor.rb,
 lib/jekyll/drops/site_drop.rb,
 lib/jekyll/liquid_renderer.rb,
 lib/jekyll/utils/platforms.rb,
 lib/jekyll/drops/theme_drop.rb,
 lib/jekyll/drops/jekyll_drop.rb,
 lib/jekyll/liquid_extensions.rb,
 lib/jekyll/commands/new_theme.rb,
 lib/jekyll/drops/excerpt_drop.rb,
 lib/jekyll/utils/thread_event.rb,
 lib/jekyll/converters/identity.rb,
 lib/jekyll/converters/markdown.rb,
 lib/jekyll/drops/document_drop.rb,
 lib/jekyll/filters/url_filters.rb,
 lib/jekyll/page_without_a_file.rb,
 lib/jekyll/readers/data_reader.rb,
 lib/jekyll/readers/page_reader.rb,
 lib/jekyll/readers/post_reader.rb,
 lib/jekyll/filters/date_filters.rb,
 lib/jekyll/frontmatter_defaults.rb,
 lib/jekyll/liquid_renderer/file.rb,
 lib/jekyll/drops/collection_drop.rb,
 lib/jekyll/liquid_renderer/table.rb,
 lib/jekyll/readers/layout_reader.rb,
 lib/jekyll/commands/serve/servlet.rb,
 lib/jekyll/converters/smartypants.rb,
 lib/jekyll/drops/static_file_drop.rb,
 lib/jekyll/filters/grouping_filters.rb,
 lib/jekyll/commands/serve/websockets.rb,
 lib/jekyll/readers/collection_reader.rb,
 lib/jekyll/drops/unified_payload_drop.rb,
 lib/jekyll/readers/static_file_reader.rb,
 lib/jekyll/readers/theme_assets_reader.rb,
 lib/jekyll/commands/serve/live_reload_reactor.rb,
 lib/jekyll/converters/markdown/kramdown_parser.rb

## Overview

Convertible provides methods for converting a pagelike item from a certain type of markup into actual content

Requires

```
self.site -> Jekyll::Site
self.content
self.content=
self.data=
self.ext=
self.output=
self.name
self.path
self.type -> :page, :post or :draft

```

## Defined Under Namespace

      **Modules:** Commands, Converters, Convertible, Deprecator, Drops, Errors, External, Filters, Hooks, LiquidExtensions, Tags, Utils
    
  
    
      **Classes:** Cache, Cleaner, Collection, CollectionReader, Command, Configuration, Converter, DataReader, Document, EntryFilter, Excerpt, FrontmatterDefaults, Inclusion, Layout, LayoutReader, LiquidRenderer, LogAdapter, Page, PageExcerpt, PageReader, PageWithoutAFile, PathManager, Plugin, PluginManager, PostReader, Profiler, Publisher, Reader, Regenerator, RelatedPosts, Renderer, Site, StaticFile, StaticFileReader, Stevenson, Theme, ThemeAssetsReader, ThemeBuilder, URL
    
  

  
    
##

      Constant Summary
      collapse
    

    
      
        VERSION =
          
        
        

```
"4.4.1"
```

        Generator =
          
        
        

```
Class.new(Plugin)
```

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**configuration**(override = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Public: Generate a Jekyll configuration Hash by merging the default options with anything in _config.yml, and adding the given options on top.

-
  
      .**env**  ⇒ Object 

Public: Tells you which Jekyll environment you are building in so you can skip tasks if you need to.

-
  
      .**logger**  ⇒ Object 

Public: Fetch the logger instance for this Jekyll process.

-
  
      .**logger=**(writer)  ⇒ Object 

Public: Set the log writer.

-
  
      .**sanitized_path**(base_directory, questionable_path)  ⇒ Object 

Public: Ensures the questionable path is prefixed with the base directory         and prepends the questionable path with the base directory if false.

-
  
      .**set_timezone**(timezone)  ⇒ Object 

Public: Set the TZ environment variable to use the timezone specified.

-
  
      .**sites**  ⇒ Object 

Public: An array of sites.

## Class Method Details

###
  
    .**configuration**(override = {})  ⇒ Object 
  

  

  

  
    

Public: Generate a Jekyll configuration Hash by merging the default options with anything in _config.yml, and adding the given options on top.

override - A Hash of config directives that override any options in both

```
the defaults and the config file.
See Jekyll::Configuration::DEFAULTS for a
list of option names and their defaults.

```

Returns the final configuration Hash.

```

114
115
116
117
118
119
120
121
122
123
124
125
```

```
# File 'lib/jekyll.rb', line 114

def configuration(override = {})
  config = Configuration.new
  override = Configuration[override].stringify_keys
  unless override.delete("skip_config_files")
    config = config.read_config_files(config.config_files(override))
  end

  # Merge DEFAULTS < _config.yml < override
  Configuration.from(Utils.deep_merge_hashes(config, override)).tap do |obj|
    set_timezone(obj["timezone"]) if obj["timezone"]
  end
end
```

###
  
    .**env**  ⇒ Object 
  

  

  

  
    

Public: Tells you which Jekyll environment you are building in so you can skip tasks if you need to.  This is useful when doing expensive compression tasks on css and images and allows you to skip that when working in development.

```

101
102
103
```

```
# File 'lib/jekyll.rb', line 101

def env
  ENV["JEKYLL_ENV"] || "development"
end
```

###
  
    .**logger**  ⇒ Object 
  

  

  

  
    

Public: Fetch the logger instance for this Jekyll process.

Returns the LogAdapter instance.

```

145
146
147
```

```
# File 'lib/jekyll.rb', line 145

def logger
  @logger ||= LogAdapter.new(Stevenson.new, (ENV["JEKYLL_LOG_LEVEL"] || :info).to_sym)
end
```

###
  
    .**logger=**(writer)  ⇒ Object 
  

  

  

  
    

Public: Set the log writer.

```
New log writer must respond to the same methods
as Ruby's internal Logger.

```

writer - the new Logger-compatible log transport

Returns the new logger.

```

156
157
158
```

```
# File 'lib/jekyll.rb', line 156

def logger=(writer)
  @logger = LogAdapter.new(writer, (ENV["JEKYLL_LOG_LEVEL"] || :info).to_sym)
end
```

###
  
    .**sanitized_path**(base_directory, questionable_path)  ⇒ Object 
  

  

  

  
    

Public: Ensures the questionable path is prefixed with the base directory

```
and prepends the questionable path with the base directory if false.

```

base_directory - the directory with which to prefix the questionable path questionable_path - the path we’re unsure about, and want prefixed

Returns the sanitized path.

```

174
175
176
177
178
179
```

```
# File 'lib/jekyll.rb', line 174

def sanitized_path(base_directory, questionable_path)
  return base_directory if base_directory.eql?(questionable_path)
  return base_directory if questionable_path.nil?

  +Jekyll::PathManager.sanitized_path(base_directory, questionable_path)
end
```

###
  
    .**set_timezone**(timezone)  ⇒ Object 
  

  

  

  
    

Public: Set the TZ environment variable to use the timezone specified

timezone - the IANA Time Zone

Returns nothing rubocop:disable Naming/AccessorMethodName

```

133
134
135
136
137
138
139
```

```
# File 'lib/jekyll.rb', line 133

def set_timezone(timezone)
  ENV["TZ"] = if Utils::Platforms.really_windows?
                Utils::WinTZ.calculate(timezone)
              else
                timezone
              end
end
```

###
  
    .**sites**  ⇒ Object 
  

  

  

  
    

Public: An array of sites

Returns the Jekyll sites created.

```

163
164
165
```

```
# File 'lib/jekyll.rb', line 163

def sites
  @sites ||= []
end
```
