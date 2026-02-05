---
date: '2026-02-05'
draft: false
title: TlugWiki - Wiki Topics
---

= Wiki Topics for consideration=

- File Uploads
** [Al](/user/hoanga/) requests: Do we allow file uploads to the wiki?  It's turned off
** [Josh](/user/jmglov/) answers: a big yessir to this!
- SSL - Currently we don't have https so all authentication to this wiki is over plain http.  Should we use https?
** [Al](/user/hoanga/): Can someone create a SSL configuration for Apache?  Out of the wikimaster's hands :)
** [Josh](/user/jmglov/) answers: I don't see a burning need for SSL
- What official pages do we need?
** [jmglov](/user/jmglov/) suggests:
*** Meetings pages?
*** Officers page
** [Edward](/user/edward/) answer: wouldn't this stuff be better on the main page that way we could solve the rss issues as well.
- RSS
** What type of RSS?
** Look at the top of [Special:Recentchanges](/special/recentchanges/). It has Atom and RSS already
*** [zev](/user/zev/): Yes, but if we were to make a meetings page that lists the meetings then we could do an RSS feed by adding these parameters to the URL "action=histroy&feed=rss", but I that would just be the edits of that page.  I would like to have the actuall details of each meeting be a unique entry in the feed.  A very shallow look on the MediaWiki help pages seems to point to Wikipedia scraping the pages and then making an external feed for that...

1. Completed Topics
- Permissions Wringing - Permissions need to be (thoroughly) tested to be sure the implementation matches the policy.
** [Al](/user/hoanga/): I think the permissions are working.  Everyone please check.
- Prettier URLS?
** YES!
** [Action Paths](http://www.mediawiki.org/wiki/Manual:%24wgActionPaths) might help 
** [jmglov](/user/jmglov/): (withdrawn) <span style="text-decoration: line-through; color: red;">Along these lines, I recommend we make the page naming convention CamelCase, instead of the current Delimit_Words_With_Underscores conventions. What say ye?</span>
*** [zev](/user/zev/): Why would we want to do that?  I see we would loose the ability to express Topic titles that have spaces in them?
** At the very least let's trash the index.php header. See: http://meta.wikimedia.org/wiki/Eliminating_index.php_from_the_url
** [Al](/user/hoanga/): Need someone with web-admin rights who can configure the apache config.  I don't have apache config rights.. Josh??  
- Logo - We need a TLUG specific wiki logo.  Which one should we use?
** How about our current TLUG penguin?
*** [Al](/user/hoanga/): Updated
- Admin only access section of Wiki?  I want to document various admin related things.  Some should be public, but some might not be appropriate?
** [Al](/user/hoanga/): This has **been implemented**.  Start documenting!
** Such as server software to monitor for security patches
- Time stamps in JST !!!!(Can we fix this soon?)
** This should be a simple setting in MediaWiki... when?
** I think we can change it through this variable: http://www.mediawiki.org/wiki/Manual:%24wgLocaltimezone
** And this :http://meta.wikimedia.org/wiki/Help:Timezone
** [Al](/user/hoanga/): **This is done** as of 2/5/2007
- Get the rest of the Wiki Admins online
** [Al](/user/hoanga/): **Done** at hackathon
** [jmglov](/user/jmglov/) suggests:
*** List policy / FAQ
**** [Al](/user/hoanga/):Done