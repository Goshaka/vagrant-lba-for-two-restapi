# vagrant-lba-for-two-restapi#

# Prerequisit:
# VirtualBox — If you don’t already have it installed, you can download from: https://www.virtualbox.org/wiki/Downloads
# Vagrant - https://www.vagrantup.com/downloads.html
# vagrant-lba-for-two-restapi installation package should be download from: https://github.com/Goshaka/vagrant-lba-for-two-restapi
# Install vagrant docker-compose before executing "vagrant up"

```bash
vagrant plugin install vagrant-docker-compose
```


# Project Architicture:
# Vagrant is managing virtual box "centos/7" on the VirtualBox infrastructure.
# On VM installed docker and docker-compose
# Using haproxy docker as LBA
# Using Flask docker as Python application framework.
# Virtual box hostname defined in the local etc/hosts file: 192.168.1.100  docker.restapi.com  # VAGRANT
# Haproxy lba is geting comming request to *:80 and moving them to one of the application flask dockers.

# Environment installation:
# 1. clone git https://github.com/Goshaka/vagrant-lba-for-two-restapi.git
# 2. Go to git project directory
# 3. Run "vagrant up"
# 4. Open "docker.restapi.com" into your internet browser.




# Due to vagrant bug sometime it's imposible to install vagrant-docker-compose plugin from Vagrant file by running "vagrant up"

'''ruby
required_plugins = %w(vagrant-docker-compose )

plugins_to_install = required_plugins.select { |plugin| not Vagrant.has_plugin? plugin }

if not plugins_to_install.empty?
puts "Installing plugins: #{plugins_to_install.join(' ')}"
if system "vagrant plugin install #{plugins_to_install.join(' ')}"
exec "vagrant #{ARGV.join(' ')}"
else
abort "Installation of one or more plugins has failed. Aborting."
end
end

'''



## Usage

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

### To install and run docker-compose, with multiple files, on `vagrant up`

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.provision :docker
  config.vm.provision :docker_compose,
    yml: [
      "/vagrant/docker-compose-base.yml",
      "/vagrant/docker-compose.yml",
      ...
    ],
    run: "always"
end
```

Equivalent to running:

```bash
docker-compose -f [yml-0] -f [yml-1] ... up -d
```

### To install, rebuild and run docker-compose on `vagrant up`

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.provision :docker
  config.vm.provision :docker_compose, yml: "/vagrant/docker-compose.yml", rebuild: true, run: "always"
end
```

Equivalent to running:

```bash
docker-compose -f [yml] rm --force
docker-compose -f [yml] build
docker-compose -f [yml] up -d
```

### To install, rebuild and run docker-compose with options on `vagrant up`

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.provision :docker
  config.vm.provision :docker_compose, yml: "/vagrant/docker-compose.yml", rebuild: true,
    options: "--x-networking", command_options: { rm: "", up: "-d --timeout 20"}, run: "always"
end
```

Equivalent to running:

```bash
docker-compose --x-networking -f [yml] rm
docker-compose --x-networking -f [yml] build
docker-compose --x-networking -f [yml] up -d --timeout 20
```


### Other configs

* `yml` – one or more [Compose files](https://docs.docker.com/compose/compose-file/) (YAML), may be a `String` for a single file, or `Array` for multiple.
* `compose_version` – defaults to `1.8.0`.
* `project_name` – compose will default to naming the project `vagrant`.
* `env` – a `Hash` of environment variables to value that are passed to the `docker-compose` commands, defaults to an empty `Hash`.
* `executable_symlink_path` – the location the executable will be symlinked to, defaults to `/usr/local/bin/docker-compose`.
* `executable_install_path` – the location the executable will be stored, defaults to `<executable_symlink_path>-<compose_version>`, i.e. `/usr/local/bin/docker-compose-1.5.0`.
* `options` - a `String` that's included as the first arguments when calling the docker-compose executable, you can use this to pass arbitrary options/flags to docker-compose, default to `nil`.
* `command_options` - a `Hash` of docker-compose commands to options, you can use this to pass arbitrary options/flags to the docker-compose commands, defaults to: `{ rm: "--force", up: "-d" }`.

## Example

See `example` in the repository for a full working example.
