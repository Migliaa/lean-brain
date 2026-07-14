# USAGE — come si usa, in parole semplici

> Questa guida è per **un umano che non c'era**. Zero gergo. Se una parola-tecnica serve, è tradotta qui sotto.

**Mini-glossario** (i 4 termini che ricorrono):
- **kernel** = il file di istruzioni che l'agente legge **a ogni sessione, automaticamente**. Costa: ogni riga qui la "paga" ogni volta. → tienilo corto.
- **libro** = un file di conoscenza che l'agente legge **solo quando serve** (non automaticamente). Costa zero finché non lo apri.
- **bibliotecario** = l'indice dei libri (`LIBRARY.md`). Gli dici «guarda qui» e lui trova il libro giusto.
- **gate** = un controllo che gira **da solo** quando fai `git commit`. Se qualcosa è sbagliato, **ferma** il commit.

---

## In una frase
L'agente parte leggendo **poco** (il kernel), e tira la conoscenza **al momento giusto** (i libri) invece di tenersela tutta in testa. Più un guardiano automatico sui commit e una cassetta di comandi per te.

## I pezzi, a cosa servono, chi fa cosa
| Pezzo | A cosa serve | Cosa fai TU | Cosa fa l'agente |
|---|---|---|---|
| `CLAUDE.md` (kernel) | le istruzioni-base sempre attive | lo scrivi corto una volta | lo legge a ogni sessione |
| `LIBRARY.md` + `library/` | la conoscenza pesante, a richiesta | ci scrivi i tuoi "libri" | li apre solo quando un tema combacia |
| `.githooks/` (gate) | impedire errori nei commit (segreti, link rotti) | lo attivi una volta | ci sbatte contro se sbaglia, e si corregge |
| `TOOLBOX.md` | le leve che usi TU mentre scrivi | lo tieni a fianco tastiera | — |

## L'uso quotidiano: 3 gesti
1. **Puntare un libro.** Quando stai per chiedere qualcosa di importante, scrivi `@LIBRARY.md` (o `/library`) + cosa stai per fare. L'agente ti dice quale libro apre e ne cita una riga — così **vedi** che l'ha usato. *(Perché non lo fa da solo? Perché da solo non è affidabile: sei tu che glielo punti al momento giusto. È il pezzo che funziona meglio.)*
2. **Far girare un comando vero.** Scrivi `! <comando>` (es. `! npm test`). L'output entra nella conversazione: l'agente vede il **risultato reale**, non uno immaginato.
3. **Lasciar bloccare il commit.** Se provi a committare un segreto o un link rotto, il gate ferma tutto e ti dice cosa. Non è un fastidio: è la rete.

## I vantaggi concreti (come capisci che sta funzionando)
| Prima | Dopo |
|---|---|
| l'agente parte leggendo tutto → lento, contesto pieno subito | parte leggero → più spazio per il lavoro vero |
| la conoscenza sparsa, spesso ignorata | tirata al momento giusto, e **verificabile** (la citazione) |
| un segreto committato per sbaglio | il commit **bloccato** prima che accada |
| tu che ripeti le stesse istruzioni | le leve nel `TOOLBOX` |

## Segnali che NON sta funzionando (e perché)
- **L'agente non apre mai un libro** → non glieli stai puntando: usa `@LIBRARY.md`. È il gesto n°1.
- **Il commit non blocca niente mai** → il gate non è attivo o non ha denti. Fai la prova in `.githooks/README.md`.
- **Va più lento di prima** → hai messo troppa roba nel kernel. Il kernel deve restare corto: il resto sono libri. Vedi `ADOPT.md → Come NON perdere prestazioni`.

➡️ **Hai già un progetto avviato e vuoi portarci questo?** → `ADOPT.md`.
