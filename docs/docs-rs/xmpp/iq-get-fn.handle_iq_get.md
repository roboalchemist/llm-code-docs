xmpp::iq::get

# Function handle_iq_get

Source

```
pub async fn handle_iq_get<C: ServerConnector>(
    agent: &mut Agent<C>,
    _events: &mut Vec<Event>,
    from: Jid,
    _to: Option<Jid>,
    id: String,
    payload: Element,
)
```
