pipeline
{
    agent any
    stages
    {
        stage ('scm checkout')
        {steps { git 'https://github.com/kumargaurav039/maven-project.git' }}

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
    }
}
