pipeline{
    agent any

    stages{
        stage('Checkout'){
            steps {
                git 'https://github.com/dellindone/jenkins-python-demo.git'
            }
        }
        stage('Install Dependencies'){
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image'){
            steps {
                sh '/usr/local/bin/docker build -t jenkins-python-demo .'
            }
        }

        stage('Stop Existing Container'){
            steps {
                sh '/usr/local/bin/docker stop jenkins-python-demo || true'
            }
        }

        stage('Remove Existing Container'){
            steps {
                sh '/usr/local/bin/docker rm jenkins-python-demo || true'
            }
        }

        stage('Run container'){
            steps {
                sh '/usr/local/bin/docker run -d -p 8000:80 --name jenkins-python-demo jenkins-python-demo'
            }
        }
    }
}