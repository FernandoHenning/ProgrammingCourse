from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import IntPrompt
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import box
from rich.theme import Theme
from rich.text import Text
import time

# Definir tema personalizado
custom_theme = Theme({
    "blanco": "white",
    "amarillo": "yellow",
    "naranja": "bright_red",
    "verde": "green",
    "azul": "blue",
    "marron": "bright_yellow",
    "negro": "black on white"
})

# Inicializar consola
console = Console(theme=custom_theme)

# Función para obtener cinturón
def obtener_cinturon(kihon: int, katas: int, kumite: int, mental: int) -> str:
    if (kihon == 1) and (katas == 1) and (kumite == 1) and (mental == 1):
        return "Blanco"
    elif (kihon == 2) and (katas == 2) and (kumite == 2) and (mental == 2):
        return "Amarillo"
    elif (kihon == 3) and (katas == 3) and (kumite == 3) and (mental == 3):
        return "Naranja"
    elif (kihon == 4) and (katas == 4) and (kumite == 4) and (mental == 4):
        return "Verde"
    elif (kihon == 5) and (katas == 5) and (kumite == 5) and (mental == 5):
        return "Azul"
    elif (kihon == 6) and (katas == 6) and (kumite == 6) and (mental == 6):
        return "Marrón"
    elif (kihon == 7) and (katas == 7) and (kumite == 7) and (mental == 7):
        return "Negro"
    else:
        return "No califica para un cinturón estándar"

def main():
    # Mostrar título
    console.print(Panel.fit("[bold yellow]SISTEMA DE EVALUACIÓN DE KARATE[/bold yellow]",
                          border_style="yellow", box=box.DOUBLE))
    
    console.print("\n[bold]Ingrese los niveles del estudiante en cada categoría[/bold]\n")
    
    # Crear tabla de referencia de cinturones
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
    
    console.print(table)
    console.print("")
    
    # Variables para almacenar las puntuaciones
    puntaje_kihon = 0
    puntaje_katas = 0
    puntaje_kumite = 0
    puntaje_mental = 0
    
    try:
        # Obtener entrada del usuario con validación
        puntaje_kihon = IntPrompt.ask("[bold cyan]KIHON[/bold cyan] - Ingresa el nivel del estudiante", 
                                      choices=["1", "2", "3", "4", "5", "6", "7"])
        
        puntaje_katas = IntPrompt.ask("[bold magenta]KATAS[/bold magenta] - Ingresa el nivel del estudiante", 
                                      choices=["1", "2", "3", "4", "5", "6", "7"])
        
        puntaje_kumite = IntPrompt.ask("[bold green]KUMITE[/bold green] - Ingresa el nivel del estudiante", 
                                       choices=["1", "2", "3", "4", "5", "6", "7"])
        
        puntaje_mental = IntPrompt.ask("[bold yellow]MENTAL[/bold yellow] - Ingresa el nivel del estudiante", 
                                       choices=["1", "2", "3", "4", "5", "6", "7"])
        
        # Mostrar progreso de análisis
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold green]Calculando resultado...[/bold green]"),
        ) as progress:
            task = progress.add_task("", total=100)
            for _ in range(10):
                progress.update(task, advance=10)
                time.sleep(0.1)
                
        # Calcular el cinturón
        cinturon = obtener_cinturon(
            kihon=puntaje_kihon,
            katas=puntaje_katas,
            kumite=puntaje_kumite,
            mental=puntaje_mental
        )
        
        # Resumen final
        console.print("\n[bold]Resultados de la Evaluación:[/bold]")
        resultados = Table(show_header=False, box=box.SIMPLE)
        resultados.add_column("Categoría", style="bold")
        resultados.add_column("Nivel")
        
        resultados.add_row("KIHON", f"Nivel {puntaje_kihon}")
        resultados.add_row("KATAS", f"Nivel {puntaje_katas}")
        resultados.add_row("KUMITE", f"Nivel {puntaje_kumite}")
        resultados.add_row("MENTAL", f"Nivel {puntaje_mental}")
        
        console.print(resultados)
        
        # Mostrar resultado final
        color_clase = cinturon.lower() if cinturon in ["Blanco", "Amarillo", "Naranja", "Verde", "Azul", "Marrón", "Negro"] else "bold red"
        texto_resultado = Text(f"El estudiante califica para el cinturón: ", style="bold")
        texto_resultado.append(cinturon, style=f"bold {color_clase}")
        
        console.print(Panel(texto_resultado, border_style="green", box=box.DOUBLE))
        
    except KeyboardInterrupt:
        console.print("\n[bold red]Programa interrumpido por el usuario.[/bold red]")
    except ValueError as e:
        console.print(f"\n[bold red]Error de entrada: {e}[/bold red]")
    except Exception as e:
        console.print(f"\n[bold red]Error inesperado: {e}[/bold red]")
    finally:
        console.print("\n[italic]Gracias por usar el Sistema de Evaluación de Karate.[/italic]")

if __name__ == "__main__":
    main()