# Module: WebsocketRails::SpecHelpers
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/spec_helpers/matchers/route_matchers.rb,

  lib/spec_helpers/matchers/trigger_matchers.rb

  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**actual_data_for_spec_message**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**actual_for_spec_message**(event, success)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**compare_trigger_data**(event, data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**expected_data_for_spec_message**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**verify_route**(event, target, non_exclusive)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**verify_trigger**(event, data, success)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**actual_data_for_spec_message**(data)  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/spec_helpers/matchers/trigger_matchers.rb', line 25

def self.actual_data_for_spec_message(data)
  data ? "with data #{data}": 'with no data'
end
```

    
  

    
      
  
### 
  
    .**actual_for_spec_message**(event, success)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/spec_helpers/matchers/trigger_matchers.rb', line 29

def self.actual_for_spec_message(event, success)
  if event.triggered?
    if success.nil?
      "triggered message #{actual_data_for_spec_message(event.data)}"
    else
      "triggered #{event.success ? 'a success' : 'a failure' } message #{actual_data_for_spec_message(event.data)}"
    end
  else
    'did not trigger any message'
  end
end
```

    
  

    
      
  
### 
  
    .**compare_trigger_data**(event, data)  ⇒ Object 
  

  

  

  
    
      

```

5
6
7
8
9
10
```

    
    
      

```
# File 'lib/spec_helpers/matchers/trigger_matchers.rb', line 5

def self.compare_trigger_data(event, data)
  return true if data.nil?
  return true if data == :any and event.data
  return true if data == :nil and event.data.nil?
  data.eql? event.data
end
```

    
  

    
      
  
### 
  
    .**expected_data_for_spec_message**(data)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/spec_helpers/matchers/trigger_matchers.rb', line 12

def self.expected_data_for_spec_message(data)
  case data
    when nil
      ''
    when :nil
      ' with no data'
    when :any
      ' with some data'
    else
      " with data #{data}"
  end
end
```

    
  

    
      
  
### 
  
    .**verify_route**(event, target, non_exclusive)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (ArgumentError)
      
      
      
    
  

  
    
      

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
19
20
```

    
    
      

```
# File 'lib/spec_helpers/matchers/route_matchers.rb', line 5

def self.verify_route(event, target, non_exclusive)

  raise ArgumentError, 'event must be of type SpecHelperEvent' unless event.is_a? WebsocketRails::SpecHelperEvent
  target_class, target_method = WebsocketRails::TargetValidator.validate_target target

  result = false
  no_of_routes = 0
  event.dispatcher.event_map.routes_for event do |controller_class, method|
    no_of_routes += 1
    controller = controller_class.new
    if controller.class == target_class and method == target_method
      result = true
    end
  end
  result and (non_exclusive or no_of_routes == 1)
end
```

    
  

    
      
  
### 
  
    .**verify_trigger**(event, data, success)  ⇒ Object 
  

  

  

  
    
      

```

41
42
43
44
45
```

    
    
      

```
# File 'lib/spec_helpers/matchers/trigger_matchers.rb', line 41

def self.verify_trigger(event, data, success)
  return false unless event.triggered?
  return false unless compare_trigger_data(event, data)
  success.nil? || success == event.success
end
```