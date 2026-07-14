# ADOPT — portare lo skeleton in un progetto GIÀ avviato

> Per chi ha già un repo con codice e magari già un file-istruzioni per l'agente. Obiettivo: aggiungere l'architettura **senza rompere niente** e **senza peggiorare le prestazioni**.

## La direzione (importante)
**L'architettura entra NEL tuo progetto. Non sposti il tuo codice.** Aggiungi il nucleo alla root e attivi un hook; il resto del repo resta identico. Nomi che collidono coi tuoi (tipico: `CLAUDE.md`, o una tua cartella `library/`) si **fondono** — regole sotto.

## Il modo facile: lo fa l'IA (protocollo `INTEGRATE.md`)
Copia i file nella root e di' alla tua IA: **«Leggi `INTEGRATE.md` ed eseguilo sul mio progetto.»** Protocollo 5 fasi: valuta → piano (aspetta OK) → integra → collauda → **ti spiega lei come si usa**. Sotto i passi manuali se preferisci controllare.

---

## I passi a mano (con le regole di collisione)
1. **Copia il NUCLEO** (`CLAUDE.md · .githooks/ · library/` coi 2 libri-metodo) nella root. Da `advanced/` prendi SOLO ciò che ti serve (LIBRARY.md/TOOLBOX.md solo se hai molti libri; ruoli solo con vera divisione-del-lavoro). **Prima di copiare: scan collisione su TUTTI i path** (`library/`, `.githooks/`, `.claude/`, ecc.), non solo `CLAUDE.md` → su ogni collisione fondi/rinomina, **mai copia cieca** (sovrascriveresti tuoi file).
2. **Kernel — la regola che salva le prestazioni:** *cosa-va-dove.*
   - Nel kernel SOLO: identità · le 3-5 regole a costo-di-violazione alto · git-discipline · il puntatore ai libri. **Tienilo corto (~20KB), e NON più grande del tuo kernel attuale** (registra la size di prima: se cresce, è una regressione).
   - Ciò che serve a **~ogni** sessione **resta nel kernel** (non farne un libro: lo perderesti). Solo la conoscenza **condizionale/rara** va in `library/`. Regola: «come-si-fa-X-di-dominio, e non-sempre-serve → libro».
   - **Hai già un `CLAUDE.md`?** Non incollarci sopra: fondi. Le righe critiche restano, le lunghe/condizionali migrano a libro.
3. **Raccogli i tuoi doc in libri.** README lunghi, note, convenzioni sparse → 2-3 file in `library/` con front-matter. Senza questo passo hai solo un hook, non il vantaggio.
4. **Attiva e configura i gate:**
   - **Hai già husky / un altro pre-commit?** Controlla: `git config --get core.hooksPath` e cerca `.husky/`. **Se popolato → NON riassegnare** `core.hooksPath` (spegneresti il tuo): fai chiamare `.githooks/guards.py` DENTRO il tuo hook esistente. Solo se vergine: `git config core.hooksPath .githooks` (unix/mac: `chmod +x .githooks/pre-commit`).
   - **Sorgenti ref-check:** metti i tuoi file auto-caricati in **`.githooks/ref-sources.txt`** (file **committato**, una per riga). Rinominato il kernel? aggiornalo lì — **mai** con un `export` (vive solo nella tua shell, lascia il gate morto in VSCode/GUI/altre shell).
   - **Estendi `SECRET_CONTENT`** in `guards.py` per il tuo stack (AWS/GCP/npm già attivi; aggiungi i tuoi).
5. **Lingua:** se il progetto lavora in un'altra lingua, traduci kernel e libri — ma **NON** i filename/path (romperebbero il ref-check) e verifica che i trigger tradotti scattino ancora.

---

## ✅ Il collaudo — prove che DEVONO passare (o non è collegato)
Non fidarti dei passi seguiti: **verifica che i denti mordano.**
1. **Kernel corto E non-regredito:** `wc -c CLAUDE.md` → sotto budget **E non più grande della tua baseline pre-merge**.
2. **Ref-check morde:** aggiungi `[x](library/non-esiste.md)` al kernel, `git add`+`git commit` → `🚫 REF-CHECK`, exit≠0 (poi togli). Se dice «INATTIVO» → non hai configurato `.githooks/ref-sources.txt`.
3. **Secret-scan morde:** usa un **nome sacrificale** (MAI un vero `.env`, che `touch` non svuota):
   `printf 'aws_key="AKIA%s"\n' 0000000000000000 > .secret-probe.txt && git add -f .secret-probe.txt && git commit` → `🚫 SECRET` (poi `git rm --cached .secret-probe.txt && rm .secret-probe.txt`).
4. **Rifai la prova-2 in una shell PULITA** (nuovo terminale) → deve ancora mordere: prova che la config è persistente, non effimera.

---

## ⚠️ Come NON perdere prestazioni (gli errori che causano il calo)
| Errore | Perché peggiora | La cura |
|---|---|---|
| **Svuoti tutti i tuoi doc nel kernel** | tassa-boot × ogni sessione esplode → più lento di prima | kernel corto (passo 2) |
| **De-kernelizzi conoscenza always-on** | ciò che serviva sempre ora è dietro un pull che l'agente salta → comportamento peggiore | frequente → resta nel kernel (passo 2) |
| **Libreria vuota** | copi lo skeleton ma non estrai i tuoi doc → solo un hook | passo 3 |
| **Riassegni `core.hooksPath` su husky** | il tuo pre-commit sparisce muto | incatena, non riassegnare (passo 4) |
| **`export` invece del file** | gate morto fuori dalla tua shell, ma il collaudo passa | `.githooks/ref-sources.txt` committato (passo 4) |
| **Secret-scan parziale** | attivo per nome ma non per il tuo stack → falso-senso-di-sicurezza | estendi `SECRET_CONTENT` + prova-3 col TUO tipo di chiave |

## In una riga
Copi il nucleo (scan-collisione prima), tieni il kernel **corto e non-regredito**, trasformi i doc **condizionali** in libri, incateni il gate senza spegnere il tuo, e **provi che morde in una shell pulita**.
