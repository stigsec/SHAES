from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib
import sys

def derive_key(password):
    return hashlib.sha256(password.encode()).digest()

def encrypt(input_file, password):
    key = derive_key(password)
    iv = get_random_bytes(16)
    output_file = f"{input_file}.shaes"
    
    if input_file.endswith(".shaes"):
        print(f"The file {input_file} is already encrypted.")
        return
    
    try:
        with open(input_file, "rb") as f_in, open(output_file, "wb") as f_out:
            f_out.write(iv)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            while chunk := f_in.read(64 * 1024):
                f_out.write(cipher.encrypt(pad(chunk, AES.block_size)))
        print(f"File encrypted as {output_file}")
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
    except Exception as e:
        print(f"Encryption failed: {e}")

def decrypt(input_file, password):
    key = derive_key(password)
    output_file = input_file.replace(".shaes", "")
    
    if not input_file.endswith(".shaes"):
        print(f"The file {input_file} does not appear to be encrypted.")
        return
    
    try:
        with open(input_file, "rb") as f_in:
            iv = f_in.read(16)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            
            decrypted_data = b""
            while chunk := f_in.read(64 * 1024):
                decrypted_data += cipher.decrypt(chunk)
            
            plaintext = unpad(decrypted_data, AES.block_size)
        
        with open(output_file, "wb") as f_out:
            f_out.write(plaintext)
        print(f"File decrypted as {output_file}")
    
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
    except (ValueError, KeyError):
        print(f"Decryption failed: Invalid password or corrupted file.")
    except Exception as e:
        print(f"Decryption failed: {e}")

def usage():
    print("Usage:")
    print("python shaes.py {enc/dec} {input_file} {password}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage()
        sys.exit(1)
    
    action = sys.argv[1].lower()
    input_file = sys.argv[2]
    password = sys.argv[3]
    
    if action == "enc":
        encrypt(input_file, password)
    elif action == "dec":
        decrypt(input_file, password)
    else:
        print(f"Invalid action: {action}. Use 'enc' for encryption or 'dec' for decryption.")
        usage()
        sys.exit(1)
