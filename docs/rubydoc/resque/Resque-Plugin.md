# Module: Resque::Plugin
  
  
  

  

  
  
  
      Extended by:
      Plugin
  
  
  
  
  

  
  
    Included in:
    Plugin
  
  

  
  
    Defined in:
    lib/resque/plugin.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        LintError =
          
        
        

```
Class.new(RuntimeError)
```

      
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**after_dequeue_hooks**(job)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given an object, returns a list `after_dequeue` hook names.

  

      
        
- 
  
    
      #**after_enqueue_hooks**(job)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given an object, returns a list `after_enqueue` hook names.

  

      
        
- 
  
    
      #**after_hooks**(job)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given an object, returns a list `after_perform` hook names.

  

      
        
- 
  
    
      #**around_hooks**(job)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given an object, returns a list `around_perform` hook names.

  

      
        
- 
  
    
      #**before_dequeue_hooks**(job)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given an object, returns a list `before_dequeue` hook names.

  

      
        
- 
  
    
      #**before_enqueue_hooks**(job)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given an object, returns a list `before_enqueue` hook names.

  

      
        
- 
  
    
      #**before_hooks**(job)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given an object, returns a list `before_perform` hook names.

  

      
        
- 
  
    
      #**failure_hooks**(job)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given an object, returns a list `on_failure` hook names.

  

      
        
- 
  
    
      #**get_hook_names**(job, hook_method_prefix)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Given an object, and a method prefix, returns a list of methods prefixed with that name (hook names).

  

      
        
- 
  
    
      #**job_methods**(job)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**lint**(plugin)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Ensure that your plugin conforms to good hook naming conventions.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**after_dequeue_hooks**(job)  ⇒ Object 
  

  

  

  
    

Given an object, returns a list `after_dequeue` hook names.

  

  

  
    
      

```

69
70
71
```

    
    
      

```
# File 'lib/resque/plugin.rb', line 69

def after_dequeue_hooks(job)
  get_hook_names(job, 'after_dequeue')
end
```

    
  

    
      
  
### 
  
    #**after_enqueue_hooks**(job)  ⇒ Object 
  

  

  

  
    

Given an object, returns a list `after_enqueue` hook names.

  

  

  
    
      

```

59
60
61
```

    
    
      

```
# File 'lib/resque/plugin.rb', line 59

def after_enqueue_hooks(job)
  get_hook_names(job, 'after_enqueue')
end
```

    
  

    
      
  
### 
  
    #**after_hooks**(job)  ⇒ Object 
  

  

  

  
    

Given an object, returns a list `after_perform` hook names.

  

  

  
    
      

```

49
50
51
```

    
    
      

```
# File 'lib/resque/plugin.rb', line 49

def after_hooks(job)
  get_hook_names(job, 'after_perform')
end
```

    
  

    
      
  
### 
  
    #**around_hooks**(job)  ⇒ Object 
  

  

  

  
    

Given an object, returns a list `around_perform` hook names.

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/resque/plugin.rb', line 44

def around_hooks(job)
  get_hook_names(job, 'around_perform')
end
```

    
  

    
      
  
### 
  
    #**before_dequeue_hooks**(job)  ⇒ Object 
  

  

  

  
    

Given an object, returns a list `before_dequeue` hook names.

  

  

  
    
      

```

74
75
76
```

    
    
      

```
# File 'lib/resque/plugin.rb', line 74

def before_dequeue_hooks(job)
  get_hook_names(job, 'before_dequeue')
end
```

    
  

    
      
  
### 
  
    #**before_enqueue_hooks**(job)  ⇒ Object 
  

  

  

  
    

Given an object, returns a list `before_enqueue` hook names.

  

  

  
    
      

```

64
65
66
```

    
    
      

```
# File 'lib/resque/plugin.rb', line 64

def before_enqueue_hooks(job)
  get_hook_names(job, 'before_enqueue')
end
```

    
  

    
      
  
### 
  
    #**before_hooks**(job)  ⇒ Object 
  

  

  

  
    

Given an object, returns a list `before_perform` hook names.

  

  

  
    
      

```

39
40
41
```

    
    
      

```
# File 'lib/resque/plugin.rb', line 39

def before_hooks(job)
  get_hook_names(job, 'before_perform')
end
```

    
  

    
      
  
### 
  
    #**failure_hooks**(job)  ⇒ Object 
  

  

  

  
    

Given an object, returns a list `on_failure` hook names.

  

  

  
    
      

```

54
55
56
```

    
    
      

```
# File 'lib/resque/plugin.rb', line 54

def failure_hooks(job)
  get_hook_names(job, 'on_failure')
end
```

    
  

    
      
  
### 
  
    #**get_hook_names**(job, hook_method_prefix)  ⇒ Object 
  

  

  

  
    

Given an object, and a method prefix, returns a list of methods prefixed with that name (hook names).

  

  

  
    
      

```

33
34
35
36
```

    
    
      

```
# File 'lib/resque/plugin.rb', line 33

def get_hook_names(job, hook_method_prefix)
  methods = (job.respond_to?(:hooks) && job.hooks) || job_methods(job)
  methods.select{|m| m.start_with?(hook_method_prefix)}.sort
end
```

    
  

    
      
  
### 
  
    #**job_methods**(job)  ⇒ Object 
  

  

  

  
    
      

```

27
28
29
```

    
    
      

```
# File 'lib/resque/plugin.rb', line 27

def job_methods(job)
  @job_methods[job] ||= job.methods.collect{|m| m.to_s}
end
```

    
  

    
      
  
### 
  
    #**lint**(plugin)  ⇒ Object 
  

  

  

  
    

Ensure that your plugin conforms to good hook naming conventions.

```
Resque::Plugin.lint(MyResquePlugin)

```

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/resque/plugin.rb', line 10

def lint(plugin)
  hooks = before_hooks(plugin) + around_hooks(plugin) + after_hooks(plugin)

  hooks.each do |hook|
    if hook.to_s.end_with?("perform")
      raise LintError, "#{plugin}.#{hook} is not namespaced"
    end
  end

  failure_hooks(plugin).each do |hook|
    if hook.to_s.end_with?("failure")
      raise LintError, "#{plugin}.#{hook} is not namespaced"
    end
  end
end
```