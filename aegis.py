import os, sys, json, requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

GROQ_API_KEY = "ENTER_YOUR_API_KEY_HERE"
API_URL = "https://api.groq.com/openai/v1/chat/completions"
console = Console()

def clean_json(text):
    """Termux clipboard bug fix"""
    bt = chr(96) * 3  
    if text.startswith(f"{bt}json"): text = text.replace(f"{bt}json", "", 1)
    if text.startswith(bt): text = text.replace(bt, "", 1)
    if text.endswith(bt): text = text.rsplit(bt, 1)[0]
    return text.strip()

def print_banner():
    banner = """
[bold #b000ff]
 █████╗ ███████╗ ██████╗ ██╗███████╗
██╔══██╗██╔════╝██╔════╝ ██║██╔════╝
███████║█████╗  ██║  ███╗██║███████╗
██╔══██║██╔══╝  ██║   ██║██║╚════██║
██║  ██║███████╗╚██████╔╝██║███████║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝╚══════╝[/bold #b000ff]
[bold white]Advanced AI Security Code Auditor[/bold white]
    """
    console.print(banner)

def analyze(file_path):
    if not os.path.exists(file_path):
        console.print(f"[bold red]❌ Error: {file_path} not found[/bold red]")
        return
    with open(file_path, "r") as f: code = f.read()
    
    console.print(f"[bold #b000ff]>>[/bold #b000ff] [dim]Target Acquired: {file_path}[/dim]\n")
    
    prompt = "You are a SAST Security Engineer. Output ONLY a valid JSON array with keys: severity (HIGH/MEDIUM/LOW), line_number, vulnerability, fix. No other text."
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "system", "content": prompt}, {"role": "user", "content": code}],
        "temperature": 0.2
    }
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    
    with console.status("[bold #b000ff]Running Threat Analysis...[/bold #b000ff]", spinner="bouncingBar"):
        try:
            res = requests.post(API_URL, headers=headers, json=payload)
            res.raise_for_status()
            out = clean_json(res.json()['choices'][0]['message']['content'])
            data = json.loads(out)
            report(data, file_path)
        except Exception as e:
            console.print(f"[bold red]❌ API Error: {str(e)}[/bold red]")

def report(data, file_path):
    console.print(Panel(f"[bold white]AEGIS SECURITY AUDIT[/bold white]\n[dim]Target: {file_path}[/dim]", border_style="#b000ff"))
    if not data:
        console.print("[bold green]✅ No vulnerabilities found. Code is clean![/bold green]\n")
    else:
        t = Table(show_header=True, header_style="bold white", border_style="#b000ff")
        t.add_column("Sev"); t.add_column("Line"); t.add_column("Vulnerability"); t.add_column("Fix")
        
        for v in data:
            sev = str(v.get("severity", "LOW")).upper()
            c = "bold red" if sev in ["HIGH","CRITICAL"] else "bold yellow" if sev=="MEDIUM" else "bold white"
            
            line_str = f"[bold #b000ff]{v.get('line_number')}[/bold #b000ff]"
            vuln_str = f"[bold white]{v.get('vulnerability')}[/bold white]"
            fix_str = f"[dim white]{v.get('fix')}[/dim white]"
            
            t.add_row(f"[{c}]{sev}[/{c}]", line_str, vuln_str, fix_str)
        
        console.print(t)
    
    # Bottom Watermark Upgrade
    console.print("[dim italic]Powered by Llama-3.1 | Engineered by[/dim italic] [bold #b000ff]PIYUSH[/bold #b000ff]\n", highlight=False)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_banner()
        console.print("[bold #b000ff]>>[/bold #b000ff] [bold white]Usage:[/bold white] python aegis.py [bold #b000ff]<file_to_scan>[/bold #b000ff]")
        console.print("[dim]Type[/dim] [bold #b000ff]python aegis.py --about[/bold #b000ff] [dim]for more info.[/dim]\n")
    else:
        arg = sys.argv[1].lower()
        if arg in ["--about", "-a", "--help", "-h"]:
            about_text = """
An elite [bold white]Static Application Security Testing (SAST)[/bold white] engine.
It scans source code to find critical vulnerabilities like SQLi, XSS, and hardcoded secrets.

[bold #b000ff]>>[/bold #b000ff] [bold white]Developer:[/bold white] [bold white on #b000ff] ✦ PIYUSH ✦ [/bold white on #b000ff]
[bold #b000ff]>>[/bold #b000ff] [bold white]Engine:[/bold white] [bold #b000ff]Llama-3.1 via Groq API[/bold #b000ff]

[bold white]Usage:[/bold white]
  python aegis.py [bold #b000ff]<filename>[/bold #b000ff]
"""
            console.print("\n")
            console.print(Panel(about_text.strip(), title="[bold #b000ff]✦ ABOUT AEGIS ✦[/bold #b000ff]", border_style="#b000ff", expand=False))
            console.print("\n")
        else:
            print_banner()
            analyze(arg)

