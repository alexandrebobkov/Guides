BACKEND INSTALLATION
====================

Ubuntu Server Installation Steps
--------------------------------

#. **Download Ubuntu Server ISO**

    Download the latest Ubuntu Server LTS ISO from the official Ubuntu website:
    https://ubuntu.com/download/server

#. **Create bootable installation media**

    Use a tool like Rufus (Windows), Etcher (cross-platform), or dd command (Linux/macOS) to create a bootable USB drive with the Ubuntu Server ISO.

#. **Boot from installation media**

    Insert the bootable USB drive and restart your computer. Access the boot menu (usually F12, F2, or Del key) and select the USB drive to boot from.

#. **Select installation language**

    Choose your preferred language for the installation process.

#. **Configure keyboard layout**

    Select your keyboard layout and variant.

#. **Choose installation type**

    Select "Ubuntu Server" for a minimal server installation.

#. **Configure network connections**

    Set up your network interface with either DHCP (automatic) or static IP configuration as needed.

#. **Configure proxy (if needed)**

    Enter proxy information if your network requires it, or leave blank to skip.

#. **Configure Ubuntu archive mirror**

    Use the default mirror or specify a custom one for package downloads.

#. **Configure storage**

    Choose guided storage configuration for automatic partitioning, or manual partitioning for custom disk layout. Confirm the storage configuration.

#. **Set up profile information**

    Enter your name, server name, username, and password for the primary user account.

#. **Enable SSH server**

    Install OpenSSH server for remote access (recommended for server installations).

#. **Select additional software**

    Choose any additional server software you want to install (Docker, etc.) or skip to install later.

#. **Complete installation**

    Wait for the installation to complete, then remove the installation media and reboot the server.

#. **Initial server setup**

    After reboot, log in with your credentials and perform initial updates:
    ``$ sudo apt update && sudo apt upgrade -y``

NodeJS Installation Steps
-------------------------

#. **Install Node.js**

    Install Node.js using the official NodeSource repository:
    ``$ curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -``
    ``$ sudo apt install -y nodejs``

#. **Install npm and Yarn**

    Install npm and Yarn using the official repositories:
    ``$ sudo apt install -y npm``
    ``$ npm install -g yarn``

Ghost CMS Installation Steps
----------------------------

#. **Update your system**

    Ensure your server is up to date:
    ``$ sudo apt update && sudo apt upgrade -y``

#. **Install Node.js, npm, and Yarn**

    Ghost CMS requires Node.js (LTS version). You may consider looking up Ghost documentatoin to check required version. At the time of publishing this guide, the versions of Nide.js and Ghost CMS are summarized in the table below:

+-----------------------------+------------------+
| Node.js Version             | Support Level    |
+=============================+==================+
| 17.x and below              | Unsupported      |
+-----------------------------+------------------+
| 18.x (Node v18 Hydrogen LTS)| Supported        |
+-----------------------------+------------------+
| 19.x                        | Unsupported      |
+-----------------------------+------------------+
| **20.x (Node v20 Iron LTS)**| **Recommended**  |
+-----------------------------+------------------+
| 21.x                        | Unsupported      |
+-----------------------------+------------------+
| **22.x (Node v22 Jod LTS)** | **Supported**    |
+-----------------------------+------------------+
| 23.x and above              | Unsupported      |
+-----------------------------+------------------+

    To install Node.js, npm, and Yarn:

    ``$ curl -sL https://deb.nodesource.com/setup_20.x | sudo -E bash -``

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
