pipeline {
    agent any
    environment {
        DOCKER_HUB_USER = "username_kamu"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/username/repo-kamu.git'
            }
        }
        stage('Build & Push') {
            steps {
                sh "docker build -t ${DOCKER_HUB_USER}/backend-tugas1:latest ./backend"
                sh "docker build -t ${DOCKER_HUB_USER}/frontend-tugas1:latest ./frontend"
                sh "docker login -u ${DOCKER_HUB_USER} -p ${DOCKER_PASSWORD}"
                sh "docker push ${DOCKER_HUB_USER}/backend-tugas1:latest"
                sh "docker push ${DOCKER_HUB_USER}/frontend-tugas1:latest"
            }
        }
        stage('Deploy to AKS') {
            steps {
                // Pastikan file kubeconfig sudah terpasang di agent Jenkins
                sh "kubectl apply -f k8s/backend-k8s.yaml"
                sh "kubectl apply -f k8s/frontend-k8s.yaml"
                sh "kubectl apply -f k8s/ingress.yaml"
            }
        }
    }
}