pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the Docker image...'
                sh 'docker build -t my-sample-app .'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'echo "No tests yet"'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Cleaning up old containers...'
                sh '''
                    docker rm -f sample-app || true
                '''
                echo 'Deploying container...'
                sh 'docker run -d --name sample-app -p 8081:8080 my-sample-app'
            }
        }
    }
}
