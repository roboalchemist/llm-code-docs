# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/pre-installation/unix.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/pre-installation/unix.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/pre-installation/unix.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/pre-installation/unix.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/pre-installation/unix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/pre-installation/unix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/pre-installation/unix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/pre-installation/unix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/pre-installation/unix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/pre-installation/unix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/pre-installation/unix.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/pre-installation/unix.md

# On Unix-based systems

SonarQube Server should not be run as root on Unix-based systems. It is recommended to create a dedicated user account for SonarQube Server (It is highly recommended for a ZIP installation).

For a ZIP installation, proceed as follows:

1. Create a dedicated user account for SonarQube Server. Note that:
   * This user does not need to have a login shell.
   * This user does not need to have a password.
   * We recommend that the user’s home directory be the same as the installation directory (recommended: `/opt/sonarqube)`.
2. Grant to this user account the read/write/execute (or owner) privileges on the installation directory.
