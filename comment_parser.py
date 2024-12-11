import sys

def remove_comments(filename):
    in_block_comment = False
    try:
        # Attempt to open and read the file
        with open(filename, 'r') as f:
            content = f.read()
        split_content = content.splitlines()

        # Process and print content without comments
        print("\n--- File Content with no comments ---")
        for line in split_content:
            if in_block_comment and "*/" not in line:
                # Currently inside a block comment and no closing tag found
                continue

            # Handle single-line comments
            if "//" in line:
                split_line = line.split("//")
                line = split_line[0]

            # Handle block comments starting
            if "/*" in line and not in_block_comment:
                in_block_comment = True
                split_line = line.split("/*")
                before_comment = split_line[0]
                after_comment = split_line[1]
                line_to_print = before_comment
                if "*/" in after_comment:
                    in_block_comment = False
                    split_after_comment = after_comment.split("*/")
                    line_to_print += split_after_comment[1]
                line = line_to_print
                if not line:
                    continue

            # Handle block comments ending
            if "*/" in line and in_block_comment:
                in_block_comment = False
                split_line = line.split("*/")
                line = split_line[1]
                if not line:
                    continue

            print(line)

    except FileNotFoundError:
        print("Error: The file was not found. Please double-check the path.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Check if the filename is provided in the command line arguments
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <path_to_source_code_file>")
        sys.exit(1)

    filename = sys.argv[1]
    remove_comments(filename)
    

if __name__ == "__main__":
    main()
