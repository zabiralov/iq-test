IMAGE = "ubuntu/xenial64"
DOMAIN = "example.com"
PUBKEY = File.read("#{Dir.home}/.ssh/id_rsa.pub")

MINIO_NODES = 6
MINIO_NETWORK = "192.168.150.1"
MINIO_NETMASK = "255.255.255.0"
MINIO_CPUS = 1
MINIO_MEMORY = 512

NGINX_NODES = 3
NGINX_NETWORK = "192.168.150.2"
NGINX_NETMASK = "255.255.255.0"
NGINX_CPUS = 1
NGINX_MEMORY = 256


Vagrant.configure("2") do |config|
  
  config.vm.provider "virtualbox" do |vb|
    vb.memory = MINIO_MEMORY
    vb.cpus = MINIO_CPUS
  end

  (1..MINIO_NODES).each do |i|
    
    config.vm.define "s3-node-#{i}" do |subconfig|
      subconfig.vm.hostname = "s3-node-#{i}.#{DOMAIN}"
      subconfig.vm.box = IMAGE
      subconfig.vm.network "private_network", ip: "#{MINIO_NETWORK}#{i}", netmask: MINIO_NETMASK
    end
  end

  config.vm.provider "virtualbox" do |vb|
    vb.memory = NGINX_MEMORY
    vb.cpus = NGINX_CPUS
  end

  (1..NGINX_NODES).each do |i|
    
    config.vm.define "lb-node-#{i}" do |subconfig|
      subconfig.vm.hostname = "lb-node-#{i}.#{DOMAIN}"
      subconfig.vm.box = IMAGE
      subconfig.vm.network "private_network", ip: "#{NGINX_NETWORK}#{i}", netmask: NGINX_NETMASK
    end
  end


  config.vm.provision "copy ssh public key", type: "shell", inline: "echo \"#{PUBKEY}\" >> /home/vagrant/.ssh/authorized_keys"

end
