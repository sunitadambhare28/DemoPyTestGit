pipeline {
    agent any

    environment {
        // Define environment variables if needed
        WORKSPACE_DIR = "${WORKSPACE}"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/sunitadambhare28/DemoPyTestGit.git', branch: 'master'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Upgrade pip and install dependencies
                    bat 'cd %WORKSPACE% && python -m pip install --upgrade pip'
                    bat 'cd %WORKSPACE% && pip install -r requirements.txt'
                    bat 'cd %WORKSPACE% && pip install pytest-html'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run the tests with pytest and generate an HTML report
                    bat 'cd %WORKSPACE% && pytest -s -v --html=report/report.html --self-contained-html'
                }
            }
        }

        stage('Archive HTML Report') {
            steps {
                script {
                    // Archive the test report
                    publishHTML(target: [
                        reportName: 'Test Report',
                        reportDir: 'report',
                        reportFiles: 'report.html'
                    ])
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Securely copy files to remote server
                    bat 'scp %WORKSPACE%\\report\\report.html user@server:/deploy/path/'

                    // OPTIONAL: SSH into server to perform further steps
                    // bat 'ssh user@server "cd /deploy/path && do-something.sh"'
                }
            }
        }
    }
}
