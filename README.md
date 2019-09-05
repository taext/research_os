## ResearchOS v0.18
Custom Linux command-line tools for handling online media in the 21st century.

- **YouTube, Bing, LibGen, VLC, GPG** and **OPML** shell integrations

<br>

### custom software

[**mediabyte**](https://github.com/taext/mediabyte) (online [player](http://www.mediabyte.xyz/)) #[idea](https://github.com/taext/research_os/blob/master/ideas/mediabyte-interesting-idea.md)

[**powercasts**](https://github.com/taext/powercasts/blob/master/README.md) #[idea](https://github.com/taext/research_os/tree/master/ideas/powercasts-interesting-idea.md)

[**calibre_tooling**](https://github.com/taext/calibre_tooling/blob/master/README.md) #[idea](https://github.com/taext/research_os/blob/master/ideas/calibre_tooling-interesting-idea.md)

<br>

### custom web parsers

[**yn**](https://github.com/taext/parsers/tree/master/youtube_parser) get YouTube video search result URLs in-line #[idea](https://github.com/taext/research_os/blob/master/ideas/yn-interesting-idea.md)

[**bn**](https://github.com/taext/parsers/tree/master/bing_parser) get Bing web search result URLs in-line #[idea](https://github.com/taext/research_os/blob/master/ideas/bn-interesting-idea.md)

[**lib**](https://github.com/taext/parsers/tree/master/libgen_parser) get Library Genesis book search results in-line #[idea](https://github.com/taext/research_os/blob/master/ideas/lib-interesting-idea.md)

[**bay**](https://github.com/taext/parsers/tree/master/the_hidden_bay_parser) get thehiddenbay.com torrent search results in-line #[idea](https://github.com/taext/research_os/blob/master/ideas/bay-interesting-idea.md)

[**dr_m3u8**](https://github.com/taext/parsers/tree/master/dr_m3u8) get .m3u8 streaming link of dr.dk tv program #[idea](https://github.com/taext/research_os/blob/master/ideas/dr_m3u8-interesting-idea.md)

[**amazon_link**](https://github.com/taext/parsers/tree/master/amazon_parser) get book title Amazon link in-line


<br>

### bin scripts

[**lg**](https://github.com/taext/research_os/blob/master/bin/lg): ls and then grep

[**cle**](https://github.com/taext/research_os/blob/master/bin/cle): encrypt clipboard with default public key #[idea](https://github.com/taext/research_os/blob/master/ideas/gem-and-cle-interesting-idea.md)

[**bs**](https://github.com/taext/research_os/blob/master/bin/bs): search Bing for arguments, open result page in browser

[**copy**](https://github.com/taext/research_os/blob/master/bin/copy): copy argument to clipboard

[**p**](https://github.com/taext/research_os/blob/master/bin/p): paste clipboard

[**see**](https://github.com/taext/research_os/blob/master/bin/see): search YouTube using random search terms from short film related [word list](https://github.com/taext/research_os/blob/master/bin/parsed_terms.txt), open in VLC #[idea](https://github.com/taext/research_os/blob/master/ideas/see-interesting-idea.md)

[**you**](https://github.com/taext/research_os/blob/master/bin/you): search youtube, open results in VLC

[**ytd**](https://github.com/taext/research_os/blob/master/bin/ytd): download youtube video to ~/Downloads

[**arte**](https://github.com/taext/research_os/blob/master/bin/arte): open arte.tv in browser

[**sq**](https://github.com/taext/research_os/blob/master/bin/sq): parse website for regex, e.g. MP3 link, get result in-line (spider queen)

[**gem**](https://github.com/taext/research_os/blob/master/bin/gem): encrypt string (argument or piped) with default public key #[idea](https://github.com/taext/research_os/blob/master/ideas/gem-and-cle-interesting-idea.md)

[**di**](https://github.com/taext/research_os/blob/master/bin/di): open di.fm in browser

[**pdf**](https://github.com/taext/research_os/blob/master/bin/pdf): open PDF filename regex matches from ~/Downloads

[**sms**](https://github.com/taext/research_os/blob/master/bin/sms): sms using Twilio (Twilio account needed)

[**sub**](https://github.com/taext/research_os/blob/master/bin/sub): download YouTube video info .json and subtitles .vtt

[**late**](https://github.com/taext/research_os/blob/master/bin/late): show n files modified the latest

[**v**](https://github.com/taext/research_os/blob/master/bin/v): open clipboard URL in VLC

[**vg**](https://github.com/taext/research_os/blob/master/bin/vg): lg then open in VLC

<br>


### Hotkeys


[**ya_paste**](https://github.com/taext/research_os/blob/master/bin/ya_paste): takes active input field text, search YouTube, open results in browser tabs (YouTube button) (e.g. Insert key)

[**ba_paste**](https://github.com/taext/research_os/blob/master/bin/ba_paste): takes active input field text, search Bing, open results in browser tabs (Bing button) (e.g. Shift+Insert key)

[**vsub_paste**](https://github.com/taext/research_os/blob/master/bin/vsub_paste): open  YouTube URL from clipboard in VLC and download video info and subtitles (VLC YouTube w. subs and info) (e.g. Shift+Win+V)

[**gen_paste**](https://github.com/taext/research_os/blob/master/bin/gen_paste): search LibGen with clipboard text, open Library Genesis results page (e.g. Alt+L)

<br>

How to setup an [Ubuntu hotkey](https://www.faqforge.com/linux/distributions/ubuntu/create-custom-keyboard-shortcut-ubuntu-16-04/).

<br>

### Aliases

**c**: google-chrome

**f**: firefox

**.** (dot): clear (terminal)

**d**: cd ~/Downloads

**docs**: cd ~/Documents

**jn**: jupyter notebook

**mp4**: ls *.mp4

**n**: nemo .

**sau**: sudo apt update; sudo apt upgrade

**yt**: youtube-dl

<br>

How to setup a [Linux alias](https://www.tecmint.com/create-alias-in-linux/).

<br>
