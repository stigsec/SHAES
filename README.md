# SHAES

**SHAES** is a lightweight Python script for encrypting and decrypting files using AES encryption in CBC mode.

---

## Features

- **Encryption**: Securely encrypt files with a password.
- **Decryption**: Decrypt previously encrypted files.
- **Error Handling**: Alerts for incorrect passwords, non-encrypted files, or missing files.
- **Lightweight**: Minimal dependencies and easy to use.

---

## Getting Started

### Dependencies

Ensure you have Python 3 installed along with the required library:

```bash
pip install pycryptodome
```

---

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/stigsec/SHAES.git
   ```

2. Navigate to the project directory:

   ```bash
   cd SHAES
   ```

---

## Usage

### Syntax

```bash
python shaes.py {enc/dec} {input_file} {password}
```

### Examples

#### Encrypt a file:

```bash
python shaes.py enc myfile.txt mypassword
```

This will create an encrypted file named `myfile.txt.shaes`.

#### Decrypt a file:

```bash
python shaes.py dec myfile.txt.shaes mypassword
```

This will create a decrypted file named `myfile.txt`.

---

## How It Works

1. **Key Derivation**: Uses SHA-256 to derive a secure key from the provided password.
2. **AES Encryption**: Encrypts data using AES in CBC mode with a randomly generated initialization vector (IV).
3. **Padding**: Ensures data alignment with AES block size using PKCS7 padding.
4. **Error Handling**: Detects invalid files or decryption attempts with incorrect passwords.

---

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE file](LICENSE) for more details.



---

Developed by [stigsec](https://github.com/stigsec).
