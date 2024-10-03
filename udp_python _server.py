from pynput import keyboard
import socket
import threading

ESP32_IP = '192.168.248.116'  # Replace with the IP address of your ESP32
ESP32_PORT = 8080
a = str()
pressed_keys = set()
last_command = None

def send_udp_message(message, ip, port): 
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.sendto(message.encode(), (ip, port))
        response, server_address = client_socket.recvfrom(1024)
        return response.decode()

def send_message_thread(message, ip, port):
    global last_command
    if message != last_command:
        last_command = message
        threading.Thread(target=send_udp_message, args=(message, ip, port)).start()

def on_press(key):
    global a 
    try:
        k = key.char
    except AttributeError:
        k = key.name
    pressed_keys.add(k)

    if 'w' in pressed_keys and 'a' in pressed_keys:
        a= send_message_thread('FL_on', ESP32_IP, ESP32_PORT)
    elif 'w' in pressed_keys and 'd' in pressed_keys:
        a =send_message_thread('FR_on', ESP32_IP, ESP32_PORT)
    elif 's' in pressed_keys and 'a' in pressed_keys:
        a= send_message_thread('BL_on', ESP32_IP, ESP32_PORT)
    elif 's' in pressed_keys and 'd' in pressed_keys:
        a = send_message_thread('BR_on', ESP32_IP, ESP32_PORT)
    elif 'w' in pressed_keys:
        a  = send_message_thread('F_on', ESP32_IP, ESP32_PORT)
    elif 's' in pressed_keys:
        a = send_message_thread('B_on', ESP32_IP, ESP32_PORT)
    elif 'd' in pressed_keys:
        a = send_message_thread('R_on', ESP32_IP, ESP32_PORT)
    elif 'a' in pressed_keys:
        a = send_message_thread('L_on', ESP32_IP, ESP32_PORT)
    elif 'b' in pressed_keys:
        a = send_message_thread('break',ESP32_IP,ESP32_PORT)
    print(a)


def on_release(key):

    global a 
    
    try:
        k = key.char
    except AttributeError:
        k = key.name
    pressed_keys.discard(k)


    if 'w' in pressed_keys and 'a' not in pressed_keys and 'd' not in pressed_keys:
        a =send_message_thread('FL_off', ESP32_IP, ESP32_PORT)
        a =send_message_thread('FR_off', ESP32_IP, ESP32_PORT)
        a =send_message_thread('B_off', ESP32_IP, ESP32_PORT)
        a =send_message_thread('F_on', ESP32_IP, ESP32_PORT)
    elif 's' in pressed_keys and 'a' not in pressed_keys and 'd' not in pressed_keys:
        a = send_message_thread('BL_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('BR_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('F_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('B_on', ESP32_IP, ESP32_PORT)
    elif 'a' in pressed_keys and 'w' not in pressed_keys and 's' not in pressed_keys:
        a = send_message_thread('F_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('B_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('R_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('L_on', ESP32_IP, ESP32_PORT)
    elif 'd' in pressed_keys and 'w' not in pressed_keys and 's' not in pressed_keys:
        a = send_message_thread('L_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('F_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('B_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('R_on', ESP32_IP, ESP32_PORT)
    elif 'w' in pressed_keys and 'a' in pressed_keys:
        a = send_message_thread('L_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('F_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('B_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('R_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('BL_off', ESP32_IP, ESP32_PORT)    
        a = send_message_thread('FR_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('BR_off', ESP32_IP, ESP32_PORT)

        a = send_message_thread('FL_on', ESP32_IP, ESP32_PORT)
    elif 'w' in pressed_keys and 'd' in pressed_keys:
        a = send_message_thread('L_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('F_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('B_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('R_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('BL_off', ESP32_IP, ESP32_PORT)    
        a = send_message_thread('FL_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('BR_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('FR_off', ESP32_IP, ESP32_PORT)
    elif 's' in pressed_keys and 'a' in pressed_keys:
        a = send_message_thread('L_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('F_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('B_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('R_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('FL_off', ESP32_IP, ESP32_PORT)    
        a = send_message_thread('BL_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('FR_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('BR_off', ESP32_IP, ESP32_PORT)

    elif 's' in pressed_keys and 'd' in pressed_keys:
        a = send_message_thread('L_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('F_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('B_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('BL_off', ESP32_IP, ESP32_PORT)    
        a = send_message_thread('R_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('FR_off', ESP32_IP, ESP32_PORT)
        a = send_message_thread('FL_off', ESP32_IP, ESP32_PORT)

        a = send_message_thread('BR_off', ESP32_IP, ESP32_PORT)
    else:
        a = send_message_thread('all_off', ESP32_IP, ESP32_PORT)


    print(a)
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
