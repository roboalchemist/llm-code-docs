xmpp::iq::result

# Function handle_iq_result

Source

```
pub async fn handle_iq_result<C: ServerConnector>(
    agent: &mut Agent<C>,
    events: &mut Vec<Event>,
    from: Jid,
    _to: Option<Jid>,
    id: String,
    payload: Element,
)
```
