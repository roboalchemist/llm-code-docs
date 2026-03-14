# Class: Pod::Source::Manager
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::Source::Manager
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/sources_manager.rb
  
  

  
    
## 
      Updating Sources
      collapse
    

    

      
        
- 
  
    
      #**add_source**(source)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Adds the provided source to the list of sources.

  

      
        
- 
  
    
      #**update**(source_name = nil, show_output = false)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Updates the local clone of the spec-repo with the given name or of all the git repos if the name is omitted.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**cdn_url?**(url)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Determines whether `url` is a CocoaPods CDN URL.

  

      
        
- 
  
    
      #**create_source_with_url**(url)  ⇒ Source 
    

    
  
  
  
  
  
  
  
  

  
    

Adds the source whose Source#url is equal to `url`, in a manner similarly to ‘pod repo add` if it is not found.

  

      
        
- 
  
    
      #**find_or_create_source_with_url**(url)  ⇒ Source 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the source whose Source#url is equal to `url`, adding the repo in a manner similarly to ‘pod repo add` if it is not found.

  

      
        
- 
  
    
      #**search_index_path**  ⇒ Pathname 
    

    
  
  
  
  
  
  
  
  

  
    

The path where the search index should be stored.

  

      
        
- 
  
    
      #**source_with_name_or_url**(name_or_url)  ⇒ Source 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the source whose Source#name or Source#url is equal to the given `name_or_url`.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_source**(source)  ⇒ Object 
  

  

  

  
    

Adds the provided source to the list of sources

  

  

Parameters:

  
    
- 
      
        source
      
      
        (Source)
      
      
      
        —
        

the source to add

      
    
  

  
    
      

```

158
159
160
```

    
    
      

```
# File 'lib/cocoapods/sources_manager.rb', line 158

def add_source(source)
  all << source unless all.any? { |s| s.url == source || s.name == source.name }
end

```

    
  

    
      
  
### 
  
    #**cdn_url?**(url)  ⇒ Boolean 
  

  

  

  
    

Determines whether `url` is a CocoaPods CDN URL.

  

  

Parameters:

  
    
- 
      
        url
      
      
        (String)
      
      
      
        —
        

The URL of the source.

      
    
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

whether `url` is a CocoaPods CDN URL,

      
    
  

  
    
      

```

73
74
75
76
77
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
```

    
    
      

```
# File 'lib/cocoapods/sources_manager.rb', line 73

def cdn_url?(url)
  return false unless url =~ %r{^https?:\/\/}

  uri_options = {}

  netrc_info = Netrc.read
  uri = URI.parse(url)
  return false unless uri.userinfo.nil?

  netrc_host = uri.host
  credentials = netrc_info[netrc_host]
  uri_options[:http_basic_authentication] = credentials if credentials

  response = OpenURI.open_uri(url.chomp('/') + '/CocoaPods-version.yml', uri_options)
  response_hash = YAML.load(response.read) # rubocop:disable Security/YAMLLoad
  response_hash.is_a?(Hash) && !Source::Metadata.new(response_hash).latest_cocoapods_version.nil?
rescue Psych::SyntaxError, ::OpenURI::HTTPError, SocketError
  return false
rescue => e
  raise Informative, "Couldn't determine repo type for URL: `#{url}`: #{e}"
end

```

    
  

    
      
  
### 
  
    #**create_source_with_url**(url)  ⇒ Source 
  

  

  

  
    

Adds the source whose Source#url is equal to `url`, in a manner similarly to ‘pod repo add` if it is not found.

  

  

Parameters:

  
    
- 
      
        url
      
      
        (String)
      
      
      
        —
        

The URL of the source.

      
    
  

Returns:

  
    
- 
      
      
        (Source)
      
      
      
        —
        

The source whose Source#url is equal to `url`,

      
    
  

Raises:

  
    
- 
      
      
        
      
      
      
        
        

If no source with the given `url` could be created,

      
    
  

  
    
      

```

35
36
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
```

    
    
      

```
# File 'lib/cocoapods/sources_manager.rb', line 35

def create_source_with_url(url)
  name = name_for_url(url)
  is_cdn = cdn_url?(url)

  # Hack to ensure that `repo add` output is shown.
  previous_title_level = UI.title_level
  UI.title_level = 0

  begin
    if is_cdn
      Command::Repo::AddCDN.parse([name, url]).run
    else
      Command::Repo::Add.parse([name, url]).run
    end
  rescue Informative => e
    message = "Unable to add a source with url `#{url}` " \
      "named `#{name}`.\n"
    message << "(#{e})\n" if Config.instance.verbose?
    message << 'You can try adding it manually in ' \
      "`#{Config.instance.repos_dir}` or via `pod repo add`."
    raise Informative, message
  ensure
    UI.title_level = previous_title_level
  end
  source = source_with_url(url)

  raise "Unable to create a source with URL #{url}" unless source

  source
end

```

    
  

    
      
  
### 
  
    #**find_or_create_source_with_url**(url)  ⇒ Source 
  

  

  

  
    

Returns the source whose Source#url is equal to `url`, adding the repo in a manner similarly to ‘pod repo add` if it is not found.

  

  

Parameters:

  
    
- 
      
        url
      
      
        (String)
      
      
      
        —
        

The URL of the source.

      
    
  

Returns:

  
    
- 
      
      
        (Source)
      
      
      
        —
        

The source whose Source#url is equal to `url`,

      
    
  

Raises:

  
    
- 
      
      
        
      
      
      
        
        

If no source with the given `url` could be created,

      
    
  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/cocoapods/sources_manager.rb', line 21

def find_or_create_source_with_url(url)
  source_with_url(url) || create_source_with_url(url)
end

```

    
  

    
      
  
### 
  
    #**search_index_path**  ⇒ Pathname 
  

  

  

  
    

Returns The path where the search index should be stored.

  

  

Returns:

  
    
- 
      
      
        (Pathname)
      
      
      
        —
        

The path where the search index should be stored.

      
    
  

  
    
      

```

111
112
113
```

    
    
      

```
# File 'lib/cocoapods/sources_manager.rb', line 111

def search_index_path
  @search_index_path ||= Config.instance.search_index_file
end

```

    
  

    
      
  
### 
  
    #**source_with_name_or_url**(name_or_url)  ⇒ Source 
  

  

  

  
    

Returns the source whose Source#name or Source#url is equal to the given `name_or_url`.

  

  

Parameters:

  
    
- 
      
        name_or_url
      
      
        (String)
      
      
      
        —
        

The name or the URL of the source.

      
    
  

Returns:

  
    
- 
      
      
        (Source)
      
      
      
        —
        

The source whose Source#name or Source#url is equal to the given `name_or_url`.

      
    
  

  
    
      

```

104
105
106
107
```

    
    
      

```
# File 'lib/cocoapods/sources_manager.rb', line 104

def source_with_name_or_url(name_or_url)
  all.find { |s| s.name == name_or_url } ||
    find_or_create_source_with_url(name_or_url)
end

```

    
  

    
      
  
### 
  
    #**update**(source_name = nil, show_output = false)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Updates the local clone of the spec-repo with the given name or of all the git repos if the name is omitted.

  

  

Parameters:

  
    
- 
      
        source_name
      
      
        (String)
      
      
        *(defaults to: nil)*
      
      
    
  
    
- 
      
        show_output
      
      
        (Boolean)
      
      
        *(defaults to: false)*
      
      
    
  

  
    
      

```

126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
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
```

    
    
      

```
# File 'lib/cocoapods/sources_manager.rb', line 126

def update(source_name = nil, show_output = false)
  if source_name
    sources = [updateable_source_named(source_name)]
  else
    sources = updateable_sources
  end

  changed_spec_paths = {}

  # Do not perform an update if the repos dir has not been setup yet.
  return unless repos_dir.exist?

  # Create the Spec_Lock file if needed and lock it so that concurrent
  # repo updates do not cause each other to fail
  File.open("#{repos_dir}/Spec_Lock", File::CREAT) do |f|
    f.flock(File::LOCK_EX)
    sources.each do |source|
      UI.section "Updating spec repo `#{source.name}`" do
        changed_source_paths = source.update(show_output)
        changed_spec_paths[source] = changed_source_paths if changed_source_paths.count > 0
        source.verify_compatibility!
      end
    end
  end
  # Perform search index update operation in background.
  update_search_index_if_needed_in_background(changed_spec_paths)
end

```