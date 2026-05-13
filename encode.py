import random

from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

table = Table(title="Encryption Layers")

table.add_column("Layer", style="cyan")
table.add_column("Keys", style="magenta")
table.add_column("Cipher", style="green")

console.print(Panel("ENCRYPTION... ", style="bold magenta"))

msg = console.input("[purple]input text to encrypt: [/purple]")
console.print(f"[red]{msg}[/red]")
msg_bytes = list(msg.encode())
print(f"original message bytes were {msg_bytes}")
counter = 1

keys = []

results = []


def randencode(msg_bytes):
    key = random.randrange(1, 256, 2)

    keys.append(key)

    supercode = [(b * key) % 256 for b in msg_bytes]

    return supercode


results = []


for i in range(3):
    msg_bytes = randencode(msg_bytes)

    results.append({"layer": counter, "key": keys[i], "cipher": msg_bytes.copy()})

    counter += 1
    table.add_row(str(i + 1), str(keys), str(msg_bytes.copy()))

console.print(table)

print("final results list:")
console.print(f"[green]results {results}[/green]\n[blue]keys {keys}[/blue]")
