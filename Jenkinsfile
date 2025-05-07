pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sunitadambhare28/DemoPyTestGit.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
                bat 'pip install pytest-html'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --html=report\\report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'report',
                reportFiles: 'report.html',
                reportName: 'Test Report'
            ])
        }
    }
}
