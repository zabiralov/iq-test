IMAGE = "ubuntu/xenial64"
NODES = 6
NETWORK = "192.168.150.1"
NETMASK = "255.255.255.0"
DOMAIN = "example.com"
CPUS = 1
MEMORY = 512
PUBKEY = File.read("#{Dir.home}/.ssh/id_rsa.pub")

Vagrant.configure("2") do |config|

  config.vm.provider "virtualbox" do |vb|
    vb.memory = MEMORY
    vb.cpus = CPUS
  end

  config.vm.provision "copy ssh public key", type: "shell", inline: "echo \"#{PUBKEY}\" >> /home/vagrant/.ssh/authorized_keys"

  (1..NODES).each do |i|
    
    config.vm.define "node0#{i}" do |subconfig|
      subconfig.vm.hostname = "node0#{i}.#{DOMAIN}"
      subconfig.vm.box = IMAGE
      subconfig.vm.network "private_network", ip: "#{NETWORK}#{i}", netmask: NETMASK
    end
  end
end
