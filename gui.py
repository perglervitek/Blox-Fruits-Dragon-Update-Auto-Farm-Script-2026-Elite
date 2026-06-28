import tkinter as tk
from tkinter import messagebox
import threading
from src.trainer import Trainer

class TrainerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🐉 Blox Fruits Dragon Update Trainer")
        self.root.geometry("480x620")
        self.root.resizable(False, False)
        self.root.configure(bg="#1a1a2e")

        self.trainer = Trainer()
        self.attached = False

        # Title label
        title = tk.Label(
            root,
            text="🐉 Blox Fruits Dragon Update Trainer",
            font=("Helvetica", 14, "bold"),
            bg="#1a1a2e",
            fg="#e74c3c"
        )
        title.pack(pady=10)

        # Frame for checkboxes
        checkbox_frame = tk.Frame(root, bg="#1a1a2e")
        checkbox_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.feature_vars = {}
                var = tk.BooleanVar()
        self.feature_vars['auto_farm_level'] = var
        cb = tk.Checkbutton(
            checkbox_frame,
            text='Auto Farm Level',
            variable=var,
            bg='#1a1a2e',
            fg='#ffffff',
            selectcolor='#e74c3c',
            activebackground='#1a1a2e',
            activeforeground='#e74c3c',
            font=('Helvetica', 11),
            anchor='w',
            command=lambda k='auto_farm_level', v=var: self.trainer.set_feature(k, v.get())
        )
        cb.pack(fill='x', pady=2)
        var = tk.BooleanVar()
        self.feature_vars['no_cooldown'] = var
        cb = tk.Checkbutton(
            checkbox_frame,
            text='No Cooldown',
            variable=var,
            bg='#1a1a2e',
            fg='#ffffff',
            selectcolor='#e74c3c',
            activebackground='#1a1a2e',
            activeforeground='#e74c3c',
            font=('Helvetica', 11),
            anchor='w',
            command=lambda k='no_cooldown', v=var: self.trainer.set_feature(k, v.get())
        )
        cb.pack(fill='x', pady=2)
        var = tk.BooleanVar()
        self.feature_vars['teleport'] = var
        cb = tk.Checkbutton(
            checkbox_frame,
            text='Teleport',
            variable=var,
            bg='#1a1a2e',
            fg='#ffffff',
            selectcolor='#e74c3c',
            activebackground='#1a1a2e',
            activeforeground='#e74c3c',
            font=('Helvetica', 11),
            anchor='w',
            command=lambda k='teleport', v=var: self.trainer.set_feature(k, v.get())
        )
        cb.pack(fill='x', pady=2)
        var = tk.BooleanVar()
        self.feature_vars['anti_ban'] = var
        cb = tk.Checkbutton(
            checkbox_frame,
            text='Anti-Ban',
            variable=var,
            bg='#1a1a2e',
            fg='#ffffff',
            selectcolor='#e74c3c',
            activebackground='#1a1a2e',
            activeforeground='#e74c3c',
            font=('Helvetica', 11),
            anchor='w',
            command=lambda k='anti_ban', v=var: self.trainer.set_feature(k, v.get())
        )
        cb.pack(fill='x', pady=2)
        var = tk.BooleanVar()
        self.feature_vars['auto_fruit_snipe'] = var
        cb = tk.Checkbutton(
            checkbox_frame,
            text='Auto Fruit Snipe',
            variable=var,
            bg='#1a1a2e',
            fg='#ffffff',
            selectcolor='#e74c3c',
            activebackground='#1a1a2e',
            activeforeground='#e74c3c',
            font=('Helvetica', 11),
            anchor='w',
            command=lambda k='auto_fruit_snipe', v=var: self.trainer.set_feature(k, v.get())
        )
        cb.pack(fill='x', pady=2)
        var = tk.BooleanVar()
        self.feature_vars['auto_raid'] = var
        cb = tk.Checkbutton(
            checkbox_frame,
            text='Auto Raid',
            variable=var,
            bg='#1a1a2e',
            fg='#ffffff',
            selectcolor='#e74c3c',
            activebackground='#1a1a2e',
            activeforeground='#e74c3c',
            font=('Helvetica', 11),
            anchor='w',
            command=lambda k='auto_raid', v=var: self.trainer.set_feature(k, v.get())
        )
        cb.pack(fill='x', pady=2)
        var = tk.BooleanVar()
        self.feature_vars['esp'] = var
        cb = tk.Checkbutton(
            checkbox_frame,
            text='ESP (Wallhack)',
            variable=var,
            bg='#1a1a2e',
            fg='#ffffff',
            selectcolor='#e74c3c',
            activebackground='#1a1a2e',
            activeforeground='#e74c3c',
            font=('Helvetica', 11),
            anchor='w',
            command=lambda k='esp', v=var: self.trainer.set_feature(k, v.get())
        )
        cb.pack(fill='x', pady=2)
        var = tk.BooleanVar()
        self.feature_vars['auto_farm_boss'] = var
        cb = tk.Checkbutton(
            checkbox_frame,
            text='Auto Farm Boss',
            variable=var,
            bg='#1a1a2e',
            fg='#ffffff',
            selectcolor='#e74c3c',
            activebackground='#1a1a2e',
            activeforeground='#e74c3c',
            font=('Helvetica', 11),
            anchor='w',
            command=lambda k='auto_farm_boss', v=var: self.trainer.set_feature(k, v.get())
        )
        cb.pack(fill='x', pady=2)
        var = tk.BooleanVar()
        self.feature_vars['auto_stats'] = var
        cb = tk.Checkbutton(
            checkbox_frame,
            text='Auto Stats',
            variable=var,
            bg='#1a1a2e',
            fg='#ffffff',
            selectcolor='#e74c3c',
            activebackground='#1a1a2e',
            activeforeground='#e74c3c',
            font=('Helvetica', 11),
            anchor='w',
            command=lambda k='auto_stats', v=var: self.trainer.set_feature(k, v.get())
        )
        cb.pack(fill='x', pady=2)
        var = tk.BooleanVar()
        self.feature_vars['auto_sea_event'] = var
        cb = tk.Checkbutton(
            checkbox_frame,
            text='Auto Sea Event',
            variable=var,
            bg='#1a1a2e',
            fg='#ffffff',
            selectcolor='#e74c3c',
            activebackground='#1a1a2e',
            activeforeground='#e74c3c',
            font=('Helvetica', 11),
            anchor='w',
            command=lambda k='auto_sea_event', v=var: self.trainer.set_feature(k, v.get())
        )
        cb.pack(fill='x', pady=2)

        # Button frame
        button_frame = tk.Frame(root, bg="#1a1a2e")
        button_frame.pack(pady=15)

        self.attach_btn = tk.Button(
            button_frame,
            text="Attach",
            command=self.attach,
            bg="#e74c3c",
            fg="#ffffff",
            activebackground="#b83550",
            activeforeground="#ffffff",
            font=("Helvetica", 10, "bold"),
            width=12,
            relief="flat"
        )
        self.attach_btn.pack(side="left", padx=10)

        self.start_btn = tk.Button(
            button_frame,
            text="Start",
            command=self.start_trainer,
            bg="#e74c3c",
            fg="#ffffff",
            activebackground="#b83550",
            activeforeground="#ffffff",
            font=("Helvetica", 10, "bold"),
            width=12,
            relief="flat",
            state="disabled"
        )
        self.start_btn.pack(side="left", padx=10)

        self.stop_btn = tk.Button(
            button_frame,
            text="Stop",
            command=self.stop_trainer,
            bg="#e74c3c",
            fg="#ffffff",
            activebackground="#b83550",
            activeforeground="#ffffff",
            font=("Helvetica", 10, "bold"),
            width=12,
            relief="flat",
            state="disabled"
        )
        self.stop_btn.pack(side="left", padx=10)

        # Status label
        self.status_label = tk.Label(
            root,
            text="Status: Not attached",
            bg="#1a1a2e",
            fg="#cccccc",
            font=("Helvetica", 10)
        )
        self.status_label.pack(pady=15)

        # Footer
        footer = tk.Label(
            root,
            text="Press INSERT to open menu in-game",
            bg="#1a1a2e",
            fg="#888888",
            font=("Helvetica", 9)
        )
        footer.pack(side="bottom", pady=10)

    def attach(self):
        if self.attached:
            messagebox.showinfo("Info", "Already attached to Roblox process.")
            return
        self.status_label.config(text="Status: Attaching...")
        self.root.update()
        if self.trainer.attach():
            self.attached = True
            self.status_label.config(text="Status: Attached to RobloxPlayerBeta.exe")
            self.start_btn.config(state="normal")
            self.attach_btn.config(state="disabled")
        else:
            self.status_label.config(text="Status: Failed to attach. Check if Roblox is running.")
            messagebox.showerror("Error", "Could not attach to Roblox. Make sure Roblox is open and you are in Blox Fruits.")

    def start_trainer(self):
        if not self.attached:
            messagebox.showwarning("Warning", "Attach to Roblox first.")
            return
        try:
            self.trainer.start()
            self.status_label.config(text="Status: Trainer running")
            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start trainer: {e}")

    def stop_trainer(self):
        self.trainer.stop()
        self.attached = False
        self.status_label.config(text="Status: Trainer stopped")
        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="disabled")
        self.attach_btn.config(state="normal")

def main():
    root = tk.Tk()
    app = TrainerGUI(root)
    root.mainloop()
