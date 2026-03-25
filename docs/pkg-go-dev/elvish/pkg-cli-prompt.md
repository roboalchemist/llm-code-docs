### Overview ¶

Package prompt provides an implementation of the cli.Prompt interface.

### Index ¶

-
          type Config

-
          type Prompt

-

-
            func New(cfg Config) *Prompt

-

-
            func (p *Prompt) Get() ui.Text

-
            func (p *Prompt) LateUpdates() <-chan struct{}

-
            func (p *Prompt) Trigger(force bool)

### Constants ¶

This section is empty.

### Variables ¶

This section is empty.

### Functions ¶

This section is empty.

### Types ¶

####

      type Config ¶
  
    
  

    
    
      

```
type Config struct {
 // The function that computes the prompt.
 Compute func() ui.Text
 // Function to transform stale prompts.
 StaleTransform func(ui.Text) ui.Text
 // Threshold for a prompt to be considered as stale.
 StaleThreshold func() time.Duration
 // How eager the prompt should be updated. When >= 5, updated when directory
 // is changed. When >= 10, always update. Default is 5.
 Eagerness func() int
}
```

Config keeps configurations for the prompt.

####

      type Prompt ¶
  
    
  

    
    
      

```
type Prompt struct {
 // contains filtered or unexported fields
}
```

Prompt implements a prompt that is executed asynchronously.

####

      func New ¶
  
    
  

    
    
      

```
func New(cfg Config) *Prompt
```

New makes a new prompt.

####

      func (*Prompt) Get ¶
  
    
  

    
    
      

```
func (p *Prompt) Get() ui.Text
```

Get returns the current content of the prompt.

####

      func (*Prompt) LateUpdates ¶
  
    
  

    
    
      

```
func (p *Prompt) LateUpdates() <-chan struct{}
```

LateUpdates returns a channel on which late updates are made available.

####

      func (*Prompt) Trigger ¶
  
    
  

    
    
      

```
func (p *Prompt) Trigger(force bool)
```

Trigger triggers an update to the prompt.
