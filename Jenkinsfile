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
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build Dcoker Image'){
            steps {
                sh 'docker build -t jenkins-python-demo .'
            }
        }

        stage('Run container'){
            steps {
                sh 'docker run -d -p 8000:80 python-demo'
            }
        }
    }
}