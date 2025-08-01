pipeline
{
    agent any
    stages
    {
        // CI part
        stage ('scm checkout')
        {steps { git 'https://github.com/Durgesh-Dhore/maven-project.git' }}

        stage ('validate')
        {steps { withMaven(globalMavenSettingsConfig: '', jdk: 'JAVA_HOME', maven: 'MVN_HOME', mavenSettingsConfig: '', traceability: true) {
    sh 'mvn validate'
}
        }}
        stage ('package')
        {steps { withMaven(globalMavenSettingsConfig: '', jdk: 'JAVA_HOME', maven: 'MVN_HOME', mavenSettingsConfig: '', traceability: true) {
    sh 'mvn clean package'
}
        }}
        //CD part
        stage ('deploy the code on tomcat')
        {steps {
            sshagent(['DEVCICD']) {
                sh 'scp -o StrictHostKeyChecking=no webapp/target/webapp.war ec2-user@172.31.14.93:/home/ec2-user/'
            }
            
        }}
    }
}


