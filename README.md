# Gen-Image

Gen-Image is a modern AI-powered image generation application that leverages **Pollination AI**, **Django**, **Bootstrap**, and **Docker** to deliver seamless image creation based on user prompts. Its intuitive design ensures a smooth user experience, making it a perfect choice for creative professionals and hobbyists.

---

## 🌟 Features

- **AI-Driven Image Generation**: Input a text prompt, and Pollination AI generates a stunning image tailored to your description.
- **Responsive Design**: Built with Bootstrap, the app works perfectly on desktop, tablet, and mobile devices.
- **User Authentication**: Secure user management system using Django's built-in authentication features.
- **Scalable Deployment**: Docker ensures the app can be deployed on any environment with ease.
- **Interactive UI**: Simple and user-friendly interface for enhanced usability.

---

## 🛠️ Technologies Used

- **Frontend**: Bootstrap for responsive and modern design.
- **Backend**: Django for secure and efficient web development.
- **AI Integration**: Pollination AI for image generation.
- **Containerization**: Docker for environment consistency and scalability.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed on your system:
- [Python 3.8+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/products/docker-desktop)
- [Bootstrap](https://getbootstrap.com/)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/gen-image.git
   cd gen-image
2. **Download Docker Desktop**:
    [Docker Desktop Windows](https://docs.docker.com/desktop/setup/install/windows-install/),
    [Docker Desktop Linux](https://docs.docker.com/desktop/setup/install/linux/)
    - enable wsl on windows
    ```bash
    wsl --update
    
3. **Navigate to the project folder**:
    ```bash
    docker build -t genimage .
    docker run -p 8000:8000 genimage
4. **Navigate to the page**
    - http://127.0.0.1:8000