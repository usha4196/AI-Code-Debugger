# 🐞 AI Code Debugger

A lightweight Python-based code debugging and static analysis tool that analyzes Python source code, detects common issues, and provides useful suggestions to improve code quality.

## 📌 Overview

**AI Code Debugger** is a command-line application designed to help developers identify common Python coding problems without manually checking every line.

The application uses Python's built-in `ast` module to validate Python syntax and performs additional static checks on the source code.

It is simple, beginner-friendly, and can be extended with AI/LLM capabilities in the future.

## ✨ Features

- 🔍 Detects Python syntax errors
- 🧠 Performs basic static code analysis
- 📏 Detects unnecessarily long lines
- ⚠️ Identifies possible unintended comparison usage
- 🐛 Detects debug `print()` statements
- 💡 Provides suggestions for fixing detected issues
- 💻 Simple command-line interface
- 🚀 Easy to run and extend

## 🛠️ Technologies Used

- **Python 3**
- **AST (Abstract Syntax Tree)**
- **Command Line Interface (CLI)**

## 📂 Project Structure

```text
AI-Code-Debugger/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

### `app.py`

Contains the main debugging and static-analysis logic.

### `requirements.txt`

Contains project dependencies.

> This project currently uses Python's built-in `ast` module, so no external Python packages are required.

### `README.md`

Contains project documentation and instructions for running the application.

## ⚙️ How It Works

The application follows these steps:

```text
User enters Python code
        ↓
Code is collected through CLI
        ↓
Python AST syntax validation
        ↓
Static code analysis
        ↓
Issues are detected
        ↓
Suggestions are generated
        ↓
Analysis report is displayed
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Code-Debugger.git
```

### 2. Navigate to the project

```bash
cd AI-Code-Debugger
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

Since the project currently uses only Python's standard library, there are no external dependencies.

## ▶️ Running the Application

Run:

```bash
python app.py
```

You will see:

```text
=== AI Code Debugger ===
Paste your Python code. Type END on a new line to finish.
```

Enter your Python code and type:

```text
END
```

when you are finished.

## 🧪 Example

### Input

```python
def calculate_sum(a, b)
    print(a + b)

calculate_sum(10, 20)
END
```

### Output

```text
--- Analysis Report ---

Issues Found:
- Syntax Error: expected ':'

Suggestions:
- Check the reported line and fix syntax issues.
```

## 🔎 Example of Static Analysis

Input:

```python
x = 10

if x == 10:
    print("Debugging")
```

The debugger can provide suggestions such as:

```text
Suggestions:
- Line 4: Remove debug print statements before production deployment.
```

## 🎯 Use Cases

This project can be useful for:

- Python beginners learning debugging
- Students practicing programming
- Identifying simple syntax errors
- Basic static code analysis
- Learning how AST-based analysis works
- Building a foundation for an AI-powered coding assistant

## 🔮 Future Improvements

The project can be extended with:

- 🤖 OpenAI/LLM-based code explanations
- 🔧 Automatic code correction
- 📊 Code quality scoring
- 🖥️ Web interface using Streamlit or Flask
- 📁 Upload Python files for analysis
- 📝 Detailed error explanations
- 🔍 More advanced static analysis rules
- 💬 Natural-language debugging assistance
- 🧪 Automated test generation
- 🔐 Secure sandboxed code execution

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push your branch
6. Create a Pull Request

## 📄 License

This project is open-source and available under the MIT License.

## 👨‍💻 Author

**Jetty Usha Rani**

Computer Science Student  
Mohan Babu University

---

⭐ If you find this project useful, consider giving the repository a star!
