from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, Input, RichLog
from rich.text import Text

class SearchResult(Static):
    def __init__(self, title: str, link: str, description: str) -> None:
        super().__init__()
        self.title = title
        self.link = link
        self.description = description

    def render(self) -> str:
        return (
            f"[bold blue]{self.title}[/bold blue]\n"
            f"[cyan]{self.link}[/cyan]\n"
            f"{self.description}"
        )

class SearchApp(App):
    CSS = """
    Screen { layout: vertical; }
    #header { height: 3; content-align: center middle; border: round yellow; }
    #search_input { height: 3; border: round green; }
    #main_area { height: 1fr; }
    #results { border: round cyan; padding: 1; align: center top; }
    SearchResult { width: 100%; max-width: 950; padding: 0 0; margin: 0 0; border: round white; background: $surface; }
    #console { border: round magenta; }
    #command_panel { height: 3; border: round blue; content-align: center middle; }
    """

    def __init__(self, query_handler=None):
        super().__init__()
        self.query_handler = query_handler  # Callback to main file

    def compose(self) -> ComposeResult:
        yield Static("SearchApp — Type a query and press Enter", id="header")
        yield Input(placeholder="Type search query and press Enter", id="search_input")
        with Horizontal(id="main_area"):
            yield Vertical(id="results")
            yield RichLog(id="console", highlight=False, markup=True)
        yield Static("Commands: CTRL + Q : Quit", id="command_panel")

    def on_mount(self) -> None:
        self.log_message("INFO", "Application started.")
        self.log_message("INFO", "Waiting for search input...")

    def on_input_submitted(self, message: Input.Submitted) -> None:
        query = message.value.strip()
        if query:
            if self.query_handler:
                self.query_handler(query)

    def add_results(self, results):
        container = self.query_one("#results", Vertical)
        for item in results:
            title = item.get("title", "")
            link = item.get("link", "")
            desc = item.get("desc", "")
            container.mount(SearchResult(title, link, desc))

    def log_message(self, level: str, msg: str):
        console = self.query_one("#console", RichLog)
    
        level_colors = {
            "INFO": "cyan",
            "WARN": "yellow",
            "ERROR": "red",
            "DEBUG": "green"
        }
    
        color = level_colors.get(level.upper(), "white")
        formatted = f"[{color}][{level.upper()}] {msg}[/{color}]"
    
        console.write(formatted)