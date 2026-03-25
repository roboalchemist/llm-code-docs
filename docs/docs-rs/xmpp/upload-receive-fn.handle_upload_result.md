xmpp::upload::receive

# Function handle_upload_result

Source

```
pub async fn handle_upload_result<C: ServerConnector>(
    from: &Jid,
    iqid: String,
    elem: Element,
    agent: &mut Agent<C>,
) -> impl IntoIterator<Item = Event>
```
