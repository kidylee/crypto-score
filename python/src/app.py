import csv
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from model import ReputationScore

engine = create_engine("mysql+mysqlconnector://example_user:example_user_password@localhost:3306/example_db")


def read_csv_file(file_path: str):
    with open(file_path, "r") as f:
        records = csv.reader(f)
        for record in records:
            yield record


def save_reputation_scores(records, session):
    for record in records:
        address, wallet_type, score = record
        rs = ReputationScore(address=address, wallet_type=wallet_type, score=score)
        session.add(rs)
    session.commit()


if __name__ == '__main__':
    scores = read_csv_file("../../data.csv")
    with Session(engine) as session:
        save_reputation_scores(scores, session)
