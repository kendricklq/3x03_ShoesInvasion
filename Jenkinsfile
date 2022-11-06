pipeline {
	agent any
	stages {
		stage('Build') {
			steps {
				echo 'Building the application ...'
				// sh 'pip install -r requirements.txt'
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
                //echo 'Testing the application ...'
				echo 'JUnit Test ...'
				sh 'ls'
				// sh 'python manage.py test'
				/*
				dir("${test_dir}"){
					sh "python manage.py test"
				} */
				
            }
	}
	}	
	post {
		success {
			dependencyCheckPublisher pattern: 'dependency-check-report.xml'
			// junit '**/target/*.xml'
		}
	}
}
