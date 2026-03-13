### Index ¶

- Variables

- 
          type PublishScheduler

- 

  - 
            func NewPublishScheduler(workers int, handle func(bundle interface{})) *PublishScheduler

- 

  - 
            func (s *PublishScheduler) Add(key string, item interface{}, size int) error

  - 
            func (s *PublishScheduler) Flush()

  - 
            func (s *PublishScheduler) FlushAndStop()

  - 
            func (s *PublishScheduler) IsPaused(orderingKey string) bool

  - 
            func (s *PublishScheduler) Pause(orderingKey string)

  - 
            func (s *PublishScheduler) Resume(orderingKey string)

- 
          type ReceiveScheduler

- 

  - 
            func NewReceiveScheduler(workers int) *ReceiveScheduler

- 

  - 
            func (s *ReceiveScheduler) Add(key string, item interface{}, handle func(item interface{})) error

  - 
            func (s *ReceiveScheduler) Shutdown()

### Constants ¶

  

This section is empty.

  
### Variables ¶

  
    
      View Source
      

```
var ErrReceiveDraining error = errors.New("pubsub: receive scheduler draining")
```

    
  

ErrReceiveDraining indicates the scheduler has shutdown and is draining.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type PublishScheduler ¶
  
    
  

    
    
      

```
type PublishScheduler struct {
	// Settings passed down to each bundler that gets created.
	DelayThreshold       time.Duration
	BundleCountThreshold int
	BundleByteThreshold  int
	BundleByteLimit      int
	BufferedByteLimit    int
	// contains filtered or unexported fields
}
```

    
  

PublishScheduler is a scheduler which is designed for Pub/Sub's Publish flow.
It bundles items before handling them. All items in this PublishScheduler use
the same handler.

Each item is added with a given key. Items added to the empty string key are
handled in random order. Items added to any other key are handled
sequentially.

    
  
  
    
#### 
      func NewPublishScheduler ¶
  
    
  

    
    
      

```
func NewPublishScheduler(workers int, handle func(bundle interface{})) *PublishScheduler
```

    
  

NewPublishScheduler returns a new PublishScheduler.

The workers arg is the number of workers that will operate on the queue of
work. A reasonably large number of workers is highly recommended. If the
workers arg is 0, then a healthy default of 10 workers is used.

The scheduler does not use a parent context. If it did, canceling that
context would immediately stop the scheduler without waiting for
undelivered messages.

The scheduler should be stopped only with FlushAndStop.

  

  
    
  
  
    
#### 
      func (*PublishScheduler) Add ¶
  
    
  

    
    
      

```
func (s *PublishScheduler) Add(key string, item interface{}, size int) error
```

    
  

Add adds an item to the scheduler at a given key.

Add never blocks. Buffering happens in the scheduler's publishers. There is
no flow control.

Since ordered keys require only a single outstanding RPC at once, it is
possible to send ordered key messages to Topic.Publish (and subsequently to
PublishScheduler.Add) faster than the bundler can publish them to the
Pub/Sub service, resulting in a backed up queue of Pub/Sub bundles. Each
item in the bundler queue is a goroutine.

  

  
    
  
  
    
#### 
      func (*PublishScheduler) Flush ¶
  
    
      added in
      v1.11.0
    
  

    
    
      

```
func (s *PublishScheduler) Flush()
```

    
  

Flush waits until all bundlers are sent.

  

  
    
  
  
    
#### 
      func (*PublishScheduler) FlushAndStop ¶
  
    
  

    
    
      

```
func (s *PublishScheduler) FlushAndStop()
```

    
  

FlushAndStop begins flushing items from bundlers and from the scheduler. It
blocks until all items have been flushed.

  

  
    
  
  
    
#### 
      func (*PublishScheduler) IsPaused ¶
  
    
  

    
    
      

```
func (s *PublishScheduler) IsPaused(orderingKey string) bool
```

    
  

IsPaused checks if the bundler associated with an ordering keys is
paused.

  

  
    
  
  
    
#### 
      func (*PublishScheduler) Pause ¶
  
    
  

    
    
      

```
func (s *PublishScheduler) Pause(orderingKey string)
```

    
  

Pause pauses the bundler associated with the provided ordering key,
preventing it from accepting new messages. Any outstanding messages
that haven't been published will error. If orderingKey is empty,
this is a no-op.

  

  
    
  
  
    
#### 
      func (*PublishScheduler) Resume ¶
  
    
  

    
    
      

```
func (s *PublishScheduler) Resume(orderingKey string)
```

    
  

Resume resumes accepting message with the provided ordering key.