# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.synced_folder "./data", "/home/vagrant/data"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "6144"
    vb.cpus = "2"
  end

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y git curl htop build-essential gdb valgrind
    sudo apt-get install -y software-properties-common
    # Install JDK 8
    sudo add-apt-repository ppa:webupd8team/java
    sudo apt-get update
    echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-set-selections
    echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-selections
    sudo apt-get install -y oracle-java8-installer
    # Add Bazel distribution
    echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
    curl https://storage.googleapis.com/bazel-apt/doc/apt-key.pub.gpg | sudo apt-key add -
    # Install Bazel
    sudo apt-get update
    sudo apt-get install -y bazel
    # Install TensorFlow
    cd /home/vagrant/data
    git clone https://github.com/tensorflow/tensorflow.git
    # cd tensorflow
    # ./configure
    # cd /home/vagrant
    sudo apt-get -y install python-pip python-dev
    export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0rc1-cp27-none-linux_x86_64.whl
    sudo pip install --upgrade $TF_BINARY_URL
  SHELL
end
