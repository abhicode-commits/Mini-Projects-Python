import string
import secrets

def generate_password(length=16, use_uppercase=True, use_numbers=True, use_symbols=True):
    """
    Ek dam secure random password generate karta hai.
    """
    # Base pool: hamesha lowercase letters rahenge
    character_pool = string.ascii_lowercase
    mandatory_chars = [secrets.choice(string.ascii_lowercase)]

    # User ki choice ke mutabik pools add karna
    if use_uppercase:
        character_pool += string.ascii_uppercase
        mandatory_chars.append(secrets.choice(string.ascii_uppercase))
        
    if use_numbers:
        character_pool += string.digits
        mandatory_chars.append(secrets.choice(string.digits))
        
    if use_symbols:
        character_pool += string.punctuation
        mandatory_chars.append(secrets.choice(string.punctuation))

    # Length check
    if length < len(mandatory_chars):
        raise ValueError(f"Password ki length kam se kam {len(mandatory_chars)} honi chahiye.")

    # Baaki bache characters ko fill karna
    remaining_length = length - len(mandatory_chars)
    password_list = mandatory_chars + [secrets.choice(character_pool) for _ in range(remaining_length)]
    
    # Characters ko aapas mein mix (shuffle) karna taaki pattern na bane
    secrets.SystemRandom().shuffle(password_list)
    
    return "".join(password_list)

# --- Code ko run karne aur output dekhne ke liye ---
if __name__ == "__main__":
    print("=== Secure Password Generator ===")
    
    # 1. Custom settings ke sath Example Output (14 characters)
    custom_pass = generate_password(length=14, use_uppercase=True, use_numbers=True, use_symbols=True)
    print(f"Example 1 (Custom 14 Chars) : {custom_pass}")
    
    # 2. Sirf Numbers aur Letters ka Example Output (12 characters)
    no_symbols_pass = generate_password(length=12, use_uppercase=True, use_numbers=True, use_symbols=False)
    print(f"Example 2 (No Symbols)      : {no_symbols_pass}")
    
    # 3. Default Strong Password (16 characters)
    default_pass = generate_password()
    print(f"Example 3 (Default Strong)   : {default_pass}")