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
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
                sh 'pip install pytest-html'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest -s -v --html=report/report.html --self-contained-html'
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
