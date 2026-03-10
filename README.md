# Devscale Bootcamp AI Enabled Python Web Development

## Assignments 4

### Features

- POST `/research` returns:
  - PDF (default)
- POST `/content` returns:
  - PDF (default)
- Scalar: `/scalar`

### Setup

```bash
pip install uv
uv venv
source .venv/bin/activate
uv sync
cp .env.example .env
# edit .env: set OPENROUTER_API_KEY and TAVILY_API_KEY
```
