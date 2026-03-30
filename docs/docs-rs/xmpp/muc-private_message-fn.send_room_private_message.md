xmpp::muc::private_message

# Function send_room_private_message

Source

```
pub async fn send_room_private_message<C: ServerConnector>(
    agent: &mut Agent<C>,
    room: BareJid,
    recipient: RoomNick,
    lang: &str,
    text: &str,
)
```
