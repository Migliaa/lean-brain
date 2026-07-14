# 📚 LIBRARY — il bibliotecario (indice deterministico della biblioteca)  ‹TEMPLATE›

> **Cos'è:** l'unica superficie di scoperta della conoscenza dell'organismo. **MAI auto-caricato, MAI un agente** — si SCANSIONA quando un trigger matcha la situazione, si tirano **al più 1-3 libri**. **Budget di questo file: ≤ ~12KB** (l'indice gonfio è il monolite travestito — il cap è curation).
> **Come si usa:** ① scaffale nella mappa · ② matcha «When you are…» · ③ tira il libro.
> **🔖 MODALITÀ BIBLIOTECARIO — se il committente ti punta qui (`@LIBRARY.md` o `/library`):** è il segnale che vuole che tu usi la biblioteca. Passi: ① matcha la situazione col trigger «When you are…» · ② **DICHIARA** quale/i libro/i (1-3) pulli · ③ **LEGGILO davvero** (Read) e **cita 1 riga** di ciò che dice · ④ procedi applicandolo. La dichiarazione+citazione è ciò che rende verificabile-a-vista che l'hai usato (il committente è il testimone). Non sai quale serve → dillo e proponi il candidato più probabile.

## 🗺️ Mappa scaffali
| Scaffale | Contenuto |
|---|---|
| **meta** — organismo & metodo | i libri-metodo universali (sotto) + `‹libri-meta del progetto›` |
| **‹dom›** — dominio | `‹libri di dominio del nuovo progetto›` |

## 📖 Libri
| When you are… | Libro | Claim in una riga | Verified |
|---|---|---|---|
| stai per FINALIZZARE un design/scelta/codice non-triviale o costoso/irreversibile | [lib-verifica-avversariale](../library/lib-verifica-avversariale.md) ⚡sting-alto | Attacca il tuo lavoro **a freddo PRIMA** di finalizzarlo: N lane indipendenti (anti-common-mode) · 4 lenti (forma-vs-sostanza · prove-che-sparano · auto-osservabile≠fuori-controllo · controllore=controllato) · tieni ciò che sopravvive | 2026-07-14 |
| stai per iniziare un ALTRO giro di design/audit/refactor invece di spedire · «prima bisogna sistemare X» | [lib-quando-fermarsi](../library/lib-quando-fermarsi.md) ⚡sting-alto | Attività≠progresso: ship-or-kill · se-già-sai-il-problema-agisci · il meta-lavoro ha un budget-duro · **il committente è l'interruttore** | 2026-07-14 |
| esporti/riusi l'architettura del cervello · progetti un organismo-agentico da zero · verifichi i componenti-core | [lib-architettura-portabile](library/lib-architettura-portabile.md) ⚡sting-alto | Skeleton non-overfittato: kernel-minimo + biblioteca-pull + gate-git-con-denti-veri + esternalità-umana; NON esportare i testimoni-teatro/multi-fronte; 5 lezioni-radice | 2026-07-14 |
| (OPZIONALE) il progetto ha vera divisione-del-lavoro ricorrente · l'umano-tramite è il collo di bottiglia | [lib-ruoli-coordinamento](library/lib-ruoli-coordinamento.md) ⚡sting-alto | Ruoli/«dipartimenti» = cartella+branch+STATUS(verità)+INTERFACE(canale) che si parlano via git; aggiungi dal VOLUME non dall'organigramma; parti dal più leggero | 2026-07-14 |
| `‹trigger di dominio›` | `‹library/lib-….md›` | `‹claim›` | — |

## 📏 Regole della biblioteca
- **Ammissione di un libro nuovo:** nomina il tipo-sessione/situazione il cui output migliora per averlo letto. Non sai nominarla → non è un libro. Front-matter obbligatorio: `id · scaffale · quando · sting · verified` + 1 riga qui.
- **Smistatore = chi produce incasella** (alla chiusura: front-matter + riga-indice).
- **Eviction = quarantena, MAI delete** (git = archivio). Rispetta `sting: alto` (obbligatorio-quando-il-trigger-matcha).
- **Kill-criterion:** una regola migrata in libro violata ≥2 volte con costo reale → **torna nel kernel** (`CLAUDE.md`).
