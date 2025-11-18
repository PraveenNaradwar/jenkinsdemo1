pipeline{
    agent any
    environment{
        Python="C:\\Users\\S\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
    }
    stages{
        stage('checkout code'){
            steps{
                checkout scm
            }
        }
        stage('Run extract file'){
                steps{
                    bat "${env.Python} extract_data.py"
                }
            }
        }
    }
    post{
        success{
            echo'pipeline completed'
        }
        failure{
            echo 'pipeline failed'
        }
        always{
            echo 'pipeline completed'
        }
    }
