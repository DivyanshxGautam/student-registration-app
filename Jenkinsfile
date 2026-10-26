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
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Form Tests') {
            steps {
                bat 'python test_form.py'
            }
        }
    }

    post {
        success {
            echo 'Build Passed: All HTML form fields verified successfully!'
        }
        failure {
            echo 'Build Failed: HTML form verification failed!'
        }
    }
}