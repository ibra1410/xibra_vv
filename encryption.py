# xibra_vv/encryption.py

class XibraV:
    def __init__(self, layers=5):
        """
        Initializes the XibraV class. You can control how many layers of encryption 
        you want to apply to your text. Default is 5 layers.
        """
        self.layers = layers

    def encrypt(self, text):
        """
        Encrypts your text by shifting each character's code point.
        More layers mean stronger encryption.
        :param text: The text you want to encrypt.
        :return: The encrypted text.
        """
        encrypted_text = text
        for _ in range(self.layers):
            encrypted_text = ''.join(chr(ord(c) + 1) for c in encrypted_text)
        return encrypted_text

    def encrypt_and_save(self, file_path, output_file_path):
        """
        Encrypts the content of a file and saves the encrypted content to a new file.
        :param file_path: Path to the file to be encrypted.
        :param output_file_path: Path to save the encrypted file.
        """
        try:
            # Read file content
            with open(file_path, 'r') as file:
                content = file.read()

            # Encrypt content
            encrypted_content = self.encrypt(content)

            # Save encrypted content to a new file
            with open(output_file_path, 'w') as file:
                file.write(encrypted_content)

            print(f"File encrypted and saved as {output_file_path}")

        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")
