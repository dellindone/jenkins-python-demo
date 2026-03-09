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
                sh '/usr/local/bin/docker build -t jenkins-python-demo:${BUILD_NUMBER} .'
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
                sh '/usr/local/bin/docker run -d -p 8000:80 --name jenkins-python-demo jenkins-python-demo:${BUILD_NUMBER}'
            }
        }

        stage('Test Application'){
            steps {
                sh '''
                    for i in {1..10}; do
                        curl -f http://127.0.0.1:8000/healthcheck && exit 0
                        echo "Waiting for service..."
                        sleep 5
                    done
                    exit 1
                '''
            }
        }
    }
}