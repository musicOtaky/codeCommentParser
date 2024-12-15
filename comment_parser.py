import sys
import re

def remove_comments(content: str) -> str:
    in_block_comment = False
    split_content = content.splitlines()
    output_lines = []

    for line in split_content:
        # If currently in a block comment and no closing token found, skip this line
        if in_block_comment and "*/" not in line:
            continue

        # Handle single-line comments
        if "//" in line:
            line = line.split("//", 1)[0]
            if line.isspace():
                continue

        # Handle block comments starting
        if "/*" in line and not in_block_comment:
            in_block_comment = True
            parts = line.split("/*", 1)
            before_comment = parts[0]
            after_comment = parts[1]
            line_to_print = before_comment
            # If the same line contains "*/", close the block comment
            if "*/" in after_comment:
                in_block_comment = False
                after_parts = after_comment.split("*/", 1)
                line_to_print += after_parts[1]
            line = line_to_print
            if (line.isspace()) or (not line):
                continue

        # Handle block comment ending if it wasn't closed above
        if "*/" in line and in_block_comment:
            in_block_comment = False
            parts = line.split("*/", 1)
            line = parts[1]
            if (line.isspace()) or (not line):
                continue

        output_lines.append(line)

    # Join the lines back into a single string with newlines
    return "\n".join(output_lines) + "\n"


def main():
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <path_to_source_code_file>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            content = f.read()

        cleaned_code = remove_comments(content)
        print(cleaned_code, end="")

    except FileNotFoundError:
        print("Error: The file was not found. Please double-check the path.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

