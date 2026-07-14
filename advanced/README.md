# advanced/ — opt-in, solo quando il nucleo non basta

Il nucleo (root) è kernel + gate + 2 libri-metodo. Qui c'è ciò che paga il suo peso **solo a una certa scala**. Non copiarlo tutto per riflesso: prendi il pezzo quando ne senti il bisogno reale (dal volume, non dall'idea).

| File | Prendilo quando… |
|---|---|
| `INTEGRATE.md` | vuoi che la tua IA adotti l'architettura su un progetto **già avviato** (valuta → integra → ti spiega). |
| `ADOPT.md` | vuoi la guida al merge dettagliata (passi manuali, collisioni, collaudo, anti-calo-prestazioni). |
| `USAGE.md` | vuoi la spiegazione d'uso a parole semplici, per un umano. |
| `LIBRARY.md` + `.claude/commands/library.md` | hai accumulato **molti** libri di dominio e ti serve un indice + il comando `/library`. Con 2-4 libri, `@file` diretto basta. |
| `TOOLBOX.md` | vuoi la cassetta-attrezzi dell'operatore (leve + catalogo libri + regola dei libri da puntare a mano). |
| `library/lib-ruoli-coordinamento.md` | hai **vera divisione-del-lavoro** ricorrente (più tipi di lavoro concorrenti) e l'umano-tramite è diventato il collo di bottiglia. Solo/semplice → **non usarlo**. |
| `library/lib-architettura-portabile.md` | vuoi i razionali profondi dello skeleton e come ri-esportarlo (è **meta**: documenta lo skeleton, non il tuo progetto). |

**Regola:** questi documentano o estendono; il valore-base è nel nucleo. Se copi `LIBRARY.md`, aggiorna `.githooks/ref-sources.txt` per includerlo (così il ref-check ne guarda i puntatori).
