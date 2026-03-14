xmpp::disco

# Function handle_disco_info_result

Source

```
pub async fn handle_disco_info_result<C: ServerConnector>(
    agent: &mut Agent<C>,
    disco: DiscoInfoResult,
    from: Jid,
)
```
