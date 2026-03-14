# Module: ActionCable::Channel::PeriodicTimers::ClassMethods
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/channel/periodic_timers.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**periodically**(callback_or_method_name = nil, every:, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Periodically performs a task on the channel, like updating an online user counter, polling a backend for new status messages, sending regular “heartbeat” messages, or doing some internal work and giving progress updates.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**periodically**(callback_or_method_name = nil, every:, &block)  ⇒ Object 
  

  

  

  
    

Periodically performs a task on the channel, like updating an online user counter, polling a backend for new status messages, sending regular “heartbeat” messages, or doing some internal work and giving progress updates.

Pass a method name or lambda argument or provide a block to call. Specify the calling period in seconds using the `every:` keyword argument.

```
periodically :transmit_progress, every: 5.seconds

periodically every: 3.minutes do
  transmit action: :update_count, count: current_count
end

```

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/action_cable/channel/periodic_timers.rb', line 31

def periodically(callback_or_method_name = nil, every:, &block)
  callback =
    if block_given?
      raise ArgumentError, "Pass a block or provide a callback arg, not both" if callback_or_method_name
      block
    else
      case callback_or_method_name
      when Proc
        callback_or_method_name
      when Symbol
        -> { __send__ callback_or_method_name }
      else
        raise ArgumentError, "Expected a Symbol method name or a Proc, got #{callback_or_method_name.inspect}"
      end
    end

  unless every.kind_of?(Numeric) && every > 0
    raise ArgumentError, "Expected every: to be a positive number of seconds, got #{every.inspect}"
  end

  self.periodic_timers += [[ callback, every: every ]]
end
```