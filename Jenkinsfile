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
        stages('run extarct file'){
            steps{
                bat "${env.python} extact.py"
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
}