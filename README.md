# 🧠 lean-brain — lo scheletro minimo di un cervello agentico

Un modo di far gestire un progetto software a un agente LLM (Claude Code) via file versionati in git. **Nucleo piccolo e onesto; il resto è opt-in.**

> Distillato da un progetto reale e ripulito dall'overfitting, poi **snellito dopo un audit avversariale** (2026-07-14) che ha bocciato l'eccesso di cerimonia. Principio-guida (uno dei suoi stessi libri): *un'architettura sana non ha bisogno di un immunosistema contro sé stessa.*

## Il nucleo (è tutto qui)
```
CLAUDE.md          kernel: istruzioni corte auto-caricate (identità · git-discipline · regole-token)
.githooks/         gate-git con denti veri: secret-scan + ref-check (link-morti). BLOCCANO il commit.
library/           i 2 libri-metodo universali (li punti a mano quando servono):
  lib-verifica-avversariale.md   attacca il tuo lavoro a freddo PRIMA di finalizzare
  lib-quando-fermarsi.md         attività ≠ progresso; ship-or-kill
LICENSE · README.md
```

## Serve davvero a te? (onestà prima di adottare)
- **Progetto piccolo / solo / senza doc da distillare** → prenditi **solo il `.githooks/` (secret-scan) e i 2 libri**. Il resto è peso che non ti ripaga. Un buon `CLAUDE.md` scritto bene copre già molto.
- **Progetto che cresce** (molti doc di dominio, più tipi di lavoro) → allora `advanced/` inizia a pagare.

## Come si usa (3 gesti)
1. **Punta un file/libro:** `@library/lib-verifica-avversariale.md` (o `@qualsiasi-file`) → il contenuto entra garantito nel contesto. *L'agente da solo non li tira in modo affidabile: glieli punti tu.*
2. **Dai risultati veri:** `! <comando>` (es. `! npm test`) → l'output entra nel contesto, niente da immaginare.
3. **Lascia bloccare il commit:** se provi a committare un segreto o un link-morto, il gate ferma tutto. Provalo: `.githooks/README.md`.

## Attivazione
1. Copia il nucleo nella root del tuo repo (riempi i `‹…›` in `CLAUDE.md`).
2. `git config core.hooksPath .githooks` — poi **fai la prova-che-spara** in [`.githooks/README.md`](.githooks/README.md) (un gate non provato non ha denti).
3. Estendi il secret-scan per il tuo stack (`.githooks/guards.py`).

## `advanced/` — opt-in, solo quando serve
- **Adottare su un progetto GIÀ avviato** senza leggere niente: di' alla tua IA *«leggi `advanced/INTEGRATE.md` ed eseguilo»* → valuta, integra e **ti spiega lei** come si usa.
- **Guida al merge dettagliata** ([`advanced/ADOPT.md`](advanced/ADOPT.md)), **uso a parole semplici** ([`advanced/USAGE.md`](advanced/USAGE.md)).
- **Indice-biblioteca + bibliotecario** ([`advanced/LIBRARY.md`](advanced/LIBRARY.md)) quando accumuli molti libri di dominio.
- **Cassetta-attrezzi operatore** ([`advanced/TOOLBOX.md`](advanced/TOOLBOX.md)), **modulo ruoli/dipartimenti** e i **libri-meta** (che documentano lo skeleton, non il tuo progetto).

## ⛔ Cosa NON è qui (le lezioni pagate care)
Testimoni-interni auto-scritti (ledger/heartbeat), multi-fronte come struttura fissa, cablaggi-non-misurati: **rilocano** `chi-controlla = chi-è-controllato`, non lo riducono. Un audit a freddo li smonta come teatro.

## In una riga
Kernel-corto + un gate che morde + 2 libri-metodo + l'operatore-che-punta. Il resto è opt-in; la lezione più preziosa è **non** costruire più del necessario.

*Assunzione: gesti `@file`/`!`/`/comando` sono di Claude Code; con un'altra IA traduci nell'equivalente.*
