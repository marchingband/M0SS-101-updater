# # # import tkinter as tk
# # # from tkinter import filedialog, messagebox
# # # import subprocess
# # # import serial.tools.list_ports
# # # import sys


# # # def list_serial_ports():
# # #     ports = serial.tools.list_ports.comports()
# # #     return [port.device for port in ports]


# # # def flash_bin():
# # #     bin_file = filedialog.askopenfilename(filetypes=[("BIN files", "*.bin")])
# # #     if not bin_file:
# # #         return

# # #     selected_port = port_var.get()
# # #     if not selected_port:
# # #         messagebox.showwarning("No Port", "Please select a serial port.")
# # #         return

# # #     python_executable = sys.executable
# # #     try:
# # #         result = subprocess.run(
# # #             [python_executable, "-m", "bflb_mcu_tool",
# # #              "--chipname=bl616",
# # #              f"--port={selected_port}",
# # #              f"--firmware={bin_file}"],
# # #             check=True, capture_output=True, text=True
# # #         )
# # #         lines = result.stdout.strip().splitlines()
# # #         if lines and "All Successful" in lines[-1]:
# # #             messagebox.showinfo("Success", "Flashing completed successfully!")
# # #         else:
# # #             last_lines = '\n'.join(lines[-10:])
# # #             messagebox.showinfo("Failed", last_lines)    
# # #     except subprocess.CalledProcessError as e:
# # #         messagebox.showerror("Error", e.stderr or str(e))


# # # # GUI setup
# # # root = tk.Tk()
# # # root.title("Synth Flasher")

# # # # Serial port dropdown
# # # tk.Label(root, text="Select Serial Port:").pack(pady=(10, 0))
# # # port_var = tk.StringVar()
# # # ports = list_serial_ports()
# # # if ports:
# # #     port_var.set(ports[0])
# # # port_menu = tk.OptionMenu(root, port_var, *ports)
# # # port_menu.pack(pady=(0, 10))

# # # # Flash button
# # # flash_button = tk.Button(root, text="Select .bin and Flash", command=flash_bin)
# # # flash_button.pack(padx=20, pady=20)

# # # root.mainloop()


# # import tkinter as tk
# # from tkinter import filedialog, messagebox
# # import subprocess
# # import serial.tools.list_ports
# # import sys
# # import threading


# # def list_serial_ports():
# #     ports = serial.tools.list_ports.comports()
# #     return [port.device for port in ports]


# # def refresh_ports():
# #     ports = list_serial_ports()
# #     port_var.set('')  # clear selection
# #     port_menu['menu'].delete(0, 'end')
# #     for port in ports:
# #         port_menu['menu'].add_command(label=port, command=tk._setit(port_var, port))
# #     if ports:
# #         port_var.set(ports[0])
# #     status_label.config(text="Ports refreshed.")


# # def flash_bin():
# #     bin_file = filedialog.askopenfilename(filetypes=[("BIN files", "*.bin")])
# #     if not bin_file:
# #         return

# #     selected_port = port_var.get()
# #     if not selected_port:
# #         messagebox.showwarning("No Port", "Please select a serial port.")
# #         return

# #     def run_flash():
# #         python_executable = sys.executable
# #         try:
# #             status_label.config(text="Flashing... please wait")
# #             flash_button.config(state='disabled')
# #             refresh_button.config(state='disabled')

# #             result = subprocess.run(
# #                 [python_executable, "-m", "bflb_mcu_tool",
# #                  "--chipname=bl616",
# #                  f"--port={selected_port}",
# #                  f"--firmware={bin_file}"],
# #                 check=True, capture_output=True, text=True
# #             )
# #             lines = result.stdout.strip().splitlines()
# #             if lines and "All Successful" in lines[-1]:
# #                 messagebox.showinfo("Success", "Flashing completed successfully!")
# #             else:
# #                 last_lines = '\n'.join(lines[-10:])
# #                 messagebox.showinfo("Failed", last_lines)
# #         except subprocess.CalledProcessError as e:
# #             messagebox.showerror("Error", e.stderr or str(e))
# #         finally:
# #             status_label.config(text="")
# #             flash_button.config(state='normal')
# #             refresh_button.config(state='normal')

# #     threading.Thread(target=run_flash, daemon=True).start()


# # # GUI setup
# # root = tk.Tk()
# # root.geometry("400x200")
# # root.title("Synth Flasher")

# # # Serial port dropdown
# # tk.Label(root, text="Select Serial Port:").pack(pady=(10, 0))
# # port_var = tk.StringVar()
# # ports = list_serial_ports()
# # if ports:
# #     port_var.set(ports[0])
# # port_menu = tk.OptionMenu(root, port_var, *ports)
# # port_menu.pack(pady=(0, 10))

# # # Refresh ports button
# # refresh_button = tk.Button(root, text="Refresh Ports", command=refresh_ports)
# # refresh_button.pack(pady=(0, 10))

# # # Flash button
# # flash_button = tk.Button(root, text="Select .bin and Flash", command=flash_bin)
# # flash_button.pack(padx=20, pady=20)

# # # Status label
# # status_label = tk.Label(root, text="", fg="#666666")
# # status_label.pack(pady=(0, 10))

# # root.mainloop()


# import tkinter as tk
# from tkinter import filedialog, messagebox
# import serial.tools.list_ports
# import threading
# import sys
# import runpy


# def list_serial_ports():
#     ports = serial.tools.list_ports.comports()
#     return [port.device for port in ports]


# def refresh_ports():
#     ports = list_serial_ports()
#     port_var.set('')
#     port_menu['menu'].delete(0, 'end')
#     for port in ports:
#         port_menu['menu'].add_command(label=port, command=tk._setit(port_var, port))
#     if ports:
#         port_var.set(ports[0])
#     status_label.config(text="Ports refreshed.")


# def flash_bin():
#     bin_file = filedialog.askopenfilename(filetypes=[("BIN files", "*.bin")])
#     if not bin_file:
#         return

#     selected_port = port_var.get()
#     if not selected_port:
#         messagebox.showwarning("No Port", "Please select a serial port.")
#         return

#     def run_flash():
#         try:
#             status_label.config(text="Flashing... please wait")
#             flash_button.config(state='disabled')
#             refresh_button.config(state='disabled')

#             # Save original sys.argv
#             original_argv = sys.argv.copy()
#             sys.argv = [
#                 "bflb_mcu_tool",
#                 "--chipname=bl616",
#                 f"--port={selected_port}",
#                 f"--firmware={bin_file}"
#             ]
#             runpy.run_module("bflb_mcu_tool", run_name="__main__")
#             messagebox.showinfo("Success", "Flashing completed successfully!")

#         except SystemExit as e:
#             if e.code != 0:
#                 messagebox.showerror("Error", f"bflb_mcu_tool failed with code {e.code}")
#             else:
#                 messagebox.showinfo("Success", "Flashing completed successfully.")
#         except Exception as e:
#             messagebox.showerror("Exception", str(e))
#         finally:
#             sys.argv = original_argv
#             status_label.config(text="")
#             flash_button.config(state='normal')
#             refresh_button.config(state='normal')

#     threading.Thread(target=run_flash, daemon=True).start()


# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry("400x200")
#     root.title("Synth Flasher")

#     tk.Label(root, text="Select Serial Port:").pack(pady=(10, 0))
#     port_var = tk.StringVar()
#     ports = list_serial_ports()
#     if ports:
#         port_var.set(ports[0])
#     port_menu = tk.OptionMenu(root, port_var, *ports)
#     port_menu.pack(pady=(0, 10))

#     refresh_button = tk.Button(root, text="Refresh Ports", command=refresh_ports)
#     refresh_button.pack(pady=(0, 10))

#     flash_button = tk.Button(root, text="Select .bin and Flash", command=flash_bin)
#     flash_button.pack(padx=20, pady=20)

#     status_label = tk.Label(root, text="", fg="#666666")
#     status_label.pack(pady=(0, 10))

#     root.mainloop()


import tkinter as tk
from tkinter import filedialog, messagebox
import serial.tools.list_ports
import threading
import subprocess
import sys


def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]


def refresh_ports():
    ports = list_serial_ports()
    port_var.set('')
    port_menu['menu'].delete(0, 'end')
    for port in ports:
        port_menu['menu'].add_command(label=port, command=tk._setit(port_var, port))
    if ports:
        port_var.set(ports[0])
    status_label.config(text="Ports refreshed.")


def flash_bin():
    bin_file = filedialog.askopenfilename(filetypes=[("BIN files", "*.bin")])
    if not bin_file:
        return

    selected_port = port_var.get()
    if not selected_port:
        messagebox.showwarning("No Port", "Please select a serial port.")
        return

    def run_flash():
        try:
            status_label.config(text="Flashing... please wait")
            flash_button.config(state='disabled')
            refresh_button.config(state='disabled')

            result = subprocess.run([
                sys.executable, "-m", "bflb_mcu_tool",
                "--chipname=bl616",
                f"--port={selected_port}",
                f"--firmware={bin_file}"
            ], check=True, capture_output=True, text=True)

            lines = result.stdout.strip().splitlines()
            if lines and "All Successful" in lines[-1]:
                messagebox.showinfo("Success", "Flashing completed successfully!")
            else:
                last_lines = '\n'.join(lines[-10:])
                messagebox.showinfo("Failed", last_lines)

        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", e.stderr or str(e))
        finally:
            status_label.config(text="")
            flash_button.config(state='normal')
            refresh_button.config(state='normal')

    threading.Thread(target=run_flash, daemon=True).start()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x200")
    root.title("Synth Flasher")

    tk.Label(root, text="Select Serial Port:").pack(pady=(10, 0))
    port_var = tk.StringVar()
    ports = list_serial_ports()
    if ports:
        port_var.set(ports[0])
    port_menu = tk.OptionMenu(root, port_var, *ports)
    port_menu.pack(pady=(0, 10))

    refresh_button = tk.Button(root, text="Refresh Ports", command=refresh_ports)
    refresh_button.pack(pady=(0, 10))

    flash_button = tk.Button(root, text="Select .bin and Flash", command=flash_bin)
    flash_button.pack(padx=20, pady=20)

    status_label = tk.Label(root, text="", fg="#666666")
    status_label.pack(pady=(0, 10))

    root.mainloop()
