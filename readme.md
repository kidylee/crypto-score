
Start mysql database
```shell
docker-compose up -d
```


Migrate database schema.
```shell
cd python
poetry shell
alembic upgrade head
```

Load data from data.csv file
```
cd src
python app.py
```


start node server
```shell
cd ../../node
npm install
npm run start

curl http://localhost:3000/scores?address=0x87bd1b4fe57985f126ea8b3c12eeabcc212080a7&walletType=Fintone
```