pipeline{
     agent any
     stages{
        stage('Checkout code'){
            steps{
                checkout scm
            }
        }
        stage('Extract Data'){
            steps{
                bat "C:\\Users\\S\\AppData\\Local\\Programs\\Python\\Python313\\python.exe extract.py"
            }
        }

    
     }

}     
