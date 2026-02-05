---
categories:
- Linux_Help:Tip_of_the_Day|xmodmap
date: '2026-02-05'
draft: false
title: Linux Help - Tip of the Day - Printing Keymap Table with xmodmap
---

xmodmap -pke

This tip is helpful when you have a (mostly) working keyboard, and one that isn't working so well. For example, I have a Dell Latitude D410 laptop with a Japanese keyboard. For some odd reason, when I tell [X.org](http://x.org/) to use a *jp106* keyboard model, the backslash / underscore / ろ key that is located just to the left of my right shift key does not work. Neither do the various Japanese input-specific special keys (半角 / 全角 / 漢字, 無変換, 変換, and カタカナ / ひらがな / ローマ字), the Windows keys, or the volume raise, lower, and mute keys. Luckily, I also have a *jp106* keyboard on my [Gentoo](http://www.gentoo.org/) desktop.

Here's how I got my keymap on the Dell laptop straightened out.

1. On the desktop, run: <pre>xmodmap -pke</pre> You will get a bunch of output like this: <pre>keycode  47 = semicolon plus kana_RE&#13;keycode  48 = colon asterisk kana_KE&#13;keycode  49 = Zenkaku_Hankaku Kanji&#13;keycode  50 = Shift_L</pre>
1. On the laptop, open at least two terminal emulators
1. In one term, cd to your home directory and edit the file *.xmodmaprc* (this file most likely will not exist, and thus be empty when you edit it)
1. In the other term, run: <pre>xev</pre> This will launch a little window that, when it has focus, will spew information about X events to the terminal from which it was launched
1. Get used to xev by giving it the focus, waiting for a second until there is no new output to the terminal window, then pressing a key. You should see out like this appear: <pre>KeyPress event, serial 27, synthetic NO, window 0x1600001,&#13;    root 0x3b, subw 0x0, time 2049376201, (158,128), root:(1269,943),&#13;    state 0x0, keycode 208 (keysym 0xff27, Hiragana_Katakana), same_screen YES,&#13;    XLookupString gives 0 bytes:&#13;    XmbLookupString gives 0 bytes:&#13;    XFilterEvent returns: False&#13;&#13;KeyRelease event, serial 30, synthetic NO, window 0x1600001,&#13;    root 0x3b, subw 0x0, time 2049376297, (158,128), root:(1269,943),&#13;    state 0x0, keycode 208 (keysym 0xff27, Hiragana_Katakana), same_screen YES,&#13;    XLookupString gives 0 bytes:</pre> The main thing you want to note here is the keycode, which will be the second bit of data in the third line of every log statement output in response to a KeyPress event.
1. Now, follow these steps for each key that is not working on the laptop:
1. On the laptop (i.e. non-working keyboard), give the xev window the focus, wait a few seconds and press the troublesome key. e.g. I press the backslash / underscore / ろ key
1. Note the keycode. e.g. I see <pre>KeyPress event, serial 27, synthetic NO, window 0x1600001,&#13;    root 0x3b, subw 0x0, time 2049376201, (158,128), root:(1269,943),&#13;    state 0x0, keycode 211 (keysym 0x0, NoSymbol), same_screen YES,&#13;    ...</pre> I note keycode 211.
1. On the desktop (i.e. working keyboard), find the line that corresponds to the key you are trying to map. Note that it may not have the same keycode. In my example, I find the line <pre>keycode 211 = backslash underscore kana_RO</pre>
1. On the laptop, switch to the terminal where you are editing *.xmodmaprc* and enter the line just as it appeared in the output of *xmodmap -pke* on the desktop, but changing the keycode if necessary. e.g. I enter <pre>keycode 211 = backslash underscore kana_RO</pre>
1. After entering mapping expressions into *.xmodmaprc* on the laptop for each of your troublesome keys, save *.xmodmaprc* and exit
1. Close *xev* by hitting Ctrl-C in the terminal from which you launched it
1. Now, make sure that the command <pre>xmodmap ${HOME}/.xmodmaprc</pre> runs on startup of your window manager. If you are using an old-school *.xinitrc*, simply add the line <pre>xmodmap ${HOME}/.xmodmaprc</pre> to the file before the window manager is started. <font color="red">**GNOME / KDE user: update this section to give instructions for running xmodmap on startup!**</font>

*xmodmap*