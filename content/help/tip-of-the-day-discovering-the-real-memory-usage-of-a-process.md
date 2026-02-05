---
categories:
- Linux_Help:Tip_of_the_Day|ps
date: '2026-02-05'
draft: false
title: Linux Help - Tip of the Day - Discovering the Real Memory Usage of a Process
---

[mailing list link](http://www.tlug.jp/ML/0602/msg00132.html)

 ps -lyu <your_username>

By default, top(1) shows the virtual and resident memory sizes of
processes, which is a little misleading, in that shared libraries are
counted over and over again, painting a scarier picture of memory
usage than the actual situation. Thanks to a comment attached to a
very useful [entry](http://virtualthreads.blogspot.com/2006/02/understanding-memory-usage-on-linux.html) in [a very useful blog](http://virtualthreads.blogspot.com/), I discovered the above
invocation of ps(1), which will list, in the "SZ" column, the size of
the process itself, discounting shared libraries and such.

For more details on all of this, see the [blog entry itself](http://virtualthreads.blogspot.com/2006/02/understanding-memory-usage-on-linux.html).

For more details on what ps(1)'s "SZ" column is really representing,
search the manpage for '^size':

 size       SZ       approximate amount of swap space that would be required if
                     the process were to dirty all writable pages and then be
                     swapped out. This number is very rough!

Cheers,
Josh

*ps*