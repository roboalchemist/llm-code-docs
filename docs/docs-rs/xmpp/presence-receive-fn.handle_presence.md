xmpp::presence::receive

# Function handle_presence

Source

```
pub async fn handle_presence<C: ServerConnector>(
    _agent: &mut Agent<C>,
    presence: Presence,
) -> Vec<Event>
```
