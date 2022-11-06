pipeline {
	agent any
	stages {
		stage('Build') {
			steps {
				echo 'Building the application ...'
			}
		}

		stage('OWASP DependencyCheck') {
			steps {
				echo 'OWASP DependencyCheck ...'
				//Disable yarn audit as not in used
				dependencyCheck additionalArguments: '--format HTML --format XML --disableYarnAudit', odcInstallation: 'Default'
			}
		} 

		stage('Test') {
	agent {
        docker { image 'python:3.9' }
    }

            steps {
				echo 'Django Test ...'
				sh 'python manage.py test'
            }
	}
	}	
	post {
		success {
			dependencyCheckPublisher pattern: 'dependency-check-report.xml'
		}
	}
}


