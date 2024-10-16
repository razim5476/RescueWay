# Disaster Network

**A comprehensive disaster management platform that provides resources, volunteer coordination, emergency alerts, and educational content to assist communities during disasters.**

## Features

- **User Management:** Register, log in, and manage user profiles.
- **Disaster Management:** Send alerts and notifications to users during disasters.
- **Fundraising:** Create and manage fundraising campaigns to support relief efforts.
- **Volunteer Management:** Sign up volunteers, manage approvals, and coordinate disaster relief efforts.
- **Resource Hub:** Provides useful links, educational content, and emergency contact information.
- **Blog Section:** Allows users to share their experiences, stories, and tips related to disaster preparedness and recovery.
- **Gallery:** Displays images related to relief efforts and disaster response.

## Installation

1. **Clone the repository:**

   
2.**Navigate to the project directory:**
  cd DisasterNetwork

3.**Set up a virtual environment:
  python -m venv venv

4.**Activate the virtual environment:
  On Windows:
  venv\Scripts\activate

  On macOS/Linux:
  source venv/bin/activate
  
  Install the required dependencies:
  pip install -r requirements.txt

  Set up the database:
  python manage.py migrate
  
  Create a superuser for admin access:
  python manage.py createsuperuser
  
  Run the development server:
  python manage.py runserver
  
  **Usage**
  Access the website at http://127.0.0.1:8000/.
  Log in or sign up to explore the features.
  Admin users can add content to the Resource Hub, approve volunteers, and manage fundraising campaigns.
  Users can read blogs, add comments, and access emergency information.
  Project Structure

  DisasterNetwork/
  ├── disaster_network/       # Project settings and URLs
  ├── user_management/        # User authentication and profiles
  ├── disaster_management/    # Alert notifications and disaster management
  ├── fundraising/            # Fundraising campaigns
  ├── volunteer_management/   # Volunteer registration and approval
  ├── resources/              # Useful links, educational content, emergency contacts
  ├── blog/                   # Blog section for user stories and experiences
  ├── gallery/                # Gallery for relief images
  └── README.md               # Project documentation


  Contributing
  Fork the repository.
  Create a new branch:

  git checkout -b feature-branch
  Make your changes.
  Commit your changes:
  git commit -m "Add new feature"
  Push to the branch:
  git push origin feature-branch
  Create a pull request.



  **Contact**
  For any questions or suggestions, feel free to reach out at [razimmuhammed8055@gmail.com].



  Technologies Used
  Backend: Django, Python
  Frontend: HTML, CSS, JavaScript, Bootstrap
  Database: SQLite (or PostgreSQL, MySQL if configured)
  Version Control: Git and GitHub
  Future Improvements
  Real-time Notifications: Implement WebSocket-based real-time notifications for alerts.
  Multi-language Support: Add support for multiple languages to cater to a global audience.
  Mobile App Integration: Develop a mobile app version for Android and iOS.
  AI and Machine Learning: Integrate AI to predict potential disaster zones using data analysis.
