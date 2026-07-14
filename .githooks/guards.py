#!/usr/bin/env python3
"""guards.py — i gate-git CON DENTI VERI dello skeleton (template portabile).

Gira nel pre-commit (l'unico choke-point che ACCADE anche se l'agente "se ne
dimentica"). Solo testimoni con denti reali, provati-che-sparano:

  (a) SECRET-SCAN (BLOCCA): file-segreto staged (.env & varianti) o materiale-chiave
      reale in QUALSIASI file di testo staged (anche .md/tests — un segreto vero lì
      dentro leak-a lo stesso). Pattern comuni attivi di default; estendine per il tuo stack.
  (b) REF-CHECK  (BLOCCA): puntatore .md morto nei file auto-caricati (kernel/indice) → exit 1.
  (c) MAIN-WARN  (avviso): commit diretto su main.

Onestà: questi gate verificano la FORMA su artefatto-git, non la sostanza. Sono un
gradino reale (il commit accade → valgono anche se l'agente li ignora), NON la cura
di 'chi-controlla = chi-è-controllato' (per quella serve un'esternalità: umano, CI su
infra altrui, la realtà). Vedi advanced/library/lib-architettura-portabile.md.

Attiva:  git config core.hooksPath .githooks   (unix/mac: chmod +x .githooks/pre-commit)
Sorgenti ref: default CLAUDE.md + LIBRARY.md; override col FILE COMMITTATO
  .githooks/ref-sources.txt (una per riga) — così il gate è vivo in OGNI shell/GUI,
  non solo in quella dove hai fatto un export.
Waiver:  SKELETON_WAIVE="secret,ref" salta i check nominati. MAI --no-verify.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")  # Windows cp1252 + emoji

REPO = Path(__file__).resolve().parents[1]

# --- (a) secret-scan ---------------------------------------------------------
# nome-file: blocca .env e le sue varianti OVUNQUE nel basename (local.env,
# .env.prod.local, ...); consente solo gli esempi/template.
_ENV_NAME = re.compile(r"(^|\.)env(\.|$)", re.I)
_ENV_ALLOW = (".example", ".sample", ".template", ".dist")
# contenuto: materiale-chiave reale, pattern a basso falso-positivo, ATTIVI di default.
# Aggiungine per il TUO stack (l'omissione è un falso-senso-di-sicurezza).
SECRET_CONTENT = [
    r"sk_live_[0-9A-Za-z]{16,}", r"sk_test_[0-9A-Za-z]{16,}", r"\bsbp_[0-9a-f]{40,}\b",
    r"AKIA[0-9A-Z]{16}",                       # AWS access key id
    r"AIza[0-9A-Za-z_\-]{35}",                 # Google API key
    r"gh[pousr]_[0-9A-Za-z]{36}",              # GitHub token
    r"xox[baprs]-[0-9A-Za-z\-]{10,}",          # Slack token
    r"npm_[0-9A-Za-z]{36}",                    # npm token
    r"-----BEGIN (?:RSA |EC |OPENSSH |PGP )?PRIVATE KEY-----",
    # assegnazione di un segreto lungo a una variabile dal nome sospetto
    r"(?i)(secret|token|passwd|password|api[_-]?key|access[_-]?key)['\"]?\s*[:=]\s*['\"][^'\"\s]{16,}['\"]",
]
_SECRETS = [re.compile(p) for p in SECRET_CONTENT]
_BINARY_EXT = (".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".gz", ".parquet",
               ".lock", ".ico", ".woff", ".woff2", ".ttf", ".mp4", ".webp")

# --- (b) ref-check -----------------------------------------------------------
def _ref_sources() -> list[str]:
    cfg = REPO / ".githooks" / "ref-sources.txt"
    if cfg.exists():
        return [l.strip() for l in cfg.read_text(encoding="utf-8").splitlines()
                if l.strip() and not l.startswith("#")]
    env = [s.strip() for s in os.environ.get("SKELETON_REF_SOURCES", "").split(",") if s.strip()]
    return env or ["CLAUDE.md", "LIBRARY.md"]

_MD_LINK = re.compile(r"\]\(([^)#]+\.md)(?:#[^)]*)?\)")           # [x](path.md)
# bare path.md, ma SOLO se delimitato a sinistra da spazio/backtick (evita di
# spezzare i nomi-con-trattino e di catturare i placeholder ‹...›).
_BARE_MD = re.compile(r"(?:(?<=\s)|(?<=`))((?:[\w./-]+/)?[\w.-]+\.md)")


def _run(cmd: list[str]) -> str:
    # decodifica UTF-8 esplicita: text=True userebbe il locale (cp1252 su Windows) e
    # crasherebbe su contenuti UTF-8 (emoji, «»/‹›) → un pre-commit che esplode blocca tutto.
    return subprocess.check_output(cmd, stderr=subprocess.DEVNULL).decode("utf-8", "replace").strip()


def _staged() -> list[str]:
    try:
        out = _run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"])
    except subprocess.CalledProcessError:
        return []
    return [l for l in out.splitlines() if l.strip()]


def check_secrets(staged: list[str]) -> int:
    rc = 0
    for f in staged:
        name = Path(f).name
        if _ENV_NAME.search(name) and not name.lower().endswith(_ENV_ALLOW):
            print(f"🚫 SECRET: mai committare il file-segreto '{f}'. Usa .env.example / docs.", file=sys.stderr)
            rc = 1
            continue
        if f.lower().endswith(_BINARY_EXT):
            continue
        try:
            content = _run(["git", "show", f":{f}"])
        except subprocess.CalledProcessError:
            continue
        if content and any(rx.search(content) for rx in _SECRETS):
            print(f"🚫 SECRET: materiale-credenziale reale in '{f}' (staged). Se è un esempio, usa un placeholder.", file=sys.stderr)
            rc = 1
    return rc


def check_ref() -> int:
    sources = _ref_sources()
    present = [s for s in sources if (REPO / s).exists()]
    missing = [s for s in sources if not (REPO / s).exists()]
    if not present:
        print(f"⚠️  REF-CHECK INATTIVO: nessuna sorgente {sources} esiste. "
              f"Rinominato il kernel? aggiorna .githooks/ref-sources.txt. Il gate NON verifica nulla.", file=sys.stderr)
        return 0
    if missing:
        print(f"⚠️  REF-CHECK: sorgente attesa mancante {missing} (verifico solo {present}; se hai rinominato, aggiorna .githooks/ref-sources.txt).", file=sys.stderr)
    dead: list[tuple[str, str]] = []
    for src in present:
        text = (REPO / src).read_text(encoding="utf-8", errors="replace")
        text = re.sub(r"```.*?```", "", text, flags=re.S)  # ignora i fenced-code (falsi-positivi)
        tokens = set(_MD_LINK.findall(text)) | set(_BARE_MD.findall(text))
        for tok in tokens:
            tok = tok.strip()
            if not tok or "‹" in tok or "<" in tok or tok.startswith(("http", "mailto")):
                continue
            if not (REPO / tok).exists():
                dead.append((src, tok))
    if dead:
        print(f"🚫 REF-CHECK: {len(dead)} puntatore/i .md morto/i nei file auto-caricati:", file=sys.stderr)
        for src, tok in dead[:8]:
            print(f"    [{src}] → '{tok}' non esiste su disco", file=sys.stderr)
        print("    Un puntatore-morto nel pavimento avvelena ogni sessione. Correggi il path o rimuovi la citazione.", file=sys.stderr)
        return 1
    return 0


def check_main() -> int:
    try:
        branch = _run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    except subprocess.CalledProcessError:
        branch = "HEAD"
    if branch == "main":
        print("⚠️  main: commit diretto su main sconsigliato (preferisci un branch + PR; branch-protection = net server-side).", file=sys.stderr)
    return 0


def main() -> int:
    waive = {w.strip() for w in os.environ.get("SKELETON_WAIVE", "").split(",") if w.strip()}
    staged = _staged()
    if not staged:
        return 0
    rc = 0
    if "secret" not in waive:
        rc |= check_secrets(staged)
    if "ref" not in waive:
        rc |= check_ref()
    check_main()
    if rc:
        print("\nGate-con-denti fallito. Correggi sopra (o SKELETON_WAIVE=…; MAI --no-verify: spegne anche i secret-scan).", file=sys.stderr)
    return rc


if __name__ == "__main__":
    sys.exit(main())
