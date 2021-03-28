pipeline {
  agent { dockerfile true }
  stages {
    stage("Test back end") {
      steps {
        sh "pip install pipenv"
        sh 'pipenv install -d'
        sh 'flake8'
      }
    }
  }
}
