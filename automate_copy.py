import os


def list_subdirectories(directory):
    subdirectories = [name for name in os.listdir(
        directory) if os.path.isdir(os.path.join(directory, name))]
    return subdirectories


def write_to_file(subdirectories, output_file):
    with open(output_file, 'w') as file:
        for subdir in subdirectories:
            file.write(f"    - assets/exercises/{subdir}/\n")


def main():
    input_directory = input("Enter the path of the directory: ")
    if not os.path.isdir(input_directory):
        print("Invalid directory path!")
        return

    subdirectories = list_subdirectories(input_directory)
    if not subdirectories:
        print("No subdirectories found in the specified directory.")
        return

    output_file = "subdirectories.txt"
    write_to_file(subdirectories, output_file)
    print(f"Subdirectories' names are written to '{output_file}' file.")


if __name__ == "__main__":
    main()
