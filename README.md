# Lockscript

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Description

**Lockscript** is a desktop application built with Python and Tkinter that lets you encrypt and decrypt text files directly from a graphical interface — no terminal knowledge required.

**How it works:**

The user selects a text file using the built-in file importer. Once a file is loaded, two actions are available: **Encrypt** and **Decrypt**. Encryption applies a Caesar-style character shift (+1) to every character in the file, transforming readable text into an unreadable form. Decryption reverses that process (-1), restoring the original content — as long as the file was previously encrypted with this same application.

**Key characteristics:**

- **File-based**: works directly on `.txt` files stored on disk. The encrypted output overwrites (or is saved alongside) the original file.
- **No external dependencies for core logic**: the encryption engine is self-contained and requires no third-party cryptography libraries.
- **Error-aware UI**: invalid file paths, unsupported formats, or missing selections trigger descriptive dialog popups rather than silent failures, making the experience beginner-friendly.
- **Environment-aware**: supports `development`, `production`, and `testing` configurations via a `.env` file, enabling clean separation between runtime contexts.
- **Distributable**: the app can be packaged into a standalone executable (`.exe` on Windows, binary on Linux/Mac) using PyInstaller, so end users do not need Python installed.

**Intended use:**

Lockscript is designed as a lightweight, educational tool to demonstrate how a full Python desktop application can be structured — covering UI, service layer, error handling, configuration management, testing, linting, and build pipelines — all within a single cohesive project.

## Technologies used

1. Python >= 3.11
2. Tkinter

## Libraries used

The dependencies are declared in `pyproject.toml`. The `requirements*.txt` files are thin wrappers (`-e .`, `-e .[dev]`, `-e .[test]`, `-e .[build]`) kept for backward-compatible muscle memory.

#### Runtime ([project.dependencies])

```
python-dotenv==1.0.1
```

#### Dev ([project.optional-dependencies] dev)

```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
```

#### Test ([project.optional-dependencies] test)

```
pytest==8.4.2
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

#### Build ([project.optional-dependencies] build)

```
pyinstaller==6.16.0
```

## Getting Started

Follow these steps to set up the project locally for development.

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -e .[dev,test]`
6. Copy the development env template into a real `.env` file (the app will not start without it):
   - Windows: `copy .env.example.dev .env`
   - Linux/Mac: `cp .env.example.dev .env`
7. Use `python app.py` or `python -m src` to execute the program

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Env Keys

The `.env` file you created in the previous step holds the runtime configuration. Below is the reference for every supported key.

1. `ENVIRONMENT`: Defines the application environment. Accepts `development`, `production`, or `testing`.

```
ENVIRONMENT=development
```

## Testing

With the project installed, you can run the test suite to verify everything works as expected.

1. Go to the repository folder
2. Execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -e .[test]`
6. Execute: `pytest --log-cli-level=INFO`

## Security Audit

Before packaging or distributing the app, scan your dependencies for known vulnerabilities using **pip-audit**.

1. Go to the repository folder
2. Activate your virtual environment
3. Execute: `pip install -e .[dev]`
4. Execute: `pip-audit`

## Build

Once tests pass and the audit is clean, you can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

> **Security notice:** The `.env` file is bundled directly into the executable by `app.spec`. Your development `.env` contains `ENVIRONMENT=development` and no real secrets, so it is safe to bundle for testing builds. For production releases, create a dedicated `.env` with production values, build the executable, then **immediately delete it** from the source tree. Never commit a production `.env` to the repository.

### Windows

1. Go to the repository folder
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -e .[build]`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Go to the repository folder
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -e .[build]`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `./build.sh`

## Known Issues

None at the moment.

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/lockscript`](https://www.diegolibonati.com.ar/#/project/lockscript)
