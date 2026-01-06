# HATEOAS: Hypermedia As The Engine Of Application State

# Source: https://en.wikipedia.org/wiki/HATEOAS, https://restfulapi.net/hateoas/, https://docs.spring.io/spring-hateoas/docs/current/reference/html/

## Overview

HATEOAS (Hypermedia As The Engine Of Application State) is a constraint of the REST (Representational State Transfer) application architecture. It is a core principle for building self-discovering REST APIs where responses contain hyperlinks to related resources, allowing clients to navigate the API dynamically without prior knowledge of the API structure.

## Background

HATEOAS is one of the six constraints defined in Roy Fielding's 2000 REST dissertation that differentiates it from other network-based architectural styles:

1. Client-Server Architecture
2. Statelessness
3. Uniform Interface
4. Cacheability
5. Layered System
6. **Code on Demand (optional)**

HATEOAS is the key component of the Uniform Interface constraint, enabling true hypermedia-driven interactions between clients and servers.

## Core Concept

In a HATEOAS-compliant API:

- **Resources are self-describing**: Each response contains information about available actions and related resources
- **Clients discover API structure dynamically**: Rather than hard-coding API endpoints, clients follow links provided in responses
- **API evolution is simplified**: The server can add, remove, or modify links without breaking clients that follow them
- **Navigation is driven by server state**: The server tells the client what actions are available, based on the current state of the resource

### Key Principle

A client should be able to navigate the API dynamically by following links in responses, similar to how a web browser navigates the internet by following hyperlinks. The server provides all necessary links for the client to discover and interact with the API.

## HATEOAS vs Traditional REST APIs

### Traditional REST API Example

```
GET /api/users/123

Response:
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com"
}
```

Clients must know in advance:
- How to get a user's posts: GET /api/users/123/posts
- How to get a user's friends: GET /api/users/123/friends
- How to update a user: PUT /api/users/123

### HATEOAS API Example

```
GET /api/users/123

Response:
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com",
  "_links": {
    "self": { "href": "/api/users/123" },
    "posts": { "href": "/api/users/123/posts" },
    "friends": { "href": "/api/users/123/friends" },
    "update": { "href": "/api/users/123", "method": "PUT" },
    "delete": { "href": "/api/users/123", "method": "DELETE" },
    "all-users": { "href": "/api/users" }
  }
}
```

Clients can discover:
- How to interact with the user resource
- Related resources and operations
- Navigation paths without prior API knowledge

## Hypermedia Formats

### HAL (Hypertext Application Language)

HAL is a simple and widely-used format for expressing hypermedia in REST APIs:

```json
{
  "_links": {
    "self": { "href": "/users/123" },
    "next": { "href": "/users/124" },
    "previous": { "href": "/users/122" },
    "all": { "href": "/users" }
  },
  "id": 123,
  "name": "John Doe"
}
```

**Characteristics:**
- Uses `_links` object for relationships
- Links have `href` (URL) and optional `title`
- Supports embedded resources via `_embedded`
- Simple and human-readable
- Widely supported across frameworks

### JSON-LD (JSON for Linking Data)

JSON-LD provides a standardized way to express linked data:

```json
{
  "@context": "https://example.com/context",
  "@id": "/users/123",
  "name": "John Doe",
  "email": "john@example.com",
  "links": [
    {
      "@rel": "next",
      "@href": "/users/124"
    },
    {
      "@rel": "previous",
      "@href": "/users/122"
    }
  ]
}
```

### Collection+JSON

Collection+JSON provides a standardized format for hypermedia-driven APIs:

```json
{
  "collection": {
    "version": "1.0",
    "href": "/users/123",
    "items": [
      {
        "href": "/users/123",
        "data": [
          { "name": "id", "value": "123" },
          { "name": "name", "value": "John Doe" }
        ],
        "links": []
      }
    ],
    "links": [
      {
        "rel": "all-users",
        "href": "/users"
      }
    ]
  }
}
```

### SIREN

SIREN is a hypermedia format that supports actions (state-changing operations):

```json
{
  "class": ["user"],
  "properties": {
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com"
  },
  "actions": [
    {
      "name": "update",
      "title": "Update User",
      "method": "PUT",
      "href": "/users/123",
      "fields": [
        { "name": "name", "type": "text" },
        { "name": "email", "type": "email" }
      ]
    },
    {
      "name": "delete",
      "title": "Delete User",
      "method": "DELETE",
      "href": "/users/123"
    }
  ],
  "links": [
    { "rel": ["self"], "href": "/users/123" },
    { "rel": ["all-users"], "href": "/users" },
    { "rel": ["friends"], "href": "/users/123/friends" }
  ]
}
```

## Benefits of HATEOAS

### 1. API Discoverability
Clients can discover available operations by examining response links. No documentation lookup needed for navigation.

### 2. Loose Coupling
Clients don't hard-code URLs. Server can change URL structure without breaking clients that follow links.

### 3. Reduced Development Friction
API consumers don't need to memorize endpoint URLs or read extensive documentation to understand how to navigate the API.

### 4. API Evolution
New operations and resources can be added without forcing all clients to update. Clients ignore unknown links.

### 5. State-Driven Navigation
The server controls what actions are available based on the current resource state. This enables workflow-like interactions.

### 6. Better Error Recovery
When links change, clients can adapt by following new links instead of failing with hard-coded URLs.

## Implementing HATEOAS

### Design Principles

1. **Include self links**: Every resource should have a link to itself
   ```json
   "_links": {
     "self": { "href": "/users/123" }
   }
   ```

2. **Provide navigation links**: Include links to parent, siblings, and related resources
   ```json
   "_links": {
     "parent": { "href": "/users" },
     "next": { "href": "/users/124" },
     "previous": { "href": "/users/122" }
   }
   ```

3. **Include action links**: For resources that support mutations, provide links with methods
   ```json
   "_links": {
     "update": { "href": "/users/123", "method": "PUT" },
     "delete": { "href": "/users/123", "method": "DELETE" }
   }
   ```

4. **Use consistent naming**: Establish conventions for link relationships (rel values)
   ```json
   "rel": ["self", "next", "previous", "all", "parent", "child"]
   ```

5. **Conditional links**: Only include links for operations that are valid in the current state
   ```json
   "_links": {
     "approve": { "href": "/orders/456/approve", "method": "POST" },  // Only if status is "pending"
     "ship": { "href": "/orders/456/ship", "method": "POST" }  // Only if status is "approved"
   }
   ```

### Example: E-commerce API with HATEOAS

#### Get a Product
```json
GET /api/products/789

{
  "id": 789,
  "name": "Wireless Mouse",
  "price": 29.99,
  "stock": 150,
  "_links": {
    "self": { "href": "/api/products/789" },
    "all-products": { "href": "/api/products" },
    "category": { "href": "/api/categories/electronics" },
    "reviews": { "href": "/api/products/789/reviews" },
    "add-to-cart": { "href": "/api/cart/items", "method": "POST" }
  }
}
```

#### Get an Order
```json
GET /api/orders/456

{
  "id": 456,
  "userId": 123,
  "status": "pending",
  "total": 99.99,
  "_links": {
    "self": { "href": "/api/orders/456" },
    "user": { "href": "/api/users/123" },
    "items": { "href": "/api/orders/456/items" },
    "approve": { "href": "/api/orders/456/approve", "method": "POST" },
    "cancel": { "href": "/api/orders/456/cancel", "method": "POST" },
    "all-orders": { "href": "/api/orders" }
  }
}
```

#### Get an Order (Shipped Status)
```json
GET /api/orders/457

{
  "id": 457,
  "userId": 124,
  "status": "shipped",
  "total": 149.99,
  "_links": {
    "self": { "href": "/api/orders/457" },
    "user": { "href": "/api/users/124" },
    "items": { "href": "/api/orders/457/items" },
    "track": { "href": "/api/orders/457/tracking" },
    "return": { "href": "/api/orders/457/return", "method": "POST" },
    "all-orders": { "href": "/api/orders" }
  }
}
```

## Implementation Frameworks

### Spring HATEOAS (Java/Spring Boot)

Spring HATEOAS provides a simple way to build HATEOAS-compliant APIs:

```java
import org.springframework.hateoas.EntityModel;
import org.springframework.hateoas.Link;
import org.springframework.hateoas.server.mvc.WebMvcLinkBuilder;

@GetMapping("/users/{id}")
public EntityModel<User> getUser(@PathVariable Long id) {
    User user = userService.findById(id);

    return EntityModel.of(user,
        WebMvcLinkBuilder.linkTo(methodName(UserController.class)
            .getUser(id))
            .withSelfRel(),
        WebMvcLinkBuilder.linkTo(methodName(UserController.class)
            .getAllUsers())
            .withRel("all-users"),
        WebMvcLinkBuilder.linkTo(methodName(PostController.class)
            .getUserPosts(id))
            .withRel("posts")
    );
}
```

### Django REST Framework with HAL

```python
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()

class UserDetailView(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)

        data = serializer.data
        data['_links'] = {
            'self': {'href': f'/api/users/{pk}/'},
            'all-users': {'href': '/api/users/'},
            'posts': {'href': f'/api/users/{pk}/posts/'}
        }

        return Response(data)
```

### Express.js Example

```javascript
const express = require('express');
const app = express();

app.get('/api/users/:id', (req, res) => {
  const user = getUserById(req.params.id);

  res.json({
    ...user,
    _links: {
      self: { href: `/api/users/${user.id}` },
      'all-users': { href: '/api/users' },
      posts: { href: `/api/users/${user.id}/posts` },
      update: { href: `/api/users/${user.id}`, method: 'PUT' },
      delete: { href: `/api/users/${user.id}`, method: 'DELETE' }
    }
  });
});
```

## Common Patterns and Best Practices

### 1. Semantic Link Relations

Use standardized relation names from IANA Link Relations registry:

```
- self: The current resource
- next: The next resource in a collection
- previous: The previous resource in a collection
- first: The first resource in a collection
- last: The last resource in a collection
- up: The parent resource
- parent: The parent resource
- child: A child resource
- related: A related resource
- alternate: An alternative representation
- item: A member of a collection
- collection: The collection resource
```

### 2. Link Objects with Metadata

Include additional metadata in links:

```json
{
  "_links": {
    "documents": {
      "href": "/api/orders/456/documents",
      "title": "Order Documents",
      "type": "application/hal+json",
      "count": 3
    }
  }
}
```

### 3. Template Links (RFC 6570)

Use URI templates for parameterized links:

```json
{
  "_links": {
    "search-users": {
      "href": "/api/users{?name,email}",
      "templated": true
    }
  }
}
```

Client can expand: `/api/users?name=John&email=john@example.com`

### 4. Conditional Links Based on State

Only expose links that represent valid transitions:

```json
{
  "id": 1,
  "status": "draft",
  "_links": {
    "self": { "href": "/api/documents/1" },
    "publish": { "href": "/api/documents/1/publish", "method": "POST" },
    "delete": { "href": "/api/documents/1", "method": "DELETE" }
  }
}
```

When published:

```json
{
  "id": 1,
  "status": "published",
  "_links": {
    "self": { "href": "/api/documents/1" },
    "unpublish": { "href": "/api/documents/1/unpublish", "method": "POST" },
    "archive": { "href": "/api/documents/1/archive", "method": "POST" }
  }
}
```

### 5. Pagination with HATEOAS

```json
{
  "page": 1,
  "pageSize": 20,
  "total": 100,
  "items": [
    { "id": 1, "name": "Item 1" },
    { "id": 2, "name": "Item 2" }
  ],
  "_links": {
    "self": { "href": "/api/items?page=1&pageSize=20" },
    "first": { "href": "/api/items?page=1&pageSize=20" },
    "last": { "href": "/api/items?page=5&pageSize=20" },
    "next": { "href": "/api/items?page=2&pageSize=20" },
    "previous": null
  }
}
```

## Challenges and Criticisms

### 1. Increased Response Size
HATEOAS responses include additional metadata (links), increasing payload size and bandwidth usage.

**Mitigation:**
- Use field filtering to allow clients to request only needed fields
- Implement response compression (gzip)
- Consider separating links from data in some cases

### 2. Client Complexity
Clients must handle dynamic link discovery and follow links, which is more complex than hard-coded URLs.

**Mitigation:**
- Provide client libraries that abstract link navigation
- Clear documentation and examples
- Standardized hypermedia formats (HAL, SIREN)

### 3. Performance Overhead
Extra HTTP requests may be needed to discover available actions.

**Mitigation:**
- Include related resources using embedding (e.g., HAL's `_embedded`)
- Design link schemas to minimize round-trips

### 4. Adoption Challenges
Many API consumers prefer explicit endpoint documentation over dynamic discovery.

**Reality:**
- True HATEOAS is rare in practice
- Most APIs implement partial HATEOAS or use it selectively

## When to Use HATEOAS

### Good Use Cases

1. **Public APIs with Versioning Requirements**: Allows API evolution without breaking clients
2. **Workflow-Oriented APIs**: Where available operations depend on current state
3. **Discovery-Focused Integrations**: Where clients benefit from self-discovery
4. **Long-Lived Client Relationships**: Where decoupling from specific URLs is valuable

### Less Ideal Use Cases

1. **High-Performance APIs**: Additional metadata can impact latency
2. **Simple CRUD APIs**: Overhead may not be justified
3. **Internal APIs**: Where API structure is stable and known
4. **Real-Time Applications**: Where bandwidth is critical

## Examples in the Wild

### GitHub API
GitHub provides hypermedia links in responses:

```json
{
  "id": 1,
  "name": "Hello-World",
  "_links": {
    "self": { "href": "https://api.github.com/repos/octocat/Hello-World" },
    "html": { "href": "https://github.com/octocat/Hello-World" },
    "clone": { "href": "https://github.com/octocat/Hello-World.git" }
  }
}
```

### PayPal API
PayPal extensively uses HATEOAS in their REST API responses for action discovery.

### Stripe API
Stripe provides links to related resources and operations in responses.

## Related Concepts

### GraphQL
GraphQL provides an alternative approach to data fetching where clients specify exactly what they need, reducing the need for HATEOAS.

### Content Negotiation
HATEOAS works alongside content negotiation to deliver the right representation based on client preferences.

### API Versioning
HATEOAS can reduce versioning needs by allowing APIs to evolve without breaking clients.

## Summary

HATEOAS is a powerful constraint of the REST architecture that enables self-discovering, loosely-coupled APIs. By including hypermedia links in responses, servers enable clients to navigate APIs dynamically without prior knowledge of endpoint URLs.

While HATEOAS offers significant benefits for API evolution and discoverability, it comes with tradeoffs in response size, client complexity, and performance. Effective use of HATEOAS requires careful design and consideration of whether the benefits justify the additional overhead for your specific use case.

The key is to find the right balance between discoverability and simplicity, often implementing partial HATEOAS where it provides the most value.

## Resources

- [Roy Fielding's REST Dissertation](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)
- [Spring HATEOAS Documentation](https://docs.spring.io/spring-hateoas/docs/current/reference/html/)
- [HAL - Hypertext Application Language](https://stateless.co/hal_specification.html)
- [IANA Link Relations Registry](https://www.iana.org/assignments/link-relations/link-relations.xhtml)
- [RESTful API Best Practices - HATEOAS](https://restfulapi.net/hateoas/)
- [JSON-LD Specification](https://json-ld.org/)
- [Collection+JSON Specification](http://amundsen.com/media-types/collection/)
- [SIREN Hypermedia Specification](https://github.com/kevinsullivan/siren)
