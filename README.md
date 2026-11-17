> **Før du endrer noe:** Les [LES MEG FØRST](LES-MEG-FORST.md). Repoet har ny historikk; gamle kloner må ikke pushes tilbake.

# mottak-pod

Fast marimo-notebook for molab-pods. Poden henter alltid siste `agent.py` fra mottaket på skynet og melder seg inn der;
alt annet (jobber, kode, checkpoints, kommandoer) styres fra mottaket. Notebooken endres aldri.

## Ny pod

1. Åpne notebooken i molab fra dette repoet (synkes fra GitHub).
2. Velg GPU (RTX PRO 6000) under notebook specs.
3. Last opp `mottak.token` (agent-tokenet, én linje) via filpanelet. Filen er persistent for notebooken.
4. Notebooken kjører cellen ved åpning (`auto_instantiate = true` i prosjektfila). Poden dukker opp i dashboardet innen et minutt.

Agent-tokenet gir bare tilgang til agentrutene i mottaket (kode, oppdrag, puls, logg, checkpoints, inference-kø).
Admin-tokenet skal aldri inn i en notebook: molab-notebooks er lesbare for alle med lenken.

## Grenser i molab

- Maks 12 timer per pod, 90 min idle → poden dør. Keepalive-jobben holder GPU-en varm; checkpoints er atomiske, så en ny pod fortsetter der forrige sluttet.
- Bare utgående HTTPS. Ingen API for å starte pods — «ny pod» = åpne lenken.
