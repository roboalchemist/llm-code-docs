xmpp::iq

# Function handle_iq

Source

```
pub async fn handle_iq<C: ServerConnector>(
    agent: &mut Agent<C>,
    iq: Iq,
) -> Vec<Event>
```
