# Source: https://docs.curator.interworks.com/users_groups/user_security/user_throttling.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# User Throttling 

> Configure user request throttling and rate limiting to prevent system abuse and improve performance stability.

As a security measure, Curator throttles certain activities for a user to mitigate malicious activities.
Where possible, this blocks the logged in user.  If there is no logged in user, then it blocks the IP address
of the user.  For instance, logins only allow a limited number of failed attempts within a time period.  If
that limit is exceeded, the user's IP address is blocked for a period of time to help prevent someone from
brute forcing another user's password.

If Curator is behind a load balancer, reverse proxy, or some other network device that makes it look like all
users are sharing the same IP address, Curator won't be able to distinguish users by IP address so they'll
share the same throttle window when tracking activities that can't be tied to a logged in user.  In that
case, if there are several different users who all mistype their password within minutes of each other,
Curator will block all users from logging in.  If this becomes a recurring issue with your Curator site, the
potential fixes are:

* Fix your network device to pass through the IP address of each user instead of proxy-ing them as a single
  IP address.  See: [Reverse Proxy](/setup/proxy_configuration/reverse_proxy)
* Configure Curator's throttle to allow more failed attempts before triggering the throttle or a shorter
  suspension time after a throttle is triggered.

## Configuring Throttle

By default, Curator only allows 5 attempts within a 15 minute period and, if the throttle is triggered, there
is a 15 minute waiting period before the user is unblocked.

To customize these settings, navigate to **Backend** > **Settings** > **Security** >
**Authentication Settings** > **Customization** section.

The **activity throttle limit** determines how many attempts are allowed for throttle activities (failed
logins, password resets, etc.).

The **activity throttle reset period** determines how long the window is before the throttle count resets.
In other words, if the throttle limit is set to 5 and this setting is 15, then the user can only mistype
their password 5 times in a 15 minute window.  If they exceed that, then their account/IP address will be blocked.

The **activity suspension time** determines how long a user/IP address is blocked after the throttle is
triggered.  In other words, if the user is blocked due to failed login attempts and this setting is 30, the
user will need to wait 30 minutes before they are allowed to try logging in again.

## Clearing Suspensions

If you need to clear a suspension for any reason, you can do so by visiting **Backend** > **Settings** > **Security** >
**Suspensions**.  Find the record that needs to be cleared, check the box to the left of it, and click the delete button
at the top of the screen.
