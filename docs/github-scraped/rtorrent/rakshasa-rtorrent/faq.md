# rTorrent Frequently Asked Questions

*User FAQ for Rakshasa's BitTorrent client.*

*rTorrent Frequently Asked Questions*

## How do I add new torrents while the client is running?

Use the backspace key to enter file input mode. The bottom
        line will change into a prompt which allows you to enter URL's
        or file paths to torrents. File name completion and directory
        listing is supported with the tab key.


## I got the message "Could not create download, failed to parse the bencoded data" when adding a torrent, what does it mean?

The torrent data the library received was not a valid torrent
        file. If this was a direct http download, try downloading the
        torrent file and add it manually. This usually happens when
        the torrent link uses some form of redirection that libcurl
        does not automatically redirect. If the failure still happens,
        make sure the file is infact an uncorrupted torrent.


## How does the session feature work?

When you start the client you can use the "-s" switch to
        specify a session directory. The client will save all
        currently running torrents in the session directory and fast
        resume data will be written when the client exits. Upon
        restarting the client it will resume all the torrents in the
        session directory.


## How do i query the tracker for more peers?

Go into the download view screen and press 't' to initiate a
        new tracker request. If the tracker requires a minimum timeout
        between requests you can override this by using the capital
        'T'. Don't abuse this feature.


## Why do I sometimes need to press ctrl-Q twice to exit the client?

The first time you press ctrl-q you initiate the
        shutdown. This causes rTorrent to send a stop message to the
        trackers of each torrent, and if the tracker is slow it might
        take more than a few seconds or until the requests time
        out. The second time ctrl-q is pressed forces the client to
        shutdown.


## It doesn't help how much i press ctrl-q, it still won't quit.

Perhaps your terminal sends a different key-code to the
        application. There's no configuration files for keys yet, so
        modify rtorrent/src/ui/root.cc:56 to use whatever key you want
        for quitting.


## When I try downloading a torrent the client aborts (SIGABRT), what should I do?

Make sure you arn't using "-fomit-frame-pointer" when
        compiling libtorrent and rtorrent, this is known to produce
        bad code for C++ exception handling. If this doesn't help, run
        the client in gdb and use "bt -20" to get a backtrace. Send
        this with a bug report.

