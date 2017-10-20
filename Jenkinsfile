pipeline {
  agent any
  stages {
    stage('test') {
      parallel {
        stage('test1') {
          steps {
            sh 'python write_file.py test123'
          }
        }
        stage('test2') {
          steps {
            sh 'python write_file.py testtest123'
            sh 'echo hello world'
          }
        }
        stage('test3') {
          steps {
            sh 'python write_file.py kfajsldfjlsd'
          }
        }
      }
    }
    stage('') {
      steps {
        sh 'cat a.txt'
      }
    }
  }
}