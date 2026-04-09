# Class: Rack::RubyProf
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Rack::RubyProf
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/ruby-prof/rack.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**call**(env)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(app, path: Dir.tmpdir, printers: nil, skip_paths: nil, only_paths: nil, merge_fibers: false, measure_mode: ::RubyProf::WALL_TIME, track_allocations: false, exclude_common: false, ignore_existing_threads: false, request_thread_only: false, min_percent: 1, sort_method: :total_time)  ⇒ RubyProf 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of RubyProf.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(app, path: Dir.tmpdir, printers: nil, skip_paths: nil, only_paths: nil, merge_fibers: false, measure_mode: ::RubyProf::WALL_TIME, track_allocations: false, exclude_common: false, ignore_existing_threads: false, request_thread_only: false, min_percent: 1, sort_method: :total_time)  ⇒ RubyProf 
  

  

  

  
    

Returns a new instance of RubyProf.

  

  

  
    
      

```

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
29
30
31
32
```

    
    
      

```
# File 'lib/ruby-prof/rack.rb', line 6

def initialize(app, path: Dir.tmpdir, printers: nil, skip_paths: nil,
               only_paths: nil, merge_fibers: false,
               measure_mode: ::RubyProf::WALL_TIME, track_allocations: false,
               exclude_common: false, ignore_existing_threads: false,
               request_thread_only: false, min_percent: 1,
               sort_method: :total_time)
  @app = app

  @tmpdir = path.to_s
  FileUtils.mkdir_p(@tmpdir)

  @printer_klasses = printers || {::RubyProf::FlatPrinter => 'flat.txt',
                                  ::RubyProf::GraphPrinter => 'graph.txt',
                                  ::RubyProf::GraphHtmlPrinter => 'graph.html',
                                  ::RubyProf::CallStackPrinter => 'call_stack.html'}

  @skip_paths = skip_paths || [%r{^/assets}, %r{\.(css|js|png|jpeg|jpg|gif)$}]
  @only_paths = only_paths
  @merge_fibers = merge_fibers
  @measure_mode = measure_mode
  @track_allocations = track_allocations
  @exclude_common = exclude_common
  @ignore_existing_threads = ignore_existing_threads
  @request_thread_only = request_thread_only
  @min_percent = min_percent
  @sort_method = sort_method
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**call**(env)  ⇒ Object 
  

  

  

  
    
      

```

34
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
```

    
    
      

```
# File 'lib/ruby-prof/rack.rb', line 34

def call(env)
  request = Rack::Request.new(env)

  if should_profile?(request.path)
    begin
      result = nil
      profile = ::RubyProf::Profile.profile(**profiling_options) do
        result = @app.call(env)
      end

      if @merge_fibers
        profile.merge!
      end

      path = request.path.gsub('/', '-')
      path.slice!(0)

      print(profile, path)
      result
    end
  else
    @app.call(env)
  end
end
```