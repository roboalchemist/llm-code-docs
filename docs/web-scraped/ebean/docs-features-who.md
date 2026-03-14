# Source: https://ebean.io/docs/features/who

Title: Who | Ebean

URL Source: https://ebean.io/docs/features/who

Markdown Content:
Who Created/Who Modified
------------------------

A common scenario in application is to mark entities with the Id of the user who created that entity and who last modified that entity.

Ebean provides a convenient way to do this via the `io.ebean.config.CurrentUserProvider` interface that you can implement.

The interface only specifies a single method `Object currentUser();` which will return your typical entity identifier: `Long, String or UUID`

Notice that Ebean instantiates the `CurrentUserProvider` by means of creating a new instance.

#### Example Implementation

This implementation does not work, it's just to provide an idea

/**
 * Returns the current user typically from a Thread local or similar context.
 */
public class MyCurrentUserProvider implements CurrentUserProvider {

  @Override
  public Object currentUser() {
    // Here you get the user id, from some kind of static
    // context access (session information, thread local, etc..)
    return someContext.getId();
  }
}

### Activation

In order to tell ebean which class implements the interface in your `application.properties` file we need to set the following property: `ebean.currentUserProvider=org.app.MyCurrentUserProvider`
