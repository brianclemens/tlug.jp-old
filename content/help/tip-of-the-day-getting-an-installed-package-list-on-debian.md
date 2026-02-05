---
categories:
- Linux_Help:Tip_of_the_Day|dpkg
date: '2026-02-05'
draft: false
title: Linux Help - Tip of the Day - Getting an Installed Package List on Debian
---

[Mailing list link](http://www.tlug.jp/ML/0602/msg00381.html)

I'll pass this on to Debian users from the Debian Laptop list.

*"I would like to get a list of all packages installed on a system, including their version in order to track the changes that has been made during a system upgrade."*

Suggested solutions:

    dpkg -l | awk '/^ii/{print $2, $3}'
    dpkg -l | grep ^ii

Regards,
Chuck

*dpkg*