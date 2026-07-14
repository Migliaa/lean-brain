---
id: lib-quando-fermarsi
scaffale: meta
quando: stai per iniziare un ALTRO giro di design/refactor/audit/analisi invece di spedire un artefatto, o senti che «prima bisogna sistemare X»
sting: alto
verified: 2026-07-14
---

# lib-quando-fermarsi — attività non è progresso

> **Il difetto:** il lavoro che *sembra* progresso — design, audit, refactor, «prima la fondazione» — può rimandare indefinitamente il completamento (o il valore consegnato). È la procrastinazione ben-confezionata: si auto-assolve perché ha l'aspetto del rigore. Provato coi numeri il 2026-07-14: una giornata con 21 commit e **zero file-prodotto**; il picco di attività coincideva col minimo di prodotto.

## I segnali che stai procrastinando (dal disco, non dall'umore)
- **Molti commit, zero artefatti-prodotto** in una finestra (rapporto meta/prodotto che sale).
- Il **picco di attività coincide col minimo di ciò-che-conta** (spedito/validato/venduto).
- **«Prima sistemiamo X»** ripetuto: una deadline che slitta senza un ricalcolo esplicito.
- Stai **costruendo lo strumento che ti direbbe di fermarti** (un odometro per scoprire ciò che già sai).

## Le regole
1. **Ship-or-kill.** Dopo N cicli di design/analisi senza un artefatto, o spedisci qualcosa di reale, o uccidi il filone, o **dichiara esplicitamente il rinvio** a chi decide — mai lasciarlo in un limbo che si auto-rinnova.
2. **Se già sai il problema, non costruire lo strumento per scoprirlo — agisci.** Sai «21 commit, 0 prodotto»? Non ti serve una metrica per confermarlo: fermati e spedisci.
3. **Il meta-lavoro NON è esente dalla regola che impone.** L'auto-miglioramento/la fondazione hanno anch'essi un budget-duro e un ship-or-kill. «Sistemare la base» è legittimo solo se ha un confine dichiarato.
4. **La distanza-dal-traguardo (completamento / valore-consegnato) è la bussola.** Ogni giro deve *avvicinare* al traguardo. Un giro che ri-verifica il piano senza avvicinarsi è sospetto.
5. **Un'architettura sana non ha bisogno di un immunosistema contro sé stessa.** Se ti servono paletti-anti-degenerazione e un poliziotto-contro-la-tua-voglia-di-costruire, il poliziotto è la *diagnosi*, non la cura: stai costruendo troppo.

## Il test in una domanda
> «Questo giro avvicina un artefatto reale al traguardo, o sto lavorando su me stesso / sullo strumento?» — se è il secondo, **fermati e spedisci il pezzo più piccolo reale.**

## L'onestà (perché questo libro è speciale)
Il momento in cui questo libro serve — *stai iterando all'infinito* — è esattamente quello in cui **meno probabilmente lo pulli da solo** (sei assorbito nel giro). Quindi il suo trigger più affidabile **non sei tu-agente: è l'operatore umano** (il tuo committente/owner), che te lo punta quando ti vede progettare senza spedire. È il suo interruttore d'emergenza, non un tuo riflesso. Se te lo punta, prendilo sul serio: probabilmente ha ragione. *Se non c'è nessun umano nel loop (es. un agente in CI/notturno), sostituiscilo con un limite deterministico auto-imposto — un budget di cicli o di tempo che spara il «fermati» per costruzione.*
