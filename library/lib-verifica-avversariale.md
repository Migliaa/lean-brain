---
id: lib-verifica-avversariale
scaffale: op
quando: stai per FINALIZZARE un design, una scelta architetturale, o un pezzo di codice non-triviale/costoso/irreversibile
sting: alto
verified: 2026-07-14
---

# lib-verifica-avversariale — attacca il tuo lavoro PRIMA di finalizzarlo

> **Il principio:** il tuo lavoro sembra sano *a te che l'hai fatto* — sei il controllore e il controllato. Un critico **a freddo** (senza il tuo contesto, senza il tuo affetto per il lavoro) trova i buchi che tu non vedi. Verifica **prima** di finalizzare/spedire, non dopo che il buco è costato. Questo metodo ha ribaltato un intero design il 2026-07-14 (i «testimoni deterministici» sembravano solidi; 5 lane a freddo hanno mostrato che erano teatro).

## Quando lanciarlo
Prima di: ratificare un design · mergiare codice non-banale · prendere una scelta irreversibile/costosa · dichiarare «fatto/completo». Più il lavoro è costoso o a-senso-unico, più lane. Per un quick-check: 1-2 lane. Per un audit serio: 4-6.

## Il metodo (fan-out a freddo)
- **Lane a freddo = meno prevenute.** Ogni agente riceve SOLO l'artefatto (il documento di design o il codice reale), **niente contesto storico**. Un revisore senza inerzia giudica sui meriti. Con un solo modello-famiglia (es. tutto-Claude) questo è anche l'**anti-common-mode** più forte rimasto: angoli indipendenti riducono il punto-cieco condiviso.
- **Angoli DIVERSI, non ridondanti.** Es.: ① spara-davvero / aggirabilità · ② gli assi-di-salute del sistema, se ne hai (correttezza, efficienza, robustezza…) · ③ bug / edge-case / portabilità · ④ il-paradosso (forma-vs-sostanza) · ⑤ steelman dell'alternativa (e se la scelta opposta fosse giusta?).
- **Tu sintetizzi** (una testa): raccogli, distingui i colpi-veri dai rumori, e — regola d'oro — **incassa i colpi giusti anche quando fanno male al tuo lavoro**. Il valore è ciò che sopravvive alla critica.

## Le 4 lenti che trovano i buchi veri
1. **Forma vs sostanza.** Il testimone/test verifica il *proxy meccanico* o la *cosa reale*? Un campo-presente ≠ contenuto-vero; un path-che-risolve ≠ file-corretto; un test-verde ≠ comportamento-giusto. L'errore che conta vive quasi sempre nella sostanza che il proxy non tocca.
2. **Prove-che-sparano, non test-verdi-a-vuoto.** Un check con «9/9 test verdi» e 0 gate reale è *verde d'aspetto*. Chiedi: c'è un caso che DIMOSTRA il blocco/il fallimento reale? Se non l'hai visto sparare, non sai se ha denti.
3. **Auto-osservabile ≠ fuori-controllo.** Una verifica è forte solo se il fatto che la scora è **fuori dal tuo controllo**. Predire/verificare una *tua* azione (auto-computabile ma auto-adempiente) non è una vera verifica: è una cerimonia. Punta al mondo (mercato, deploy, fatti esterni), non a te stesso.
4. **Controllore=controllato ⇒ enforcement minimo.** Dove chi-verifica coincide con chi-è-verificato, il sistema si concede l'enforcement più basso della sua scala. La cura non è un testimone più-elaborato (che scrivi/aggiri tu): è un testimone **esterno** — un check che gira dove non puoi editarlo (CI su infra altrui), un umano nel loop, o la realtà a una data. Se non ne hai nessuno, sei nella *rilocazione*, non nella riduzione.

## Anti-pattern
- **Fidarsi del proprio verde.** Il verde-meccanico fabbrica falsa-fiducia proprio dove non c'è verifica.
- **Premortem a-mente.** Deve attaccare l'artefatto REALE (il codice, il documento), verificato — non un'idea generica di esso.
- **Lane ridondanti.** 5 agenti con lo stesso angolo = 1 angolo pagato 5 volte. Diversifica le lenti.
- **Sovra-verificare il triviale.** Scala l'effort al costo/irreversibilità del lavoro; un typo-fix non merita 6 lane.

## In una riga
Prima di finalizzare qualcosa che costa: fallo a pezzi **a freddo, da più angoli**, cercando dove verifichi la *forma* invece della *sostanza* — e tieni ciò che sopravvive.
