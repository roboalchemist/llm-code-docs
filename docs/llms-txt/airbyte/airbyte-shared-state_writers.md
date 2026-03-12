# Source: https://docs.airbyte.com/developers/pyairbyte/reference/airbyte/shared/airbyte-shared-state_writers.md

# Module airbyte.shared.state\_writers

Copy Page

State writer implementation.

## Classes[​](#classes "Direct link to Classes")

`NoOpStateWriter()` : A state writer that does not write state artifacts.

Even though state messages are not sent anywhere, they are still stored in memory and can be accessed using the `state_message_artifacts` property and other methods inherited from the `StateProviderBase` class

Initialize the state writer.

### Ancestors (in MRO)[​](#ancestors-in-mro "Direct link to Ancestors (in MRO)")

* airbyte.shared.state\_writers.StateWriterBase
* airbyte.shared.state\_providers.StateProviderBase
* abc.ABC

`StateWriterBase()` : A class to write state artifacts.

This class is used to write state artifacts to a state store. It also serves as a provider of cached state artifacts.

Initialize the state writer.

### Ancestors (in MRO)[​](#ancestors-in-mro-1 "Direct link to Ancestors (in MRO)")

* airbyte.shared.state\_providers.StateProviderBase
* abc.ABC

### Descendants[​](#descendants "Direct link to Descendants")

* airbyte.caches.\_state\_backend.SqlStateWriter
* airbyte.shared.state\_writers.NoOpStateWriter
* airbyte.shared.state\_writers.StdOutStateWriter

### Methods[​](#methods "Direct link to Methods")

`write_state(self, state_message: AirbyteStateMessage) ‑> None` : Save or 'write' a state artifact.

This method is final and should not be overridden. Subclasses should instead overwrite the `_write_state` method.

`StdOutStateWriter()` : A state writer that writes state artifacts to stdout.

This is useful when we want PyAirbyte to behave like a "Destination" in the Airbyte protocol.

Initialize the state writer.

### Ancestors (in MRO)[​](#ancestors-in-mro-2 "Direct link to Ancestors (in MRO)")

* airbyte.shared.state\_writers.StateWriterBase
* airbyte.shared.state\_providers.StateProviderBase
* abc.ABC
