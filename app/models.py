"""
from app import db


class YogurtData(db.Model):
    __tablename__ = "YogurtData"
    features_id = db.Column(db.Integer, primary_key=True)
    streptococcus_initial = db.Column(db.Float, index=True, nullable=False)
    lactobacillus_initial = db.Column(db.Float, index=True, nullable=False)
    ideal_temperature = db.Column(db.Float, index=True, nullable=False)
    minimum_milk_proteins = db.Column(db.Float, index=True, nullable=False)
    titratable_acidity = db.Column(db.Float, index=True, nullable=False)
    ph_milk_sour = db.Column(db.Float, index=True, nullable=False)
    fat_milk_over_100mg = db.Column(db.Float, index=True, nullable=False)
    quality_product = db.Column(db.String(20), index=True, nullable=False)
    streptococcus_final = db.Column(db.Float, index=True, nullable=False)
    lactobacillus_final = db.Column(db.Float, index=True, nullable=False)


db.create_all()
"""
