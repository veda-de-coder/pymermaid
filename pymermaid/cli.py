"""
Command-line interface for PyMermaid.
"""
import click
from .app import parse_and_render

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.option('--format', default='png', help='Output format (png, svg, etc.)')
def cli(input_file, output_file, format):
    """Convert Mermaid diagram to various formats."""
    with open(input_file, 'r') as f:
        content = f.read()
    
    result = parse_and_render(content, format)
    
    with open(output_file, 'w') as f:
        f.write(result)
