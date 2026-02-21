# Source: https://dramatiq.io/best_practices.html

Title: Best Practices — Dramatiq 2.0.1 documentation

URL Source: https://dramatiq.io/best_practices.html

Markdown Content:
Concurrent Actors[¶](https://dramatiq.io/best_practices.html#concurrent-actors "Link to this heading")
------------------------------------------------------------------------------------------------------

Your actor will run concurrently with other actors in the system. You need to be mindful of the impact this has on your database, any third party services you might be calling and the resources available on the systems running your workers. Additionally, you need to be mindful of data races between actors that manipulate the same objects in your database.

Retriable Actors[¶](https://dramatiq.io/best_practices.html#retriable-actors "Link to this heading")
----------------------------------------------------------------------------------------------------

Dramatiq actors may receive the same message multiple times in the event of a worker failure (hardware, network or power failure). This means that, for any given message, running your actor multiple times must be safe. This is also known as being “idempotent”.

Simple Messages[¶](https://dramatiq.io/best_practices.html#simple-messages "Link to this heading")
--------------------------------------------------------------------------------------------------

Attempting to send an actor any object that can’t be encoded to JSON by the standard `json` package will fail immediately so you’ll want to limit your actor parameters to the following object types: bool, int, float, bytes, string, list and dict.

Additionally, since messages are sent over the wire you’ll want to keep them as short as possible. For example, if you’ve got an actor that operates over `User` objects in your system, send that actor the user’s id rather than the serialized user. Or, if you have an actor that operates on a file, send the path to the file in the message, rather than the body of the file.

Error Reporting[¶](https://dramatiq.io/best_practices.html#error-reporting "Link to this heading")
--------------------------------------------------------------------------------------------------

Invariably, you’re probably going to introduce issues in production every now and then and some of those issues are going to affect your tasks. You should use an error reporting service such as [Sentry](https://sentry.io/welcome/) so you get notified of these errors as soon as they occur.
