# Voting System Template

Welcome to the **Voting System Template**, a base project built for educational purposes.  
This project was created for a workshop about **electronic voting systems** and includes the core modules of **authentication**, **user management**, **votings**, and **votes**.  
Participants are expected to **extend** and **customize** the application during the session.

---

## Features

- **User Authentication:** Secure login and registration.
- **Voting Creation and Management:** Users can create votings and cast votes.
- **Session-Based Security:** Prevents double voting and enforces access rules.

---

## Tech Stack

- **Backend:** Django Rest Framework (Python)
- **Database:** SQLite (for simplicity)

---

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-repo/voting-system-template.git
   cd voting-system-template
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

---

## How we Extended It

---

## Authors

> Please add your name and contribution below:

- **Your Name** – Initial project setup and backend implementation
- **[Add your name here]** – [e.g., Frontend improvement / Voting logic extension]
- **[Add your name here]** – [e.g., Email notification feature]

---

## License

MIT License. Free to use and modify during the workshop.
