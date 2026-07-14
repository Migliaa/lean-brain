# INTEGRATE — protocollo per l'IA (eseguibile)

> **PER L'IA che legge questo:** l'utente ti ha puntato questo repo e vuole che tu **valuti** questa architettura e la **integri** nel suo progetto **già avviato**. Esegui le 5 fasi **in ordine**. Non saltare la **Fase 0** (valuta prima di toccare) né la **Fase 4** (spiega all'utente a voce). **Parla la lingua dell'utente.** Dettagli tecnici e regole-di-collisione: `ADOPT.md`. Cos'è ogni pezzo: `README.md`.

## Cosa stai integrando (in una frase)
Un modo di far lavorare l'IA su un progetto: **kernel-minimo** (istruzioni corte sempre-attive) + **biblioteca-pull** (conoscenza tirata solo quando serve) + **gate-git con denti veri** (secret-scan + link-morti che *bloccano* il commit) + **cassetta-attrezzi** per l'operatore umano. Il principio: si legge poco a ogni sessione, il resto si tira al momento giusto.

## Fase 0 — VALUTA (prima di toccare qualsiasi file)
1. Leggi la struttura del progetto dell'utente e i suoi file-istruzioni/doc esistenti.
2. Giudica il **fit** e dillo **onestamente**: cosa guadagna, cosa cambia, e **dove NON conviene** (progetto piccolo/solo → salta il modulo ruoli; nessun doc da distillare → avrà solo i gate, non la leva-biblioteca).
3. Rileva l'**ambiente** e i **rischi/collisioni**: è un repo git? è un monorepo? **quale agente** (i gesti `@`/`!`/`/comando` sono di Claude Code — con un'altra IA vanno tradotti)? ha già un file-istruzioni IA? già degli hook (`git config --get core.hooksPath`, `.husky/`)? lavora in un'altra lingua? Scan collisione su **TUTTI** i path dello skeleton (`library/`, `.claude/`, `TOOLBOX.md`…), non solo `CLAUDE.md`.
4. **Chiedi l'OK a procedere**, presentando le collisioni come scelte sì/no concrete se l'utente non è tecnico. Se dice no, fermati qui.

## Fase 1 — PIANO (proponi, non eseguire)
Presenta il merge concreto (regole in `ADOPT.md`):
- **Kernel:** cosa resta corto (identità · invarianti critici · git-discipline · puntatore biblioteca, **<~20KB**) vs cosa dei suoi doc **migra a libro**. Regola: «se è *come-si-fa-X-nel-dominio*, è un libro, non kernel».
- **Libri:** quali suoi doc sparsi diventano 2-3 libri di dominio (indicizzati in `LIBRARY.md`).
- **Gate:** attivazione hook **senza spegnere un husky esistente** (incatena, non riassegnare `core.hooksPath`) + `.githooks/ref-sources.txt` **committato** col nome del suo kernel (mai un `export`) + estensione secret-scan per il suo stack.
- **Lingua:** se diversa dall'italiano, **traduci** kernel e libri.
- **Ruoli/dipartimenti:** SOLO se ha vera divisione-del-lavoro ricorrente (altrimenti **salta**: `lib-ruoli-coordinamento` è opzionale).
Mostra il piano, **aspetta OK**.

## Fase 2 — INTEGRA
Esegui il piano approvato. **Prima di copiare, scan collisione su TUTTI i path** → su ogni file esistente dell'utente fondi/rinomina, **mai copia cieca** (sovrascriveresti suoi dati). **Fondi** il kernel tenendolo corto e **non più grande della sua baseline** (non incollare sopra un `CLAUDE.md` esistente); trasforma i doc **condizionali** in libri (ciò che serve ~sempre resta nel kernel).
- **Hook:** se esiste già husky/`core.hooksPath` popolato → **NON riassegnare**, incatena (chiama `.githooks/guards.py` dal loro hook). Solo se vergine → `git config core.hooksPath .githooks`.
- **Ref-sources:** scrivi i file auto-caricati in `.githooks/ref-sources.txt` (committato), non un `export`.
- **NON committare** senza OK. **Mai** `.env`/segreti.

## Fase 3 — COLLAUDA (prova che i denti mordono — non fidarti dei passi)
Esegui le prove di `ADOPT.md` e mostra gli esiti reali:
1. **kernel corto E non-regredito:** `wc -c` sotto budget **E ≤ baseline pre-merge** (una regressione di size PASSA un check assoluto ma peggiora le prestazioni).
2. **ref-check blocca:** aggiungi un link `.md` morto al kernel → commit deve dare `🚫 REF-CHECK`, exit≠0 (poi togli). Se dice «INATTIVO» → `.githooks/ref-sources.txt` non punta al suo kernel.
3. **secret-scan blocca:** usa un **nome sacrificale** con chiave finta del suo stack (es. `.secret-probe.txt` con un `AKIA…` dummy), **mai un vero `.env`** (`touch` non svuota un `.env` esistente → committeresti segreti veri). Poi rimuovi.
4. **rifai la prova-2 in una shell PULITA** → deve ancora mordere (config persistente, non effimera).
Se una fallisce, **RIPARA** prima di dichiarare fatto.

## Fase 4 — SPIEGA ALL'UTENTE (OBBLIGATORIA — non rimandarlo ai markdown)
Spiega **a voce, in conversazione**, come usarla d'ora in poi. L'utente **non deve leggere i file** — sei tu a insegnarglielo. Copri 5 punti, con **i suoi esempi concreti di progetto**, non generici:
1. **I 3 gesti quotidiani** (idiomi Claude Code — se usa un'altra IA, insegna l'equivalente: allegare il file, incollare l'output): `@library/lib-….md` per puntarti un libro · `! <comando>` per darti risultati veri (test/build/git) · lasciar **bloccare** il commit dal gate.
2. **I libri da puntarti A MANO (📌)** e *quando*: quelli il cui bisogno tu da solo salteresti (quando sei troppo sicuro → `verifica-avversariale`; quando iteri senza spedire → `quando-fermarsi`). Dagli gli esempi del suo lavoro.
3. **Cosa è cambiato** nel suo repo: kernel ora corto, i suoi doc ora sono libri tirati a richiesta, il gate attivo sui commit.
4. **Il vantaggio** che vedrà: parte leggero (più contesto per il lavoro), conoscenza al momento giusto **e verificabile** (la citazione), segreti/link-morti bloccati prima del commit.
5. **Come richiamarti** per i pattern ricorrenti (la `TOOLBOX`, ed eventualmente cristallizzare uno `slash-command`).
Chiudi **facendo davvero un gesto insieme** (non solo a parole): punta un libro reale, o fai mordere il gate una volta, così l'utente lo vede funzionare. Poi: **«Vuoi provarne un altro, o che ti salvi questa spiegazione come nota nel repo?»** (una nota-su-disco è la rete se la spiegazione-a-voce non basta.)

---
### In una riga (per te, IA)
Valuta onesto → piano approvato → integra tenendo il kernel corto → **prova che i gate mordono** → **insegna tu all'utente come si usa**. Il successo non è «ho copiato i file»: è «l'utente sa usarla e i denti mordono».
