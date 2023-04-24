def palindrom(text):
    
    words = text.lower().split()
    words = [word.strip(",.;:!?") for word in words]
    
   
    palindromes = [word for word in words if word == word[::-1]]
    
    return palindromes


def validate_ip(ip_address):
    
    octets = ip_address.split('.')
    
    
    if len(octets) != 4:
        return False
    
    
    for octet in octets:
        if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
            return False
    
    return True


import platform

def get_os():
    os_name = platform.system()
    
    if os_name == 'Darwin':
        return 'Mac'
    elif os_name == 'Windows':
        return 'Windows'
    elif os_name == 'Linux':
        return 'Linux'
    else:
        return 'Unknown'
