pipeline {
    agent { docker { image 'pmantini/assignment-cosc6380:latest' } }
    
    environment {
        PATH = "env/bin/:$PATH"
    }
    stages {
        stage('build') {
            steps {
                sh 'python dip_hw2_shapes.py  > output/shape_counting/output.txt'
            }
        }                
    }
    post {
        always {
            archiveArtifacts artifacts: 'output/**/*.* ', onlyIfSuccessful: true
        }
    }
}

