FROM node:18-alpine

WORKDIR /app

COPY . .

WORKDIR /app/client

RUN npm i 

EXPOSE 3000
CMD ["npm","run","start" ]
