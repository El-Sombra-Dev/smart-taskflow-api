# Contributing to Smart TaskFlow API

Thank you for considering a contribution.

## Getting Started

1. Fork the repository.
2. Create a branch for your work.
3. Create and activate a virtual environment.
4. Install dependencies.
5. Make your changes and verify the API locally.

```bash
git checkout -b feature/your-feature-name
python -m venv venv
# Windows: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

## Pull Requests

- Keep pull requests focused and clearly described.
- Do not commit `.env`, local databases, virtual environments, or credentials.
- Update documentation when behavior or endpoints change.
- Ensure the project starts successfully before opening a pull request.

## Reporting Issues

Open an issue with:

- A clear title and expected behavior.
- Steps to reproduce the issue.
- Error messages or relevant logs.
- Your Python and operating system versions.
