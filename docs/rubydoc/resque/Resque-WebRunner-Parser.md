# Class: Resque::WebRunner::Parser
  
  
  

  
  
    Inherits:
    
      OptionParser
      
        

          
- Object
          
            
- OptionParser
          
            
- Resque::WebRunner::Parser
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/web_runner.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**command**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute command.

  

    
      
- 
  
    
      #**options**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute options.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**boolean_option**(*argv)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(app_name)  ⇒ Parser 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Parser.

  

      
        
- 
  
    
      #**string_option**(*argv)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(app_name)  ⇒ Parser 
  

  

  

  
    

Returns a new instance of Parser.

  

  

  
    
      

```

333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 333

def initialize(app_name)
  super("", 24, '  ')
  self.banner = "Usage: #{app_name} [options]"

  @options = {}
  basename = app_name.gsub(/\W+/, "_")
  on('-K', "--kill", "kill the running process and exit") { @command = :kill }
  on('-S', "--status", "display the current running PID and URL then quit") { @command = :status }
  string_option("-s", "--server SERVER", "serve using SERVER (thin/mongrel/webrick)", :rack_handler)
  string_option("-o", "--host HOST", "listen on HOST (default: #{HOST})", :host)
  string_option("-p", "--port PORT", "use PORT (default: #{PORT})", :port)
  on("-x", "--no-proxy", "ignore env proxy settings (e.g. http_proxy)") { opts[:no_proxy] = true }
  boolean_option("-F", "--foreground", "don't daemonize, run in the foreground", :foreground)
  boolean_option("-L", "--no-launch", "don't launch the browser", :skip_launch)
  boolean_option('-d', "--debug", "raise the log level to :debug (default: :info)", :debug)
  string_option("--app-dir APP_DIR", "set the app dir where files are stored (default: ~/#{basename}/)", :app_dir)
  string_option("-P", "--pid-file PID_FILE", "set the path to the pid file (default: app_dir/#{basename}.pid)", :pid_file)
  string_option("--log-file LOG_FILE", "set the path to the log file (default: app_dir/#{basename}.log)", :log_file)
  string_option("--url-file URL_FILE", "set the path to the URL file (default: app_dir/#{basename}.url)", :url_file)
  string_option('-N NAMESPACE', "--namespace NAMESPACE", "set the Redis namespace", :redis_namespace)
  string_option('-r redis-connection', "--redis redis-connection", "set the Redis connection string", :redis_conf)
  string_option('-a url-prefix', "--append url-prefix", "set reverse_proxy friendly prefix to links", :url_prefix)
  separator ""
  separator "Common options:"
  on_tail("-h", "--help", "Show this message") { @command = :help }
  on_tail("--version", "Show version") { @command = :version }
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**command**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute command.

  

  

  
    
      

```

331
332
333
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 331

def command
  @command
end
```

    
  

    
      
      
      
  
### 
  
    #**options**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute options.

  

  

  
    
      

```

331
332
333
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 331

def options
  @options
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**boolean_option**(*argv)  ⇒ Object 
  

  

  

  
    
      

```

361
362
363
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 361

def boolean_option(*argv)
  k = argv.pop; on(*argv) { options[k] = true }
end
```

    
  

    
      
  
### 
  
    #**string_option**(*argv)  ⇒ Object 
  

  

  

  
    
      

```

365
366
367
```

    
    
      

```
# File 'lib/resque/web_runner.rb', line 365

def string_option(*argv)
  k = argv.pop; on(*argv) { |value| options[k] = value }
end
```