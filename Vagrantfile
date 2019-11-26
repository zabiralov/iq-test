IMAGE = "ubuntu/xenial64"
NODES = 6
NETWORK = "192.168.150."
NETMASK = "255.255.255.0"
DOMAIN = "example.com"
CPUS = 1
MEMORY = 512

Vagrant.configure("2") do |config|

  config.vm.provider "virtualbox" do |vb|
    vb.memory = MEMORY
    vb.cpus = CPUS
  end

  (1..NODES).each do |i|
    
    config.vm.define "node0#{i}" do |subconfig|
      subconfig.vm.hostname = "node0#{i}.#{DOMAIN}"
      subconfig.vm.box = IMAGE
      subconfig.vm.network "private_network", ip: "#{NETWORK}#{i}", netmask: NETMASK
    end
  end
end
