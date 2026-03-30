xmpp::muc::room

# Function join_room

Source

```
pub async fn join_room<C: ServerConnector>(
    agent: &mut Agent<C>,
    room: BareJid,
    nick: Option<String>,
    password: Option<String>,
    lang: &str,
    status: &str,
)
```
