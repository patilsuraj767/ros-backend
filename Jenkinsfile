pipeline {
  agent none

  stages {
    stage("Test back end") {
      agent {
        dockerfile {
          filename "Dockerfile"
        }
      }

      steps {
        sh "pip install pipenv"
        sh 'pipenv install -d'
        sh 'flake8'
      }
    }
  }
}
