pipeline {
    agent any
    environment {
        // Sesuaikan dengan Username Docker Hub kamu
        DOCKER_HUB_USER = "muhiban"
    }
    stages {
        stage('Checkout') {
            steps {
                // Mengambil kode dari GitHub
                git branch: 'main', url: 'https://github.com/muhiban12/Cloud_TP2.git'
            }
        }

        stage('Build & Push') {
            steps {
                // Memanggil kredensial Docker Hub (ID harus sesuai dengan yang ada di Jenkins)
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USER')]) {
                    bat "docker build -t %DOCKER_HUB_USER%/backend-tugas1:latest ./backend"
                    bat "docker build -t %DOCKER_HUB_USER%/frontend-tugas1:latest ./frontend"
                    
                    // Login dan Push menggunakan variabel dari credentials
                    bat "docker login -u %DOCKER_USER% -p %DOCKER_PASSWORD%"
                    bat "docker push %DOCKER_HUB_USER%/backend-tugas1:latest"
                    bat "docker push %DOCKER_HUB_USER%/frontend-tugas1:latest"
                }
            }
        }

        stage('Deploy to AKS') {
            steps {
                // Memanggil file kubeconfig yang diupload sebagai 'Secret file' dengan ID 'k8s-config'
                withCredentials([file(credentialsId: 'k8s-config', variable: 'KUBECONFIG')]) {
                    // Menggunakan flag --kubeconfig agar kubectl tahu letak file kuncinya di Windows
                    bat "kubectl --kubeconfig=%KUBECONFIG% apply -f k8s/backend-k8s.yaml"
                    bat "kubectl --kubeconfig=%KUBECONFIG% apply -f k8s/frontend-k8s.yaml"
                    bat "kubectl --kubeconfig=%KUBECONFIG% apply -f k8s/ingress.yaml"
                }
            }
        }
    }
}
