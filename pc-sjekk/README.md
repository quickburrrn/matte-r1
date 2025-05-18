# PC-Sjekk Til Eksamen

I denne mappen ligger to programmer som sjekker PC-en din for ulovlige programmer. Samme som finnes på USB under stikkprøver på eksamen i Agder Fylkeskommune per 16.05.2025.


### kontroll.exe

Dette programmet er standard programmet under stikkprøvene til Agder Fylkeskommune per 16.05.2025.

Her får du opp input om kandidatnummer, der du kan skrive hva du vil. Etterhvert vil det dukke opp enten en grønn eller rød skjem. Grønn skjerm betyr at PCen din er godkjent. Ved rød skjerm betyr det at PCen din inneholder ulovlige programmer, og du vil få en liste med disse.



### AI.exe

Dette programmet er nyere og ikke implementert overalt i stikkprøver.

Her sjekkes PCen din for lokale LLM-er / chatmodeller. Denne vil både lete etter mistenkelige filer og prossesser på PCen, som betyr at om du kjører en virtuell maskin prossess til f.eks. Docker eller andre liknende kontainer tjenester, vil dette bli oppdaget.