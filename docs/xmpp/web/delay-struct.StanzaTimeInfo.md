xmpp::delay

# Struct StanzaTimeInfo

Source

```
pub struct StanzaTimeInfo {
    pub received: DateTime<Utc>,
    pub delays: Vec<Delay>,
}
```

## Fields§

§`received: DateTime<Utc>`

Time information when the message was received by the library
§`delays: Vec<Delay>`

Time information claimed by the sender or an intermediary.

**Warning**: this has security implications. See XEP-0203 security section.

## Implementations§
