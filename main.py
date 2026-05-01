import typer
from rich import print
from file_writer import save_markdown
from generator import generate


def main(
      idea: str = typer.Argument(..., help="Natural-language product idea to design."),
      output: str | None = typer.Option(None, "--output", "-o", help="Optional markdown output path."),
):
      print("[cyan]Generating system design...[/cyan]")
    
      result = generate(idea)

      output_path = save_markdown(result, output)

      print(result)
      print(f"[green]\nSaved output to: {output_path}[/green]")

      return 0


if __name__ == "__main__":
    typer.run(main)
