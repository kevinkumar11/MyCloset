MyCloset, A Clothing Inventory & Profit Analytics Dashboard
An inventory management and analytics tool for tracking purchases, sales, and profit margins for clothing resale businesses.
Built with Python, Streamlit, and SQLite among other tools.

ABOUT:
This project was developed to manage and analyze my personal Depop(an online platform for selling mostly clothing) resale inventory.
Over time, I had accumulated 100s of clothing items, making it challenging to track purchase details, selling prices, and time spent in inventory.
There are many sellers that face the same struggles as me, some I have even met and spoke with in real life.
I designed this system to centralize all my inventory data in one place, where I can view and filter items by category, brand, size, etc.
Also integrated a Statistics Dashboard in order to create a better understanding on what products can generate the most revenue, as well as shortest time spent in store.

SCREENSHOTS:

FEATURES:
Add and update items with description, brand, type, size, purchase date, purchase price, and photo
Mark items as sold and record sold price and date
Filter inventory dynamically by type, brand, and size (auto-updates as new items are added)
Track days in inventory, profit margins, and top-selling categories
Automated Selenium testing for UI and functionality

TECH STACK:

Languages & Libraries:
Python,
Pandas,
Streamlit,
SQLite,
Selenium

Analytics Tools:
Plotly

Development & Project Management:
JIRA (requirements tracking, user stories),
Git & GitHub,
VS Code

PROJECT STRUCTURE:
clothing-inventory-dashboard/
│
├── db/                         # SQLite database files
├── db_inventory.py             # Database connection & queries
├── create_page.py               # Page to add inventory items
├── display_inventory_page.py    # Page to view and filter inventory
├── stats_page.py                # Analytics & stats page
├── test_streamlit_app.py        # Selenium test scripts
├── sales_app.py                 # Main Streamlit entry point
└── README.md                    # Project documentation

GETTING STARTED/HOW TO USE:

Prerequisites:
Python 3.10+
pip

Installation:
git clone https://github.com/kevinkumar11/sales-app.git
cd sales-app
pip install -r requirements.txt

Run the app:
streamlit run sales_app.py

IN DEVELOPMENT CURRENTLY:
Cross-posting feature among other selling apps (i.g. Grailed, Mercari, Poshmark)
Bulk Actions, allowing you to execute a similar command to multiple listings at once





