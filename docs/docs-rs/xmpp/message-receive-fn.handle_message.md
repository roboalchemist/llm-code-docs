xmpp::message::receive

# Function handle_message

Source

```
pub async fn handle_message<C: ServerConnector>(
    agent: &mut Agent<C>,
    message: Message,
) -> Vec<Event>
```
