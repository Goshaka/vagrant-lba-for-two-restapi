# vagrant-lba-for-two-restapi#

# Prerequisit:
### VirtualBox — If you don’t already have it installed, you can download from: https://www.virtualbox.org/wiki/Downloads
### Vagrant - https://www.vagrantup.com/downloads.html
### vagrant-lba-for-two-restapi installation package should be download from: https://github.com/Goshaka/vagrant-lba-for-two-restapi
# Install vagrant docker-compose before executing "vagrant up"
### Due to vagrant bug sometime it's imposible to install vagrant-docker-compose plugin from Vagrant file by running "vagrant up"

```bash
vagrant plugin install vagrant-docker-compose
```
### Example of the vagrant plugin installation error:

```bash
C:/HashiCorp/Vagrant/embedded/gems/2.1.2/gems/vagrant-2.1.2/bin/vagrant:47:in `[]=': Invalid argument - ruby_setenv(VAGRANT_NO_PLUGINS) (Errno::EINVAL)
        from C:/HashiCorp/Vagrant/embedded/gems/2.1.2/gems/vagrant-2.1.2/bin/vagrant:47:in `block in <main>'
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


# Usage:

### To install and run docker-compose on `vagrant up`
### Open internet browser and put one of the REST API URL:
### http://docker.restapi.com/rest1 or  http://docker.restapi.com/rest2


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


