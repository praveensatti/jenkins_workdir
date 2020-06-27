node{
    stage('checkout_GitLab'){
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'GitLab', url: 'https://github.com/praveensatti/jenkins_workdir.git']]])
    }
    stage("bash_file"){
        sh label: '', script: 'sh first_script.sh'
    }
    stage("Play_Run"){
        sh "echo \"Helow world\" "
        //sh "#!/bin/bash \n"  + "ansible-playbook jplay.yml -i jen_inventory --remote-user praveensatti"
        // sh $ansible
        //ansiblePlaybook colorized: true, credentialsId: 'hostlogin', disableHostKeyChecking: true, installation: 'ansible', inventory: 'jen_inventory', playbook: 'jplay.yml'
    }
    stage('MVN'){
        def var1 = 'cd && pwd'
        sh (var1)
        
    }
}