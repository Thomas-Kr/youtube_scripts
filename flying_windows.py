import win32gui
import win32api
import subprocess
import psutil

WIDTH = win32api.GetSystemMetrics(0)
HEIGHT = win32api.GetSystemMetrics(1)

def is_process_running(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False

class Window:
    def __init__(self, window_title, speed_x, speed_y):
        self.window_title = window_title
        self.speed_x = speed_x
        self.speed_y = speed_y

        self.hwnd = win32gui.FindWindow(None, self.window_title)
        if self.hwnd:
            rect = win32gui.GetWindowRect(self.hwnd)
            self.x = rect[0]
            self.y = rect[1]
            self.width = rect[2] - rect[0]
            self.height = rect[3] - rect[1]

    def move(self):
        if self.x + self.width > WIDTH or self.x < 0:
            self.speed_x *= -1
        if self.y + self.height > HEIGHT or self.y < 0:
            self.speed_y *= -1

        self.x += self.speed_x
        self.y += self.speed_y
        win32gui.MoveWindow(self.hwnd, self.x, self.y, self.width, self.height, True)

class Mouse:
    def __init__(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.x = win32api.GetCursorPos()[0]
        self.y = win32api.GetCursorPos()[1]

    def move(self):
        if self.x > WIDTH or self.x < 0:
            self.speed_x *= -1
        if self.y > HEIGHT or self.y < 0:
            self.speed_y *= -1

        self.x += self.speed_x
        self.y += self.speed_y

        win32api.SetCursorPos((self.x, self.y))

def is_windows_colission_detected(window_1: Window, window_2: Window):
    if (window_1.y + window_1.height > window_2.y and 
        window_1.y < window_2.y + window_2.height):
        if window_1.x > window_2.x and window_1.x < window_2.x + window_2.width:
            return True
        elif (window_1.x + window_1.width < window_2.x + window_2.width and 
              window_1.x + window_1.width> window_2.x):
            return True
    return False

def is_mouse_colission_detected(window: Window, mouse: Window):
    if (window.y + window.height > mouse.y and window.y < mouse.y and 
        window.x + window.width > mouse.x and window.x < mouse.x):
        if (window.y - window.speed_y > mouse.y - mouse.speed_y or 
            window.y - window.speed_y + window.height < mouse.y - mouse.speed_y):
            return 1
        else:
            return 2
    return False

subprocess.Popen(['notepad.exe'])
subprocess.Popen(['mspaint.exe'])

while (is_process_running('notepad.exe') is False and 
       is_process_running('mspaint.exe') is False):
    continue

window_1 = Window('Untitled - Notepad', speed_x=2, speed_y=1)
window_2 = Window('Untitled - Paint', speed_x=2, speed_y=1)

windows = [window_1, window_2]

mouse = Mouse(speed_x=3, speed_y=2)

while True:
    window_1.move()
    window_2.move()
    mouse.move()

    if is_windows_colission_detected(window_1, window_2):
        window_1.speed_x, window_2.speed_x = window_2.speed_x, window_1.speed_x
        window_1.speed_y, window_2.speed_y = window_2.speed_y, window_1.speed_y

    for window in windows:
        output = is_mouse_colission_detected(window, mouse)
        if output == 1:
            mouse.speed_y *= -1
        elif output == 2:
            mouse.speed_x *= -1