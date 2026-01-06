pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests using venv') {
            steps {
                bat """
                "%WORKSPACE%\\venv\\Scripts\\python.exe" ^
                "%WORKSPACE%\\run_tests_and_send_report.py"
                """
            }
        }
    }

    post {
        always {
            echo "Test execution completed"
        }
    }
}
