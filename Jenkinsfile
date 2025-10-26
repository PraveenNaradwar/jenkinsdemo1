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
                bat "python extract.py"
            }
        }

        }
     }
