# Source: https://www.exim.org/howto/rbl.html

Title: Using DNS Block Lists (DNSBLs)

URL Source: https://www.exim.org/howto/rbl.html

Markdown Content:
The MAPS (Mail Abuse Protection System) RBL (Realtime Blackhole List) was the first application of a way of using a DNS list as a means of identifying hosts that have been associated with the sending of spam mail. A full description of the service and the technology and ethics behind it could once be found at [http://www.mail-abuse.org/rbl/](http://www.mail-abuse.org/rbl/) along with more general mail policy information at [http://www.mail-abuse.org/](http://www.mail-abuse.org/).

In the few years since MAPS started operating, other similar services although with different aims, procedures and reliabilities have been introduced - MAPS itself has a number of these (ie MAPS/DUL which maintains lists of dial up modems). At this point in time there are many 10s of services with varying charters - lists of these can be found at [http://relays.osirusoft.com/](http://relays.osirusoft.com/) and [http://spamblock.outblaze.com/spamchk.html](http://spamblock.outblaze.com/spamchk.html). The services are now normally referred to as a DNS Block List (DNSBL), rather than RBLs, however you will find that earlier Exim documentation (ie for version 3.x) will use the older term.

### Exim DNSBL Support

Exim has supported RBL from version 1.80, although the flexibility was increased (with a related change configuration options) on the release of Exim 3.00. With the release of Exim 4.00 the whole basis of policy checks on incoming mail changed to be based on a set of Access Control Lists (ACLs) applied at various during the incoming mail transaction. For this reason the configuration of Exim 4.x and later to use DNSBLs is complete different to that used for earlier versions.

### Exim 4.x DNSBL Usage

In Exim 4.x a DNSBL lookup can be used in any of the incoming SMTP ACLs. However it is typical for the lookups to be used in the ACL handling RCPT TO - this allows policies to accept mail for postmaster or other special local parts (for example so a blocked sender can talk to the local postmaster about getting blocks lifted or excluded)

The use of DNSBLs is substantially documented in the main exim specification or the 4.x versions, so will not be covered in detail here. However a couple of examples can be given

# Add a warning header if the sending host is in these
# DNSBLs but acccept the message (or rather leave it for
# later ACLs to accept/deny
warn message = X-blacklisted-at: $dnslist_domain
     dnslists = blackholes.mail-abuse.org : \
                dialup.mail-abuse.org

# Reject messages from senders listed in these DNSBLs
deny dnslists = blackholes.mail-abuse.org
Documentation on these features can be found in the specification section on [Access Control Lists](https://www.exim.org/exim-html-current/doc/html/spec_html/ch40.html).

A typical configuration would be a mail system which rejects mail from machines that appear within either the MAPS RBL list or the MAPS DUL (Dial-Up List), and also checks hosts in the RSS lists but only marking each message has coming via an RBLed host rather than rejecting them. Additionally all mail to the local postmaster always gets through, even if the host is in the MAPS RBL list. You also have a local private set of IPs which relay out through this mail server on net 192.168.0.0/24 - these cannot be contacted from outside your organisation so RBL is not an issue.

The information to do more complicated manipulations can be found in the specification document and is outside the scope of this note.
