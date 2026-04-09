# Class: StackProf::Middleware
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- StackProf::Middleware
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/stackprof/middleware.rb
  
  

  
## Class Attribute Summary collapse

  

    
      
- 
  
    
      .**enabled**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute enabled.

  

    
      
- 
  
    
      .**interval**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute interval.

  

    
      
- 
  
    
      .**metadata**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute metadata.

  

    
      
- 
  
    
      .**mode**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute mode.

  

    
      
- 
  
    
      .**path**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute path.

  

    
      
- 
  
    
      .**raw**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute raw.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**enabled?**(env)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**save**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**call**(env)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(app, options = {})  ⇒ Middleware 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Middleware.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(app, options = {})  ⇒ Middleware 
  

  

  

  
    

Returns a new instance of Middleware.

  

  

  
    
      

```

5
6
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
```

    
    
      

```
# File 'lib/stackprof/middleware.rb', line 5

def initialize(app, options = {})
  @app       = app
  @options   = options
  @num_reqs  = options[:save_every] || nil

  Middleware.mode     = options[:mode] || :cpu
  Middleware.interval = options[:interval] || 1000
  Middleware.raw      = options[:raw] || false
  Middleware.enabled  = options[:enabled]
  options[:path]      = 'tmp/' if options[:path].to_s.empty?
  Middleware.path     = options[:path]
  Middleware.metadata = options[:metadata] || {}
  at_exit{ Middleware.save } if options[:save_at_exit]
end
```

    
  

  

  
    
## Class Attribute Details

    
      
      
      
  
### 
  
    .**enabled**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute enabled.

  

  

  
    
      

```

40
41
42
```

    
    
      

```
# File 'lib/stackprof/middleware.rb', line 40

def enabled
  @enabled
end
```

    
  

    
      
      
      
  
### 
  
    .**interval**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute interval.

  

  

  
    
      

```

40
41
42
```

    
    
      

```
# File 'lib/stackprof/middleware.rb', line 40

def interval
  @interval
end
```

    
  

    
      
      
      
  
### 
  
    .**metadata**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute metadata.

  

  

  
    
      

```

40
41
42
```

    
    
      

```
# File 'lib/stackprof/middleware.rb', line 40

def metadata
  @metadata
end
```

    
  

    
      
      
      
  
### 
  
    .**mode**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute mode.

  

  

  
    
      

```

40
41
42
```

    
    
      

```
# File 'lib/stackprof/middleware.rb', line 40

def mode
  @mode
end
```

    
  

    
      
      
      
  
### 
  
    .**path**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute path.

  

  

  
    
      

```

40
41
42
```

    
    
      

```
# File 'lib/stackprof/middleware.rb', line 40

def path
  @path
end
```

    
  

    
      
      
      
  
### 
  
    .**raw**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute raw.

  

  

  
    
      

```

40
41
42
```

    
    
      

```
# File 'lib/stackprof/middleware.rb', line 40

def raw
  @raw
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**enabled?**(env)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

42
43
44
45
46
47
48
```

    
    
      

```
# File 'lib/stackprof/middleware.rb', line 42

def enabled?(env)
  if enabled.respond_to?(:call)
    enabled.call(env)
  else
    enabled
  end
end
```

    
  

    
      
  
### 
  
    .**save**  ⇒ Object 
  

  

  

  
    
      

```

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
65
66
67
68
```

    
    
      

```
# File 'lib/stackprof/middleware.rb', line 50

def save
  if results = StackProf.results
    path = Middleware.path
    is_directory = path != path.chomp('/')

    if is_directory
      filename = "stackprof-#{results[:mode]}-#{Process.pid}-#{Time.now.to_i}.dump"
    else
      filename = File.basename(path)
      path = File.dirname(path)
    end

    FileUtils.mkdir_p(path)
    File.open(File.join(path, filename), 'wb') do |f|
      f.write Marshal.dump(results)
    end
    filename
  end
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**call**(env)  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
23
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
```

    
    
      

```
# File 'lib/stackprof/middleware.rb', line 20

def call(env)
  enabled = Middleware.enabled?(env)
  StackProf.start(
    mode:     Middleware.mode,
    interval: Middleware.interval,
    raw:      Middleware.raw,
    metadata: Middleware.metadata,
  ) if enabled
  @app.call(env)
ensure
  if enabled
    StackProf.stop
    if @num_reqs && (@num_reqs-=1) == 0
      @num_reqs = @options[:save_every]
      Middleware.save
    end
  end
end
```