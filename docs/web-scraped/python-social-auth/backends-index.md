# Backends/Index

Source: https://python-social-auth.readthedocs.io/en/latest/backends/index.html

Backends
¶

Here’s a list and detailed instructions on how to set up the support for each
backend.

Adding new backend support
¶

Add new backends is quite easy, usually adding just a 

class

 with a couple
methods overrides to retrieve user data from services API. Follow the details
in the 
Implementation
 docs.

Adding a new backend

Common attributes

OAuth

OpenID

Auth APIs

Common backend methods

Supported backends
¶

Here’s the list of currently supported backends.

Non-social backends
¶

Email Auth

Backend settings

Email validation

Password handling

Username Auth

Backend settings

Password handling

Base OAuth and OpenID classes
¶

OAuth

OpenID

Username

SAML

Required Dependency

Required Configuration

Basic Usage

Advanced Settings

Advanced Usage

Troubleshooting

Social backends
¶

Amazon

Angel List

AOL

AppleID

Appsfuel

Appsfuel Live

Appsfuel Sandbox

ArcGIS

OAuth2

Auth0

Auth0 OAuth2

Auth0 OpenID Connect

IdP Setup

Application Configuration

Scopes

Microsoft Azure Active Directory

IdP Setup

Application Configuration

Tenant Support

B2C Tenant

Battle.net

Beats

OAuth2

Behance

DEPRECATED NOTICE

Belgium EID

Bitbucket

OAuth2

OAuth1

User ID

Bitbucket Data Center OAuth2

Configuration

Extra Configuration

Box.net

Bungie

CAS (OpenID Connect via Apereo CAS)

Username

Scopes

ChangeTip

Clef

Coinbase

Cognito

Coursera

DailyMotion

DigitalOcean

Discogs

Discord

Discourse

Using multiple Discourse instances

Disqus

Docker

Docker.io OAuth2

Douban

Douban OAuth1

Douban OAuth2

Dribbble

Drip

Dropbox

OAuth2 Api V2

OAuth1

OAuth2

Edmodo

Etsy OAuth2

Configuration

Extra Configuration

Eventbrite OAuth

EVE Online Single Sign-On (SSO)

Evernote OAuth

Sandbox

Facebook

OAuth2

Canvas Application

Facebook Limited Login

App creation

Configuration

Django Configuration

Fedora

Scopes

Environment

Fitbit

OAuth 2.0 or OAuth 1.0a

OAuth 2.0 specific settings

Flat

Flickr

Foursquare

GitHub

GitHub for Organizations

GitHub for Teams

GitHub for Enterprises

GitHub Apps

GitHub Enterprise

GitHub Enterprise for Organizations

GitHub Enterprise for Teams

GitLab

Gitea

Google

Google OAuth

Google OAuth2

Google One Tap

Google+ Sign-In

Google OpenID

Orkut

User identification

Refresh Tokens

Scopes deprecation

Grafana

Instagram

Jawbone

Just Giving

OAuth2

Kakao

Keycloak - Open Source Red Hat SSO

IdP Setup

Application Configuration

User ID Configuration

Khan Academy

Kick

Last.fm

Launchpad

Lifescience AAI

Scopes

Line.me

LinkedIn

OpenID Connect

OAuth2

LiveJournal

MSN Live Connect

LoginRadius

Lyft

MailChimp

Mail.ru OAuth

Legacy OAuth2 authorization

MapMyFitness

MediaWiki OAuth1 backend

Usage

General documentation

Developer documentation

Code based on

Meetup

Mendeley

OAuth1

OAuth2

Microsoft Graph

MineID

Self-hosted MineID

Mixcloud OAuth2

Moves

NationBuilder

NationBuilder

Naver

NFDI (OpenID Connect)

Username

Scopes

NGP VAN ActionID

Odnoklassniki.ru

OAuth2

IFrame applications

Okta

Okta OAuth2

Okta OpenID Connect

OpenStreetMap (Legacy OAuth 1.0a)

OpenStreetMap OAuth 2

Configuration

Extra Configuration

OIDC (OpenID Connect)

IdP Setup

Authentication Request Parameters

Username

Scopes

Orbi

ORCID

Member API

Sandbox

Osso - Open Source SAML SSO

Patreon

Mozilla Persona

Pinterest

PixelPin

PixelPin OAuth2

Pocket

Podio

Qiita

QQ

Quizlet

Rdio

OAuth 1.0a

OAuth 2.0

Extra Fields

Readability

Reddit

RunKeeper

Salesforce

Seznam

User ID

Shimmering Verify

Shopify

SimpleLogin

Sketchfab

Skyrock

Slack

SoundCloud

Spotify

OAuth2

SUSE

openSUSE OpenID

Stackoverflow

Steam OpenID

StockTwits

Strava

Stripe

Taobao OAuth

Telegram

ThisIsMyJam

Trello

TripIt

Tumblr

Twilio

Twitch

Twitter

Twitter API v2

Udata

Datagouvfr OAuth2

Uber

OAuth2

Untappd

Upwork

OAuth1

Hashicorp Vault

Vault OIDC configuration

Scopes

Vend

Vimeo

VK.com (former Vkontakte)

OAuth2

OAuth2 Application

OpenAPI

Weibo OAuth

Withings

Wunderlist

XING

Yahoo

Yahoo OpenID

Yahoo OAuth2

Yammer

Production Mode

Staging Mode

Zotero