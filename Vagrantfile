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
  