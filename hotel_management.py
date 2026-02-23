import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from PIL import Image, ImageTk  # Pillow for image handling

# MongoDB Connection
client = MongoClient('mongodb://localhost:27017/')  # Change if needed
db = client['hotel_management']  # Database name
collection = db['customers']  # Collection name

# Create the main application window
root = tk.Tk()
root.title("Hotel Management System")
root.geometry("800x700")  # Set the size of the window

# Load the background image using Pillow
background_image_path = "atlantis-the-palm.jpg"  # Replace with the actual image path

try:
    bg_image = Image.open(background_image_path)  # Open the image file
    bg_image = bg_image.resize((1360, 1020), Image.LANCZOS)  # Resize to fit the window
    bg_photo = ImageTk.PhotoImage(bg_image)  # Convert the image to Tkinter-compatible format

    # Create a label to display the background image
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Make the label fill the entire window

except Exception as e:
    print(f"Error loading background image: {e}")
    bg_label = tk.Label(root, text="Error loading background image", font=("Arial", 14), fg="red")
    bg_label.pack()

# Add a title label with custom font and color
title_label = tk.Label(root, text="Welcome to the Hotel Management System", font=("Arial", 24, "bold"), fg="yellow", bg="orange")
title_label.place(relx=0.5, y=20, anchor="n")  # Centered at the top

# Create a frame for the form with a light color for simulated translucency
form_frame = tk.Frame(root, bg="light blue", bd=3, relief=tk.RAISED, padx=20, pady=20)  # Light gray for pseudo-transparency
form_frame.place(x=50, rely=0.2)  # Place the form frame near the left side, 50px from the left

# Labels and entry fields for customer details
name_label = tk.Label(form_frame, text="Customer Name", font=("Arial", 16), bg="#F0F0F0")
name_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
name_entry = tk.Entry(form_frame, font=("Arial", 14), width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)

room_type_label = tk.Label(form_frame, text="Room Type (Single/Double)", font=("Arial", 16), bg="#F0F0F0")
room_type_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
room_type_entry = tk.Entry(form_frame, font=("Arial", 14), width=30)
room_type_entry.grid(row=1, column=1, padx=10, pady=10)

days_label = tk.Label(form_frame, text="Number of Days", font=("Arial", 16), bg="#F0F0F0")
days_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
days_entry = tk.Entry(form_frame, font=("Arial", 14), width=30)
days_entry.grid(row=2, column=1, padx=10, pady=10)

# Extra details - Phone Number, Email, Location
phone_label = tk.Label(form_frame, text="Phone Number", font=("Arial", 16), bg="#F0F0F0")
phone_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)
phone_entry = tk.Entry(form_frame, font=("Arial", 14), width=30)
phone_entry.grid(row=3, column=1, padx=10, pady=10)

email_label = tk.Label(form_frame, text="Email Address", font=("Arial", 16), bg="#F0F0F0")
email_label.grid(row=4, column=0, sticky=tk.W, padx=10, pady=10)
email_entry = tk.Entry(form_frame, font=("Arial", 14), width=30)
email_entry.grid(row=4, column=1, padx=10, pady=10)

location_label = tk.Label(form_frame, text="Location", font=("Arial", 16), bg="#F0F0F0")
location_label.grid(row=5, column=0, sticky=tk.W, padx=10, pady=10)
location_entry = tk.Entry(form_frame, font=("Arial", 14), width=30)
location_entry.grid(row=5, column=1, padx=10, pady=10)

# New fields for Food Details
food_label = tk.Label(form_frame, text="Food Preference", font=("Arial", 16), bg="#F0F0F0")
food_label.grid(row=6, column=0, sticky=tk.W, padx=10, pady=10)
food_entry = tk.Entry(form_frame, font=("Arial", 14), width=30)
food_entry.grid(row=6, column=1, padx=10, pady=10)

special_requests_label = tk.Label(form_frame, text="Special Requests", font=("Arial", 16), bg="#F0F0F0")
special_requests_label.grid(row=7, column=0, sticky=tk.W, padx=10, pady=10)
special_requests_entry = tk.Entry(form_frame, font=("Arial", 14), width=30)
special_requests_entry.grid(row=7, column=1, padx=10, pady=10)

# Function to book a room
def book_room():
    customer_name = name_entry.get()
    room_type = room_type_entry.get()
    days = days_entry.get()
    phone_number = phone_entry.get()
    email = email_entry.get()
    location = location_entry.get()
    food_preference = food_entry.get()
    special_requests = special_requests_entry.get()

    if customer_name and room_type and days and phone_number and email and location and food_preference:
        try:
            days = int(days)
            # Insert data into MongoDB
            collection.insert_one({
                'customer_name': customer_name,
                'room_type': room_type,
                'days': days,
                'phone_number': phone_number,
                'email': email,
                'location': location,
                'food_preference': food_preference,
                'special_requests': special_requests
            })
            messagebox.showinfo("Success", "Room Booked Successfully!")
            clear_entries()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of days.")
    else:
        messagebox.showerror("Error", "All fields are required!")

# Function to view bookings
def view_bookings():
    bookings = collection.find()
    booking_info = ""
    for booking in bookings:
        booking_info += f"Name: {booking['customer_name']}, Room: {booking['room_type']}, Days: {booking['days']}, Phone: {booking['phone_number']}, Email: {booking['email']}, Location: {booking['location']}, Food: {booking['food_preference']}, Requests: {booking['special_requests']}\n"

    if booking_info:
        messagebox.showinfo("All Bookings", booking_info)
    else:
        messagebox.showinfo("No Bookings", "No bookings found!")

# Clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    room_type_entry.delete(0, tk.END)
    days_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    location_entry.delete(0, tk.END)
    food_entry.delete(0, tk.END)
    special_requests_entry.delete(0, tk.END)

# Buttons Frame
button_frame = tk.Frame(root, bg="light green")
button_frame.place(x=50, rely=0.8, anchor="w")  # Place the buttons on the left side below the form

# Buttons for actions
save_button = tk.Button(button_frame, text="Book Room", font=("Arial", 16), bg="navy", fg="white", width=12, command=book_room)
save_button.grid(row=0, column=0, padx=20, pady=10)

view_button = tk.Button(button_frame, text="View Bookings", font=("Arial", 16), bg="green", fg="white", width=12, command=view_bookings)
view_button.grid(row=0, column=1, padx=20, pady=10)

# Run the Tkinter event loop
root.mainloop()
