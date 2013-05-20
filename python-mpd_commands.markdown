python-mpd
==========

[](#title)

-   [Sign in or create your account](/login/)
-   [Project List ▾](/)
    -   [python-mpd](/p/python-mpd/)

-   [Help](/help/ "Help and accessibility features")

[Project Home](/p/python-mpd/) [Downloads](/p/python-mpd/downloads/)
[Documentation](/p/python-mpd/doc/) [Issues](/p/python-mpd/issues/)
[Source](/p/python-mpd/source/tree/master/) [Code
Review](/p/python-mpd/review/)

[Source Tree](/p/python-mpd/source/tree/master/) | [Change
Log](/p/python-mpd/source/changes/master/) | [How To Get The
Code](/p/python-mpd/source/help/)

[Root](/p/python-mpd/source/tree/master/)/[doc](/p/python-mpd/source/tree/master/doc)/[commands.txt](/p/python-mpd/source/tree/master/doc/commands.txt)
-------------------------------------------------------------------------------------------------------------------------------------------------------

  -------------- ----------------------------------------------------------------
  [1](#L1)       == Status Commands
  [2](#L2)       clearerror -\> fetch\_nothing
  [3](#L3)       currentsong -\> fetch\_object
  [4](#L4)       idle [\<str\>] -\> fetch\_list
  [5](#L5)       noidle -\> None
  [6](#L6)       status -\> fetch\_object
  [7](#L7)       stats -\> fetch\_object
  [8](#L8)       
  [9](#L9)       == Playback Option Commands
  [10](#L10)     consume \<bool\> -\> fetch\_nothing
  [11](#L11)     crossfade \<int\> -\> fetch\_nothing
  [12](#L12)     mixrampdb \<str\> -\> fetch\_nothing
  [13](#L13)     mixrampdelay \<int\> -\> fetch\_nothing
  [14](#L14)     random \<bool\> -\> fetch\_nothing
  [15](#L15)     repeat \<bool\> -\> fetch\_nothing
  [16](#L16)     setvol \<int\> -\> fetch\_nothing
  [17](#L17)     single \<bool\> -\> fetch\_nothing
  [18](#L18)     replay\_gain\_mode \<str\> -\> fetch\_nothing
  [19](#L19)     replay\_gain\_status -\> fetch\_item
  [20](#L20)     volume \<int\> -\> fetch\_nothing
  [21](#L21)     
  [22](#L22)     == Playback Control Commands
  [23](#L23)     next -\> fetch\_nothing
  [24](#L24)     pause [\<bool\>] -\> fetch\_nothing
  [25](#L25)     play [\<int\>] -\> fetch\_nothing
  [26](#L26)     playid [\<int\>] -\> fetch\_nothing
  [27](#L27)     previous -\> fetch\_nothing
  [28](#L28)     seek \<int\> \<int\> -\> fetch\_nothing
  [29](#L29)     seekid \<int\> \<int\> -\> fetch\_nothing
  [30](#L30)     stop -\> fetch\_nothing
  [31](#L31)     
  [32](#L32)     == Playlist Commands
  [33](#L33)     add \<str\> -\> fetch\_nothing
  [34](#L34)     addid \<str\> [\<int\>] -\> fetch\_item
  [35](#L35)     clear -\> fetch\_nothing
  [36](#L36)     delete \<int\> -\> fetch\_nothing
  [37](#L37)     deleteid \<int\> -\> fetch\_nothing
  [38](#L38)     move \<int\> \<int\> -\> fetch\_nothing
  [39](#L39)     moveid \<int\> \<int\> -\> fetch\_nothing
  [40](#L40)     playlist -\> fetch\_playlist
  [41](#L41)     playlistfind \<locate\> -\> fetch\_songs
  [42](#L42)     playlistid [\<int\>] -\> fetch\_songs
  [43](#L43)     playlistinfo [\<int\>] -\> fetch\_songs
  [44](#L44)     playlistsearch \<locate\> -\> fetch\_songs
  [45](#L45)     plchanges \<int\> -\> fetch\_songs
  [46](#L46)     plchangesposid \<int\> -\> fetch\_changes
  [47](#L47)     shuffle [\<str\>] -\> fetch\_nothing
  [48](#L48)     swap \<int\> \<int\> -\> fetch\_nothing
  [49](#L49)     swapid \<int\> \<int\> -\> fetch\_nothing
  [50](#L50)     
  [51](#L51)     == Stored Playlist Commands
  [52](#L52)     listplaylist \<str\> -\> fetch\_list
  [53](#L53)     listplaylistinfo \<str\> -\> fetch\_songs
  [54](#L54)     listplaylists -\> fetch\_playlists
  [55](#L55)     load \<str\> -\> fetch\_nothing
  [56](#L56)     playlistadd \<str\> \<str\> -\> fetch\_nothing
  [57](#L57)     playlistclear \<str\> -\> fetch\_nothing
  [58](#L58)     playlistdelete \<str\> \<int\> -\> fetch\_nothing
  [59](#L59)     playlistmove \<str\> \<int\> \<int\> -\> fetch\_nothing
  [60](#L60)     rename \<str\> \<str\> -\> fetch\_nothing
  [61](#L61)     rm \<str\> -\> fetch\_nothing
  [62](#L62)     save \<str\> -\> fetch\_nothing
  [63](#L63)     
  [64](#L64)     == Database Commands
  [65](#L65)     count \<locate\> -\> fetch\_object
  [66](#L66)     find \<locate\> -\> fetch\_songs
  [67](#L67)     findadd \<locate\> -\> fetch\_nothing
  [68](#L68)     list \<str\> [\<locate\>] -\> fetch\_list
  [69](#L69)     listall [\<str\>] -\> fetch\_database
  [70](#L70)     listallinfo [\<str\>] -\> fetch\_database
  [71](#L71)     lsinfo [\<str\>] -\> fetch\_database
  [72](#L72)     search \<locate\> -\> fetch\_songs
  [73](#L73)     update [\<str\>] -\> fetch\_item
  [74](#L74)     rescan [\<str\>] -\> fetch\_item
  [75](#L75)     
  [76](#L76)     == Sticker Commands
  [77](#L77)     sticker get \<str\> \<str\> \<str\> -\> fetch\_item
  [78](#L78)     sticker set \<str\> \<str\> \<str\> \<str\> -\> fetch\_nothing
  [79](#L79)     sticker delete \<str\> \<str\> [\<str\>] -\> fetch\_nothing
  [80](#L80)     sticker list \<str\> \<str\> -\> fetch\_list
  [81](#L81)     sticker find \<str\> \<str\> \<str\> -\> fetch\_songs
  [82](#L82)     
  [83](#L83)     == Connection Commands
  [84](#L84)     close -\> None
  [85](#L85)     kill -\> None
  [86](#L86)     password \<str\> -\> fetch\_nothing
  [87](#L87)     ping -\> fetch\_nothing
  [88](#L88)     
  [89](#L89)     == Audio Output Commands
  [90](#L90)     disableoutput \<int\> -\> fetch\_nothing
  [91](#L91)     enableoutput \<int\> -\> fetch\_nothing
  [92](#L92)     outputs -\> fetch\_outputs
  [93](#L93)     
  [94](#L94)     == Reflection Commands
  [95](#L95)     commands -\> fetch\_list
  [96](#L96)     notcommands -\> fetch\_list
  [97](#L97)     tagtypes -\> fetch\_list
  [98](#L98)     urlhandlers -\> fetch\_list
  [99](#L99)     decoders -\> fetch\_plugins
  [100](#L100)   
  -------------- ----------------------------------------------------------------

[![Archive](http://jatreuman.indefero.net/media/idf/img/package-grey.png?d554b)](/p/python-mpd/source/file/master/doc/commands.txt)
[Download this file](/p/python-mpd/source/file/master/doc/commands.txt)

### Branches

-   [master](/p/python-mpd/source/tree/master/)

### Tags

-   [v0.3.0](/p/python-mpd/source/tree/v0.3.0/)
-   [v0.2.1](/p/python-mpd/source/tree/v0.2.1/)
-   [v0.2.0](/p/python-mpd/source/tree/v0.2.0/)
-   [v0.1.0](/p/python-mpd/source/tree/v0.1.0/)

