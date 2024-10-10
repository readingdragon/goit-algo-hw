from pathlib import Path
import shutil
import sys

# funtion for parse arguments
def parse_arguments():
    if len(sys.argv) < 2:
        print("Alarm! Incorrect using script! Enter two arquments <source_directory> and [destination_directory]")
        sys.exit(1)

    source_dir = Path(sys.argv[1])
    destination_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    return source_dir, destination_dir

# function for copy files
def copy_files_recursively(source_dir, destination_dir):
    try:
        for item in source_dir.iterdir():
            if item.is_dir():
                copy_files_recursively(item, destination_dir)
            elif item.is_file():
                file_ext = item.suffix.lower()  # get files extensions
                if not file_ext:
                    file_ext = "no_extension"  # if file doesn't have extension
                
                # make subdir for all files type
                ext_dir = destination_dir / (file_ext[1:] if file_ext != "no_extension" else file_ext)
                ext_dir.mkdir(parents=True, exist_ok=True)  
                
                # copy files to appropriate dir
                dest_file_path = ext_dir / item.name
                shutil.copy2(item, dest_file_path)
                print(f"Copied: {item} -> {dest_file_path}")
    
    except PermissionError:
        print(f"Oops, no access to: {source_dir}")
    except Exception as e:
        print(f"Something goes wrong and the problem is: {e}")

def main():
    source_dir, destination_dir = parse_arguments()

    # check if the path from the user is correct
    if not source_dir.exists() or not source_dir.is_dir:
        print(f"Your dir is not a dir or doesn't exist at all: {source_dir}")
        sys.exit(1)

    # make dir if it doesn't exist
    destination_dir.mkdir(parents=True, exist_ok=True)

    copy_files_recursively(source_dir, destination_dir)

    print("Congrats! Job done, all files copied!")

if __name__ == "__main__":
    main()
