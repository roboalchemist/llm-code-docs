xmpp::event_loop

# Function wait_for_events

Source

```
pub async fn wait_for_events<C: ServerConnector>(
    agent: &mut Agent<C>,
) -> Option<Vec<Event>>
```
