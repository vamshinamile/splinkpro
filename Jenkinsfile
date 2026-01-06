pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\vamshi.namile\\AppData\\Local\\Python\\bin\\python.exe" --version'
                bat '"C:\\Users\\vamshi.namile\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run API Tests') {
            steps {
                bat '"C:\\Users\\vamshi.namile\\AppData\\Local\\Python\\bin\\python.exe" -m pytest -v'
            }
        }
    }
}
