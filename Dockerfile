FROM 5hojib/aeon:dev

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["bash", "start.sh"]
