xmpp::muc::room

# Function leave_room

Source

```
pub async fn leave_room<C: ServerConnector>(
    agent: &mut Agent<C>,
    room_jid: BareJid,
    nickname: RoomNick,
    lang: impl Into<String>,
    status: impl Into<String>,
)
```
