GHOST CMS INSTALLATION
======================

Installation Steps
------------------

#. **Update your system**  

   Ensure your server is up to date:  
   ``$ sudo apt update && sudo apt upgrade -y``

#. **Install Node.js, npm, and Yarn**  

Ghost CMS requires Node.js (LTS version). You may consider looking up Ghost documentatoin to check required version. At the time of publishing this guide, the versions of Nide.js and Ghost CMS are summarized in the table below:
   
  

To install Node.js, npm, and Yarn:  

   ``$ curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash -``  

   ``$ sudo apt install -y nodejs``  

   ``$ sudo npm install -g yarn``

#. **Install Ghost-CLI**  

   Ghost-CLI is a command-line tool for installing and managing Ghost:  

   ``$ sudo npm install -g ghost-cli@latest``

#. **Create a directory for Ghost**  

   Choose a directory (e.g., /var/www/ghost) and set correct permissions:  

   ``$ sudo mkdir -p /var/www/ghost``  

   ``$ sudo chown $USER:$USER /var/www/ghost``  

   ``$ cd /var/www/ghost``

#. **Install Ghost**  

   Run the install command inside your Ghost directory:  

   ``$ ghost install``

#. **Configure Nginx and SSL (optional but recommended)**  

   Ghost-CLI can set up Nginx and SSL for you during installation. Follow the prompts to enable these features.

#. **Start Ghost**  

   Once installed, start Ghost:  

   ``$ ghost start``

#. **Access the Ghost Admin**  

   Open your browser and go to ``http://your-domain.ca/ghost`` to complete the setup via the web interface.