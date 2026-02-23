🏨 Hotel Management System

A desktop-based Hotel Management System built using Python (Tkinter GUI) and MongoDB.
This application allows users to book hotel rooms, store customer data in a database, and view all bookings through a simple graphical interface.

📌 Features

✅ User-friendly GUI using Tkinter

✅ MongoDB database integration

✅ Room booking form with validation

✅ View all stored bookings

✅ Background image support

✅ Mandatory & optional fields

🛠️ Tech Stack
Technology	Purpose
Python	Core programming language
Tkinter	GUI framework
Pillow (PIL)	Image handling
PyMongo	MongoDB connection
MongoDB	Database
📁 Project Structure
HOTEL-MANAGEMENT-SYSTEM-/
├── hotel_management.py
├── atlantis-the-palm.jpg
├── README.md
└── .gitignore
🗄️ Database Details

Database Name: hotel_management

Collection Name: customers

MongoDB URI: mongodb://localhost:27017/

Make sure MongoDB is installed and running locally before starting the application.

📝 Booking Form Fields
🔴 Mandatory Fields

Customer Name

Room Type (Single / Double)

Number of Days

Phone Number

🟢 Optional Fields

Email Address

Location

Food Preference

Special Requests

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/GUNJIVENKATAKRISHNAKARTHIK/HOTEL-MANAGEMENT-SYSTEM-.git
cd HOTEL-MANAGEMENT-SYSTEM-
2️⃣ Install Required Packages
pip install pymongo pillow
3️⃣ Install & Start MongoDB

Make sure MongoDB is running:

mongod
▶️ Run the Application
python hotel_management.py
💡 How It Works

User enters booking details in the form.

Clicks Book Room.

Data is validated (first 4 fields required).

Information is stored in MongoDB.

Click View Bookings to see all saved records.

🧹 Ignored Files

This project uses a .gitignore file to exclude:

.idea/

__pycache__/

*.pyc

These files are environment-specific and not required to run the project.

🚀 Future Improvements

Add pricing & automatic bill calculation

Add update/delete booking feature

Add search functionality

Add admin login system

Export bookings to CSV

👨‍💻 Author

GUNJI VENKATA KRISHNA KARTHIK
