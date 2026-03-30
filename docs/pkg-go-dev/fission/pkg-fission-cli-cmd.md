### Index ¶

- 
        func GetClientConfig(kubeContext string) (clientcmd.ClientConfig, error)

- 
        func SetClientset(client Client)

- 
          type Client

- 

  - 
            func NewClient(opts ClientOptions) (*Client, error)

- 

  - 
            func (c *Client) SetFissionClientset(fissionClientSet versioned.Interface)

  - 
            func (c *Client) SetKubernetesClient(kubernetesClient kubernetes.Interface)

- 
          type ClientOptions

- 
          type CommandAction

- 
          type CommandActioner

- 

  - 
            func (c *CommandActioner) Client() Client

  - 
            func (c *CommandActioner) GetResourceNamespace(input cli.Input, deprecatedFlag string) (namespace, currentNS string, err error)

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func GetClientConfig ¶
  
    
      added in
      v1.18.0
    
  

    
    
      

```
func GetClientConfig(kubeContext string) (clientcmd.ClientConfig, error)
```