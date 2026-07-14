# 🧰 TOOLBOX — la cassetta degli attrezzi (per il committente)  ‹TEMPLATE›

> **Cos'è:** le leve che TU usi mentre scrivi il prompt per rendere l'agente più accurato/efficiente. Tienila a fianco della tastiera. **Non auto-caricata** (zero costo-token): è tua.
> **Perché esiste:** la vera esternalità che migliora un agente LLM **sei tu** — i meccanismi che si auto-gestiscono il contesto *rilocano* il problema (`controllore=controllato`); tu che al momento giusto punti il file/libro/comando giusto sei enforcement reale.

---

## A. 📚 LA BIBLIOTECA MANUALE (il cuore)
Da solo l'agente **non pulla affidabilmente** i libri. La cura: **tu glieli punti.** Due modi:

**① Semplice (raccomandato) — punta il BIBLIOTECARIO:** `@LIBRARY.md` + «fai il bibliotecario» (o `/library <cosa stai per fare>`). L'agente dichiara quale libro pulla, lo legge, ne cita una riga (vedi a vista che l'ha usato), poi procede. **Un solo comando.**
**② Diretto (quando SAI quale) — punta il LIBRO:** `@library/lib-X.md` → il contenuto entra **garantito** nel contesto. Più forte, ma devi sapere quale.

### 📚 CATALOGO DEI LIBRI
> Legenda: **⭐ portante** · **📌 punta l'INDIRIZZO diretto** (`@library/lib-X.md`) — la sola `/library` rischia di NON farglielo pullare (vedi la regola sotto).

**Universali (inclusi nello skeleton):**
| Libro | Serve quando | |
|---|---|---|
| `lib-verifica-avversariale` | prima di finalizzare qualcosa di costoso/irreversibile | ⭐ 📌 |
| `lib-quando-fermarsi` | l'agente itera/progetta senza spedire | ⭐ 📌 |
| `lib-architettura-portabile` | esporti/riusi l'architettura | |
| `lib-ruoli-coordinamento` | (opzionale) hai vera divisione-del-lavoro | |

**⚠️ La regola del 📌 (perché alcuni vanno puntati a mano):** un libro va puntato **all'indirizzo diretto** quando il suo trigger scatta **proprio nel momento in cui l'agente è meno capace di riconoscere che gli serve** — cioè quando è *troppo sicuro* del proprio lavoro (`verifica-avversariale`) o *assorbito nel giro* (`quando-fermarsi`). Lì `/library` non basta: l'agente non si auto-diagnostica. **Sei tu** a scrivere `@library/lib-….md`. È l'insight-chiave: i libri più preziosi sono quelli che l'agente da solo salterebbe.

**Di dominio (li aggiungi tu):** `‹elenca qui i tuoi libri; marca ⭐ i portanti e 📌 quelli da puntare a mano›`

**Opzionali dei ruoli/dipartimenti:** se attivi un ruolo (`lib-ruoli-coordinamento`), porta i **suoi** libri — 1 operativo («come funziona il ruolo») + N di dominio. Elencali qui sotto il ruolo (lo skeleton non li fornisce, sono tuoi):
`‹ruolo› → operativo: ‹lib-…› · dominio: ‹lib-…, lib-…›`

---

## B. 🔧 LE LEVE (Claude Code — verificate)
| Leva | Cosa fa | Quando |
|---|---|---|
| **`@percorso/file`** | inserisce il **contenuto** del file nel contesto (`@` + Tab) | quando **sai già** quale file serve → più veloce/accurato che farlo cercare |
| **`! comando`** | esegue un comando **reale**, l'output entra nel contesto | per far vedere **risultati veri** (test, build, git) invece di farli immaginare |
| **`Shift+Tab` → Plan mode** | pianifica **senza toccare i file** | prima di refactor grossi / per vedere l'impatto |
| **`/compact`** | riassume la conversazione, libera contesto | conversazione lunga / contesto pieno |
| **`/fast`** | fast mode (stessa qualità, più veloce) | lavoro meccanico |
| **direttive-testo** | modulano il comportamento | «effort pieno» su design · «fermati e proponi opzioni» · «onestà brutale» · «consulta prima @libro» |

---

## C. 🎯 PATTERN D'ORO (scenario → mossa) — riempi col tuo dominio
- **«‹task ricorrente›»** → `@library/lib-….md` + `@‹file›` + «‹direttiva›»
- **«Fammi vedere se i test passano»** → `! ‹comando-test›` (risultato vero, non immaginato)
- **«Prima di una scelta irreversibile»** → `@library/lib-verifica-avversariale.md` + «premortem a freddo»

---

## D. ⚙️ CRISTALLIZZARE (opzionale)
Se un pattern torna spesso, cristallizzalo in un **custom slash-command** (`.claude/commands/<nome>.md`) → lo invochi con `/<nome>`. Ma solo dai pattern che usi davvero (mai dalla tecnologia).

> **Manutenzione:** questa cassetta cresce dall'**uso**, non dall'idea.
