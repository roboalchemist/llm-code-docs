# Source: https://support.anydesk.com/docs/url-handler

> [**Relevant for:** Admin, IT agent]
>
> [**Platform:** Windows, macOS (6.3.1+), and Linux ]

You can use URL handlers to automatically launch AnyDesk and start a remote session. It\'s particularly useful for IT administrators and support teams who manage remote access through internal portals or dashboards.

> ::: blockquote-title
> 💡 **NOTE**
> :::
>
> AnyDesk must be **installed** on your device for URL handlers to work.

------------------------------------------------------------------------

## How to use URL handlers 

You can embed AnyDesk links using standard HTML. When you click the link, AnyDesk opens and sends a connection request to the specified ID or alias.

``` 
<a href="anydesk:user@namespace">Connect to AnyDesk</a>
```

------------------------------------------------------------------------

## URL handlers by client type 

The format of the URL depends on the type of AnyDesk client you\'re using.

### Standard clients 

Use this format if you\'re using a standard AnyDesk client downloaded from the official website:

``` 
anydesk:<anydesk-id-or-alias>
```

**Example:** `anydesk:123456789`

------------------------------------------------------------------------

### Custom clients (my.anydesk I) 

#### Non-MSI custom clients 

``` 
anydesk-<prefix>:<anydesk-id-or-alias>
```

**Example:** `anydesk-abc12345:123456789`

#### MSI custom clients (Windows only) 

``` 
anydesk:AnyDesk-<prefix>_msi:<anydesk-id-or-alias>
```

**Example:** `anydesk:AnyDesk-abc12345_msi:123456789`

------------------------------------------------------------------------

### Custom clients (my.anydesk II) 

#### Non-MSI custom clients 

``` 
anydesk:AnyDesk-ad_<prefix>:<anydesk-id-or-alias>
```

**Example:** `anydesk:AnyDesk-ad_abc12345:123456789`

#### MSI custom clients (Windows only) 

``` 
anydesk:AnyDesk-ad_<prefix>_msi:<anydesk-id-or-alias>
```

**Example:** `anydesk:AnyDesk-ad_abc12345_msi:123456789`

------------------------------------------------------------------------

## Initiate sessions from my.anydesk 

You can also use this feature directly in the [my.anydesk](http://my.anydesk.com/v2):

1.  Go to the **Clients** tab.

2.  Select the client you want to connect to.

3.  Click **Connect** to launch a session using a URL handler.

> ::: blockquote-title
> 🚨 [**IMPORTANT**]
> :::
>
> URL handlers in the management console work only with the **standard AnyDesk client** downloaded from our [official website](https://anydesk.com/downloads).

------------------------------------------------------------------------

## Example use case 

If you use a web-based support dashboard, you can collect customer AnyDesk IDs through a form. These IDs can be automatically converted into clickable AnyDesk URLs. When an IT agent clicks the link, AnyDesk opens and starts the session immediately, no need to manually enter the ID.