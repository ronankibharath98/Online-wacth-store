from sqlalchemy import create_engine, text
import os

db_connection_string = "mysql+pymysql://mjp88b9yjlhu6akt13yp:pscale_pw_43RGrAOMlHYnONGxORJfTahDbZc8E3gP6juCf8DDt38@aws.connect.psdb.cloud/kalaonlinestore?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from watch"))

  result_dicts = []
  for row in result.all():
    result_dicts.append(row._asdict())
  print(result_dicts)


def load_products_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from watch"))
    products = []
    for row in result.all():
      products.append(row._asdict())
    return products
