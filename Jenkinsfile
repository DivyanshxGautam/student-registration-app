pipeline {
    agent any

    stages {
        stage('Checkout Source Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python test dependencies...'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Execute Automated Tests') {
            steps {
                echo 'Running BeautifulSoup DOM validation tests...'
                sh 'python3 test_form.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline Execution Status: SUCCESS (All HTML input fields verified)'
        }
        failure {
            echo 'Pipeline Execution Status: FAILURE (HTML form verification failed)'
        }
    }
}