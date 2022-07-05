documentation for py server
http://homepages.math.uic.edu/~jan/mcs275/mcs275notes/lec23.html
py path: which python3




## STAGE-5 / WEB interface (ui / frontend)

    * tech stack:
        - HTML
        - CSS
        - JS

        - Networking basics
        - HTTP(S) Basics
        - DNS basics



## WEB App / site

              HTTP(S) / TCP/IP
[backend]   <------------------>    [frontend]

DB + py                               HTML





[Server]    <--  internet/net     <-- reqest  [Client]
    |       -->                   --> responce   |
serverApp.py                             Chrome browser







(MVT pattern)
CLIENT ----> req --->
        ^             \
        |              VIEW (cgi/py) --(data)-->\
        |                                        MODEL <---> DB
        |                  <------------(data)--/
        |                 /
        |              (embed)
        |                 |
        |                 |
        \                 v
          <---res<---- TEMPLATE(.html)