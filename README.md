# vagrant-lba-for-two-restapi#

# Prerequisit:
### VirtualBox — If you don’t already have it installed, you can download from: https://www.virtualbox.org/wiki/Downloads
### Vagrant - https://www.vagrantup.com/downloads.html
### vagrant-lba-for-two-restapi installation package should be download from: https://github.com/Goshaka/vagrant-lba-for-two-restapi
# Install vagrant docker-compose before executing "vagrant up"

```bash
vagrant plugin install vagrant-docker-compose
```


# Project Architicture:
### Vagrant is managing virtual box "centos/7" on the VirtualBox infrastructure.
### On VM installed docker and docker-compose
### Using haproxy docker as LBA
### Using Flask docker as Python application framework.
### Virtual box hostname defined in the local etc/hosts file: 192.168.1.100  docker.restapi.com  # VAGRANT
### Haproxy lba is geting comming request to *:80 and moving them to one of the application flask dockers.

# Environment installation:
### 1. clone git https://github.com/Goshaka/vagrant-lba-for-two-restapi.git
### 2. Go to git project directory
### 3. Run "vagrant up"
### 4. Open "docker.restapi.com" into your internet browser.


# Due to vagrant bug sometime it's imposible to install vagrant-docker-compose plugin from Vagrant file by running "vagrant up"


# Usage

### To install and run docker-compose on `vagrant up`

```ruby
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
```

Equivalent to running:

```bash
docker-compose -f [yml] up -d
```

# Test Environment Details:
### OS Windows 10
### Vagrant Installed Version: 2.1.2
### Oracle VM VirtualBox Version 5.2.18 r124319
### Chrome Internet Browser last version

# Environment health check:
### Open http://docker.restapi.com

# Environment test:
### Test Rest Api 1:
### http://docker.restapi.com/rest1
### Test Rest Api 2:
### http://docker.restapi.com/rest2


