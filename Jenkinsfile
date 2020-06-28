node{
    parameters {
        string(name: 'imagename', defaultValue: 'python_flask_app', description: 'def name to build image')
        string(name: 'version', defaultValue: 'v1', description: 'def version to build image')

    }
    stage('checkout_GitLab'){
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'GitLab', url: 'https://github.com/praveensatti/jenkins_workdir.git']]])
    }
    stage('Dcoekr build'){
        def testImage = "docker build -t  praveensatti/${imagename}:${version} ."
        sh(testImage)
      // def customImage = docker.build("$(imagename)", "Dockerfile")
    }
    stage("Push_image"){
        def comm="docker push praveensatti/${imagename}:${version}"
        sh(comm)
    }
    stage("Removing_local_image"){
        def ot="docker rmi praveensatti/${imagename}:${version}"
        sh(ot)
    }
}