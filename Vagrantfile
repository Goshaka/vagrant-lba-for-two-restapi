Vagrant.configure("2") do |config|
  config.vm.hostname = "docker.restapi.com"
  config.vm.box = "centos/7"
  config.vm.network "private_network", ip: "192.168.1.100"
  
  config.vm.synced_folder './', '/vagrant',  type: "rsync"
 
  config.vm.provider "virtualbox" do |v|
    v.name = "docker1"
    v.memory = 4096
    v.cpus = 2
  end
  config.vm.provision :shell do |shell|
    shell.inline = <<-SHELL
      sudo yum -y install epel-release
      sudo yum -y install python-pip
      sudo pip install --upgrade pip
      sudo pip install six==1.4
      sudo pip install docker-py
      sudo ls -artl /vagrant/
	  sudo cd /vagrant/
	  sudo pwd
	 SHELL
  end
 
config.vm.provision :docker
config.vm.provision :docker_compose, yml: ["/vagrant/docker/docker-compose.yml"]

end
  