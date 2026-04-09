# Class: Resque::Failure::RedisMultiQueue
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- Resque::Failure::RedisMultiQueue
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/failure/redis_multi_queue.rb
  
  

## Overview

  
    

A Failure backend that stores exceptions in Redis. Very simple but works out of the box, along with support in the Resque web app.

  

  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#exception, #payload, #queue, #worker

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**all**(offset = 0, limit = 1, queue = :failed)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**clear**(queue = :failed)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**count**(queue = nil, class_name = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**data_store**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**each**(offset = 0, limit = self.count, queue = :failed, class_name = nil, order = 'desc')  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**queues**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**remove**(id, queue = :failed)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**remove_queue**(queue)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**requeue**(id, queue = :failed)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
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
  
    .**all**(offset = 0, limit = 1, queue = :failed)  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
```

    
    
      

```
# File 'lib/resque/failure/redis_multi_queue.rb', line 45

def self.all(offset = 0, limit = 1, queue = :failed)
  Resque.list_range(queue, offset, limit)
end
```

    
  

    
      
  
### 
  
    .**clear**(queue = :failed)  ⇒ Object 
  

  

  

  
    
      

```

69
70
71
72
```

    
    
      

```
# File 'lib/resque/failure/redis_multi_queue.rb', line 69

def self.clear(queue = :failed)
  queues = queue ? Array(queue) : self.queues
  queues.each { |queue| data_store.clear_failed_queue(queue) }
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
40
41
42
43
```

    
    
      

```
# File 'lib/resque/failure/redis_multi_queue.rb', line 29

def self.count(queue = nil, class_name = nil)
  if queue
    if class_name
      n = 0
      each(0, count(queue), queue, class_name) { n += 1 }
      n
    else
      data_store.num_failed(queue).to_i
    end
  else
    total = 0
    queues.each { |q| total += count(q) }
    total
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
# File 'lib/resque/failure/redis_multi_queue.rb', line 11

def self.data_store
  Resque.data_store
end
```

    
  

    
      
  
### 
  
    .**each**(offset = 0, limit = self.count, queue = :failed, class_name = nil, order = 'desc')  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/resque/failure/redis_multi_queue.rb', line 53

def self.each(offset = 0, limit = self.count, queue = :failed, class_name = nil, order = 'desc')
  items = all(offset, limit, queue)
  items = [items] unless items.is_a? Array
  reversed = false
  if order.eql? 'desc'
    items.reverse!
    reversed = true
  end
  items.each_with_index do |item, i|
    if !class_name || (item['payload'] && item['payload']['class'] == class_name)
      id = reversed ? (items.length - 1) + (offset - i) : offset + i
      yield id, item
    end
  end
end
```

    
  

    
      
  
### 
  
    .**queues**  ⇒ Object 
  

  

  

  
    
      

```

49
50
51
```

    
    
      

```
# File 'lib/resque/failure/redis_multi_queue.rb', line 49

def self.queues
  data_store.failed_queue_names(:failed_queues)
end
```

    
  

    
      
  
### 
  
    .**remove**(id, queue = :failed)  ⇒ Object 
  

  

  

  
    
      

```

81
82
83
```

    
    
      

```
# File 'lib/resque/failure/redis_multi_queue.rb', line 81

def self.remove(id, queue = :failed)
  data_store.remove_from_failed_queue(id,queue)
end
```

    
  

    
      
  
### 
  
    .**remove_queue**(queue)  ⇒ Object 
  

  

  

  
    
      

```

94
95
96
```

    
    
      

```
# File 'lib/resque/failure/redis_multi_queue.rb', line 94

def self.remove_queue(queue)
  data_store.remove_failed_queue(Resque::Failure.failure_queue_name(queue))
end
```

    
  

    
      
  
### 
  
    .**requeue**(id, queue = :failed)  ⇒ Object 
  

  

  

  
    
      

```

74
75
76
77
78
79
```

    
    
      

```
# File 'lib/resque/failure/redis_multi_queue.rb', line 74

def self.requeue(id, queue = :failed)
  item = all(id, 1, queue)
  item['retried_at'] = Time.now.strftime("%Y/%m/%d %H:%M:%S")
  data_store.update_item_in_failed_queue(id,Resque.encode(item),queue)
  Job.create(item['queue'], item['payload']['class'], *item['payload']['args'])
end
```

    
  

    
      
  
### 
  
    .**requeue_all**  ⇒ Object 
  

  

  

  
    
      

```

90
91
92
```

    
    
      

```
# File 'lib/resque/failure/redis_multi_queue.rb', line 90

def self.requeue_all
  queues.each { |queue| requeue_queue(Resque::Failure.job_queue_name(queue)) }
end
```

    
  

    
      
  
### 
  
    .**requeue_queue**(queue)  ⇒ Object 
  

  

  

  
    
      

```

85
86
87
88
```

    
    
      

```
# File 'lib/resque/failure/redis_multi_queue.rb', line 85

def self.requeue_queue(queue)
  failure_queue = Resque::Failure.failure_queue_name(queue)
  each(0, count(failure_queue), failure_queue) { |id, _| requeue(id, failure_queue) }
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
# File 'lib/resque/failure/redis_multi_queue.rb', line 7

def data_store
  Resque.data_store
end
```

    
  

    
      
  
### 
  
    #**filter_backtrace**(backtrace)  ⇒ Object 
  

  

  

  
    
      

```

98
99
100
101
```

    
    
      

```
# File 'lib/resque/failure/redis_multi_queue.rb', line 98

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
# File 'lib/resque/failure/redis_multi_queue.rb', line 15

def save
  data = {
    :failed_at => Time.now.strftime("%Y/%m/%d %H:%M:%S %Z"),
    :payload   => payload,
    :exception => exception.class.to_s,
    :error     => UTF8Util.clean(exception.to_s),
    :backtrace => filter_backtrace(Array(exception.backtrace)),
    :worker    => worker.to_s,
    :queue     => queue
  }
  data = Resque.encode(data)
  data_store.push_to_failed_queue(data,Resque::Failure.failure_queue_name(queue))
end
```