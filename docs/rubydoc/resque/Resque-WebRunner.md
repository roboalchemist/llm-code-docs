# Class: Resque::WebRunner
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Resque::WebRunner
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/web_runner.rb
  
  

## Defined Under Namespace

  
    
  
    
      **Classes:** Parser
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        PORT =
          
        
        

```
5678
```

      
        HOST =
          
        
        

```
WINDOWS ? 'localhost' : '0.0.0.0'
```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**app**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute app.

  

    
      
- 
  
    
      #**app_name**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute app_name.

  

    
      
- 
  
    
      #**args**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute args.

  

    
      
- 
  
    
      #**filesystem_friendly_app_name**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute filesystem_friendly_app_name.

  

    
      
- 
  
    
      #**options**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute options.

  

    
      
- 
  
    
      #**port**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute port.

  

    
      
- 
  
    
      #**rack_handler**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute rack_handler.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**get_rackup_or_rack_handler**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**logger**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**logger=**(logger)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**announce_port_attempted**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**app_dir**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**before_run**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_for_running**(path = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**daemon_execute**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**daemonize!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Adapted from Rackup.

  

      
        
- 
  
    
      #**find_port**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**host**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(*runtime_args)  ⇒ WebRunner 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of WebRunner.

  

      
        
- 
  
    
      #**kill!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**launch!**(specific_url = nil, path = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**launch_path**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**load_config_file**(config_path)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Loads a config file at config_path and evals it in the context of the @app.

  

      
        
- 
  
    
      #**log_file**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**logger**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**pid_file**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**port_open?**(check_url = nil)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**run!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**start**(path = launch_path)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**status**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**uri_open**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**url**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**url_file**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**write_url**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(*runtime_args)  ⇒ WebRunner 
  

  

  

  
    

Returns a new instance of WebRunner.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 26

def initialize(*runtime_args)
  @options = runtime_args.last.is_a?(Hash) ? runtime_args.pop : {}

  self.class.logger.level = options[:debug] ? Logger::DEBUG : Logger::INFO

  @app      = Resque::Server
  @app_name = 'resque-web'
  @filesystem_friendly_app_name = @app_name.gsub(/\W+/, "_")

  @args = load_options(runtime_args)

  @rack_handler = (s = options[:rack_handler]) ? self.class.get_rackup_or_rack_handler.get(s) : setup_rack_handler

  case option_parser.command
  when :help
    puts option_parser
  when :kill
    kill!
  when :status
    status
  when :version
    puts "resque #{Resque::VERSION}"
    puts "rack #{Rack::VERSION.join('.')}"
    puts "sinatra #{Sinatra::VERSION}" if defined?(Sinatra)
  else
    before_run
    start unless options[:start] == false
  end
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**app**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute app.

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 20

def app
  @app
end
```

    
  

    
      
      
      
  
### 
  
    #**app_name**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute app_name.

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 20

def app_name
  @app_name
end
```

    
  

    
      
      
      
  
### 
  
    #**args**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute args.

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 20

def args
  @args
end
```

    
  

    
      
      
      
  
### 
  
    #**filesystem_friendly_app_name**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute filesystem_friendly_app_name.

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 20

def filesystem_friendly_app_name
  @filesystem_friendly_app_name
end
```

    
  

    
      
      
      
  
### 
  
    #**options**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute options.

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 20

def options
  @options
end
```

    
  

    
      
      
      
  
### 
  
    #**port**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute port.

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 20

def port
  @port
end
```

    
  

    
      
      
      
  
### 
  
    #**rack_handler**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute rack_handler.

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 20

def rack_handler
  @rack_handler
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**get_rackup_or_rack_handler**  ⇒ Object 
  

  

  

  
    
      

```

277
278
279
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 277

def self.get_rackup_or_rack_handler
  defined?(::Rackup::Handler) && ::Rack.release >= '3' ? ::Rackup::Handler : ::Rack::Handler
end
```

    
  

    
      
  
### 
  
    .**logger**  ⇒ Object 
  

  

  

  
    
      

```

263
264
265
266
267
268
269
270
271
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 263

def self.logger
  @logger ||= LOGGER if defined?(LOGGER)
  if !@logger
    @logger           = Logger.new(STDOUT)
    @logger.formatter = Proc.new {|s, t, n, msg| "[#{t}] #{msg}\n"}
    @logger
  end
  @logger
end
```

    
  

    
      
  
### 
  
    .**logger=**(logger)  ⇒ Object 
  

  

  

  
    
      

```

259
260
261
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 259

def self.logger=(logger)
  @logger = logger
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**announce_port_attempted**  ⇒ Object 
  

  

  

  
    
      

```

144
145
146
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 144

def announce_port_attempted
  logger.info "trying port #{port}..."
end
```

    
  

    
      
  
### 
  
    #**app_dir**  ⇒ Object 
  

  

  

  
    
      

```

64
65
66
67
68
69
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 64

def app_dir
  if !options[:app_dir] && !ENV['HOME']
    raise ArgumentError.new("nor --app-dir neither ENV['HOME'] defined")
  end
  options[:app_dir] || File.join(ENV['HOME'], filesystem_friendly_app_name)
end
```

    
  

    
      
  
### 
  
    #**before_run**  ⇒ Object 
  

  

  

  
    
      

```

91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 91

def before_run
  if (redis_conf = options[:redis_conf])
    logger.info "Using Redis connection '#{redis_conf}'"
    Resque.redis = redis_conf
  end
  if (namespace = options[:redis_namespace])
    logger.info "Using Redis namespace '#{namespace}'"
    Resque.redis.namespace = namespace
  end
  if (url_prefix = options[:url_prefix])
    logger.info "Using URL Prefix '#{url_prefix}'"
    Resque::Server.url_prefix = url_prefix
  end
  app.set(options.merge web_runner: self)
  path = (ENV['RESQUECONFIG'] || args.first)
  load_config_file(path.to_s.strip) if path
end
```

    
  

    
      
  
### 
  
    #**check_for_running**(path = nil)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 168

def check_for_running(path = nil)
  if File.exist?(pid_file) && File.exist?(url_file)
    running_url = File.read(url_file)
    if !port_open?(running_url)
      logger.warn "'#{app_name}' is already running at #{running_url}"
      launch!(running_url, path)
      exit!(1)
    end
  end
end
```

    
  

    
      
  
### 
  
    #**daemon_execute**  ⇒ Object 
  

  

  

  
    
      

```

213
214
215
216
217
218
219
220
221
222
223
224
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 213

def daemon_execute
  File.umask 0000
  FileUtils.touch log_file
  STDIN.reopen    log_file
  STDOUT.reopen   log_file, "a"
  STDERR.reopen   log_file, "a"

  logger.debug "Child Process: #{Process.pid}"

  File.open(pid_file, 'w') {|f| f.write("#{Process.pid}") }
  at_exit { delete_pid! }
end
```

    
  

    
      
  
### 
  
    #**daemonize!**  ⇒ Object 
  

  

  

  
    

Adapted from Rackup

  

  

  
    
      

```

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
208
209
210
211
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 195

def daemonize!
  if JRUBY
    # It's not a true daemon but when executed with & works like one
    thread = Thread.new {daemon_execute}
    thread.join

  elsif RUBY_VERSION < "1.9"
    logger.debug "Parent Process: #{Process.pid}"
    exit!(0) if fork
    logger.debug "Child Process: #{Process.pid}"
    daemon_execute

  else
    Process.daemon(true, true)
    daemon_execute
  end
end
```

    
  

    
      
  
### 
  
    #**find_port**  ⇒ Object 
  

  

  

  
    
      

```

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
135
136
137
138
139
140
141
142
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 125

def find_port
  if @port = options[:port]
    announce_port_attempted

    unless port_open?
      logger.warn "Port #{port} is already in use. Please try another. " +
                  "You can also omit the port flag, and we'll find one for you."
    end
  else
    @port = PORT
    announce_port_attempted

    until port_open?
      @port += 1
      announce_port_attempted
    end
  end
end
```

    
  

    
      
  
### 
  
    #**host**  ⇒ Object 
  

  

  

  
    
      

```

83
84
85
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 83

def host
  options.fetch(:host) { HOST }
end
```

    
  

    
      
  
### 
  
    #**kill!**  ⇒ Object 
  

  

  

  
    
      

```

232
233
234
235
236
237
238
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 232

def kill!
  pid = File.read(pid_file)
  logger.warn "Sending #{kill_command} to #{pid.to_i}"
  Process.kill(kill_command, pid.to_i)
rescue => e
  logger.warn "pid not found at #{pid_file} : #{e}"
end
```

    
  

    
      
  
### 
  
    #**launch!**(specific_url = nil, path = nil)  ⇒ Object 
  

  

  

  
    
      

```

226
227
228
229
230
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 226

def launch!(specific_url = nil, path = nil)
  return if options[:skip_launch]
  cmd = WINDOWS ? "start" : "open"
  system "#{cmd} #{specific_url || url}#{path}"
end
```

    
  

    
      
  
### 
  
    #**launch_path**  ⇒ Object 
  

  

  

  
    
      

```

56
57
58
59
60
61
62
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 56

def launch_path
  if options[:launch_path].respond_to?(:call)
    options[:launch_path].call(self)
  else
    options[:launch_path]
  end
end
```

    
  

    
      
  
### 
  
    #**load_config_file**(config_path)  ⇒ Object 
  

  

  

  
    

Loads a config file at config_path and evals it in the context of the @app.

  

  

  
    
      

```

251
252
253
254
255
256
257
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 251

def load_config_file(config_path)
  abort "Can not find config file at #{config_path}" if !File.readable?(config_path)
  config = File.read(config_path)
  # trim off anything after __END__
  config.sub!(/^__END__\n.*/, '')
  @app.module_eval(config)
end
```

    
  

    
      
  
### 
  
    #**log_file**  ⇒ Object 
  

  

  

  
    
      

```

79
80
81
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 79

def log_file
  options[:log_file] || File.join(app_dir, "#{filesystem_friendly_app_name}.log")
end
```

    
  

    
      
  
### 
  
    #**logger**  ⇒ Object 
  

  

  

  
    
      

```

273
274
275
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 273

def logger
  self.class.logger
end
```

    
  

    
      
  
### 
  
    #**pid_file**  ⇒ Object 
  

  

  

  
    
      

```

71
72
73
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 71

def pid_file
  options[:pid_file] || File.join(app_dir, "#{filesystem_friendly_app_name}.pid")
end
```

    
  

    
      
  
### 
  
    #**port_open?**(check_url = nil)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

148
149
150
151
152
153
154
155
156
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 148

def port_open?(check_url = nil)
  begin
    check_url ||= url
    options[:no_proxy] ? uri_open(check_url, :proxy => nil) : uri_open(check_url)
    false
  rescue Errno::ECONNREFUSED, Errno::EPERM, Errno::ETIMEDOUT
    true
  end
end
```

    
  

    
      
  
### 
  
    #**run!**  ⇒ Object 
  

  

  

  
    
      

```

179
180
181
182
183
184
185
186
187
188
189
190
191
192
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 179

def run!
  logger.info "Running with Rack handler: #{@rack_handler.inspect}"

  rack_handler.run app, :Host => host, :Port => port do |server|
    kill_commands.each do |command|
      trap(command) do
        ## Use thins' hard #stop! if available, otherwise just #stop
        server.respond_to?(:stop!) ? server.stop! : server.stop
        logger.info "'#{app_name}' received INT ... stopping"
        delete_pid!
      end
    end
  end
end
```

    
  

    
      
  
### 
  
    #**start**(path = launch_path)  ⇒ Object 
  

  

  

  
    
      

```

109
110
111
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
122
123
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 109

def start(path = launch_path)
  logger.info "Running with Windows Settings" if WINDOWS
  logger.info "Running with JRuby" if JRUBY
  logger.info "Starting '#{app_name}'..."

  check_for_running(path)
  find_port
  write_url
  launch!(url, path)
  daemonize! unless options[:foreground]
  run!
rescue RuntimeError => e
  logger.warn "There was an error starting '#{app_name}': #{e}"
  exit
end
```

    
  

    
      
  
### 
  
    #**status**  ⇒ Object 
  

  

  

  
    
      

```

240
241
242
243
244
245
246
247
248
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 240

def status
  if File.exist?(pid_file)
    logger.info "'#{app_name}' running"
    logger.info "PID #{File.read(pid_file)}"
    logger.info "URL #{File.read(url_file)}" if File.exist?(url_file)
  else
    logger.info "'#{app_name}' not running!"
  end
end
```

    
  

    
      
  
### 
  
    #**uri_open**(*args)  ⇒ Object 
  

  

  

  
    
      

```

158
159
160
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 158

def uri_open(*args)
  (RbConfig::CONFIG['ruby_version'] < '2.7') ? open(*args) : URI.open(*args)
end
```

    
  

    
      
  
### 
  
    #**url**  ⇒ Object 
  

  

  

  
    
      

```

87
88
89
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 87

def url
  "http://#{host}:#{port}"
end
```

    
  

    
      
  
### 
  
    #**url_file**  ⇒ Object 
  

  

  

  
    
      

```

75
76
77
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 75

def url_file
  options[:url_file] || File.join(app_dir, "#{filesystem_friendly_app_name}.url")
end
```

    
  

    
      
  
### 
  
    #**write_url**  ⇒ Object 
  

  

  

  
    
      

```

162
163
164
165
166
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 162

def write_url
  # Make sure app dir is setup
  FileUtils.mkdir_p(app_dir)
  File.open(url_file, 'w') {|f| f << url }
end
```