---
id: lib-ruoli-coordinamento
scaffale: meta
quando: il progetto ha vera divisione-del-lavoro ricorrente (più tipi di lavoro: legale·contenuti·ops·…) E abbastanza volume da giustificare sessioni-ruolo separate · l'umano-che-fa-da-tramite è diventato il collo di bottiglia
sting: alto
---

# lib-ruoli-coordinamento — ruoli/«dipartimenti» che si coordinano via git (MODULO OPZIONALE)

> **⚠️ OPZIONALE — leggi prima questo.** Questo modulo NON fa parte dello skeleton-base. Aggiungilo solo se hai **davvero** più tipi di lavoro ricorrente che una singola sessione non regge bene. Progetto solo/semplice → **non usarlo**: sono ruoli-cerimonia che non pagano il loro peso (stessa regola dell'automazione: si aggiunge dal *volume/dolore*, mai perché «un'azienda vera ha i dipartimenti»). Non è il multi-agente-autonomo-parallelo (bocciato altrove): è **divisione-del-lavoro invocata su richiesta**.

## Il principio
Un **ruolo** (legale, contenuti, ops, validazione, report… — i *tuoi*, non quelli di un altro progetto) è una **specializzazione di sessione**. Il valore non è nei nomi: è nella regola che **il contenuto viaggia nei file-git, mai "a voce"**. L'umano è trigger/trasporto, non il canale.

## Cosa possiede un ruolo (i 4 elementi)
1. **Una cartella sua** (`<ruolo>/`) — proprietà esclusiva, ci scrive solo lui.
2. **Un branch suo** — committa lì; il pianificatore (org) rivede (`git diff`) e mergia. Mai su main.
3. **`<ruolo>/STATUS.md`** = i **fatti** del ruolo (dove è, cosa ha fatto). **È la verità.** Se STATUS e messaggi divergono, **vince STATUS**.
4. **`<ruolo>/INTERFACE.md`** = il **canale messaggi** (a scrittura-singola per sezione): direttive che scendono, digest che sale.

## Le regole di coordinamento
- **Direttiva giù / digest su.** L'org scrive gli ordini in `📥 Da ORG`; il ruolo risponde in `📤 Da <RUOLO>` + tiene un `📍 Digest` corto. L'org legge le caselle a ogni avvio (così resta aggiornato senza che l'umano glielo ricordi).
- **Fuori-dominio → escala, non decide.** Il ruolo che incontra una scelta fuori dalla sua cartella la passa all'org con un messaggio autosufficiente (contesto + opzioni), non la risolve da sé.
- **Gate-chain.** Il lavoro passa per stati espliciti: **PASS · CONCERNS · FAIL · WAIVED** (1 riga nello STATUS). La catena non salta anelli.

## I template (copia-incolla)
`<ruolo>/STATUS.md`:
```
# <RUOLO> — STATUS (i fatti; questa è la verità)
## 📍 Dove siamo
## ✅ Fatto  ## 🚧 In corso  ## ⛔ Bloccato-da
## 🚦 Gate: [PASS|CONCERNS|FAIL|WAIVED] — <1 riga>
```
`<ruolo>/INTERFACE.md`:
```
# <RUOLO> — INTERFACE (messaggi; la verità è STATUS)
## 📍 Digest (3 righe max, per l'org)
## 📥 Da ORG   (direttive in ingresso)
## 📤 Da <RUOLO>  (digest/escalation in uscita)
```

## Ogni ruolo porta il suo fascio di libri
Un ruolo non è solo una cartella: porta con sé **due tipi di libro**, **entrambi tuoi** (lo skeleton NON li fornisce — sarebbero contenuto-overfit; fornisce questa *convenzione*):
1. **1 libro-operativo del ruolo** — «come funziona QUESTO ruolo nel mio progetto»: perimetro, procedure, i suoi gate/checkpoint. È il manuale-del-ruolo. Trigger: «When you are… operi come <ruolo>». *(Es.: un ruolo legale → un libro sul suo perimetro e i suoi punti-di-controllo; un ruolo contenuti → la sua pipeline di pubblicazione.)*
2. **N libri-di-dominio che il ruolo consuma** — la conoscenza che gli serve per lavorare (per un legale: le materie/regole rilevanti; per i contenuti: voce/guardrail). Stessi scaffali della biblioteca comune.

**Regole:** indicizzali in `LIBRARY.md` sotto uno **scaffale del ruolo**; nel work-order del ruolo **spingi (push) i 1-3 libri** invece di sperare che l'agente li pulli da solo (→ vedi `TOOLBOX §CATALOGO`: alcuni vanno puntati a mano). Un ruolo senza libri è un guscio: la sua competenza vive nei suoi libri.

## La trappola (onestà)
La cerimonia-completa (caselle-mailbox lette a ogni ciclo, digest bidirezionale) è **pesante**. Parti dal **minimo**: un `STATUS.md` per ruolo + la regola escala-fuori-dominio. Aggiungi le `INTERFACE.md` **solo quando** l'umano-tramite diventa davvero il collo di bottiglia. Il contenuto di ogni ruolo è sempre tuo — esporta il *pattern*, scrivi i *tuoi* ruoli.

## In una riga
Ruoli = cartella + branch + STATUS(verità) + INTERFACE(canale), che si parlano nei file-git; aggiungili dal volume, non dall'organigramma, e parti dal più leggero.
