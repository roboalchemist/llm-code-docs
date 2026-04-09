# Module: Resque::ServerHelper
  
  
  

  

  
  
  
  
  
      Includes:
      Rack::Utils
  
  
  

  

  
  
    Defined in:
    lib/resque/server_helper.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**class_if_current**(path = '')  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**current_page**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**current_section**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**failed_class_counts**(queue = )  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**failed_date_format**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

failed.erb helpers#.

  

      
        
- 
  
    
      #**failed_end_at**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**failed_multiple_queues?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**failed_order**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**failed_per_page**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**failed_size**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**failed_start_at**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**page_entries_info**(start, stop, size, name = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**partial**(template, local_vars = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**partial?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**path_prefix**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**poll**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**redis_get_size**(key)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**redis_get_value_as_array**(key, start = 0)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**show_args**(args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**tab**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**tabs**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**url_path**(*path_parts)  ⇒ Object 
    

    
      (also: #u)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**url_prefix**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**worker_hosts**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**worker_hosts!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**class_if_current**(path = '')  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 25

def class_if_current(path = '')
  'class="current"' if current_page[0, path.size] == path
end
```

    
  

    
      
  
### 
  
    #**current_page**  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 12

def current_page
  url_path request.path_info.sub('/','')
end
```

    
  

    
      
  
### 
  
    #**current_section**  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 8

def current_section
  url_path request.path_info.sub('/','').split('/')[0].downcase
end
```

    
  

    
      
  
### 
  
    #**failed_class_counts**(queue = )  ⇒ Object 
  

  

  

  
    
      

```

163
164
165
166
167
168
169
170
171
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 163

def failed_class_counts(queue = params[:queue])
  classes = Hash.new(0)
  Resque::Failure.each(0, Resque::Failure.count(queue), queue) do |_, item|
    class_name = item['payload']['class'] if item['payload']
    class_name ||= "nil"
    classes[class_name] += 1
  end
  classes
end
```

    
  

    
      
  
### 
  
    #**failed_date_format**  ⇒ Object 
  

  

  

  
    

failed.erb helpers#

  

  

  
    
      

```

124
125
126
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 124

def failed_date_format
  "%Y/%m/%d %T %z"
end
```

    
  

    
      
  
### 
  
    #**failed_end_at**  ⇒ Object 
  

  

  

  
    
      

```

151
152
153
154
155
156
157
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 151

def failed_end_at
  if failed_start_at + failed_per_page > failed_size
    failed_size
  else
    failed_start_at  + failed_per_page - 1
  end
end
```

    
  

    
      
  
### 
  
    #**failed_multiple_queues?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

128
129
130
131
132
133
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 128

def failed_multiple_queues?
  return @multiple_failed_queues if defined?(@multiple_failed_queues)

  @multiple_failed_queues = Resque::Failure.queues.size > 1 ||
    (defined?(Resque::Failure::RedisMultiQueue) && Resque::Failure.backend == Resque::Failure::RedisMultiQueue)
end
```

    
  

    
      
  
### 
  
    #**failed_order**  ⇒ Object 
  

  

  

  
    
      

```

159
160
161
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 159

def failed_order
  params[:order] || 'desc'
end
```

    
  

    
      
  
### 
  
    #**failed_per_page**  ⇒ Object 
  

  

  

  
    
      

```

139
140
141
142
143
144
145
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 139

def failed_per_page
  @failed_per_page = if params[:class]
    failed_size
  else
    20
  end
end
```

    
  

    
      
  
### 
  
    #**failed_size**  ⇒ Object 
  

  

  

  
    
      

```

135
136
137
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 135

def failed_size
  @failed_size ||= Resque::Failure.count(params[:queue], params[:class])
end
```

    
  

    
      
  
### 
  
    #**failed_start_at**  ⇒ Object 
  

  

  

  
    
      

```

147
148
149
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 147

def failed_start_at
  params[:start].to_i
end
```

    
  

    
      
  
### 
  
    #**page_entries_info**(start, stop, size, name = nil)  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/resque/server_helper.rb', line 173

def page_entries_info(start, stop, size, name = nil)
  if size == 0
    name ? "No #{name}s" : '<b>0</b>'
  elsif size == 1
    'Showing <b>1</b>' + (name ? " #{name}" : '')
  elsif size > failed_per_page
    "Showing #{start}-#{stop} of <b>#{size}</b>" + (name ? " #{name}s" : '')
  else
    "Showing #{start} to <b>#{size - 1}</b>" + (name ? " #{name}s" : '')
  end
end
```

    
  

    
      
  
### 
  
    #**partial**(template, local_vars = {})  ⇒ Object 
  

  

  

  
    
      

```

104
105
106
107
108
109
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 104

def partial(template, local_vars = {})
  @partial = true
  erb(template.to_sym, {:layout => false}, local_vars)
ensure
  @partial = false
end
```

    
  

    
      
  
### 
  
    #**partial?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

100
101
102
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 100

def partial?
  @partial
end
```

    
  

    
      
  
### 
  
    #**path_prefix**  ⇒ Object 
  

  

  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 21

def path_prefix
  request.env['SCRIPT_NAME']
end
```

    
  

    
      
  
### 
  
    #**poll**  ⇒ Object 
  

  

  

  
    
      

```

111
112
113
114
115
116
117
118
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 111

def poll
  if defined?(@polling) && @polling
    text = "Last Updated: #{Time.now.strftime("%H:%M:%S")}"
  else
    text = "<a href='#{u(request.path_info)}.poll' rel='poll'>Live Poll!!</a>"
  end
  "<p class='poll'>#{text}</p>"
end
```

    
  

    
      
  
### 
  
    #**redis_get_size**(key)  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/resque/server_helper.rb', line 43

def redis_get_size(key)
  case Resque.redis.type(key)
  when 'none'
    0
  when 'hash'
    Resque.redis.hlen(key)
  when 'list'
    Resque.redis.llen(key)
  when 'set'
    Resque.redis.scard(key)
  when 'string'
    Resque.redis.get(key).length
  when 'zset'
    Resque.redis.zcard(key)
  end
end
```

    
  

    
      
  
### 
  
    #**redis_get_value_as_array**(key, start = 0)  ⇒ Object 
  

  

  

  
    
      

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
74
75
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 60

def redis_get_value_as_array(key, start=0)
  case Resque.redis.type(key)
  when 'none'
    []
  when 'hash'
    Resque.redis.hgetall(key).to_a[start..(start + 20)]
  when 'list'
    Resque.redis.lrange(key, start, start + 20)
  when 'set'
    Resque.redis.smembers(key)[start..(start + 20)]
  when 'string'
    [Resque.redis.get(key)]
  when 'zset'
    Resque.redis.zrange(key, start, start + 20)
  end
end
```

    
  

    
      
  
### 
  
    #**show_args**(args)  ⇒ Object 
  

  

  

  
    
      

```

77
78
79
80
81
82
83
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 77

def show_args(args)
  Array(args).map do |a|
    a.to_yaml
  end.join("\n")
rescue
  args.to_s
end
```

    
  

    
      
  
### 
  
    #**tab**(name)  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
32
33
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 29

def tab(name)
  dname = name.to_s.downcase
  path = url_path(dname)
  "<li #{class_if_current(path)}><a href='#{path.gsub(" ", "_")}'>#{name}</a></li>"
end
```

    
  

    
      
  
### 
  
    #**tabs**  ⇒ Object 
  

  

  

  
    
      

```

35
36
37
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 35

def tabs
  Resque::Server.tabs
end
```

    
  

    
      
  
### 
  
    #**url_path**(*path_parts)  ⇒ Object 
  

  
    Also known as:
    u
    
  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 16

def url_path(*path_parts)
  [ url_prefix, path_prefix, path_parts ].join("/").squeeze('/')
end
```

    
  

    
      
  
### 
  
    #**url_prefix**  ⇒ Object 
  

  

  

  
    
      

```

39
40
41
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 39

def url_prefix
  Resque::Server.url_prefix
end
```

    
  

    
      
  
### 
  
    #**worker_hosts**  ⇒ Object 
  

  

  

  
    
      

```

85
86
87
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 85

def worker_hosts
  @worker_hosts ||= worker_hosts!
end
```

    
  

    
      
  
### 
  
    #**worker_hosts!**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/resque/server_helper.rb', line 89

def worker_hosts!
  hosts = Hash.new { [] }

  Resque.workers.each do |worker|
    host, _ = worker.to_s.split(':')
    hosts[host] += [worker.to_s]
  end

  hosts
end
```