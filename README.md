# WebSHELL

**WebSHELL** is a powerful tool for generating a PHP backdoor and setting up a Netcat listener for reverse shell connections. It automates the process of creating a PHP file that connects back to your machine and starting a Netcat server to catch the incoming shell.

## Features

- **Automatic IP Detection**: Retrieves your local IP address automatically.
- **PHP Backdoor Generation**: Creates a PHP script for a reverse shell.
- **Netcat Listener**: Starts a Netcat server on port 4444 to receive the reverse shell connection.

## Requirements

- Python 3.x
- `termcolor` library

To install the required Python libraries, run:

```bash
pip install -r requirements.txt
```

## Usage

1. **Run the Script**: Execute the Python script to generate the PHP backdoor and start the Netcat listener.

    ```bash
    python WebSHELL.py
    ```

2. **Deploy the Backdoor**: Upload the generated `backdoor.php` to a target web server.

3. **Listen for Connections**: The script automatically starts a Netcat server on port 4444 to listen for incoming connections.

## Example Output

```
 __      __      ___.     _________ ___ ______________.____    .____     
/  \    /  \ ____\_ |__  /   _____//   |   \_   _____/|    |   |    |    
\   \/\/   // __ \| __ \ \_____  \/    ~    \    __)_ |    |   |    |    
 \        /\  ___/| \_\ \/        \    Y    /        \|    |___|    |___ 
  \__/\  /  \___  >___  /_______  /\___|_  /_______  /|_______ \_______ \\
       \/       \/    \/        \/       \/        \/         \/       \/

Author: g4ur4v007
Version: 1.0
Netcat server is starting with the following command:
nc -lvnp 4444
```

## Notes

- **Ethical Use Only**: This tool is intended for ethical hacking, penetration testing, and security research. Unauthorized use may be illegal and unethical.
- **Dependencies**: Ensure that Netcat is installed on your system for the tool to work properly.

## Author

- **g4ur4v007**

## License

This project is licensed under the GNU 3.0 License - see the [LICENSE](LICENSE) file for details.
```
