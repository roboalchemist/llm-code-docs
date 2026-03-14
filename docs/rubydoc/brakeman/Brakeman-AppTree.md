# Class: Brakeman::AppTree
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Brakeman::AppTree
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/app_tree.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        VIEW_EXTENSIONS =
          
        
        

```
%w[html.erb html.haml rhtml js.erb html.slim].join(",")
```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**root**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute root.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**from_options**(options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**controller_paths**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**exists?**(path)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**expand_path**(path)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Should only be used by Brakeman::FilePath.

  

      
        
- 
  
    
      #**file_path**(path)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a new Brakeman::FilePath.

  

      
        
- 
  
    
      #**gemspec**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(root, init_options = {})  ⇒ AppTree 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of AppTree.

  

      
        
- 
  
    
      #**initializer_paths**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**layout_exists?**(name)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**lib_paths**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**marshallable**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Call this to be able to marshall the AppTree.

  

      
        
- 
  
    
      #**model_paths**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**relative_path**(path)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Should only be used by Brakeman::FilePath Use AppTree#file_path(path).relative instead.

  

      
        
- 
  
    
      #**ruby_file_paths**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**template_paths**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(root, init_options = {})  ⇒ AppTree 
  

  

  

  
    

Returns a new instance of AppTree.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/app_tree.rb', line 60

def initialize(root, init_options = {})
  @root = root
  @project_root_path = Pathname.new(@root)
  @skip_files = init_options[:skip_files]
  @only_files = init_options[:only_files]
  @additional_libs_path = init_options[:additional_libs_path] || []
  @engine_paths = init_options[:engine_paths] || []
  @absolute_engine_paths = @engine_paths.select { |path| path.start_with?(File::SEPARATOR) }
  @relative_engine_paths = @engine_paths - @absolute_engine_paths
  @skip_vendor = init_options[:skip_vendor]
  @follow_symlinks = init_options[:follow_symlinks]
  @gemspec = nil
  @root_search_pattern = nil
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**root**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute root.

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/brakeman/app_tree.rb', line 8

def root
  @root
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**from_options**(options)  ⇒ Object 
  

  

  

  
    
      

```

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
26
27
28
```

    
    
      

```
# File 'lib/brakeman/app_tree.rb', line 10

def self.from_options(options)
  root = File.expand_path options[:app_path]

  # Convert files into Regexp for matching
  init_options = {}
  if options[:skip_files]
    init_options[:skip_files] = regex_for_paths(options[:skip_files])
  end

  if options[:only_files]
    init_options[:only_files] = regex_for_paths(options[:only_files])
  end
  init_options[:additional_libs_path] = options[:additional_libs_path]
  init_options[:engine_paths] = options[:engine_paths]
  init_options[:skip_vendor] = options[:skip_vendor]
  init_options[:follow_symlinks] = options[:follow_symlinks]

  new(root, init_options)
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**controller_paths**  ⇒ Object 
  

  

  

  
    
      

```

113
114
115
```

    
    
      

```
# File 'lib/brakeman/app_tree.rb', line 113

def controller_paths
  @controller_paths ||= prioritize_concerns(find_paths("app/**/controllers"))
end
```

    
  

    
      
  
### 
  
    #**exists?**(path)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

97
98
99
100
101
102
103
```

    
    
      

```
# File 'lib/brakeman/app_tree.rb', line 97

def exists?(path)
  if path.is_a? Brakeman::FilePath
    path.exists?
  else
    File.exist?(File.join(@root, path))
  end
end
```

    
  

    
      
  
### 
  
    #**expand_path**(path)  ⇒ Object 
  

  

  

  
    

Should only be used by Brakeman::FilePath. Use AppTree#file_path(path).absolute instead.

  

  

  
    
      

```

82
83
84
```

    
    
      

```
# File 'lib/brakeman/app_tree.rb', line 82

def expand_path(path)
  File.expand_path(path, @root)
end
```

    
  

    
      
  
### 
  
    #**file_path**(path)  ⇒ Object 
  

  

  

  
    

Create a new Brakeman::FilePath

  

  

  
    
      

```

76
77
78
```

    
    
      

```
# File 'lib/brakeman/app_tree.rb', line 76

def file_path(path)
  Brakeman::FilePath.from_app_tree(self, path)
end
```

    
  

    
      
  
### 
  
    #**gemspec**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/brakeman/app_tree.rb', line 137

def gemspec
  return @gemspec unless @gemspec.nil?

  gemspecs =  Dir.glob(File.join(@root, "*.gemspec"))

  if gemspecs.length > 1 or gemspecs.empty?
    @gemspec = false
  else
    @gemspec = file_path(File.basename(gemspecs.first))
  end
end
```

    
  

    
      
  
### 
  
    #**initializer_paths**  ⇒ Object 
  

  

  

  
    
      

```

109
110
111
```

    
    
      

```
# File 'lib/brakeman/app_tree.rb', line 109

def initializer_paths
  @initializer_paths ||= prioritize_concerns(find_paths("config/initializers"))
end
```

    
  

    
      
  
### 
  
    #**layout_exists?**(name)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

126
127
128
```

    
    
      

```
# File 'lib/brakeman/app_tree.rb', line 126

def layout_exists?(name)
  !Dir.glob("#{root_search_pattern}app/views/layouts/#{name}.html.{erb,haml,slim}").empty?
end
```

    
  

    
      
  
### 
  
    #**lib_paths**  ⇒ Object 
  

  

  

  
    
      

```

130
131
132
133
134
135
```

    
    
      

```
# File 'lib/brakeman/app_tree.rb', line 130

def lib_paths
  @lib_files ||= find_paths("lib").reject { |path| path.relative.include? "/generators/" or path.relative.include? "lib/tasks/" or path.relative.include? "lib/templates/" } +
                 find_additional_lib_paths +
                 find_helper_paths +
                 find_job_paths
end
```

    
  

    
      
  
### 
  
    #**marshallable**  ⇒ Object 
  

  

  

  
    

Call this to be able to marshall the AppTree

  

  

  
    
      

```

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
# File 'lib/brakeman/app_tree.rb', line 151

def marshallable
  @initializer_paths = @initializer_paths.to_a
  @controller_paths = @controller_paths.to_a
  @template_paths = @template_paths.to_a
  @lib_files = @file_paths.to_a

  self
end
```

    
  

    
      
  
### 
  
    #**model_paths**  ⇒ Object 
  

  

  

  
    
      

```

117
118
119
```

    
    
      

```
# File 'lib/brakeman/app_tree.rb', line 117

def model_paths
  @model_paths ||= prioritize_concerns(find_paths("app/**/models"))
end
```

    
  

    
      
  
### 
  
    #**relative_path**(path)  ⇒ Object 
  

  

  

  
    

Should only be used by Brakeman::FilePath Use AppTree#file_path(path).relative instead.

  

  

  
    
      

```

88
89
90
91
92
93
94
95
```

    
    
      

```
# File 'lib/brakeman/app_tree.rb', line 88

def relative_path(path)
  pname = Pathname.new path
  if path and not path.empty? and pname.absolute?
    pname.relative_path_from(Pathname.new(self.root)).to_s
  else
    path
  end
end
```

    
  

    
      
  
### 
  
    #**ruby_file_paths**  ⇒ Object 
  

  

  

  
    
      

```

105
106
107
```

    
    
      

```
# File 'lib/brakeman/app_tree.rb', line 105

def ruby_file_paths
  find_paths(".").uniq
end
```

    
  

    
      
  
### 
  
    #**template_paths**  ⇒ Object 
  

  

  

  
    
      

```

121
122
123
124
```

    
    
      

```
# File 'lib/brakeman/app_tree.rb', line 121

def template_paths
  @template_paths ||= find_paths(".", "*.{#{VIEW_EXTENSIONS}}") +
    find_paths(".", "*.{erb,haml,slim}").reject { |path| File.basename(path).count(".") > 1 }
end
```