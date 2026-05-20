from rich.console import Console
from rich.table import Table

def print_top_artists(artists):
    table = Table(title="Kuunnelluimmat artistit")

    table.add_column("Artisti", style="cyan", no_wrap=True)

    for artist in artists:
        table.add_row(artist)

    console = Console()
    console.print(table)