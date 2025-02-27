import itertools

def brute_force_attack(target_password):
    length = len(target_password)
    digits = '0123456789'
    
    # Generate all possible combinations of the given length
    for attempt in itertools.product(digits, repeat=length):
        attempt_password = ''.join(attempt)
        if attempt_password == target_password:
            return attempt_password
    return None

# Example usage
target_passwords = ['1234', '123456', '12345678']

for target in target_passwords:
    cracked_password = brute_force_attack(target)
    if cracked_password:
        print(f"Password '{target}' cracked successfully: {cracked_password}")
    else:
        print(f"Failed to crack password: {target}")
