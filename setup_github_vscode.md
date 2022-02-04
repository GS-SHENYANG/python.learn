在vscode所在机器上的设置：
    git config --global user.name "username"
    git config --global user.email "email address"

    ssh-keygen -t rsa -C "27382901@qq.com"
    cat ～/.ssh/id_rsa.pub
将公钥复制到github.com账户的setting里ssh key
本地测试
    ssh -T git@ithub.com


