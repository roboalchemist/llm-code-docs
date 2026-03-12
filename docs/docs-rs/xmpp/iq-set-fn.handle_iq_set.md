xmpp::iq::set

# Function handle_iq_set

Source

```
pub async fn handle_iq_set<C: ServerConnector>(
    agent: &mut Agent<C>,
    _events: &mut Vec<Event>,
    from: Jid,
    _to: Option<Jid>,
    id: String,
    _payload: Element,
)
```
