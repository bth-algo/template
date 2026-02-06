lös kmom01.
ny branch
gå tillbaka till kmom01, ändra kod
hoppa till kmom02 utan commit.
repeat ovanstående med commit.

skapa kmom03.
repeat ovanstående mellan 01 och 03?


M kmom01 först --- jag tror att kmom02 också mergades automatiskt när jag mergade 01.
M kmom02 först
PR mot kmom01 <-- kmom02


PROBLEM
om de får Ux på kmom01, går tillbaka och fixar. Hoppar till kmom02 igen. Då ligger det ändringar i kmom01 som inte finns i 02. 01 mergas in i main och så småningom mergas kmom02 in i main där ändringen saknas. Vad händer då?!??!? Lokalt när jag hoppar mellan branches är det inte något problem men blir nog i github när PR öppnas och sen ska mergas.
Jag tror man slipper det problemet om man gör PR mot föregående branch istället för mot main. Fast hur gör vi då när vi godkänner kmom01 PR. Den måste ju med main då. Sen mergar vi in kmom02.. till kmom01. Gör vi en ny PR i slutet från kmom01 mot main?
TESTA I GITHUB ATT SKAPA BRANCHES, GÖR ÄNDRINGAR, SKAPA pr OCH MERGA. TESTA SKAPA BRANCHES FRÅN MAIN, ANDRA BRANCHES OCH SEN MERGA MOT MAIN OCH MOT ANDRA BRANCHES. kOLLA i copilot på det flödes diagrammen som finns som visar de olika arbetssäten.

lokalt i repot nu har jag kvar att göra klart kmom02 efter att jag fixade en Ux i kmom01 och har nu hoppat tillbaka till kmom02. Så nu finns en ändring i kmom01 som inte finns i kmom02.



Om studs kör på fler datorer och byter till annan. då följer inte branches med. Kan laddas ner med
```
git fetch --all
git branch -r | grep -v '\->' | while read remote; do git branch --track "${remote#origin/}" "$remote" 2>/dev/null || true; done
git pull --all
```



När gör push i branch, i github får man då upp en fråga om att skapa en Pr och knapp som gör det. Vi vill inte att de gör det före de är klara. behöver ha en text som varnar om det.


Om det har påbörjat kmom02 och hoppar tbx till kmom01  och har marvin filen öppen i vscode. Då blir den överstruken och röd. Om de sparar filen skapas den i kmom01 branchen. Väldigt lätt att råka göra det. Man hade velat stänga alla öppna filer när gör switch.


De kan får G på senare kmom före tidigare om de har fått Ux eller inte lämnat in tidig i tid men den sena i tid. Om man kör flödet merga till tidigare branch istället för main, vad händer om man mergar in 02 i 01 före 01 är klar? 
