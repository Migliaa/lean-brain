# .githooks — i gate-git con denti veri

## Attivazione (una volta, dalla root del repo)
```sh
git config core.hooksPath .githooks
# unix/mac: chmod +x .githooks/pre-commit
```
⚠️ **Hai già husky / un altro pre-commit?** NON riassegnare `core.hooksPath` (spegneresti il loro). Invece fai chiamare `.githooks/guards.py` dal tuo hook esistente. Controlla prima: `git config --get core.hooksPath`.

## Cosa blocca
| Check | Denti | Cosa |
|---|---|---|
| **secret-scan** | 🚫 BLOCCA | file-segreto (`.env` & varianti) o chiave reale (Stripe/AWS/GCP/GitHub/Slack/npm/PEM + assegnazioni sospette) in **qualsiasi** file di testo staged |
| **ref-check** | 🚫 BLOCCA | puntatore `.md` morto nei file di `.githooks/ref-sources.txt` |
| **main-warn** | ⚠️ avvisa | commit diretto su `main` |

**Config sorgenti ref-check:** `.githooks/ref-sources.txt` (committato, una per riga). Rinominato il kernel? aggiornalo lì — **non** con un `export` (che vive solo nella tua shell e lascia il gate morto altrove).
**Estendi il secret-scan** per il tuo stack: aggiungi pattern in `SECRET_CONTENT` (dentro `guards.py`).

## La prova-che-spara (fallo prima di fidarti — `lib-verifica-avversariale`)
Un gate «tutto verde e 0 blocchi» è verde-d'aspetto. Verifica che i denti mordano DAVVERO:
```sh
# 1) ref-check DEVE bloccare un path morto
echo '[rotto](library/lib-non-esiste.md)' >> CLAUDE.md
git add CLAUDE.md && git commit -m "test"      # atteso: 🚫 REF-CHECK, exit 1
git checkout CLAUDE.md                            # ripristina

# 2) secret-scan DEVE bloccare una chiave finta del TUO stack
#    (NOME sacrificale, MAI un vero .env: touch .env non svuota un .env esistente!)
printf 'aws_key="AKIA%s"\n' 0000000000000000 > .secret-probe.txt   # AKIA + 16 char = chiave finta
git add -f .secret-probe.txt && git commit -m "test"   # atteso: 🚫 SECRET, exit 1
git rm --cached .secret-probe.txt && rm .secret-probe.txt
```
Se uno dei due NON blocca, il gate non ha denti: sistemalo prima di dichiararlo attivo.

## Onestà
Questi gate verificano la **forma** su artefatto-git, non la **sostanza**. Sono un gradino reale (il commit accade → il gate vale anche se l'agente se ne dimentica), **non** la cura di `chi-controlla = chi-è-controllato` — quella richiede un'esternalità (umano, CI su infra altrui, la realtà). Vedi `advanced/library/lib-architettura-portabile.md`.
