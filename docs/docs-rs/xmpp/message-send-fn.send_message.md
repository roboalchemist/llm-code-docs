xmpp::message::send

# Function send_message

Source

```
pub async fn send_message<C: ServerConnector>(
    agent: &mut Agent<C>,
    recipient: Jid,
    type_: MessageType,
    lang: &str,
    text: &str,
)
```
