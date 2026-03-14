# Class: Resque::Failure::Redis
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- Resque::Failure::Redis
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/failure/redis.rb
  
  

## Overview

  
    

A Failure backend that stores exceptions in Redis. Very simple but works out of the box, along with support in the Resque web app.

  

  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#exception, #payload, #queue, #worker

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**all**(offset = 0, limit = 1, queue = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**check_queue**(queue)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**clear**(queue = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**count**(queue = nil, class_name = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**data_store**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**each**(offset = 0, limit = self.count, queue = :failed, class_name = nil, order = 'desc')  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**queues**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**remove**(id, queue = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**remove_queue**(queue)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**requeue**(id, queue = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**requeue_all**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**requeue_queue**(queue)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**data_store**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**filter_backtrace**(backtrace)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**save**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#initialize, #log, url

  
## Constructor Details

  
    

This class inherits a constructor from Resque::Failure::Base
  

  
    
## Class Method Details

    
      
  
### 
  
    .**all**(offset = 0, limit = 1, queue = nil)  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
48
```

    
    
      

```
# File 'lib/resque/failure/redis.rb', line 45

def self.all(offset = 0, limit = 1, queue = nil)
  check_queue(queue)
  Resque.list_range(:failed, offset, limit)
end

```

    
  

    
      
  
### 
  
    .**check_queue**(queue)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (ArgumentError)
      
      
      
    
  

  
    
      

```

117
118
119
```

    
    
      

```
# File 'lib/resque/failure/redis.rb', line 117

def self.check_queue(queue)
  raise ArgumentError, "invalid queue: #{queue}" if queue && queue.to_s != "failed"
end

```

    
  

    
      
  
### 
  
    .**clear**(queue = nil)  ⇒ Object 
  

  

  

  
    
      

```

73
74
75
76
```

    
    
      

```
# File 'lib/resque/failure/redis.rb', line 73

def self.clear(queue = nil)
  check_queue(queue)
  data_store.clear_failed_queue
end

```

    
  

    
      
  
### 
  
    .**count**(queue = nil, class_name = nil)  ⇒ Object 
  

  

  

  
    
      

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
# File 'lib/resque/failure/redis.rb', line 29

def self.count(queue = nil, class_name = nil)
  check_queue(queue)

  if class_name
    n = 0
    each(0, count(queue), queue, class_name) { n += 1 }
    n
  else
    data_store.num_failed
  end
end

```

    
  

    
      
  
### 
  
    .**data_store**  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/resque/failure/redis.rb', line 11

def self.data_store
  Resque.data_store
end

```

    
  

    
      
  
### 
  
    .**each**(offset = 0, limit = self.count, queue = :failed, class_name = nil, order = 'desc')  ⇒ Object 
  

  

  

  
    
      

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
69
70
71
```

    
    
      

```
# File 'lib/resque/failure/redis.rb', line 50

def self.each(offset = 0, limit = self.count, queue = :failed, class_name = nil, order = 'desc')
  if class_name
    original_limit = limit
    limit = count
  end
  all_items = limit == 1 ? [all(offset,limit,queue)] : Array(all(offset, limit, queue))
  reversed = false
  if order.eql? 'desc'
    all_items.reverse!
    reversed = true
  end
  all_items.each_with_index do |item, i|
    if !class_name || (item['payload'] && item['payload']['class'] == class_name && (original_limit -= 1) >= 0)
      if reversed
        id = (all_items.length - 1) + (offset - i)
      else
        id = offset + i
      end
      yield id, item
    end
  end
end

```

    
  

    
      
  
### 
  
    .**queues**  ⇒ Object 
  

  

  

  
    
      

```

41
42
43
```

    
    
      

```
# File 'lib/resque/failure/redis.rb', line 41

def self.queues
  data_store.failed_queue_names
end

```

    
  

    
      
  
### 
  
    .**remove**(id, queue = nil)  ⇒ Object 
  

  

  

  
    
      

```

86
87
88
89
```

    
    
      

```
# File 'lib/resque/failure/redis.rb', line 86

def self.remove(id, queue = nil)
  check_queue(queue)
  data_store.remove_from_failed_queue(id, queue)
end

```

    
  

    
      
  
### 
  
    .**remove_queue**(queue)  ⇒ Object 
  

  

  

  
    
      

```

105
106
107
108
109
110
111
112
113
114
115
```

    
    
      

```
# File 'lib/resque/failure/redis.rb', line 105

def self.remove_queue(queue)
  i = 0
  while job = all(i)
    if job['queue'] == queue
      # This will remove the failure from the array so do not increment the index.
      remove(i)
    else
      i += 1
    end
  end
end

```

    
  

    
      
  
### 
  
    .**requeue**(id, queue = nil)  ⇒ Object 
  

  

  

  
    
      

```

78
79
80
81
82
83
84
```

    
    
      

```
# File 'lib/resque/failure/redis.rb', line 78

def self.requeue(id, queue = nil)
  check_queue(queue)
  item = all(id)
  item['retried_at'] = UTF8Util.clean(Time.now.strftime("%Y/%m/%d %H:%M:%S %Z"))
  data_store.update_item_in_failed_queue(id,Resque.encode(item))
  Job.create(item['queue'], item['payload']['class'], *item['payload']['args'])
end

```

    
  

    
      
  
### 
  
    .**requeue_all**  ⇒ Object 
  

  

  

  
    
      

```

99
100
101
102
103
```

    
    
      

```
# File 'lib/resque/failure/redis.rb', line 99

def self.requeue_all
  count.times do |num|
    requeue(num)
  end
end

```

    
  

    
      
  
### 
  
    .**requeue_queue**(queue)  ⇒ Object 
  

  

  

  
    
      

```

91
92
93
94
95
96
97
```

    
    
      

```
# File 'lib/resque/failure/redis.rb', line 91

def self.requeue_queue(queue)
  i = 0
  while job = all(i)
     requeue(i) if job['queue'] == queue
     i += 1
  end
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**data_store**  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/resque/failure/redis.rb', line 7

def data_store
  Resque.data_store
end

```

    
  

    
      
  
### 
  
    #**filter_backtrace**(backtrace)  ⇒ Object 
  

  

  

  
    
      

```

121
122
123
124
```

    
    
      

```
# File 'lib/resque/failure/redis.rb', line 121

def filter_backtrace(backtrace)
  index = backtrace.index { |item| item.include?('/lib/resque/job.rb') }
  backtrace.first(index.to_i)
end

```

    
  

    
      
  
### 
  
    #**save**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/resque/failure/redis.rb', line 15

def save
  data = {
    :failed_at => UTF8Util.clean(Time.now.strftime("%Y/%m/%d %H:%M:%S %Z")),
    :payload   => payload,
    :exception => exception.class.to_s,
    :error     => UTF8Util.clean(exception.to_s),
    :backtrace => filter_backtrace(Array(exception.backtrace)),
    :worker    => worker.to_s,
    :queue     => queue
  }
  data = Resque.encode(data)
  data_store.push_to_failed_queue(data)
end

```