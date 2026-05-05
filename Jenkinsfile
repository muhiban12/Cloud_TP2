pipeline {
    agent any
    environment {
        DOCKER_HUB_USER = "muhiban"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/muhiban12/Cloud_TP2.git'
            }
        }

        stage('Build & Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USER')]) {
                    // Gunakan sh dan ganti pemanggilan variabel ke $DOCKER_HUB_USER
                    sh "docker build -t ${DOCKER_HUB_USER}/backend-tugas1:latest ./backend"
                    sh "docker build -t ${DOCKER_HUB_USER}/frontend-tugas1:latest ./frontend"
                    
                    sh "docker login -u ${DOCKER_USER} -p ${DOCKER_PASSWORD}"
                    sh "docker push ${DOCKER_HUB_USER}/backend-tugas1:latest"
                    sh "docker push ${DOCKER_HUB_USER}/frontend-tugas1:latest"
                }
            }
        }

        stage('Deploy to AKS') {
            steps {
                withCredentials([file(credentialsId: 'k8s-config', variable: 'KUBECONFIG')]) {
                    // Pastikan variabel KUBECONFIG juga dipanggil dengan tanda $
                    sh "kubectl --kubeconfig=${KUBECONFIG} apply -f k8s/backend-k8s.yaml"
                    sh "kubectl --kubeconfig=${KUBECONFIG} apply -f k8s/frontend-k8s.yaml"
                    sh "kubectl --kubeconfig=${KUBECONFIG} apply -f k8s/ingress.yaml"
                }
            }
        }
    }
}
