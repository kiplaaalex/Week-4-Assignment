from docx import Document
import os

def read_and_modify_file():
    filename = input("Enter the name of the .docx file to read: ")

    # Check file exists
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        return

    # Try to read the .docx file
    try:
        doc = Document(filename)
        content = '\n'.join([para.text for para in doc.paragraphs])
        print("File read successfully!")

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Create a new filename
        new_filename = "modified_" + os.path.splitext(os.path.basename(filename))[0] + ".txt"
        with open(new_filename, 'w', encoding='utf-8') as new_file:
            new_file.write(modified_content)
            print(f"Modified content written to '{new_filename}'.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    read_and_modify_file()
