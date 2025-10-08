FROM alpine:latest

WORKDIR /home/cyrhades

# Installe le serveur SSH et les outils nécessaires
RUN apk update && \
    apk add openssh && \
    mkdir /var/run/sshd

# Génère les clés SSH
RUN ssh-keygen -A

# Copie le fichier message_ssh.txt depuis le système hôte vers le conteneur
COPY message.txt /etc/motd

COPY ./lfm.py /home/cyrhades/lfm.py

# Crée un utilisateur "cyrhades" avec mot de passe "secret"
RUN adduser -D cyrhades && \
    echo "cyrhades:secret" | chpasswd

# Autorise la connexion SSH pour cet utilisateur
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Expose le port SSH (par défaut, le port 22)
EXPOSE 22

# Démarre le service SSH au lancement du conteneur
CMD ["/usr/sbin/sshd", "-D"]