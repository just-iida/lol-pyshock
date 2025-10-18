import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import requests
import threading
import time
import urllib3
import webbrowser

# Disable insecure request warnings for local API calls
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- Constants ---
CONFIG_FILE = 'config.config'
PISHOCK_API_URL = 'https://do.pishock.com/api/apioperate/'
LOL_CLIENT_API_BASE_URL = 'https://127.0.0.1:2999/liveclientdata'
GITHUB_LINK = 'https://github.com/just-iida/lol-pyshock'
GITHUB_LOGO = "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"

# Using a dictionary for clarity over "magic numbers"
OPERATIONS = {
    "Shock": "0",
    "Vibrate": "1",
    "Beep": "2"
}


class LoLPiShockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LoL PyShock")
        self.root.geometry("400x480")
        self.root.resizable(False, False)

        self.is_running = False
        self.worker_thread = None

        # --- UI Variables ---
        self.username_var = tk.StringVar()
        self.apikey_var = tk.StringVar()
        self.code_var = tk.StringVar()
        self.operation_var = tk.StringVar(value=OPERATIONS["Shock"])
        self.duration_var = tk.DoubleVar(value=1)
        self.intensity_var = tk.DoubleVar(value=100)
        self.status_var = tk.StringVar(value="Status: Idle")

        self.create_widgets()
        self.load_config()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Make the main frame's columns expandable
        main_frame.columnconfigure(0, weight=1)

        # --- Link Buttons Section ---
        links_frame = ttk.LabelFrame(main_frame, text="Links", padding=10)
        links_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))

        # Store the PhotoImage in an instance variable to prevent garbage collection
        self.github_icon = tk.PhotoImage(data=GITHUB_LOGO).subsample(10, 10) # Resize the icon
        github_button = ttk.Button(links_frame, image=self.github_icon, text="GitHub", compound=tk.LEFT, command=lambda: self.open_link(GITHUB_LINK))
        github_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

        # --- Configuration Section ---
        config_frame = ttk.LabelFrame(main_frame, text="PiShock Configuration", padding="10")
        config_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

        ttk.Label(config_frame, text="Username:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.username_entry = ttk.Entry(config_frame, textvariable=self.username_var, width=40)
        self.username_entry.grid(row=0, column=1, sticky=tk.W)

        ttk.Label(config_frame, text="API Key:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.apikey_entry = ttk.Entry(config_frame, textvariable=self.apikey_var, show="*", width=40)
        self.apikey_entry.grid(row=1, column=1, sticky=tk.W)

        ttk.Label(config_frame, text="Shocker Code:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.code_entry = ttk.Entry(config_frame, textvariable=self.code_var, width=40)
        self.code_entry.grid(row=2, column=1, sticky=tk.W)

        # --- Operation Settings ---
        op_frame = ttk.LabelFrame(main_frame, text="Operation Settings", padding="10")
        op_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)

        op_frame.columnconfigure(1, weight=1)

        for i, (text, value) in enumerate(OPERATIONS.items()):
            ttk.Radiobutton(op_frame, text=text, variable=self.operation_var, value=value).grid(
                row=i, column=0, columnspan=3, sticky=tk.W)

        ttk.Label(op_frame, text="Intensity (1-100):").grid(row=3, column=0, sticky=tk.W, pady=(10, 0))
        self.intensity_value_label = ttk.Label(op_frame, text=f"{int(self.intensity_var.get())}")
        self.intensity_value_label.grid(row=3, column=2, sticky=tk.E, pady=(10, 0), padx=5)
        self.intensity_scale = ttk.Scale(op_frame, from_=1, to=100, orient=tk.HORIZONTAL, variable=self.intensity_var,
                                         command=self._update_slider_labels)
        self.intensity_scale.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E))

        ttk.Label(op_frame, text="Duration (1-15s):").grid(row=5, column=0, sticky=tk.W, pady=(10, 0))
        self.duration_value_label = ttk.Label(op_frame, text=f"{int(self.duration_var.get())}s")
        self.duration_value_label.grid(row=5, column=2, sticky=tk.E, pady=(10, 0), padx=5)
        self.duration_scale = ttk.Scale(op_frame, from_=1, to=15, orient=tk.HORIZONTAL, variable=self.duration_var,
                                        command=self._update_slider_labels)
        self.duration_scale.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E))

        # --- Control Buttons ---
        button_frame = ttk.Frame(main_frame, padding="5")
        button_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))

        self.save_button = ttk.Button(button_frame, text="Save Config", command=self.save_config)
        self.save_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

        self.test_button = ttk.Button(button_frame, text="Test (Beep)", command=self.test_pishock)
        self.test_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

        self.test_current_button = ttk.Button(button_frame, text="Test Current", command=self.test_current_config)
        self.test_current_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

        self.start_stop_button = ttk.Button(button_frame, text="Start", command=self.toggle_worker)
        self.start_stop_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

        # --- Status Bar ---
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W, padding=5)
        status_bar.grid(row=1, column=0, sticky=(tk.W, tk.E))

    def _update_slider_labels(self, _=None):
        """Updates the labels next to the sliders with the current value."""
        self.intensity_value_label.config(text=f"{int(self.intensity_var.get())}")
        self.duration_value_label.config(text=f"{int(self.duration_var.get())}s")

    def get_config_payload(self):
        return {
            "Username": self.username_var.get(),
            "Apikey": self.apikey_var.get(),
            "Code": self.code_var.get(),
            "Op": self.operation_var.get(),
            "Duration": int(self.duration_var.get()),
            "Intensity": int(self.intensity_var.get())
        }

    def open_link(self, url):
        webbrowser.open(url)


    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r') as f:
                    config = json.load(f)
                    self.username_var.set(config.get("Username", ""))
                    self.apikey_var.set(config.get("Apikey", ""))
                    self.code_var.set(config.get("Code", ""))
                    self.operation_var.set(config.get("Op", OPERATIONS["Shock"]))
                    self.duration_var.set(config.get("Duration", 1))
                    self.intensity_var.set(config.get("Intensity", 100))
                self.update_status("Config loaded successfully.")
                self._update_slider_labels()
            except (json.JSONDecodeError, TypeError):
                self.update_status("Error: Could not read config file. It might be corrupted.")
        else:
            self.update_status("No config file found. Please enter details and save.")

    def save_config(self):
        config = self.get_config_payload()
        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.update_status("Configuration saved successfully!")
            messagebox.showinfo("Success", "Configuration saved!")
        except IOError as e:
            self.update_status(f"Error saving config: {e}")
            messagebox.showerror("Error", f"Could not save config file:\n{e}")

    def _send_pishock_request(self, payload, op_name="operation"):
        """Centralized function to send requests to the PiShock API."""
        self.update_status(f"Sending {op_name.lower()}...")
        try:
            # Use a slightly longer timeout to be safe
            response = requests.post(PISHOCK_API_URL, json=payload, timeout=10)
            if response.status_code == 200:
                self.update_status(f"{op_name.capitalize()} sent successfully. Response: {response.text}")
            else:
                self.update_status(f"{op_name.capitalize()} failed. Status: {response.status_code}, Info: {response.text}")
        except requests.RequestException as e:
            self.update_status(f"API Error: {e}")

    def test_pishock(self):
        """Sends a simple beep test."""
        payload = self.get_config_payload()
        payload["Op"] = OPERATIONS["Beep"]
        payload["Duration"] = 1
        payload["Intensity"] = 10 # Beeps don't need high intensity

        threading.Thread(target=self._send_pishock_request, args=(payload, "test beep"), daemon=True).start()

    def test_current_config(self):
        """Sends a test signal using the current UI settings."""
        payload = self.get_config_payload()
        # Find the operation name from its value for a nice status message
        op_name = next((k for k, v in OPERATIONS.items() if v == payload["Op"]), "operation")

        threading.Thread(target=self._send_pishock_request, args=(payload, f"test {op_name}"), daemon=True).start()

    def toggle_worker(self):
        if self.is_running:
            self.is_running = False
            self.start_stop_button.config(text="Start")
            self.update_status("Status: Stopped by user.")
        else:
            self.is_running = True
            self.start_stop_button.config(text="Stop")
            self.worker_thread = threading.Thread(target=self.main_loop, daemon=True)
            self.worker_thread.start()

    def update_status(self, message):
        # For more complex apps, consider root.after() to schedule UI updates from threads
        # e.g., self.root.after(0, lambda: self.status_var.set(f"Status: {message}"))
        self.status_var.set(f"Status: {message}")

    def main_loop(self):
        # Validate config before starting
        config = self.get_config_payload()
        if not all([config.get("Username"), config.get("Apikey"), config.get("Code")]):
            self.update_status("Error: PiShock credentials cannot be empty.")
            # This runs in a thread, so we need to safely toggle the state back
            self.root.after(0, self.toggle_worker)
            return

        self.update_status("Worker started. Looking for game...")

        victim_name = None
        cooldown = False

        while self.is_running:
            try:
                # 1. Check if in game by getting active player name
                player_name_req = requests.get(
                                               f'{LOL_CLIENT_API_BASE_URL}/activeplayername',
                                               verify=False,
                                               timeout=1)
                if player_name_req.status_code == 200:
                    if not victim_name:
                        victim_name = player_name_req.json()
                        self.update_status(f"Game found! Monitoring player: {victim_name}")
                else:
                    # This case handles being in client but not in game
                    victim_name = None
                    cooldown = False
                    self.update_status("In client, waiting for game to start...")
                    time.sleep(5)
                    continue

                # 2. If in game, check player death status
                gamedata_req = requests.get(f'{LOL_CLIENT_API_BASE_URL}/playerlist', verify=False, timeout=1)
                player_list = gamedata_req.json()

                active_player_data = next((p for p in player_list if p['summonerName'] == victim_name), None)

                if active_player_data:
                    if active_player_data["isDead"] and not cooldown:
                        op_name = next((k for k, v in OPERATIONS.items() if v == self.operation_var.get()), "action")
                        self.update_status(f"Death detected! Sending {op_name.lower()} to {victim_name}.")
                        shock_payload = self.get_config_payload()  # Get latest config from UI
                        threading.Thread(target=self._send_pishock_request, args=(shock_payload, op_name), daemon=True).start()
                        cooldown = True
                    elif not active_player_data["isDead"] and cooldown:
                        self.update_status(f"Player respawned. Re-arming. Monitoring {victim_name}")
                        cooldown = False

            except requests.exceptions.ConnectionError:
                victim_name = None
                cooldown = False
                self.update_status("Game not detected. Looking for game...")
                time.sleep(5)  # Wait longer if game is not running
                continue
            except (requests.RequestException, json.JSONDecodeError) as e:
                self.update_status(f"API Error: {e}. Retrying...")

            time.sleep(0.5)  # Polling interval

        if not self.is_running:
            self.update_status("Status: Idle")


if __name__ == "__main__":
    root = tk.Tk()
    app = LoLPiShockApp(root)
    root.mainloop()