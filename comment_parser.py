def main():
    # Prompt the user for the filename
    filename = input("Enter the path to the source code file: ")
    comments = []
    in_block_comment = False


    try:
        # Attempt to open and read the file
        with open(filename, 'r') as f:
            content = f.read()
        
        # For now, just output what we read to ensure the interface works
    
        split_content = content.splitlines()
        print("\n--- File Contents ---")
        print(content)
        print("---------------------")

        print("\n--- File Content with no comments ---")
        # Check sourcecode for comments
        for line in split_content:
            if (in_block_comment) and ("*/" not in line):
                continue
            if "//" in line:
                split_line = line.split("//")
                line = split_line[0]
            if ("/*" in line) and (in_block_comment == False):
                in_block_comment = True 
                split_line = line.split("/*")
                before_comment = split_line[0]
                after_comment = split_line[1]
                line_to_print = before_comment
                if ("*/" in after_comment):
                    in_block_comment = False
                    split_after_comment = after_comment.split("*/")
                    line_to_print += split_after_comment[1]
                line = line_to_print
                if (not line):
                    continue
            if ("*/" in line):
                in_block_comment = False
                split_line = line.split("*/")
                line = split_line[1]
                if (not line):
                    continue
            print(line)
            
            


    except FileNotFoundError:
        print("Error: The file was not found. Please double-check the path.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()