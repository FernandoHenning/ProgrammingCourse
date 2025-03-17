from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import IntPrompt
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import box
from rich.theme import Theme
from rich.text import Text

from logic import obtener_cinturon
from logic import alumnos
from logic import cinturon_por_alumno
import time

custom_theme = Theme(
    {
        "blanco": "white",
        "amarillo": "yellow",
        "naranja": "bright_red",
        "verde": "green",
        "azul": "blue",
        "marron": "bright_yellow",
        "negro": "black on white",
    }
)

console = Console(theme=custom_theme)


def render_cli():
    try:
        for alumno in alumnos:
            render_title(alumno)

            guide_table = build_guide_table()
            console.print(guide_table)
            console.print("")

            puntaje_kihon = 0
            puntaje_katas = 0
            puntaje_kumite = 0
            puntaje_mental = 0

            puntaje_kihon = prompt_user_for_score_of("KIHON")
            puntaje_katas = prompt_user_for_score_of("KATAS")
            puntaje_kumite = prompt_user_for_score_of("KUMITE")
            puntaje_mental = prompt_user_for_score_of("MENTAL")

            render_progress_bar()
            cinturon = obtener_cinturon(
                kihon=puntaje_kihon,
                katas=puntaje_katas,
                kumite=puntaje_kumite,
                mental=puntaje_mental,
            )

            cinturon_por_alumno[alumno] = cinturon

            results_table = build_results_table(
                puntaje_kihon=puntaje_kihon,
                puntaje_katas=puntaje_katas,
                puntaje_kumite=puntaje_kumite,
                puntaje_mental=puntaje_mental,
            )
            render_result(cinturon=cinturon, resultados=results_table)
            time.sleep(2)
            console.clear()

        print_results_per_student()

    except KeyboardInterrupt:
        console.print("\n[bold red]Programa interrumpido por el usuario.[/bold red]")
    except ValueError as e:
        console.print(f"\n[bold red]Error de entrada: {e}[/bold red]")
    except Exception as e:
        console.print(f"\n[bold red]Error inesperado: {e}[/bold red]")
    finally:
        console.print(
            "\n[italic]Gracias por usar el Sistema de Evaluación de Karate.[/italic]"
        )


def prompt_user_for_score_of(score_of_name: str) -> int:
    return IntPrompt.ask(
        f"[bold cyan]{score_of_name}[/bold cyan] - Ingresa el nivel del estudiante",
        choices=["1", "2", "3", "4", "5", "6", "7"],
    )


def build_guide_table():
    table = Table(title="[bold]Guía de Cinturones[/bold]")
    table.add_column("Nivel", justify="center", style="bold")
    table.add_column("Cinturón", style="bold")
    table.add_column("Color", style="bold")

    table.add_row("1", "Blanco", "[blanco]■■■■■[/blanco]")
    table.add_row("2", "Amarillo", "[amarillo]■■■■■[/amarillo]")
    table.add_row("3", "Naranja", "[naranja]■■■■■[/naranja]")
    table.add_row("4", "Verde", "[verde]■■■■■[/verde]")
    table.add_row("5", "Azul", "[azul]■■■■■[/azul]")
    table.add_row("6", "Marrón", "[marron]■■■■■[/marron]")
    table.add_row("7", "Negro", "[negro]■■■■■[/negro]")
    return table


def render_title(alumno: str):
    console.print(
        Panel.fit(
            "[bold yellow]SISTEMA DE EVALUACIÓN DE KARATE[/bold yellow]",
            border_style="yellow",
            box=box.DOUBLE,
        )
    )
    console.print(f"\n[bold green]Evaluando a {alumno}[/bold green]\n")
    console.print(
        "\n[bold]Ingrese los niveles del estudiante en cada categoría[/bold]\n"
    )


def render_progress_bar():
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold green]Calculando resultado...[/bold green]"),
    ) as progress:
        task = progress.add_task("", total=100)
        for _ in range(10):
            progress.update(task, advance=10)
            time.sleep(0.1)


def print_results_per_student():
    table = Table(title="[bold]Resultados por alumno[/bold]")
    table.add_column("Alumno", justify="center", style="bold")
    table.add_column("Nuevo Cinturón", style="bold")
    for alumno, cinturon in cinturon_por_alumno.items():
        table.add_row(alumno, f"[{cinturon.lower()}]■■■■■[/{cinturon.lower()}]")
    console.print(table)


def build_results_table(
    puntaje_kihon: int, puntaje_katas: int, puntaje_kumite: int, puntaje_mental: int
):
    resultados = Table(show_header=False, box=box.SIMPLE)
    resultados.add_column("Categoría", style="bold")
    resultados.add_column("Nivel")

    resultados.add_row("KIHON", f"Nivel {puntaje_kihon}")
    resultados.add_row("KATAS", f"Nivel {puntaje_katas}")
    resultados.add_row("KUMITE", f"Nivel {puntaje_kumite}")
    resultados.add_row("MENTAL", f"Nivel {puntaje_mental}")
    return resultados


def render_result(cinturon: str, resultados: Table):
    console.print("\n[bold]Resultados de la Evaluación:[/bold]")

    console.print(resultados)

    texto_resultado = Text(f"El estudiante califica para el cinturón: ", style="bold")
    texto_resultado.append(cinturon, style=f"bold")

    console.print(Panel(texto_resultado, border_style="green", box=box.DOUBLE))
