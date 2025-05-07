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
               powershell 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                powershell 'pytest -s -v --html=report/report.html --self-contained-html'
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
