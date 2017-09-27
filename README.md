# Getting   To   Philosophy 

## Objective

Your   goal   is   to   build   a      front-end   form   that   takes   an   input   of   a   Wikipedia   URL   and   interacts   with a   back-end   API   you’ve   built.   It   will   store   the   data   in   a   database   you’ve   designed,   and   print   out the   path   taken   from   clicking   the   first   link   of   each   page   to   get   to   Philosophy.
The   API   should   take   a   single   Wikipedia   link   as   input,   should   visit   the   given   page,   and   keep going   through   the   first   link   (more   rules   on   the   link   below)   on   each   next   page   until   Philosophy   is reached.   The   path   taken   should   be   stored   in   the   database   with   a   unique   identifier   for   any   given path.   The   front-end   should   display   the   path   taken   to   reach   Philosophy.   It   should   also   display   the amount   of   hops   it   took   to   get   to   the   page.
Here’s   some   more   reading   about   how   the   back-end   should   work.   It’s   important   to   look   at   this page   as   there   are   some   details   on   the   implementation   there: http://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy .

### The   summarized   method   to   do   this   is:
1. Clicking   on   the   first   non-parenthesized,   non-italicized   link
2. Ignoring   external   links,   links   to   the   current   page,   or   red   links   (links   to   non-existent   pages)
3. Stopping   when   reaching   "Philosophy",   a   page   with   no   links   or   a   page   that   does   not   exist,
or   when   a   loop   occurs

### I   will   evaluate   you   in   the   following   aspects:
How   you   structured   your   code
The   Architecture   you   used
Code   quality

### Some   tips:
Because   not   every   single   link   will   lead   to   Philosophy,   think   about   defining   a   maximum number   of   hops
Think   about   how   to   handle   if/when   you   get   stuck   in   a   loop
Find   out   how   to   ignore   citations/sound/extraneous   links
