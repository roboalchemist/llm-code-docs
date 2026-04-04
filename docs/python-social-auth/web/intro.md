# Intro

Source: https://python-social-auth.readthedocs.io/en/latest/intro.html

Introduction
¶

Python Social Auth aims to be an easy to setup social authentication and
authorization mechanism for Python projects supporting protocols like 
OAuth
 (1
and 2), 
OpenID
 and others.

Features
¶

This application provides user registration and login using social sites
credentials, here are some features, probably not a full list yet.

Supported frameworks
¶

Multiple frameworks support:

Django

Flask

Pyramid

Webpy

Tornado

More frameworks can be added easily (and should be even easier in the future
once the code matures).

Auth providers
¶

Several supported service by simple backends definition (easy to add new ones
or extend current one):

Angel
 OAuth2

Beats
 OAuth2

Behance
 OAuth2

Bitbucket
 OAuth1

Box
 OAuth2

Dailymotion
 OAuth2

Deezer
 OAuth2

Disqus
 OAuth2

Douban
 OAuth1 and OAuth2

Dropbox
 OAuth1

Eventbrite
 OAuth2

Evernote
 OAuth1

Facebook
 OAuth2 and OAuth2 for Applications

Fitbit
 OAuth2 and OAuth1

Flat
 OAuth2

Flickr
 OAuth1

Foursquare
 OAuth2

Google App Engine
 Auth

GitHub
 OAuth2

Google
 OAuth1, OAuth2 and OpenID

Instagram
 OAuth2

Kakao
 OAuth2

Keycloak
 OpenID

Linkedin
 OAuth1

Live
 OAuth2

Livejournal
 OpenID

Mailru
 OAuth2

MineID
 OAuth2

Mixcloud
 OAuth2

Mozilla Persona

NaszaKlasa
 OAuth2

NGPVAN ActionID
 OpenID

Odnoklassniki
 OAuth2 and Application Auth

OpenID

Podio
 OAuth2

Pinterest
 OAuth2

Rdio
 OAuth1 and OAuth2

Readability
 OAuth1

Shopify
 OAuth2

Skyrock
 OAuth1

Soundcloud
 OAuth2

Spotify
 OAuth2

ThisIsMyJam
 OAuth1

Stackoverflow
 OAuth2

Steam
 OpenID

Stocktwits
 OAuth2

Stripe
 OAuth2

Tripit
 OAuth1

Tumblr
 OAuth1

Twilio
 Auth

Twitch
 OAuth2

Twitter
 OAuth1

Upwork
 OAuth1

Vimeo
 OAuth1

VK.com
 OpenAPI, OAuth2 and OAuth2 for Applications

Weibo
 OAuth2

Wunderlist
 OAuth2

Xing
 OAuth1

Yahoo
 OpenID and OAuth1

Yammer
 OAuth2

Yandex
 OAuth1, OAuth2 and OpenID

User data
¶

Basic user data population, to allow custom fields values from providers
response.

Social accounts association
¶

Multiple social accounts can be associated to a single user.

Authentication and disconnection processing
¶

Extensible pipeline to handle authentication, association and disconnection
mechanism in ways that suits your project. Check 
Authentication Pipeline

section.