pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the Docker image...'
                sh 'docker build -t flask-app .'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                // Replace with actual tests
                sh 'echo "No tests yet"'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying container locally...'
                sh 'docker run -d -p 5000:5000 --name flask-container flask-app || true'
            }
        }
    }
}
