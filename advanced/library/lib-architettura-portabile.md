---
id: lib-architettura-portabile
scaffale: meta
quando: esporti/riusi l'architettura del cervello per un altro progetto · progetti un organismo-agentico da zero · verifichi che i componenti-core funzionino ancora
sting: alto
verified: 2026-07-14
---

# lib-architettura-portabile — lo skeleton non-overfittato di un cervello agentico

> **Cos'è:** la struttura riusabile di un "cervello" — un agente LLM che gestisce un progetto software via file versionati in git — distillata da TickDistill (giugno-luglio 2026) e **ripulita dall'overfitting**. Metà di questo libro è cosa costruire; metà è cosa NON costruire (le lezioni pagate care). Un'esportazione onesta esporta i pezzi-con-denti-veri e lascia il teatro.

## Il principio-madre
**Kernel piccolo / conscio grande.** Ciò che si auto-carica a OGNI sessione (il costo pagato N×M) è **minimo**: identità + gli invarianti a costo-di-violazione-alto + la mappa della biblioteca. Tutto il resto è **pull-on-demand**. Il costo di ogni KB nell'auto-load si moltiplica per ogni sessione e ogni sub-agente → il budget-kernel è la difesa contro il gonfiamento.

## I COMPONENTI CHE FUNZIONANO (esportali)
1. **Kernel-minimo** (`CLAUDE.md`): identità/routing + le guardie universali (git-scoped, env-check, no-secret) + lo scheletro-metodo + le regole-token + il puntatore alla biblioteca. **Budget duro, add-one-evict-one.** MAI la conoscenza-di-dominio qui (va nei libri).
2. **Biblioteca-pull** (`LIBRARY.md` = bibliotecario + `library/lib-*.md`): conoscenza distillata in libri, indicizzati per trigger «When you are…», tirati 1-3 alla volta, **mai auto-caricati**. Un libro = «nomina il tipo-di-task il cui output migliora per averlo letto». `sting: alto` = obbligatorio-quando-il-trigger-matcha.
3. **Gate deterministici con denti REALI** (`.githooks/`): un pre-commit che BLOCCA al choke-point (secret-scan, anti-leak su contenuti pubblici, ref-check su puntatori-morti). **Solo i portanti**, e **provati-che-sparano** (un test che dimostra il blocco reale, non «9/9 verdi e 0 gate»). Il commit *accade* → il gate vale anche se l'LLM «se ne dimentica».
4. **Esternalità-umana** (`TOOLBOX.md`): la cassetta di leve che l'operatore usa a mano per puntare file/libri/comandi. **È la vera esternalità** — l'unica difesa affidabile contro `controllore=controllato`, perché l'LLM non si auto-enforcia.
5. **Git-discipline**: worktree+branch per le sessioni-non-principali, `add` scoped, `.env` mai committato, HEAD-heal solo ancestor-safe.
6. **Libri-metodo universali** (non-overfittati, esportali sempre): [[lib-verifica-avversariale]] (attacca il tuo lavoro a freddo prima di finalizzarlo) · [[lib-quando-fermarsi]] (attività≠progresso).

## I COMPONENTI SCARTATI (le lezioni — NON esportarli)
1. **Multi-fronte / multi-agente auto-gestito come struttura permanente.** Eleva un non-collo-di-bottiglia se il volume-concorrente non c'è (teoria dei vincoli). Pre-scala è over-engineering: *si automatizza dal dolore/volume, mai dalla tecnologia*. Il fan-out di agenti resta utile **on-demand** (audit, ricerca parallela), non come architettura-fissa.
2. **Testimoni-interni auto-scritti** (ledger di predizioni auto-scorate, heartbeat, lint report-only-nel-rito). **RILOCANO** `controllore=controllato`, non lo riducono: li scrive/mantiene/aggira lo stesso LLM controllato. Un audit a freddo li smonta come teatro-che-muore-orfano.
3. **Cablaggi comportamentali (🧠) non-misurati in massa.** Consumano ragionamento a ogni turno, crescono monotòni, e il loro costo non è mai misurabile per-riflesso → potatura impossibile-per-costo. Tienine pochi, nel kernel, e solo quelli con costo-di-violazione-alto.

## LE LEZIONI-RADICE (il vero tesoro esportabile)
1. **`controllore=controllato ⇒ enforcement minimo.** Dove chi-verifica coincide con chi-è-verificato, il sistema si concede l'enforcement più basso. **La cura è l'esternalità** (umano / CI su infra altrui / la realtà a una data), non un testimone più-elaborato.
2. **Forma vs sostanza.** I testimoni deterministici verificano un proxy meccanico; l'errore che conta vive nella sostanza. Un verde-di-forma fabbrica falsa-fiducia proprio dove non c'è verifica.
3. **Auto-osservabile ≠ fuori-controllo.** Una verifica è forte solo se il fatto è fuori dal controllo di chi è verificato.
4. **Attività ≠ progresso.** Un'architettura sana non ha bisogno di un immunosistema contro sé stessa: se costruisci un poliziotto contro la tua tendenza a costruire, il poliziotto è la diagnosi.
5. **Verifica-avversariale a freddo PRIMA di finalizzare** (non dopo): il modo più affidabile di trovare i buchi del proprio lavoro.

## LO SKELETON MINIMO (il file-tree da esportare)
```
CLAUDE.md              # kernel-minimo (template svuotato dal dominio)
LIBRARY.md             # il bibliotecario (indice + istruzione modalità-bibliotecario)
library/               # i libri-metodo universali + i libri-di-dominio del NUOVO progetto
  lib-verifica-avversariale.md   # universale
  lib-quando-fermarsi.md         # universale
.githooks/             # pre-commit con denti veri (secret/leak/ref-check) + core.hooksPath
TOOLBOX.md             # la cassetta-attrezzi dell'operatore
```
**Cosa NON mettere:** testimoni-teatro, multi-fronte, cablaggi-meta-non-misurati, i registri-di-stato TickDistill-specifici.

## REGISTRO-COMPONENTI: come verificare che funzioni ancora
| componente | denti? | come lo verifichi |
|---|---|---|
| kernel-minimo | budget | `wc -c CLAUDE.md` < budget; nessuna conoscenza-di-dominio dentro |
| biblioteca | pull | l'operatore ti punta `@LIBRARY.md`; tu dichiari+leggi+citi il libro |
| gate-git | **sì (blocca)** | un commit-di-prova che DEVE essere bloccato (path-morto / secret) → exit≠0 |
| esternalità-umana | sì | l'operatore usa `TOOLBOX.md`; è l'unico enforcement affidabile |
| git-discipline | sì | worktree isolati, 0 `.env` committati |

## In una riga
Kernel-minimo + biblioteca-pull + pochi-gate-con-denti-veri + l'operatore-che-punta. Il resto — testimoni-interni, multi-agente-fisso, cablaggi-a-vuoto — è peso o teatro: la lezione più preziosa è **non** costruirli.
