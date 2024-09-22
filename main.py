import tkinter as tk
from tkinter import messagebox
import json
from sending_data import send_json_data  # Import the function to send data

def submit_form():
    # Get the values entered by the user
    cmd_name = entry_cmd_name.get()
    data = entry_data.get()
    range_val = entry_range.get()
    status = status_var.get()

    # Check if any fields are empty
    if not cmd_name or not data or not range_val or not status:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    # Create a dictionary with the form data
    form_data = {
        "cmd_name": cmd_name,
        "data": data,
        "range": range_val,
        "status": status
    }

    # Convert the form data to JSON
    json_data = json.dumps(form_data, indent=4)

    # Write the JSON data to sending_data.py
    try:
        with open('sending_data.py', 'w') as f:
            f.write(f"json_data = '''{json_data}'''\n")
        messagebox.showinfo("Success", "Data has been successfully written to sending_data.py")
        
        # Clear the fields after submission
        entry_cmd_name.delete(0, tk.END)  # Clear the 'Cmd Name' entry
        entry_data.delete(0, tk.END)      # Clear the 'Data' entry
        entry_range.delete(0, tk.END)     # Clear the 'Range' entry
        status_var.set("Pass")            # Reset the status to 'Pass'

        # Send the data over UDP using the send_json_data function
        server_ip = "127.0.0.1"  # Replace with the C++ server's IP
        server_port = 12345       # Replace with the correct port
        send_json_data(server_ip, server_port, form_data)
        messagebox.showinfo("Success", "Data has been sent successfully")
        
    except Exception as e:
        messagebox.showerror("File Error", f"An error occurred: {str(e)}")

# Create the main window
app = tk.Tk()
app.title("JSON Form Sender")
app.geometry("400x350")

# Create labels and entries using pack()
tk.Label(app, text="Cmd Name:").pack(pady=5)
entry_cmd_name = tk.Entry(app)
entry_cmd_name.pack(fill=tk.X, padx=10)

tk.Label(app, text="Data:").pack(pady=5)
entry_data = tk.Entry(app)
entry_data.pack(fill=tk.X, padx=10)

tk.Label(app, text="Range:").pack(pady=5)
entry_range = tk.Entry(app)
entry_range.pack(fill=tk.X, padx=10)

# Status Label
tk.Label(app, text="Status:").pack(pady=5)

# Create a variable for the status option
status_var = tk.StringVar()
status_var.set("Pass")  # Default value is "Pass"

# Create an OptionMenu for status selection
status_menu = tk.OptionMenu(app, status_var, "Pass", "Fail")
status_menu.pack(pady=5)

# Submit button at the bottom
submit_button = tk.Button(app, text="Submit", command=submit_form)
submit_button.pack(pady=20)

# Start the event loop
app.mainloop()
