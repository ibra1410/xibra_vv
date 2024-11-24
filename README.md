# xibra_v

Hey there! Welcome to **xibra_v**, a super simple encryption library written in Python. This library allows you to easily encrypt text and files with a simple encryption method. You can also customize the encryption by adding layers to make it stronger.

## How it works

- **Encrypt Text**: Apply multiple layers of encryption to plain text for stronger encryption.
- **Encrypt Files**: Encrypt entire files and save the encrypted content to a new file.

## How to use it?

### Encrypting Text:

```python
from xibra_v import XibraV

# Initialize with 5 layers of encryption
encryption = XibraV(layers=5)

# Encrypt your text
encrypted_text = encryption.encrypt("Hello, this is a secret!")
print(encrypted_text)
## Installation

To install **xibra_v**, you can use **pip**. Follow the steps below to install it:

### Install via pip from GitHub:

If you'd like to install directly from the GitHub repository, simply run this command:

```bash
pip install git+https://github.com/yourusername/xibra_v.git
