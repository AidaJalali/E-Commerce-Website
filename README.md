# 🛍 Django E-Commerce Website  
A simple e-commerce website built with **Django**, allowing users to browse products, add items to their cart, and place orders (without payment integration).  

---

## 📌 Features  
✅ **User Authentication** – Sign up, log in, and log out functionality.  
✅ **Product Management** – View product details and browse categories.  
✅ **Shopping Cart** – Add/remove products and update quantities.  
✅ **Order Placement** – Users can place an order (without payment).  
✅ **Admin Dashboard** – Manage products, orders, and users.  

---

## 🚀 Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/AidaJalali/E-Commerce-Website.git
cd E-Commerce-Website
```

### 2️⃣ Create & Activate a Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate   # For macOS/Linux  
.\venv\Scripts\activate    # For Windows  
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations  
```bash
python manage.py migrate
```

### 5️⃣ Create a Superuser (For Admin Access)  
```bash
python manage.py createsuperuser
```
Follow the prompts to set a username and password.

### 6️⃣ Run the Development Server  
```bash
python manage.py runserver
```
Now, visit **`http://127.0.0.1:8000/`** in your browser.


## 💡 Technologies Used  
- **Django** – Backend framework  
- **SQLite** – Database (can be replaced with PostgreSQL/MySQL)  
- **Bootstrap** – Frontend styling  
- **HTML, CSS, JavaScript** – For UI design  

---

## 📜 License  
This project is open-source and free to use.  

---

## 🎯 Next Steps  
🚀 Add payment integration (e.g., Stripe, PayPal).  
📦 Implement product categories and search functionality.  
📊 Improve UI with better CSS and JavaScript animations.  
