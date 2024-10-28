import tkinter as tk
from cefpython3 import cefpython as cef
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import sys

# Timer GUI
class DebateTimerApp:
    def __init__(self, root, html_path):
        self.root = root
        self.root.title("Policy Debate Timer")
        self.html_path = html_path
        self.setup_gui()
        self.start_server()

    def setup_gui(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Timer display
        self.timer_label = tk.Label(self.frame, text="00:00", font=("Helvetica", 48))
        self.timer_label.pack(pady=20)

        # Buttons for each timer type
        self.create_timer_buttons()

        # Webview setup
        self.open_webview(self.html_path)

    def create_timer_buttons(self):
        button_frame = tk.Frame(self.frame)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="8 min Constructives", command=lambda: self.start_timer(480)).pack(side=tk.LEFT)
        tk.Button(button_frame, text="3 min CX", command=lambda: self.start_timer(180)).pack(side=tk.LEFT)
        tk.Button(button_frame, text="5 min Rebuttals", command=lambda: self.start_timer(300)).pack(side=tk.LEFT)

    def start_timer(self, duration):
        self.remaining_time = duration
        self.update_timer_display()
        self.countdown()

    def countdown(self):
        if self.remaining_time >= 0:
            self.update_timer_display()
            self.remaining_time -= 1
            self.root.after(1000, self.countdown)

    def update_timer_display(self):
        mins, secs = divmod(self.remaining_time, 60)
        self.timer_label.config(text=f"{mins:02}:{secs:02}")

    def open_webview(self, html_file):
        with open(html_file, 'r') as f:
            html_content = f.read()
        cef.Initialize()
        self.browser = cef.CreateBrowserSync(window_info=None, url="data:text/html;charset=utf-8," + html_content)
        self.browser.SetFocus()

    def start_server(self):
        server_thread = threading.Thread(target=self.run_server, daemon=True)
        server_thread.start()

    def run_server(self):
        class UpdateHandler(BaseHTTPRequestHandler):
            def do_POST(self):
                content_length = int(self.headers['Content-Length'])
                new_html = self.rfile.read(content_length).decode('utf-8')
                with open(self.html_path, 'w') as f:
                    f.write(new_html)
                self.send_response(200)
                self.end_headers()
                self.server.app.update_webview()

        server = HTTPServer(('localhost', 5000), UpdateHandler)
        server.app = self
        server.serve_forever()

    def update_webview(self):
        self.browser.Reload()

if __name__ == "__main__":
    root = tk.Tk()
    html_path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/current_buffer.html"
    app = DebateTimerApp(root, html_path)
    root.mainloop()
