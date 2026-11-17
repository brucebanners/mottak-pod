# Fast notebook for molab-pods. Endres ikke. Kjører ved åpning (auto_instantiate) og starter agenten fra mottaket.
# Tokenet ligger IKKE her: last opp filen `mottak.token` (agent-tokenet, én linje) via filpanelet én gang per notebook.
import marimo

__generated_with = "0.25.1"
app = marimo.App()


@app.cell
def _():
    import os, pathlib, subprocess, urllib.request
    tok = pathlib.Path("mottak.token")
    assert tok.exists(), "Last opp mottak.token (agent-tokenet) via filpanelet"
    TOKEN = tok.read_text().strip()
    subprocess.run(["pkill", "-f", "agent.py"])
    req = urllib.request.Request("https://mottak.samsai.no/kode/agent.py", headers={"X-Token": TOKEN, "User-Agent": "skynet-agent/1"})
    open("agent.py", "wb").write(urllib.request.urlopen(req, timeout=60).read())
    p = subprocess.Popen(["python3", "agent.py"], stdout=open("agent.log", "w"), stderr=subprocess.STDOUT,
                         start_new_session=True, env=dict(os.environ, MOTTAK_TOKEN=TOKEN))
    print("agent PID", p.pid)
    return


if __name__ == "__main__":
    app.run()
