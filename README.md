# QuizGen 🧠

A modern Quiz Generation Application that creates AI and ML multiple-choice questions (MCQs) with intelligent explanations. Built with React, FastAPI, and powered by OpenAI's GPT-3.5 Turbo.

![QuizGen](frontend/quiz.webp)

## ✨ Features

- **AI-Powered Quiz Generation**: Generate high-quality MCQs on AI and ML topics
- **Smart Question Format**: 4 options per question with one correct answer
- **Detailed Explanations**: AI-generated explanations for correct answers
- **User Authentication**: Secure authentication powered by Clerk
- **Modern UI**: Clean, responsive interface built with React and Vite
- **Real-time API**: Fast and efficient FastAPI backend
- **Persistent Storage**: SQLite database for data management

## 🛠️ Tech Stack

### Frontend
- **React** - Modern JavaScript library for building user interfaces
- **Vite** - Fast build tool and development server
- **Clerk** - User authentication and management
- **React Router** - Client-side routing

### Backend
- **Python** - Programming language
- **FastAPI** - Modern, fast web framework for building APIs
- **SQLite** - Lightweight database for data storage
- **SQLAlchemy** - SQL toolkit and ORM

### AI Integration
- **OpenAI API** - GPT-3.5 Turbo model
- **Temperature**: 0.6 for balanced creativity and accuracy

### Development Tools
- **Ngrok** - Secure tunneling for local development
- **UV** - Fast Python package manager

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** (v16 or higher)
- **Python** (v3.13 or higher)
- **npm** or **yarn**
- **Git**

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ahmadsultan03/QuizGen.git
cd QuizGen-App
```

### 2. Backend Setup

#### Navigate to Backend Directory
```bash
cd backend
```

#### Install Python Dependencies
```bash
# Using UV (recommended)
uv sync

# Or using pip
pip install -r requirements.txt
```

#### Environment Configuration
Create a `.env` file in the backend directory:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Clerk Configuration
CLERK_SECRET_KEY=your_clerk_secret_key_here
CLERK_WEBHOOK_SECRET=your_clerk_webhook_secret_here

# Database Configuration
DATABASE_URL=sqlite:///./database.db

# Ngrok Configuration
NGROK_AUTH_TOKEN=your_ngrok_auth_token_here
```

#### Initialize Database
```bash
python -c "from src.database import create_tables; create_tables()"
```

### 3. Frontend Setup

#### Navigate to Frontend Directory
```bash
cd ../frontend
```

#### Install Dependencies
```bash
npm install
# or
yarn install
```

#### Environment Configuration
Create a `.env` file in the frontend directory:

```env
VITE_CLERK_PUBLISHABLE_KEY=your_clerk_publishable_key_here
VITE_API_BASE_URL=http://localhost:8000
```

## 🔧 Configuration

### OpenAI API Key Setup
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Create an account or sign in
3. Navigate to API Keys section
4. Create a new API key
5. Add the key to your backend `.env` file

### Clerk Authentication Setup
1. Visit [Clerk Dashboard](https://clerk.com/)
2. Create a new application
3. Get your publishable key and secret key
4. Configure webhook endpoints for user management
5. Add keys to respective `.env` files

### Ngrok Setup
1. Visit [Ngrok](https://ngrok.com/)
2. Create an account
3. Get your auth token
4. Install ngrok CLI
5. Add token to backend `.env` file

## 🏃‍♂️ Running the Application

### Start Backend Server
```bash
cd backend
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

### Start Frontend Development Server
```bash
cd frontend
npm run dev
# or
yarn dev
```

### Access the Application
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 📁 Project Structure

```
QuizGen-App/
├── backend/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── services/
│   ├── server.py
│   ├── pyproject.toml
│   └── database.db
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── utils/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── public/
│   ├── package.json
│   └── vite.config.js
└── README.md
```

## 🔌 API Endpoints

### Authentication
- `POST /auth/webhook` - Clerk webhook for user management

### Quiz Management
- `GET /api/quizzes` - Get all quizzes
- `POST /api/quizzes` - Create new quiz
- `GET /api/quizzes/{id}` - Get specific quiz
- `DELETE /api/quizzes/{id}` - Delete quiz

### Question Generation
- `POST /api/generate` - Generate AI-powered questions

## 🧪 Usage

1. **Sign Up/Login**: Use Clerk authentication to create an account
2. **Generate Quiz**: Click on "Generate Quiz" and specify your topic
3. **Take Quiz**: Answer the multiple-choice questions
4. **View Results**: See your score and explanations for correct answers
5. **Save Progress**: Your quizzes are automatically saved to your account

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for providing the GPT-3.5 Turbo API
- Clerk for authentication services
- FastAPI and React communities for excellent documentation
- All contributors who helped improve this project

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/ahmadsultan03/QuizGen.git/issues) page
2. Create a new issue with detailed information
3. Contact m.ahmad.sultan82@gmail.com
4. Whatsapp: +92-306-1611301

---

**Happy Learning! 🎓**
