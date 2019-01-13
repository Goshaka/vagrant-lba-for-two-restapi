# vagrant-lba-for-two-restapi

# Prerequisites:
### VirtualBox - If not installed, you can download from: https://www.virtualbox.org/wiki/Downloads
### Vagrant - https://www.vagrantup.com/downloads.html
### vagrant-lba-for-two-restapi installation package. Download from: https://github.com/Goshaka/vagrant-lba-for-two-restapi
### Due to Vagrant bug, sometimes it is not possible to install vagrant-docker-compose plugin from the Vagrant file by running "vagrant up"
### Vagrant docker-compose must be installed before executing "vagrant up"

```bash
vagrant plugin install vagrant-docker-compose
```
### Example of the Vagrant plugin installation error:
```bash
C:/HashiCorp/Vagrant/embedded/gems/2.1.2/gems/vagrant-2.1.2/bin/vagrant:47:in `[]=': Invalid argument - ruby_setenv(VAGRANT_NO_PLUGINS) (Errno::EINVAL)
        from C:/HashiCorp/Vagrant/embedded/gems/2.1.2/gems/vagrant-2.1.2/bin/vagrant:47:in `block in <main>'
```

# Project Architecture:
### Vagrant is managing virtual box "centos/7" on the VirtualBox infrastructure
### On VM installed docker and docker-compose
### Using haproxy docker as LBA
### Using Flask docker as Python application framework
### Virtual box hostname defined in the local etc/hosts file: 192.168.1.100  docker.restapi.com  # VAGRANT
### Haproxy lba gets a request to *:80 and moving them to one of the application flask dockers

# Environment Installation:
### 1. Clone git https://github.com/Goshaka/vagrant-lba-for-two-restapi.git
### 2. Go to git project directory
### 3. Run "vagrant up"
### 4. From your internet browser,open "docker.restapi.com"


# How to use:
### Open internet browser and copy one of the REST API URLs:
### http://docker.restapi.com/rest1 or  http://docker.restapi.com/rest2


# Test Environment Details:
### OS Windows 10
### Vagrant Installed Version: 2.1.2
### Oracle VM VirtualBox Version 5.2.18 r124319
### Chrome Internet Browser last version

# Environment Health Check:
### Open http://docker.restapi.com

# Environment Test:
### Test Rest Api 1:
### http://docker.restapi.com/rest1
### Test Rest Api 2:
### http://docker.restapi.com/rest2


