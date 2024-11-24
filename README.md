# xibra_v

Hey there! This is **xibra_v**, a super simple encryption library in Python. It lets you encrypt text and files using a really basic encryption method, with customizable "layers" to make the encryption stronger.

## How it works

- You can **encrypt** plain text by applying several layers of encryption.
- You can **encrypt files** and save them with the encrypted content.

## How to use it?

### Encrypting Text:

```python
from xibra_v import XibraV

# Initialize with 5 layers of encryption
encryption = XibraV(layers=5)

# Encrypt your text
encrypted_text = encryption.encrypt("Hello, this is a secret!")
print(encrypted_text)
