# WebMock Ruby Gem Documentation

WebMock is a Ruby library for stubbing and setting expectations on HTTP requests.

It allows you to:
- Stub HTTP requests at the HTTP client library level
- Set expectations on HTTP requests
- Match requests based on method, URI, headers, and body
- Perform smart matching of URIs in different representations
- Work with popular testing frameworks (RSpec, Test::Unit, MiniTest)

## Features

- Low-level HTTP request stubbing (no need to change tests when switching HTTP libraries)
- Request expectation setting and verification
- Flexible request matching (method, URI, headers, body)
- Smart URI matching (handles encoding variations)
- Smart header matching
- Support for multiple testing frameworks and HTTP libraries

## Supported HTTP Libraries

- Async::HTTP::Client
- Curb
- EM-HTTP-Request
- Excon
- HTTPClient
- HTTP Gem (http.rb)
- httpx
- Manticore
- Net::HTTP and derivatives (HTTParty, REST Client)
- Patron
- Typhoeus

## Documentation Files

- **README.md** - Main documentation and installation guide
- **CHANGELOG.md** - Version history and changes
- **LICENSE.md** - License information
- **index.md** - Archived documentation from webmock.github.io

## Installation

```bash
gem install webmock
```

Or add to your Gemfile:

```ruby
group :test do
  gem "webmock"
end
```

## Key Resources

- GitHub Repository: https://github.com/bblimke/webmock
- RubyGems: https://rubygems.org/gems/webmock
- RubyDoc: https://www.rubydoc.info/gems/webmock
