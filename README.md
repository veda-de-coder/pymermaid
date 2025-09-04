# PyMermaid

A Python library for parsing and rendering Mermaid diagrams.

## Features

- Parse Mermaid flowchart syntax
- Generate diagrams using Graphviz
- Command-line interface
- REST API
- Python API

## Installation

```bash
pip install pymermaid
```

## Usage

### Command Line

```bash
pymermaid input.mmd output.png --format png
```

### Python API

```python
from pymermaid import parse_and_render

content = """
A[Start] --> B[Process]
B --> C[End]
"""

result = parse_and_render(content, format='png')
```

### REST API

```bash
uvicorn pymermaid.api:app --reload
```

Then send a POST request to `/render`:

```json
{
    "content": "A[Start] --> B[Process]\\nB --> C[End]",
    "format": "png"
}
```

## Development

1. Clone the repository
2. Install dependencies: `pip install -e ".[dev]"`
3. Run tests: `pytest`

## License

MIT
