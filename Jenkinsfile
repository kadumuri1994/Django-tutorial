node ('master') {

    def PWD = pwd();
    def BRANCH_NAME = "master"

    stage ('Pull the latest code base') {
        checkout([$class: 'GitSCM', branches: [[name: "master"]], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: "kadumuri05", url: "https://github.com/kadumuri1994/Django-tutorial.git/"]]])
    }

}
