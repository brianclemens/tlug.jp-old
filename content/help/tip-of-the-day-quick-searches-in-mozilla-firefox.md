---
categories:
- Linux_Help:Tip_of_the_Day|Firefox
date: '2026-02-05'
draft: false
title: Linux Help - Tip of the Day - Quick Searches in Mozilla Firefox
---

[Mailing list archive link](http://www.tlug.jp/ML/0602/msg00169.html)

I assume many TLUGgers already know this one, but:

1. Browse to your favourite search engine (e.g. Google)
1. Search for your favourite thing (e.g. TLUG): http://www.google.com/search?hl=en&q=tlug&btnG=Google+Search
1. Bookmark the results page (I suggest filing the bookmark in a folder called "Quick Searches" or something like that)
1. Bookmarks > Manage Bookmarks
1. Locate the bookmark you just created
1. Right click, then select Properties
1. In the "Location:" textbox, find the search term that you used when creating the bookmark (e.g. "tlug", from our previous example)
1. Replace the search term with "%s", taking care to not change anything else in the URI (e.g. our "Location:" textbox should now read "http://www.google.com/search?hl=en&q=%s&btnG=Google+Search";)
1. In the "Keyword:" textbox, enter a single word or letter (e.g. "g") to use as the keyword for quick searches (explanation to follow)
1. In the "Description:" textbox, enter the same word you chose for "Keyword:" (e.g. "g"); this is simply because the Bookmarks Manager does not display the keyword in its simple view
1. Click OK
1. Return to a browser window, click in the location textbox, and enter the keyword that you selected above, a single space, then some search terms (e.g. g "quick-n-dirty guides")
1. Press Enter or click Go
1. Voila!

For additional fun, I have attached a bookmarks file containing a folder full of my favourite quick searches. You can import this straight into your Mozilla / Firefox by choosing the Bookmarks >
Manage Bookmarks to open the Bookmarks Manager, then selecting File > Import from the menu. Choose From File, click Next, select my quick-searches.html file from wherever you saved it, then click open. This will create a new folder called "jmglov Quick Searches" in your top-level Bookmarks folder.

Use these as a starting point for your own collection!

Cheers,
Josh

PS: Yes, I do know about Mycroft search plugins [http://mycroft.mozdev.org/download.html?name=pgp.mit.edu&submitform=Search] [http://mycroft.mozdev.org/download.html?name=kobesearch.cpan.org&submitform=Search] [http://www.jmglov.net/opensource/], but I find "Ctrl + L g foo Enter" faster even than "Ctrl + L Tab foo (Ctrl +
(Up|Down))* Enter". :)

*Firefox*