import ast

def analyze_code(code):
    issues = []
    suggestions = []

    try:
        ast.parse(code)
    except SyntaxError as e:
        issues.append(f"Syntax Error: {e}")
        suggestions.append("Check the reported line and fix syntax issues.")
        return issues, suggestions

    lines = code.split("\n")

    for i, line in enumerate(lines, start=1):
        if len(line) > 100:
            issues.append(f"Line {i}: Long line detected.")
            suggestions.append("Keep lines under 100 characters.")

        if "==" in line and "if" not in line and "while" not in line:
            issues.append(f"Line {i}: Possible unintended comparison.")
            suggestions.append("Verify whether comparison is intended.")

        if "print(" in line:
            suggestions.append(f"Line {i}: Remove debug print statements before production deployment.")

    if not issues:
        suggestions.append("No major issues detected. Code looks valid.")

    return issues, suggestions


def main():
    print("=== AI Code Debugger ===")
    print("Paste your Python code. Type END on a new line to finish.")

    code_lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        code_lines.append(line)

    code = "\n".join(code_lines)

    issues, suggestions = analyze_code(code)

    print("\n--- Analysis Report ---")

    if issues:
        print("\nIssues Found:")
        for issue in issues:
            print("-", issue)
    else:
        print("\nNo issues found.")

    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)


if __name__ == "__main__":
    main()
