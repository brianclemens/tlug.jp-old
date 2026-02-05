---
categories:
- Linux_Help:Tip_of_the_Day|Firefox
date: '2026-02-05'
draft: false
title: Linux Help - Tip of the Day - Word Selection in Mozilla Firefox
---

Author: [User:Jmglov](/user/jmglov/)

[Mailing list archive link](http://www.tlug.jp/ML/0705/msg00372.html)

This one is stolen from the Env Improvement Ninjas at work--as Keith can attest--but it is too cool not to share.

Typically, double-clicking in the location bar in Firefox selects the whole URI. This is counter-intuitive to old Unix hackers, who are used to double-clicking on a word in *xterm* to select just that word. Here's how to correct this behaviour in Firefox:

1. Open Firefox
1. Enter about:config in your location bar and hit Enter
1. Type in layout.word
1. Two preferences should appear (both should default to false)
1. layout.word_select.eat_space_to_next_word
1. layout.word_select.stop_at_punctuation
1. Double-click on *layout.word_select.stop_at_punctuation* to toggle it to true
1. Close about:config
1. Double-click in the location in Firefox and see what gets selected

[Firefox](/category/linux-help/tip-of-the-day/)