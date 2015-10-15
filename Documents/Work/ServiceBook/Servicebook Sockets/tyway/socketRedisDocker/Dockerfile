# Set the base image to Ubuntu
FROM    ubuntu

# File Author / Maintainer
MAINTAINER Mitchell Tieleman / ServiceBook

# Install Node.js and other dependencies
RUN apt-get update && \
    apt-get -y install curl && \
    curl -sL https://deb.nodesource.com/setup | sudo bash - && \
    apt-get -y install python build-essential nodejs

# Install nodemon
RUN npm install -g nodemon

# Provides cached layer for node_modules
ADD package.json /tmp/package.json
RUN cd /tmp && npm install
RUN npm install redis --save
RUN mkdir -p /src && cp -a /tmp/node_modules /src/

# Define working directory
WORKDIR /src
ADD . /src

# Expose port
#EXPOSE  80

# Run app using nodemon
#CMD ["node", "/src/server.js"]
