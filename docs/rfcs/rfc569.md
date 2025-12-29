---
title: "NETED: A Common Editor for the ARPA Network"
---

# 1. n m

For unsigned m, the n(ext) request causes the pointer to be moved
"down" m lines.  If m is negative, the pointer is moved "up" m lines.
If m is not specified, the pointer is moved one line.  If the end of
the file is reached, an "End of file reached by n m" message is output
by NETED; the pointer is left "after" the last line.

# 2. l string

The l(ocate) request causes the pointer to be moved to the net line
containing the character string "string" (which may contain blanks);
the line is output.  If no match is found, a message of the form "End
of file reached by l string" will be output (and the pointer will
have returned to the top of the file).  The search will not wrap
around the end of the file; however, if the string was above the
starting position of the pointer, a repetition of the locate request
will find it, in view of the fact that the pointer would have been
moved to the top of the file.  To find any occurrence of the string --
rather than the next occurrence -- it is necessary to move the pointer
to the top of the file before doing the locate (see following
request).

# 3. t

Move the pointer to the top of the file.

NETED SPEC                                                       p. 6

# 4. b

Move the pointer to the bottom of the file and enter input mode.

5.  "."

Leave the pointer where it is and enter input mode.  (First new line
goes after current old line.)

# 6. i string

The i(nsert) request cause a line consisting of string (which will
probably contain blanks) to be inserted after the current line.  The
pointer is moved to the new line.  Edit mode is not left.

# 7. r string

The r(eplace) request causes a line consisting of string (probably
containing blanks) to replace the current line.

# 8. p m

The p(rint) request causes the current line and the succeeding m - i
lines to be output.  If m is not specified, only the current line will
be output.  End of file considerations are the same as with "n".

# 9. c /s1/s2/ m g

The c(hange) request is quite powerful, although perhaps a bit complex
to new users.  In the line being pointed at, the string of characters
s1 is replaced by the string of characters s2.  If s1 is void, s2 will
be inserted at the beginning of the line; if s2 is void, s1 will be
deleted from the line.  Any character not appearing within either
character string may be used in place of the slash (/) as a delimiter.
If a number, m, is present, the request will affect m lines, starting
with the one being pointed at.  All lines in which a change was made
are printed.  The pointer is left at the last line scanned.  If the
letter "g" is absent (after the final delimiter) only the first
occurrence of s1 within a line will be changed.  If "g" (for "global")
is present, all occurrences of s1 within a line will be changed.  (If
s1 is void, "g" has no effect.)  NOTE WELL:  blanks in both strings
are significant and must be counted exactly.  End of file
considerations are the same as with "n".

# 10. d m

The d(elete) request causes m lines, including the current one, to be
deleted from the working copy of the file.  If m is not specified, only
the current line is deleted.  The pointer is left at a null line above
the first undeleted line.  End of file considerations are the same as
with "n".

NETED                                                           p. 7

# 11. w

Write out the working copy into the storage hierarchy but remain in
NETED.  (Useful for those who fear crashes and don't want to lose all
the work performed.)

# 12. save

Write out the working copy into the storage hierarchy and exit from
NETED.

Additional specs:

a.  On Multics, type-ahead is permitted.  This approach is recommended
for all versions of NETED, but is of course not required as various
Servers' NCP Implementations may prohibit it; however:

b.  If an error is detected, the offending line is output, and pending
typeahead (if any) must be discarded (to guard against the possibility
of the pending request's being predicated on the success of erroneous
request).

c.  The command is not reinvokable, in the sense that work is lost if
you "quit" out of it via the Telnet Interrupt Process command or its
equivalent; indeed, quitting out is the general method of negating
large amounts of incorrect work and retaining the original file
intact.

(When the time comes, I'll be glad to furnish examples for the users'
manual version; but for now, that's all there is.)

NOTE

It really does work, unsophisticated though it may be.  I think that
it's sufficient to get new users going, and necessary to give them a
fighting chance.  It would even be of utility within the NWG, for
those of us who don't like having to learn new editors all the time.
If anybody wants to try it, I'll make a version available to
"anonymous users" (see the Multics section in the Resource Notebook if
you don't already know how to get in our sampling account), under the
name "neted".  (*) (If you do try it, please delete files when done
with them.)

______________

(*)  Knowledgeable Multics users with their own accounts can instead
link to >udd>cn>map>neted.  It is also there under the names "eds" if
you want to save typing a couple of characters.
