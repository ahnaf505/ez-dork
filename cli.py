from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich import box
from rich.markdown import Markdown

console = Console()

def main_banner():
	md = Markdown("# ez-dork == ez-dork == ez-dork")
	console.print(md, style="dodger_blue2")

def help_menu():
	description = Text(
    "ez-dork is a powerful utility that helps you do OSINT using dorking, "
  	"automate dorking on multiplesearch engine.",
    style="italic bright_white"
	)
	console.print(Align(description, align="left"))
	
	table = Table(title="📜 Commands", box=box.ROUNDED, border_style="bright_cyan")
	table.add_column("Command", style="bold green", no_wrap=True)
	table.add_column("Description", style="white")
	table.add_column("Example", style="bright_yellow")
	
	table.add_row("fullname", "Initialize search using a full name", '`main.py fullname "{full_name}"`')
	table.add_row("phone", "Initialize search using a phone number", '`main.py phone {country_code} {phone_number}`')
	table.add_row("address", "Initialize search using an address", '`main.py address "{address}`')
	table.add_row("social", "Initialize search using a social media handle", '`main.py social "{social_media_handle}"`')
	table.add_row("alias", "Initialize search using an alias", '`main.py alias "{name_alias}"`')
	
	console.print(table)
	
	tips_text = Text.from_markup(
	    "[bold bright_magenta]💡 Tips:[/bold bright_magenta]\n"
	    "- Use [green]--verbose[/green] for detailed logs.\n"
	    "- For phone number dorking [red]do not[/red] use dashed or spaces.\n"
	    "- Run [yellow]ez-dork config[/yellow] to customize settings."
	)
	console.print(Panel(tips_text, title="Quick Tips", border_style="magenta", expand=False))
	
	footer = Text("Made with ❤️  by Ahnaf", style="bold white on dark_green", justify="center")
	console.print(Panel(footer, expand=True, style="green"))


