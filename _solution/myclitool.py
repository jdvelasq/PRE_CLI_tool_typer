"""Command line interface (CLI) tool"""

#
# Estructura:
#
# mycli +--- command_1
#       |    +--- subcommand_1
#       |    \--- subcommand_2
#       |
#       +--- command_2
#       |    +--- subcommand_1
#       |    \--- subcommand_2
#


import typer

app = typer.Typer(help="Herramienta de linea de comandos")

# =========================================================================
# COMMAND1 Group
# =========================================================================
command1_app = typer.Typer(help="Comandos relacionados con COMMAND1")
app.add_typer(command1_app, name="command1")


@command1_app.command("run")
def command_1_subcommand_1(a: str = typer.Option(..., help="Valor del parametro a")):
    """Ejecuta un subcomando 1-1"""
    typer.echo(f"\n---> Ejecutando command 1 subcommand 1: a = {a}\n")


@command1_app.command("stop")
def command_1_subcommand_2(b: str = typer.Option(..., help="Valor del parametro b")):
    """Ejecuta un subcomando 1-2"""
    typer.echo(f"\n---> Ejecutando command 1 subcommand 2: b = {b}\n")


# =========================================================================
# COMMAND2 Group
# =========================================================================
command2_app = typer.Typer(help="Comandos relacionados con COMMAND2")
app.add_typer(command2_app, name="command2")


@command2_app.command("jump")
def command_2_subcommand_1(c: str = typer.Option(..., help="Valor del parametro c")):
    """Ejecuta un subcomando 2-1"""
    typer.echo(f"\n---> Ejecutando command 2 subcommand 1: c = {c}\n")


@command2_app.command("cry")
def command_2_subcommand_2(d: str = typer.Option(..., help="Valor del parametro d")):
    """Ejecuta un subcomando 2-2"""
    typer.echo(f"\n---> Ejecutando command 2 subcommand 2: d = {d}\n")


if __name__ == "__main__":
    app()
