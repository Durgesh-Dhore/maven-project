pipeline
{
    agent any
    stages
    {
        // CI part
        stage ('scm checkout')
        {steps { git 'https://github.com/kumargaurav039/maven-project.git' }}

        stage ('validate')
        {steps { withMaven(globalMavenSettingsConfig: '', jdk: 'JAVA_HOME', maven: 'MVN_HOME', mavenSettingsConfig: '', traceability: true) {
    sh 'mvn validate'
}
        }}
        stage ('package')
        {steps { withMaven(globalMavenSettingsConfig: '', jdk: 'JAVA_HOME', maven: 'MVN_HOME', mavenSettingsConfig: '', traceability: true) {
    sh 'mvn package'
}
        }}
        //CD part
        stage ('deploy the code on tomcat')
        {steps {
            sshagent(['DEVCICD']) {
                sh 'scp -o StrictHostKeyChecking=no webapp/target/webapp.war ec2-user@172.31.14.93:/usr/share/tomcat/webapps'
            }
        }}
    }
}
