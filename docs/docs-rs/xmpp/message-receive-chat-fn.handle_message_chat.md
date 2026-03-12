xmpp::message::receive::chat

# Function handle_message_chat

Source

```
pub async fn handle_message_chat<C: ServerConnector>(
    agent: &mut Agent<C>,
    events: &mut Vec<Event>,
    from: Jid,
    message: &Message,
    time_info: StanzaTimeInfo,
)
```
