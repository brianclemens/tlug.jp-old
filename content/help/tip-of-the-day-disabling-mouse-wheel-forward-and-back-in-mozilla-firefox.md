---
categories:
- Linux_Help:Tip_of_the_Day|Firefox
date: '2026-02-05'
draft: false
title: Linux Help - Tip of the Day - Disabling Mouse Wheel Forward and Back in Mozilla
  Firefox
---

{{ML|0707/msg00028.html|Josh Glover}}

I don't know if anyone else has run into this, but every once in a
while, if I get my mouse pointer too close to the edge of a window in
Firefox, attempting to scroll with the wheel results in Firefox going
back a page (or several pages, for particularly vigorous scroll
attempts). I do not find this behaviour useful at all, since I can
think of at least two other ways to go back (my favourite being the
Backspace key, but I've been known to click on the back button when
Firefox and Openbox have a focus-handling bug convergence). If you are
with me, here's how to disable this annoying feature:

1. [Optional] Open a new tab
1. Type "about:config" into the location bar and press Enter
1. Type "wheel" into the Filter textbox; a bunch of options should appear
1. Locate "mousewheel.horizscroll.withnokey.action"
1. Double-click on it to edit the value
1. Enter 0 as the value and click on the OK button
1. [Optional] Close the about:config tab


Cheers,<br />
Josh

[Firefox](/category/linux-help/tip-of-the-day/)